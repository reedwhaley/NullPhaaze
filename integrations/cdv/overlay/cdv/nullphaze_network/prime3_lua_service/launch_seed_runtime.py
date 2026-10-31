# Launch only a verified private seed image with a separate copied profile. Boundary names
# here: prepare, retire_previous, launch.
"""Launch only a verified private seed image with a separate copied profile."""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

import psutil

from nullphaze_network.prime3_lua_service import probe
from randovania.games.prime3.multiworld import checkpoint


def prepare(root, profile_from):
    root, profile_from = root.resolve(), profile_from.resolve()
    build = json.loads((root / "build.json").read_text())
    if (build.get("private_validation_only") is not True or build.get("production_export_enabled") is not False
            or build.get("image_verified") is not True or not build.get("disc_roundtrip", {}).get("passed")
            or build["service"]["areas"] != 284
            or build["service"]["core_removed_areas"] != ["bd0bc908940a1a0c", "ef19aa26828b708b"]
            or build["callbacks"]["checks"] != 100):
        raise ValueError("Private seed build has not passed coverage/integrity gates")
    image = root / "image/RM3E01.wbfs"
    if probe.file_hash(image) != build["image_sha256"]:
        raise ValueError("Seed image changed after integrity validation")
    fixture = (root / "disposable-checkpoint.bin").read_bytes()
    checkpoint.validate(fixture, (root / "profile.bin").read_bytes())
    if probe.file_hash(root / "disposable-checkpoint.bin") != build["private_fixture"]["sha256"]:
        raise ValueError("Private checkpoint changed after build")
    filename = build["private_fixture"]["filename"]
    if len(filename) != 8 or any(c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567" for c in filename):
        raise ValueError("Unexpected private native save filename")
    if profile_from == root or root in profile_from.parents or profile_from in root.parents:
        raise ValueError("Private build and original profile must be disjoint")
    output = root / "run"
    output.mkdir(exist_ok=False)
    profile = output / "dolphin-user"
    hashes = {}
    for name in ("Config", "Wii"):
        source = profile_from / name
        if not source.is_dir() or any(path.is_symlink() or path.is_junction() for path in source.rglob("*")):
            raise ValueError("Expected a regular original profile tree")
        shutil.copytree(source, profile / name)
        for file in source.rglob("*"):
            if file.is_file():
                relative = file.relative_to(profile_from)
                hashes[str(relative)] = probe.file_hash(file)
                if probe.file_hash(profile / relative) != hashes[str(relative)]:
                    raise ValueError("Private profile copy mismatch")
    save = profile / "Wii/title/00010000/524d3345/data" / filename
    if not save.parent.is_dir():
        raise ValueError("Copied title save directory missing")
    with save.open("xb") as stream:
        stream.write(fixture)
    return image, profile, output, build, hashes, save


def retire_previous(launch_path, output):
    previous = json.loads(launch_path.read_text())
    command = previous["command"]
    profile = Path(command[command.index("--user") + 1]).resolve()
    if profile.parent != launch_path.resolve().parent or profile.name != "dolphin-user":
        raise ValueError("Previous run does not own the claimed private profile")
    data = profile / "Wii/title/00010000/524d3345/data"
    save = Path(previous["private_save"]) if "private_save" in previous else data / "cp3w.bin"
    if save.resolve().parent != data.resolve():
        raise ValueError("Previous save is outside its owned title directory")
    digest = previous.get("private_save_sha256", previous.get("network_container_sha256"))
    if not digest:
        raise ValueError("Previous launch has no private checkpoint hash")
    if probe.file_hash(save) != digest:
        raise ValueError("Previous private checkpoint changed; preserve and inspect before replacing the run")
    process = psutil.Process(previous["pid"])
    actual = process.cmdline()
    if (process.name().lower() != "dolphin.exe" or "--user" not in actual
            or Path(actual[actual.index("--user") + 1]).resolve() != profile):
        raise ValueError("Previous PID is not the owned private Dolphin instance")
    observer_pid = previous.get("observer_pid")
    if observer_pid is not None and psutil.pid_exists(observer_pid):
        observer = psutil.Process(observer_pid)
        args = observer.cmdline()
        if ("nullphaze_network.prime3_lua_service.observe_seed_runtime" not in args or "--root" not in args
                or Path(args[args.index("--root") + 1]).resolve() != launch_path.resolve().parent.parent):
            raise ValueError("Previous observer PID no longer belongs to this private run")
        observer.terminate()
        observer.wait(timeout=20)
    process.terminate()
    process.wait(timeout=20)
    if probe.file_hash(save) != digest:
        raise ValueError("Previous private checkpoint changed during process shutdown")
    (output / "previous-session.json").write_text(json.dumps({
        "launch": str(launch_path), "pid": previous["pid"], "save_sha256": digest,
        "save_unchanged": True, "unsaved_runtime_replaced": True,
    }, indent=2))


def launch(root, profile_from, dolphin, manifest, previous_launch=None):
    image, profile, output, build, hashes, save = prepare(root, profile_from)
    if previous_launch is not None:
        retire_previous(previous_launch, output)
    command = [str(dolphin), "--user", str(profile), "--exec", str(image),
               "--config", "Dolphin.Core.EnableCheats=False", "--config", "Dolphin.General.GDBPort=-1"]
    with (output / "stdout.log").open("xb") as out, (output / "stderr.log").open("xb") as err:
        process = subprocess.Popen(command, stdout=out, stderr=err)
    report = {"pid": process.pid, "command": command, "original_profile_hashes": hashes,
              "private_save": str(save), "private_save_sha256": probe.file_hash(save),
              "image_sha256": build["image_sha256"], "debugger": False, "grants_enabled": False,
              "hardware_modified": False, "live_result": "awaiting_human_save_load"}
    with (output / "observer.stdout.log").open("xb") as out, (output / "observer.stderr.log").open("xb") as err:
        observer = subprocess.Popen([sys.executable, "-m", "nullphaze_network.prime3_lua_service.observe_seed_runtime",
                                     "--root", str(root), "--manifest", str(manifest),
                                     "--output", str(root / "live-readonly")],
                                    stdout=out, stderr=err, creationflags=subprocess.CREATE_NO_WINDOW)
    report["observer_pid"] = observer.pid
    (output / "launch.json").write_text(json.dumps(report, indent=2))
    print(json.dumps({"pid": process.pid, "observer_pid": observer.pid, "save_filename": save.name}), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("root", "profile-from", "dolphin", "manifest"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--previous-launch", type=Path)
    args = parser.parse_args()
    launch(args.root.resolve(), args.profile_from.resolve(), args.dolphin.resolve(), args.manifest.resolve(),
           args.previous_launch.resolve() if args.previous_launch else None)
