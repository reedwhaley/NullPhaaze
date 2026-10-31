/*
 * The sequence descriptors are a compile-time ABI shared by queue and delivery. Their
 * resource IDs and counts are not an arbitrary network mutation interface.
 */
/* Compiled sequence descriptors, not arbitrary network mutation arguments. */
typedef unsigned int u32;
typedef unsigned char u8;
extern const u8 network_save_profile[80];
extern void network_codec_sha256(const u8 *,u32,u8 *);
static u32 seq_get(const u8 *p) { return ((u32)p[0]<<24)|((u32)p[1]<<16)|((u32)p[2]<<8)|p[3]; }
static void seq_put(u8 *p,u32 n) { p[0]=n>>24; p[1]=n>>16; p[2]=n>>8; p[3]=n; }
static int seq_equal(const u8 *a,const u8 *b,u32 n) { u32 d=0; while(n--) d|=*a++ ^ *b++; return !d; }
static void seq_history(u32 cursor,u8 out[32]) {
    u8 data[136]; u32 i,j;
    for(i=0;i<32;i++) out[i]=0;
    for(i=0;i<80;i++) data[32+i]=network_save_profile[i];
    for(j=0;j<cursor;j++) {
        for(i=0;i<32;i++) data[i]=out[i];
        for(i=0;i<6;i++) seq_put(data+112+4*i,sequence_steps[j][i]);
        network_codec_sha256(data,136,out);
    }
}
