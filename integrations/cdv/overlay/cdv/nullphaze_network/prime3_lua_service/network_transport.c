/*
 * Reuse CP3W framing/session parsing for semantic status/delivery. Reset queued intent
 * with its peer/session while leaving committed inventory and checkpoint receipts for
 * reconciliation.
 */
/* Opt-in adapter around the diagnostic CP3W UDP transport, not the TCP tracker. */
static __attribute__((noinline)) int cp3w_network_dispatch(unsigned int,unsigned int);
extern void network_delivery_cancel(void);
#ifdef CP3W_OWNED_CP3W
/* Keep the established parser, never execute its withdrawn IOS lifecycle. */
#define runtime_poll_entry_impl legacy_runtime_poll_entry_impl
#endif
#include "../prime3_wii_runtime/relocated_runtime.c"
#ifdef CP3W_OWNED_CP3W
#undef runtime_poll_entry_impl
extern volatile u32 readiness_state[20], udp_probe_state[16];
void runtime_poll_entry_impl(void) { runtime_poll_counter++; }
#endif
extern u32 network_delivery_request(u32,u32,u32,const u8 *,u32,u8 *,u32 *);
#if defined(CP3W_TRACKER_READ_ONLY) || defined(CP3W_ITEM_SEQUENCE_TEST) || defined(CP3W_MULTIWORLD)
#include "tracker_transport.c"
#endif
#ifdef CP3W_MULTIWORLD
#include "connection_notice.h"
static u32 owned_mw_verified;
static struct mw_connection_notice owned_connection_notice;
#endif

int network_delivery_session_valid(u32 session) {
#ifdef CP3W_OWNED_CP3W
    if(readiness_state[18] || udp_probe_state[10] || udp_probe_state[1]==8u) return 0;
#endif
    return runtime_transport_cp3w_negotiated_flag && runtime_transport_cp3w_session_id==session;
}

#ifdef CP3W_OWNED_CP3W
/* Peer-bound, session-local proof before the explicit fixed delivery request. */
volatile u32 owned_cp3w_state[8] __attribute__((section(".data.readiness"),aligned(32))) = {
    0x4f435031u,0,0,0,0,0,0,0
};
#if defined(CP3W_TRACKER_READ_ONLY) || defined(CP3W_ITEM_SEQUENCE_TEST) || defined(CP3W_MULTIWORLD)
void owned_cp3w_reset_session(void) {
    /* Invalidate queued intent with the peer/session. Keep committed inventory
       and checkpoint receipts; reconnect must reconcile those, not grant again
       simply because the new HELLO has a different session ID. */
#ifdef CP3W_MULTIWORLD
    owned_mw_verified=0;
#endif
    network_delivery_cancel();
    runtime_transport_cp3w_negotiated_flag=0;
    runtime_transport_cp3w_session_id=0;
    runtime_transport_cp3w_accepted_capabilities=0;
    owned_cp3w_state[2]=0;
    tracker_session=0;
}
#endif
static u8 owned_peer[8];
#ifdef CP3W_MULTIWORLD
#include "multiworld_lease.h"
static unsigned long long owned_last_activity;
static unsigned long long owned_timebase(void) {
    u32 high,low,again;
    do {
        __asm__ volatile("mftbu %0" : "=r"(high));
        __asm__ volatile("mftb %0" : "=r"(low));
        __asm__ volatile("mftbu %0" : "=r"(again));
    } while(high!=again);
    return ((unsigned long long)high<<32)|low;
}
/* Read health and consume only a presentation edge; no transport/save writes. */
u32 owned_cp3w_claim_connection_notice(void) {
    u32 bus_clock=*(volatile u32 *)0x800000f8u;
    if(bus_clock<100000000u || bus_clock>400000000u) return 0;
    return mw_connection_notice_claim(&owned_connection_notice,
        mw_connection_live(owned_mw_verified,runtime_transport_cp3w_negotiated_flag,
            readiness_state[18] || udp_probe_state[10],owned_timebase(),
            owned_last_activity,bus_clock));
}
#endif
/* Snapshot only: these fields never influence framing or grant decisions. */
volatile u32 owned_cp3w_diagnostic[16] __attribute__((section(".data.readiness"),aligned(32))) = {
    0x4f434431u,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
};
u32 owned_cp3w_limit(void) {
#ifdef CP3W_MULTIWORLD
    return 0; /* Production sessions have no diagnostic packet-count ceiling. */
#elif defined(CP3W_TRACKER_READ_ONLY) || defined(CP3W_ITEM_SEQUENCE_TEST)
    return owned_cp3w_state[1]>=4096u;
#else
    return owned_cp3w_state[1]>=256u;
#endif
}
u32 owned_cp3w_request(const u8 *input,u32 length,const u8 *peer,u8 *output) {
    u32 i,command,was_negotiated=runtime_transport_cp3w_negotiated_flag;
#ifdef CP3W_MULTIWORLD
    u32 same_peer=1;
    unsigned long long now=owned_timebase();
    u32 bus_clock=*(volatile u32 *)0x800000f8u;
    if(was_negotiated) for(i=0;i<8;i++) if(peer[i]!=owned_peer[i]) same_peer=0;
    /* Only the supported Wii executable is installed. An invalid OS clock
       leaves ownership unchanged rather than expiring an active peer. */
    if(was_negotiated && bus_clock>=100000000u && bus_clock<=400000000u &&
       mw_peer_may_replace(same_peer,now,owned_last_activity,bus_clock)) {
        owned_cp3w_reset_session(); was_negotiated=0;
    }
#endif
    for(i=1;i<16;i++) owned_cp3w_diagnostic[i]=0;
    owned_cp3w_diagnostic[1]=length; owned_cp3w_diagnostic[2]=1;
    owned_cp3w_diagnostic[5]=length>=4 ? runtime_read_be32(input) : 0;
    owned_cp3w_diagnostic[7]=length>=16 ? runtime_read_be32(input+12) : 0;
    owned_cp3w_diagnostic[11]=was_negotiated;
    owned_cp3w_state[1]++;
    if(length>RUNTIME_UDP_RECEIVE_CAPACITY) { owned_cp3w_diagnostic[2]=0x84; return 0; }
    if(was_negotiated) for(i=0;i<8;i++) if(peer[i]!=owned_peer[i]) {
        owned_cp3w_state[5]++; owned_cp3w_diagnostic[2]=0x81; return 0;
    }
    runtime_transport_last_receive_length=length;
    runtime_transport_prepared_send_length=0;
    for(i=0;i<length;i++) runtime_transport_receive_payload_buffer[i]=input[i];
    owned_cp3w_diagnostic[2]=2;
    owned_cp3w_diagnostic[6]=length>=4 ? runtime_read_be32(runtime_transport_receive_payload_buffer) : 0;
    if(length>=4) {
        owned_cp3w_diagnostic[8]=runtime_read_be32(input+length-4);
        owned_cp3w_diagnostic[9]=runtime_crc32(input,length-4);
    }
    if(runtime_transport_validate_cp3w_ping_pong_frame()!=0) {
        owned_cp3w_state[5]++; owned_cp3w_diagnostic[2]=0x82;
        owned_cp3w_diagnostic[3]=runtime_transport_cp3w_last_frame_result; return 0;
    }
    owned_cp3w_diagnostic[2]=3;
    owned_cp3w_diagnostic[3]=runtime_transport_cp3w_last_frame_result;
    command=runtime_transport_cp3w_last_command;
#if defined(CP3W_TRACKER_READ_ONLY) || defined(CP3W_ITEM_SEQUENCE_TEST) || defined(CP3W_MULTIWORLD)
    if(command==RUNTIME_CP3W_COMMAND_DISCONNECT ||
       (command==RUNTIME_CP3W_COMMAND_HELLO && !was_negotiated)) tracker_session=0;
#endif
    if(command!=RUNTIME_CP3W_COMMAND_HELLO && command!=RUNTIME_CP3W_COMMAND_PING &&
       command!=RUNTIME_CP3W_COMMAND_DISCONNECT && command!=7u && command!=8u
#if defined(CP3W_TRACKER_READ_ONLY) || defined(CP3W_ITEM_SEQUENCE_TEST) || defined(CP3W_MULTIWORLD)
       && command!=9u
#ifdef CP3W_MULTIWORLD
       && command!=10u && command!=11u
#endif
#endif
       ) {
        owned_cp3w_state[5]++; owned_cp3w_diagnostic[2]=0x83; return 0;
    }
#if defined(CP3W_RX_AUDIT) || defined(CP3W_TRACKER_READ_ONLY)
    if(command==8u) {
        runtime_transport_prepare_cp3w_error_response(runtime_transport_cp3w_last_request_id,
            command,10,"Receive audit is read only",26);
    } else
#endif
    if(command==8u && owned_cp3w_state[2]!=3u) {
        owned_cp3w_state[6]++;
        runtime_transport_prepare_cp3w_error_response(runtime_transport_cp3w_last_request_id,
            command,10,"Session checks required",23);
    } else {
        runtime_transport_dispatch_cp3w_hello_session_request();
        if(!was_negotiated && runtime_transport_cp3w_negotiated_flag) {
#ifdef CP3W_MULTIWORLD
            owned_mw_verified=0;
#endif
            for(i=0;i<8;i++) owned_peer[i]=peer[i];
            owned_cp3w_state[2]=0; owned_cp3w_state[3]++;
        }
        if(command==RUNTIME_CP3W_COMMAND_PING && runtime_transport_cp3w_negotiated_flag &&
           runtime_transport_cp3w_last_dispatch_result==RUNTIME_CP3W_FRAME_RESULT_VALID) owned_cp3w_state[2]|=1u;
        /* READY or already-applied status is safe; only a fresh explicit capsule mutates. */
        if(command==7u && !runtime_transport_cp3w_last_dispatch_result &&
           runtime_transport_prepared_send_length==164u &&
           (runtime_transport_send_payload_bytes[17]==1u || runtime_transport_send_payload_bytes[17]==3u))
            owned_cp3w_state[2]|=2u;
        if(command==RUNTIME_CP3W_COMMAND_DISCONNECT) owned_cp3w_state[2]=0;
    }
    if(owned_cp3w_limit()) { network_delivery_cancel(); runtime_transport_cp3w_negotiated_flag=0; }
    if(runtime_transport_prepared_send_length>RUNTIME_UDP_SEND_CAPACITY) return 0;
    owned_cp3w_diagnostic[2]=5;
    owned_cp3w_diagnostic[4]=runtime_transport_cp3w_last_dispatch_result;
    owned_cp3w_diagnostic[10]=runtime_transport_prepared_send_length;
    owned_cp3w_diagnostic[11]=runtime_transport_cp3w_negotiated_flag;
    for(i=0;i<runtime_transport_prepared_send_length;i++) output[i]=runtime_transport_send_payload_bytes[i];
    owned_cp3w_state[4]+=runtime_transport_prepared_send_length!=0;
#ifdef CP3W_MULTIWORLD
    if(mw_peer_successful_reply(runtime_transport_cp3w_negotiated_flag,
                               runtime_transport_send_payload_bytes, runtime_transport_prepared_send_length)) {
        owned_last_activity=now;
        /* HELLO alone is not proof of a seed/world-bound multiworld client. */
        if(command==10u || command==11u) owned_mw_verified=1;
    }
#endif
    return runtime_transport_prepared_send_length;
}
#endif
static int cp3w_network_dispatch(u32 command,u32 length) {
    /* This dispatch adds semantic delivery to CP3W's existing framed parser.
       Packet CRC/length checks are transport integrity, not proof of a grant
       or save. The reply carries the service result without inventing either. */
    u32 code,size=0,crc,i;
#if defined(CP3W_TRACKER_READ_ONLY) || defined(CP3W_ITEM_SEQUENCE_TEST) || defined(CP3W_MULTIWORLD)
    u8 response[404];
#else
    u8 response[144];
#endif
    static const char error[]="Fixed delivery rejected; no durable acknowledgement.";
    if(!runtime_transport_cp3w_negotiated_flag) code=9;
#if defined(CP3W_TRACKER_READ_ONLY) || defined(CP3W_ITEM_SEQUENCE_TEST) || defined(CP3W_MULTIWORLD)
    else if(command==9u) {
        if(!(runtime_transport_cp3w_accepted_capabilities & (1u<<14))) code=11;
        else code=tracker_request(runtime_transport_cp3w_session_id,
            (const u8 *)(runtime_transport_receive_payload_buffer+16),length,response,&size);
    }
#ifdef CP3W_TRACKER_READ_ONLY
    else code=4;
#endif
#endif
#ifndef CP3W_TRACKER_READ_ONLY
#ifdef CP3W_MULTIWORLD
    else if(command==10u || command==11u) {
        if(!(runtime_transport_cp3w_accepted_capabilities & (1u<<15))) code=11;
        else code=network_delivery_request(command,runtime_transport_cp3w_session_id,
            runtime_transport_cp3w_last_request_id,
            (const u8 *)(runtime_transport_receive_payload_buffer+16),length,response,&size);
    }
    else code=4;
#else
    else if(!(runtime_transport_cp3w_accepted_capabilities & (1u<<13))) code=11;
    else code=network_delivery_request(command,runtime_transport_cp3w_session_id,
        runtime_transport_cp3w_last_request_id,
        (const u8 *)(runtime_transport_receive_payload_buffer+16),length,response,&size);
#endif
#endif
    if(code) {
        runtime_transport_prepare_cp3w_error_response(runtime_transport_cp3w_last_request_id,
            command,code,error,sizeof(error)-1);
        runtime_transport_cp3w_last_dispatch_result=code;
        return 7;
    }
    runtime_memzero(runtime_transport_send_payload_bytes,sizeof(runtime_transport_send_payload_bytes));
    runtime_memcpy(runtime_transport_send_payload_bytes,runtime_cp3w_magic,4);
    runtime_transport_send_payload_bytes[4]=1; runtime_transport_send_payload_bytes[5]=2;
    runtime_transport_send_payload_bytes[6]=command;
    runtime_write_be32(runtime_transport_send_payload_bytes+8,runtime_transport_cp3w_last_request_id);
    runtime_write_be32(runtime_transport_send_payload_bytes+12,size);
    for(i=0;i<size;i++) runtime_transport_send_payload_bytes[16+i]=response[i];
    crc=runtime_crc32(runtime_transport_send_payload_bytes,16+size);
    runtime_write_be32(runtime_transport_send_payload_bytes+16+size,crc);
    runtime_transport_prepared_send_length=20+size;
    runtime_transport_cp3w_last_response_id=runtime_transport_cp3w_last_request_id;
    runtime_transport_cp3w_last_response_status=0;
    runtime_transport_cp3w_last_dispatch_result=0;
    return 1;
}
