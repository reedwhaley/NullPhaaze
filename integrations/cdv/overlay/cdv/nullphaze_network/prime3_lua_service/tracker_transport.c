/*
 * Both pages come from one frozen 150-word snapshot. Reusing the page-zero request retains
 * that token/sample instead of mixing inventory across a pickup or load.
 */
/* Included by network_transport.c. Two pages belong to one frozen snapshot. */
extern int bridge_tracker_snapshot(u32 *);
extern const u8 network_save_profile[80];
static u32 tracker_words[150], tracker_token, tracker_session, tracker_start_id;
static u32 tracker_request(u32 session,const u8 *in,u32 length,u8 *out,u32 *size) {
    /* Freeze all 150 words for page zero and reuse them for page one. Re-reading
       live inventory per page would combine states across a pickup or load.
       Retrying page zero with the same request ID retains that same snapshot. */
    u32 i,page,token,offset;
    *size=0;
    if(length!=92u) return 5;
    if(runtime_read_be32(in)!=session) return 10;
    for(i=0;i<80;i++) if(in[4+i]!=network_save_profile[i]) return 10;
    token=runtime_read_be32(in+84); page=runtime_read_be32(in+88);
    if(page>1u || (!token && page)) return 5;
    if(!page && !token) {
      if(tracker_session!=session || tracker_start_id!=runtime_transport_cp3w_last_request_id) {
        for(i=0;i<150;i++) tracker_words[i]=0;
        if(!bridge_tracker_snapshot(tracker_words)) {
            for(i=0;i<150;i++) tracker_words[i]=0;
            tracker_words[0]=0x54524b31u;
        }
        tracker_token++; if(!tracker_token) tracker_token++;
        tracker_session=session;
        tracker_start_id=runtime_transport_cp3w_last_request_id;
      }
    } else if(token!=tracker_token || session!=tracker_session) return 10;
    offset=page*300u;
    runtime_write_be32(out,1); runtime_write_be32(out+4,session);
    runtime_write_be32(out+8,tracker_token); runtime_write_be32(out+12,offset);
    runtime_write_be32(out+16,600); runtime_write_be32(out+20,300);
    for(i=0;i<80;i++) out[24+i]=network_save_profile[i];
    for(i=0;i<75;i++) runtime_write_be32(out+104+4*i,tracker_words[page*75+i]);
    *size=404; return 0;
}
