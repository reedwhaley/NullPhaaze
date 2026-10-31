# Build an opt-in pass-through native save-event diagnostic, without save changes. Boundary
# names here: events, main.
"""Build an opt-in pass-through native save-event diagnostic, without save changes."""

from __future__ import annotations

import argparse
import os
import struct
import sys
from pathlib import Path

if __package__ in {None, ""}:
    _repository_root = os.fspath(Path(__file__).resolve().parents[2])
    if _repository_root not in sys.path:
        sys.path.insert(0, _repository_root)

from nullphaze_network.prime3_lua_service import bridge
from nullphaze_network.prime3_lua_service.receipt_lifecycle import EVENTS as LIFECYCLE_EVENTS

HOOKS = (
    (0x801D6D00, 0x80344F24, "save_trace_crc"),
    (0x801D6A30, 0x803FA4D8, "save_trace_write"),
    (0x801D6B88, 0x803FA4D8, "save_trace_write"),
    (0x801D5FC0, 0x801D625C, "save_trace_complete"),
    (0x801D5FA0, 0x801D61A8, "save_trace_complete_initial"),
    (0x803FA218, 0x80507C8C, "save_trace_close"),
    (0x803FA20C, 0x80507D80, "save_trace_safe_close"),
    (0x801D7F8C, 0x801D86A4, "save_trace_snapshot_active"),
    (0x801D8678, 0x801D8790, "save_trace_snapshot_stored"),
    (0x801D6DF8, 0x801D84DC, "save_trace_slot_load"),
)
EVENTS = {
    1: "buffer_checksum",
    2: "write_begin",
    3: "write_queued",
    5: "completion_enter",
    6: "completion_return",
    7: "close_return",
    8: "safe_close_return",
    9: "active_snapshot_begin",
    10: "active_snapshot_return",
    11: "stored_snapshot_begin",
    12: "stored_snapshot_return",
    13: "slot_load",
    33: "synthetic_receipt_changed",
    34: "fixed_receipt_delivery",
}
SIZE = 8224
EVENTS.update(LIFECYCLE_EVENTS)


def events(raw: bytes) -> tuple[int, list[dict]]:
    if len(raw) != SIZE:
        raise ValueError("Incomplete trace buffer")
    words = struct.unpack(">2056I", raw)
    if words[:2] != (0x53505631, 1):
        raise ValueError("Native save trace identity mismatch")
    latest = words[2]
    rows = []
    for index in range(max(0, latest - 128), latest):
        record = words[8 + (index & 127) * 16 : 24 + (index & 127) * 16]
        if record[0] != index + 1:
            raise ValueError("Native event publication is incomplete")
        if record[1] not in EVENTS:
            raise ValueError("Unknown native event kind")
        rows.append({"sequence": record[0], "event": EVENTS[record[1]], "words": list(record)})
    return latest, rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-data", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--wit", type=Path, required=True)
    parser.add_argument("--native-save-trace", action="store_true", required=True)
    args = parser.parse_args()
    report = bridge.build(args.source_data, args.output, args.wit, save_trace=True)
    print(f"Built diagnostic save trace {report['probe_id']}; no grant or save-format change.")


if __name__ == "__main__":
    main()
