# Generate the bounded native allowlist from the recipient-aware seed. A foreign-recipient
# location records its collected bit without granting the displayed foreign item locally.
# Boundary names here: seed_tables, compile_seed.
"""Produce a bounded native allowlist from one recipient-aware export."""
from __future__ import annotations

import base64
import hashlib

from randovania.bitpacking.bitpacking import BitPackDecoder
from randovania.game.game_enum import RandovaniaGame
from randovania.game_description import default_database
from randovania.games.prime3.multiworld.manifest import pickup_bytes, validate_manifest
from randovania.games.prime3.multiworld.recipes import compile_recipe, resource_limits
from randovania.network_common.pickup_serializer import BitPackPickupEntry


def seed_tables(manifest: dict, pickup_mapping: list[dict] | None = None):
    # This is the export-time boundary between serialized RDV pickups and the
    # small native recipe table. RDS handles resources elsewhere; a network
    # packet cannot ask it to deserialize new behavior into a running game.
    validate_manifest(manifest)
    if pickup_mapping is not None and [row["index"] for row in pickup_mapping] != list(range(100)):
        raise ValueError("Native addon requires all 100 audited event mappings")
    database = default_database.resource_database_for(RandovaniaGame.METROID_PRIME_CORRUPTION)
    encoded = {key: row["pickup"] for key, row in manifest["incoming_recipes"].items()}
    incoming_keys = set(encoded)
    for row in manifest["locations"]:
        if row["local"]:
            encoded[row["pickup_key"]] = row["pickup"]
    if not 0 < len(encoded) <= 256:
        raise ValueError("Seed exceeds the bounded native recipe allowlist")
    recipes = {}
    for key, value in sorted(encoded.items()):
        raw = base64.b85decode(value)
        # validate_manifest authenticates sender-bound incoming keys. Local
        # recipes retain their canonical pickup-only digest.
        if len(raw) > 4096 or (key not in incoming_keys and hashlib.sha256(raw).hexdigest() != key):
            raise ValueError("Corruption pickup encoding/digest mismatch")
        pickup = BitPackPickupEntry.bit_pack_unpack(BitPackDecoder(raw), database)
        if pickup_bytes(pickup, database) != raw:
            raise ValueError("Pickup encoding is not canonical")
        recipes[key] = compile_recipe(pickup)
    indices = {key: index for index, key in enumerate(recipes)}
    return recipes, incoming_keys, indices


def compile_seed(manifest: dict, pickup_mapping: list[dict]) -> str:
    recipes, incoming_keys, indices = seed_tables(manifest, pickup_mapping)
    database = default_database.resource_database_for(RandovaniaGame.METROID_PRIME_CORRUPTION)

    def array(values):
        return "{" + ",".join(str(value) + "u" for value in values) + "}"

    def gains(values, maximum):
        return "{" + ",".join(array(pair) for pair in (*values, *((0, 0),) * (maximum - len(values)))) + "}"

    recipe_rows = []
    for recipe in recipes.values():
        lock = recipe.lock or (0, 0, 0)
        recipe_rows.append("{" + ",".join((
            *(str(value) + "u" for value in (len(recipe.progression), len(recipe.extra), int(recipe.respects_lock),
                                             int(recipe.unlocks), *lock)),
            gains(recipe.progression, 4), gains(recipe.extra, 8),
        )) + "}")
    locations = []
    for row, mapped in zip(manifest["locations"], pickup_mapping, strict=True):
        # A foreign recipient gets a collected-location bit, not a local grant.
        # The model at that location is selected separately from this sentinel.
        locations.append(array((indices[row["pickup_key"]] if row["local"] else 0xffffffff,
                                mapped["area"] >> 32, mapped["area"] & 0xffffffff)))
    declarations = {
        "unsigned char mw_world[16]": array(bytes.fromhex(manifest["world_uuid"].replace("-", ""))),
        "unsigned char mw_seed[32]": array(bytes.fromhex(manifest["seed_fingerprint"])),
        "unsigned int mw_limits[63]": array(resource_limits()),
        "unsigned int mw_native_ids[63]": array(item.extra["item_id"] for item in database.item),
        "struct mw_recipe mw_recipes[MW_RECIPE_COUNT]": "{" + ",".join(recipe_rows) + "}",
        "unsigned char mw_recipe_keys[MW_RECIPE_COUNT][32]": "{" + ",".join(array(bytes.fromhex(key)) for key in recipes) + "}",
        "unsigned int mw_incoming_allowed[MW_RECIPE_COUNT]": array(int(key in incoming_keys) for key in recipes),
        "unsigned int mw_locations[100][3]": "{" + ",".join(locations) + "}",
    }
    return ("/* Generated from one seed; no host-provided addresses. GPL addon. */\n"
            "#define CP3W_MULTIWORLD 1\n#define CP3W_NO_DIAGNOSTICS 1\n"
            f"#define MW_SAVE_SLOT {manifest['save_slot']}u\n#define MW_RECIPE_COUNT {len(recipes)}u\n"
            "#ifndef __ASSEMBLER__\n#include \"multiworld_plan.h\"\n" + "\n".join(
                f"static const {declaration} __attribute__((unused)) = {value};"
                for declaration, value in declarations.items()
            ) + "\n#endif\n")
