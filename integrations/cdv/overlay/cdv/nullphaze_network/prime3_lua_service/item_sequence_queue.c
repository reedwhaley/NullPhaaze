/*
 * This queue admits the fixed sequence protocol and its declared payload. Queueing remains
 * separate from retail mutation and from durable checkpoint acknowledgement.
 */
#include "item_sequence_common.h"
extern u32 coupling_delivery_view(u32,u8 *);
extern int network_delivery_session_valid(u32);
extern volatile u32 receipt_delivery_state[16];
#define WORD(a) (*(volatile const u32 *)(a))
struct queue { u32 magic,pending,game,generation,session,received,queued,duplicates;
    u32 rejected,expired,last_result,last_request_id,last_cursor,last_generation,reserved[2]; };
__attribute__((section(".data.network_delivery")))
volatile struct queue network_delivery_state={.magic=0x4e444c31u};
#define Q network_delivery_state
void network_delivery_cancel(void) { if(Q.pending) Q.expired++; Q.pending=0; Q.reserved[0]=0; }
int network_delivery_allow(u32 game,u32 gen) {
    if(!Q.pending) return 0;
    if(Q.game!=game || Q.generation!=gen || !network_delivery_session_valid(Q.session)) {
        network_delivery_cancel(); return 0;
    }
    return 1;
}
u32 network_sequence_pending(void) { return Q.pending ? Q.reserved[0] : 0; }
u32 network_delivery_request(u32 command,u32 session,u32 id,const u8 *in,u32 n,u8 *out,u32 *size) {
    u8 current[56],second[56],expected[32]; u32 game,gen,cursor,result,i,sequence=0;
    *size=0; Q.received++; Q.last_request_id=id;
    if(Q.magic!=0x4e444c31u || (command!=7u && command!=8u)) return 4;
    if(n!=(command==7u ? 84u:140u)) return 5;
    if(seq_get(in)!=session || !network_delivery_session_valid(session) ||
       !seq_equal(in+4,network_save_profile,80)) return 10;
    if(command==8u) {
        sequence=seq_get(in+88);
        if(!sequence || sequence>CP3W_SEQUENCE_COUNT) return 10;
        for(i=0;i<6;i++) if(seq_get(in+84+4*i)!=sequence_steps[sequence-1][i]) return 10;
        seq_history(sequence,expected);
        if(!seq_equal(in+108,expected,32)) return 10;
    }
    if(receipt_delivery_state[0]!=0x52444731u || receipt_delivery_state[1]==4u) return 10;
    game=WORD(0x8067dc0cu); gen=coupling_delivery_view(game,current);
    if(gen && (WORD(0x8067dc0cu)!=game || coupling_delivery_view(game,second)!=gen ||
       !seq_equal(current,second,56) || current[0])) gen=0;
    cursor=gen ? seq_get(current+20):0xffffffffu;
    if(Q.pending && (!gen || Q.game!=game || Q.generation!=gen || Q.session!=session)) network_delivery_cancel();
    if(!gen) result=0;
    else {
        if(cursor>CP3W_SEQUENCE_COUNT) return 10;
        seq_history(cursor,expected);
        if(!seq_equal(current+24,expected,32)) return 10;
        if(Q.pending && cursor>=Q.reserved[0]) { Q.pending=0; Q.reserved[0]=0; }
        result=Q.pending ? 2u : (cursor ? 3u:1u);
        if(command==8u) {
            if(sequence<=cursor) { result=4; Q.duplicates++; }
            else if(sequence!=cursor+1u || (Q.pending && Q.reserved[0]!=sequence)) return 10;
            else {
                if(!Q.pending) { Q.queued++; Q.pending=1; Q.game=game; Q.generation=gen;
                    Q.session=session; Q.reserved[0]=sequence; }
                result=2;
            }
        }
    }
    out[0]=1; out[1]=result; out[2]=out[3]=0;
    seq_put(out+4,session); seq_put(out+8,gen); seq_put(out+12,cursor); seq_put(out+16,Q.pending);
    for(i=0;i<3;i++) seq_put(out+20+4*i,receipt_delivery_state[2+i]);
    for(i=0;i<32;i++) out[32+i]=gen ? current[24+i]:0;
    for(i=0;i<80;i++) out[64+i]=network_save_profile[i];
    Q.last_result=result; Q.last_cursor=cursor; Q.last_generation=gen; *size=144;
    return 0;
}
