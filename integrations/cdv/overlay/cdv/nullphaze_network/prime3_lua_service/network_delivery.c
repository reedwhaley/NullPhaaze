/*
 * The compile-time branch selects the current seed-authorized service or the fixed
 * diagnostic queue. A queued capsule response is volatile state, not a durable-save
 * acknowledgement.
 */
#ifdef CP3W_MULTIWORLD
#include "multiworld_service.c"
#elif defined(CP3W_ITEM_SEQUENCE_TEST)
#include "item_sequence_queue.c"
#else
/* Fixed capsule queue. Only receipt_delivery_tick may call retail mutators. */
typedef unsigned int u32;
typedef unsigned char u8;
extern const u8 network_save_profile[80];
extern u32 coupling_delivery_view(u32,u8 *);
extern void network_codec_sha256(const u8 *,u32,u8 *);
extern int network_delivery_session_valid(u32);
extern volatile u32 receipt_delivery_state[16];
#define WORD(a) (*(volatile const u32 *)(a))
struct queue {
    u32 magic,pending,game,generation,session,received,queued,duplicates;
    u32 rejected,expired,last_result,last_request_id,last_cursor,last_generation,reserved[2];
};
__attribute__((section(".data.network_delivery")))
volatile struct queue network_delivery_state={.magic=0x4e444c31u};
#define Q network_delivery_state
static int equal(const u8 *a,const u8 *b,u32 n) { u32 d=0; while(n--) d|=*a++ ^ *b++; return !d; }
static u32 get32(const u8 *p) { return ((u32)p[0]<<24)|((u32)p[1]<<16)|((u32)p[2]<<8)|p[3]; }
static void put32(u8 *p,u32 n) { p[0]=n>>24; p[1]=n>>16; p[2]=n>>8; p[3]=n; }
void network_delivery_cancel(void) { if(Q.pending) Q.expired++; Q.pending=0; }
int network_delivery_allow(u32 game,u32 gen) {
    if(!Q.pending) return 0;
    if(Q.game!=game || Q.generation!=gen || !network_delivery_session_valid(Q.session)) {
        network_delivery_cancel(); return 0;
    }
    return 1;
}
static u32 view(u32 *game,u8 out[56]) {
    u8 second[56]; u32 gen;
    *game=WORD(0x8067dc0cu); gen=coupling_delivery_view(*game,out);
    if(!gen || WORD(0x8067dc0cu)!=*game || coupling_delivery_view(*game,second)!=gen ||
       !equal(out,second,56) || out[0]!=0u) return 0;
    return gen;
}
static void history(u8 out[32]) {
    u8 data[136]; u32 i;
    for(i=0;i<136;i++) data[i]=0;
    for(i=0;i<80;i++) data[32+i]=network_save_profile[i];
    data[119]=1; data[123]=4; data[127]=5; data[131]=5; data[135]=1;
    network_codec_sha256(data,136,out);
}
/* Returns a CP3W error code, or a144-byte volatile-state response. */
u32 network_delivery_request(u32 command,u32 session,u32 id,const u8 *in,u32 n,u8 *out,u32 *size) {
    u8 current[56],expected[32],zero[32]; u32 game,gen,cursor,result,i;
    static const u32 capsule[6]={0,1,4,5,5,1};
    *size=0;
    if(Q.magic!=0x4e444c31u) return 10;
    Q.received++; Q.last_request_id=id;
    if(command!=7u && command!=8u) { Q.rejected++; return 4; }
    if(n!=(command==7u ? 84u:140u)) { Q.rejected++; return 5; }
    if(get32(in)!=session || !network_delivery_session_valid(session) ||
       !equal(in+4,network_save_profile,80)) { Q.rejected++; return 10; }
    history(expected); for(i=0;i<32;i++) zero[i]=0;
    if(command==8u) {
        for(i=0;i<6;i++) if(get32(in+84+4*i)!=capsule[i]) { Q.rejected++; return 10; }
        if(!equal(in+108,expected,32)) { Q.rejected++; return 10; }
    }
    if(receipt_delivery_state[0]!=0x52444731u || receipt_delivery_state[1]==4u) return 10;
    gen=view(&game,current); cursor=gen ? get32(current+20):0xffffffffu;
    if(Q.pending && (!gen || Q.game!=game || Q.generation!=gen || Q.session!=session)) network_delivery_cancel();
    if(!gen) result=0;
    else if(cursor==1u && equal(current+24,expected,32)) {
        Q.pending=0;
        if(receipt_delivery_state[5]!=game || receipt_delivery_state[6]!=gen ||
           (receipt_delivery_state[1]!=2u && receipt_delivery_state[1]!=3u)) {
            gen=0; cursor=0xffffffffu; result=0;
        } else {
            result=command==8u ? 4u:3u;
            if(command==8u) Q.duplicates++;
        }
    } else if(cursor==0u && equal(current+24,zero,32)) {
        if(command==8u && !Q.pending) {
            Q.game=game; Q.generation=gen; Q.session=session; Q.queued++; Q.pending=1;
        }
        result=Q.pending ? 2u:1u;
    } else { Q.rejected++; return 10; }
    out[0]=1; out[1]=result; out[2]=0; out[3]=0; /* No durable-ack flag. */
    put32(out+4,session); put32(out+8,gen); put32(out+12,cursor); put32(out+16,Q.pending);
    for(i=0;i<3;i++) put32(out+20+4*i,receipt_delivery_state[2+i]);
    for(i=0;i<32;i++) out[32+i]=gen ? current[24+i]:0;
    for(i=0;i<80;i++) out[64+i]=network_save_profile[i];
    Q.last_result=result; Q.last_cursor=cursor; Q.last_generation=gen; *size=144;
    return 0;
}
#endif
