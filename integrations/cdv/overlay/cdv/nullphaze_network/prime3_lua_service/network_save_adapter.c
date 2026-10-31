/*
 * Pair the native save payload with validated networking receipt records at the IO
 * boundary. Unknown container identity, bounds or coupling state must not become an
 * implicit new checkpoint.
 */
#include "receipt_layout.h"
/* Migrated-copy experiment only. Receipt bytes are preserved, never advanced. */
typedef unsigned int u32;
typedef unsigned char u8;
extern const u8 network_save_profile[80];
extern int network_codec_validate(const u8 *, u32, const u8 *);
extern int network_codec_encode(u8 *, u32, const u8 *, const u8 *, const u8 *);
#ifdef CP3W_RECEIPT_COUPLING
extern void coupling_loaded(const u8 *,const u8 *);
extern int coupling_prepare_save(const u8 *,u8 *);
#endif

struct adapter {
    u32 magic, phase, file, destination;
    u8 records[CP3W_RECORD_BYTES];
    u8 wire[CP3W_WIRE_SIZE] __attribute__((aligned(32)));
};
__attribute__((section(".data.network_save_adapter")))
volatile struct adapter network_save_state = {0x4e535631u,0,0,0,{0},{0}};
#define WORD(a) (*(volatile u32 *)(a))
#define EXPORTED __attribute__((section(".text.network_save_hooks")))

static int valid(u32 address, u32 size) {
    return !(address & 3u) &&
        ((address >= 0x80000000u && address <= 0x81800000u-size) ||
         (address >= 0x90000000u && address <= 0x94000000u-size));
}
static u32 fail(u32 file) {
    if (valid(file,0x16cu)) WORD(file+0x10u)=0xfffffffbu;
    return 0;
}

EXPORTED u32 network_save_read(u32 file, u32 destination, u32 size, u32 offset, u32 origin) {
    u32 task;
    if (network_save_state.magic != 0x4e535631u || (network_save_state.phase != 0u && network_save_state.phase != 3u)
        || size != 65536u || offset || origin || !valid(file,0x16cu) || !valid(destination,size)) return fail(file);
    network_save_state.phase=1;
    network_save_state.file=file;
    network_save_state.destination=destination;
    task=((u32 (*)(u32,u32,u32,u32,u32))0x803fa414u)(file,(u32)network_save_state.wire,CP3W_WIRE_SIZE,0,0);
    if (!task) { network_save_state.phase=0; return fail(file); }
    return task;
}

EXPORTED u32 network_save_read_complete(u32 manager, u32 result) {
    u32 index;
    if (!result) {
        if (network_save_state.phase != 1u || !valid(manager,0x4ae8u)
            || WORD(manager+0x4adcu) != network_save_state.file
            || WORD(manager+0x4ad8u) != network_save_state.destination
            || !network_codec_validate((const u8 *)network_save_state.wire,CP3W_WIRE_SIZE,network_save_profile)) result=0xfffffffbu;
        else {
            u8 *destination=(u8 *)network_save_state.destination;
            for (index=0; index<65536u; ++index) destination[index]=network_save_state.wire[88u+index];
            for (index=0; index<CP3W_RECORD_BYTES; ++index) network_save_state.records[index]=network_save_state.wire[65624u+index];
#ifdef CP3W_RECEIPT_COUPLING
            coupling_loaded(destination,(const u8 *)network_save_state.records);
#endif
        }
    }
    network_save_state.phase=result ? 0u : 3u;
    return ((u32 (*)(u32,u32))0x801d606cu)(manager,result);
}

EXPORTED u32 network_save_write(u32 file, u32 source, u32 size, u32 offset, u32 origin) {
    u32 task;
#ifdef CP3W_MULTIWORLD
    /* The engine creates a new private file from its own blank container.
       Accept no existing gameplay payload on this initialization path. */
    if(network_save_state.magic==0x4e535631u && network_save_state.phase==0u && size==65536u &&
       !offset && !origin && valid(source,size) && valid(file,0x16cu)) {
        const u8 *retail=(const u8 *)source; u32 i,j;
        if(retail[16] || retail[17] || retail[18]) return fail(file);
        for(i=0;i<CP3W_RECORD_BYTES;i++) network_save_state.records[i]=0;
        for(i=0;i<3u;i++) {
            network_save_state.records[CP3W_RECEIPT_SIZE*i]=(u8)i;
            for(j=0;j<16u;j++) network_save_state.records[CP3W_RECEIPT_SIZE*i+4u+j]=network_save_profile[32u+16u*i+j];
        }
        coupling_loaded(retail,(const u8 *)network_save_state.records);
        network_save_state.phase=3;
    }
#endif
    if (network_save_state.magic != 0x4e535631u || network_save_state.phase != 3u || size != 65536u
        || offset || origin || !valid(file,0x16cu) || !valid(source,size)) return fail(file);
#ifdef CP3W_RECEIPT_COUPLING
    if (!coupling_prepare_save((const u8 *)source,(u8 *)network_save_state.records)) return fail(file);
#endif
    network_save_state.phase=2;
    if (!network_codec_encode((u8 *)network_save_state.wire,CP3W_WIRE_SIZE,(const u8 *)source,network_save_profile,
                             (const u8 *)network_save_state.records)) {
        network_save_state.phase=3;
        return fail(file);
    }
    task=((u32 (*)(u32,u32,u32,u32,u32))0x803fa4d8u)(file,(u32)network_save_state.wire,CP3W_WIRE_SIZE,0,0);
    if (!task) { network_save_state.phase=3; return fail(file); }
    return task;
}

void network_save_write_done(void) {
    if (network_save_state.phase == 2u) network_save_state.phase=3;
}
