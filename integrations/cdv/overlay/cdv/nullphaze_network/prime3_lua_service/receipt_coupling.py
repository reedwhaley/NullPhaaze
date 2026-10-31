# Opt-in synthetic-receipt checkpoint coupling experiment; never enables grants. Boundary
# names here: decode_state, seed, main.
"""Opt-in synthetic-receipt checkpoint coupling experiment; never enables grants."""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import os
import struct
import sys
import uuid
from pathlib import Path

if __package__ in {None, ""}:
    _repository_root = os.fspath(Path(__file__).resolve().parents[2])
    if _repository_root not in sys.path:
        sys.path.insert(0, _repository_root)

from nullphaze_network.prime3_lua_service import network_save
from nullphaze_network.prime3_lua_service.save_container import container_layout

DESTRUCTORS = (
    0x801D5E94,
    0x801D6E40,
    0x801D6E88,
    0x801D6ED0,
    0x801D6F18,
    0x801D6FD8,
    0x801D7024,
    0x801D72A8,
    0x801D72F4,
    0x801D7584,
    0x801D75D0,
    0x801D7690,
    0x801D76DC,
    0x801D7C3C,
    0x801D7D9C,
    0x801D7DE4,
    0x801D7E38,
    0x801D7E80,
    0x801D7F30,
    0x801D7F7C,
    0x801D8620,
    0x801D8758,
    0x802EE66C,
    0x802EEC1C,
    0x802F0BC0,
)
HOOKS = (
    (0x801D8610, 0x800B76C4, "coupling_load_construct"),
    (0x801D8748, 0x800B76C4, "coupling_clone_construct"),
    (0x802EFB28, 0x800BAC68, "coupling_copy_vectors"),
    *((a, 0x801D84DC, "save_trace_slot_load") for a in (0x801D7250, 0x801D7D54)),
    *(
        (a, 0x801D8790, "save_trace_snapshot_stored")
        for a in (0x801D6344, 0x801D63AC, 0x801D721C, 0x801D7C60, 0x801D84C0)
    ),
    *((a, 0x800BADDC, "coupling_transfer") for a in (0x801D6354, 0x801D63BC, 0x801D7C70)),
    *((a, 0x800B87CC, "coupling_destroy") for a in DESTRUCTORS),
)
STATE_SIZE = 4500


def decode_state(raw: bytes) -> dict:
    if len(raw) != STATE_SIZE:
        raise ValueError("Invalid coupling state length")
    words = struct.unpack_from(">9I", raw)
    if words[0] != 0x43505231:
        raise ValueError("Unknown coupling state")

    def receipt(offset):
        slot, reserved, identity, cursor, history = network_save.RECORD.unpack_from(raw, offset)
        if reserved != bytes(3) or slot >= 3 or (cursor == 0) != (history == bytes(32)):
            raise ValueError("Invalid receipt record")
        return {
            "slot": slot,
            "identity": str(uuid.UUID(bytes=identity)),
            "cursor": cursor,
            "history_digest": history.hex(),
        }

    def view(offset):
        flag = struct.unpack_from(">I", raw, offset)[0]
        if flag not in {0, 1}:
            raise ValueError("Invalid receipt view validity")
        return None if not flag else {"sha256": raw[offset + 4 : offset + 36].hex(), "receipt": receipt(offset + 36)}

    owners = []
    for i in range(8):
        offset = 1012 + 436 * i
        game, generation, slot = struct.unpack_from(">3I", raw, offset)
        if not game:
            continue
        if slot >= 3 or not generation:
            raise ValueError("Invalid receipt owner")
        owners.append(
            {
                "game": game,
                "generation": generation,
                "slot": slot,
                "current": receipt(offset + 12),
                "vectors": [view(offset + 68 + 92 * j) for j in range(4)],
            }
        )
    return {
        "fault": words[1],
        "epoch": words[2],
        "generation": words[3],
        "ticks": words[7],
        "test_stage": words[8],
        "owners": owners,
        "disk": [view(92 + 92 * i) for i in range(3)],
        "stored": [view(368 + 92 * i) for i in range(3)],
        "pending": [view(644 + 92 * i) for i in range(4)],
    }


def seed(source: Path, output: Path) -> dict:
    source, output = source.resolve(), output.resolve()
    if output.exists() or source == output or source in output.parents:
        raise ValueError("Use a new synthetic fixture directory")
    raw = source.read_bytes()
    checkpoint = network_save.decode(raw)
    lineage = uuid.uuid4()
    present = {s["index"] for s in container_layout(checkpoint.retail)["slots"]}
    receipts = tuple(
        network_save.Receipt(
            i,
            network_save.slot_identity(lineage, i),
            0x101 if i in present else 0,
            b"\x11" * 32 if i in present else bytes(32),
        )
        for i in range(3)
    )
    value = dataclasses.replace(checkpoint, campaign=uuid.uuid4(), lineage=lineage, receipts=receipts)
    wire = network_save.encode(value)
    output.mkdir(parents=True)
    (output / "input.cp3w").write_bytes(raw)
    (output / "synthetic.cp3w").write_bytes(wire)
    (output / "profile.bin").write_bytes(network_save.bound_profile(value))
    report = {
        "synthetic_only": True,
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "fixture_sha256": hashlib.sha256(wire).hexdigest(),
        "retail_payload_unchanged": True,
        "profile_hex": network_save.bound_profile(value).hex(),
        "cursor": 0x101,
        "production_grants_enabled": False,
    }
    (output / "fixture.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed-from", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(seed(args.seed_from, args.output), indent=2))


if __name__ == "__main__":
    main()
