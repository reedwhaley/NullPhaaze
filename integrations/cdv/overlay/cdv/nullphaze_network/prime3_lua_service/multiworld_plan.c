/*
 * Plan logical resource deltas against the compiled limits before touching native
 * inventory. Progression, launcher locks and temporary expansions must follow the same
 * recipe semantics as the host.
 */
/* SPDX-License-Identifier: GPL-3.0-or-later */
#include "multiworld_plan.h"
static int permitted(mw_u32 id) {
    return id < 19u || (id >= 20u && id <= 35u) || id == 37u || id == 38u || id == 39u ||
        id == 43u || id == 44u || id == 46u || (id >= 59u && id <= 62u);
}
static int valid_gain(const struct mw_gain *g, const mw_u32 *limits) {
    return g->resource < MW_RESOURCE_COUNT && permitted(g->resource) && g->quantity <= limits[g->resource];
}
static void add(mw_u32 *out, mw_u32 id, mw_u32 amount, const mw_u32 *limits) {
    mw_u32 room = limits[id] - out[id];
    out[id] += amount < room ? amount : room;
}
int mw_plan(const struct mw_recipe *r, const mw_u32 *in, const mw_u32 *limits, mw_u32 *out) {
    mw_u32 i,stage=0,id,locked=0;
    if(!r || !in || !limits || !out || out==in || r->stages>MW_MAX_STAGES || r->extras>MW_MAX_EXTRAS ||
       r->respects_lock>1u || r->unlocks>1u) return 0;
    for(i=0;i<MW_RESOURCE_COUNT;i++) if(in[i]>limits[i]) return 0;
    for(i=0;i<r->stages;i++) if(!valid_gain(&r->progression[i],limits)) return 0;
    for(i=0;i<r->extras;i++) if(!valid_gain(&r->extra[i],limits)) return 0;
    if(r->launcher || r->target || r->temporary) {
        if(!((r->launcher==59u && r->target==4u && r->temporary==61u) ||
             (r->launcher==60u && r->target==44u && r->temporary==62u))) return 0;
        locked=r->respects_lock && !r->unlocks && !in[r->launcher];
    } else if(r->unlocks) return 0;
    for(i=0;i<MW_RESOURCE_COUNT;i++) out[i]=in[i];
    if(r->stages) {
        while(stage+1u<r->stages && in[r->progression[stage].resource]) stage++;
        id=r->progression[stage].resource;
        if(locked && id==r->target) id=r->temporary;
        add(out,id,r->progression[stage].quantity,limits);
    }
    for(i=0;i<r->extras;i++) {
        id=r->extra[i].resource;
        if(locked && id==r->target) id=r->temporary;
        add(out,id,r->extra[i].quantity,limits);
    }
    if(r->unlocks) {
        out[r->launcher]=1;
        add(out,r->target,out[r->temporary],limits);
        out[r->temporary]=0;
    }
    return 1;
}
