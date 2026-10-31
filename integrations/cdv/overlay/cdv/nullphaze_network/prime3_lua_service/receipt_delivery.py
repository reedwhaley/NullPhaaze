# Fixed, local, receipted missile delivery for an explicitly disposable save. Boundary names
# here: history, spec, validate_manifest, decode, seed.
"""Fixed, local, receipted missile delivery for an explicitly disposable save."""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import importlib
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

FIXED = {
    "schema": 1,
    "kind": "fixed_local_receipted_missile_disposable_save",
    "slot": 0,
    "sequence": 1,
    "item_id": 4,
    "capacity_before": 20,
    "capacity_delta": 5,
    "amount_delta": 5,
    "percentage_delta": 1,
    "network_operations": 0,
    "production": False,
}
FIELDS = (
    "magic",
    "stage",
    "attempts",
    "applied",
    "duplicates",
    "game",
    "generation",
    "ticks",
    "before_amount",
    "before_capacity",
    "before_percent",
    "before_percent_capacity",
    "after_amount",
    "after_capacity",
    "after_percent",
    "after_percent_capacity",
)


def history(profile: bytes) -> bytes:
    network_save.validate_profile(profile)
    return hashlib.sha256(bytes(32) + profile + struct.pack(">6I", 0, 1, 4, 5, 5, 1)).digest()


def spec(native: dict) -> dict:
    return {**FIXED, "state_address": native["delivery_state_address"], "state_size": 64}


def validate_manifest(manifest: dict, *, allow_network: bool = False) -> bool:
    delivery = manifest.get("receipt_delivery_probe")
    if delivery is None:
        return False
    if "network_delivery_probe" in manifest:
        if not allow_network:
            raise ValueError("Network delivery requires a separate network acceptance validator")
        importlib.import_module("nullphaze_network.prime3_lua_service.network_delivery").validate_extension(manifest)
    native = manifest.get("lua_location_bridge", {})
    adapter = manifest.get("network_save_adapter", {})
    coupling = manifest.get("receipt_coupling_probe", {})
    if (
        any(delivery.get(k) != v for k, v in FIXED.items())
        or delivery.get("state_size") != 64
        or delivery.get("state_address") != native.get("delivery_state_address")
        or not native.get("experimental_receipt_delivery")
        or not native.get("experimental_receipt_coupling")
        or manifest.get("production_grants_enabled") is not False
        or manifest.get("services", {}).get("grant") != "fixed_receipted_disposable_missile_only"
        or adapter.get("filename") != "cp3w.bin"
        or adapter.get("grants_enabled") is not True
        or adapter.get("receipt_advancement_enabled") is not True
        or coupling.get("synthetic_receipts_only") is not False
        or coupling.get("inventory_writes") is not True
        or coupling.get("cursors") != [0, 1]
    ):
        raise ValueError("Unsupported fixed receipted delivery experiment")
    profile = bytes.fromhex(adapter["profile_hex"])
    network_save.validate_profile(profile)
    return True


def decode(raw: bytes) -> dict:
    if len(raw) != 64:
        raise ValueError("Invalid delivery state length")
    values = struct.unpack(">16I", raw)
    if values[0] != 0x52444731 or values[1] not in range(5):
        raise ValueError("Invalid fixed delivery state")
    return dict(zip(FIELDS, values, strict=True))


def seed(source: Path, output: Path) -> dict:
    source, output = source.resolve(), output.resolve()
    if output.exists() or source == output or source in output.parents:
        raise ValueError("Use a new disposable delivery fixture directory")
    raw = source.read_bytes()
    value = network_save.decode(raw)
    if container_layout(value.retail)["active_slot_index"] != 0:
        raise ValueError("Fixed delivery supports active slot0 only")
    lineage = uuid.uuid4()
    receipts = tuple(network_save.Receipt(i, network_save.slot_identity(lineage, i), 0, bytes(32)) for i in range(3))
    value = dataclasses.replace(value, campaign=uuid.uuid4(), lineage=lineage, receipts=receipts)
    wire, profile = network_save.encode(value), network_save.bound_profile(value)
    report = {
        **FIXED,
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "fixture_sha256": hashlib.sha256(wire).hexdigest(),
        "retail_payload_unchanged": True,
        "expected_history": history(profile).hex(),
    }
    output.mkdir(parents=True)
    (output / "input.cp3w").write_bytes(raw)
    (output / "delivery.cp3w").write_bytes(wire)
    (output / "profile.bin").write_bytes(profile)
    (output / "fixture.json").write_text(json.dumps(report, indent=2) + "\n")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed-from", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(seed(args.seed_from, args.output), indent=2))


if __name__ == "__main__":
    main()
