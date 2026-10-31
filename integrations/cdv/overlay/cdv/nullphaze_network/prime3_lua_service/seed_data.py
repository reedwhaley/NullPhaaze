# Encode the validated world, recipe table, locations and presentation data into the fixed
# template region. Size/layout checks keep seed personalization away from executable
# instructions. Boundary names here: compile_data.
"""GPL addon seed table encoding for a fixed, independently compiled runtime.

Only the bounded data table and checkpoint identity are personalized. No game
address, function pointer, instruction, or arbitrary write is supplied by a seed.
"""
from __future__ import annotations

import struct
import uuid

from randovania.game.game_enum import RandovaniaGame
from randovania.game_description import default_database
from randovania.games.prime3.multiworld.recipes import resource_limits
from randovania.games.prime3.multiworld.seed_compiler import seed_tables

MAGIC = b"NPMWPL01"
SIZE = 42736
MAX_RECIPES = 256
HEADER = ("#define CP3W_MULTIWORLD 1\n#define CP3W_NO_DIAGNOSTICS 1\n"
          "#define CP3W_PATCHABLE_SEED 1\n#ifndef __ASSEMBLER__\n"
          '#include "multiworld_seed_data.h"\n#endif\n')


def compile_data(manifest, mapping):
    recipes, incoming, indices = seed_tables(manifest, mapping)
    database = default_database.resource_database_for(RandovaniaGame.METROID_PRIME_CORRUPTION)
    values = bytearray(MAGIC + struct.pack(">II", 1, SIZE))
    values.extend(uuid.UUID(manifest["world_uuid"]).bytes)
    values.extend(bytes.fromhex(manifest["seed_fingerprint"]))

    def words(*items):
        if any(type(value) is not int or not 0 <= value <= 0xffffffff for value in items):
            raise ValueError("Seed data word outside unsigned 32-bit range")
        values.extend(struct.pack(">" + "I" * len(items), *items))

    words(manifest["save_slot"], len(recipes))
    words(*resource_limits())
    words(*(item.extra["item_id"] for item in database.item))
    for recipe in recipes.values():
        words(len(recipe.progression), len(recipe.extra), int(recipe.respects_lock), int(recipe.unlocks),
              *(recipe.lock or (0, 0, 0)))
        for gains, limit in ((recipe.progression, 4), (recipe.extra, 8)):
            for pair in (*gains, *((0, 0),) * (limit - len(gains))):
                words(*pair)
    values.extend(bytes((MAX_RECIPES - len(recipes)) * 124))
    for key in recipes:
        values.extend(bytes.fromhex(key))
    values.extend(bytes((MAX_RECIPES - len(recipes)) * 32))
    words(*(int(key in incoming) for key in recipes), *((0,) * (MAX_RECIPES - len(recipes))))
    for location, mapped in zip(manifest["locations"], mapping, strict=True):
        if type(mapped["area"]) is not int or not 0 <= mapped["area"] <= 0xffffffffffffffff:
            raise ValueError("Unmapped Corruption pickup area")
        words(indices[location["pickup_key"]] if location["local"] else 0xffffffff,
              mapped["area"] >> 32, mapped["area"] & 0xffffffff)
    if len(values) != SIZE:
        raise ValueError("Runtime seed table layout mismatch")
    return bytes(values)
