# Guarded native checkpoint handoff diagnostics; no grants or receipt advancement. Boundary
# names here: fingerprints, validate, verify_handoffs, main.
"""Guarded native checkpoint handoff diagnostics; no grants or receipt advancement."""

from __future__ import annotations

import argparse
import importlib
import json
import os
import struct
import sys
from pathlib import Path

if __package__ in {None, ""}:
    _repository_root = os.fspath(Path(__file__).resolve().parents[2])
    if _repository_root not in sys.path:
        sys.path.insert(0, _repository_root)

from nullphaze_network.prime3_lua_service.receipt_delivery import validate_manifest as fixed_delivery_manifest

HOOKS = (
    (0x800B7F54, 0x800BA8CC, "receipt_trace_slot_checkpoint"),
    (0x800B8B18, 0x800BA8CC, "receipt_trace_slot_checkpoint"),
    (0x800B9028, 0x800BA8CC, "receipt_trace_slot_checkpoint"),
    (0x8024D86C, 0x800BAA98, "receipt_trace_backup_checkpoint"),
    (0x802EFBE4, 0x800BAA98, "receipt_trace_backup_checkpoint"),
    (0x802EFA88, 0x802EFC90, "receipt_trace_select_slot"),
    (0x802EFA94, 0x802F0BE4, "receipt_trace_source_vector"),
    (0x802EFAE8, 0x800B76C4, "receipt_trace_construct"),
    (0x802EFA60, 0x802F0B9C, "receipt_trace_install"),
    (0x802EFAF8, 0x802F0B9C, "receipt_trace_install"),
)
EVENTS = {
    14: "receipt_slot_checkpoint_begin",
    15: "receipt_slot_checkpoint_return",
    16: "receipt_backup_checkpoint_begin",
    17: "receipt_backup_checkpoint_return",
    18: "receipt_select_slot",
    20: "receipt_restore_source",
    22: "receipt_construct_begin",
    23: "receipt_construct_return",
    24: "receipt_install_begin",
    25: "receipt_install_return",
    29: "receipt_vector_fingerprint",
    30: "receipt_digest_0",
    31: "receipt_digest_1",
    32: "receipt_digest_2",
}


def fingerprints(events: list[dict]) -> tuple[list[dict], list[dict]]:
    """Decode committed hash fragments, rejecting missing/reordered publication."""
    pending, complete, unavailable = {}, [], []
    origins = {}
    for event in events:
        words = event["words"]
        kind, context, a, b, c = words[1:6]
        if kind in {15, 17, 20}:
            vector = {15: b, 17: a, 20: context}[kind]
            origins[vector] = {"operation": event["event"], "owner": context, "slot": a if kind == 15 else None}
        if kind == 29:
            if context in pending:
                raise ValueError("Incomplete fingerprint before vector reuse")
            item = {"vector": context, "size": a, "data": b, "sequence": words[0], **origins.get(context, {})}
            if c == 0:
                unavailable.append(item)
            elif c == 1 and a == 0x3C86:
                pending[context] = (item, [])
            else:
                raise ValueError("Invalid fingerprint dimensions or validity flag")
        elif kind in {30, 31, 32}:
            if context not in pending:
                raise ValueError("Orphan fingerprint fragment")
            item, digest = pending[context]
            if kind != 30 + len(digest) // 3 or (kind == 32 and c != 0):
                raise ValueError("Fingerprint fragments out of order")
            digest.extend((a, b) if kind == 32 else (a, b, c))
            if kind == 32:
                item["sha256"] = struct.pack(">8I", *digest).hex()
                complete.append(item)
                del pending[context]
    if pending:
        raise ValueError("Capture ends during fingerprint publication")
    return complete, unavailable


def validate(rows: list[dict], manifest: dict) -> dict:
    errors = []
    if not rows or rows[0].get("kind") != "capture_start" or rows[-1].get("kind") != "capture_end":
        errors.append("Capture lacks clean start/end")
    identity = {
        "native_build": manifest.get("probe_id"),
        "native_image_parts": manifest.get("image", {}).get("parts"),
        "native_immutable_sha256": manifest.get("lua_location_bridge", {}).get("immutable_sha256"),
        "method": "passive_read_only_no_gdb",
    }
    if not manifest.get("receipt_lifecycle_trace") or (
        rows and any(not value or rows[0].get(k) != value for k, value in identity.items())
    ):
        errors.append("Lifecycle capture identity mismatch")
    if any(row.get("kind") in {"native_event_loss", "native_trace_reset"} for row in rows):
        errors.append("Native event loss/reset requires a new bounded capture")
    try:
        fixed_delivery = fixed_delivery_manifest(manifest, allow_network=True)
    except (ValueError, KeyError):
        fixed_delivery = False
    if manifest.get("production_grants_enabled") is not False or (
        manifest.get("services", {}).get("grant") != "disabled" and not fixed_delivery
    ):
        errors.append("Lifecycle diagnostic must not enable grants")
    events = [row for row in rows if row.get("kind") == "native_event"]
    all_events = importlib.import_module("nullphaze_network.prime3_lua_service.save_native_trace").EVENTS
    previous = 0
    hashes, unavailable = [], []
    try:
        for event in events:
            words = event.get("words")
            if (
                not isinstance(words, list)
                or len(words) != 16
                or any(type(w) is not int or not 0 <= w <= 0xFFFFFFFF for w in words)
            ):
                raise ValueError("Invalid native event words")
            if (
                words[0] != previous + 1
                or words[0] != event.get("sequence")
                or all_events.get(words[1]) != event.get("event")
            ):
                raise ValueError("Invalid native event sequence or kind")
            previous = words[0]
        hashes, unavailable = fingerprints(events)
        if not any(item.get("operation") == "receipt_restore_source" for item in hashes):
            raise ValueError("No fingerprinted native restore source")
        for begin, end in ((22, 23), (24, 25)):
            if not any(e["words"][1] == begin for e in events) or not any(e["words"][1] == end for e in events):
                raise ValueError("Missing constructor or ownership handoff")
        verify_handoffs(events)
    except ValueError as error:
        errors.append(str(error))
    return {
        "passed": not errors,
        "errors": sorted(set(errors)),
        "fingerprints": hashes,
        "unavailable_vectors": unavailable,
        "native_events": len(events),
        "scope": "checkpoint fingerprint and ownership observations only; not receipt coupling acceptance",
        "receipt_coupling_verified": False,
        "production_grants_enabled": False,
        "hardware_verified": False,
    }


def verify_handoffs(events: list[dict]) -> None:
    pending = {}
    for event in events:
        words = event["words"]
        kind = words[1]
        if kind in {22, 24}:
            if kind in pending:
                raise ValueError("Overlapping ownership handoff")
            pending[kind] = words
        elif kind in {23, 25}:
            begin = pending.pop(kind - 1, None)
            if begin is None:
                raise ValueError("Ownership return without begin")
            if kind == 23:
                if words[2] != begin[2] or words[3:5] != begin[3:5] or words[5] != begin[2]:
                    raise ValueError("Constructor arguments or result mismatch")
            elif words[2:4] != begin[2:4] or words[4] != words[3] or words[5] != words[2]:
                raise ValueError("Ownership installation mismatch")
    if pending:
        raise ValueError("Incomplete ownership handoff")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build", type=Path, required=True)
    parser.add_argument("--capture", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads((args.build / "build.json").read_text(encoding="utf-8"))
    rows = [json.loads(line) for line in args.capture.read_text(encoding="utf-8").splitlines() if line.strip()]
    result = validate(rows, manifest)
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
