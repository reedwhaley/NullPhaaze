/*
 * This linker map places entry bridge_install with fixed address/limit values 0x817e1000,
 * 0x817ff000. I keep section order, alignment and exported symbols paired with the
 * bridge/bootstrap metadata; moving a section requires a new guarded build proof.
 */
OUTPUT_ARCH(powerpc:common)
ENTRY(bridge_install)
SECTIONS
{
    . = 0x817e1000;
    .text : ALIGN(32) {
        KEEP(*(.text.bridge_install))
        KEEP(*(.text.bridge_boot))
        KEEP(*(.text.save_trace_hooks))
        KEEP(*(.text.network_save_hooks))
        KEEP(*(.text.receipt_lifecycle_hooks))
        KEEP(*(.text.receipt_coupling_hooks))
        *(.text .text.* .rodata .rodata.*)
        . = ALIGN(32);
    }
    .data : ALIGN(32) {
        KEEP(*(.data.save_native_trace))
        KEEP(*(.data.network_save_adapter))
        KEEP(*(.data.receipt_coupling))
        . = ALIGN(32);
    }
    .bss : { *(.bss .bss.* .sbss .sbss.* COMMON) }
    ASSERT(SIZEOF(.data) == 78752, "exact trace, adapter and coupling workspace required")
    ASSERT(SIZEOF(.bss) == 0, "coupling cannot depend on BSS")
    ASSERT(. < 0x817ff000, "coupling exceeds reserved region with stack guard")
    /DISCARD/ : { *(.comment .eh_frame .note*) }
}
