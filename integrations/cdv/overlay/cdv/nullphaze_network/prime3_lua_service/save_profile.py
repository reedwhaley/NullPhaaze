# Read-only evidence for the retail player-state inventory save prefix. Boundary names here:
# profile, analyze, main.
"""Read-only evidence for the retail player-state inventory save prefix.

This is not a save.bin parser, save writer, or approved receipt allocation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

if __package__ in {None, ""}:
    _repository_root = os.fspath(Path(__file__).resolve().parents[2])
    if _repository_root not in sys.path:
        sys.path.insert(0, _repository_root)

from capstone import CS_ARCH_PPC, CS_MODE_32, CS_MODE_BIG_ENDIAN, Cs

from randovania.games.prime3.exporter.dol_patcher import parse_dol_header
from nullphaze_network.prime3_lua_service.inventory_profile import extract_profile

WINDOWS = {
    "save_prefix": (0x80190E74, 0x80190F58),
    "inventory_read_and_following_word": (0x80190B94, 0x80190C34),
    "declared_limit_bit_width": (0x8018F320, 0x8018F340),
    "bitstream_write": (0x8038FB58, 0x8038FC58),
}


def profile(dol: bytes) -> dict:
    inventory = extract_profile(dol)
    header = parse_dol_header(dol)
    fields = []
    skipped = []
    bit_offset = 128  # PLST tag, player+4, health bits, PRST tag.
    for item in inventory["items"]:
        if not item["flags"] & 0x80000000:
            skipped.append({"id": item["id"], "name": item["name"], "restored_amount_capacity": [0, 0]})
            continue
        width = item["declared_limit"].bit_length()
        fields.append(
            {
                **item,
                "bits_per_value": width,
                "amount_bit_offset": bit_offset,
                "capacity_bit_offset": bit_offset + width,
            }
        )
        bit_offset += 2 * width
    windows = {}
    for name, (start, end) in WINDOWS.items():
        raw = dol[header.offset_for_address(start) : header.offset_for_address(start) + end - start]
        windows[name] = {"start": start, "end": end, "sha256": hashlib.sha256(raw).hexdigest()}
    return {
        "schema": 1,
        "dol_sha256": inventory["dol_sha256"],
        "table_sha256": inventory["table_sha256"],
        "scope": "player-state prefix bit offsets only; not disk offsets or complete save format",
        "prefix_words": ["PLST", "player_state+4", "health_float_bits", "PRST"],
        "saved_fields": fields,
        "not_serialized_fields": skipped,
        "following_tag": "POWR",
        "following_tag_bit_offset": bit_offset,
        "alignment_padding_before_following_tag_bits": 0,
        "windows": windows,
        "approved_receipt_storage": None,
        "full_save_integrity_or_atomicity_verified": False,
        "hardware_verified": False,
        "production_grants_enabled": False,
    }


def analyze(dol: bytes, output: Path) -> dict:
    result = profile(dol)
    if output.exists():
        raise ValueError("Use a new save-analysis directory")
    output.mkdir(parents=True)
    header = parse_dol_header(dol)
    disassembler = Cs(CS_ARCH_PPC, CS_MODE_32 | CS_MODE_BIG_ENDIAN)
    disassembler.skipdata = True
    for name, (start, end) in WINDOWS.items():
        offset = header.offset_for_address(start)
        listing = "\n".join(
            f"{item.address:08x}: {bytes(item.bytes).hex()} {item.mnemonic} {item.op_str}"
            for item in disassembler.disasm(dol[offset : offset + end - start], start)
        )
        (output / f"{name}.asm").write_text(listing + "\n", encoding="utf-8")
    (output / "analysis.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dol", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = analyze(args.source_dol.read_bytes(), args.output)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
