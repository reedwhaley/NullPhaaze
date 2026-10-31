# Decode the bounded CP3W envelope and inventory pages with explicit field sizes/checksums.
# Unavailable snapshots cannot retain a stale owner's inventory or location. Boundary names
# here: TrackerProtocolError, RuntimeRequestRejected, validate_profile, request, response.
"""Bounded read-only UDP snapshots, distinct from the retired TCP tracker wire format."""

from __future__ import annotations

import dataclasses
import math
import struct
import uuid
import zlib

HEADER = struct.Struct(">4sBBBBII")
CAPABILITY = 1 << 14
SNAPSHOT_COMMAND = 9
PROFILE_SIZE = 80
TOTAL = 600
PAGE_SIZE = 300


class TrackerProtocolError(ValueError):
    pass


class RuntimeRequestRejected(TrackerProtocolError):
    def __init__(self, status: int):
        super().__init__(f"Runtime rejected tracker request (status {status})")
        self.status = status


def validate_profile(profile: bytes) -> None:
    if len(profile) != PROFILE_SIZE or not any(profile[:16]) or not any(profile[16:32]):
        raise TrackerProtocolError("Expected a bound campaign and checkpoint profile")
    lineage = uuid.UUID(bytes=profile[16:32])
    if profile[32:] != b"".join(uuid.uuid5(lineage, f"CP3W slot {i}").bytes for i in range(3)):
        raise TrackerProtocolError("Invalid checkpoint slot identities")


def request(command: int, request_id: int, payload: bytes = b"") -> bytes:
    if command not in (1, 3, 4, SNAPSHOT_COMMAND):
        raise TrackerProtocolError("Tracker cannot send this command")
    raw = HEADER.pack(b"CP3W", 1, 1, command, 0, request_id, len(payload)) + payload
    return raw + struct.pack(">I", zlib.crc32(raw))


def response(raw: bytes, command: int, request_id: int) -> bytes:
    if not 20 <= len(raw) <= 512:
        raise TrackerProtocolError("Invalid datagram size")
    magic, version, kind, actual_command, status, actual_id, size = HEADER.unpack_from(raw)
    if (magic, version, kind, actual_command, actual_id) != (b"CP3W", 1, 2, command, request_id):
        raise TrackerProtocolError("Mismatched response envelope")
    if size != len(raw) - 20 or struct.unpack(">I", raw[-4:])[0] != zlib.crc32(raw[:-4]):
        raise TrackerProtocolError("Invalid datagram length or checksum")
    if status != 0:
        if status != 1 or size < 6:
            raise TrackerProtocolError("Malformed runtime error response")
        code, rejected_command, message_size = struct.unpack_from(">HHH", raw, 16)
        if rejected_command != command or message_size != size - 6:
            raise TrackerProtocolError("Malformed runtime error response")
        raise RuntimeRequestRejected(code)
    return raw[16:-4]


@dataclasses.dataclass(frozen=True)
class Snapshot:
    available: bool
    world: int = 0
    area: int = 0
    internal_area: int = 0
    area_index: int = 0
    health: float = 0
    records: tuple[tuple[int, int], ...] = ()

    @classmethod
    def decode(cls, raw: bytes) -> Snapshot:
        if len(raw) != TOTAL:
            raise TrackerProtocolError("Incomplete snapshot")
        magic, available, world, area, internal, index, health = struct.unpack_from(">IIQQQIf", raw)
        if magic != 0x54524B31 or available not in (0, 1):
            raise TrackerProtocolError("Unsupported snapshot schema")
        if not available:
            if any(raw[8:]):
                raise TrackerProtocolError("Unavailable snapshot contains stale state")
            return cls(False)
        if world in (0, 2**64 - 1) or area in (0, 2**64 - 1) or index >= 512:
            raise TrackerProtocolError("Invalid location")
        if not math.isfinite(health) or not 0 <= health <= 100000:
            raise TrackerProtocolError("Invalid health")
        records = tuple(struct.iter_unpack(">II", raw[40:]))
        if len(records) != 70:
            raise TrackerProtocolError("Incomplete inventory")
        return cls(True, world, area, internal, index, health, records)


def page(payload: bytes, profile: bytes, session: int, token: int, index: int) -> tuple[int, bytes]:
    if len(payload) != 404 or index not in (0, 1):
        raise TrackerProtocolError("Invalid snapshot page")
    schema, actual_session, actual_token, offset, total, length = struct.unpack_from(">6I", payload)
    if (schema, actual_session, offset, total, length) != (1, session, index * PAGE_SIZE, TOTAL, PAGE_SIZE):
        raise TrackerProtocolError("Inconsistent snapshot page")
    if not actual_token or (token and actual_token != token) or payload[24:104] != profile:
        raise TrackerProtocolError("Snapshot identity changed")
    return actual_token, payload[104:]
