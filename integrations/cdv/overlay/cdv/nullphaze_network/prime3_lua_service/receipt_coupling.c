/*
 * Bind each receipt to its actual native checkpoint/slot bytes. The live cursor can lead
 * disk; only a validated disk read advances the saved anchor used for replay evidence.
 */
#include "receipt_layout.h"
/* Experimental checkpoint-associated receipt views. No inventory/grant calls. */
typedef unsigned int u32;
typedef unsigned char u8;
extern void network_codec_sha256(const u8 *,u32,u8 *);
extern const u8 network_save_profile[80];
extern void save_trace_record(u32,u32,u32,u32,u32);
#define WORD(a) (*(volatile u32 *)(a))
#define EXPORTED __attribute__((section(".text.receipt_coupling_hooks")))
struct view { u32 valid; u8 hash[32], receipt[CP3W_RECEIPT_SIZE]; };
struct owner { u32 game, generation, slot; u8 current[CP3W_RECEIPT_SIZE]; struct view vector[4]; };
struct coupling {
    u32 magic, fault, epoch, generation, load_slot, selected_valid, selected_slot;
    u32 ticks, test_stage;
    u8 selected[CP3W_RECEIPT_SIZE];
    struct view disk[3], stored[3], pending[4];
    struct owner owners[8];
};
__attribute__((section(".data.receipt_coupling")))
volatile struct coupling receipt_coupling_state = { .magic=0x43505231u };
#define S receipt_coupling_state

static void copy(volatile void *to,const volatile void *from,u32 n) {
    volatile u8 *d=to; const volatile u8 *s=from;
    while(n--) *d++=*s++;
}
static void clear(volatile void *to,u32 n) { volatile u8 *d=to; while(n--) *d++=0; }
static int equal(const volatile void *a,const volatile void *b,u32 n) {
    const volatile u8 *p=a,*q=b; u32 d=0; while(n--) d|=*p++ ^ *q++; return !d;
}
static int valid(u32 a,u32 n) {
    return n && !(a&3u) && ((a>=0x80000000u && a<=0x81800000u-n) ||
        (a>=0x90000000u && a<=0x94000000u-n));
}
static void fault(u32 code) { if(!S.fault) S.fault=code; }
static volatile struct owner *owner(u32 game);
#ifdef CP3W_RECEIPT_DELIVERY
extern int delivery_in_progress(void);
u32 coupling_delivery_view(u32 game,u8 *out) {
    volatile struct owner *o=owner(game);
    if(S.magic!=0x43505231u || S.fault || !o) return 0;
    copy(out,o->current,CP3W_RECEIPT_SIZE); return o->generation;
}
#ifdef CP3W_MULTIWORLD
/* Only a validated disk read proves persistence here. A write submission or
   callback alone must not retire the host's retained delivery records. */
u32 coupling_saved_cursor(u32 game) {
    volatile struct owner *o=owner(game); const volatile u8 *p;
    if(S.fault || !o || o->slot>=3u || !S.disk[o->slot].valid) return 0;
    p=S.disk[o->slot].receipt+20;
    return ((u32)p[0]<<24)|((u32)p[1]<<16)|((u32)p[2]<<8)|p[3];
}
#endif
void coupling_delivery_fault(void) { fault(17); }
int coupling_delivery_commit(u32 game,u32 gen,const u8 *prior,const u8 *next) {
    /* Compare-and-replace the current owner's receipt while delivery is active.
       The generation prevents a reused game pointer from accepting an old
       request. Disk state remains separate until a validated container read. */
    volatile struct owner *o=owner(game);
    if(S.fault || !delivery_in_progress() || !o || o->generation!=gen || !equal(o->current,prior,CP3W_RECEIPT_SIZE)) return 0;
    copy(o->current,next,CP3W_RECEIPT_SIZE); return 1;
}
#define REJECT_DELIVERY() do { if(delivery_in_progress()) { fault(17); return; } } while(0)
#else
#define REJECT_DELIVERY() do {} while(0)
#endif
static int digest(u32 data,u32 n,u8 hash[32]) {
    if(n!=0x3c86u || !valid(data,n)) return 0;
    network_codec_sha256((const u8 *)data,n,hash); return 1;
}
static int vector_hash(u32 vector,u8 hash[32]) {
    return valid(vector,12) && digest(WORD(vector+8),WORD(vector),hash);
}
static volatile struct owner *owner(u32 game) {
    u32 i; if(!game) return 0;
    for(i=0;i<8;i++) if(S.owners[i].game==game) return &S.owners[i];
    return 0;
}
static void forget(u32 game) {
    volatile struct owner *o=owner(game); if(o) clear(o,sizeof(*o));
}
static volatile struct owner *create(u32 game,const volatile u8 *receipt) {
    u32 i; volatile struct owner *o;
    if(!valid(game,0x1a50u)) { fault(1); return 0; }
    forget(game);
    for(i=0;i<8;i++) if(!S.owners[i].game) {
        o=&S.owners[i]; clear(o,sizeof(*o));
        o->game=game; o->generation=++S.generation; o->slot=receipt[0];
        if(o->slot>=3u) { fault(2); clear(o,sizeof(*o)); return 0; }
        copy(o->current,receipt,CP3W_RECEIPT_SIZE); return o;
    }
    fault(3); return 0;
}
#ifdef CP3W_MULTIWORLD
static void bind_new_slot(u32 game) {
    /* Mii selection serializes the new slot before installing its playable
       game. Bind that native serialization to zero receipts only when the
       validated private container has no checkpoint for the exported slot. */
    if(game && !owner(game) && !S.fault && S.epoch && valid(game,0x1a50u) &&
       WORD(game+0x60u)==MW_SAVE_SLOT && !S.disk[MW_SAVE_SLOT].valid) {
        u8 receipt[CP3W_RECEIPT_SIZE]; clear(receipt,sizeof(receipt)); receipt[0]=MW_SAVE_SLOT;
        copy(receipt+4,network_save_profile+32+16u*MW_SAVE_SLOT,16); create(game,receipt);
    }
}
#endif
static int resolve_candidate(const volatile struct view *v,const u8 hash[32],
                             volatile struct view *out,u32 *found) {
    if(!v->valid || !equal(hash,v->hash,32)) return 1;
    if(*found && !equal(out->receipt,v->receipt,CP3W_RECEIPT_SIZE)) { fault(8); return 0; }
    copy(out,v,sizeof(*out)); *found=1; return 1;
}
static int resolve(u32 index,const u8 hash[32],volatile struct view *out) {
    u32 found=0;
    if(index>=4u) return 0;
    if(!resolve_candidate(&S.pending[index],hash,out,&found)) return 0;
    if(index<3u) {
        if(!resolve_candidate(&S.disk[index],hash,out,&found) ||
           !resolve_candidate(&S.stored[index],hash,out,&found)) return 0;
    }
    return found;
}

/* Called only after the enclosing container and bound profile validate. */
void coupling_loaded(const u8 *retail,const u8 *records) {
    u32 i,offset=19053u,epoch=S.epoch+1u;
    REJECT_DELIVERY();
    /* The native save manager rereads disk while a live game is still owned.
       Refresh its disk anchors without discarding the unsaved live view. */
    if(!owner(WORD(0x8067dc0cu))) {
        clear(&S,sizeof(S)); S.magic=0x43505231u; S.selected_slot=0xffffffffu;
    }
    S.epoch=epoch; clear(S.disk,sizeof(S.disk));
    for(i=0;i<3;i++) {
        if(retail[16+i]>1u) { fault(4); return; }
        if(!retail[16+i]) continue;
        if(offset>65536u-0x3c86u) { fault(4); return; }
        S.disk[i].valid=1;
        network_codec_sha256(retail+offset,0x3c86u,(u8 *)S.disk[i].hash);
        copy(S.disk[i].receipt,records+CP3W_RECEIPT_SIZE*i,CP3W_RECEIPT_SIZE);
        offset+=0x3c86u;
    }
}
void coupling_checkpoint(u32 game,u32 vector) {
    /* A death/checkpoint reload can restore older inventory. Keep its receipt
       with the native vector hash so replay resumes from that same point,
       rather than from the host's newest cursor. */
    volatile struct owner *o=owner(game); u32 i; u8 hash[32];
    REJECT_DELIVERY();
    if(!o) return; /* The retail blank/menu game has no loaded receipt view. */
    if(vector==game+0x1500u) i=3;
    else if(vector>=game+0x14dcu && vector<game+0x1500u && !((vector-game-0x14dcu)%12u))
        i=(vector-game-0x14dcu)/12u;
    else { fault(5); return; }
    if(i<3u && o->slot!=i) { fault(16); return; }
    clear(&o->vector[i],sizeof(struct view));
    if(vector_hash(vector,hash)) {
        o->vector[i].valid=1; copy(o->vector[i].hash,hash,32);
        copy(o->vector[i].receipt,o->current,CP3W_RECEIPT_SIZE);
    }
}
void coupling_before_install(u32 holder,u32 game) {
    volatile struct owner *o; u32 old,i; u8 hash[32];
    REJECT_DELIVERY();
#ifdef CP3W_MULTIWORLD
    /* A newly selected empty slot has no prior checkpoint receipt. Only the
       explicitly exported slot in an initialized, bound private container may
       acquire an initial zero view. Existing/loaded worlds must retain theirs. */
    bind_new_slot(game);
#endif
    if(game || !valid(holder,4)) return;
    old=WORD(holder); o=owner(old);
    clear(S.pending,sizeof(S.pending)); S.selected_valid=0; S.selected_slot=0xffffffffu;
    if(o) for(i=0;i<4;i++) {
        u32 vector=old+(i==3u ? 0x1500u : 0x14dcu+12u*i);
        if(o->vector[i].valid && vector_hash(vector,hash) && equal(hash,o->vector[i].hash,32))
            copy(&S.pending[i],&o->vector[i],sizeof(struct view));
    }
}
void coupling_selected_slot(u32 slot) { S.selected_slot=slot; }
void coupling_source(u32 vector) {
    struct view found; u8 hash[32]; u32 slot=S.selected_slot;
    S.selected_valid=0;
    if(!vector_hash(vector,hash) || !resolve(slot<3u ? slot : 3u,hash,&found)) { fault(6); return; }
    copy(S.selected,found.receipt,CP3W_RECEIPT_SIZE); S.selected_valid=1;
}
void coupling_begin_construct(u32 game) {
    REJECT_DELIVERY();
    if(!S.selected_valid) { fault(7); return; }
    create(game,S.selected); S.selected_valid=0;
}
void coupling_load_begin(u32 slot) { S.load_slot=slot; }
void coupling_load_end(void) { S.load_slot=0; }

EXPORTED u32 coupling_load_construct(u32 game,u32 stream,u32 flag) {
    u32 i,j,found=0,result; u8 hash[32],receipt[CP3W_RECEIPT_SIZE];
    if(valid(S.load_slot,0x3c90u) && digest(S.load_slot+4,WORD(S.load_slot),hash)) {
        for(i=0;i<3;i++) if(S.disk[i].valid && equal(hash,S.disk[i].hash,32)) {
            if(found && !equal(receipt,S.disk[i].receipt,CP3W_RECEIPT_SIZE)) { fault(8); found=0; break; }
            copy(receipt,S.disk[i].receipt,CP3W_RECEIPT_SIZE); found=1;
        }
        /* A stream constructor is also used to clone an in-memory checkpoint
           during save preparation, not only to deserialize bytes from disk. */
        for(i=0;i<8;i++) if(S.owners[i].game) for(j=0;j<4;j++) {
            const volatile struct view *v=&S.owners[i].vector[j];
            if(v->valid && equal(hash,v->hash,32)) {
                if(found && !equal(receipt,v->receipt,CP3W_RECEIPT_SIZE)) { fault(8); found=0; break; }
                copy(receipt,v->receipt,CP3W_RECEIPT_SIZE); found=1;
            }
        }
    }
    if(found && !S.fault) create(game,receipt); else fault(8);
    result=((u32 (*)(u32,u32,u32))0x800b76c4u)(game,stream,flag);
    if(result!=game) { forget(game); fault(9); }
    return result;
}
EXPORTED u32 coupling_clone_construct(u32 game,u32 stream,u32 flag) {
    volatile struct owner *o=owner(WORD(0x8067dc0cu)); u32 result;
    if(o) create(game,o->current);
#ifndef CP3W_MULTIWORLD
    else fault(10);
#endif
    result=((u32 (*)(u32,u32,u32))0x800b76c4u)(game,stream,flag);
    if(result!=game) { forget(game); fault(9); }
    return result;
}
EXPORTED u32 coupling_destroy(u32 game,u32 mode) {
    forget(game); return ((u32 (*)(u32,u32))0x800b87ccu)(game,mode);
}
EXPORTED u32 coupling_copy_vectors(u32 game,u32 vectors) {
    u32 i,result=((u32 (*)(u32,u32))0x800bac68u)(game,vectors);
    volatile struct owner *o=owner(game); u8 hash[32];
    if(!o) { fault(11); return result; }
    for(i=0;i<3;i++) {
        clear(&o->vector[i],sizeof(struct view));
        if(vector_hash(game+0x14dcu+12u*i,hash) && !resolve(i,hash,&o->vector[i])) fault(12);
    }
    return result;
}
EXPORTED u32 coupling_transfer(u32 game,u32 index,u32 data) {
    u32 result=((u32 (*)(u32,u32,u32))0x800baddcu)(game,index,data);
    volatile struct owner *o=owner(game),*source; u8 hash[32],source_hash[32];
    if(!o || index>=3u) return result;
    clear(&o->vector[index],sizeof(struct view));
    if(data<4u || !valid(data-4u,0x3c90u)) { fault(15); return result; }
    source=owner(WORD(data+0x3c88u));
    if(!source || source->slot!=index || !digest(data,WORD(data-4u),source_hash) ||
       !vector_hash(game+0x14dcu+12u*index,hash) || !equal(hash,source_hash,32)) { fault(15); return result; }
    o->vector[index].valid=1; copy(o->vector[index].hash,hash,32);
    copy(o->vector[index].receipt,source->current,CP3W_RECEIPT_SIZE);
    return result;
}
void coupling_stored(u32 slot) {
    volatile struct owner *o; u8 hash[32];
    REJECT_DELIVERY();
    if(!valid(slot,0x3c90u)) { fault(13); return; }
#ifdef CP3W_MULTIWORLD
    bind_new_slot(WORD(slot+0x3c8cu));
#endif
    o=owner(WORD(slot+0x3c8cu));
    if(!o) {
        /* Native save preparation serializes temporary blank slot objects.
           They do not acquire a receipt; require later known serializations
           for every present output slot before permitting any file write. */
        clear(S.stored,sizeof(S.stored)); return;
    }
    if(!digest(slot+4,WORD(slot),hash)) { fault(13); return; }
    S.stored[o->slot].valid=1; copy(S.stored[o->slot].hash,hash,32);
    copy(S.stored[o->slot].receipt,o->current,CP3W_RECEIPT_SIZE);
}

/* Require each serialized slot to match its exact stored receipt view. */
int coupling_prepare_save(const u8 *retail,u8 *records) {
    /* Do not attach the newest receipt to whichever bytes the save manager
       happens to serialize. Match every present slot to its stored hash first;
       otherwise saved inventory and receipt history could disagree on reload. */
    u32 i,offset=19053u; u8 hash[32]; const volatile struct view *v;
#ifdef CP3W_RECEIPT_DELIVERY
    if(delivery_in_progress()) { fault(17); return 0; }
#endif
    if(S.magic!=0x43505231u || S.fault) return 0;
    for(i=0;i<3;i++) {
        if(retail[16+i]>1u) return 0;
        if(!retail[16+i]) {
            copy(records+CP3W_RECEIPT_SIZE*i,S.disk[i].receipt,CP3W_RECEIPT_SIZE);
            /* Absent slots retain the bound identity but must have zero cursor/history. */
            records[CP3W_RECEIPT_SIZE*i]=(u8)i; records[CP3W_RECEIPT_SIZE*i+1]=records[CP3W_RECEIPT_SIZE*i+2]=records[CP3W_RECEIPT_SIZE*i+3]=0;
            copy(records+CP3W_RECEIPT_SIZE*i+4,network_save_profile+32+16*i,16);
            clear(records+CP3W_RECEIPT_SIZE*i+20,CP3W_RECEIPT_SIZE-20u); continue;
        }
        if(offset>65536u-0x3c86u) return 0;
        network_codec_sha256(retail+offset,0x3c86u,hash); offset+=0x3c86u;
        v=&S.stored[i];
        if(!v->valid || !equal(hash,v->hash,32)) { fault(14); return 0; }
        copy(records+CP3W_RECEIPT_SIZE*i,v->receipt,CP3W_RECEIPT_SIZE);
    }
    return 1;
}

/* Synthetic fixture only: 0x101 -> 0x202; after save, 0x202 -> 0x303.
   This is NOT a grant receipt API and never calls an inventory writer. */
#ifndef CP3W_RECEIPT_DELIVERY
EXPORTED void coupling_test_tick(void) {
    volatile struct owner *o=owner(WORD(0x8067dc0cu)); u32 cursor,i;
    if(!o || S.fault) return;
    cursor=((u32)o->current[20]<<24)|((u32)o->current[21]<<16)|((u32)o->current[22]<<8)|o->current[23];
    if(S.test_stage==0 && cursor==0x101u && ++S.ticks>=8u) {
        o->current[22]=2; o->current[23]=2;
        for(i=24;i<CP3W_RECEIPT_SIZE;i++) o->current[i]=0x22;
        S.test_stage=1; save_trace_record(33,o->game,0x202u,o->generation,o->slot);
    }
    if(S.test_stage==1 && S.stored[o->slot].valid && S.stored[o->slot].receipt[22]==2u &&
       S.stored[o->slot].receipt[23]==2u) {
        o->current[22]=3; o->current[23]=3;
        for(i=24;i<CP3W_RECEIPT_SIZE;i++) o->current[i]=0x33;
        S.test_stage=2; save_trace_record(33,o->game,0x303u,o->generation,o->slot);
    }
}
#endif
