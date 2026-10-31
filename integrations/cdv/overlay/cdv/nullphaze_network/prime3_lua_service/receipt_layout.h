/*
 * MW01 uses its own 80-byte receipt and new-save container; the older experiment uses 56
 * bytes. Preserve the compile-time layout boundary and the three-slot wire-size
 * calculation.
 */
/* SPDX-License-Identifier: GPL-3.0-or-later
 * MW01 is a new-save format; the experimental CP3WNSV1 remains unchanged. */
#ifndef CP3W_RECEIPT_LAYOUT_H
#define CP3W_RECEIPT_LAYOUT_H
#ifdef CP3W_MULTIWORLD
#define CP3W_RECEIPT_SIZE 80u
#define CP3W_SAVE_MAGIC "NPMWSV01"
#define CP3W_SAVE_VERSION 0x00020058u
#else
#define CP3W_RECEIPT_SIZE 56u
#define CP3W_SAVE_MAGIC "CP3WNSV1"
#define CP3W_SAVE_VERSION 0x00010058u
#endif
#define CP3W_RECORD_BYTES (3u * CP3W_RECEIPT_SIZE)
#define CP3W_WIRE_SIZE (65536u + 88u + CP3W_RECORD_BYTES + 4u)
#endif
