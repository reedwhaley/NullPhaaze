/*
 * This linker map places entry payload_entry with fixed address/limit values 0x806843c0,
 * 0x81100000. I keep section order, alignment and exported symbols paired with the
 * bridge/bootstrap metadata; moving a section requires a new guarded build proof.
 */
OUTPUT_ARCH(powerpc:common)
ENTRY(payload_entry)
SECTIONS
{
    . = 0x806843c0;
    .text : ALIGN(32)
    {
        *(.text.payload)
        *(.rodata.bridge_blob)
        . = ALIGN(32);
    }
    ASSERT(. < 0x81100000, "staging code exceeds retail apploader boundary")
    /DISCARD/ : { *(.comment .eh_frame .note*) }
}
