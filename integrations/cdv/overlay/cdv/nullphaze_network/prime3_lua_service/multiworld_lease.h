/*
 * Peer/session liveness uses the hardware timebase and a bounded lease. Reconnect can
 * replace transport ownership without acknowledging a new item or saving a checkpoint.
 */
/* SPDX-License-Identifier: GPL-3.0-or-later */
#ifndef NULLPHAZE_MULTIWORLD_LEASE_H
#define NULLPHAZE_MULTIWORLD_LEASE_H
/* Broadway's time base is the OS-reported bus clock divided by four. */
static int mw_peer_lease_expired(unsigned long long now, unsigned long long last,
                                 unsigned int bus_clock) {
    return now >= last && now - last >= ((unsigned long long)bus_clock / 4u) * 30u;
}
/* A stalled game poll must not revoke the existing peer's session on resume.
   The lease only permits a different peer to replace an abandoned owner. */
static int mw_peer_may_replace(unsigned int same_peer, unsigned long long now,
                               unsigned long long last, unsigned int bus_clock) {
    return !same_peer && bus_clock >= 100000000u && bus_clock <= 400000000u &&
        mw_peer_lease_expired(now,last,bus_clock);
}
static int mw_peer_successful_reply(unsigned int negotiated, const unsigned char *reply,
                                    unsigned int size) {
    /* Parser HELLO/PING success is 1; addon command success is 0. Use the
       common wire response status rather than either internal convention. */
    return negotiated && size >= 20u && reply[5] == 2u && reply[7] == 0u;
}
#endif
