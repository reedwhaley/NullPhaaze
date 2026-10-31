# The exporter stages this game's seed edits and external image-tool work around the
# preserved input. Keep source verification, resource readback and final publication as
# separate gates. Boundary names here: CorruptionGameExportParams, CorruptionOutputFormats,
# file_sha, validate_patch_data, CorruptionGameExporter.
"""NullPhaaze modification, 2026-10-16: source-backend disc export (GPL-3.0-or-later).
Inputs are read-only; successful exports remove their owned working directory.
"""
from __future__ import annotations
import dataclasses
import errno
import hashlib
import json
import logging
import os
from importlib.metadata import version as distribution_version
from pathlib import Path
import shutil
import subprocess
import tempfile
from nullphaze_core.storage import available_bytes
from enum import Enum
from randovania.exporter.game_exporter import GameExporter, GameExportParams
from randovania.games.prime3.exporter.toolchain import extract_prime3_disc_image, resolve_prime3_toolchain
from randovania.patching.patchers.exceptions import UnableToExportError


def _require_free_space(directory, required):
    free = available_bytes(directory)
    if free < required:
        gib = 1024**3
        raise UnableToExportError(
            f'Not enough free space on the drive containing {directory}. '
            f'This export needs at least {required/gib:.1f} GiB free; {free/gib:.1f} GiB is available. '
            'Choose an output folder on a drive with more space or free space before retrying. '
            'Failed exports retain .nullphaze-export-* working folders beside the output. '
            'Review those folders before removing any you no longer need.')


@dataclasses.dataclass(frozen=True)
class CorruptionGameExportParams(GameExportParams):
    input_path: Path
    output_path: Path
    output_format: CorruptionOutputFormats
    mp3_update: bool = False
    model_cache_path: Path | None = None
    import_model_games: frozenset[str] = frozenset()


class CorruptionOutputFormats(Enum):
    WBFS = 'wbfs'
    ISO = 'iso'


def file_sha(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()



VERIFIED_INPUT_SHA256 = '3621e6522f99e8c6755353530f2d571489b805bee85c054a96ac52c7e32ee71e'
# User-reported image that exports in stock CDV. Payload compatibility is still
# enforced independently by nullphaze_core's extracted-file fingerprints.
PROVISIONAL_INPUT_SHA1 = 'c8f61de724c8928c6b458b0de30dbe6e402d4889'
PROVISIONAL_INPUT_PROFILES = {
    PROVISIONAL_INPUT_SHA1: 'stock-cdv-reported-usa-rev0',
    # User-reported image, not independently verified against retail payloads.
    # CRC32: b8fe9c21; MD5: b8c81edf28bde8740c82bed0f5dde7a6
    '9dcaa2db1acb8ab965956887bbab652a80b1933c': 'user-reported-usa-rev0-20261024',
}


def _input_profile(source, sha256):
    if sha256 == VERIFIED_INPUT_SHA256:
        return {'id': 'verified-usa-rev0', 'provisional': False}
    with source.open('rb') as stream:
        sha1 = hashlib.file_digest(stream, 'sha1').hexdigest()
    if sha1 in PROVISIONAL_INPUT_PROFILES:
        return {'id': PROVISIONAL_INPUT_PROFILES[sha1], 'provisional': True, 'sha1': sha1}
    raise ValueError('Input image is not on the USA revision 0 allowed list. '
                     f'SHA-256: {sha256}; SHA-1: {sha1}')


def _cleanup_export_work(work, output_parent):
    # Delete only this export's directory, never a user-selected path or a link.
    resolved = work.resolve(strict=True)
    if (work.is_symlink() or work.is_junction()
            or resolved.parent != output_parent.resolve()
            or not resolved.name.startswith('.nullphaze-export-')):
        raise ValueError('Refusing cleanup outside the owned export directory')
    shutil.rmtree(resolved)



def _remove_attract_videos(extracted):
    # Match CDV's empty placeholders, generated from source rather than shipped assets.
    removed = {}
    for name in ('attract01.thp', 'Attract02.thp'):
        path = extracted/'DATA/files/Video/FrontEnd'/name
        if path.is_symlink() or not path.resolve(strict=True).is_relative_to(extracted.resolve()):
            raise ValueError('Attract video must be inside the owned extraction')
        removed[name] = path.stat().st_size
        path.write_bytes(b'')
    return removed


def validate_patch_data(patch_data):
    from randovania.games.prime3.exporter.nothing_pickups import nothing_indices
    nothing_indices(patch_data)
    if not isinstance(patch_data.get('warp_to_space', False), bool):
        raise ValueError('Warp to Space must be enabled or disabled')
    for option in ('fast_ziplines', 'seed_hints'):
        if type(patch_data.get(option, False)) is not bool:
            raise ValueError(f'{option} must be enabled or disabled')
    if patch_data.get('seed_hints', False):
        from randovania.games.prime3.exporter.seed_hints import validate_data
        validate_data(patch_data.get('hint_data'))
    if 'item_location_hints' in patch_data:
        from randovania.games.prime3.exporter.item_location_hints import validate_data as validate_item_hints
        validate_item_hints(patch_data['item_location_hints'])
    if 'hyper_item_hints' in patch_data:
        from randovania.games.prime3.exporter.hyper_hints import validate_data as validate_hyper_hints
        validate_hyper_hints(patch_data['hyper_item_hints'])
    from randovania.games.prime3.layout.hint_mode import validate_hint_settings
    validate_hint_settings(patch_data)
    if patch_data.get('menu_identity') is not None:
        from randovania.games.prime3.exporter.main_menu import validate_metadata
        validate_metadata(patch_data['menu_identity'])
    if patch_data.get('mp3_update') or patch_data.get('disable_deflicker'):
        raise ValueError('MP3Update and its deflicker patch are excluded from NullPhaaze. Disable both in the preset.')
    if patch_data.get('multiworld') is not None:
        from nullphaze_network.prime3_lua_service.runtime_export import preflight
        preflight(patch_data['multiworld'])
    if patch_data.get('multiworld') is not None or 'pickup_scan_text' in patch_data:
        from randovania.games.prime3.exporter.pickup_scans import scan_rows
        scan_rows(patch_data)


class CorruptionGameExporter(GameExporter):
    _busy = False

    @property
    def can_start_new_export(self):
        return not self._busy

    @property
    def export_can_be_aborted(self):
        return False

    def export_params_type(self):
        return CorruptionGameExportParams

    def _do_export_game(self, patch_data, export_params, progress_update):
        if self._busy:
            raise RuntimeError('An export is already running.')
        if not isinstance(export_params, CorruptionGameExportParams):
            raise TypeError('Expected CorruptionGameExportParams')
        validate_patch_data(patch_data)
        if export_params.mp3_update:
            raise ValueError('MP3Update is excluded from NullPhaaze.')
        source, output = export_params.input_path.resolve(), export_params.output_path.absolute()
        if output.exists() or output.is_symlink():
            raise FileExistsError(f'Output already exists: {output}')
        if output.suffix.lower() != '.'+export_params.output_format.value:
            raise ValueError('Output extension must match the selected format.')
        if not output.parent.is_dir():
            raise ValueError('Choose an existing output directory.')
        with source.open('rb') as stream:
            header = stream.read(8)
        if len(header) != 8 or header[:6] != b'RM3E01' or header[7] != 0:
            raise ValueError('This backend supports Metroid Prime 3 USA revision 0 (RM3E01).')
        # Extraction, separate patched PAKs and the rebuilt image coexist. Reserve
        # three input-image sizes plus headroom, for both ISO and WBFS exports.
        copies = 4 if patch_data.get('multiworld_models') and any(
            row['game'] in export_params.import_model_games for row in patch_data['multiworld_models']) else 3
        if patch_data.get('multiworld') is not None:
            copies = max(copies, 5)  # callback/service staging plus final image roundtrip
        _require_free_space(output.parent, copies*source.stat().st_size + 512*1024**2)
        toolchain = resolve_prime3_toolchain()
        self._busy = True
        work = None
        receipt = {}
        try:
            work = Path(tempfile.mkdtemp(prefix='.nullphaze-export-', dir=output.parent))
            receipt = {'completed': False, 'input': str(source), 'output': str(output), 'patchData': patch_data,
                       'backend': 'nullphaze_core_rds',
                       'rdsVersion': distribution_version('retro-data-structures'),
                       'launcherSha256': file_sha(toolchain.randomizer_command[0]),
                       'codecSha256': file_sha(toolchain.lzokay_library) if toolchain.lzokay_library else None, 'witSha256': file_sha(toolchain.wit_command[0]),
                       'mp3UpdateExcluded': True, 'gameplayVerified': False}
            (work/'receipt.json').write_text(json.dumps(receipt, indent=2))
            progress_update('Checking source image...', 0.01)
            receipt['inputSha256'] = file_sha(source)
            receipt['inputProfile'] = _input_profile(source, receipt['inputSha256'])
            extracted, patched = work/'extracted', work/'patched'
            extracted.mkdir()
            extract_prime3_disc_image(toolchain, source, extracted, progress_update)
            if patch_data.get('seed_hints', False) and 'hyper_item_hints' in patch_data:
                from randovania.games.prime3.exporter.hint_logbook import capture_originals
                receipt['hintRoomPreimages'] = capture_originals(
                    extracted/'DATA/files', work/'hint-originals')
            location_profile = None
            if patch_data.get('multiworld') is not None:
                from nullphaze_network.prime3_lua_service.location import extract_profile
                location_profile = extract_profile((extracted/'DATA/sys/main.dol').read_bytes(),
                                                   (extracted/'DATA/files/Worlds.pak').read_bytes())
            progress_update('Removing attract videos...', 0.32)
            receipt['attractVideoBytesRemoved'] = _remove_attract_videos(extracted)
            progress_update('Patching extracted game files...', 0.35)
            _run_process(_build_randomizer_command(toolchain, patch_data, extracted/'DATA/files', patched),
                         env=toolchain.randomizer_environment, log=work/'patcher')
            files = sorted(patched.iterdir())
            if len(files) != 11 or any(not path.is_file() for path in files):
                raise ValueError('Patcher did not produce the expected eleven output files.')
            receipt['patchedFiles'] = {path.name: file_sha(path) for path in files}
            for path in files:
                shutil.copyfile(path, extracted/'DATA/files'/path.name)
            network_templates = None
            if patch_data.get('multiworld') is not None:
                # The native audio template is in an Olympus room. Capture only
                # its required actors/streams before removing that unused world.
                from nullphaze_network.prime3_lua_service.multiworld_presentation import read_templates
                network_templates = read_templates(extracted/'DATA/files')
            receipt['olympusAssetsRetained'] = True
            if patch_data.get('warp_to_space', False):
                from randovania.games.prime3.exporter.warp_to_space import install
                receipt['warpToSpace'] = install(extracted/'DATA/files', work/'warp-to-space')
            if patch_data.get('fast_ziplines', False):
                from randovania.games.prime3.exporter.fast_ziplines import install as install_ziplines
                receipt['fastZiplines'] = install_ziplines(extracted/'DATA/files',work/'fast-ziplines')
                for name, path in receipt['fastZiplines']['archives'].items():
                    shutil.copyfile(path,extracted/'DATA/files'/name)
            from randovania.games.prime3.exporter.room_fixes import install as install_room_fixes
            receipt['roomFixes'] = install_room_fixes(extracted/'DATA/files',work/'room-fixes')
            for name,path in receipt['roomFixes']['archives'].items():
                shutil.copyfile(path,extracted/'DATA/files'/name)
            if patch_data.get('multiworld') is not None:
                progress_update('Applying recipient-specific pickup models...', 0.62)
                receipt['multiworldModels'] = _apply_multiworld_models(
                    patch_data, export_params, extracted/'DATA/files', work/'models')
                from nullphaze_network.prime3_lua_service.runtime_export import install
                receipt['multiworldRuntime'] = install(
                    extracted/'DATA', work/'network-addon', patch_data['multiworld'],
                    lambda text, fraction: progress_update(text, 0.63 + 0.06*fraction),
                    location_profile=location_profile, templates=network_templates)
                from randovania.games.prime3.exporter.wc24_error_filter import install as install_wc24_filter
                receipt['wc24ErrorFilter'] = install_wc24_filter(extracted/'DATA')
            receipt['nothingModels'] = _apply_nothing_models(
                patch_data, extracted/'DATA/files', work/'nothing-models')
            from randovania.games.prime3.exporter.pickup_scans import install as install_pickup_scans
            receipt['pickupScans'] = install_pickup_scans(
                extracted/'DATA/files', work/'pickup-scans', patch_data)
            for name, path in receipt['pickupScans']['archives'].items():
                shutil.copyfile(path, extracted/'DATA/files'/name)
            if 'item_location_hints' in patch_data and not patch_data.get('seed_hints',False):
                from randovania.games.prime3.exporter.item_location_hints import install as install_item_hints
                receipt['itemLocationHints'] = install_item_hints(
                    extracted/'DATA/files',work/'item-location-hints',patch_data['item_location_hints'])
                for name,path in receipt['itemLocationHints']['archives'].items():
                    shutil.copyfile(path,extracted/'DATA/files'/name)
            if patch_data.get('seed_hints', False):
                from randovania.games.prime3.exporter.seed_hints import install as install_hints
                receipt['seedHints'] = install_hints(extracted/'DATA/files',work/'seed-hints',patch_data['hint_data'])
                for name, path in receipt['seedHints']['archives'].items():
                    shutil.copyfile(path,extracted/'DATA/files'/name)
                if 'hyper_item_hints' in patch_data:
                    from randovania.games.prime3.exporter.hyper_hints import install as install_hyper_hints
                    receipt['hyperItemHints'] = install_hyper_hints(
                        extracted/'DATA/files', work/'hyper-hints', patch_data['hyper_item_hints'])
                    for name,path in receipt['hyperItemHints']['archives'].items():
                        shutil.copyfile(path,extracted/'DATA/files'/name)
                    from randovania.games.prime3.exporter.hint_logbook import install as install_hint_logbook
                    from randovania.games.prime3.layout.hint_mode import enabled_hint_keys
                    enabled = enabled_hint_keys(patch_data)
                    if enabled:
                        receipt['hintLogbook'] = install_hint_logbook(
                            extracted/'DATA/files', work/'hint-logbook', work/'hint-originals',
                            **({'enabled': enabled} if 'hint_settings' in patch_data else {}))
                        for name,path in receipt['hintLogbook']['archives'].items():
                            shutil.copyfile(path,extracted/'DATA/files'/name)
            if patch_data.get('menu_identity') is not None:
                from randovania.games.prime3.exporter.main_menu import patch_archive
                menu_work = work/'main-menu'
                menu_work.mkdir()
                receipt['mainMenu'] = patch_archive(
                    extracted/'DATA/files/GuiDVD.pak', menu_work/'GuiDVD.pak', patch_data['menu_identity'])
                shutil.copyfile(menu_work/'GuiDVD.pak', extracted/'DATA/files/GuiDVD.pak')
            from randovania.games.prime3.exporter.full_map import install as install_full_map
            receipt['fullMap'] = install_full_map(extracted/'DATA/files', work/'full-map')
            for name, path in receipt['fullMap']['archives'].items():
                shutil.copyfile(path, extracted/'DATA/files'/name)
            from randovania.games.prime3.exporter.loading_recap import install as skip_loading_recap
            receipt['loadingRecap'] = skip_loading_recap(extracted/'DATA')
            from nullphaze_core.pak_compaction import compact
            compacted = work/'compact-paks'
            compacted.mkdir()
            receipt['pakPayloadReduction'] = []
            for number in (1,3,4,5,7):
                name = f'Metroid{number}.pak'
                result = compact(extracted/'DATA/files'/name, compacted/name)
                receipt['pakPayloadReduction'].append(result)
                shutil.copyfile(compacted/name, extracted/'DATA/files'/name)
            progress_update('Building '+export_params.output_format.value.upper()+'...', 0.7)
            _require_free_space(work, source.stat().st_size + 256*1024**2)
            staged = work/('image.'+export_params.output_format.value)
            params = dataclasses.replace(export_params, output_path=staged)
            _run_process(_build_wit_command(toolchain, extracted/'DATA', params), log=work/'wit')
            if not staged.is_file() or staged.stat().st_size == 0:
                raise ValueError('WIT produced no image.')
            if list(work.glob(staged.name+'.*')):
                raise ValueError('Unexpected split image; refusing to publish an incomplete image.')
            progress_update('Verifying rebuilt image...', 0.9)
            _run_process((*toolchain.wit_command, 'VERIFY', str(staged)), log=work/'wit-verify')
            if patch_data.get('multiworld') is not None:
                from nullphaze_network.prime3_lua_service.runtime_export import verify_image
                receipt['multiworldRoundtrip'] = verify_image(
                    staged, extracted/'DATA', work/'roundtrip', toolchain, progress_update)
            receipt['outputSha256'] = file_sha(staged)
            receipt['outputBytes'] = staged.stat().st_size
            receipt['inputUnchanged'] = file_sha(source) == receipt['inputSha256']
            if not receipt['inputUnchanged']:
                raise ValueError('Source image changed during export.')
            # Same-volume publication fails if destination exists; unlinking the staging
            # image during cleanup preserves the published hard link.
            os.link(staged, output)
            receipt['completed'] = True
            progress_update('Removing temporary export files...', 0.98)
            try:
                _cleanup_export_work(work, output.parent)
            except (OSError, ValueError) as cleanup_error:
                receipt['cleanupError'] = str(cleanup_error)
                logging.warning('Export succeeded, but working files could not be removed: %s', work,
                                exc_info=True)
                progress_update(f'Export complete. Could not remove working files: {work}', 1.0)
            else:
                progress_update('Export complete', 1.0)
        except Exception as error:
            if isinstance(error, OSError) and error.errno == errno.ENOSPC:
                error = UnableToExportError(
                    f'The output drive ran out of space. Free space or choose another drive and retry. '
                    f'Working files and diagnostics are retained in {work}.')
            receipt['error'] = str(error)
            raise error
        finally:
            self._busy = False
            # Keep the receipt available after successful staging cleanup too.
            self.last_receipt = dict(receipt)
            if work is not None and work.exists():
                try:
                    (work/'receipt.json').write_text(json.dumps(receipt, indent=2)+'\n')
                except OSError:
                    logging.exception('Could not update export receipt in %s', work)


def _apply_nothing_models(patch_data, source, output):
    from randovania.games.prime3.exporter.nothing_pickups import install
    report = install(source, output, patch_data)
    for name, expected in report['archives'].items():
        if file_sha(output/name) != expected:
            raise ValueError('Nothing model archive changed during export staging')
        shutil.copyfile(output/name, source/name)
    return report


def _optional_flag(flag, enabled):
    return (flag,) if enabled else ()


def _apply_multiworld_models(patch_data, export_params, source, output):
    from nullphaze_network.prime3_lua_service.multiworld_models import patch_archives
    from randovania.games.prime3.exporter.models import model_plan

    plan = model_plan(patch_data['multiworld'])
    if patch_data.get('multiworld_models', plan) != plan:
        raise ValueError('Pickup visual plan does not match the recipient-aware seed')
    if any(row['game'] in export_params.import_model_games for row in plan) and export_params.model_cache_path is None:
        raise ValueError('A local validated Corruption model cache is required for foreign pickups')
    report = patch_archives(source, output, plan, export_params.model_cache_path,
                            enabled_games=export_params.import_model_games)
    for name in report['archives']:
        shutil.copyfile(output/name, source/name)
        if file_sha(output/name) != file_sha(source/name):
            raise ValueError('Model-patched archive changed during export staging')
    return report


def _run_process(command, env=None, log=None):
    process = subprocess.run(command, env=None if env is None else {**os.environ, **env},
                             capture_output=True, text=True, timeout=3600)
    if log is not None:
        log.with_suffix('.stdout.log').write_text(process.stdout)
        log.with_suffix('.stderr.log').write_text(process.stderr)
    # WIT can print a structural error and still return zero (e.g. an incomplete
    # split image). Such diagnostics are failures regardless of the process status.
    diagnostics = process.stdout+'\n'+process.stderr
    if 'no space left on device' in diagnostics.lower():
        raise UnableToExportError(
            'The output drive ran out of space while building the game image. '
            'Free space or choose another drive and retry. '
            f'Working files and diagnostics are retained in {log.parent if log is not None else Path(command[-1]).parent}.')
    if process.returncode or '!! ERROR' in diagnostics or '!! FATAL' in diagnostics:
        raise RuntimeError(f'Prime 3 helper failed ({Path(command[0]).name}, exit code {process.returncode})\n'
                           +diagnostics[-12000:])


def _build_randomizer_command(toolchain, patch_data, input_path, output_path):
    validate_patch_data(patch_data)
    return (*toolchain.randomizer_command, '--input-path', str(input_path), '--output-path', str(output_path),
            '--layout', patch_data['seed'], '--starting-items', *patch_data['starting_items'].split(),
            '--starting-location', *patch_data['starting_location'].split(),
            *_optional_flag('--random-door-colors', patch_data['random_door_colors']),
            *_optional_flag('--random-welding-colors', patch_data['random_welding_colors']),
            '--hyper-hints', '--fast-flying',
            *_optional_flag('--exclude-olympus', patch_data.get('exclude_olympus', False)),
            *_optional_flag('--retain-space-assets', patch_data.get('warp_to_space', False)),
            *_optional_flag('--require-launcher', patch_data['missile_required_mains']),
            *_optional_flag('--require-ship-missile', patch_data['ship_missile_required_mains']),
            *_optional_flag('--phaaze-skip', patch_data['phaaze_skip']))


def _build_wit_command(toolchain, extracted_data_path, export_params):
    return (*toolchain.wit_command, 'COPY', '-I' if export_params.output_format == CorruptionOutputFormats.ISO else '-B',
            '--no-split', '--trunc', str(extracted_data_path), str(export_params.output_path))
