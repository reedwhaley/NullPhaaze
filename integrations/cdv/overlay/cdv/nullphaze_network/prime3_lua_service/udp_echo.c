/*
 * The owned socket submits callback-driven asynchronous IOS IO. Preserve the accepted
 * blocking receive flags; the experimental NONBLOCK flag uses the Wii constant rather than
 * host socket flags.
 */
/* One owned socket; optionally bounded rearming, no CP3W dispatch or game writes. */
typedef unsigned int u32;
typedef int s32;
typedef unsigned char u8;
struct vector { void *data; u32 size; };
struct udp_diagnostic {
    u32 magic, phase, serial, pending, completed;
    s32 result;
    u32 callbacks, rejected;
    s32 submit;
    u32 submitted_tick, error;
    s32 socket;
    u32 received, sent, ticks;
    s32 ip_handle;
};
#define DATA __attribute__((section(".data.readiness"), aligned(32)))
volatile struct udp_diagnostic udp_probe_state DATA = {
    0x55445031u, 0, 0, 0, 0, 0x7fffffff, 0, 0, 0x7fffffff, 0, 0, -1, 0, 0, 0, -1
};
#if defined(CP3W_TRACKER_READ_ONLY) || defined(CP3W_ITEM_SEQUENCE_TEST) || defined(CP3W_MULTIWORLD)
extern void owned_cp3w_reset_session(void);
volatile u32 udp_tracker_reset_state[8] DATA = {0x54525331u,0,8,0,0,0,0,0};
#endif
u32 udp_create[8] DATA = {2, 2, 0, 0, 0, 0, 0, 0};
u32 udp_bind[16] DATA = {0};
u32 udp_recv_params[8] DATA = {0};
u32 udp_send_params[16] DATA = {0};
struct vector udp_vectors[4] DATA = {{0,0},{0,0},{0,0},{0,0}};
#ifdef CP3W_OWNED_CP3W
u8 udp_rx[512] DATA = {0};
#ifdef CP3W_RX_MEM2
#if !defined(CP3W_OWNED_CP3W) || (defined(CP3W_RX_AUDIT) && CP3W_RX_PREFILL != 0)
#error MEM2 receive requires the owned transport and zero prefill
#endif
/* Reserved before retail OS arena initialization, retained until reboot. */
volatile u32 udp_mem2_reservation[8] DATA = {0x4d325258u,0,0,0,0,512,0,0};
void udp_reserve_mem2(void) {
    volatile u32 *lo=(volatile u32 *)0x80003124u;
    volatile u32 *hi=(volatile u32 *)0x80003128u;
    u32 low=*lo, high=*hi, base;
    if(udp_mem2_reservation[1]) return;
    udp_mem2_reservation[1]=1;
    udp_mem2_reservation[2]=low;
    udp_mem2_reservation[3]=high;
    if(low<0x90000800u || high>0x94000000u || high<low ||
       (low&31u) || (high&31u) || high-low<4096u) return;
    base=high-4096u;
    *hi=base;
    __asm__ volatile("sync" ::: "memory");
    if(*hi!=base) return;
    udp_mem2_reservation[4]=base;
    udp_mem2_reservation[6]=4096;
    udp_mem2_reservation[1]=2;
}
#define udp_rx (*(u8 (*)[512])udp_mem2_reservation[4])
static u32 mem2_owned(void) {
    u32 base=udp_mem2_reservation[4];
    /* Verify both the boot bound and the SDK arena after game initialization. */
    return udp_mem2_reservation[1]==2 && base>=0x90000800u &&
        base<=0x94000000u-4096u && !(base&31u) &&
        *(volatile u32 *)0x80003128u==base &&
        *(volatile u32 *)0x8067e484u==base &&
        *(volatile u32 *)0x80679b6cu>=udp_mem2_reservation[2] &&
        *(volatile u32 *)0x80679b6cu<=base;
}
#endif
u8 udp_tx[512] DATA = {0};
u32 udp_reply_length DATA = 0;
extern u32 owned_cp3w_request(const u8 *,u32,const u8 *,u8 *);
extern u32 owned_cp3w_limit(void);
#ifdef CP3W_RX_AUDIT
#ifndef CP3W_RX_PREFILL
#define CP3W_RX_PREFILL 165
#endif
#if CP3W_RX_PREFILL == 0
/* Match the A5 image's buffer addresses despite constant-folded zero stores. */
__asm__(".section .text.rx_zero_layout,\"ax\"\n.space 64\n.previous");
#endif
volatile u32 udp_receive_audit[16] DATA = {0x52584131u,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
u8 udp_callback_snapshot[512] DATA = {0};
u8 udp_dispatch_snapshot[512] DATA = {0};
static u32 audit_tail(volatile const u8 *data, u32 length) {
    u32 i, value=0;
    if(length<4 || length>sizeof(udp_rx)) return 0;
    for(i=length-4;i<length;i++) value=(value<<8)|data[i];
    return value;
}
static u32 audit_crc(volatile const u8 *data, u32 length) {
    u32 i, bit, crc=0xffffffffu;
    if(length<4 || length>sizeof(udp_rx)) return 0;
    for(i=0;i<length-4;i++) {
        crc^=data[i];
        for(bit=0;bit<8;bit++) crc=(crc>>1)^((crc&1u)?0xedb88320u:0);
    }
    return crc^0xffffffffu;
}
static void audit_receive(u32 length, u32 after) {
    volatile const u8 *uncached=(volatile const u8 *)((u32)udp_rx|0x40000000u);
    u8 *snapshot=after?udp_dispatch_snapshot:udp_callback_snapshot;
    u32 i, head=0;
    __asm__ volatile("sync" ::: "memory");
    udp_receive_audit[after?4:2]=audit_tail(udp_rx,length);
    udp_receive_audit[after?5:3]=audit_tail(uncached,length);
    /* Retain the complete buffer, including untouched sentinel bytes. */
    for(i=0;i<sizeof(udp_rx);i++) snapshot[i]=uncached[i];
    for(i=0;i<4;i++) head=(head<<8)|uncached[i];
    udp_receive_audit[after?15:14]=head;
    udp_receive_audit[11]=CP3W_RX_PREFILL*0x01010101u;
    if(after) {
        udp_receive_audit[6]=audit_crc(udp_rx,length);
        udp_receive_audit[7]=audit_crc(uncached,length);
        udp_receive_audit[8]=udp_vectors[1].size;
        udp_receive_audit[9]=(u32)udp_vectors[1].data;
        udp_receive_audit[10]=udp_probe_state.serial;
    } else udp_receive_audit[1]=length;
    __asm__ volatile("sync" ::: "memory");
}
#endif
#else
u8 udp_rx[64] DATA = {0};
#endif
u8 udp_peer[32] DATA = {0};
#ifdef CP3W_OWNED_CP3W
/* Packet framing and session checks are handled by the existing CP3W parser. */
#elif defined(CP3W_UDP_TX_ONLY)
static const u8 signature[16] = "CP3W-UDP-TX-v1";
#else
static const u8 signature[] = "CP3W-UDP-ECHO-v1";
#endif

static void cache(void *data, u32 size, u32 invalidate) {
    u32 p = (u32)data, end = p + size;
    for (; p < end; p += 32) {
        if (invalidate) __asm__ volatile("dcbi 0,%0" :: "r"(p) : "memory");
        else __asm__ volatile("dcbf 0,%0" :: "r"(p) : "memory");
    }
    __asm__ volatile("sync" ::: "memory");
}

static s32 done(s32 result, void *token) {
    volatile struct udp_diagnostic *d = &udp_probe_state;
    if ((u32)token != (0x55440000u | d->serial) || !d->pending || d->completed) {
        d->rejected++;
        return 0;
    }
    d->result = result;
    d->callbacks++;
#ifdef CP3W_RX_AUDIT
    if(d->phase==5) audit_receive((u32)result,0);
#endif
    __asm__ volatile("sync" ::: "memory");
    d->completed = 1;
    return 0;
}

void udp_probe_tick(s32 fd, u32 ticks) {
    volatile struct udp_diagnostic *d = &udp_probe_state;
    u32 i, command, size;
    void *input;
#ifdef CP3W_RX_MEM2
    if(!mem2_owned()) { d->error=11; d->phase=9; return; }
#endif
    d->ticks = ticks;
    if (d->error || d->phase == 8
#ifdef CP3W_UDP_TX_ONLY
        || d->phase == 13
#endif
#ifdef CP3W_UDP_NONBLOCK
        || d->phase == 12
#endif
    ) return;
    if (!d->phase) d->ip_handle = fd;
    if (fd < 0 || fd != d->ip_handle) { d->error = 9; d->phase = 9; return; }
    if (d->pending) {
        if (!d->completed) {
            if (ticks - d->submitted_tick > (d->phase == 5 ? 1200u : 60u)) {
                d->error = 8; d->phase = 9;
            }
            return;
        }
        d->pending = 0; d->completed = 0;
#ifdef CP3W_UDP_STARTUP
        if (d->phase == 10) {
            if (d->result != 0) { d->error = 10; d->phase = 9; }
            else d->phase = 11;
        } else
#endif
        if (d->phase == 1) {
            if (d->result < 0) { d->error = 1; d->phase = 9; }
            else { d->socket = d->result; d->phase = 2; }
        } else if (d->phase == 3) {
            if (d->result != 0) { d->error = 2; d->phase = 9; }
            else d->phase = 4;
        } else if (d->phase == 5) {
            cache(udp_rx, sizeof(udp_rx), 1);
            cache(udp_peer, sizeof(udp_peer), 1);
#ifdef CP3W_RX_AUDIT
            audit_receive((u32)d->result,1);
#endif
#ifdef CP3W_UDP_NONBLOCK
            /* Raw IOS EAGAIN: one empty receive completed, not an echo or retry. */
            if (d->result == -6) { d->phase = 12; return; }
#endif
#ifdef CP3W_OWNED_CP3W
#if defined(CP3W_TRACKER_READ_ONLY) || defined(CP3W_ITEM_SEQUENCE_TEST) || defined(CP3W_MULTIWORLD)
            /* Dolphin maps a closed UDP peer's ICMP reset to raw IOS -15. */
#ifdef CP3W_MULTIWORLD
            if(d->result == -15) {
#else
            if(d->result == -15 && udp_tracker_reset_state[1] < 8u) {
#endif
                udp_tracker_reset_state[1]++;
                udp_tracker_reset_state[3]=d->serial;
                udp_tracker_reset_state[4]=ticks;
                owned_cp3w_reset_session();
                d->phase=4;
                return;
            }
#endif
            if (d->result < 0 || d->result > (s32)sizeof(udp_rx)) {
                d->error = 3; d->phase = 9; return;
            }
#else
            if (d->result != 32) { d->error = 3; d->phase = 9; return; }
            for (i = 0; i < 16; ++i) if (udp_rx[i] != signature[i]) {
                d->error = 4; d->phase = 9; return;
            }
#endif
            if (udp_peer[0] != 8 || udp_peer[1] != 2 || !(udp_peer[2] | udp_peer[3]) ||
                !udp_peer[4] || udp_peer[4] >= 224) {
                d->error = 5; d->phase = 9; return;
            }
#ifdef CP3W_OWNED_CP3W
            d->received += (u32)d->result;
            udp_reply_length=owned_cp3w_request(udp_rx,(u32)d->result,udp_peer,udp_tx);
            d->phase=udp_reply_length ? 6 : (owned_cp3w_limit() ? 8 : 4);
#else
            d->received += 32; d->phase = 6;
#endif
        } else if (d->phase == 7) {
#ifdef CP3W_OWNED_CP3W
            if (d->result != (s32)udp_reply_length) { d->error = 6; d->phase = 9; }
            else { d->sent += udp_reply_length; d->phase = owned_cp3w_limit() ? 8 : 4; }
#else
            if (d->result != 32) { d->error = 6; d->phase = 9; }
#ifdef CP3W_UDP_TX_ONLY
            else { d->sent = 32; d->phase = 13; }
#elif defined(CP3W_UDP_REARM)
            /* Reuse buffers only after the owned send callback has completed. */
            else { d->sent += 32; d->phase = d->sent < 32u * 32u ? 4 : 8; }
#else
            else { d->sent = 32; d->phase = 8; }
#endif
#endif
        }
#if defined(CP3W_UDP_DWELL) && !defined(CP3W_TRACKER_READ_ONLY) && !defined(CP3W_ITEM_SEQUENCE_TEST) && !defined(CP3W_MULTIWORLD)
        /* Time each quiet phase from consumption of its successful completion. */
        if (!d->error && (d->phase == 11 || d->phase == 2 || d->phase == 4))
            d->submitted_tick = ticks;
#endif
        return;
    }
#if defined(CP3W_UDP_DWELL) && !defined(CP3W_TRACKER_READ_ONLY) && !defined(CP3W_ITEM_SEQUENCE_TEST) && !defined(CP3W_MULTIWORLD)
    if ((d->phase == 11 || d->phase == 2 || d->phase == 4) &&
        ticks - d->submitted_tick < 60u
#ifdef CP3W_OWNED_CP3W
        && d->serial<=3u
#elif defined(CP3W_UDP_REARM)
        && !d->sent
#endif
    ) return;
#endif
    if (d->phase == 0 || d->phase == 2
#ifdef CP3W_UDP_STARTUP
        || d->phase == 11
#endif
    ) {
#ifdef CP3W_UDP_STARTUP
        if (!d->phase) { input = (void *)0; size = 0; command = 31; d->phase = 10; }
        else if (d->phase == 11)
#else
        if (!d->phase)
#endif
        { input = udp_create; size = 12; command = 15; d->phase = 1; }
        else {
            u8 *name = (u8 *)udp_bind + 8;
            udp_bind[0] = (u32)d->socket; udp_bind[1] = 1;
            name[0] = 8; name[1] = 2; name[2] = 0xaa; name[3] = 0x9a;
            input = udp_bind; size = 36; command = 2; d->phase = 3;
        }
        if (size) cache(input, size == 12 ? 32 : 64, 0);
        d->serial++; d->pending = 1; d->completed = 0; d->submitted_tick = ticks;
        d->submit = ((s32 (*)(s32,u32,void *,u32,void *,u32,s32 (*)(s32,void *),void *))0x80504fe0u)(
            fd, command, input, size, (void *)0, 0, done, (void *)(0x55440000u | d->serial));
    } else if (d->phase == 4 || d->phase == 6) {
        u32 inputs, outputs;
#ifdef CP3W_UDP_TX_ONLY
        /* Input-only IOCTLV control: never arm the failing receive path. */
        u8 *name = (u8 *)udp_send_params + 12;
        for (i = 0; i < 16; ++i) udp_rx[i] = signature[i];
        ((u32 *)udp_rx)[4] = CP3W_UDP_TX_NONCE_0;
        ((u32 *)udp_rx)[5] = CP3W_UDP_TX_NONCE_1;
        ((u32 *)udp_rx)[6] = CP3W_UDP_TX_NONCE_2;
        ((u32 *)udp_rx)[7] = CP3W_UDP_TX_NONCE_3;
        udp_send_params[0] = (u32)d->socket; udp_send_params[2] = 1;
        name[0] = 8; name[1] = 2; name[2] = 0xaa; name[3] = 0x9b;
        udp_send_params[4] = CP3W_UDP_TX_HOST;
        udp_vectors[0].data = udp_rx; udp_vectors[0].size = 32;
        udp_vectors[1].data = udp_send_params; udp_vectors[1].size = 40;
        cache(udp_rx, 64, 0); cache(udp_send_params, 64, 0);
        inputs = 2; outputs = 0; command = 13; d->phase = 7;
#else
        if (d->phase == 4) {
#if defined(CP3W_UDP_REARM) || defined(CP3W_OWNED_CP3W)
            /* IOS converts vectors in place; rebuild all vectors below each time. */
            for (i = 0; i < sizeof(udp_rx); ++i) udp_rx[i] =
#ifdef CP3W_RX_AUDIT
                CP3W_RX_PREFILL;
#else
                0;
#endif
            for (i = 0; i < sizeof(udp_peer); ++i) udp_peer[i] = 0;
#endif
            udp_recv_params[0] = (u32)d->socket;
#ifdef CP3W_UDP_PEER_LENGTH
            /* Match the caller-supplied sockaddr capacity used by libogc. */
            udp_peer[0] = 8;
#endif
#ifdef CP3W_UDP_NONBLOCK
            udp_recv_params[1] = 4; /* SO_MSG_NONBLOCK, not host MSG_DONTWAIT. */
#endif
            /* Without the experimental NONBLOCK define, flags stay zero.
               The receive waits in the asynchronous IOS request below; this
               callback-driven path must not become a synchronous game-thread
               recv loop. Preserve the accepted receive mode when documenting
               or rebuilding the migrated patcher. */
            udp_vectors[0].data = udp_recv_params; udp_vectors[0].size = 8;
            udp_vectors[1].data = udp_rx; udp_vectors[1].size = sizeof(udp_rx);
            udp_vectors[2].data = udp_peer; udp_vectors[2].size = 8;
            cache(udp_recv_params, 32, 0); cache(udp_rx, sizeof(udp_rx), 0); cache(udp_peer, 32, 0);
            inputs = 1; outputs = 2; command = 12; d->phase = 5;
        } else {
            udp_send_params[0] = (u32)d->socket; udp_send_params[2] = 1;
            for (i = 0; i < 8; ++i) ((u8 *)udp_send_params)[12 + i] = udp_peer[i];
#ifdef CP3W_OWNED_CP3W
            udp_vectors[0].data = udp_tx; udp_vectors[0].size = udp_reply_length;
            cache(udp_tx, sizeof(udp_tx), 0);
#else
            udp_vectors[0].data = udp_rx; udp_vectors[0].size = 32;
#endif
            udp_vectors[1].data = udp_send_params; udp_vectors[1].size = 40;
            cache(udp_rx, 64, 0); cache(udp_send_params, 64, 0);
            inputs = 2; outputs = 0; command = 13; d->phase = 7;
        }
#endif
        cache(udp_vectors, 32, 0);
        d->serial++; d->pending = 1; d->completed = 0; d->submitted_tick = ticks;
        d->submit = ((s32 (*)(s32,u32,u32,u32,struct vector *,s32 (*)(s32,void *),void *))0x80505384u)(
            fd, command, inputs, outputs, udp_vectors, done, (void *)(0x55440000u | d->serial));
    }
    if (d->submit < 0) { d->pending = 0; d->error = 7; d->phase = 9; }
}
