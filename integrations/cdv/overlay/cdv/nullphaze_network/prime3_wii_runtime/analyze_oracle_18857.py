#!/usr/bin/env python3
# Recover static evidence from the known-good 18857 injected DOL section. Boundary names
# here: branch_target, strings, main.
"""Recover static evidence from the known-good 18857 injected DOL section.

This is deliberately an offline reverse-engineering aid.  It neither patches a
DOL nor executes the extracted PowerPC payload.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import struct
from collections import Counter
from pathlib import Path

from capstone import CS_ARCH_PPC, CS_MODE_32, CS_MODE_BIG_ENDIAN, Cs

TEXT2_ADDRESS = 0x806843C0
TEXT2_SIZE = 0xB000
RUNTIME_OFFSET = 0x200
RUNTIME_ADDRESS = 0x817E1000
RETAIL_VENEERS = {
    0x80504668: "IOS_OpenAsync",
    0x805048A0: "IOS_CloseAsync",
    0x80504FE0: "IOS_IoctlAsync",
    0x80505384: "IOS_IoctlvAsync",
}


def branch_target(word: int, address: int) -> int | None:
    # PPC opcode 18.  AA=0 in both installed DOL hook branches.
    if word >> 26 != 18:
        return None
    displacement = word & 0x03FFFFFC
    if displacement & 0x02000000:
        displacement -= 0x04000000
    return displacement if word & 2 else (address + displacement) & 0xFFFFFFFF


def strings(data: bytes, base: int) -> list[tuple[int, str]]:
    result = []
    start = None
    for index, value in enumerate(data + b"\0"):
        if 0x20 <= value < 0x7F:
            if start is None:
                start = index
        elif start is not None:
            if index - start >= 4:
                result.append((base + start, data[start:index].decode("ascii")))
            start = None
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("dol", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    dol = args.dol.read_bytes()
    # DOL text section index 2 is the oracle's appended injected section.
    offsets = struct.unpack(">7I", dol[:0x1C])
    addresses = struct.unpack(">7I", dol[0x48:0x64])
    sizes = struct.unpack(">7I", dol[0x90:0xAC])
    index = next(
        i for i, (address, size) in enumerate(zip(addresses, sizes)) if address == TEXT2_ADDRESS and size == TEXT2_SIZE
    )
    raw = dol[offsets[index] : offsets[index] + sizes[index]]
    (args.output / "oracle_text2_806843c0.bin").write_bytes(raw)
    runtime = raw[RUNTIME_OFFSET:]
    md = Cs(CS_ARCH_PPC, CS_MODE_32 | CS_MODE_BIG_ENDIAN)
    md.detail = True
    instructions = list(md.disasm(runtime, RUNTIME_ADDRESS))
    branches: list[dict[str, str]] = []
    calls: list[dict[str, str]] = []
    memory: list[dict[str, str]] = []
    targets: Counter[int] = Counter()
    function_entries = {RUNTIME_ADDRESS}
    for instruction in instructions:
        mnemonic = instruction.mnemonic
        op = instruction.op_str
        if mnemonic.startswith("b"):
            target = None
            if op.startswith("0x"):
                target = int(op.split()[0], 16)
            branches.append(
                {
                    "address": f"0x{instruction.address:08X}",
                    "bytes": instruction.bytes.hex(),
                    "mnemonic": mnemonic,
                    "operand": op,
                    "target": "" if target is None else f"0x{target:08X}",
                }
            )
            if target is not None:
                targets[target] += 1
                if mnemonic in {"bl", "bla"} and RUNTIME_ADDRESS <= target < RUNTIME_ADDRESS + len(runtime):
                    function_entries.add(target)
        # Identify direct absolute retail veneer materialization in the three
        # instruction pattern: lis r12, high; ori r12, r12, low; mtctr r12; bctrl.
        if mnemonic in {"lwz", "stw", "lbz", "stb", "lhz", "sth", "lwzu", "stwu"} and "0x817e" in op.lower():
            memory.append(
                {
                    "address": f"0x{instruction.address:08X}",
                    "bytes": instruction.bytes.hex(),
                    "instruction": f"{mnemonic} {op}",
                    "kind": "runtime-state absolute",
                }
            )

    for pos in range(len(instructions) - 3):
        a, b, c, d = instructions[pos : pos + 4]
        if a.mnemonic == "lis" and b.mnemonic == "ori" and c.mnemonic == "mtctr" and d.mnemonic == "bctrl":
            # Capstone prints signed immediates for lis. Use raw words to avoid
            # presentation ambiguity.
            aword = int.from_bytes(a.bytes, "big")
            bword = int.from_bytes(b.bytes, "big")
            register_a = (aword >> 21) & 31
            register_b_dst = (bword >> 21) & 31
            register_b_src = (bword >> 16) & 31
            ctr_reg = (int.from_bytes(c.bytes, "big") >> 21) & 31
            if register_a == register_b_dst == register_b_src == ctr_reg:
                target = ((aword & 0xFFFF) << 16) | (bword & 0xFFFF)
                if target in RETAIL_VENEERS:
                    calls.append(
                        {
                            "callsite": f"0x{d.address:08X}",
                            "materialization": f"0x{a.address:08X}-0x{c.address:08X}",
                            "target": f"0x{target:08X}",
                            "name": RETAIL_VENEERS[target],
                        }
                    )

    with (args.output / "oracle_text2_disassembly.txt").open("w", encoding="ascii", newline="\n") as stream:
        stream.write(f"# text2 {TEXT2_ADDRESS:08X}-{TEXT2_ADDRESS + len(raw):08X}\n")
        stream.write(f"# relocated runtime {RUNTIME_ADDRESS:08X}-{RUNTIME_ADDRESS + len(runtime):08X}\n")
        for instruction in instructions:
            stream.write(
                f"{instruction.address:08X}: {instruction.bytes.hex():<8} "
                f"{instruction.mnemonic:<10} {instruction.op_str}\n"
            )
    tables = (
        ("oracle_branch_targets.csv", branches),
        ("oracle_ios_calls.csv", calls),
        ("oracle_state_accesses.csv", memory),
    )
    for name, rows in tables:
        with (args.output / name).open("w", encoding="ascii", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=rows[0].keys() if rows else ["none"])
            writer.writeheader()
            writer.writerows(rows)
    with (args.output / "oracle_strings.csv").open("w", encoding="ascii", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(("address", "string"))
        writer.writerows((f"0x{address:08X}", value) for address, value in strings(runtime, RUNTIME_ADDRESS))
    with (args.output / "oracle_function_candidates.csv").open("w", encoding="ascii", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(("address", "source", "inbound_direct_branches"))
        for address in sorted(function_entries):
            source = "runtime entry" if address == RUNTIME_ADDRESS else "bl target"
            writer.writerow((f"0x{address:08X}", source, targets[address]))
    with (args.output / "oracle_cfg.dot").open("w", encoding="ascii", newline="\n") as stream:
        stream.write("digraph oracle {\n")
        for row in branches:
            if row["target"]:
                stream.write(f'  "{row["address"]}" -> "{row["target"]}" [label="{row["mnemonic"]}"];\n')
        stream.write("}\n")
    entry_word = struct.unpack(">I", dol[0x20:0x24])[0]  # only documentary fallback below
    report = args.output / "oracle_analysis_summary.txt"
    report.write_text(
        "\n".join(
            [
                f"oracle_dol_sha256={hashlib.sha256(dol).hexdigest()}",
                f"text2_file_offset=0x{offsets[index]:X}",
                f"text2_sha256={hashlib.sha256(raw).hexdigest()}",
                f"runtime_offset=0x{RUNTIME_OFFSET:X}",
                f"runtime_size=0x{len(runtime):X}",
                f"runtime_sha256={hashlib.sha256(runtime).hexdigest()}",
                f"direct_retail_veneer_calls={len(calls)}",
                f"branch_records={len(branches)}",
                f"function_candidates={len(function_entries)}",
                f"dol_header_word_20=0x{entry_word:08X}",
            ]
        )
        + "\n",
        encoding="ascii",
    )


if __name__ == "__main__":
    main()
