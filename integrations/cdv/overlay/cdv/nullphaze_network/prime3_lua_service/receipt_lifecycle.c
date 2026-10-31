/*
 * These pass-through ownership traces observe checkpoint handoffs. Trace callbacks must
 * not advance receipts, grant inventory or alter the retail save result.
 */
/* Diagnostic-only checkpoint ownership trace. No receipt or inventory writes. */
typedef unsigned int u32;
typedef unsigned char u8;
extern void save_trace_record(u32, u32, u32, u32, u32);
extern void network_codec_sha256(const u8 *, u32, u8 *);
#ifdef CP3W_RECEIPT_COUPLING
extern void coupling_checkpoint(u32,u32);
extern void coupling_before_install(u32,u32);
extern void coupling_selected_slot(u32);
extern void coupling_source(u32);
extern void coupling_begin_construct(u32);
#endif
#define WORD(a) (*(volatile u32 *)(a))
#define EXPORTED __attribute__((section(".text.receipt_lifecycle_hooks")))

static int valid(u32 address, u32 size) {
    return !(address & 3u) &&
        ((address >= 0x80000000u && address <= 0x81800000u-size) ||
         (address >= 0x90000000u && address <= 0x94000000u-size));
}

static void fingerprint(u32 vector) {
    u32 size=0, data=0, digest[8];
    if (valid(vector,12)) { size=WORD(vector); data=WORD(vector+8); }
    if (size != 0x3c86u || !valid(data,0x3c86u)) {
        save_trace_record(29,vector,size,data,0);
        return;
    }
    network_codec_sha256((const u8 *)data,size,(u8 *)digest);
    save_trace_record(29,vector,size,data,1);
    save_trace_record(30,vector,digest[0],digest[1],digest[2]);
    save_trace_record(31,vector,digest[3],digest[4],digest[5]);
    save_trace_record(32,vector,digest[6],digest[7],0);
}

EXPORTED u32 receipt_trace_slot_checkpoint(u32 game) {
    u32 result, slot=valid(game,0x1a50u) ? WORD(game+0x60u) : 0xffffffffu;
    u32 vector=slot < 3u ? game+0x14dcu+12u*slot : 0;
    save_trace_record(14,game,slot,vector,0);
    result=((u32 (*)(u32))0x800ba8ccu)(game);
    save_trace_record(15,game,slot,vector,result);
    fingerprint(vector);
#ifdef CP3W_RECEIPT_COUPLING
    coupling_checkpoint(game,vector);
#endif
    return result;
}

EXPORTED u32 receipt_trace_backup_checkpoint(u32 game) {
    u32 result, vector=valid(game,0x1a50u) ? game+0x1500u : 0;
    save_trace_record(16,game,vector,0,0);
    result=((u32 (*)(u32))0x800baa98u)(game);
    save_trace_record(17,game,vector,0,result);
    fingerprint(vector);
#ifdef CP3W_RECEIPT_COUPLING
    coupling_checkpoint(game,vector);
#endif
    return result;
}

EXPORTED u32 receipt_trace_select_slot(u32 vectors,u32 slot) {
    u32 result=((u32 (*)(u32,u32))0x802efc90u)(vectors,slot);
    save_trace_record(18,vectors,slot,result,0);
#ifdef CP3W_RECEIPT_COUPLING
    coupling_selected_slot(slot);
#endif
    return result;
}

EXPORTED u32 receipt_trace_source_vector(u32 vector) {
    u32 result=((u32 (*)(u32))0x802f0be4u)(vector);
    save_trace_record(20,vector,result,0,0);
    fingerprint(vector);
#ifdef CP3W_RECEIPT_COUPLING
    coupling_source(vector);
#endif
    return result;
}

EXPORTED u32 receipt_trace_construct(u32 game,u32 stream,u32 flag) {
    u32 result;
    save_trace_record(22,game,stream,flag,0);
#ifdef CP3W_RECEIPT_COUPLING
    coupling_begin_construct(game);
#endif
    result=((u32 (*)(u32,u32,u32))0x800b76c4u)(game,stream,flag);
    save_trace_record(23,result,stream,flag,game);
    return result;
}

EXPORTED u32 receipt_trace_install(u32 holder,u32 game) {
    u32 result;
    save_trace_record(24,holder,game,valid(holder,4) ? WORD(holder) : 0,0);
#ifdef CP3W_RECEIPT_COUPLING
    coupling_before_install(holder,game);
#endif
    result=((u32 (*)(u32,u32))0x802f0b9cu)(holder,game);
    save_trace_record(25,holder,game,valid(holder,4) ? WORD(holder) : 0,result);
    return result;
}
