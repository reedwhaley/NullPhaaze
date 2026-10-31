# Exact, read-only inventory binding profile for the supported retail executable. Boundary
# names here: extract_profile, bindings.
"""Exact, read-only inventory binding profile for the supported retail executable."""

from __future__ import annotations

import hashlib
import struct

from randovania.games.prime3.exporter.dol_patcher import parse_dol_header, virtual_address_to_file_offset

RETAIL_HASH = "6b550f221602074747a2e61b0aa064203fd493f6865dfb3b1a912682065e6104"
TABLE_ADDRESS = 0x8057B568
RETAIL_NAMES = (
    "PowerBeam",
    "PlasmaBeam",
    "NovaBeam",
    "ChargeUpgrade",
    "Missile",
    "IceMissile",
    "SeekerMissile",
    "GrappleBeamPull",
    "GrappleBeamSwing",
    "GrappleBeamVoltage",
    "Bomb",
    "CombatVisor",
    "ScanVisor",
    "CommandVisor",
    "XRayVisor",
    "DoubleJump",
    "ScrewAttack",
    "SuitType",
    "Energy",
    "HypermodeEnergy",
    "EnergyTank",
    "ItemPercentage",
    "Fuses",
    "Fuse1",
    "Fuse2",
    "Fuse3",
    "Fuse4",
    "Fuse5",
    "Fuse6",
    "Fuse7",
    "Fuse8",
    "Fuse9",
    "MorphBall",
    "BoostBall",
    "SpiderBall",
    "HyperModeTank",
    "HyperModeBeam",
    "HyperModeMissile",
    "HyperModeBall",
    "HyperModeGrapple",
    "HyperModePermanent",
    "HyperModePhaaze",
    "HyperModeOriginal",
    "HyperModeCharge",
    "ShipGrapple",
    "ShipMissile",
    "FaceCorruptionLevel",
    "PhazonBall",
    "CannonBall",
    "ActivateMorphballBoost",
    "HyperShot",
    "CommandVisorJammed",
    "FusesUsed",
    "Fuse1Used",
    "Fuse2Used",
    "Fuse3Used",
    "Fuse4Used",
    "Fuse5Used",
    "Fuse6Used",
    "Fuse7Used",
    "Fuse8Used",
    "Fuse9Used",
    "Stat_EnemiesKilled",
    "Stat_ShotsFired",
    "Stat_DamageReceived",
    "Stat_DataSaves",
    "Stat_HypermodeUses",
    "Stat_CommandoKills",
    "Stat_TinCanHighScore",
    "Stat_TinCanCurrentScore",
)
BASIC_IDS = (0, 4, 18, 45, 6)


def extract_profile(dol: bytes) -> dict:
    if hashlib.sha256(dol).hexdigest() != RETAIL_HASH:
        raise ValueError("Unsupported retail DOL for inventory bindings")
    header = parse_dol_header(dol)
    offset = virtual_address_to_file_offset(header.sections, TABLE_ADDRESS, len(RETAIL_NAMES) * 12)
    table = dol[offset : offset + len(RETAIL_NAMES) * 12]
    items = []
    for item_id, expected_name in enumerate(RETAIL_NAMES):
        pointer, limit, flags = struct.unpack_from(">III", table, item_id * 12)
        start = virtual_address_to_file_offset(header.sections, pointer, len(expected_name) + 1)
        if dol[start : start + len(expected_name) + 1] != expected_name.encode("ascii") + b"\0":
            raise ValueError("Retail inventory name table mismatch")
        items.append({"id": item_id, "name": expected_name, "declared_limit": limit, "flags": flags})
    return {
        "schema": 2,
        "dol_sha256": RETAIL_HASH,
        "table_address": TABLE_ADDRESS,
        "table_sha256": hashlib.sha256(table).hexdigest(),
        "items": items,
        "amount_getter": 0x80191624,
        "capacity_getter": 0x80191798,
        "name_lookup": 0x8018ED9C,
        "mode_getter": 0x8019161C,
        "energy_semantics": "truncated current health; capacity = truncate(base + per_tank * EnergyTank amount)",
        "other_semantics": "amount/capacity at player_state + 0x54/0x58 + 12 * item_id; mode getter returns zero",
        "grants_enabled": False,
    }


def bindings(manifest: dict) -> tuple[int, tuple[str, ...], tuple[int, ...]]:
    profile = manifest.get("inventory_profile")
    if profile is None:
        return 1, tuple(RETAIL_NAMES[index] for index in BASIC_IDS), BASIC_IDS
    if not isinstance(profile, dict) or profile.get("schema") != 2 or profile.get("dol_sha256") != RETAIL_HASH:
        raise ValueError("Unsupported inventory binding profile")
    items = profile.get("items")
    if not isinstance(items, list) or len(items) != len(RETAIL_NAMES):
        raise ValueError("Incomplete inventory binding profile")
    for item_id, (item, name) in enumerate(zip(items, RETAIL_NAMES, strict=True)):
        if (
            not isinstance(item, dict)
            or type(item.get("id")) is not int
            or item["id"] != item_id
            or item.get("name") != name
        ):
            raise ValueError("Inventory binding IDs/names/order mismatch")
    return 2, RETAIL_NAMES, tuple(range(len(RETAIL_NAMES)))
