# Unpublished seed-runtime validation build; does not enable production exports. Boundary
# names here: build.
"""Unpublished seed-runtime validation build; does not enable production exports."""

import argparse
import hashlib
import json
import shutil
import struct
import subprocess
import zlib
from pathlib import Path

from nullphaze_network.prime3_lua_service import (
    bridge,
    location,
    multiworld_areas,
    multiworld_service_areas,
    network_save,
    probe,
)
from randovania.games.prime3.multiworld import checkpoint, seed_compiler


def build(root, fixture, resume=False, model_cache=None):
    if resume and model_cache is not None:
        raise ValueError("Model integration requires a fresh runtime validation build")
    project = Path(__file__).resolve().parents[3]
    original = Path(r"E:\ROMS\Corruption Extract\DATA")
    inputs = project / "artifacts/multiworld-validation"
    root.mkdir(parents=True, exist_ok=resume)
    suffix = "-resumed" if resume else ""
    manifest = json.loads((inputs / "manifest.json").read_text())
    audit = json.loads((project / "evidence/multiworld-seed-pickup-audit.json").read_text())
    profile = bytes.fromhex(manifest["checkpoint_profile"])
    if profile != (inputs / "profile.bin").read_bytes():
        raise ValueError("Seed checkpoint profile differs from the handed-off compiler input")
    (root / "profile.bin").write_bytes(profile)
    (root / "seed.h").write_text(seed_compiler.compile_seed(manifest, audit["pickups"]))
    report = {"private_validation_only": True, "production_export_enabled": False,
              "world_uuid": manifest["world_uuid"], "input_files": {}, "hardware_modified": False}
    files = list((inputs / "core-seed").iterdir())
    if len(files) != 11 or any(not file.is_file() for file in files):
        raise ValueError("Expected the unchanged eleven-file core output")
    for file in files:
        report["input_files"][file.name] = probe.file_hash(file)
    native_options = {"save_trace": True, "network_profile": root / "profile.bin", "receipt_lifecycle": True,
                      "receipt_coupling": True, "receipt_delivery": True, "network_delivery": True,
                      "owned_network_delivery": True, "owned_receive_mem2": True,
                      "multiworld_header": root / "seed.h"}
    native = bridge.compile_bridge(root / ("native" + suffix), **native_options)
    repeated = bridge.compile_bridge(root / ("native-repeat" + suffix), **native_options)
    if native != repeated:
        raise ValueError("Seed runtime is not reproducible")
    patched_dol, dol_report = bridge.patch_dol((original / "sys/main.dol").read_bytes(),
                                            root / ("native" + suffix), root / ("bootstrap" + suffix))
    report["native"] = native
    report["dol"] = dol_report
    data = root / "image/DATA"
    callbacks = root / ("callbacks" + suffix)
    report["callbacks"] = multiworld_areas.patch_archives(inputs / "core-seed", callbacks, manifest, audit)
    if not resume:
        shutil.copytree(original, data)
        for file in files:
            shutil.copyfile(file, data / "files" / file.name)
        for path in callbacks.iterdir():
            shutil.copyfile(path, data / "files" / path.name)
    else:
        expected = {path.relative_to(original): path for path in original.rglob("*") if path.is_file()}
        expected.update({Path("files") / path.name: path for path in files})
        expected.update({Path("files") / path.name: path for path in callbacks.iterdir()})
        for relative, source in expected.items():
            if probe.file_hash(source) != probe.file_hash(data / relative):
                raise ValueError(f"Cannot resume modified staging input: {relative}")
    report["location_profile"] = location.extract_profile((original / "sys/main.dol").read_bytes(),
                                                         (original / "files/Worlds.pak").read_bytes())
    if model_cache is not None:
        from randovania.games.prime3.exporter.models import model_plan
        from nullphaze_network.prime3_lua_service.multiworld_models import patch_archives

        report["models"] = patch_archives(data / "files", root / "model-areas", model_plan(manifest), model_cache)
        for name in report["models"]["archives"]:
            shutil.copyfile(root / "model-areas" / name, data / "files" / name)
    report["service"] = multiworld_service_areas.patch_archives(
        data / "files", root / "service-areas", report["location_profile"], resume=resume)
    for path in (root / "service-areas").iterdir():
        shutil.copyfile(path, data / "files" / path.name)
    (data / "sys/main.dol").write_bytes(patched_dol)
    # An explicitly supplied disposable fixture is copied, never migrated in place.
    old = fixture.read_bytes()
    retail = network_save.decode(old).retail
    records = bytearray(3 * checkpoint.RECORD_SIZE)
    for slot in range(3):
        records[slot * 80] = slot
        records[slot * 80 + 4:slot * 80 + 20] = profile[32 + 16 * slot:48 + 16 * slot]
    wire = checkpoint.MAGIC + struct.pack(">II", checkpoint.VERSION, checkpoint.TOTAL_SIZE) + profile[:32]
    wire += struct.pack(">II", 65536, 3) + hashlib.sha256(retail).digest() + retail + records
    wire += struct.pack(">I", zlib.crc32(wire))
    checkpoint.validate(wire, profile)
    (root / "disposable-checkpoint.bin").write_bytes(wire)
    report["private_fixture"] = {"source_sha256": hashlib.sha256(old).hexdigest(),
                                 "sha256": hashlib.sha256(wire).hexdigest(),
                                 "filename": native["multiworld"]["save_filename"], "existing_save_migration": False}
    image = root / "image/RM3E01.wbfs"
    wit = project / "cdv/native/wit/wit.exe"
    if not wit.exists():
        wit = Path(r"C:\Users\Reed Whaley\Documents\MP3 Networking\randovania\data\gollop_mp3_patcher\wit\bin\wit.exe")
    for command in ([str(wit), "COPY", "-B", "--no-split", "--trunc", str(data), str(image)],
                    [str(wit), "VERIFY", str(image)]):
        completed = subprocess.run(command, capture_output=True, text=True, timeout=3600, check=False)
        (root / f"wit-{command[1].lower()}.log").write_text(completed.stdout + completed.stderr)
        if completed.returncode or "!!" in completed.stderr:
            raise ValueError("Validation image integrity command failed")
    if fixture.read_bytes() != old or any(probe.file_hash(inputs / "core-seed" / name) != digest
                                         for name, digest in report["input_files"].items()):
        raise ValueError("An immutable input changed")
    report["image_sha256"] = probe.file_hash(image)
    report["image_verified"] = True
    report["disc_roundtrip"] = bridge.verify_roundtrip(image, root / "roundtrip", wit, {
        "files": {str(path.relative_to(data)).replace("\\", "/"): probe.file_hash(path)
                  for path in data.rglob("*") if path.is_file()},
        "dol_sha256": probe.sha256(patched_dol),
        "output_pak_sha256": probe.file_hash(data / "files/UniverseArea.pak"),
    })
    report["native_execution"] = "pending_Dolphin"
    (root / "build.json").write_text(json.dumps(report, indent=2))
    print(json.dumps({"image_verified": True, "service_areas": report["service"]["areas"],
                      "callbacks": report["callbacks"]["checks"],
                      "save_filename": native["multiworld"]["save_filename"]}), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--disposable-fixture", type=Path, required=True)
    parser.add_argument("--resume-after-service-failure", action="store_true")
    parser.add_argument("--model-cache", type=Path)
    args = parser.parse_args()
    build(args.root.resolve(), args.disposable_fixture.resolve(), args.resume_after_service_failure,
          args.model_cache.resolve() if args.model_cache else None)
