# Observe the read-only probe through bounded memory reads, without GDB or Lua calls.
# Boundary names here: DeferredSample, Memory, table_pointer, integer, owner.
"""Observe the read-only probe through bounded memory reads, without GDB or Lua calls."""

from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import math
import os
import struct
import sys
import time
from pathlib import Path

if __package__ in {None, ""}:
    _repository_root = os.fspath(Path(__file__).resolve().parents[2])
    if _repository_root not in sys.path:
        sys.path.insert(0, _repository_root)

from nullphaze_network.prime3_lua_service.capture import GAME_STATE_POINTER, ITEM_IDS, ITEMS
from nullphaze_network.prime3_lua_service.inventory_profile import bindings
from nullphaze_network.prime3_lua_service.probe import sha256, verify_image

ACTOR_VTABLE = 0x805962A0
RETAIL_R2 = 0x806869C0


class DeferredSample(ValueError):
    """Expected asynchronous change; retain the source-validated actor cache."""


class Memory:
    def __init__(self, read, *, manifest: dict | None = None):
        self._read = read
        self.schema, self.names, self.item_ids = bindings(manifest or {})
        self.location_profile = (manifest or {}).get("location_profile")
        self.grant_profile = (manifest or {}).get("inventory_write_probe")
        self.bridge_profile = (manifest or {}).get("lua_location_bridge")

    def read(self, address: int, length: int) -> bytes:
        if not 0 < length <= 65536 or not any(
            low <= address <= high - length for low, high in ((0x80000000, 0x81800000), (0x90000000, 0x94000000))
        ):
            raise ValueError("Read outside bounded retail RAM")
        result = self._read(address, length)
        if len(result) != length:
            raise ValueError("Short memory read")
        return result

    def word(self, address: int) -> int:
        return int.from_bytes(self.read(address, 4), "big")

    def region_sha256(self, address: int, length: int) -> str:
        if type(length) is not int or not 0 < length <= 0x40000:
            raise ValueError("Immutable region exceeds reserved bridge bound")
        digest = hashlib.sha256()
        for offset in range(0, length, 16384):
            digest.update(self.read(address + offset, min(16384, length - offset)))
        return digest.hexdigest()

    def string(self, address: int) -> str:
        if self.read(address + 4, 1) != b"\x04":
            raise ValueError("Not a retail Lua TString")
        length = self.word(address + 12)
        if not 0 < length <= 64:
            raise ValueError("Lua key string exceeds bound")
        return self.read(address + 16, length).decode("ascii")

    def value(self, raw: bytes):
        tag, value = struct.unpack(">II", raw)
        if tag == 0:
            return None
        if tag == 1 and value in {0, 1}:
            return bool(value)
        if tag == 3:
            number = struct.unpack(">f", raw[4:])[0]
            if math.isfinite(number):
                return number
        if tag == 4:
            return self.string(value)
        if tag == 5:
            return ("table", value)
        raise ValueError("Unsupported or inconsistent Lua value")

    def table(self, address: int) -> dict:
        header = self.read(address, 32)
        if header[4] != 5 or header[7] > 9:
            raise ValueError("Invalid or oversized Lua hash table")
        nodes = self.word(address + 16)
        raw = self.read(nodes, (1 << header[7]) * 20)
        result = {}
        for offset in range(0, len(raw), 20):
            if int.from_bytes(raw[offset : offset + 4], "big") != 4:
                continue
            key = self.string(int.from_bytes(raw[offset + 4 : offset + 8], "big"))
            # Global tables contain functions and userdata. Decode only the
            # requested diagnostic table and the probe's bounded field names.
            if key in {
                "CP3WProbe",
                "schema",
                "sequence",
                "snapshots",
                "failures",
                "available",
                "records",
                "items",
                "amount",
                "capacity",
                "changed",
                "change_count",
                "location",
                "location_changes",
                "world_id",
                "area_id",
                "internal_id",
                "area_index",
                "grant_status",
                "grant_attempts",
            }:
                if key in result:
                    raise ValueError("Duplicate Lua probe key")
                result[key] = self.value(raw[offset + 8 : offset + 16])
        return result

    def array(self, address: int, count: int) -> list:
        if self.read(address + 4, 1) != b"\x05":
            raise ValueError("Array does not reference a Lua table")
        capacity = self.word(address + 28)
        if not 0 < count <= len(self.names) or not count <= capacity <= 1 << (count - 1).bit_length():
            raise ValueError("Unexpected Lua array size")
        raw = self.read(self.word(address + 12), capacity * 8)
        if any(int.from_bytes(raw[index * 8 : index * 8 + 4], "big") != 0 for index in range(count, capacity)):
            raise ValueError("Unexpected extra Lua array elements")
        return [self.value(raw[index * 8 : index * 8 + 8]) for index in range(count)]


def table_pointer(value) -> int:
    if not isinstance(value, tuple) or len(value) != 2 or value[0] != "table":
        raise ValueError("Expected a Lua table")
    return value[1]


def integer(value) -> int:
    if type(value) is not float or not 0 <= value <= 0xFFFFFFFF or not value.is_integer():
        raise ValueError("Expected a finite unsigned Lua integer")
    return int(value)


def owner(memory: Memory, actor: int, source_hash: str) -> tuple[int, int]:
    if memory.word(actor) != ACTOR_VTABLE:
        raise ValueError("Actor is not the supported retail LUAX class")
    source, length = memory.word(actor + 0xE0), memory.word(actor + 0xE8)
    if sha256(memory.read(source, length)) != source_hash:
        raise ValueError("Actor Lua source does not match this probe")
    wrapper = memory.word(actor + 0xD0)
    state = memory.word(wrapper)
    if memory.word(state + 0x5C) != wrapper or memory.word(state + 0x40) != 5:
        raise ValueError("LuaPlus ownership or global-table tag mismatch")
    globals_table = memory.table(memory.word(state + 0x44))
    return state, table_pointer(globals_table.get("CP3WProbe"))


def probe_snapshot(memory: Memory, table: int) -> dict:
    fields = memory.table(table)
    if integer(fields.get("schema")) != getattr(memory, "schema", 1) or fields.get("available") is not True:
        raise ValueError("Probe is unavailable or has an unknown schema")
    sequence = integer(fields.get("sequence"))
    if sequence != integer(fields.get("snapshots")) + integer(fields.get("failures")):
        raise ValueError("Probe publication is in progress")
    names = getattr(memory, "names", ITEMS)
    if memory.array(table_pointer(fields.get("items")), len(names)) != list(names):
        raise ValueError("Probe item names or order mismatch")
    records = {}
    for name, value in zip(names, memory.array(table_pointer(fields.get("records")), len(names)), strict=True):
        record = memory.table(table_pointer(value))
        records[name] = {key: integer(record.get(key)) for key in ("amount", "capacity")}
    result = {"sequence": sequence, "records": records, "failures": integer(fields.get("failures"))}
    if "change_count" in fields:
        result["change_count"] = integer(fields["change_count"])
        if type(fields.get("changed")) is not bool or fields["changed"] != (result["change_count"] > 0):
            raise ValueError("Inconsistent probe change diagnostics")
        result["changed"] = fields["changed"]
    if getattr(memory, "location_profile", None) is not None:
        location = memory.table(table_pointer(fields.get("location")))
        if type(location.get("available")) is not bool:
            raise ValueError("Invalid Lua location availability")
        if location["available"]:
            for key in ("world_id", "area_id", "internal_id"):
                value = location.get(key)
                if not isinstance(value, str) or len(value) != 16 or any(c not in "0123456789abcdef" for c in value):
                    raise ValueError("Invalid Lua location ID")
            location["area_index"] = integer(location.get("area_index"))
            if location["area_index"] >= 512:
                raise ValueError("Invalid Lua location index")
        elif set(location) != {"available"}:
            raise ValueError("Unavailable Lua location retains stale fields")
        result["location"] = location
        result["location_changes"] = integer(fields.get("location_changes"))
    if getattr(memory, "grant_profile", None) is not None:
        status = fields.get("grant_status")
        if not isinstance(status, str) or status not in {
            "WAITING",
            "GRANTED",
            "ALREADY_GRANTED",
            "FAILED",
            "INELIGIBLE",
        }:
            raise ValueError("Unknown test grant status")
        result["grant_status"] = status
        result["grant_attempts"] = integer(fields.get("grant_attempts"))
    return result


def native_snapshot(memory: Memory) -> dict:
    game = memory.word(GAME_STATE_POINTER)
    player = memory.word(game + 0x24)
    records = {}
    for name, item_id in zip(getattr(memory, "names", ITEMS), getattr(memory, "item_ids", ITEM_IDS), strict=True):
        amount, capacity = struct.unpack(">II", memory.read(player + 0x54 + item_id * 12, 8))
        records[name] = {"amount": amount, "capacity": capacity}
    health = struct.unpack(">f", memory.read(player + 0xC, 4))[0]
    per_tank = struct.unpack(">f", memory.read(RETAIL_R2 - 0x5F50, 4))[0]
    base = struct.unpack(">f", memory.read(RETAIL_R2 - 0x5F54, 4))[0]
    records["Energy"] = {
        "amount": math.trunc(health),
        "capacity": math.trunc(base + per_tank * memory.word(player + 0x144)),
    }
    return {"game_state": game, "player_state": player, "world_id": memory.read(game + 8, 8).hex(), "records": records}


def collect(memory: Memory, actor: int, source_hash: str) -> dict:
    state, table = owner(memory, actor, source_hash)
    profile = getattr(memory, "location_profile", None)
    location_before = native_location(memory, profile) if profile is not None else None
    native_before = native_snapshot(memory)
    first = probe_snapshot(memory, table)
    native = native_snapshot(memory)
    second = probe_snapshot(memory, table)
    location_after = native_location(memory, profile) if profile is not None else None
    if first != second or native_before != native or owner(memory, actor, source_hash) != (state, table):
        raise DeferredSample("Concurrent game, actor, or Lua snapshot change")
    if first["records"] != native["records"]:
        raise DeferredSample("Lua sample has not converged with current native inventory")
    if profile is not None and (location_before != location_after or first["location"] != location_after):
        raise DeferredSample("Lua sample has not converged with current native location")
    extra = {}
    if getattr(memory, "grant_profile", None) is not None:
        receipt_address = memory.bridge_profile["mutable_receipt_address"]
        receipt = memory.read(receipt_address, 32)
        if receipt != memory.read(receipt_address, 32):
            raise DeferredSample("Concurrent grant receipt change")
        words = struct.unpack(">8I", receipt)
        if words[0] != 0x47525031 or words[1] not in {0, 2, 3}:
            raise DeferredSample("Test grant is in progress or has an invalid receipt")
        extra["grant_receipt"] = list(words)
    return {
        **first,
        "actor": actor,
        "actor_id": memory.word(actor + 8),
        "lua_state": state,
        "probe_table": table,
        "native_records": native["records"],
        "native_parity": True,
        "world_id": native["world_id"],
        "wall_time": time.time(),
        "observation": "double_collected_quiescent",
        **({"native_location": location_after, "location_parity": True} if profile is not None else {}),
        **extra,
    }


def native_location(memory: Memory, profile: dict) -> dict:
    try:
        native = importlib.import_module("nullphaze_network.prime3_lua_service.location").collect(memory, profile)
    except DeferredSample:
        raise
    except ValueError:
        return {"available": False}
    return {
        "available": True,
        "world_id": native["world_id"],
        "area_id": native["area_id"],
        "internal_id": native["area_internal_id"],
        "area_index": native["area_index"],
    }


def capture_running(deadline: float, stop_file: Path | None) -> bool:
    return time.monotonic() < deadline and (stop_file is None or not stop_file.exists())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build", type=Path, required=True)
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--seconds", type=int, default=60)
    parser.add_argument("--stop-file", type=Path, help="Stop cleanly when this initially absent host marker appears")
    args = parser.parse_args()
    if not 1 <= args.seconds <= 3600:
        parser.error("--seconds must be between 1 and 3600")
    if args.stop_file is not None and (args.stop_file.exists() or args.stop_file.resolve() == args.output.resolve()):
        parser.error("--stop-file must be absent and different from --output")
    manifest = json.loads((args.build / "build.json").read_text(encoding="utf-8"))
    image = verify_image(args.build.resolve(), manifest)
    launch = json.loads((args.run / "launch.json").read_text(encoding="utf-8"))
    psutil = importlib.import_module("psutil")
    processes = [p for p in psutil.process_iter(["name", "cmdline"]) if (p.info["name"] or "").lower() == "dolphin.exe"]
    if len(processes) != 1 or processes[0].pid != launch["pid"] or str(image) not in processes[0].cmdline():
        raise ValueError("Exactly the recorded Dolphin/image process must be running")
    engine = importlib.import_module("dolphin_memory_engine")
    engine.hook()
    memory = Memory(engine.read_bytes, manifest=manifest)
    code_verified = memory.location_profile is None
    deadline = time.monotonic() + args.seconds
    actor = None
    previous = None
    count = 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with args.output.open("x", encoding="utf-8") as log:
            log.write(
                json.dumps(
                    {
                        "kind": "capture_start",
                        "platform": "dolphin",
                        "method": "passive_read_only",
                        "probe_id": manifest["probe_id"],
                        "lua_source_sha256": manifest["lua_source_sha256"],
                        "image_sha256": manifest["image"]["sha256"],
                        "image_parts": manifest["image"]["parts"],
                    }
                )
                + "\n"
            )
            while capture_running(deadline, args.stop_file):
                try:
                    if not code_verified:
                        importlib.import_module("nullphaze_network.prime3_lua_service.location").verify_native_code(
                            memory, memory.location_profile
                        )
                        bridge = manifest["lua_location_bridge"]
                        if memory.region_sha256(bridge["address"], bridge.get("immutable_size", bridge["size"])) != (
                            bridge.get("immutable_sha256", bridge["binary_sha256"])
                        ):
                            raise ValueError("Live bridge code does not match the build")
                        if memory.word(bridge["hook"]["address"]) != bridge["hook"]["replacement_word"]:
                            raise ValueError("Live bridge registration hook mismatch")
                        code_verified = True
                    if actor is None:
                        # One bulk MEM1 discovery scan; all subsequent reads are bounded.
                        data = engine.read_bytes(0x80000000, 0x1800000)
                        candidates = []
                        offset = data.find(ACTOR_VTABLE.to_bytes(4, "big"))
                        while offset >= 0:
                            candidate = 0x80000000 + offset
                            if offset % 4 == 0:
                                try:
                                    owner(memory, candidate, manifest["lua_source_sha256"])
                                    candidates.append(candidate)
                                except (ValueError, RuntimeError):
                                    pass
                            offset = data.find(ACTOR_VTABLE.to_bytes(4, "big"), offset + 4)
                        if len(candidates) != 1:
                            raise ValueError("Expected exactly one source-matched live probe actor")
                        actor = candidates[0]
                    row = collect(memory, actor, manifest["lua_source_sha256"])
                    identity = (row["actor"], row["lua_state"], row["probe_table"], row["sequence"])
                    if identity != previous:
                        log.write(json.dumps(row, sort_keys=True) + "\n")
                        previous = identity
                        count += 1
                except (ValueError, RuntimeError) as error:
                    log.write(json.dumps({"kind": "deferred", "reason": str(error), "wall_time": time.time()}) + "\n")
                    if not isinstance(error, DeferredSample):
                        actor = None
                log.flush()
                time.sleep(1)
            log.write(
                json.dumps(
                    {
                        "kind": "capture_end",
                        "snapshots": count,
                        "reason": "stop_file" if args.stop_file is not None and args.stop_file.exists() else "deadline",
                    }
                )
                + "\n"
            )
    finally:
        engine.un_hook()
    print(f"Captured {count} coherent quiescent samples; hardware and atomic snapshot acceptance remain unestablished.")
    if count == 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
