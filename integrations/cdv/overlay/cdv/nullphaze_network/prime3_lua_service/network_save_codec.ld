/*
 * This linker map places entry network_codec_validate with fixed address/limit values
 * 0x817e1000, 0x817ef000. I keep section order, alignment and exported symbols paired with
 * the bridge/bootstrap metadata; moving a section requires a new guarded build proof.
 */
OUTPUT_ARCH(powerpc:common)
ENTRY(network_codec_validate)
SECTIONS
{
    . = 0x817e1000;
    .text : ALIGN(32) {
        KEEP(*(.text.network_codec_validate))
        KEEP(*(.text.network_codec_encode))
        KEEP(*(.text.network_codec_sha256))
        *(.text .text.* .rodata .rodata.*)
        . = ALIGN(32);
    }
    .data : { *(.data .data.* .sdata .sdata.*) }
    .bss : { *(.bss .bss.* .sbss .sbss.* COMMON) }
    ASSERT(SIZEOF(.data) == 0, "codec cannot own mutable state")
    ASSERT(SIZEOF(.bss) == 0, "codec cannot depend on BSS")
    ASSERT(. < 0x817ef000, "codec exceeds isolated test range")
    /DISCARD/ : { *(.comment .eh_frame .note*) }
}
