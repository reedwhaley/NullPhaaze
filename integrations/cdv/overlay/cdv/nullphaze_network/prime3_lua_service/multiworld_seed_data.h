/*
 * The header fixes the seed-data region and its C structure sizes. Python personalization
 * must preserve those offsets and stay inside the declared region.
 */
/* SPDX-License-Identifier: GPL-3.0-or-later
 * Fixed-size, seed-authorized configuration. No executable bytes or addresses. */
#ifndef NULLPHAZE_MULTIWORLD_SEED_DATA_H
#define NULLPHAZE_MULTIWORLD_SEED_DATA_H
#include "multiworld_plan.h"
struct mw_seed_configuration {
    unsigned char magic[8];
    mw_u32 schema, size;
    unsigned char world[16], seed[32];
    mw_u32 save_slot, recipe_count;
    mw_u32 limits[63], native_ids[63];
    struct mw_recipe recipes[256];
    unsigned char keys[256][32];
    mw_u32 incoming_allowed[256], locations[100][3];
};
extern const struct mw_seed_configuration mw_seed_data;
typedef char mw_seed_configuration_size_check[sizeof(struct mw_seed_configuration)==42736 ? 1 : -1];
#define MW_SAVE_SLOT (mw_seed_data.save_slot)
#define MW_RECIPE_COUNT (mw_seed_data.recipe_count)
#define mw_world (mw_seed_data.world)
#define mw_seed (mw_seed_data.seed)
#define mw_limits (mw_seed_data.limits)
#define mw_native_ids (mw_seed_data.native_ids)
#define mw_recipes (mw_seed_data.recipes)
#define mw_recipe_keys (mw_seed_data.keys)
#define mw_incoming_allowed (mw_seed_data.incoming_allowed)
#define mw_locations (mw_seed_data.locations)
#endif
