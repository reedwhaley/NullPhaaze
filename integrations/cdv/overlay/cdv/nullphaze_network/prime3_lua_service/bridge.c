/*
 * The retail Lua dispatcher enters this bounded bridge. Keep the supported executable
 * guards and callback ABI with the installed native service; diagnostic flags do not
 * authorize general game writes.
 */
/* Supported retail NTSC-U only; entered through the game's own Lua dispatcher. */
typedef unsigned int u32;
typedef int (*lua_function)(void *);
#ifdef CP3W_NETWORK_DELIVERY
extern void runtime_entry(void);
#endif

/* The shared relocation bootstrap calls this once before original startup. */
__attribute__((section(".text.bridge_boot")))
void bridge_boot(void) {
#ifdef CP3W_RX_MEM2
    extern void udp_reserve_mem2(void);
    udp_reserve_mem2();
#endif
#ifdef CP3W_NETWORK_DELIVERY
    runtime_entry();
#endif
}

#define LUA_GLOBALS_INDEX (-10001)
#ifndef CP3W_MEM1_RESERVED_HIGH
#define CP3W_MEM1_RESERVED_HIGH 0x817e0000u
#endif
#define MEM1_RESERVED_HIGH CP3W_MEM1_RESERVED_HIGH
#define SET_TABLE ((void (*)(void *, int))0x8044e168u)
#define PUSH_STRING ((const char *(*)(void *, const char *))0x8044dae0u)
#define PUSH_CLOSURE ((void (*)(void *, lua_function, int))0x8044dc60u)
#if defined(CP3W_NETWORK_READINESS) || defined(CP3W_OWNED_CP3W)
extern int readiness_tick(void *);
extern int readiness_render(void *);
#endif
#ifdef CP3W_RECEIPT_COUPLING
#ifdef CP3W_RECEIPT_DELIVERY
extern void receipt_delivery_tick(void *);
static int receipt_tick(void *state) { receipt_delivery_tick(state); return 0; }
#else
extern void coupling_test_tick(void);
static int receipt_tick(void *state) { (void)state; coupling_test_tick(); return 0; }
#endif
#endif

struct location {
    u32 game, context, world, player, area;
    u32 world_hi, world_lo, area_hi, area_lo, internal_hi, internal_lo, index;
};

static int range(u32 address, u32 size) {
    return size && !(address & 3u) &&
        ((address >= 0x80000000u && address <= 0x81800000u - size) ||
         (address >= 0x90000000u && address <= 0x94000000u - size));
}

static u32 word(u32 address) {
    return *(volatile const u32 *)address;
}

static int snapshot(struct location *out) {
    u32 vector, count;
    if (word(0x80000034u) != MEM1_RESERVED_HIGH || word(0x80003110u) != MEM1_RESERVED_HIGH)
        return 0;
    out->game = word(0x8067dc0cu);
    out->context = word(0x805c4f98u);
    if (!range(out->game, 0x10u) || !range(out->context, 0x2188u)) return 0;
    out->world = word(out->context + 0x2134u);
    out->player = word(out->context + 0x2184u);
    if (!range(out->world, 0x80u) || !range(out->player, 4u) ||
        word(out->player) != 0x80592c78u) return 0;
    out->world_hi = word(out->world + 0x18u);
    out->world_lo = word(out->world + 0x1cu);
    if (word(out->game + 8u) != out->world_hi || word(out->game + 12u) != out->world_lo)
        return 0;
    count = word(out->world + 0x30u);
    out->index = word(out->world + 0x7cu);
    vector = word(out->world + 0x38u);
    if (!count || count > 512u || out->index >= count || !range(vector, count * 8u)) return 0;
    out->area = word(vector + out->index * 8u + 4u);
    if (!range(out->area, 0x9cu) || word(out->area) != 0x8059110cu ||
        word(out->area + 4u) != out->index || word(out->area + 0x98u) != 0x11u) return 0;
    out->area_hi = word(out->area + 0x58u);
    out->area_lo = word(out->area + 0x5cu);
    out->internal_hi = word(out->area + 0x60u);
    out->internal_lo = word(out->area + 0x64u);
    if ((out->area_hi == 0xffffffffu && out->area_lo == 0xffffffffu) ||
        (!out->area_hi && !out->area_lo)) return 0;
    return 1;
}

#if defined(CP3W_TRACKER_READ_ONLY) || defined(CP3W_ITEM_SEQUENCE_TEST) || defined(CP3W_MULTIWORLD)
/* Called by the owned dispatcher on the game thread; never invokes a mutator. */
int bridge_tracker_snapshot(u32 *out) {
    struct location first, second;
    u32 game, inventory, i, a[140], b[140];
    if (!snapshot(&first)) return 0;
    game=first.game;
    if(!range(game,0x28u)) return 0;
    inventory=word(game+0x24u);
    if(!range(inventory,0x998u) || !(*(volatile unsigned char *)inventory & 0x80u)) return 0;
    for(i=0;i<140;i++) a[i]=word(inventory+0x54u+(i/2u)*12u+(i%2u)*4u);
    out[9]=word(inventory+0xcu);
    for(i=0;i<140;i++) b[i]=word(inventory+0x54u+(i/2u)*12u+(i%2u)*4u);
    if(!snapshot(&second) || word(game+0x24u)!=inventory || word(inventory+0xcu)!=out[9]) return 0;
    for(i=0;i<sizeof(first)/4u;i++) if(((u32 *)&first)[i]!=((u32 *)&second)[i]) return 0;
    for(i=0;i<140;i++) if(a[i]!=b[i]) return 0;
    out[0]=0x54524b31u; out[1]=1;
    out[2]=first.world_hi; out[3]=first.world_lo;
    out[4]=first.area_hi; out[5]=first.area_lo;
    out[6]=first.internal_hi; out[7]=first.internal_lo; out[8]=first.index;
    for(i=0;i<140;i++) out[10+i]=a[i];
    return 1;
}
#endif

#ifdef CP3W_MULTIWORLD
static void hex32(char *,u32);
extern u32 owned_cp3w_claim_connection_notice(void);
static int bridge_connection_notice(void *state) {
    u32 event;
    if(!range((u32)state,0x60u)) return 0;
    event=owned_cp3w_claim_connection_notice();
    if(!event) return 0;
    PUSH_STRING(state,event==1u ? "lost" : "restored");
    return 1;
}
int bridge_area_matches(u32 hi,u32 lo) {
    struct location first,second; u32 i;
    if(!snapshot(&first) || !snapshot(&second) || first.area_hi!=hi || first.area_lo!=lo) return 0;
    for(i=0;i<sizeof(first)/4u;i++) if(((u32 *)&first)[i]!=((u32 *)&second)[i]) return 0;
    return 1;
}
extern int mw_collect_location(u32);
extern u32 mw_presentation(u32 *);
#include "multiworld_lua.inc"
#include "multiworld_presentation_lua.inc"
static int bridge_mw_presentation(void *state) {
    char text[18]; u32 recipe,serial=mw_presentation(&recipe);
    hex32(text,serial); text[8]=':'; hex32(text+9,recipe); text[17]=0;
    PUSH_STRING(state,text); return 1;
}
#endif

static void hex32(char *out, u32 value) {
    static const char digits[] = "0123456789abcdef";
    u32 i;
    for (i = 0; i < 8; ++i) out[i] = digits[(value >> (28u - 4u * i)) & 15u];
}

#ifdef CP3W_OWNED_CP3W
extern volatile u32 readiness_state[20], udp_probe_state[16], owned_cp3w_state[8];
extern volatile u32 owned_cp3w_diagnostic[16], receipt_delivery_state[16];
int bridge_network_status(void *state) {
    char text[126];
    u32 i;
    const u32 values[14] = {readiness_state[1],readiness_state[9],udp_probe_state[1],
        readiness_state[18] ? readiness_state[18] : udp_probe_state[10],
        owned_cp3w_diagnostic[11],owned_cp3w_state[2],owned_cp3w_state[3],owned_cp3w_state[5],
        owned_cp3w_diagnostic[3],owned_cp3w_diagnostic[4],receipt_delivery_state[3],receipt_delivery_state[2],
        word(0x8067dc0cu),receipt_delivery_state[6]};
    if(!range((u32)state,0x60u)) return 0;
    for(i=0;i<14;i++) { hex32(text+i*9,values[i]); text[i*9+8]=':'; }
    text[125]=0;
    PUSH_STRING(state,text);
    return 1;
}
#endif

int bridge_read_location(void *state) {
    struct location first, second;
    const u32 *a = (const u32 *)&first;
    const u32 *b = (const u32 *)&second;
    char text[60];
    u32 i;
    if (!range((u32)state, 0x60u) || !snapshot(&first) || !snapshot(&second)) return 0;
    for (i = 0; i < sizeof(first) / sizeof(u32); ++i) if (a[i] != b[i]) return 0;
    hex32(text, first.world_hi); hex32(text + 8, first.world_lo); text[16] = ':';
    hex32(text + 17, first.area_hi); hex32(text + 25, first.area_lo); text[33] = ':';
    hex32(text + 34, first.internal_hi); hex32(text + 42, first.internal_lo); text[50] = ':';
    hex32(text + 51, first.index); text[59] = 0;
    PUSH_STRING(state, text);
    return 1;
}

__attribute__((section(".text.bridge_install")))
void bridge_install(void *state, int index) {
    /* Finish the displaced IsCurrentWorld registration before adding ours. */
    SET_TABLE(state, index);
    if (index != LUA_GLOBALS_INDEX) return;
#ifdef CP3W_MULTIWORLD
    mw_register_locations(state);
    mw_register_presentation(state);
    PUSH_STRING(state,"CP3WPresentation"); PUSH_CLOSURE(state,bridge_mw_presentation,0);
    SET_TABLE(state,LUA_GLOBALS_INDEX);
    PUSH_STRING(state,"CP3WClaimConnectionNotice"); PUSH_CLOSURE(state,bridge_connection_notice,0);
    SET_TABLE(state,LUA_GLOBALS_INDEX);
#endif
    PUSH_STRING(state, "CP3WReadLocation");
    PUSH_CLOSURE(state, bridge_read_location, 0);
    SET_TABLE(state, LUA_GLOBALS_INDEX);
#if defined(CP3W_NETWORK_READINESS) || defined(CP3W_OWNED_CP3W)
    PUSH_STRING(state, "CP3WNetworkReadinessTick");
    PUSH_CLOSURE(state, readiness_tick, 0);
    SET_TABLE(state, LUA_GLOBALS_INDEX);
    PUSH_STRING(state, "CP3WNetworkReadinessDraw");
    PUSH_CLOSURE(state, readiness_render, 0);
    SET_TABLE(state, LUA_GLOBALS_INDEX);
#endif
#ifdef CP3W_OWNED_CP3W
    PUSH_STRING(state, "CP3WNetworkStatus");
    PUSH_CLOSURE(state, bridge_network_status, 0);
    SET_TABLE(state, LUA_GLOBALS_INDEX);
#endif
#ifdef CP3W_RECEIPT_COUPLING
    PUSH_STRING(state, "CP3WReceiptProbeTick");
    PUSH_CLOSURE(state, receipt_tick, 0);
    SET_TABLE(state, LUA_GLOBALS_INDEX);
#endif
}
