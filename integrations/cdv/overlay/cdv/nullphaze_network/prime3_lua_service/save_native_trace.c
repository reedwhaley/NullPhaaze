/*
 * Save-event instrumentation passes through retail IO results. It records evidence without
 * changing inventory, checkpoint selection or persistence outcomes.
 */
/* Diagnostic pass-through only: never changes inventory, saves, or IO results. */
typedef unsigned int u32;
typedef u32 (*call1)(u32);
typedef u32 (*call2)(u32, u32);
typedef u32 (*call3)(u32, u32, u32);
typedef u32 (*call4)(u32, u32, u32, u32);
typedef u32 (*call5)(u32, u32, u32, u32, u32);
#ifdef CP3W_NETWORK_SAVE_ADAPTER
extern u32 network_save_write(u32,u32,u32,u32,u32);
extern void network_save_write_done(void);
#endif
#ifdef CP3W_RECEIPT_COUPLING
extern void coupling_load_begin(u32);
extern void coupling_load_end(void);
extern void coupling_stored(u32);
#endif

struct event { u32 word[16]; };
struct trace {
    u32 magic, version, sequence, tracked_file, reserved[4];
    struct event events[128];
};
__attribute__((section(".data.save_native_trace")))
volatile struct trace save_trace_data = {0x53505631u, 1, 0, 0, {0}, {{{0}}}};

#define WORD(a) (*(volatile u32 *)(a))
#define EXPORTED __attribute__((section(".text.save_trace_hooks")))

static int valid(u32 address, u32 size) {
    return !(address & 3u) &&
        ((address >= 0x80000000u && address <= 0x81800000u - size) ||
         (address >= 0x90000000u && address <= 0x94000000u - size));
}

static void record(u32 type, u32 context, u32 a, u32 b, u32 c, u32 slot) {
    u32 sequence = __atomic_fetch_add(&save_trace_data.sequence, 1, __ATOMIC_RELAXED);
    volatile struct event *event = &save_trace_data.events[sequence & 127u];
    u32 game = WORD(0x8067dc0cu);
    u32 stored = valid(slot, 0x3c90u) ? WORD(slot + 0x3c8cu) : 0;
    event->word[0] = 0;
    __asm__ volatile("sync" ::: "memory");
    event->word[1] = type;
    event->word[2] = context;
    event->word[3] = a;
    event->word[4] = b;
    event->word[5] = c;
    event->word[6] = game;
    event->word[7] = valid(game, 0x64u) ? WORD(game + 0x24u) : 0;
    event->word[8] = stored;
    event->word[9] = valid(stored, 0x28u) ? WORD(stored + 0x24u) : 0;
    event->word[10] = valid(game, 0x64u) ? WORD(game + 0x60u) : 0xffffffffu;
    event->word[11] = valid(context, 0x4ae8u) && type == 6u ? WORD(context + 0x4cu) : 0;
    event->word[12] = valid(context, 0x4ae8u) && type == 6u ? WORD(context + 0x50u) : 0;
    event->word[13] = 0;
    event->word[14] = 0;
    event->word[15] = 0;
    __asm__ volatile("sync" ::: "memory");
    event->word[0] = sequence + 1u;
}

#ifdef CP3W_RECEIPT_LIFECYCLE_TRACE
void save_trace_record(u32 type,u32 context,u32 a,u32 b,u32 c) {
    record(type,context,a,b,c,0);
}
#endif

EXPORTED u32 save_trace_crc(u32 data, u32 size, u32 seed) {
    u32 result = ((call3)0x80344f24u)(data, size, seed);
    record(1, data, size, seed, result, 0);
    return result;
}

EXPORTED u32 save_trace_write(u32 file, u32 buffer, u32 size, u32 offset, u32 origin) {
    u32 result;
    save_trace_data.tracked_file = file;
    __asm__ volatile("sync" ::: "memory");
    record(2, file, buffer, size, offset, 0);
#ifdef CP3W_NETWORK_SAVE_ADAPTER
    result = network_save_write(file, buffer, size, offset, origin);
#else
    result = ((call5)0x803fa4d8u)(file, buffer, size, offset, origin);
#endif
    record(3, file, result, origin, 0, 0);
    return result;
}

EXPORTED u32 save_trace_complete(u32 manager, u32 result, u32 mode, u32 error) {
    u32 returned;
    record(5, manager, result, mode, error, 0);
    returned = ((call4)0x801d625cu)(manager, result, mode, error);
#ifdef CP3W_NETWORK_SAVE_ADAPTER
    network_save_write_done();
#endif
    record(6, manager, result, mode, error, 0);
    return returned;
}

EXPORTED u32 save_trace_complete_initial(u32 manager, u32 result) {
    u32 returned;
    record(5, manager, result, 0xffffffffu, 0, 0);
    returned = ((call2)0x801d61a8u)(manager, result);
#ifdef CP3W_NETWORK_SAVE_ADAPTER
    network_save_write_done();
#endif
    record(6, manager, result, 0xffffffffu, 0, 0);
    return returned;
}

EXPORTED u32 save_trace_close(u32 info) {
    u32 result = ((call1)0x80507c8cu)(info);
    u32 file = save_trace_data.tracked_file;
    __asm__ volatile("sync" ::: "memory");
    if (file && info == file + 0xccu) record(7, info, result, file, 0, 0);
    return result;
}

EXPORTED u32 save_trace_safe_close(u32 info) {
    u32 result = ((call1)0x80507d80u)(info);
    u32 file = save_trace_data.tracked_file;
    __asm__ volatile("sync" ::: "memory");
    if (file && info == file + 0xccu) record(8, info, result, file, 0, 0);
    return result;
}

EXPORTED u32 save_trace_snapshot_active(u32 slot) {
    u32 result;
    record(9, slot, 0, 0, 0, slot);
    result = ((call1)0x801d86a4u)(slot);
#ifdef CP3W_RECEIPT_COUPLING
    coupling_stored(slot);
#endif
    record(10, slot, result, 0, 0, slot);
    return result;
}

EXPORTED u32 save_trace_snapshot_stored(u32 slot) {
    u32 result;
    record(11, slot, 0, 0, 0, slot);
    result = ((call1)0x801d8790u)(slot);
#ifdef CP3W_RECEIPT_COUPLING
    coupling_stored(slot);
#endif
    record(12, slot, result, 0, 0, slot);
    return result;
}

EXPORTED u32 save_trace_slot_load(u32 slot, u32 stream) {
    u32 result;
#ifdef CP3W_RECEIPT_COUPLING
    coupling_load_begin(slot);
#endif
    result = ((call2)0x801d84dcu)(slot, stream);
#ifdef CP3W_RECEIPT_COUPLING
    coupling_load_end();
    coupling_stored(slot);
#endif
    record(13, slot, result, stream, 0, slot);
    return result;
}
