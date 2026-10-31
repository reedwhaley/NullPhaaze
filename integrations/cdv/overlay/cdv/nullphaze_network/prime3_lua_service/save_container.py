# Read-only retail save fingerprints and bounded native persistence evidence. Boundary names
# here: digest, container_layout, inspect_save, analyze, main.
"""Read-only retail save fingerprints and bounded native persistence evidence.

Tag discovery is not a complete container parser or a verified save-slot map.
This tool neither patches saves nor enables game hooks.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import zlib
from pathlib import Path

if __package__ in {None, ""}:
    _repository_root = os.fspath(Path(__file__).resolve().parents[2])
    if _repository_root not in sys.path:
        sys.path.insert(0, _repository_root)

from capstone import CS_ARCH_PPC, CS_MODE_32, CS_MODE_BIG_ENDIAN, Cs

from randovania.games.prime3.exporter.dol_patcher import parse_dol_header
from nullphaze_network.prime3_lua_service.save_profile import profile

WINDOWS = {
    "container_validate": (0x801D5994, 0x801D5A48),
    "game_state_write_window": (0x800B9628, 0x800B9D80),
    "save_manager_io_window": (0x801D5B00, 0x801D6E00),
    "file_io_wrapper_window": (0x803F9FE8, 0x803FA700),
    "slot_buffer_write_and_refresh": (0x801D865C, 0x801D87F8),
    "active_slot_getter": (0x802918D8, 0x802918E0),
    "container_checksum": (0x80344F24, 0x80344FF0),
    "container_header_read_write": (0x801D81D0, 0x801D83C0),
    "slot_input_and_container_loop": (0x801D6D60, 0x801D6F78),
}
SIZE = 0x10000
SYSTEM_SIZE = 0x4A56
SLOT_SIZE = 0x3C86
PAYLOAD_START = 23


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def container_layout(data: bytes) -> dict:
    if len(data) != SIZE:
        raise ValueError("Only the observed 65536-byte retail container is supported")
    if int.from_bytes(data[:4], "big") != zlib.crc32(data[4:]) ^ 0xFFFFFFFF:
        raise ValueError("Retail save checksum mismatch")
    active = int.from_bytes(data[12:16], "big")
    present = list(data[16:19])
    if active not in range(3) or any(flag not in {0, 1} for flag in present):
        raise ValueError("Unsupported active slot or presence flags")
    if data[19:23] != b"SAVH" or data[23:27] != b"SYST":
        raise ValueError("Retail container header/system tag mismatch")
    slots = []
    offset = PAYLOAD_START + SYSTEM_SIZE
    for index, flag in enumerate(present):
        if flag:
            slots.append({"index": index, "offset": offset, "size": SLOT_SIZE})
            offset += SLOT_SIZE
    if offset > len(data):
        raise ValueError("Slot payloads exceed the container")
    return {
        "active_slot_index": active,
        "presence": present,
        "opaque_native_fingerprint": data[4:12].hex(),
        "system_payload_offset": PAYLOAD_START,
        "system_payload_size": SYSTEM_SIZE,
        "slots": slots,
        "serialized_extent": offset,
    }


def inspect_save(data: bytes, layout: dict) -> dict:
    framing = container_layout(data)
    stored = int.from_bytes(data[:4], "big")
    calculated = zlib.crc32(data[4:]) ^ 0xFFFFFFFF
    if stored != calculated:
        raise ValueError("Retail save checksum mismatch")
    bits = "".join(f"{byte:08b}" for byte in data)

    def tag(text: bytes) -> str:
        return "".join(f"{byte:08b}" for byte in text)

    def word(start: int, width: int) -> int:
        return int(bits[start : start + width], 2)

    prefixes = []
    position = bits.find(tag(b"PLST"))
    while position >= 0:
        next_tag = position + layout["following_tag_bit_offset"]
        if bits[position + 96 : position + 128] == tag(b"PRST") and bits[next_tag : next_tag + 32] == tag(b"POWR"):
            records = {}
            for item in layout["saved_fields"]:
                width = item["bits_per_value"]
                amount = word(position + item["amount_bit_offset"], width)
                capacity = word(position + item["capacity_bit_offset"], width)
                if max(amount, capacity) > item["declared_limit"]:
                    raise ValueError("Tagged player inventory exceeds the retail declared limit")
                records[item["name"]] = {"amount": amount, "capacity": capacity}
            slot = next(
                (
                    slot
                    for slot in framing["slots"]
                    if slot["offset"] * 8 <= position and next_tag + 32 <= (slot["offset"] + slot["size"]) * 8
                ),
                None,
            )
            if slot is None:
                raise ValueError("Player prefix is outside a present slot")
            prefixes.append(
                {
                    "bit_offset": position,
                    "byte_offset": position // 8,
                    "bit_in_byte": position % 8,
                    "opaque_player_word": word(position + 32, 32),
                    "health_float_bits": f"{word(position + 64, 32):08x}",
                    "records": records,
                    "slot_index": slot["index"],
                }
            )
        position = bits.find(tag(b"PLST"), position + 1)
    if not prefixes:
        raise ValueError("No structurally matched retail player-state prefix")
    return {
        "size": len(data),
        "sha256": digest(data),
        "stored_checksum": f"{stored:08x}",
        "checksum_matches": True,
        "checksum_formula": "zlib.crc32(bytes[4:]) XOR 0xffffffff, stored big-endian at offset0",
        "player_prefixes": prefixes,
        "container_framing": framing,
        "scope": "outer framing, checksum and tagged prefix only; native commit atomicity unverified",
        "full_container_parse": False,
    }


def analyze(dol: bytes, saves: list[Path], output: Path) -> dict:
    layout = profile(dol)
    if output.exists():
        raise ValueError("Use a new persistence-analysis output directory")
    captured = []
    for source in saves:
        data = source.read_bytes()
        if data != source.read_bytes():
            raise ValueError("Save changed during capture; retry after native save completes")
        captured.append((data, inspect_save(data, layout)))
    output.mkdir(parents=True)
    header = parse_dol_header(dol)
    disassembler = Cs(CS_ARCH_PPC, CS_MODE_32 | CS_MODE_BIG_ENDIAN)
    disassembler.skipdata = True
    evidence = {}
    for name, (start, end) in WINDOWS.items():
        offset = header.offset_for_address(start)
        raw = dol[offset : offset + end - start]
        listing = "\n".join(
            f"{item.address:08x}: {bytes(item.bytes).hex()} {item.mnemonic} {item.op_str}"
            for item in disassembler.disasm(raw, start)
        )
        (output / f"{name}.asm").write_text(listing + "\n", encoding="utf-8")
        evidence[name] = {"start": start, "end": end, "sha256": digest(raw)}
    snapshots = []
    for index, (data, metadata) in enumerate(captured):
        name = f"save-{index}.bin"
        (output / name).write_bytes(data)
        snapshots.append({"snapshot": name, **metadata})
    filename = 0x8057D898
    offset = header.offset_for_address(filename)
    if dol[offset : offset + 9] != b"save.bin\0":
        raise ValueError("Original save filename fingerprint mismatch")
    result = {
        "schema": 1,
        "dol_sha256": digest(dol),
        "windows": evidence,
        "original_save_filename_address": filename,
        "save_filename_pointer_address": 0x80681098,
        "snapshots": snapshots,
        "native_layout": {
            "container_size": SIZE,
            "system_payload_size": 0x4A56,
            "slot_payload_size": 0x3C86,
            "slot_count": 3,
            "manager_size": 0x4AE8,
            "manager_buffer_size_offset": 0x4AD0,
            "manager_buffer_pointer_offset": 0x4AD8,
            "manager_slot_array_offset": 0x4AB4,
            "active_game_slot_index_offset": 0x60,
            "unallocated_extension_bytes_verified": 0,
        },
        "native_save_atomicity_verified": False,
        "production_grants_enabled": False,
        "writes_source": False,
    }
    (output / "analysis.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dol", type=Path, required=True)
    parser.add_argument("--save-file", type=Path, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = analyze(args.source_dol.read_bytes(), args.save_file, args.output)
    print(json.dumps({"snapshots": len(report["snapshots"]), "output": os.fspath(args.output)}, indent=2))


if __name__ == "__main__":
    main()
