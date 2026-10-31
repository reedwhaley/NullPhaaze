# Exact-executable guards for the isolated pre-OS MEM2 reservation experiment. Boundary
# names here: validate, validate_owned_manifest.
"""Exact-executable guards for the isolated pre-OS MEM2 reservation experiment."""

import struct

from randovania.games.prime3.exporter.dol_patcher import parse_dol_header
from nullphaze_network.prime3_lua_service import probe

# Names describe observed instructions and callers, not imported SDK symbols.
GUARDS = {
    0x80006510: 0x3DA08068,  # Retail r13 base setup.
    0x80006514: 0x61AD01C0,
    0x804DE280: 0x80633128,  # OS initialization consumes boot MEM2 upper bound.
    0x804DE28C: 0x480010E5,  # Calls the upper-bound setter below.
    0x804DF340: 0x806DE2C4,  # Upper bound getter at r13-0x1d3c.
    0x804DF358: 0x806D99AC,  # Lower bound getter at r13-0x6654.
    0x804DF370: 0x906DE2C4,  # Upper bound setter.
    0x8038F9D0: 0x4814F971,  # Game heap captures the SDK upper bound.
    0x805052C4: 0x3C058000,  # Output vector cached -> physical, subtract 0x80000000.
    0x80505318: 0x3C048000,  # Input vector conversion, same mapping.
}


def validate(original: bytes) -> dict:
    if probe.sha256(original) != probe.RETAIL_HASH:
        raise ValueError("MEM2 contract requires the exact supported retail executable")
    header = parse_dol_header(original)
    for address, expected in GUARDS.items():
        if struct.unpack_from(">I", original, header.offset_for_address(address))[0] != expected:
            raise ValueError(f"MEM2 contract instruction mismatch at {address:#x}")
    return {
        "dol_sha256": probe.RETAIL_HASH,
        "guarded_instructions": len(GUARDS),
        "reservation": "dynamic boot arena upper bound minus4096, before OS initialization",
        "payload": "first512 bytes of owned reservation; no fixed MEM2 payload address",
        "physical_conversion": "cached pointer minus0x80000000, inverse plus0x80000000",
        "root_cause_proven": False,
    }


def validate_owned_manifest(manifest: dict) -> None:
    native = manifest.get("lua_location_bridge", {})
    memory = manifest.get("owned_receive_memory")
    if not native.get("owned_receive_mem2") and memory is None:
        return
    base, size = native.get("address"), native.get("size")
    if (
        native.get("owned_receive_mem2") is not True
        or native.get("owned_network_delivery") is not True
        or native.get("receive_audit_read_only", False) is not False
        or not isinstance(memory, dict)
        or memory.get("schema") != 1
        or memory.get("kind") != "checked_boot_mem2_reservation"
        or memory.get("size") != 32
        or memory.get("reserved_bytes") != 4096
        or memory.get("payload_bytes") != 512
        or memory.get("before_os_init") is not True
        or type(memory.get("address")) is not int
        or type(base) is not int
        or type(size) is not int
        or memory["address"] != native.get("symbols", {}).get("udp_mem2_reservation")
        or not base <= memory["address"] <= base + size - 32
    ):
        raise ValueError("Unknown owned MEM2 receive contract")
