# Prepare local Corruption model assets from the user's three retail images. Boundary names
# here: digest, catalog, validate_image, LocalModelConverter, canonicalize_bounds.
"""Prepare local Corruption model assets from the user's three retail images.

GPL-3.0-or-later. Uses the separately attributed NullPhaaze networking converters.
No game payloads are shipped here; the catalog contains identities and hashes only.
"""
from __future__ import annotations

import copy
import hashlib
import json
import math
import tempfile
from pathlib import Path

from randovania import get_data_path
from randovania.lib.rds_compat import install_legacy_asset_manager_api

install_legacy_asset_manager_api()

from nullphaze_network.prime3_lua_service.imported_gallery_assets import GalleryAssets
from nullphaze_network.prime3_lua_service.imported_gallery_opaque_emission import opaque_emission_mesh
from nullphaze_network.prime3_lua_service.imported_gallery_sources import add_raw, SUPPORTED
from nullphaze_network.prime3_lua_service.multiworld_models import ModelCache, RENDERER
from retro_data_structures.asset_manager import AssetManager
from retro_data_structures.conversion.asset_converter import AssetConverter
from retro_data_structures.conversion.conversions import converter_for
from retro_data_structures.file_provider import IsoFileProvider, PathFileProvider
from retro_data_structures.formats import format_for
from retro_data_structures.game_check import Game

CONVERTER_VERSION = 'optional-local-model-games-v2'


def digest(path: Path) -> str:
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def catalog() -> dict:
    return json.loads((get_data_path() / 'prime3/imported_model_catalog.json').read_text())


def validate_image(path: Path, prefix: bytes, title: str) -> None:
    if not path.is_file() or path.is_symlink() or path.suffix.lower() != '.iso':
        raise ValueError(f'Select a retail {title} ISO image: {path}')
    with path.open('rb') as stream:
        header = stream.read(32)
    if not header.startswith(prefix):
        raise ValueError(f'The selected image is not {title}: {path}')
    # Parse the file system now, rather than allowing a mislabeled/truncated ISO.
    IsoFileProvider(path)


class LocalModelConverter(GalleryAssets):
    """The accepted opaque-emission and model-matched presentation recipe."""

    def mesh(self, row, source_skin, scale, center, bone_map, bounds):
        canonicalize_bounds(row, scale, center, bounds)
        mesh, skin = super().mesh(row, source_skin, scale, center, bone_map, bounds)
        return opaque_emission_mesh(mesh)[0], skin


def canonicalize_bounds(row, scale, center, bounds):
    """Stabilize near-zero pose centering across NumPy/BLAS implementations.

    Windows and Linux matrix products can differ in their final double-precision
    bits. A near-zero box center then becomes a different *single*-precision root
    translation. Use the reviewed presentation coordinates only after recomputing
    the bounds from the source and proving agreement to 2e-12 relative/absolute.
    These are numeric presentation metadata, not cached resource payloads.
    """
    reference = catalog()['presentation'][row['game'] + ':' + row['name']]
    expected = reference['center'] + reference['bounds'][0] + reference['bounds'][1]
    actual = list(center) + list(bounds[0]) + list(bounds[1])
    if (not math.isfinite(scale) or abs(scale - reference['scale']) > 2e-12 * max(1, abs(reference['scale']))) or any(
        not math.isfinite(a) or abs(a - b) > 2e-12 * max(1, abs(b))
        for a, b in zip(actual, expected, strict=True)
    ):
        raise ValueError(f'Source pose bounds differ from the validated model: {row["game"]} {row["name"]}')
    # GalleryAssets.convert deliberately passes these mutable lists into mesh
    # before it computes bone and animation translations; normalize both paths.
    center[:] = reference['center']
    bounds[0][:] = reference['bounds'][0]
    bounds[1][:] = reference['bounds'][1]


def source_models(prime_iso, echoes_iso, custom, echoes_cache):
    """Recreate the audited source overlays using freshly exported local assets."""
    import zlib
    if prime_iso is None:
        empty = custom.parent / 'empty-source'
        (empty / 'files').mkdir(parents=True)
        (empty / 'sys').mkdir()
        # RDS requests a DOL header for a Prime-format asset container. This
        # empty synthetic header has no sections and is never exported/run.
        (empty / 'sys/main.dol').write_bytes(bytes(256))
        provider = PathFileProvider(empty)
    else:
        provider = IsoFileProvider(prime_iso)
    prime = AssetManager(provider, Game.PRIME)
    for path in sorted(custom.iterdir()):
        kind = path.suffix[1:]
        if kind not in SUPPORTED:
            continue
        raw = path.read_bytes()
        if len(raw) > 6 and raw[4] == 0x78:
            try:
                decoded = zlib.decompress(raw[4:])
            except zlib.error:
                pass
            else:
                if len(decoded) != int.from_bytes(raw[:4], 'big'):
                    raise ValueError('Compressed custom model length mismatch')
                raw = decoded
        add_raw(prime, int(path.stem, 16), kind, raw)
    metadata = json.loads((echoes_cache / 'meta.json').read_text()) if echoes_iso else {'new_assets': [], 'items': {}}
    for row in metadata['new_assets']:
        kind, identity = row['type'], row['new_id']
        if kind not in SUPPORTED:
            raise ValueError(f'Unsupported Echoes model dependency: {kind}')
        add_raw(prime, identity, kind, (echoes_cache / f'{identity}.{kind}').read_bytes())
    rows = [dict(row, game='Prime') for row in catalog()['prime_catalog']] if prime_iso else []
    echoes = AssetManager(IsoFileProvider(echoes_iso), Game.ECHOES) if echoes_iso else None
    next_id = 0xFFFE0000

    def new_id(_):
        nonlocal next_id
        identity = next_id
        next_id += 1
        return identity

    converter = AssetConverter(Game.PRIME, {Game.ECHOES: echoes}, new_id, converter_for)
    gamecube = next((row for row in rows if row['name'] == 'RandovaniaGamecube'), None)
    model_data = json.loads((get_data_path() / 'ClarisPrimeRandomizer/RandomizerData.json').read_text())
    for original in model_data['ModelData'] if echoes_iso else []:
        row = dict(game='Echoes', name=original['Name'], model=original['Model'],
                   ancs=original['AnimSet'], character=original['Character'], animation=original['DefaultAnim'])
        cached = metadata['items'].get('prime2_' + row['name'])
        if cached:
            row.update(model=cached['cmdl'], ancs=cached['ancs'], character=cached['character'])
        elif row['model'] == 0xFFFFFFFF:
            if gamecube is None:
                # These three catalog entries have no retail Echoes model.
                # Keep the core's native Corruption presentation; no Prime
                # image or Gamecube placeholder is needed for Echoes-only use.
                continue
            row.update(model=gamecube['model'], ancs=gamecube['ancs'], character=0)
        else:
            row['model'] = converter.convert_id(row['model'], Game.ECHOES)
        rows.append(row)
    for asset in converter.converted_assets.values():
        add_raw(prime, asset.id, asset.type, format_for(asset.type).build(asset.resource, target_game=Game.PRIME))
    for row in rows:
        if row['ancs'] != 0xFFFFFFFF:
            if prime.get_asset_type(row['ancs']) != 'ANCS':
                candidates = []
                for path in custom.glob('*.ANCS'):
                    identity = int(path.stem, 16)
                    chars = prime.get_parsed_asset(identity)._raw.character_set.characters
                    if row['character'] < len(chars) and chars[row['character']].model_id == row['model']:
                        candidates.append(identity)
                if len(candidates) != 1:
                    raise ValueError(f'Ambiguous custom animation mapping: {row["name"]}')
                row['ancs'] = candidates[0]
            character = prime.get_parsed_asset(row['ancs'])._raw.character_set.characters[row['character']]
            row.update(model=character.model_id, skin=character.skin_id, skeleton=character.skeleton_id)
        if not prime.does_asset_exists(row['model']):
            raise ValueError(f'Missing source model: {row["game"]} {row["name"]}')
    expected_count = (47 if prime_iso else 0) + ((46 if prime_iso else 43) if echoes_iso else 0)
    if len(rows) != expected_count:
        raise ValueError('Incomplete source model catalog')
    return prime, rows


def build_cache(prime_iso, echoes_iso, corruption_iso, output, progress):
    """Build in a new private staging directory; caller publishes only after verification."""
    import py_randomprime
    from randovania.patching.prime.asset_conversion import convert_prime2_pickups

    output.mkdir()
    custom = output / 'prime-custom'
    progress('Reading Prime model assets', 0.1)
    if prime_iso is not None:
        py_randomprime.patch_iso(prime_iso, output / 'unused.iso', {
            'runMode': 'export_assets', 'exportAssetDir': str(custom),
            'preferences': {'cacheDir': str(output / 'backend-cache')}, 'seed': 0,
        }, py_randomprime.ProgressNotifier(lambda percent, message: progress(message, 0.15)))
    else:
        custom.mkdir()
    if (output / 'unused.iso').exists() and (output / 'unused.iso').stat().st_size:
        raise ValueError('Asset-only extraction unexpectedly created a game image')
    echoes_cache = output / 'echoes-source'
    progress('Reading Echoes model assets', 0.2)
    if echoes_iso is not None:
        convert_prime2_pickups(echoes_iso, echoes_cache, lambda text, fraction: progress(text, 0.2 + fraction * 0.2))
    source, rows = source_models(prime_iso, echoes_iso, custom, echoes_cache)
    native = AssetManager(IsoFileProvider(corruption_iso), Game.CORRUPTION)
    converter = LocalModelConverter(source, native)
    entries = []
    for index, row in enumerate(rows):
        progress(f'Preparing {row["game"]}: {row["name"]}', 0.4 + index / len(rows) * 0.5)
        entries.append(converter.convert(copy.deepcopy(row)))
    resources = converter.finish()
    assets = output / 'assets'
    assets.mkdir()
    hashes = {}
    for resource in resources:
        path = assets / f'{resource.identity:016x}.{resource.kind.decode()}'
        path.write_bytes(resource.read())
        hashes[path.name] = digest(path)
    expected = expected_files(prime_iso is not None, echoes_iso is not None)
    if hashes != expected:
        changed = sorted(name for name in set(hashes) | set(expected) if hashes.get(name) != expected.get(name))
        raise ValueError(f'Converted models differ from the validated renderer ({len(changed)} resources; '
                         f'first: {changed[:3]}). No cache or game image was published.')
    # Resource insertion order affects MREA dependency ordering. Preserve the
    # validated catalog order rather than filesystem or conversion traversal.
    games = (['Prime'] if prime_iso else []) + (['Echoes'] if echoes_iso else [])
    manifest = dict(renderer=RENDERER, entries=entries, files=dict(expected), local_user_assets_only=True,
                    games=games, native_fallbacks=(['PowerBeam INCOMPLETE', 'CombatVisor INCOMPLETE',
                    'MorphBall INCOMPLETE'] if echoes_iso and not prime_iso else []))
    (output / 'models.json').write_text(json.dumps(manifest, indent=2))
    ModelCache(output)
    return manifest


def expected_files(use_prime, use_echoes):
    data = catalog()
    if use_prime and use_echoes:
        return data['expected_files']
    if not use_prime and not use_echoes:
        return {}
    names = set(data['inventories']['prime' if use_prime else 'echoes'])
    return {name: value for name, value in data['expected_files'].items() if name in names}


def prepare_cache(prime_iso: Path | None, echoes_iso: Path | None, corruption_iso: Path, cache_root: Path, progress) -> Path | None:
    """Reuse only verified assets bound to these inputs; never replace an existing cache."""
    if prime_iso is None and echoes_iso is None:
        return None
    inputs = {}
    for name, path, prefix, title in (
        ('prime', prime_iso, b'GM8', 'Metroid Prime'),
        ('echoes', echoes_iso, b'G2M', 'Metroid Prime 2: Echoes'),
        ('corruption', corruption_iso, b'RM3', 'Metroid Prime 3: Corruption'),
    ):
        if path is None:
            continue
        progress(f'Checking {title} image', 0)
        validate_image(path, prefix, title)
        inputs[name] = digest(path)
    key = hashlib.sha256(json.dumps({'images': inputs, 'converter': CONVERTER_VERSION}, sort_keys=True).encode()).hexdigest()
    cache_root.mkdir(parents=True, exist_ok=True)
    destination = cache_root / key
    if destination.exists():
        ModelCache(destination)
        manifest = json.loads((destination / 'models.json').read_text())
        if (manifest.get('source_images') != inputs or manifest.get('converter_version') != CONVERTER_VERSION
                or manifest['files'] != expected_files(prime_iso is not None, echoes_iso is not None)):
            raise ValueError(f'Model cache provenance mismatch: {destination}')
        progress('Using verified cross-game models', 1)
        return destination
    # TemporaryDirectory cleans only this operation's own staging assets on failure.
    with tempfile.TemporaryDirectory(prefix='.prepare-models-', dir=cache_root) as staging:
        stage = Path(staging) / 'cache'
        manifest = build_cache(prime_iso, echoes_iso, corruption_iso, stage, progress)
        for name, path in (('prime', prime_iso), ('echoes', echoes_iso), ('corruption', corruption_iso)):
            if path is None:
                continue
            if digest(path) != inputs[name]:
                raise ValueError(f'{name} source image changed while preparing models')
        manifest['source_images'] = inputs
        manifest['converter_version'] = CONVERTER_VERSION
        (stage / 'models.json').write_text(json.dumps(manifest, indent=2))
        # Keep only the complete model cache; raw source overlays stay in private staging.
        ready = Path(staging) / 'ready'
        ready.mkdir()
        (stage / 'assets').rename(ready / 'assets')
        (stage / 'models.json').rename(ready / 'models.json')
        # Publish the complete directory in one rename on the same filesystem.
        # A simultaneous preparation may win; validate it rather than replacing it.
        try:
            ready.rename(destination)
        except FileExistsError:
            ModelCache(destination)
            existing = json.loads((destination / 'models.json').read_text())
            if (existing.get('source_images') != inputs or existing.get('converter_version') != CONVERTER_VERSION
                    or existing['files'] != expected_files(prime_iso is not None, echoes_iso is not None)):
                raise ValueError('Concurrent model cache provenance mismatch')
    progress('Cross-game models ready', 1)
    return destination


def main(argv=None):
    import argparse
    parser = argparse.ArgumentParser()
    for name in ('prime', 'echoes', 'corruption', 'cache-root'):
        parser.add_argument('--' + name, required=name in ('corruption', 'cache-root'), type=Path)
    args = parser.parse_args(argv)
    result = prepare_cache(args.prime, args.echoes, args.corruption, args.cache_root,
                           lambda text, fraction: print(text, flush=True))
    cache = ModelCache(result) if result else None
    print(json.dumps({'cache': str(result) if result else None,
                      'verified_resources': len(cache.resources) if cache else 0,
                      'models': len(cache.entries) if cache else 0}))
    return 0
