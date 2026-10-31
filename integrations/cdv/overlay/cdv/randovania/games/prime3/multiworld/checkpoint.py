# Validate the private save envelope, native payload integrity and slot receipts.
# Persistence and inventory/checkpoint pairing still depend on the game-side coupling hooks.
# Boundary names here: validate.
"""MW01 checkpoint integrity, independent of filesystem and live-game adapters.

This validates the envelope around a native save; it does not parse gameplay
state or migrate single-player saves. Inventory/checkpoint pairing is enforced
by the game-side coupling hooks before encoding.
"""
from __future__ import annotations

import hashlib
import struct
import zlib

MAGIC = b"NPMWSV01"
VERSION = 0x00020058
RETAIL_SIZE = 65536
HEADER_SIZE = 88
RECORD_SIZE = 80
TOTAL_SIZE = HEADER_SIZE + RETAIL_SIZE + 3 * RECORD_SIZE + 4


def validate(data: bytes, profile: bytes) -> None:
    # CRC covers the container; SHA-256 binds its native save payload, and each
    # receipt carries its slot identity. None of those checks proves a pending
    # write completed. The game-side read/coupling path supplies that evidence.
    from randovania.game_connection.prime3_wii_tracker_protocol import validate_profile

    validate_profile(profile)
    if len(data) != TOTAL_SIZE or data[:8] != MAGIC:
        raise ValueError("Not a bound MW01 checkpoint; create a new multiworld save")
    if struct.unpack_from(">II", data, 8) != (VERSION, TOTAL_SIZE) or data[16:48] != profile[:32]:
        raise ValueError("Checkpoint world/seed identity mismatch")
    if struct.unpack_from(">II", data, 48) != (RETAIL_SIZE, 3):
        raise ValueError("Invalid checkpoint section bounds")
    if int.from_bytes(data[-4:], "big") != zlib.crc32(data[:-4]):
        raise ValueError("Checkpoint checksum mismatch")
    retail = data[HEADER_SIZE:HEADER_SIZE + RETAIL_SIZE]
    if (retail[19:27] != b"SAVHSYST" or int.from_bytes(retail[12:16], "big") > 2
            or any(flag not in (0, 1) for flag in retail[16:19])
            or int.from_bytes(retail[:4], "big") ^ 0xffffffff != zlib.crc32(retail[4:])
            or hashlib.sha256(retail).digest() != data[56:88]):
        raise ValueError("Native save payload integrity mismatch")
    for slot in range(3):
        offset = HEADER_SIZE + RETAIL_SIZE + slot * RECORD_SIZE
        record = data[offset:offset + RECORD_SIZE]
        cursor = int.from_bytes(record[20:24], "big")
        if (record[:4] != bytes([slot, 0, 0, 0]) or record[4:20] != profile[32 + slot * 16:48 + slot * 16]
                or not 0 <= cursor <= 256 or (cursor == 0) != (record[24:56] == bytes(32))
                or record[68] & 0xf0 or record[69] & 0xfc or record[70:72] != bytes(2)
                or int.from_bytes(record[72:74], "big") > 255
                or int.from_bytes(record[74:76], "big") > 13 or record[76:80] != bytes(4)
                or (not retail[16 + slot] and (cursor or record[56:] != bytes(24)))):
            raise ValueError(f"Invalid checkpoint receipt in slot {slot + 1}")
