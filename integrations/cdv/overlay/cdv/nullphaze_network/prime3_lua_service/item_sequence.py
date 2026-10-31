# Dolphin-only, compiled item sequence; never an arbitrary item-write service. Boundary
# names here: plan, validate, history, compile_flags, metadata.
"""Dolphin-only, compiled item sequence; never an arbitrary item-write service."""

from __future__ import annotations

import dataclasses
import hashlib
import json
import struct
import uuid
import zlib
from pathlib import Path

from retro_data_structures.enums.corruption import State

from nullphaze_network.prime3_lua_service import network_save, save_container, save_profile, sequence_presentation

# Catalog aliases are intentionally distinct deliveries with distinct receipts.
ITEMS = (
    ("MissileExpansion", 4, 5),
    ("MainRequiredMissileExpansion", 4, 5),
    ("EnergyTank", 20, 1),
    ("SpaceJump", 15, 1),
    ("IceMissile", 5, 1),
    ("SeekerMissile", 6, 1),
    ("ProgressiveMissile", 5, 1),
    ("ChargeUpgrade", 3, 1),
    ("PlasmaBeam", 1, 1),
    ("NovaBeam", 2, 1),
    ("ProgressiveBeam", 1, 1),
    ("GrappleLasso", 7, 1),
    ("GrappleSwing", 8, 1),
    ("GrappleVoltage", 9, 1),
    ("Bomb", 10, 1),
    ("ScanVisor", 12, 1),
    ("CombatVisor", 11, 1),
    ("CommandVisor", 13, 1),
    ("XRayVisor", 14, 1),
    ("ScrewAttack", 16, 1),
    ("Suit", 17, 5),
    ("MorphBall", 32, 1),
    ("BoostBall", 33, 1),
    ("SpiderBall", 34, 1),
    ("HyperModeTank", 35, 1),
    ("HyperBall", 38, 1),
    ("HyperMissile", 37, 1),
    ("HyperGrapple", 39, 1),
    ("ShipMissileExpansion", 45, 1),
    ("MainRequiredShipMissileExpansion", 45, 1),
    ("ShipGrapple", 44, 1),
    *((f"Fuse{i}", 22 + i, 1) for i in range(1, 10)),
    ("MissileLauncher", 4, 5),
    ("ConverterMissileLauncher", 4, 5),
    ("ShipMissile", 45, 3),
    ("ConverterShipMissile", 45, 3),
)
SCHEMA = "cp3w-dolphin-item-sequence-v1"
COMBINED = {
    "schema": 1,
    "native_snapshot_command": 9,
    "session_owner": "one_paced_loopback_client",
    "cdv_view": "read_only_loopback_broker",
}


def plan():
    # Exercise both progressive stages before their direct-item counterparts.
    order = [6, 6, 10, 10] + [i for i in range(len(ITEMS)) if i not in (6, 10)]
    stages = {6: 0, 10: 0}
    result = []
    for sequence, item in enumerate(order, 1):
        name, native, amount = ITEMS[item]
        if item in stages:
            native += stages[item]
            stages[item] += 1
        operations = [[native, amount, amount]]
        result.append(
            {
                "sequence": sequence,
                "catalog_id": item,
                "name": name,
                "descriptor": [0, sequence, item, amount, amount, 1],
                "operations": operations,
            }
        )
    return {
        "schema": SCHEMA,
        "dolphin_only": True,
        "production": False,
        "baseline": "power-beam-combat-visor-99-health-no-optional-items",
        "steps": result,
    }


def validate(value):
    if value != plan():
        raise ValueError("Unknown compiled Dolphin item sequence")
    return value


def history(profile, cursor):
    network_save.validate_profile(profile)
    if type(cursor) is not int or not 0 <= cursor <= len(plan()["steps"]):
        raise ValueError("Item sequence cursor outside compiled plan")
    digest = bytes(32)
    for step in plan()["steps"][:cursor]:
        digest = hashlib.sha256(digest + profile + struct.pack(">6I", *step["descriptor"])).digest()
    return digest


def compile_flags(path, output, *, owned, mem2, receipt, tracker):
    if path is None:
        return ()
    if not (owned and mem2 and receipt) or tracker:
        raise ValueError("Item sequence requires separate owned MEM2 delivery, not tracker mode")
    value = validate(json.loads(Path(path).read_text()))
    rows = []
    for step in value["steps"]:
        operation = step["operations"][0]
        rows.append("{" + ",".join(map(str, [*step["descriptor"], *operation])) + "}")
    header = output / "item_sequence_plan.h"
    header.write_text(
        "#define CP3W_SEQUENCE_COUNT " + str(len(rows)) + "u\n"
        "#ifndef __ASSEMBLER__\n"
        "static const unsigned int sequence_steps[][9] __attribute__((unused)) = {" + ",".join(rows) + "};\n#endif\n"
    )
    return ("-DCP3W_ITEM_SEQUENCE_TEST", "-DCP3W_NO_DIAGNOSTICS", "-include", str(header))


def metadata(path):
    if path is None:
        return {}
    return {
        "item_sequence_test": plan(),
        "item_sequence_sources": {
            name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in ("item_sequence_common.h", "item_sequence_queue.c", "item_sequence_delivery.c")
        },
    }


def symbols(path):
    return {"bridge_tracker_snapshot"} if path is not None else set()


def presentation(source, messages, path, native_hash=None):
    if path is None:
        return source, messages
    states = [s for s in State if s.name.startswith("InternalState")]
    messages = tuple(
        (f"SequenceReceived{i}", states[i - 1], sequence_presentation.notice(step))
        for i, step in enumerate(plan()["steps"], 1)
    )
    if not native_hash or len(native_hash) != 64:
        raise ValueError("Sequence Lua requires the exact native binary identity")
    identity = hashlib.sha256(Path(sequence_presentation.__file__).read_bytes()).hexdigest()
    return (
        Path(__file__).with_suffix(".lua").read_text()
        + "\n-- Native SHA256 "
        + native_hash
        + "\n-- Pickup presentation SHA256 "
        + identity
        + "\n"
    ), messages


def configure_manifest(report, path):
    if path is not None:
        report["item_sequence_test"] = plan()
        report["combined_tracker_test"] = dict(COMBINED)
        report["services"]["grant"] = "compiled_dolphin_item_sequence_only"
        report["receipt_delivery_probe"] = {
            "schema": 1,
            "kind": SCHEMA,
            "production": False,
            "state_address": report["lua_location_bridge"]["delivery_state_address"],
            "state_size": 64,
        }
        report["receipt_coupling_probe"]["cursors"] = list(range(len(plan()["steps"]) + 1))
        report["network_delivery_probe"]["kind"] = SCHEMA
        report["owned_transport_probe"]["frame_limit"] = 4096
        report["presentation"] = {
            "diagnostic_panel": False,
            "diagnostic_hud": False,
            "pickup_hud": "non_modal_timed_hud",
        }


def validate_manifest(manifest):
    value = manifest.get("item_sequence_test")
    if value is None:
        return False
    validate(value)
    native = manifest.get("lua_location_bridge", {})
    if (
        manifest.get("combined_tracker_test") != COMBINED
        or "bridge_tracker_snapshot" not in native.get("symbols", {})
        or native.get("item_sequence_test") != value
        or native.get("tracker_read_only")
        or manifest.get("services", {}).get("grant") != "compiled_dolphin_item_sequence_only"
        or manifest.get("production_grants_enabled") is not False
        or manifest.get("network_save_adapter", {}).get("grants_enabled") is not True
        or manifest.get("owned_transport_probe", {}).get("frame_limit") != 4096
    ):
        raise ValueError("Invalid isolated item-sequence manifest")
    network_save.validate_profile(bytes.fromhex(manifest["network_save_adapter"]["profile_hex"]))
    return True


def seed(source: Path, output: Path, dol: bytes):
    source, output = source.resolve(), output.resolve()
    if output.exists() or source == output or source in output.parents:
        raise ValueError("Use a new isolated item-sequence fixture directory")
    original = source.read_bytes()
    checkpoint = network_save.decode(original)
    layout = save_profile.profile(dol)
    inspected = save_container.inspect_save(checkpoint.retail, layout)
    prefixes = [p for p in inspected["player_prefixes"] if p["slot_index"] == 0]
    if len(prefixes) != 1 or inspected["container_framing"]["active_slot_index"] != 0:
        raise ValueError("Expected exactly one slot0 inventory prefix")
    bits = list("".join(f"{b:08b}" for b in checkpoint.retail))
    start = prefixes[0]["bit_offset"]

    def put(offset, width, value):
        bits[start + offset : start + offset + width] = f"{value:0{width}b}"

    put(64, 32, int.from_bytes(struct.pack(">f", 99.0), "big"))
    for field in layout["saved_fields"]:
        value = int(field["id"] in (0, 11))
        for key in ("amount_bit_offset", "capacity_bit_offset"):
            put(field[key], field["bits_per_value"], value)
    retail = bytearray(int("".join(bits[i : i + 8]), 2) for i in range(0, len(bits), 8))
    struct.pack_into(">I", retail, 0, zlib.crc32(retail[4:]) ^ 0xFFFFFFFF)
    lineage = uuid.uuid4()
    checkpoint = dataclasses.replace(
        checkpoint,
        retail=bytes(retail),
        campaign=uuid.uuid4(),
        lineage=lineage,
        receipts=tuple(network_save.Receipt(i, network_save.slot_identity(lineage, i)) for i in range(3)),
    )
    wire = network_save.encode(checkpoint)
    checked = save_container.inspect_save(network_save.decode(wire).retail, layout)
    assert checked["player_prefixes"][0]["health_float_bits"] == "42c60000"
    output.mkdir(parents=True)
    (output / "delivery.cp3w").write_bytes(wire)
    (output / "profile.bin").write_bytes(network_save.bound_profile(checkpoint))
    (output / "sequence.json").write_text(json.dumps(plan(), indent=2) + "\n")
    report = {
        "source_sha256": hashlib.sha256(original).hexdigest(),
        "fixture_sha256": hashlib.sha256(wire).hexdigest(),
        "inventory": checked,
        "source_unchanged": source.read_bytes() == original,
        "console_modified": False,
    }
    (output / "fixture.json").write_text(json.dumps(report, indent=2) + "\n")
    return report
