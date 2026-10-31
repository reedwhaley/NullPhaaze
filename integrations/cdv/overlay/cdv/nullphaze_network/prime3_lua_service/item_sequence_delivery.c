/*
 * Apply only the compiled private item sequence after its receipt/owner gates. Inventory
 * changes and committed history must move together; the host cannot supply new sequence
 * operations.
 */
#include "item_sequence_common.h"
extern u32 coupling_delivery_view(u32,u8 *);
extern int coupling_delivery_commit(u32,u32,const u8 *,const u8 *);
extern void coupling_delivery_fault(void);
extern void save_trace_record(u32,u32,u32,u32,u32);
extern int bridge_read_location(void *);
extern int network_delivery_allow(u32,u32);
extern u32 network_sequence_pending(void);
#define WORD(a) (*(volatile u32 *)(a))
#define ADD_CAPACITY ((void (*)(void *,u32,int))0x8019111cu)
#define ADD_AMOUNT ((void (*)(void *,u32,int))0x801913a0u)
struct delivery { u32 magic,stage,attempts,applied,duplicates,game,generation,ticks;
    u32 before_amount,before_capacity,before_percent,before_percent_capacity;
    u32 after_amount,after_capacity,after_percent,after_percent_capacity; };
__attribute__((section(".data.receipt_delivery")))
volatile struct delivery receipt_delivery_state={.magic=0x52444731u};
#define D receipt_delivery_state
int delivery_in_progress(void) { return D.stage==1u; }
static int valid(u32 a,u32 n) { return !(a&3u) &&
    ((a>=0x80000000u && a<=0x81800000u-n)||(a>=0x90000000u && a<=0x94000000u-n)); }
static void fail(void) { D.stage=4; coupling_delivery_fault(); save_trace_record(34,D.game,4,D.attempts,D.applied); }
__attribute__((section(".text.receipt_delivery")))
void receipt_delivery_tick(void *state) {
    u8 prior[56],next[56],expected[32]; u32 game,player,gen,cursor,sequence,item,cap,amount,limit,i;
    if(D.magic!=0x52444731u || D.stage==4u || D.stage==1u) return;
    game=WORD(0x8067dc0cu); gen=coupling_delivery_view(game,prior);
    if(!gen || prior[0]) return;
    if(!valid(game,0x28u)) return;
    player=WORD(game+0x24u);
    if(!valid(player,0x998u) || !(*(volatile u8 *)player&0x80u) ||
       !WORD(player+0xcu) || WORD(player+0xcu)>=0x45000000u) return;
    if(!bridge_read_location(state) || WORD(0x8067dc0cu)!=game || WORD(game+0x24u)!=player) return;
    if(!network_delivery_allow(game,gen)) { D.ticks=0; return; }
    sequence=network_sequence_pending(); cursor=seq_get(prior+20);
    if(!sequence || sequence>CP3W_SEQUENCE_COUNT || cursor>=CP3W_SEQUENCE_COUNT) return;
    if(sequence!=cursor+1u) return;
    seq_history(cursor,expected);
    if(!seq_equal(prior+24,expected,32)) { fail(); return; }
    if(D.game!=game || D.generation!=gen) { D.game=game; D.generation=gen; D.ticks=0; }
    if(++D.ticks<2u) return;
    item=sequence_steps[cursor][6]; cap=sequence_steps[cursor][7]; amount=sequence_steps[cursor][8];
    limit=WORD(0x8057b568u+12u*item+4u);
    D.before_amount=WORD(player+0x54u+12u*item); D.before_capacity=WORD(player+0x58u+12u*item);
    D.before_percent=WORD(player+0x150u); D.before_percent_capacity=WORD(player+0x154u);
    if(D.before_amount>D.before_capacity || D.before_capacity>limit || D.before_percent_capacity>=255u) {
        fail(); return;
    }
    for(i=0;i<56;i++) next[i]=prior[i];
    seq_put(next+20,sequence); seq_history(sequence,next+24);
    D.stage=1; D.attempts++;
    ADD_CAPACITY((void *)player,21u,1); ADD_AMOUNT((void *)player,21u,1);
    ADD_CAPACITY((void *)player,item,cap); ADD_AMOUNT((void *)player,item,amount);
    D.after_amount=WORD(player+0x54u+12u*item); D.after_capacity=WORD(player+0x58u+12u*item);
    D.after_percent=WORD(player+0x150u); D.after_percent_capacity=WORD(player+0x154u);
    cap=D.before_capacity+cap; if(cap>limit) cap=limit;
    amount=D.before_amount+amount; if(amount>cap) amount=cap;
    if(D.after_amount!=amount || D.after_capacity!=cap || D.after_percent!=D.before_percent+1u ||
       D.after_percent_capacity!=D.before_percent_capacity+1u || WORD(0x8067dc0cu)!=game ||
       WORD(game+0x24u)!=player || !coupling_delivery_commit(game,gen,prior,next)) { fail(); return; }
    D.applied++; D.stage=2; D.ticks=0; save_trace_record(34,game,sequence,gen,item);
}
