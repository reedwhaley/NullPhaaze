# Read-only native world/area discovery; no Lua calls, hooks or network service. Boundary
# names here: extract_profile, verify_native_code, snapshot, collect, main.
"""Read-only native world/area discovery; no Lua calls, hooks or network service."""

from __future__ import annotations

import argparse
import importlib
import json
import os
import sys
import time
from pathlib import Path

from construct import Struct

if __package__ in {None, ""}:
    _repository_root = os.fspath(Path(__file__).resolve().parents[2])
    if _repository_root not in sys.path:
        sys.path.insert(0, _repository_root)

from retro_data_structures.formats.mlvl import Prime3MLVL
from retro_data_structures.formats.pak import Pak
from retro_data_structures.formats.strg import Strg
from retro_data_structures.game_check import Game

from randovania.games.prime3.exporter.dol_patcher import parse_dol_header, virtual_address_to_file_offset
from nullphaze_network.prime3_lua_service.inventory_profile import RETAIL_HASH
from nullphaze_network.prime3_lua_service.observe import GAME_STATE_POINTER, DeferredSample, Memory
from nullphaze_network.prime3_lua_service.probe import sha256, verify_image

WORLDS_HASH = "09d2e05518f00a6562989c847af9af0a8bbc441193db5230236bbfb9b50a86c1"
STATE_MANAGER = 0x805C4F70
PLAYER_VTABLE = 0x80592C78
AREA_VTABLE = 0x8059110C
NATIVE_FUNCTIONS = {
    "world_area_lookup": (0x802C5F2C, 0x18),
    "world_area_loaded": (0x802C5EF0, 0x3C),
    "current_area_consumer_prefix": (0x802C5F44, 0x28),
    "lua_world_comparison": (0x802247F8, 0x38),
    "area_constructor_identity_prefix": (0x8008F734, 0xC4),
}


def extract_profile(dol: bytes, worlds_pak: bytes) -> dict:
    if sha256(dol) != RETAIL_HASH or sha256(worlds_pak) != WORLDS_HASH:
        raise ValueError("Location discovery requires the exact original retail DOL and Worlds.pak")
    header = parse_dol_header(dol)
    functions = {}
    for name, (address, size) in NATIVE_FUNCTIONS.items():
        offset = virtual_address_to_file_offset(header.sections, address, size)
        functions[name] = {"address": address, "size": size, "sha256": sha256(dol[offset : offset + size])}
    pak = Pak.parse(worlds_pak, Game.CORRUPTION)
    worlds = {}
    for world_id, resource in pak.get_all_assets():
        if resource.type != "MLVL":
            continue
        # Only the header and area table are needed. Some original worlds have
        # trailing layer/save metadata not handled by the library's full parser.
        fields = Prime3MLVL.subcons[:7]
        if [field.name for field in fields] != [
            "magic",
            "version",
            "world_name_id",
            "temple_key_world_index",
            "world_save_info_id",
            "default_skybox_id",
            "areas",
        ]:
            raise ValueError("Unsupported installed MLVL header layout")
        if not 0 < int.from_bytes(resource.data[0x24:0x28], "big") <= 512:
            raise ValueError("MLVL area count outside discovery bound")
        level = Struct(*fields).parse(resource.data, target_game=Game.CORRUPTION)
        areas = []
        for index, area in enumerate(level.areas):
            label = area.internal_area_name
            if area.area_name_id != 0xFFFFFFFFFFFFFFFF:
                strings = pak.get_asset(area.area_name_id)
                if strings is None or strings.type != "STRG":
                    raise ValueError("MLVL references a missing area name")
                names = list(Strg.parse(strings.data, Game.CORRUPTION).get_strings("ENGL"))
                if not names:
                    raise ValueError("Empty MLVL area name")
                label = names[0]
            areas.append(
                {
                    "index": index,
                    "mrea_id": f"{area.area_mrea_id:016x}",
                    "internal_id": f"{area.internal_area_id:016x}",
                    "name": label,
                    "internal_name": area.internal_area_name,
                }
            )
        if not 0 < len(areas) <= 512:
            raise ValueError("MLVL area count outside discovery bound")
        worlds[f"{world_id:016x}"] = areas
    if not worlds:
        raise ValueError("Worlds.pak has no MLVL metadata")
    return {
        "schema": 1,
        "dol_sha256": RETAIL_HASH,
        "worlds_pak_sha256": WORLDS_HASH,
        "native_functions": functions,
        "worlds": worlds,
        "scope": "native read-only discovery; not a Lua or CP3W location service",
        "metadata_scope": "MLVL header/area tables only; layer/save tails not interpreted",
    }


def verify_native_code(memory: Memory, profile: dict) -> None:
    for function in profile["native_functions"].values():
        if sha256(memory.read(function["address"], function["size"])) != function["sha256"]:
            raise ValueError("Live native location code does not match the retail profile")


def snapshot(memory: Memory, profile: dict) -> dict:
    game = memory.word(GAME_STATE_POINTER)
    context = memory.word(STATE_MANAGER + 0x28)
    if not game or not context or game % 4 or context % 4:
        raise ValueError("Game or state context unavailable")
    world = memory.word(context + 0x2134)
    player = memory.word(context + 0x2184)
    if not world or not player or world % 4 or player % 4 or memory.word(player) != PLAYER_VTABLE:
        raise ValueError("World or gameplay player unavailable")
    world_id = memory.read(world + 0x18, 8).hex()
    if world_id != memory.read(game + 8, 8).hex() or world_id not in profile["worlds"]:
        raise ValueError("World identity is unknown or has not converged")
    areas = profile["worlds"][world_id]
    count = memory.word(world + 0x30)
    index = memory.word(world + 0x7C)
    if count != len(areas) or not 0 <= index < count <= 512:
        raise ValueError("Current area index/count unavailable or inconsistent with MLVL")
    vector = memory.word(world + 0x38)
    if not vector or vector % 4:
        raise ValueError("Area vector unavailable or unaligned")
    area = memory.word(vector + 8 * index + 4)
    if not area or area % 4 or memory.word(area) != AREA_VTABLE or memory.word(area + 0x98) != 0x11:
        raise ValueError("Current area is not fully loaded")
    expected = areas[index]
    mrea_id = memory.read(area + 0x58, 8).hex()
    internal_id = memory.read(area + 0x60, 8).hex()
    if memory.word(area + 4) != index or mrea_id != expected["mrea_id"] or internal_id != expected["internal_id"]:
        raise ValueError("Loaded area identity does not match MLVL")
    return {
        "schema": 1,
        "available": True,
        "game_state": game,
        "context": context,
        "world": world,
        "player": player,
        "area": area,
        "world_id": world_id,
        "area_index": index,
        "area_count": count,
        "area_id": mrea_id,
        "area_internal_id": internal_id,
        "area_vtable": AREA_VTABLE,
        "area_name": expected["name"],
        "area_load_state": 0x11,
    }


def collect(memory: Memory, profile: dict) -> dict:
    first = snapshot(memory, profile)
    if first != snapshot(memory, profile):
        raise DeferredSample("Concurrent native world/area change")
    return first


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-data", type=Path, required=True)
    parser.add_argument("--build", type=Path, required=True)
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True, help="New directory for profile/capture")
    parser.add_argument("--seconds", type=int, default=180)
    args = parser.parse_args()
    source, output = args.source_data.resolve(), args.output.resolve()
    if output.exists() or source == output or source in output.parents or output in source.parents:
        parser.error("Use a new output directory disjoint from the original extraction")
    if not 1 <= args.seconds <= 3600:
        parser.error("--seconds must be 1..3600")
    profile = extract_profile((source / "sys/main.dol").read_bytes(), (source / "files/Worlds.pak").read_bytes())
    manifest = json.loads((args.build / "build.json").read_text(encoding="utf-8"))
    if manifest.get("dol_sha256") != RETAIL_HASH:
        raise ValueError("Probe image does not use the original supported DOL")
    image = verify_image(args.build.resolve(), manifest)
    launch = json.loads((args.run / "launch.json").read_text(encoding="utf-8"))
    psutil = importlib.import_module("psutil")
    processes = [p for p in psutil.process_iter(["name"]) if (p.info["name"] or "").lower() == "dolphin.exe"]
    if len(processes) != 1 or processes[0].pid != launch["pid"] or str(image) not in processes[0].cmdline():
        raise ValueError("Exactly the recorded Dolphin/image process must be running")
    engine = importlib.import_module("dolphin_memory_engine")
    engine.hook()
    memory = Memory(engine.read_bytes)
    count = 0
    try:
        verify_native_code(memory, profile)
        output.mkdir(parents=True)
        encoded = json.dumps(profile, indent=2, sort_keys=True) + "\n"
        (output / "profile.json").write_text(encoded, encoding="utf-8")
        with (output / "capture.jsonl").open("x", encoding="utf-8") as log:
            log.write(
                json.dumps(
                    {
                        "kind": "capture_start",
                        "method": "passive_native_location_discovery",
                        "pid": launch["pid"],
                        "probe_id": manifest["probe_id"],
                        "image_parts": manifest["image"]["parts"],
                        "profile_sha256": sha256(encoded.encode()),
                    }
                )
                + "\n"
            )
            deadline = time.monotonic() + args.seconds
            while time.monotonic() < deadline:
                try:
                    row = collect(memory, profile)
                    count += 1
                    row.update(kind="location", host_sample=count, wall_time=time.time())
                except (ValueError, RuntimeError) as error:
                    row = {
                        "kind": "unavailable",
                        "available": False,
                        "world_id": None,
                        "area_id": None,
                        "reason": str(error),
                        "wall_time": time.time(),
                    }
                log.write(json.dumps(row, sort_keys=True) + "\n")
                log.flush()
                time.sleep(1)
            log.write(json.dumps({"kind": "capture_end", "samples": count}) + "\n")
    finally:
        engine.un_hook()
    print(f"Captured {count} coherent native location samples; no Lua/hardware/collected-check service claim.")
    if count == 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
