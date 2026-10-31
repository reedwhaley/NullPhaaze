/*
 * The frame-completion pump owns the half-second native network cadence independently of
 * room Lua. Preserve the supported EndScene guard and retain Lua ownership of receipt
 * application.
 */
/* SPDX-License-Identifier: GPL-3.0-or-later
 * Transport-only pump on the caller of retail CGraphics::EndScene. No Lua APIs,
 * inventory mutators, receipt commits, save operations or presentation calls. */
#include "frame_poll.h"
typedef unsigned int u32;
extern int readiness_tick(void *);
volatile u32 network_frame_poll_state[4]; /* entries, steps, started, busy */
static unsigned long long network_frame_last;
#ifdef MW_HOST_TEST
extern unsigned long long mw_test_frame_time;
extern u32 mw_test_frame_clock;
static unsigned long long frame_timebase(void) { return mw_test_frame_time; }
#else
static unsigned long long frame_timebase(void) {
    u32 high,low,again;
    do {
        __asm__ volatile("mftbu %0" : "=r"(high));
        __asm__ volatile("mftb %0" : "=r"(low));
        __asm__ volatile("mftbu %0" : "=r"(again));
    } while(high!=again);
    return ((unsigned long long)high<<32)|low;
}
#endif
void network_frame_poll(void) {
    unsigned long long now;
    u32 clock;
    network_frame_poll_state[0]++;
    if(network_frame_poll_state[3]) return;
    now=frame_timebase();
#ifdef MW_HOST_TEST
    clock=mw_test_frame_clock;
#else
    clock=*(volatile u32 *)0x800000f8u;
#endif
    if(!mw_frame_poll_due(now,network_frame_last,clock,network_frame_poll_state[2])) return;
    network_frame_poll_state[3]=1;
    network_frame_last=now; network_frame_poll_state[2]=1;
    readiness_tick((void *)0);
    network_frame_poll_state[1]++;
    network_frame_poll_state[3]=0;
}
