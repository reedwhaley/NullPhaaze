/*
 * This linker map places entry runtime_entry with fixed address/limit values 0xB0C0,
 * 0xB118, 0xB370, 0xBA10. I keep section order, alignment and exported symbols paired with
 * the bridge/bootstrap metadata; moving a section requires a new guarded build proof.
 */
OUTPUT_ARCH(powerpc:common)
ENTRY(runtime_entry)

SECTIONS
{
    runtime_layout_base = DEFINED(__runtime_link_address) ? __runtime_link_address : 0;
    runtime_preserve_ping_layout =
        DEFINED(__runtime_preserve_ping_layout) ? __runtime_preserve_ping_layout : 0;
    runtime_force_isolated_layout =
        DEFINED(__runtime_force_isolated_layout) ? __runtime_force_isolated_layout : 0;
    . = runtime_layout_base;

    runtime_code_start = .;
    .text : ALIGN(4)
    {
        KEEP(*(.text.runtime.entry))
        KEEP(*(.text.runtime.keep))
        *(.text.runtime .text.runtime.*)
        *(.text .text.*)
    }
    runtime_executable_code_end = .;
    ASSERT(
        !runtime_preserve_ping_layout || . <= runtime_layout_base + 0xB0C0,
        "runtime executable code overlaps fixed diagnostic switch tables"
    )
    . = runtime_preserve_ping_layout ? runtime_layout_base + 0xB0C0 : ALIGN(4);
    .runtime_switch_rodata : ALIGN(4)
    {
        *(.rodata.CSWTCH.*)
    }
    ASSERT(
        !runtime_preserve_ping_layout || . <= runtime_layout_base + 0xB118,
        "runtime switch tables exceed diagnostic range"
    )
    . = runtime_preserve_ping_layout ? runtime_layout_base + 0xB118 : ALIGN(4);
    .runtime_rodata : ALIGN(4)
    {
        *(.rodata.runtime)
        *(.rodata)
    }
    ASSERT(
        !runtime_preserve_ping_layout || . <= runtime_layout_base + 0xB370,
        "fixed runtime rodata exceeds diagnostic range"
    )
    . = runtime_preserve_ping_layout ? runtime_layout_base + 0xB370 : ALIGN(4);
    .runtime_compiler_rodata : ALIGN(4)
    {
        *(.rodata.runtime.core)
        *(.rodata.*)
    }
    . = runtime_force_isolated_layout ? runtime_layout_base + 0xBA10 : .;
    runtime_code_end = .;

    . = ALIGN(32);
    ASSERT(
        !runtime_preserve_ping_layout || . <= runtime_layout_base + 0xC740,
        "runtime code overlaps production snapshot"
    )
    . = runtime_preserve_ping_layout
        ? runtime_layout_base + 0xC740
        : runtime_force_isolated_layout ? runtime_layout_base + 0xBA20 : ALIGN(32);
    runtime_production_snapshot_start = .;
    .production_snapshot : ALIGN(32)
    {
        KEEP(*(.production_snapshot))
    }
    runtime_production_snapshot_end = .;
    ASSERT(
        runtime_production_snapshot_end - runtime_production_snapshot_start == 0x70,
        "production snapshot size changed"
    )
    ASSERT(
        !runtime_preserve_ping_layout || runtime_production_snapshot_end <= runtime_layout_base + 0xC7C0,
        "production snapshot overlaps state"
    )
    /* Keep networking state addresses stable after compiling out the renderer. */
    . = runtime_preserve_ping_layout
        ? runtime_layout_base + 0xC7C0
        : runtime_force_isolated_layout ? runtime_layout_base + 0xBAA0 : ALIGN(32);
    runtime_state_start = .;
    .runtime_state : ALIGN(32)
    {
        KEEP(*(.runtime_state.canary))
        *(.runtime_state .runtime_state.*)
        *(.data .data.*)
        *(.bss .bss.* COMMON)
    }
    . = runtime_force_isolated_layout ? runtime_layout_base + 0xCC80 : .;
    runtime_state_end = .;

    /DISCARD/ :
    {
        *(.comment)
        *(.eh_frame)
        *(.note*)
    }
}
