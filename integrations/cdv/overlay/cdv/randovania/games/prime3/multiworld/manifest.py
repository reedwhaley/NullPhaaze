# The exported world/seed/slot and canonical pickup encoding define authorized recipes.
# sender-v1 also binds sender identity; presentation text cannot silently select another
# incoming recipe. Boundary names here: canonical, pickup_bytes, pickup_key,
# sender_pickup_key, remote_pickup_key.
"""Recipient-aware seed description; this never edits the MIT core catalog."""
from __future__ import annotations

import base64
import hashlib
import json
import uuid

from randovania.bitpacking import bitpacking
from randovania.game.game_enum import RandovaniaGame
from randovania.game_description import default_database
from randovania.game_description.assignment import PickupTarget
from randovania.game_description.resources.pickup_index import PickupIndex
from randovania.interface_common.players_configuration import INVALID_UUID
from randovania.network_common.nullphaze_multiworld import CONTRACT, SUPPORTED_GAMES
from randovania.network_common.pickup_serializer import BitPackPickupEntry

SCHEMA = 1
LOCATION_COUNT = 100


def canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")


def pickup_bytes(pickup, database) -> bytes:
    return bitpacking.pack_value(BitPackPickupEntry(pickup, database))


def pickup_key(pickup, database) -> str:
    return hashlib.sha256(pickup_bytes(pickup, database)).hexdigest()


def sender_pickup_key(raw: bytes, sender: str) -> str:
    """A bounded recipe identity includes its exported sender display name.

    Identical items from different players need distinct presentation events;
    their inventory recipes remain identical. No runtime text is accepted.
    """
    if not isinstance(sender, str) or not 1 <= len(sender) <= 256 or not sender.strip():
        raise ValueError("Invalid incoming sender name")
    return hashlib.sha256(canonical(["Corruption sender recipe v1", hashlib.sha256(raw).hexdigest(), sender])).hexdigest()


def remote_pickup_key(manifest, pickup, database, sender):
    # sender-v1 binds the exported sender name as well as the canonical pickup.
    # Two equal-looking items from different players can have distinct notices.
    # Renaming a world after export must not silently select another recipe.
    raw = pickup_bytes(pickup, database)
    if manifest.get("incoming_presentation") == "sender-v1":
        key = sender_pickup_key(raw, sender)
    else:
        key = hashlib.sha256(raw).hexdigest()
    if key not in manifest["incoming_recipes"]:
        expected = sorted({recipe.get("sender_name", "legacy sender")
                           for recipe in manifest["incoming_recipes"].values()
                           if base64.b85decode(recipe["pickup"]) == raw})
        detail = (f"Exported senders for this item: {', '.join(expected)}. "
                  "If world names changed after export, re-export the matching world."
                  if expected else "This item is not an authorized incoming recipe for the exported world.")
        raise ValueError(f"Incoming item/sender does not match this exported seed: "
                         f"{pickup.name!r} from {sender!r}. {detail}")
    return key


def validate_manifest(manifest: dict) -> None:
    if manifest.get("schema") != SCHEMA or manifest.get("contract") != CONTRACT:
        raise ValueError("Unsupported Corruption multiworld manifest")
    world = uuid.UUID(manifest["world_uuid"])
    if world in (INVALID_UUID, uuid.UUID(int=0)):
        raise ValueError("Multiworld requires a session-assigned world UUID")
    if len(bytes.fromhex(manifest["seed_fingerprint"])) != 32:
        raise ValueError("Invalid multiworld seed fingerprint")
    from randovania.game_connection.prime3_wii_tracker_protocol import validate_profile

    profile = bytes.fromhex(manifest["checkpoint_profile"])
    validate_profile(profile)
    lineage = uuid.uuid5(world, manifest["seed_fingerprint"])
    expected_profile = world.bytes + lineage.bytes + b"".join(
        uuid.uuid5(lineage, f"CP3W slot {i}").bytes for i in range(3)
    )
    if profile != expected_profile:
        raise ValueError("Checkpoint profile does not match world/seed identity")
    if type(manifest["save_slot"]) is not int or not 0 <= manifest["save_slot"] < 3 or manifest["save_policy"] != "new-multiworld-save-only":
        raise ValueError("Multiworld requires an explicit new bound save slot")
    locations = manifest["locations"]
    if [row["index"] for row in locations] != list(range(LOCATION_COUNT)) or any(type(row["index"]) is not int for row in locations):
        raise ValueError("Expected all 100 distinct Corruption pickup indices")
    for row in locations:
        if row["recipient_game"] not in {game.value for game in SUPPORTED_GAMES}:
            raise ValueError("Unsupported recipient game")
        recipient = uuid.UUID(row["recipient_world"])
        if (recipient in (INVALID_UUID, uuid.UUID(int=0)) or type(row["local"]) is not bool
                or row["local"] != (recipient == world)):
            raise ValueError("Conflicting recipient/world binding")
        if "pickup" in row:
            raw = base64.b85decode(row["pickup"])
            if len(raw) > 4096 or hashlib.sha256(raw).hexdigest() != row["pickup_key"]:
                raise ValueError("Location pickup digest mismatch")
    if manifest.get("incoming_presentation") not in (None, "sender-v1"):
        raise ValueError("Unsupported incoming item presentation")
    sources = set()
    for key, recipe in manifest["incoming_recipes"].items():
        raw = base64.b85decode(recipe["pickup"])
        expected_key = (sender_pickup_key(raw, recipe.get("sender_name"))
                        if manifest.get("incoming_presentation") == "sender-v1" else hashlib.sha256(raw).hexdigest())
        if len(raw) > 4096 or expected_key != key:
            raise ValueError("Incoming pickup recipe digest mismatch")
        for source in recipe.get("sources", []):
            provider = uuid.UUID(source["world_uuid"])
            index = source["index"]
            pair = provider, index
            if (provider in (world, INVALID_UUID, uuid.UUID(int=0)) or type(index) is not int
                    or not 0 <= index < 1000 or pair in sources):
                raise ValueError("Invalid or repeated incoming pickup source")
            sources.add(pair)


def create_manifest(factory, *, save_slot: int = 0) -> dict:
    config = factory.players_config
    if config.is_coop:
        raise ValueError("Shared-world co-op is not supported by Corruption multiworld v1")
    if not config.is_multiworld:
        raise ValueError("A multiworld session is required")
    for player in factory.description.all_patches:
        if factory.description.get_preset(player).game not in SUPPORTED_GAMES:
            raise ValueError("This private release supports Prime 1, Echoes and Corruption only")
        if config.uuids.get(player, INVALID_UUID) in (INVALID_UUID, uuid.UUID(int=0)):
            raise ValueError("Every multiworld participant requires its assigned world UUID")
    locations = []
    recipes = {}
    for provider, patches in sorted(factory.description.all_patches.items()):
        assignments = dict(patches.pickup_assignment)
        if provider == config.player_index:
            if any(not 0 <= index.index < LOCATION_COUNT for index in assignments):
                raise ValueError("Unmapped Corruption pickup index")
            for index in range(LOCATION_COUNT):
                assignments.setdefault(PickupIndex(index), PickupTarget(factory.create_useless_pickup(), provider))
        for index, target in sorted(assignments.items(), key=lambda pair: pair[0].index):
            if target.player == config.player_index and provider != config.player_index:
                raw = pickup_bytes(target.pickup, factory.game.resource_database)
                sender = config.player_names[provider]
                recipe = recipes.setdefault(sender_pickup_key(raw, sender), {
                    "name": target.pickup.name, "pickup": base64.b85encode(raw).decode("ascii"),
                    "sender_name": sender,
                    "sources": [],
                })
                recipe["sources"].append({"world_uuid": str(config.uuids[provider]), "index": index.index})
            if provider == config.player_index:
                recipient_game = factory.description.get_preset(target.player).game
                recipient_database = default_database.resource_database_for(recipient_game)
                encoded = pickup_bytes(target.pickup, recipient_database)
                locations.append({
                    "index": index.index,
                    "assigned": index in patches.pickup_assignment,
                    "recipient_world": str(config.uuids[target.player]),
                    "recipient_game": recipient_game.value,
                    "recipient_name": config.player_names[target.player],
                    "item_name": target.pickup.name,
                    "pickup": base64.b85encode(encoded).decode("ascii"),
                    "pickup_key": hashlib.sha256(encoded).hexdigest(),
                    "local": config.should_target_local_player(target.player),
                })
    if getattr(factory.description, "diagnostic_mirrors", False):
        from randovania.network_common.diagnostic_mirrors import mirror_name, mirror_uuid, mirror_pickups

        sender = mirror_name(config.player_index)
        provider_uuid = mirror_uuid(config.get_own_uuid())
        for index, (_, _, pickup) in enumerate(mirror_pickups(factory.description, config.player_index)):
            raw = pickup_bytes(pickup, factory.game.resource_database)
            recipe = recipes.setdefault(sender_pickup_key(raw, sender), {
                "name": pickup.name, "pickup": base64.b85encode(raw).decode("ascii"),
                "sender_name": sender, "sources": [],
            })
            recipe["sources"].append({"world_uuid": str(provider_uuid), "index": index})
    manifest = {
        "schema": SCHEMA, "contract": CONTRACT,
        "world_uuid": str(config.get_own_uuid()), "save_slot": save_slot,
        "save_policy": "new-multiworld-save-only",
        "locations": locations, "incoming_recipes": recipes,
        "incoming_presentation": "sender-v1",
    }
    # Includes every world's placement and preset, not a runtime checkpoint UUID.
    manifest["seed_fingerprint"] = hashlib.sha256(factory.description.as_binary(force_spoiler=True)).hexdigest()
    lineage = uuid.uuid5(config.get_own_uuid(), manifest["seed_fingerprint"])
    manifest["checkpoint_profile"] = (config.get_own_uuid().bytes + lineage.bytes + b"".join(
        uuid.uuid5(lineage, f"CP3W slot {i}").bytes for i in range(3)
    )).hex()
    validate_manifest(manifest)
    return manifest
