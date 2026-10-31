# Fail-closed launcher recognition for the separate read-only receive audit. Boundary names
# here: validate_manifest.
"""Fail-closed launcher recognition for the separate read-only receive audit."""

from nullphaze_network.prime3_lua_service import network_save


def validate_manifest(manifest: dict) -> bool:
    audit = manifest.get("receive_audit_probe")
    native = manifest.get("lua_location_bridge", {})
    if audit is None:
        if native.get("receive_audit_read_only"):
            raise ValueError("Receive audit is missing its explicit read-only manifest")
        return False
    adapter = manifest.get("network_save_adapter", {})
    address = audit.get("address")
    base, size = native.get("address"), native.get("size")
    if (
        native.get("receive_audit_read_only") is not True
        or native.get("owned_network_delivery") is not True
        or native.get("experimental_network_delivery") is not True
        or audit.get("schema") != 1
        or audit.get("size") != 64
        or audit.get("cached_and_uncached") is not True
        or audit.get("delivery_requests_blocked") is not True
        or manifest.get("production_grants_enabled") is not False
        or manifest.get("services", {}).get("grant") != "disabled_receive_contract_audit"
        or adapter.get("filename") != "cp3w.bin"
        or adapter.get("grants_enabled") is not False
        or adapter.get("receipt_advancement_enabled") is not False
        or type(address) is not int
        or type(base) is not int
        or type(size) is not int
    ):
        raise ValueError("Unsupported read-only receive audit")
    if address != native.get("symbols", {}).get("udp_receive_audit") or not base <= address <= base + size - 64:
        raise ValueError("Receive audit state is outside its native image")
    reservation = audit.get("mem2_reservation")
    if native.get("receive_audit_mem2") or reservation is not None:
        if (
            native.get("receive_audit_mem2") is not True
            or audit.get("prefill_byte") != 0
            or not isinstance(reservation, dict)
            or reservation.get("size") != 32
            or reservation.get("reserved_bytes") != 4096
            or reservation.get("payload_bytes") != 512
            or reservation.get("before_os_init") is not True
            or type(reservation.get("address")) is not int
            or reservation["address"] != native.get("symbols", {}).get("udp_mem2_reservation")
            or not base <= reservation["address"] <= base + size - 32
        ):
            raise ValueError("Unsupported MEM2 receive reservation manifest")
    network_save.validate_profile(bytes.fromhex(adapter["profile_hex"]))
    return True
