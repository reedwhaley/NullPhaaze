/*
 * Embed the 80-byte bound checkpoint profile. Keep the profile in its declared data
 * section so seed binding cannot overwrite neighboring instructions.
 */
.section .rodata.network_save_profile,"a",@progbits
.balign 4
.global network_save_profile
network_save_profile:
.incbin NETWORK_SAVE_PROFILE_BINARY
