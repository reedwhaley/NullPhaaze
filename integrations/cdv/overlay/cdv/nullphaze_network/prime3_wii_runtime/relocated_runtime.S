/*
 * This is the relocated runtime entry ABI. Keep the assembly entry, linked C body and
 * exported metadata aligned; a successful link alone does not establish a supported retail
 * hook.
 */
.section .text.runtime.entry, "ax", @progbits

#ifndef PRIME3_ENABLE_RECURRING_HOOK_DIAGNOSTICS
#define PRIME3_ENABLE_RECURRING_HOOK_DIAGNOSTICS 0
#endif

#ifndef PRIME3_IOS_UDP_DIAGNOSTIC_MODE
#define PRIME3_IOS_UDP_DIAGNOSTIC_MODE 0
#endif

#if PRIME3_IOS_UDP_DIAGNOSTIC_MODE == 22 || PRIME3_IOS_UDP_DIAGNOSTIC_MODE == 23
#define PRIME3_ENABLE_NATIVE_NETWORK_READINESS 1
#else
#define PRIME3_ENABLE_NATIVE_NETWORK_READINESS 0
#endif

.global runtime_entry
.global runtime_poll_entry
.global runtime_poll_hook_wrapper
.global runtime_call_retail_ios_open_async
.global runtime_call_retail_ios_close_async
.global runtime_call_retail_read_async
.global runtime_call_retail_write_async
.global runtime_call_retail_ios_ioctl_async
.global runtime_call_retail_ios_ioctlv_async
.global runtime_call_retail_nwc24_open_lib
.global runtime_call_retail_network_bootstrap
.global runtime_read_retail_so_fd
.global runtime_call_retail_veneer_selftest
.global runtime_canary_start
.global runtime_canary_end

.type runtime_entry, @function
.type runtime_poll_entry, @function
.type runtime_poll_hook_wrapper, @function
.type runtime_call_retail_ios_open_async, @function
.type runtime_call_retail_ios_close_async, @function
.type runtime_call_retail_read_async, @function
.type runtime_call_retail_write_async, @function
.type runtime_call_retail_ios_ioctl_async, @function
.type runtime_call_retail_ios_ioctlv_async, @function
.type runtime_call_retail_nwc24_open_lib, @function
.type runtime_call_retail_network_bootstrap, @function
.type runtime_read_retail_so_fd, @function
.type runtime_call_retail_veneer_selftest, @function

runtime_entry:
#if PRIME3_EARLY_SDA_CAPTURE
    lis     11, runtime_abi_probe_saved_r2@ha
    stw     2, runtime_abi_probe_saved_r2@l(11)
    lis     11, runtime_abi_probe_saved_r13@ha
    stw     13, runtime_abi_probe_saved_r13@l(11)
    lis     11, runtime_abi_probe_after_call_flag@ha
    li      12, 1
    stw     12, runtime_abi_probe_after_call_flag@l(11)
#endif
    b       runtime_entry_impl

.size runtime_entry, . - runtime_entry

runtime_poll_entry:
    b       runtime_poll_entry_impl

.size runtime_poll_entry, . - runtime_poll_entry

.macro diag_increment symbol
#if PRIME3_ENABLE_RECURRING_HOOK_DIAGNOSTICS
    lis     11, \symbol@ha
    lwz     12, \symbol@l(11)
    addi    12, 12, 1
    stw     12, \symbol@l(11)
#endif
.endm

.macro diag_store_marker value
#if PRIME3_ENABLE_RECURRING_HOOK_DIAGNOSTICS
    lis     11, runtime_last_execution_marker@ha
    lis     12, \value@h
    ori     12, 12, \value@l
    stw     12, runtime_last_execution_marker@l(11)
#endif
.endm

.macro capture_game_sda_registers
    lis     11, runtime_verified_game_r2@ha
    stw     2, runtime_verified_game_r2@l(11)
    lis     11, runtime_verified_game_r13@ha
    stw     13, runtime_verified_game_r13@l(11)
.endm

.macro install_verified_game_sda_registers
    lis     11, runtime_verified_game_r2@ha
    lwz     2, runtime_verified_game_r2@l(11)
    lis     11, runtime_verified_game_r13@ha
    lwz     13, runtime_verified_game_r13@l(11)
.endm

.macro retail_call_veneer name, target
\name:
    stwu    1, -0x20(1)
    addi    11, 1, 0x20
    lis     12, runtime_abi_probe_stack_pointer_before@ha
    stw     11, runtime_abi_probe_stack_pointer_before@l(12)
    mflr    0
    stw     0, 0x08(1)
    stw     2, 0x0C(1)
    stw     13, 0x10(1)
    lis     11, runtime_abi_probe_saved_lr@ha
    stw     0, runtime_abi_probe_saved_lr@l(11)
    lis     11, runtime_abi_probe_saved_r2@ha
    stw     2, runtime_abi_probe_saved_r2@l(11)
    lis     11, runtime_abi_probe_saved_r13@ha
    stw     13, runtime_abi_probe_saved_r13@l(11)
    lis     11, runtime_abi_probe_pre_call_args@ha
    stw     3, runtime_abi_probe_pre_call_args@l(11)
    stw     4, runtime_abi_probe_pre_call_args+4@l(11)
    stw     5, runtime_abi_probe_pre_call_args+8@l(11)
    stw     6, runtime_abi_probe_pre_call_args+12@l(11)
    stw     7, runtime_abi_probe_pre_call_args+16@l(11)
    stw     8, runtime_abi_probe_pre_call_args+20@l(11)
    stw     9, runtime_abi_probe_pre_call_args+24@l(11)
    stw     10, runtime_abi_probe_pre_call_args+28@l(11)
    diag_increment runtime_retail_veneer_entry_count
    diag_store_marker 0xC0DE0005
    install_verified_game_sda_registers
    diag_store_marker 0xC0DE0006
    lis     12, \target@h
    ori     12, 12, \target@l
    lis     11, runtime_abi_probe_target_ctr@ha
    stw     12, runtime_abi_probe_target_ctr@l(11)
    mtctr   12
    bctrl
    stw     3, 0x14(1)
    diag_increment runtime_retail_target_return_count
    diag_store_marker 0xC0DE0007
    lwz     2, 0x0C(1)
    lwz     13, 0x10(1)
    lis     11, runtime_abi_probe_restored_r2@ha
    stw     2, runtime_abi_probe_restored_r2@l(11)
    lis     11, runtime_abi_probe_restored_r13@ha
    stw     13, runtime_abi_probe_restored_r13@l(11)
    diag_store_marker 0xC0DE0008
    lwz     0, 0x08(1)
    lis     11, runtime_abi_probe_restored_lr@ha
    stw     0, runtime_abi_probe_restored_lr@l(11)
    mtlr    0
    lwz     3, 0x14(1)
    diag_increment runtime_retail_veneer_exit_count
    diag_store_marker 0xC0DE0009
    addi    1, 1, 0x20
    lis     11, runtime_abi_probe_stack_pointer_after@ha
    stw     1, runtime_abi_probe_stack_pointer_after@l(11)
    blr

.size \name, . - \name
.endm

runtime_poll_hook_wrapper:
    stwu    1, -0x40(1)
    mflr    0
    stw     0, 0x3C(1)
    mfcr    0
    stw     0, 0x38(1)
    mfxer   0
    stw     0, 0x34(1)
    stw     2, 0x30(1)
    stw     3, 0x2C(1)
    stw     11, 0x28(1)
    stw     12, 0x24(1)
    stw     13, 0x20(1)
    capture_game_sda_registers

    diag_increment runtime_hook_wrapper_entry_count
    diag_store_marker 0xC0DE0001
    diag_increment runtime_hook_wrapper_before_poll_count

    bl      runtime_poll_entry_impl

    diag_increment runtime_poll_exit_count
    diag_increment runtime_hook_wrapper_after_poll_count
    diag_store_marker 0xC0DE0006

    lwz     3, 0x2C(1)

    diag_store_marker 0xC0DE0007
    diag_increment runtime_hook_wrapper_exit_count

    lwz     13, 0x20(1)
    lwz     12, 0x24(1)
    lwz     11, 0x28(1)
    lwz     2, 0x30(1)
    lwz     0, 0x34(1)
    mtxer   0
    lwz     0, 0x38(1)
    mtcrf   0xFF, 0
    lwz     0, 0x3C(1)
    mtlr    0
    addi    1, 1, 0x40
    lwz     3, 0x24(3)
    diag_store_marker 0xC0DE0008
    lis     12, PRIME3_RUNTIME_POLL_HOOK_CONTINUATION_ADDRESS@h
    ori     12, 12, PRIME3_RUNTIME_POLL_HOOK_CONTINUATION_ADDRESS@l
    mtctr   12
    bctr

.size runtime_poll_hook_wrapper, . - runtime_poll_hook_wrapper

retail_call_veneer runtime_call_retail_ios_open_async, PRIME3_RETAIL_IOS_OPEN_ASYNC_ADDRESS
retail_call_veneer runtime_call_retail_ios_close_async, PRIME3_RETAIL_IOS_CLOSE_ASYNC_ADDRESS
retail_call_veneer runtime_call_retail_read_async, PRIME3_RETAIL_IOS_READ_ASYNC_ADDRESS
retail_call_veneer runtime_call_retail_write_async, PRIME3_RETAIL_IOS_WRITE_ASYNC_ADDRESS
retail_call_veneer runtime_call_retail_ios_ioctl_async, PRIME3_RETAIL_IOS_IOCTL_ASYNC_ADDRESS
retail_call_veneer runtime_call_retail_ios_ioctlv_async, PRIME3_RETAIL_IOS_IOCTLV_ASYNC_ADDRESS
retail_call_veneer runtime_call_retail_nwc24_open_lib, PRIME3_RETAIL_NWC24_OPEN_LIB_ADDRESS
retail_call_veneer runtime_call_retail_network_bootstrap, PRIME3_RETAIL_NETWORK_BOOTSTRAP_ADDRESS
retail_call_veneer runtime_call_retail_veneer_selftest, runtime_local_veneer_selftest_target

runtime_read_retail_so_fd:
    stwu    1, -0x10(1)
    stw     13, 0x08(1)
    install_verified_game_sda_registers
    lwz     3, PRIME3_RETAIL_SO_FD_SDA_OFFSET(13)
    lwz     13, 0x08(1)
    addi    1, 1, 0x10
    blr

.size runtime_read_retail_so_fd, . - runtime_read_retail_so_fd

.section .runtime_state.canary, "aw", @progbits
.balign 32
runtime_canary_start:
    .byte   0x50, 0x33, 0x48, 0x49, 0x52, 0x55, 0x4E, 0x54
    .byte   0x49, 0x4D, 0x45, 0x43, 0x41, 0x4E, 0x41, 0x52
runtime_canary_end:
