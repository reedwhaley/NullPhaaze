/*
 * Admission checks the exported identity, owner generation, next sequence, prior history
 * and recipe allowlist. Queue intent in the transport path; apply and verify retail
 * mutations on the game thread.
 */
/* SPDX-License-Identifier: GPL-3.0-or-later
 * Seed-bound semantic delivery. The generated table is the only recipe source.
 * Included by network_delivery.c only in CP3W_MULTIWORLD builds. */
#include "receipt_layout.h"
#include "multiworld_plan.c"
typedef unsigned int u32;
typedef unsigned char u8;
extern const u8 network_save_profile[80];
extern u32 coupling_delivery_view(u32,u8 *);
extern u32 coupling_saved_cursor(u32);
extern int coupling_delivery_commit(u32,u32,const u8 *,const u8 *);
extern void coupling_delivery_fault(void);
extern void network_codec_sha256(const u8 *,u32,u8 *);
extern int network_delivery_session_valid(u32);
extern int bridge_area_matches(u32,u32);
#ifdef MW_HOST_TEST
extern u32 mw_test_word(u32);
extern u32 mw_test_player(u32);
extern void mw_test_capacity(void *,u32,int);
extern void mw_test_amount(void *,u32,int);
#define WORD(a) mw_test_word(a)
#define ADD_CAPACITY mw_test_capacity
#define ADD_AMOUNT mw_test_amount
#else
#define WORD(a) (*(volatile u32 *)(a))
#define ADD_CAPACITY ((void (*)(void *,u32,int))0x8019111cu)
#define ADD_AMOUNT ((void (*)(void *,u32,int))0x801913a0u)
#endif
struct queue {
    u32 magic,pending,game,generation,session,received,queued,duplicates;
    u32 rejected,expired,last_result,last_request_id,last_cursor,last_generation,reserved[2];
};
__attribute__((section(".data.network_delivery")))
volatile struct queue network_delivery_state={.magic=0x4e444c31u};
__attribute__((section(".data.receipt_delivery")))
volatile u32 receipt_delivery_state[16]={0x52444731u};
#define Q network_delivery_state
#define D receipt_delivery_state
static u32 mw_presentation_sequence,mw_presentation_recipe,mw_presentation_serial;
static u32 mw_applied_stage,mw_presentation_game,mw_presentation_generation,mw_presentation_event,mw_presentation_claimed;
static int equal(const u8 *a,const u8 *b,u32 n) { u32 d=0; while(n--) d|=*a++ ^ *b++; return !d; }
static void copy(u8 *a,const u8 *b,u32 n) { while(n--) *a++=*b++; }
static u32 get32(const u8 *p) { return ((u32)p[0]<<24)|((u32)p[1]<<16)|((u32)p[2]<<8)|p[3]; }
static void put32(u8 *p,u32 n) { p[0]=n>>24; p[1]=n>>16; p[2]=n>>8; p[3]=n; }
#ifndef MW_HOST_TEST
static int valid(u32 a,u32 n) { return !(a&3u) &&
    ((a>=0x80000000u && a<=0x81800000u-n)||(a>=0x90000000u && a<=0x94000000u-n)); }
#endif
static void fault(void) { D[1]=4; coupling_delivery_fault(); }
int delivery_in_progress(void) { return D[1]==1u; }
void network_delivery_cancel(void) { if(Q.pending) Q.expired++; Q.pending=0; }
int network_delivery_allow(u32 game,u32 gen) {
    if(!Q.pending) return 0;
    if(Q.game!=game || Q.generation!=gen || !network_delivery_session_valid(Q.session)) {
        network_delivery_cancel(); return 0;
    }
    return 1;
}
static u32 view(u32 *game,u8 out[CP3W_RECEIPT_SIZE]) {
    /* Read the receipt twice around the active-game pointer. I need one stable
       owner/generation, not a cursor from the old game beside the new player.
       These address/layout guards belong to the supported executable build. */
    u8 second[CP3W_RECEIPT_SIZE]; u32 gen;
    *game=WORD(0x8067dc0cu); gen=coupling_delivery_view(*game,out);
    if(!gen || WORD(0x8067dc0cu)!=*game || coupling_delivery_view(*game,second)!=gen ||
       !equal(out,second,CP3W_RECEIPT_SIZE) || out[0]!=MW_SAVE_SLOT) return 0;
    return gen;
}
static u32 player_for(u32 game) {
#ifdef MW_HOST_TEST
    return mw_test_player(game);
#else
    u32 player;
    if(!valid(game,0x28u)) return 0;
    player=WORD(game+0x24u);
    if(!valid(player,0x998u) || !(*(volatile u8 *)player&0x80u) || !WORD(player+0xcu) ||
       WORD(player+0xcu)>=0x45000000u) return 0;
    return player;
#endif
}
static void history(const u8 *prior,u32 sequence,u32 recipe,u8 *out) {
    u8 data[68]; copy(data,prior,32); put32(data+32,sequence); copy(data+36,mw_recipe_keys[recipe],32);
    network_codec_sha256(data,68,out);
}
static int logical(u32 player,const u8 *receipt,u32 *out) {
    u32 i,id,amount,capacity,total=0;
    for(i=0;i<63u;i++) {
        out[i]=0;
        if(!permitted(i)) continue;
        id=mw_native_ids[i];
        if(id>=1000u) continue;
        amount=WORD(player+0x54u+12u*id); capacity=WORD(player+0x58u+12u*id);
        if(i==17u) { if(amount>6u) return 0; out[i]=amount>=5u; }
        else if(i>=23u && i<=31u) {
            u32 used=WORD(player+0x54u+12u*(53u+i-23u));
            if(amount>1u || used>1u) return 0;
            out[i]=(amount || used); total+=out[i];
        } else if(i!=22u) {
            if(amount>capacity || capacity>mw_limits[i]) return 0;
            out[i]=capacity;
        }
    }
    out[22]=total; out[59]=receipt[69]&1u; out[60]=(receipt[69]>>1)&1u;
    out[61]=((u32)receipt[72]<<8)|receipt[73]; out[62]=((u32)receipt[74]<<8)|receipt[75];
    return 1;
}
static int apply(u32 game,u32 gen,u32 recipe,u8 *prior,u8 *next) {
    /* Plan against the logical inventory first, then call the retail mutators
       on the game thread. Compare the observed result before publishing next.
       A fault after a mutator is terminal; this is not an inventory rollback. */
    u32 player=player_for(game),before[63],after[63],checked[63],i,id,amount,capacity,wanted,stage=0;
    if(!player || !logical(player,prior,before) || !mw_plan(&mw_recipes[recipe],before,mw_limits,after)) return 0;
    while(stage+1u<mw_recipes[recipe].stages && before[mw_recipes[recipe].progression[stage].resource]) stage++;
    D[1]=1; D[2]++;
    for(i=0;i<63u;i++) if(after[i]!=before[i] && i!=22u && i<59u) {
        id=mw_native_ids[i];
        if(id>=70u || after[i]<before[i]) { fault(); return 0; }
        if(i==17u) {
            amount=WORD(player+0x54u+12u*id); capacity=WORD(player+0x58u+12u*id);
            wanted=amount>=5u ? amount : 5u;
            if(capacity<wanted) ADD_CAPACITY((void *)player,id,(int)(wanted-capacity));
            if(amount<wanted) ADD_AMOUNT((void *)player,id,(int)(wanted-amount));
        } else {
            ADD_CAPACITY((void *)player,id,(int)(after[i]-before[i]));
            ADD_AMOUNT((void *)player,id,(int)(after[i]-before[i]));
        }
    }
    next[69]=(u8)(after[59]|(after[60]<<1));
    next[72]=(u8)(after[61]>>8); next[73]=(u8)after[61];
    next[74]=(u8)(after[62]>>8); next[75]=(u8)after[62];
    if(WORD(0x8067dc0cu)!=game || WORD(game+0x24u)!=player || !logical(player,next,checked)) { fault(); return 0; }
    for(i=0;i<63u;i++) {
        /* Energy Tank's native helper also changes Energy automatically. */
        if(i==18u && after[20]!=before[20]) continue;
        if(after[i]!=checked[i]) { fault(); return 0; }
    }
    if(!coupling_delivery_commit(game,gen,prior,next)) { fault(); return 0; }
    /* This commits the live owner's receipt, not a durable-save ACK. Saving
       must later pair this receipt with the exact serialized inventory. */
    mw_applied_stage=stage; D[3]++; D[1]=2; return 1;
}
void receipt_delivery_tick(void *state) {
    /* UDP only queues intent. The owning Lua callback performs the grant here,
       after checking that the queued session and checkpoint owner still match. */
    u8 prior[CP3W_RECEIPT_SIZE],next[CP3W_RECEIPT_SIZE]; u32 game,gen,sequence,recipe;
    (void)state;
    if(D[1]==4u || delivery_in_progress()) return;
    gen=view(&game,prior);
    if(!gen || !network_delivery_allow(game,gen) || !player_for(game)) return;
    /* Keep one committed notice until its owning current-area bank claims it.
       A new checkpoint owner discards unsaved presentation, never inventory. */
    if(mw_presentation_serial && !mw_presentation_claimed &&
       mw_presentation_game==game && mw_presentation_generation==gen) return;
    sequence=Q.reserved[0]; recipe=Q.reserved[1];
    if(sequence!=get32(prior+20)+1u || recipe>=MW_RECIPE_COUNT) { fault(); return; }
    copy(next,prior,CP3W_RECEIPT_SIZE); put32(next+20,sequence); history(prior+24,sequence,recipe,next+24);
    if(apply(game,gen,recipe,prior,next)) {
        Q.pending=0;
        /* A legitimate redelivery after checkpoint rollback may have a lower
           sequence than a prior, unsaved session. Duplicates never reach apply. */
        mw_presentation_sequence=sequence; mw_presentation_recipe=recipe; mw_presentation_serial++;
        mw_presentation_game=game; mw_presentation_generation=gen;
        mw_presentation_event=recipe*4u+mw_applied_stage; mw_presentation_claimed=0;
    }
}
int mw_collect_location(u32 index) {
    /* Local and foreign pickups share the collected bit. The generated table
       uses ffffffff for a foreign recipient, so that path records the check
       without granting the displayed foreign item to this Corruption player. */
    u8 prior[CP3W_RECEIPT_SIZE],next[CP3W_RECEIPT_SIZE]; u32 game,gen,recipe;
    if(index>=100u || D[1]==4u || delivery_in_progress()) return 0;
    if(!bridge_area_matches(mw_locations[index][1],mw_locations[index][2])) return 0;
    gen=view(&game,prior); if(!gen || !player_for(game)) return 0;
    if(prior[56+index/8u]&(1u<<(index%8u))) return 1;
    copy(next,prior,CP3W_RECEIPT_SIZE); next[56+index/8u]|=(u8)(1u<<(index%8u));
    recipe=mw_locations[index][0];
    if(recipe!=0xffffffffu) return apply(game,gen,recipe,prior,next);
    D[1]=1;
    if(!coupling_delivery_commit(game,gen,prior,next)) { fault(); return 0; }
    D[1]=2; return 1;
}
/* A read-only Lua presentation poll. Retrying a receipt never advances it. */
u32 mw_presentation(u32 *recipe) { *recipe=mw_presentation_recipe; return mw_presentation_serial; }
u32 mw_claim_presentation(u32 bank) {
    u8 receipt[CP3W_RECEIPT_SIZE]; u32 game,gen;
    if(!mw_presentation_serial || mw_presentation_claimed || bank>=64u ||
       mw_presentation_event/16u!=bank) return 0xffffffffu;
    gen=view(&game,receipt);
    if(!gen || game!=mw_presentation_game || gen!=mw_presentation_generation) return 0xffffffffu;
    mw_presentation_claimed=1; return mw_presentation_event;
}
static u32 status(u8 *out,u32 *size) {
    /* Report both cursors. The live cursor may lead disk until a verified read
       refreshes the saved anchor; a normal UDP response must not collapse them. */
    u8 receipt[CP3W_RECEIPT_SIZE]; u32 game,gen,i,cursor=0,saved=0;
    for(i=0;i<126u;i++) out[i]=0;
    copy(out,(const u8 *)"MW01",4); copy(out+4,mw_world,16); copy(out+20,mw_seed,32);
    put32(out+52,MW_SAVE_SLOT);
    gen=view(&game,receipt); put32(out+56,gen);
    if(gen) {
        cursor=get32(receipt+20); saved=coupling_saved_cursor(game);
        if(saved>cursor) saved=cursor;
        put32(out+60,cursor); put32(out+64,saved);
        put32(out+68,player_for(game)!=0 && D[1]!=4u);
        put32(out+72,Q.pending && Q.game==game && Q.generation==gen);
        copy(out+76,receipt+24,32); copy(out+108,receipt+56,13);
        out[121]=receipt[69]; copy(out+122,receipt+72,4);
    }
    *size=126u; return D[1]==4u ? 10u : 0u;
}
u32 network_delivery_request(u32 command,u32 session,u32 id,const u8 *in,u32 n,u8 *out,u32 *size) {
    u8 prior[CP3W_RECEIPT_SIZE],expected[32]; u32 game,gen,sequence,recipe;
    *size=0; Q.received++; Q.last_request_id=id;
    if(command!=10u && command!=11u) return 4;
    if(n!=(command==10u ? 84u : 212u)) return 5;
    if(get32(in)!=session || !network_delivery_session_valid(session) || !equal(in+4,network_save_profile,80)) return 10;
    if(command==10u) return status(out,size);
    in+=84;
    if(!equal(in,mw_world,16) || !equal(in+16,mw_seed,32) || get32(in+48)!=MW_SAVE_SLOT || get32(in+60)) return 10;
    gen=view(&game,prior);
    if(!gen || get32(in+52)!=gen || !player_for(game) || D[1]==4u) return 10;
    sequence=get32(in+56);
    if(!sequence || sequence>256u) return 10;
    for(recipe=0;recipe<MW_RECIPE_COUNT;recipe++) if(mw_incoming_allowed[recipe] && equal(in+96,mw_recipe_keys[recipe],32)) break;
    if(recipe==MW_RECIPE_COUNT) return 10;
    if(sequence==get32(prior+20)) {
        /* A retry of the last applied item must reproduce its history hash.
           Equal sequence alone is insufficient: reject a different recipe or
           prior history instead of acknowledging it as the same delivery. */
        history(in+64,sequence,recipe,expected);
        if(!equal(expected,prior+24,32)) return 10;
        Q.duplicates++; return status(out,size);
    }
    if(sequence!=get32(prior+20)+1u || !equal(in+64,prior+24,32)) return 10;
    if(Q.pending && (Q.game!=game || Q.generation!=gen)) network_delivery_cancel();
    if(Q.pending) {
        if(Q.reserved[0]!=sequence || Q.reserved[1]!=recipe) return 10;
        Q.duplicates++;
    } else {
        /* Admission is bounded by profile, owner generation, next sequence,
           prior history and the exported incoming allowlist above. Queue one
           recipe; never call retail inventory functions from this handler. */
        Q.game=game; Q.generation=gen; Q.session=session; Q.reserved[0]=sequence; Q.reserved[1]=recipe;
        Q.pending=1; Q.queued++;
    }
    return status(out,size);
}
