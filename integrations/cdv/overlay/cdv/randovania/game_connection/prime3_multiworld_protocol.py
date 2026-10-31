# The MW01 wire extension carries bound world/seed/slot identity, both receipt cursors and
# recipe keys. Validate field limits and unavailable-state zeros before exposing a status
# object. Boundary names here: MultiworldStatus, delivery_request.
"""Capability-gated semantic CP3W extension; no arbitrary RAM operations."""
from __future__ import annotations

import dataclasses
import struct
import uuid

from randovania.game_connection.prime3_wii_tracker_protocol import TrackerProtocolError

CAPABILITY = 1 << 15
STATUS_COMMAND = 10
DELIVER_COMMAND = 11
STATUS = struct.Struct(">4s16s32sIIIIII32s13sBHH")
DELIVERY = struct.Struct(">16s32sIIII32s32s")


@dataclasses.dataclass(frozen=True)
class MultiworldStatus:
    world_uuid: uuid.UUID
    seed_fingerprint: str
    save_slot: int
    generation: int
    cursor: int
    saved_cursor: int
    ready: bool
    pending: bool
    history: bytes
    locations: frozenset[int]
    launcher_bits: int = 0
    locked_missiles: int = 0
    locked_ship_missiles: int = 0

    @property
    def binding(self):
        return {"world_uuid": str(self.world_uuid), "seed_fingerprint": self.seed_fingerprint,
                "save_slot": self.save_slot}

    @classmethod
    def decode(cls, raw):
        if len(raw) != STATUS.size:
            raise TrackerProtocolError("Invalid multiworld status size")
        magic, world, seed, slot, generation, cursor, saved, ready, pending, history, bitmap, launchers, missiles, ship = STATUS.unpack(raw)
        if (magic != b"MW01" or not any(world) or not any(seed) or slot >= 3
                or not 0 <= saved <= cursor <= 256 or ready not in (0, 1) or pending not in (0, 1)
                or bitmap[-1] & 0xF0 or launchers & ~3 or missiles > 255 or ship > 13):
            raise TrackerProtocolError("Invalid multiworld status fields")
        if not generation and (cursor or saved or ready or pending or any(history) or any(bitmap)
                               or launchers or missiles or ship):
            raise TrackerProtocolError("Unavailable runtime retained stale save state")
        locations = frozenset(i for i in range(100) if bitmap[i // 8] & (1 << (i % 8)))
        return cls(uuid.UUID(bytes=world), seed.hex(), slot, generation, cursor, saved,
                   bool(ready), bool(pending), history, locations, launchers, missiles, ship)


def delivery_request(status: MultiworldStatus, sequence: int, recipe: str) -> bytes:
    if not status.ready or status.pending or sequence != status.cursor + 1 or sequence > 256:
        raise ValueError("Runtime is not ready for this delivery")
    key = bytes.fromhex(recipe)
    if len(key) != 32:
        raise ValueError("Invalid recipe identifier")
    return DELIVERY.pack(status.world_uuid.bytes, bytes.fromhex(status.seed_fingerprint), status.save_slot,
                         status.generation, sequence, 0, status.history, key)
