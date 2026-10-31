/*
 * Encode and validate the private checkpoint container and bound profile with explicit
 * sizes/checksums. The codec does not itself apply a grant or prove disk IO completed.
 */
#include "receipt_layout.h"
/* Experimental offline/native codec component. No filesystem or grant calls. */
typedef unsigned int u32;
typedef unsigned char u8;

#define RETAIL_SIZE 65536u
#define TOTAL_SIZE CP3W_WIRE_SIZE
#define HEADER_SIZE 88u
#define RECORD_SIZE CP3W_RECEIPT_SIZE

static const u32 round_constants[64] = {
    0x428a2f98u,0x71374491u,0xb5c0fbcfu,0xe9b5dba5u,0x3956c25bu,0x59f111f1u,0x923f82a4u,0xab1c5ed5u,
    0xd807aa98u,0x12835b01u,0x243185beu,0x550c7dc3u,0x72be5d74u,0x80deb1feu,0x9bdc06a7u,0xc19bf174u,
    0xe49b69c1u,0xefbe4786u,0x0fc19dc6u,0x240ca1ccu,0x2de92c6fu,0x4a7484aau,0x5cb0a9dcu,0x76f988dau,
    0x983e5152u,0xa831c66du,0xb00327c8u,0xbf597fc7u,0xc6e00bf3u,0xd5a79147u,0x06ca6351u,0x14292967u,
    0x27b70a85u,0x2e1b2138u,0x4d2c6dfcu,0x53380d13u,0x650a7354u,0x766a0abbu,0x81c2c92eu,0x92722c85u,
    0xa2bfe8a1u,0xa81a664bu,0xc24b8b70u,0xc76c51a3u,0xd192e819u,0xd6990624u,0xf40e3585u,0x106aa070u,
    0x19a4c116u,0x1e376c08u,0x2748774cu,0x34b0bcb5u,0x391c0cb3u,0x4ed8aa4au,0x5b9cca4fu,0x682e6ff3u,
    0x748f82eeu,0x78a5636fu,0x84c87814u,0x8cc70208u,0x90befffau,0xa4506cebu,0xbef9a3f7u,0xc67178f2u
};

static u32 get32(const u8 *p) {
    return ((u32)p[0] << 24) | ((u32)p[1] << 16) | ((u32)p[2] << 8) | p[3];
}
static void put32(u8 *p, u32 value) {
    p[0] = value >> 24; p[1] = value >> 16; p[2] = value >> 8; p[3] = value;
}
static int equal(const u8 *a, const u8 *b, u32 size) {
    u32 different = 0;
    while (size--) different |= *a++ ^ *b++;
    return different == 0;
}
static int nonzero(const u8 *p, u32 size) {
    u32 value = 0;
    while (size--) value |= *p++;
    return value != 0;
}
static u32 rotate(u32 value, u32 shift) {
    return (value >> shift) | (value << (32u - shift));
}

void network_codec_sha256(const u8 *data, u32 size, u8 *output) {
    u32 state[8] = {0x6a09e667u,0xbb67ae85u,0x3c6ef372u,0xa54ff53au,
                    0x510e527fu,0x9b05688cu,0x1f83d9abu,0x5be0cd19u};
    u32 words[64], offset, index, total = (size + 9u + 63u) & ~63u;
    for (offset = 0; offset < total; offset += 64u) {
        u32 a,b,c,d,e,f,g,h;
        for (index = 0; index < 16u; ++index) {
            u32 value = 0, byte;
            for (byte = 0; byte < 4u; ++byte) {
                u32 position = offset + 4u * index + byte;
                u32 octet = position < size ? data[position] : position == size ? 0x80u : 0;
                if (position >= total - 4u) octet = (size * 8u) >> (8u * (total - position - 1u));
                value = (value << 8) | (octet & 255u);
            }
            words[index] = value;
        }
        for (index = 16; index < 64u; ++index) {
            u32 x = words[index-15], y = words[index-2];
            words[index] = words[index-16] + (rotate(x,7)^rotate(x,18)^(x>>3)) + words[index-7]
                + (rotate(y,17)^rotate(y,19)^(y>>10));
        }
        a=state[0]; b=state[1]; c=state[2]; d=state[3]; e=state[4]; f=state[5]; g=state[6]; h=state[7];
        for (index = 0; index < 64u; ++index) {
            u32 first = h + (rotate(e,6)^rotate(e,11)^rotate(e,25)) + ((e&f)^((~e)&g))
                + round_constants[index] + words[index];
            u32 second = (rotate(a,2)^rotate(a,13)^rotate(a,22)) + ((a&b)^(a&c)^(b&c));
            h=g; g=f; f=e; e=d+first; d=c; c=b; b=a; a=first+second;
        }
        state[0]+=a; state[1]+=b; state[2]+=c; state[3]+=d;
        state[4]+=e; state[5]+=f; state[6]+=g; state[7]+=h;
    }
    for (index=0; index<8u; ++index) put32(output + 4u*index, state[index]);
}

static u32 crc32(const u8 *data, u32 size) {
#ifdef CP3W_CODEC_HOST_TEST
    u32 crc=0xffffffffu,i,j;
    for(i=0;i<size;i++) {
        crc^=data[i];
        for(j=0;j<8u;j++) crc=(crc>>1)^((0u-(crc&1u))&0xedb88320u);
    }
    return crc^0xffffffffu;
#else
    /* Original verified retail CRC returns the unfinalized value. */
    return ((u32 (*)(const u8 *, u32, u32))0x80344f24u)(data, size, 0xffffffffu) ^ 0xffffffffu;
#endif
}

static int retail_valid(const u8 *retail) {
    u32 index;
    if ((get32(retail) ^ 0xffffffffu) != crc32(retail+4, RETAIL_SIZE-4)) return 0;
    if (get32(retail+12) > 2u || !equal(retail+19, (const u8 *)"SAVHSYST", 8)) return 0;
    for (index=0; index<3u; ++index) if (retail[16+index] > 1u) return 0;
    return 1;
}

/* Profile: campaign UUID, lineage UUID, then the three derived slot UUIDs. */
#if defined(_WIN32) && defined(CP3W_CODEC_HOST_TEST)
__declspec(dllexport)
#endif
int network_codec_validate(const u8 *wire, u32 size, const u8 *profile) {
    u8 hash[32];
    u32 index;
    const u8 *retail = wire + HEADER_SIZE;
    if (size != TOTAL_SIZE) return 0;
    if (!equal(wire, (const u8 *)CP3W_SAVE_MAGIC, 8) || get32(wire+8) != CP3W_SAVE_VERSION
        || get32(wire+12) != TOTAL_SIZE || get32(wire+48) != RETAIL_SIZE || get32(wire+52) != 3u) return 0;
    if (get32(wire+TOTAL_SIZE-4) != crc32(wire,TOTAL_SIZE-4)) return 0;
    if (!nonzero(profile,16) || !nonzero(profile+16,16) || !equal(wire+16,profile,32)) return 0;
    if (!retail_valid(retail)) return 0;
    network_codec_sha256(retail,RETAIL_SIZE,hash);
    if (!equal(hash,wire+56,32)) return 0;
    for (index=0; index<3u; ++index) {
        const u8 *record = retail + RETAIL_SIZE + index * RECORD_SIZE;
        u32 cursor = get32(record+20);
        if (record[0] != index || nonzero(record+1,3) || !equal(record+4,profile+32+16u*index,16)) return 0;
        if ((cursor == 0u) != !nonzero(record+24,32) || (!retail[16+index] && cursor)) return 0;
#ifdef CP3W_MULTIWORLD
        if(cursor>256u || (record[68]&0xf0u) || (record[69]&0xfcu) || nonzero(record+70,2) ||
           (((u32)record[72]<<8)|record[73])>255u || (((u32)record[74]<<8)|record[75])>13u ||
           nonzero(record+76,4) || (!retail[16+index] && nonzero(record+56,24))) return 0;
#endif
    }
    return 1;
}

/* All pointers refer to nonoverlapping, caller-sized diagnostic buffers. */
#if defined(_WIN32) && defined(CP3W_CODEC_HOST_TEST)
__declspec(dllexport)
#endif
int network_codec_encode(u8 *wire, u32 size, const u8 *retail, const u8 *profile, const u8 *records) {
    u32 index;
    if (size != TOTAL_SIZE || !retail_valid(retail)) return 0;
    for (index=0; index<TOTAL_SIZE; ++index) wire[index]=0;
    for (index=0; index<8u; ++index) wire[index]=((const u8 *)CP3W_SAVE_MAGIC)[index];
    put32(wire+8,CP3W_SAVE_VERSION); put32(wire+12,TOTAL_SIZE);
    for (index=0; index<32u; ++index) wire[16+index]=profile[index];
    put32(wire+48,RETAIL_SIZE); put32(wire+52,3);
    for (index=0; index<RETAIL_SIZE; ++index) wire[HEADER_SIZE+index]=retail[index];
    network_codec_sha256(retail,RETAIL_SIZE,wire+56);
    for (index=0; index<CP3W_RECORD_BYTES; ++index) wire[HEADER_SIZE+RETAIL_SIZE+index]=records[index];
    put32(wire+TOTAL_SIZE-4,crc32(wire,TOTAL_SIZE-4));
    return network_codec_validate(wire,size,profile);
}
