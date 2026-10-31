/*
 * The native recipe ABI fixes 63 resources, four progression stages and eight extras. Keep
 * the C table layout paired with the Python seed encoder.
 */
/* SPDX-License-Identifier: GPL-3.0-or-later
 * Nullphaze resource planner. No memory addresses or engine calls. */
#ifndef NULLPHAZE_MULTIWORLD_PLAN_H
#define NULLPHAZE_MULTIWORLD_PLAN_H
typedef unsigned int mw_u32;
#define MW_RESOURCE_COUNT 63u
#define MW_MAX_STAGES 4u
#define MW_MAX_EXTRAS 8u
struct mw_gain { mw_u32 resource, quantity; };
struct mw_recipe {
    mw_u32 stages, extras, respects_lock, unlocks;
    mw_u32 launcher, target, temporary;
    struct mw_gain progression[MW_MAX_STAGES], extra[MW_MAX_EXTRAS];
};
#ifdef _WIN32
#define MW_EXPORT __declspec(dllexport)
#else
#define MW_EXPORT
#endif
MW_EXPORT int mw_plan(const struct mw_recipe *, const mw_u32 *, const mw_u32 *, mw_u32 *);
#endif
