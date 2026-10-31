/*
 * The owned KD backend and withdrawn legacy lifecycle remain separate compile-time modes.
 * Readiness evidence must not re-enable the rejected IOS lifecycle or imply grant
 * authorization.
 */
/* Separate compile-time backends: withdrawn legacy and owned KD-only diagnostic. */
typedef unsigned int u32;
typedef int s32;
typedef unsigned short u16;
typedef unsigned char u8;
#if defined(CP3W_TRACKER_READ_ONLY) || defined(CP3W_ITEM_SEQUENCE_TEST) || defined(CP3W_MULTIWORLD)
#define READINESS_START_TICKS 1u
#else
#define READINESS_START_TICKS 90u
#endif
#ifdef CP3W_UDP_ECHO
extern void udp_probe_tick(s32, u32);
extern volatile u32 udp_probe_state[16];
#ifdef CP3W_OWNED_CP3W
extern volatile u32 owned_cp3w_diagnostic[16], owned_cp3w_state[8];
#ifdef CP3W_RX_AUDIT
extern volatile u32 udp_receive_audit[16];
#endif
#endif
#endif
struct diagnostic {
    u32 magic, stage, ticks, nwc_calls, boot_calls;
    s32 nwc_result, boot_result, descriptor;
    u32 descriptor_changes, host_id, queries;
    s32 submit_result, callback_result;
    u32 pending, completed, submitted_tick, callbacks, rejected_callbacks, error;
    s32 borrowed_descriptor;
};
volatile struct diagnostic readiness_state __attribute__((section(".data.readiness"), aligned(32))) = {
    0x52445931u, 0, 0, 0, 0, 0x7fffffffu, 0x7fffffffu, -1,
    0, 0, 0, 0x7fffffff, 0x7fffffff, 0, 0, 0, 0, 0, 0, -1
};

#ifndef CP3W_KD_READINESS
static s32 descriptor(void) {
    u32 sda;
    __asm__ volatile("mr %0,13" : "=r"(sda));
    if (sda < 0x80010000u || sda >= 0x81800000u || (sda & 3u)) return -1;
    return *(volatile const s32 *)(sda - 26024u);
}
#else
volatile u32 kd_output[8] __attribute__((section(".data.readiness"), aligned(32))) = {
    0x7fffffffu, 0x7fffffffu, 0x7fffffffu, 0x7fffffffu,
    0x7fffffffu, 0x7fffffffu, 0x7fffffffu, 0x7fffffffu
};
#endif

static s32 completed(s32 result, void *token) {
    if ((u32)token != (0x52440000u | readiness_state.queries) || !readiness_state.pending || readiness_state.completed) {
        readiness_state.rejected_callbacks++;
        return 0;
    }
    readiness_state.callback_result = result;
    readiness_state.callbacks++;
    __asm__ volatile("sync" ::: "memory");
    readiness_state.completed = 1;
    return 0;
}

#ifndef CP3W_NO_DIAGNOSTICS
/* Same bounded 3x5 XFB technique as the existing native diagnostic overlay. */
static u16 glyph(char c) {
    static const u16 letters[] = {
        0x2bed,0x6bae,0x3923,0x6b6e,0x79a7,0x79a4,0x397b,0x5bed,0x7497,
        0x124a,0x5bad,0x4927,0x5fed,0x5f6d,0x2b6a,0x6ba4,0x2b7b,0x6bad,
        0x388e,0x7492,0x5b6f,0x5b6a,0x5b7f,0x5aad,0x5a92,0x72a7
    };
    static const u16 digits[] = {0x7b6f,0x2492,0x73e7,0x73cf,0x5bc9,0x79cf,0x79ef,0x7249,0x7bef,0x7bcf};
    if (c >= '0' && c <= '9') return digits[c - '0'];
    if (c >= 'A' && c <= 'Z') return letters[c - 'A'];
    return 0;
}

static void hex(char *out, u32 value) {
    static const char digits[] = "0123456789ABCDEF";
    u32 i;
    for (i = 0; i < 8; ++i) out[i] = digits[(value >> (28 - 4 * i)) & 15];
}

static void line(u8 *fb, u32 stride, u32 row, const char *text) {
    u32 col, y, x, sy, sx;
    for (col = 0; text[col] && col < 72; ++col) {
        u16 bits = glyph(text[col]);
        for (y = 0; y < 5; ++y) for (x = 0; x < 3; ++x)
            for (sy = 0; sy < 2; ++sy) for (sx = 0; sx < 2; ++sx) {
                u32 pixel = (12 + row * 12 + y * 2 + sy) * stride + 12 + col * 8 + x * 2 + sx;
                fb[pixel * 2] = (bits & (1u << ((4 - y) * 3 + 2 - x))) ? 235 : 32;
            }
    }
}

void readiness_draw(void) {
    volatile const u16 *vi = (volatile const u16 *)0xcc002000u;
    u32 width = ((vi[0x48 / 2] >> 8) & 0x7fu) * 16u;
    u32 stride = (vi[0x48 / 2] & 0xffu) * 16u;
    u32 height = (vi[0] >> 4) & 0x3ffu;
    u32 reg, physical, i, start, end, index;
    char text[] = "WC 00000000 BOO 00000000";
    const u32 values[12] = {
        readiness_state.stage, readiness_state.ticks,
        (u32)readiness_state.nwc_result, (u32)readiness_state.boot_result,
#ifdef CP3W_KD_READINESS
        (u32)readiness_state.descriptor, readiness_state.queries,
        kd_output[0],
#ifdef CP3W_IP_READINESS
        readiness_state.host_id,
#else
        kd_output[1],
#endif
        (u32)readiness_state.submit_result, readiness_state.callbacks,
#else
        (u32)readiness_state.descriptor, readiness_state.descriptor_changes,
        readiness_state.host_id, readiness_state.queries,
        (u32)readiness_state.submit_result, (u32)readiness_state.callback_result,
#endif
        readiness_state.pending, readiness_state.error
    };
#ifdef CP3W_KD_READINESS
    static const char * const labels[] = {"PH 00000000 TIC 00000000", "OP 00000000 IO  00000000",
        "FD 00000000 TOK 00000000",
#ifdef CP3W_IP_READINESS
        "NW 00000000 IP  00000000",
#else
        "NW 00000000 W1  00000000",
#endif
        "SU 00000000 CB  00000000", "PN 00000000 ERR 00000000"};
#else
    static const char * const labels[] = {"PH 00000000 TIC 00000000", "WC 00000000 BOO 00000000",
        "FD 00000000 CHG 00000000", "IP 00000000 TRY 00000000",
        "SU 00000000 CB  00000000", "PN 00000000 ERR 00000000"};
#endif
    if (width < 600 || width > 720 || stride < width || stride > 1024 || height <
#ifdef CP3W_OWNED_CP3W
        224
#elif defined(CP3W_UDP_ECHO)
        160
#else
        100
#endif
        || height > 576) return;
    for (index = 0; index < 2; ++index) {
        reg = ((u32)vi[(0x1c + index * 8) / 2] << 16) | vi[(0x1e + index * 8) / 2];
        physical = (reg & 0xffffffu) << ((reg & 0x10000000u) ? 5 : 0);
        if ((physical & 3u) || !(
            (physical >= 0x100000u && physical <= 0x17c0000u - stride * height * 2u) ||
            (physical >= 0x10000000u && physical <= 0x14000000u - stride * height * 2u))) continue;
        {
            u8 *fb = (u8 *)(physical | 0x80000000u);
#ifdef CP3W_UDP_ECHO
#ifdef CP3W_OWNED_CP3W
#ifdef CP3W_RX_AUDIT
#if defined(CP3W_RX_MEM2)
            line(fb, stride, 0, "CP3W RX MEM2 NO GRANTS");
#elif CP3W_RX_PREFILL == 0
            line(fb, stride, 0, "CP3W RX ZERO NO GRANTS");
#else
            line(fb, stride, 0, "CP3W RX A5 NO GRANTS");
#endif
#else
#ifdef CP3W_TRACKER_READ_ONLY
            line(fb, stride, 0, "CP3W TRACKER READ ONLY");
#else
            line(fb, stride, 0, "CP3W OWNED SESSION GRANT");
#endif
#endif
#elif defined(CP3W_UDP_TX_ONLY)
            line(fb, stride, 0, "CP3W UDP TX ONLY");
#elif defined(CP3W_UDP_REARM)
            line(fb, stride, 0, "CP3W UDP REARM32");
#elif defined(CP3W_UDP_PEER_LENGTH)
            line(fb, stride, 0, "CP3W UDP PEER LEN8");
#else
            line(fb, stride, 0, "CP3W UDP ECHO PROBE");
#endif
#elif defined(CP3W_KD_READINESS)
#ifdef CP3W_IP_READINESS
            line(fb, stride, 0, "CP3W OWNED IP NO SOCKETS");
#else
            line(fb, stride, 0, "CP3W KD ONLY NO SOCKETS");
#endif
#else
            line(fb, stride, 0, "CP3W READINESS NO SOCKETS");
#endif
            for (i = 0; i < 6; ++i) {
                u32 c;
                for (c = 0; c < sizeof(text); ++c) text[c] = labels[i][c];
                hex(text + 3, values[i * 2]); hex(text + 16, values[i * 2 + 1]);
                line(fb, stride, i + 1, text);
            }
            start = (u32)fb + 12 * stride * 2;
#ifdef CP3W_UDP_ECHO
            {
                static const char * const extra[] = {"UP 00000000 SOC 00000000", "RX 00000000 TX  00000000",
                    "US 00000000 UER 00000000", "UR 00000000 UCB 00000000"};
                const u32 more[] = {udp_probe_state[1],udp_probe_state[11],udp_probe_state[12],udp_probe_state[13],
                    udp_probe_state[2],udp_probe_state[10],udp_probe_state[5],udp_probe_state[6]};
                for (i = 0; i < 4; ++i) {
                    u32 c;
                    for (c = 0; c < sizeof(text); ++c) text[c] = extra[i][c];
                    hex(text + 3, more[i * 2]); hex(text + 16, more[i * 2 + 1]);
                    line(fb, stride, 7 + i, text);
                }
            }
#ifdef CP3W_OWNED_CP3W
            {
                static const char * const audit[] = {"ST 00000000 FR  00000000", "IN 00000000 CP  00000000",
                    "LN 00000000 DL  00000000", "RC 00000000 CC  00000000",
                    "DR 00000000 PL  00000000", "NG 00000000 RJ  00000000"};
                const u32 data[] = {owned_cp3w_diagnostic[2],owned_cp3w_diagnostic[3],
                    owned_cp3w_diagnostic[5],owned_cp3w_diagnostic[6],owned_cp3w_diagnostic[1],owned_cp3w_diagnostic[7],
                    owned_cp3w_diagnostic[8],owned_cp3w_diagnostic[9],owned_cp3w_diagnostic[4],owned_cp3w_diagnostic[10],
                    owned_cp3w_diagnostic[11],owned_cp3w_state[5]};
                for(i=0;i<6;i++) {
                    u32 c;
                    for(c=0;c<sizeof(text);c++) text[c]=audit[i][c];
                    hex(text+3,data[i*2]); hex(text+16,data[i*2+1]);
                    line(fb,stride,11+i,text);
                }
            }
#ifdef CP3W_RX_AUDIT
            {
                static const char *const labels[] = {"BC 00000000 BU  00000000", "AC 00000000 AU  00000000",
                    "CK 00000000 UK  00000000", "BH 00000000 AH  00000000"};
                for(i=0;i<4;i++) {
                    u32 c;
                    for(c=0;c<sizeof(text);c++) text[c]=labels[i][c];
                    hex(text+3,udp_receive_audit[i==3?14:2+i*2]); hex(text+16,udp_receive_audit[i==3?15:3+i*2]);
                    line(fb,stride,3+i,text);
                }
                {
                    char address[]="IP 00000000 AS  00000000";
                    hex(address+3,readiness_state.host_id); hex(address+16,udp_receive_audit[10]);
                    line(fb,stride,2,address);
                }
            }
#endif
            end = (u32)fb + 224 * stride * 2;
#else
            end = (u32)fb + 152 * stride * 2;
#endif
#else
            end = (u32)fb + 96 * stride * 2;
#endif
            for (start &= ~31u; start < end; start += 32) __asm__ volatile("dcbf 0,%0" :: "r"(start) : "memory");
            __asm__ volatile("sync" ::: "memory");
        }
    }
}

#else
void readiness_draw(void) {}
#endif

#ifndef CP3W_KD_READINESS
int readiness_tick(void *lua) {
    volatile struct diagnostic *d = &readiness_state;
    s32 fd;
    (void)lua;
    d->ticks++;
    fd = descriptor();
    if (fd != d->descriptor) { d->descriptor_changes++; d->descriptor = fd; }
    if (d->error) {
        /* Terminal errors stay latched even if a timed-out callback arrives. */
    } else if (d->borrowed_descriptor >= 0 && fd != d->borrowed_descriptor) {
        d->stage = 5; d->error = 7;
    } else if (d->pending) {
        if (d->completed) {
            d->pending = 0; d->completed = 0;
            if ((u32)d->callback_result && ((u32)d->callback_result >> 24) != 0xffu) {
                d->host_id = (u32)d->callback_result; d->stage = 4;
            } else {
                d->host_id = 0;
                d->stage = d->queries < 120 ? 3 : 5;
                if (d->stage == 5) d->error = 4;
            }
        } else if (d->ticks - d->submitted_tick > 60) {
            /* Keep ownership of outstanding callback state; never reuse it. */
            d->stage = 6; d->error = 5;
        }
    } else if (d->stage == 0 && d->ticks >= 90) {
        d->stage = 1;
    } else if (d->stage == 1) {
        d->nwc_calls++;
        d->nwc_result = ((s32 (*)(void))0x805541b8u)();
        d->stage = d->nwc_result < 0 ? 5 : 2;
        if (d->stage == 5) d->error = 1;
    } else if (d->stage == 2) {
        d->boot_calls++;
        d->boot_result = ((s32 (*)(void))0x80508dd4u)();
        d->descriptor = descriptor();
        d->stage = d->boot_result != 0 || d->descriptor < 0 ? 5 : 3;
        if (d->stage == 3) d->borrowed_descriptor = d->descriptor;
        if (d->stage == 5) d->error = 2;
    } else if ((d->stage == 3 || d->stage == 4) && d->queries < 120 &&
               (!d->queries || d->ticks - d->submitted_tick >= 10)) {
        if (d->descriptor < 0) { d->stage = 5; d->error = 3; }
        else {
            d->queries++; d->pending = 1; d->completed = 0; d->submitted_tick = d->ticks;
            d->submit_result = ((s32 (*)(s32,u32,void *,u32,void *,u32,s32 (*)(s32,void *),void *))0x80504fe0u)(
                d->descriptor, 16, (void *)0, 0, (void *)0, 0, completed, (void *)(0x52440000u | d->queries));
            if (d->submit_result < 0) { d->pending = 0; d->stage = 5; d->error = 6; }
        }
    }
    return 0;
}
#else
int readiness_tick(void *lua) {
    volatile struct diagnostic *d = &readiness_state;
    (void)lua;
    d->ticks++;
    if (d->error) return 0;
    if (d->stage == 10) {
#ifdef CP3W_UDP_ECHO
        udp_probe_tick(d->descriptor, d->ticks);
#endif
        return 0;
    }
#ifndef CP3W_IP_READINESS
    if (d->stage == 5) return 0;
#endif
    if (d->pending) {
        if (d->completed) {
            d->pending = 0; d->completed = 0;
            if (d->queries == 1) {
                d->nwc_result = d->callback_result;
                if (d->callback_result < 0) { d->stage = 6; d->error = 1; }
                else { d->descriptor = d->callback_result; d->stage = 3; }
            }
#ifdef CP3W_IP_READINESS
            else if (d->queries == 3) {
                if (d->callback_result < 0) { d->stage = 6; d->error = 7; }
                else { d->descriptor = d->callback_result; d->stage = 8; }
            } else if (d->queries >= 4) {
                u32 ip = (u32)d->callback_result;
                d->host_id = ip;
                if ((ip >> 24) == 0xffu || (!ip && d->queries >= 15)) {
                    d->stage = 6; d->error = 10;
                } else if (!ip) {
                    /* A zero snapshot may precede IP readiness; do not reopen devices. */
                    d->stage = 8;
                    d->submitted_tick = d->ticks;
                }
                else d->stage = 10;
            }
#endif
            else {
                d->boot_result = d->callback_result;
                __asm__ volatile("dcbi 0,%0; sync" :: "r"(kd_output) : "memory");
                if (d->callback_result < 0) { d->stage = 6; d->error = 2; }
                else if ((s32)kd_output[0] < 0 && (s32)kd_output[0] != -15) {
                    d->stage = 6; d->error = 3;
                } else d->stage = 5;
            }
        } else if (d->ticks - d->submitted_tick > 60) { d->stage = 6; d->error = 4; }
        return 0;
    }
    if (d->stage == 0 && d->ticks >= READINESS_START_TICKS) d->stage = 1;
    else if (d->stage == 1) {
        d->queries = 1; d->pending = 1; d->completed = 0; d->submitted_tick = d->ticks;
        d->stage = 2;
        d->submit_result = ((s32 (*)(const char *,s32,s32 (*)(s32,void *),void *))0x80504668u)(
            "/dev/net/kd/request", 0, completed, (void *)0x52440001u);
        if (d->submit_result < 0) { d->pending = 0; d->stage = 6; d->error = 5; }
    } else if (d->stage == 3) {
        d->queries = 2; d->pending = 1; d->completed = 0; d->submitted_tick = d->ticks;
        d->stage = 4;
        __asm__ volatile("dcbf 0,%0; sync" :: "r"(kd_output) : "memory");
        d->submit_result = ((s32 (*)(s32,u32,void *,u32,void *,u32,s32 (*)(s32,void *),void *))0x80504fe0u)(
            d->descriptor, 6, (void *)0, 0, (void *)kd_output, 32, completed, (void *)0x52440002u);
        if (d->submit_result < 0) { d->pending = 0; d->stage = 6; d->error = 6; }
    }
#ifdef CP3W_IP_READINESS
    else if (d->stage == 5) {
        /* Only an explicit zero KD result may authorize the IP experiment. */
        if (d->boot_result != 0 || kd_output[0] != 0) { d->stage = 6; d->error = 11; return 0; }
        d->borrowed_descriptor = d->descriptor; /* This is our retained KD handle, never retail-owned. */
        d->descriptor = -1;
        d->queries = 3; d->pending = 1; d->completed = 0; d->submitted_tick = d->ticks;
        d->stage = 7;
        d->submit_result = ((s32 (*)(const char *,s32,s32 (*)(s32,void *),void *))0x80504668u)(
            "/dev/net/ip/top", 0, completed, (void *)0x52440003u);
        if (d->submit_result < 0) { d->pending = 0; d->stage = 6; d->error = 8; }
    } else if (d->stage == 8) {
        if (d->queries >= 4 && d->ticks - d->submitted_tick < 10) return 0;
        d->queries++; d->pending = 1; d->completed = 0; d->submitted_tick = d->ticks;
        d->stage = 9;
        d->submit_result = ((s32 (*)(s32,u32,void *,u32,void *,u32,s32 (*)(s32,void *),void *))0x80504fe0u)(
            d->descriptor, 16, (void *)0, 0, (void *)0, 0, completed, (void *)(0x52440000u | d->queries));
        if (d->submit_result < 0) { d->pending = 0; d->stage = 6; d->error = 9; }
    }
#endif
    return 0;
}
#endif

int readiness_render(void *lua) {
    (void)lua;
    readiness_draw();
    return 0;
}
