# Install the addon on the actual post-core seed and verify its input/output resources.
# Historical MIT-core wording describes lineage; this package's aggregate RDS terms are in
# NOTICE.md. Boundary names here: pickup_map, file_sha, preflight, verify_image, install.
"""GPL addon installation on the actual seed, after the MIT core operation."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil

from nullphaze_network.prime3_lua_service import (
    bridge, location, multiworld_areas, multiworld_presentation,
    multiworld_service_areas, runtime_assets,
)
from randovania.games.prime3.multiworld.manifest import validate_manifest

PICKUP_MAP_SHA256 = "74d801e6f7f70276d6a039c1a26157436675ffe30d98914d7f6d0d9ea0e4c525"


def pickup_map():
    path = Path(__file__).resolve().parents[1] / "data/prime3_multiworld_pickups.json"
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != PICKUP_MAP_SHA256:
        raise ValueError("The audited Corruption pickup mapping changed")
    result = json.loads(raw)
    if result["schema"] != 1 or [row["index"] for row in result["pickups"]] != list(range(100)):
        raise ValueError("Incomplete Corruption pickup event mapping")
    return result


def file_sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def preflight(manifest, *, asset_directory=None):
    validate_manifest(manifest)
    audit = pickup_map()
    rows = multiworld_presentation.plan(manifest, audit["pickups"])
    runtime_assets.load(asset_directory)
    return audit, rows


def verify_image(image, staged_data, output, toolchain, progress):
    """Read the finished container back and compare every staged game file."""
    from randovania.games.prime3.exporter.toolchain import extract_prime3_disc_image
    extract_prime3_disc_image(toolchain, image, output,
                             lambda text, fraction: progress(text, 0.91 + 0.05*fraction))
    extracted = output / 'DATA'
    expected = {path.relative_to(staged_data).as_posix(): path
                for path in staged_data.rglob('*') if path.is_file()}
    actual = {path.relative_to(extracted).as_posix(): path
              for path in extracted.rglob('*') if path.is_file()}
    if actual.keys() != expected.keys():
        raise ValueError('Final multiworld image file inventory differs from staging')
    regenerated = []
    for name, source in expected.items():
        if file_sha(source) != file_sha(actual[name]):
            bridge.verify_container_metadata(name, source.read_bytes(), actual[name].read_bytes())
            regenerated.append(name)
    return {'passed': True, 'files': len(expected), 'container_metadata': regenerated,
            'patched_dol_verified': True, 'all_game_resources_verified': True}


def install(data, output, manifest, progress=lambda *_: None, *, location_profile, asset_directory=None, templates=None):
    """Modify only the caller-owned extraction, preserving every unrelated resource."""
    data, output = Path(data), Path(output)
    audit, presentation = preflight(manifest, asset_directory=asset_directory)
    output.mkdir(parents=True, exist_ok=False)
    original_dol = (data / "sys/main.dol").read_bytes()
    # Capture this profile from the verified retail extraction before the core
    # modifies Worlds.pak. Never restore a retail archive over a randomized seed.
    profile = location_profile
    if (profile.get("schema") != 1 or profile.get("dol_sha256") != file_sha(data / "sys/main.dol")
            or profile.get("worlds_pak_sha256") != location.WORLDS_HASH):
        raise ValueError("Networking requires a verified original location profile")
    native = runtime_assets.bind_seed(manifest, audit["pickups"], output / "native", directory=asset_directory)
    dol, dol_report = bridge.patch_dol(original_dol, output / "native", output / "bootstrap-unused",
                                     bootstrap_template=asset_directory or runtime_assets.default_directory())
    # Connection notices also need the timed MEMO template when this world
    # has no incoming item presentation rows.
    if templates is None:
        templates = multiworld_presentation.read_templates(data / "files")

    def install_archives(stage, report):
        for name in report["archives"]:
            source, target = stage / name, data / "files" / name
            checksum = file_sha(source)
            shutil.copyfile(source, target)
            if file_sha(target) != checksum:
                raise ValueError("Networking addon archive changed during staging")

    progress("Installing audited pickup callbacks...", 0.1)
    callbacks = multiworld_areas.patch_archives(data / "files", output / "callbacks", manifest, audit)
    install_archives(output / "callbacks", callbacks)
    progress("Installing networking and item presentation...", 0.4)
    services = multiworld_service_areas.patch_archives(
        data / "files", output / "services", profile, presentation=presentation, templates=templates)
    install_archives(output / "services", services)
    (data / "sys/main.dol").write_bytes(dol)
    if file_sha(data / "sys/main.dol") != hashlib.sha256(dol).hexdigest():
        raise ValueError("Networking DOL changed during staging")
    result = {"world_uuid": manifest["world_uuid"], "seed_fingerprint": manifest["seed_fingerprint"],
              "save_slot": manifest["save_slot"], "save_filename": native["multiworld"]["save_filename"],
              "new_multiworld_save_only": True, "existing_save_migration": False,
              "pickup_mapping_sha256": PICKUP_MAP_SHA256, "callbacks": callbacks,
              "service": services, "native": native, "dol": dol_report,
              "compiler_required_on_client": False, "core_interface_unchanged": True,
              "final_dol_sha256": file_sha(data / "sys/main.dol")}
    (output / "installation.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    progress("Networking runtime installed and checked", 1.0)
    return result
