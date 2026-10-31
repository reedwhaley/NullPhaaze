/*
 * This hook preserves the retail calling context around the frame pump and resumes the
 * displaced path. Register saves and continuation address are part of the hook contract.
 */
/* SPDX-License-Identifier: GPL-3.0-or-later */
.section .text.network_frame_poll,"ax",@progbits
.global network_frame_poll_hook
.type network_frame_poll_hook,@function
network_frame_poll_hook:
    /* CGraphics::EndScene has no arguments or return value. The C call preserves
       nonvolatile registers; restore the caller LR before the displaced entry. */
    stwu 1,-0x20(1)
    mflr 0
    stw 0,0x24(1)
    bl network_frame_poll
    lwz 0,0x24(1)
    mtlr 0
    addi 1,1,0x20
    stwu 1,-0x130(1)
    lis 12,0x803e
    ori 12,12,0x9f7c
    mtctr 12
    bctr
.size network_frame_poll_hook,.-network_frame_poll_hook
