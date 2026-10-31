# Experimental offline networking-save container; NOT wired into the game. Boundary names
# here: Receipt, Checkpoint, slot_identity, bound_profile, validate_profile.
"""Experimental offline networking-save container; NOT wired into the game.

The embedded retail checkpoint and per-slot cursors are one checksummed file.
This codec does not establish native save atomicity, grant/receipt consistency,
authentication, or production suitability.
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import os
import struct
import sys
import uuid
import zlib
from pathlib import Path

if __package__ in {None, ""}:
    _repository_root = os.fspath(Path(__file__).resolve().parents[2])
    if _repository_root not in sys.path:
        sys.path.insert(0, _repository_root)

from nullphaze_network.prime3_lua_service.save_container import SIZE, container_layout, inspect_save
from nullphaze_network.prime3_lua_service.save_profile import profile

MAGIC = b"CP3WNSV1"
VERSION = 1
HEADER = struct.Struct(">8sHHI16s16sII32s")
RECORD = struct.Struct(">B3s16sI32s")
TOTAL_SIZE = HEADER.size + SIZE + 3 * RECORD.size + 4
ZERO_HASH = bytes(32)


@dataclasses.dataclass(frozen=True)
class Receipt:
    slot: int
    identity: uuid.UUID
    cursor: int = 0
    history_digest: bytes = ZERO_HASH


@dataclasses.dataclass(frozen=True)
class Checkpoint:
    campaign: uuid.UUID
    lineage: uuid.UUID
    retail: bytes
    receipts: tuple[Receipt, ...]


def slot_identity(lineage: uuid.UUID, slot: int) -> uuid.UUID:
    return uuid.uuid5(lineage, f"CP3W slot {slot}")


def bound_profile(checkpoint: Checkpoint) -> bytes:
    return (
        checkpoint.campaign.bytes + checkpoint.lineage.bytes + b"".join(r.identity.bytes for r in checkpoint.receipts)
    )


def validate_profile(profile: bytes) -> None:
    if len(profile) != 80 or not any(profile[:16]) or not any(profile[16:32]):
        raise ValueError("Expected nonzero campaign, lineage and three bound slot identities")
    lineage = uuid.UUID(bytes=profile[16:32])
    if profile[32:] != b"".join(slot_identity(lineage, index).bytes for index in range(3)):
        raise ValueError("Networking profile slot identities do not match lineage")


def validate(checkpoint: Checkpoint) -> None:
    framing = container_layout(checkpoint.retail)
    if checkpoint.campaign.int == 0 or checkpoint.lineage.int == 0:
        raise ValueError("Campaign and save lineage must be explicit nonzero UUIDs")
    if len(checkpoint.receipts) != 3:
        raise ValueError("Exactly three ordered slot receipts required")
    for index, receipt in enumerate(checkpoint.receipts):
        if type(receipt.slot) is not int or receipt.slot != index:
            raise ValueError("Receipt slot order mismatch")
        if receipt.identity != slot_identity(checkpoint.lineage, index):
            raise ValueError("Receipt identity does not match save lineage and slot")
        if type(receipt.cursor) is not int or not 0 <= receipt.cursor <= 0xFFFFFFFF:
            raise ValueError("Delivery cursor is outside uint32 range")
        if not isinstance(receipt.history_digest, bytes) or len(receipt.history_digest) != 32:
            raise ValueError("History digest must be exactly 32 bytes")
        if (receipt.cursor == 0) != (receipt.history_digest == ZERO_HASH):
            raise ValueError("History digest and zero cursor disagree")
        if not framing["presence"][index] and receipt.cursor:
            raise ValueError("Absent slot cannot have delivered items")


def encode(checkpoint: Checkpoint) -> bytes:
    validate(checkpoint)
    header = HEADER.pack(
        MAGIC,
        VERSION,
        HEADER.size,
        TOTAL_SIZE,
        checkpoint.campaign.bytes,
        checkpoint.lineage.bytes,
        SIZE,
        3,
        hashlib.sha256(checkpoint.retail).digest(),
    )
    records = b"".join(
        RECORD.pack(receipt.slot, bytes(3), receipt.identity.bytes, receipt.cursor, receipt.history_digest)
        for receipt in checkpoint.receipts
    )
    payload = header + checkpoint.retail + records
    return payload + struct.pack(">I", zlib.crc32(payload))


def decode(data: bytes) -> Checkpoint:
    if len(data) != TOTAL_SIZE:
        raise ValueError("Networking-save length mismatch")
    if zlib.crc32(data[:-4]) != int.from_bytes(data[-4:], "big"):
        raise ValueError("Networking-save checksum mismatch")
    magic, version, header_size, size, campaign, lineage, retail_size, count, retail_hash = HEADER.unpack_from(data)
    if (magic, version, header_size, size, retail_size, count) != (MAGIC, VERSION, HEADER.size, TOTAL_SIZE, SIZE, 3):
        raise ValueError("Unsupported networking-save schema or dimensions")
    retail = data[HEADER.size : HEADER.size + SIZE]
    if hashlib.sha256(retail).digest() != retail_hash:
        raise ValueError("Embedded retail checkpoint digest mismatch")
    receipts = []
    for index in range(3):
        slot, reserved, identity, cursor, history = RECORD.unpack_from(data, HEADER.size + SIZE + index * RECORD.size)
        if reserved != bytes(3):
            raise ValueError("Nonzero reserved receipt bytes")
        receipts.append(Receipt(slot, uuid.UUID(bytes=identity), cursor, history))
    checkpoint = Checkpoint(uuid.UUID(bytes=campaign), uuid.UUID(bytes=lineage), retail, tuple(receipts))
    validate(checkpoint)
    return checkpoint


def migrate(source: Path, dol: bytes, output: Path, campaign: uuid.UUID, lineage: uuid.UUID) -> dict:
    source, output = source.resolve(), output.resolve()
    if output.exists() or source.parent == output or source.parent in output.parents or output in source.parents:
        raise ValueError("Use a new migration directory disjoint from the source profile")
    layout = profile(dol)
    original = source.read_bytes()
    if original != source.read_bytes():
        raise ValueError("Source changed during migration capture")
    inspected = inspect_save(original, layout)
    checkpoint = Checkpoint(
        campaign, lineage, original, tuple(Receipt(index, slot_identity(lineage, index)) for index in range(3))
    )
    encoded = encode(checkpoint)
    if decode(encoded) != checkpoint:
        raise ValueError("Networking-save round trip failed")
    output.mkdir(parents=True)
    for name, data in (("legacy-save.bin", original), ("save.cp3w", encoded)):
        with (output / name).open("xb") as stream:
            stream.write(data)
    report = {
        "schema": 1,
        "status": "experimental_offline_migration_not_game_loadable",
        "campaign_id": str(campaign),
        "save_lineage": str(lineage),
        "source_sha256": inspected["sha256"],
        "backup": "legacy-save.bin",
        "networking_save": "save.cp3w",
        "networking_save_sha256": hashlib.sha256(encoded).hexdigest(),
        "networking_save_bytes": len(encoded),
        "embedded_retail_unchanged": decode(encoded).retail == original,
        "receipts_initialized_to_zero": True,
        "present_slots": inspected["container_framing"]["presence"],
        "native_integrated": False,
        "native_atomicity_verified": False,
        "source_modified": False,
        "production_grants_enabled": False,
        "warning": "Do not install this experimental file on a console or rename it to save.bin",
    }
    with (output / "migration.json").open("x", encoding="utf-8") as stream:
        json.dump(report, stream, indent=2, sort_keys=True)
        stream.write("\n")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-save", type=Path, required=True)
    parser.add_argument("--source-dol", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--campaign-id", type=uuid.UUID, required=True)
    parser.add_argument("--save-lineage", type=uuid.UUID, required=True)
    parser.add_argument("--experimental-offline-migration", action="store_true", required=True)
    args = parser.parse_args()
    print(
        json.dumps(
            migrate(args.source_save, args.source_dol.read_bytes(), args.output, args.campaign_id, args.save_lineage),
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
