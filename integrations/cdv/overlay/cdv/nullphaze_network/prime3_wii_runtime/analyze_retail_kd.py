# Read-only attribution of the supported retail KD adapters and rejected IP aliases.
# Boundary names here: branch_target, analyze, main.
"""Read-only attribution of the supported retail KD adapters and rejected IP aliases."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import struct
import sys
from pathlib import Path

from capstone import CS_ARCH_PPC, CS_MODE_32, CS_MODE_BIG_ENDIAN, Cs

if __package__ in {None, ""}:
    root = os.fspath(Path(__file__).resolve().parents[2])
    if root not in sys.path:
        sys.path.insert(0, root)

from randovania.games.prime3.exporter.dol_patcher import parse_dol_header
from nullphaze_network.prime3_lua_service.readiness import inspect_retail_contract, validate_kd_contract

FUNCTIONS = {
    "title_nwc24_open_callsite": (0x802C1D50, 0x802C1E04),
    "nwc24_open_entry": (0x8054E390, 0x8054E3B0),
    "nwc24_open_core": (0x8054E3B0, 0x8054E57C),
    "nwc24_close": (0x8054E57C, 0x8054E5E8),
    "scheduler_suspend_refcount": (0x805541B8, 0x80554288),
    "scheduler_suspend_command1": (0x80554920, 0x80554930),
    "scheduler_resume_command3": (0x80554ABC, 0x80554ACC),
    "scheduler_command_core": (0x80554ACC, 0x80554C28),
    "kd_open_adapter": (0x80555CDC, 0x80555D54),
    "kd_close_adapter": (0x80555D54, 0x80555D88),
    "kd_ioctl_sync_adapter": (0x80555D88, 0x80555DD0),
    "kd_ioctl_async_adapter": (0x80555DD0, 0x80555E2C),
    "kd_async_callback": (0x80555E34, 0x80555E50),
    "kd_shutdown_prepare": (0x8055637C, 0x80556424),
    "kd_shutdown_request": (0x80556424, 0x805564F4),
}


def branch_target(address: int, word: int) -> int | None:
    if word >> 26 != 18:
        return None
    delta = word & 0x3FFFFFC
    if delta & 0x2000000:
        delta -= 0x4000000
    return (delta if word & 2 else address + delta) & 0xFFFFFFFF


def analyze(original: bytes) -> dict:
    validate_kd_contract(original)
    header = parse_dol_header(original)
    functions = {}
    for name, (start, end) in FUNCTIONS.items():
        offset = header.offset_for_address(start)
        data = original[offset : offset + end - start]
        calls = []
        for i in range(0, len(data), 4):
            word = struct.unpack_from(">I", data, i)[0]
            target = branch_target(start + i, word)
            if target is not None and (word & 1 or not start <= target < end):
                calls.append({"address": start + i, "target": target, "link": bool(word & 1)})
        functions[name] = {"start": start, "end": end, "sha256": hashlib.sha256(data).hexdigest(), "calls": calls}
    paths = {}
    for path in (b"/dev/net/kd/request", b"/dev/net/ip/top", b"/dev/net/ncd/manage", b"/dev/net/ssl"):
        locations = []
        for section in header.sections:
            if not section.size:
                continue
            data = original[section.file_offset : section.file_offset + section.size]
            offset = data.find(path + b"\0")
            while offset >= 0:
                locations.append(section.address + offset)
                offset = data.find(path + b"\0", offset + 1)
        paths[path.decode()] = locations
    return {
        "schema": 1,
        "input_sha256": hashlib.sha256(original).hexdigest(),
        "read_only": True,
        "functions": functions,
        "literal_paths": paths,
        "rejected_contract": inspect_retail_contract(original),
        "attributed_kd_generic_abi": {
            "open": 0x80555CDC,
            "close": 0x80555D54,
            "ioctl_sync": 0x80555D88,
            "ioctl_async": 0x80555DD0,
            "callback": 0x80555E34,
        },
        "actual_library_open": {
            "address": 0x8054E390,
            "workspace_argument": "r3, nonnull and 32-byte aligned",
            "title_callsite": 0x802C1DA0,
            "title_workspace_allocation": 0x4000,
        },
        "scheduler_commands": {"suspend": 1, "try_suspend": 2, "resume": 3},
        "native_ip_descriptor_attributed": False,
        "absence_scope": "Literal paths only; lack of a literal does not prove absence of indirect or RSO services",
        "next_safe_probe": "Owned KD open plus command6, retaining only that handle; no library, ES/FS or IP calls",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dol", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError("Use a new audit output directory")
    original = args.dol.read_bytes()
    report = analyze(original)
    args.output.mkdir(parents=True)
    (args.output / "audit.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    decoder = Cs(CS_ARCH_PPC, CS_MODE_32 | CS_MODE_BIG_ENDIAN)
    decoder.skipdata = True
    header = parse_dol_header(original)
    for name, (start, end) in FUNCTIONS.items():
        offset = header.offset_for_address(start)
        lines = [
            f"{i.address:08X} {i.bytes.hex()} {i.mnemonic} {i.op_str}"
            for i in decoder.disasm(original[offset : offset + end - start], start)
        ]
        (args.output / f"{name}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    if original != args.dol.read_bytes():
        raise ValueError("Input changed during read-only audit")
    print("Attributed KD adapters; no retail IP descriptor or socket ownership claimed.")


if __name__ == "__main__":
    main()
