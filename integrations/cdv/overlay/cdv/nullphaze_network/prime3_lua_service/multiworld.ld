/*
 * This linker map places entry bridge_install with fixed address/limit values 0x817c1000,
 * 0x817e8440, 0x817fc3e0, 0x817ff000. I keep section order, alignment and exported symbols
 * paired with the bridge/bootstrap metadata; moving a section requires a new guarded build
 * proof.
 */
OUTPUT_ARCH(powerpc:common)
ENTRY(bridge_install)
SECTIONS {
    . = 0x817c1000;
    .text : ALIGN(32) {
        KEEP(*(.text.bridge_install)) KEEP(*(.text.bridge_boot))
        KEEP(*(.text.save_trace_hooks)) KEEP(*(.text.network_save_hooks))
        KEEP(*(.text.receipt_lifecycle_hooks)) KEEP(*(.text.receipt_coupling_hooks))
        KEEP(*(.text.receipt_delivery)) KEEP(*(.text.runtime.entry))
        KEEP(*(.text.rx_zero_layout))
        KEEP(*(.text.network_frame_poll))
        *(.text .text.* .rodata .rodata.*)
        . = ALIGN(32);
        . += 32; /* Preserve the startup-tested multiworld mutable-data placement. */
    }
    .data : ALIGN(32) {
        KEEP(*(.data.save_native_trace)) KEEP(*(.data.network_save_adapter))
        KEEP(*(.data.receipt_coupling)) KEEP(*(.data.receipt_delivery))
        KEEP(*(.data.network_delivery))
        . = ALIGN(32);
    }
    .owned_udp : ALIGN(32) { KEEP(*(.data.readiness)) }
    .runtime_state : ALIGN(32) {
        KEEP(*(.runtime_state.canary)) *(.runtime_state .runtime_state.*)
        *(.production_snapshot)
        *(.bss .bss.* .sbss .sbss.* COMMON)
        . = ALIGN(32);
    }
    ASSERT(SIZEOF(.data) == 80224, "exact multiworld receipt/network queue workspace required")
    ASSERT(ADDR(.data) == 0x817e8440, "multiworld startup-tested data placement changed")
    ASSERT(udp_probe_state == 0x817fc3e0, "multiworld startup-tested UDP placement changed")
    ASSERT(. < 0x817ff000, "combined runtime exceeds reserved memory/stack guard")
    /DISCARD/ : { *(.comment .eh_frame .note*) }
}
