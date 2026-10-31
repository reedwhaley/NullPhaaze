/*
 * Embed the fixed seed-data blob in its own section. The linker and Python binder must
 * agree on that section's address and size before personalizing a template.
 */
/* SPDX-License-Identifier: GPL-3.0-or-later */
.section .rodata.multiworld_seed,"a",@progbits
.balign 4
.global mw_seed_data
.type mw_seed_data,@object
mw_seed_data:
.incbin MULTIWORLD_SEED_DATA_BINARY
.size mw_seed_data, .-mw_seed_data
