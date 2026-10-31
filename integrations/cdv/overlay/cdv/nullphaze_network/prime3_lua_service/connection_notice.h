/*
 * Connection notices consume a presentation edge from negotiated session health. A
 * lost/restored cue must not change inventory, save state or transport ownership.
 */
/* SPDX-License-Identifier: GPL-3.0-or-later */
#ifndef NULLPHAZE_CONNECTION_NOTICE_H
#define NULLPHAZE_CONNECTION_NOTICE_H
#include "multiworld_lease.h"
struct mw_connection_notice { unsigned int seen, live; };
static int mw_connection_live(unsigned int verified, unsigned int negotiated,
                              unsigned int fault, unsigned long long now,
                              unsigned long long last, unsigned int bus_clock) {
    return verified && negotiated && !fault && now >= last &&
        bus_clock >= 100000000u && bus_clock <= 400000000u &&
        !mw_peer_lease_expired(now,last,bus_clock);
}
/* One global consumer survives room reloads. Initial offline state is quiet. */
static unsigned int mw_connection_notice_claim(struct mw_connection_notice *state,
                                                unsigned int live) {
    live = !!live;
    if(!state->seen) {
        if(live) { state->seen=1; state->live=1; }
        return 0;
    }
    if(state->live==live) return 0;
    state->live=live;
    return live ? 2u : 1u;
}
#endif
