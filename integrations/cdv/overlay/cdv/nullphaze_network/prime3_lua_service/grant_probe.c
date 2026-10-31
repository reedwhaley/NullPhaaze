/*
 * This is the disposable-save one-shot missile experiment. Its narrow
 * retail/room/inventory preconditions do not authorize arbitrary network-provided
 * resources.
 */
/* Disposable-save experiment only. No network input or durable receipt claim. */
typedef unsigned int u32;
typedef int (*lua_function)(void *);
extern void bridge_read_only_install(void *, int);
extern int bridge_read_location(void *);

#define WORD(a) (*(volatile u32 *)(a))
#define PUSH_STRING ((void (*)(void *, const char *))0x8044dae0u)
#define PUSH_CLOSURE ((void (*)(void *, lua_function, int))0x8044dc60u)
#define SET_TABLE ((void (*)(void *, int))0x8044e168u)
#define ADD_CAPACITY ((void (*)(void *, u32, int))0x8019111cu)
#define ADD_AMOUNT ((void (*)(void *, u32, int))0x801913a0u)

struct receipt {
    u32 cookie, stage, before_amount, before_capacity;
    u32 after_amount, after_capacity, before_percent, before_percent_capacity;
};
__attribute__((section(".data.grant_probe")))
volatile struct receipt grant_probe_receipt = {0x47525031u, 0, 0, 0, 0, 0, 0, 0};

static int range(u32 address, u32 size) {
    return !(address & 3u) &&
        ((address >= 0x80000000u && address <= 0x81800000u - size) ||
         (address >= 0x90000000u && address <= 0x94000000u - size));
}

static int result(void *state, const char *text) {
    PUSH_STRING(state, text);
    return 1;
}

int grant_probe_once(void *state) {
    u32 game, player, context, world, amount, capacity, percent, percent_capacity, health;
    if (grant_probe_receipt.cookie != 0x47525031u)
        return result(state, "FAILED");
    if (grant_probe_receipt.stage)
        return result(state, grant_probe_receipt.stage == 2 ? "ALREADY_GRANTED" : "FAILED");
    game = WORD(0x8067dc0cu);
    if (!range(game, 0x28u)) return result(state, "DEFERRED");
    player = WORD(game + 0x24u);
    if (!range(player, 0x998u) || !(*(volatile unsigned char *)player & 0x80u))
        return result(state, "DEFERRED");
    health = WORD(player + 0xcu);
    if (!health || health >= 0x45000000u || WORD(player + 0x144u) > 14u)
        return result(state, "DEFERRED");
    if (!bridge_read_location(state)) return result(state, "DEFERRED");
    /* The location result is below our final status and discarded by Lua. */
    if (WORD(0x8067dc0cu) != game || WORD(game + 0x24u) != player)
        return result(state, "DEFERRED");
    context = WORD(0x805c4f98u);
    if (!range(context, 0x2188u)) return result(state, "DEFERRED");
    world = WORD(context + 0x2134u);
    if (!range(world, 0x80u) || WORD(world + 0x18u) != 0xc133f919u ||
        WORD(world + 0x1cu) != 0xc108bdf9u || WORD(world + 0x7cu) != 2u)
        return result(state, "DEFERRED");
    amount = WORD(player + 0x84u);
    capacity = WORD(player + 0x88u);
    percent = WORD(player + 0x150u);
    percent_capacity = WORD(player + 0x154u);
    if (capacity != 15u || amount > capacity || percent > percent_capacity || percent_capacity >= 255u)
        return result(state, "INELIGIBLE");
    grant_probe_receipt.before_amount = amount;
    grant_probe_receipt.before_capacity = capacity;
    grant_probe_receipt.before_percent = percent;
    grant_probe_receipt.before_percent_capacity = percent_capacity;
    /* Claim before invoking listeners: reentrant calls cannot apply twice. */
    grant_probe_receipt.stage = 1;
    ADD_CAPACITY((void *)player, 21u, 1);
    ADD_AMOUNT((void *)player, 21u, 1);
    ADD_CAPACITY((void *)player, 4u, 5);
    ADD_AMOUNT((void *)player, 4u, 5);
    grant_probe_receipt.after_amount = WORD(player + 0x84u);
    grant_probe_receipt.after_capacity = WORD(player + 0x88u);
    if (grant_probe_receipt.after_amount != amount + 5u || grant_probe_receipt.after_capacity != 20u ||
        WORD(player + 0x150u) != percent + 1u || WORD(player + 0x154u) != percent_capacity + 1u) {
        grant_probe_receipt.stage = 3;
        return result(state, "FAILED");
    }
    grant_probe_receipt.stage = 2;
    return result(state, "GRANTED");
}

__attribute__((section(".text.bridge_install")))
void bridge_install(void *state, int index) {
    bridge_read_only_install(state, index);
    if (index != -10001) return;
    PUSH_STRING(state, "CP3WGrantMissileExpansion");
    PUSH_CLOSURE(state, grant_probe_once, 0);
    SET_TABLE(state, -10001);
}
