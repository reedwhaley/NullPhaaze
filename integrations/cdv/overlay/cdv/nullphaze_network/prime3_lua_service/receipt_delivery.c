/*
 * Compile-time selection separates current multiworld delivery, the item-sequence
 * experiment and the fixed missile probe. Keep the disposable probe's narrow preconditions
 * outside general delivery.
 */
#ifdef CP3W_MULTIWORLD
/* General seed-authorized delivery is linked from multiworld_service.c. */
#elif defined(CP3W_ITEM_SEQUENCE_TEST)
#include "item_sequence_delivery.c"
#else
/* Fixed local delivery experiment. No network input or general grant API. */
typedef unsigned int u32;
typedef unsigned char u8;
extern const u8 network_save_profile[80];
extern void network_codec_sha256(const u8 *,u32,u8 *);
extern u32 coupling_delivery_view(u32,u8 *);
extern int coupling_delivery_commit(u32,u32,const u8 *,const u8 *);
extern void coupling_delivery_fault(void);
extern void save_trace_record(u32,u32,u32,u32,u32);
extern int bridge_read_location(void *);
#ifdef CP3W_NETWORK_DELIVERY
extern int network_delivery_allow(u32,u32);
#endif
#define WORD(a) (*(volatile u32 *)(a))
#define ADD_CAPACITY ((void (*)(void *,u32,int))0x8019111cu)
#define ADD_AMOUNT ((void (*)(void *,u32,int))0x801913a0u)
struct delivery {
    u32 magic,stage,attempts,applied,duplicates,game,generation,ticks;
    u32 before_amount,before_capacity,before_percent,before_percent_capacity;
    u32 after_amount,after_capacity,after_percent,after_percent_capacity;
};
__attribute__((section(".data.receipt_delivery")))
volatile struct delivery receipt_delivery_state={.magic=0x52444731u};
#define D receipt_delivery_state
int delivery_in_progress(void) { return D.stage==1u; }
static int valid(u32 a,u32 n) {
    return !(a&3u) && ((a>=0x80000000u && a<=0x81800000u-n) ||
        (a>=0x90000000u && a<=0x94000000u-n));
}
static int equal(const u8 *a,const u8 *b,u32 n) {
    u32 d=0; while(n--) d|=*a++ ^ *b++; return !d;
}
static void fail(void) {
    D.stage=4; coupling_delivery_fault();
    save_trace_record(34,D.game,4,D.attempts,D.applied);
}

/* Runs synchronously inside the existing Lua game-thread callback. */
__attribute__((section(".text.receipt_delivery")))
void receipt_delivery_tick(void *state) {
#ifdef CP3W_TRACKER_READ_ONLY
    (void)state;
    return;
#endif
    u8 prior[56],next[56],message[136],history[32];
    u32 game,player,gen,i,cursor;
    if(D.magic!=0x52444731u || D.stage==4u || D.stage==1u) return;
    game=WORD(0x8067dc0cu); gen=coupling_delivery_view(game,prior);
    if(!gen || prior[0]!=0u) return;
    if(D.game!=game || D.generation!=gen) {
        D.game=game; D.generation=gen; D.ticks=0; D.stage=0;
    }
    if(!valid(game,0x28u)) return;
    player=WORD(game+0x24u);
    if(!valid(player,0x998u) || !(*(volatile u8 *)player & 0x80u) ||
       !WORD(player+0xcu) || WORD(player+0xcu)>=0x45000000u || WORD(player+0x144u)>14u) return;
    if(!bridge_read_location(state)) return;
    if(WORD(0x8067dc0cu)!=game || WORD(game+0x24u)!=player) return;
    /* Same verified world/area and eligibility as the accepted fixed probe. */
    {
        u32 context=WORD(0x805c4f98u),world;
        if(!valid(context,0x2188u)) return;
        world=WORD(context+0x2134u);
        if(!valid(world,0x80u) || WORD(world+0x18u)!=0xc133f919u ||
           WORD(world+0x1cu)!=0xc108bdf9u || WORD(world+0x7cu)!=2u) return;
    }
    /* H(zero previous history || bound profile || slot,seq,item,amount,cap,percent).
       The fixed sequence is 1. A different payload/history is a hard fault. */
    for(i=0;i<136;i++) message[i]=0;
    for(i=0;i<80;i++) message[32+i]=network_save_profile[i];
    message[119]=1; message[123]=4; message[127]=5;
    message[131]=5; message[135]=1;
    network_codec_sha256(message,136,history);
    cursor=((u32)prior[20]<<24)|((u32)prior[21]<<16)|((u32)prior[22]<<8)|prior[23];
    if(cursor==1u) {
        if(!equal(prior+24,history,32) || WORD(player+0x88u)!=25u) { fail(); return; }
        if(D.stage!=3u) { D.duplicates++; D.stage=3; save_trace_record(34,game,3,gen,D.duplicates); }
        return;
    }
    if(cursor || !equal(prior+24,message,32)) { fail(); return; }
#ifdef CP3W_NETWORK_DELIVERY
    if(!network_delivery_allow(game,gen)) { D.ticks=0; return; }
#endif
    if(++D.ticks<8u) return;
    D.before_amount=WORD(player+0x84u); D.before_capacity=WORD(player+0x88u);
    D.before_percent=WORD(player+0x150u); D.before_percent_capacity=WORD(player+0x154u);
    if(D.before_capacity!=20u || D.before_amount>20u ||
       D.before_percent>D.before_percent_capacity || D.before_percent_capacity>=255u) { fail(); return; }
    for(i=0;i<56;i++) next[i]=prior[i];
    next[23]=1; for(i=0;i<32;i++) next[24+i]=history[i];
    D.stage=1; D.attempts++;
    ADD_CAPACITY((void *)player,21u,1); ADD_AMOUNT((void *)player,21u,1);
    ADD_CAPACITY((void *)player,4u,5); ADD_AMOUNT((void *)player,4u,5);
    D.after_amount=WORD(player+0x84u); D.after_capacity=WORD(player+0x88u);
    D.after_percent=WORD(player+0x150u); D.after_percent_capacity=WORD(player+0x154u);
    if(D.after_amount!=D.before_amount+5u || D.after_capacity!=25u ||
       D.after_percent!=D.before_percent+1u || D.after_percent_capacity!=D.before_percent_capacity+1u ||
       WORD(0x8067dc0cu)!=game || WORD(game+0x24u)!=player ||
       !coupling_delivery_commit(game,gen,prior,next)) { fail(); return; }
    D.applied++; D.stage=2; save_trace_record(34,game,2,gen,D.applied);
}
#endif
