/*
 * These bounded zero-argument Lua claims consume presentation notices from the committed
 * receipt path. Claims never advance inventory or its receipt cursor.
 */
/* SPDX-License-Identifier: GPL-3.0-or-later. Zero-argument bounded HUD claims. */
extern u32 mw_claim_presentation(u32);
#define MW_BANKS(X) \
 X(0) X(1) X(2) X(3) X(4) X(5) X(6) X(7) \
 X(8) X(9) X(10) X(11) X(12) X(13) X(14) X(15) \
 X(16) X(17) X(18) X(19) X(20) X(21) X(22) X(23) \
 X(24) X(25) X(26) X(27) X(28) X(29) X(30) X(31) \
 X(32) X(33) X(34) X(35) X(36) X(37) X(38) X(39) \
 X(40) X(41) X(42) X(43) X(44) X(45) X(46) X(47) \
 X(48) X(49) X(50) X(51) X(52) X(53) X(54) X(55) \
 X(56) X(57) X(58) X(59) X(60) X(61) X(62) X(63)
#define MW_BANK_FUNCTION(n) \
 static int mw_claim_bank_##n(void *state) { \
     char text[9]; u32 event=mw_claim_presentation(n); \
     if(event==0xffffffffu) return 0; \
     hex32(text,event); text[8]=0; PUSH_STRING(state,text); return 1; \
 }
MW_BANKS(MW_BANK_FUNCTION)
#undef MW_BANK_FUNCTION
static void mw_register_presentation(void *state) {
#define MW_BANK_REGISTER(n) \
 PUSH_STRING(state,"CP3WClaimMWBank" #n); PUSH_CLOSURE(state,mw_claim_bank_##n,0); SET_TABLE(state,LUA_GLOBALS_INDEX);
 MW_BANKS(MW_BANK_REGISTER)
#undef MW_BANK_REGISTER
}
#undef MW_BANKS
