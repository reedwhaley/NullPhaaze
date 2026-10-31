/*
 * Embed the already compiled bridge in the bootstrap. The loader's copy/cache ranges must
 * match the complete blob and its reserved destination.
 */
.section .rodata.bridge_blob, "a", @progbits
.balign 32
.global payload_embedded_runtime_start
.global payload_embedded_runtime_end
payload_embedded_runtime_start:
.incbin BRIDGE_BINARY
payload_embedded_runtime_end:
