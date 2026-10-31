# Fail-closed manifest guard for the separate read-only CDV experiment. Boundary names here:
# compile_flags, native_metadata, configure_manifest, instrument_lua, symbols.
"""Fail-closed manifest guard for the separate read-only CDV experiment."""

import hashlib

from nullphaze_network.prime3_lua_service import mem2_contract, network_save

SPEC = {
    "schema": 1,
    "command": 9,
    "capability": 1 << 14,
    "snapshot_bytes": 600,
    "page_bytes": 300,
    "datagrams_max": 4096,
    "bound_profile": True,
    "connection_reset_rearms_max": 8,
    "startup_trigger": "save_lua",
    "initial_delay_ticks": 1,
    "udp_dwell_ticks": 0,
}


def compile_flags(enabled, owned, mem2, receipt, profile):
    if type(enabled) is not bool or (enabled and not (owned and mem2 and receipt and profile is not None)):
        raise ValueError("Tracker requires explicit owned MEM2 transport and bound checkpoint profile")
    return ("-DCP3W_TRACKER_READ_ONLY",) if enabled else ()


def native_metadata(enabled, source):
    if not enabled:
        return {}

    return {
        "tracker_read_only": True,
        "tracker_source_sha256": hashlib.sha256(source.with_name("tracker_transport.c").read_bytes()).hexdigest(),
    }


def configure_manifest(report, enabled):
    if not enabled:
        return
    report["tracker_read_only"] = dict(SPEC)
    report["services"]["grant"] = "disabled_read_only_tracker"
    report["network_save_adapter"].update(grants_enabled=False, receipt_advancement_enabled=False)
    report["receipt_lifecycle_trace"].update(grants_enabled=False, receipt_advancement_enabled=False)
    report["receipt_coupling_probe"]["inventory_writes"] = False


def instrument_lua(lua, enabled):
    marker = "\n-- CP3W read-only CDV tracker v3: save-level startup without diagnostic holds; no grants.\n"
    return lua + (marker if enabled else "")


def symbols(wanted, enabled):
    if enabled:
        return (
            wanted
            - {
                "network_delivery_request",
                "network_delivery_allow",
                "coupling_delivery_view",
                "coupling_delivery_commit",
            }
        ) | {"bridge_tracker_snapshot", "udp_tracker_reset_state", "owned_cp3w_reset_session"}
    return wanted


def validate_manifest(manifest):
    if "tracker_read_only" not in manifest:
        return False
    native = manifest.get("lua_location_bridge", {})
    if native.get("quiet_tracker") or "presentation" in manifest:
        from nullphaze_network.prime3_lua_service.quiet import SPEC as quiet_spec  # noqa: PLC0415

        if native.get("quiet_tracker") is not True or manifest.get("presentation") != quiet_spec:
            raise ValueError("Unknown quiet tracker presentation")
    adapter = manifest.get("network_save_adapter", {})
    if (
        manifest["tracker_read_only"] != SPEC
        or native.get("tracker_read_only") is not True
        or manifest.get("services", {}).get("grant") != "disabled_read_only_tracker"
        or manifest.get("production_grants_enabled") is not False
        or adapter.get("grants_enabled") is not False
        or adapter.get("receipt_advancement_enabled") is not False
        or manifest.get("receipt_coupling_probe", {}).get("inventory_writes") is not False
        or any(k in native.get("symbols", {}) for k in ("network_delivery_request", "coupling_delivery_commit"))
    ):
        raise ValueError("Unsupported read-only tracker manifest")
    network_save.validate_profile(bytes.fromhex(adapter["profile_hex"]))
    mem2_contract.validate_owned_manifest(manifest)
    return True
