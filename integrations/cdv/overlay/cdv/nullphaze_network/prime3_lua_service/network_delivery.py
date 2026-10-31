# Opt-in fixed UDP delivery experiment; no durable ACK or general item service. Boundary
# names here: Result, State, request, response, validate_extension.
"""Opt-in fixed UDP delivery experiment; no durable ACK or general item service."""

from __future__ import annotations

import dataclasses
import enum
import importlib
import struct
from pathlib import Path

from nullphaze_network.prime3_lua_service import network_save, receipt_delivery

BASE = 0x817C1000
RESERVED_HIGH = 0x817C0000
CAPABILITY = 1 << 13
RUNTIME_MODE = 19
STATE_COMMAND = 7
DELIVER_COMMAND = 8
HEADER = struct.Struct(">BBBB7I")
SPEC = {
    "schema": 1,
    "kind": "fixed_receipted_udp_disposable_v1",
    "port": 43674,
    "runtime_mode": RUNTIME_MODE,
    "capability": CAPABILITY,
    "commands": [7, 8],
    "queue_size": 64,
    "automatic_grant": False,
    "durable_ack": False,
    "production": False,
}
SYMBOLS = {
    "network_delivery_state",
    "network_delivery_request",
    "network_delivery_allow",
    "network_delivery_cancel",
    "runtime_poll_hook_wrapper",
    "runtime_network_diagnostics_block",
    "runtime_transport_phase",
    "runtime_poll_counter",
    "runtime_transport_cp3w_session_id",
    "runtime_transport_cp3w_negotiated_flag",
    "runtime_transport_cp3w_accepted_capabilities",
    "runtime_transport_cp3w_last_request_id",
    "runtime_transport_receive_payload_buffer",
    "runtime_transport_send_payload_bytes",
    "runtime_transport_prepared_send_length",
    "cp3w_network_dispatch",
    "runtime_poll_entry_impl",
    "runtime_transport_socket_request",
    "runtime_transport_bind_params",
    "runtime_transport_ip_fd",
    "runtime_transport_socket_fd",
    "runtime_transport_service_started",
    "runtime_transport_socket_fd_owned",
    "runtime_transport_socket_ready",
    "runtime_transport_get_host_id_submit_count",
    "runtime_transport_get_host_id_callback_count",
    "runtime_transport_host_id_available",
    "runtime_transport_host_id_ready",
    "runtime_transport_kd_closed",
}


class Result(enum.IntEnum):
    UNAVAILABLE = 0
    READY = 1
    QUEUED = 2
    APPLIED_VOLATILE = 3
    DUPLICATE = 4


@dataclasses.dataclass(frozen=True)
class State:
    result: Result
    session: int
    generation: int
    cursor: int
    pending: int
    attempts: int
    applied: int
    duplicates: int
    history: bytes


def request(session: int, profile: bytes, *, deliver: bool = False) -> bytes:
    network_save.validate_profile(profile)
    if type(session) is not int or not 0 <= session <= 0xFFFFFFFF:
        raise ValueError("Invalid network session")
    payload = struct.pack(">I", session) + profile
    if deliver:
        payload += struct.pack(">6I", 0, 1, 4, 5, 5, 1) + receipt_delivery.history(profile)
    return payload


def response(raw: bytes, session: int, profile: bytes) -> State:
    network_save.validate_profile(profile)
    if len(raw) != 144 or raw[64:] != profile:
        raise ValueError("Network state dimensions/profile mismatch")
    schema, result, slot, flags, *values = HEADER.unpack_from(raw)
    if schema != 1 or slot or flags or values[0] != session or values[3] not in {0, 1}:
        raise ValueError("Network state schema/session/flags mismatch")
    state = State(Result(result), *values, raw[32:64])
    if state.result == Result.UNAVAILABLE:
        if state.generation or state.cursor != 0xFFFFFFFF or state.pending or state.history != bytes(32):
            raise ValueError("Unavailable state retains stale receipt data")
    elif not state.generation:
        raise ValueError("Available state lacks a lifetime")
    elif state.result in {Result.READY, Result.QUEUED}:
        if state.cursor or state.history != bytes(32) or state.pending != (state.result == Result.QUEUED):
            raise ValueError("Pending state differs from receipt0")
    elif state.cursor != 1 or state.history != receipt_delivery.history(profile) or state.pending:
        raise ValueError("Applied state differs from fixed receipt1")
    if state.attempts != state.applied:
        raise ValueError("Partial or conflicting mutation counters")
    return state


def validate_extension(manifest):
    importlib.import_module("nullphaze_network.prime3_lua_service.mem2_contract").validate_owned_manifest(manifest)
    spec = manifest.get("network_delivery_probe", {})
    native = manifest.get("lua_location_bridge", {})
    if (
        any(spec.get(k) != v for k, v in SPEC.items())
        or native.get("address") != BASE
        or native.get("reserved_high") != RESERVED_HIGH
        or native.get("experimental_network_delivery") is not True
        or spec.get("state_address") != native.get("network_delivery_state_address")
        or native.get("network_delivery_state_size") != 64
        or spec.get("poll_hook") != native.get("network_poll_hook")
        or spec.get("poll_hook", {}).get("address") != 0x800BB71C
    ):
        raise ValueError("Unknown network delivery experiment/layout")
    owned = manifest.get("owned_transport_probe")
    if native.get("owned_network_delivery"):
        expected = {
            "schema": 1,
            "kind": "owned_cp3w_fixed_grant_v1",
            "frame_limit": 256,
            "packet_capacity": 512,
            "peer_capacity": 8,
            "receive_flags": 0,
            "startup_limit": 1,
            "socket_limit": 1,
            "legacy_ios_poll_disabled": True,
            "requires_session_ping_and_ready": True,
        }
        if not isinstance(owned, dict) or any(owned.get(key) != value for key, value in expected.items()):
            raise ValueError("Unknown owned CP3W transport contract")
        for key, symbol in (("state_address", "owned_cp3w_state"), ("udp_state_address", "udp_probe_state")):
            if owned.get(key) != native.get("symbols", {}).get(symbol):
                raise ValueError("Owned CP3W state address mismatch")
    elif owned is not None:
        raise ValueError("Owned CP3W manifest lacks opt-in native implementation")


def compiler_defines():
    rb = importlib.import_module("nullphaze_network.prime3_wii_runtime.build_payload")

    values = {
        "PRIME3_RUNTIME_EXECUTED_MARKER_VALUE": rb.RELOCATED_EXECUTED_MARKER_VALUE,
        "PRIME3_RUNTIME_SUCCESS_STATUS_VALUE": rb.RELOCATED_SUCCESS_STATUS_VALUE,
        "PRIME3_RUNTIME_POLL_HOOK_CONTINUATION_ADDRESS": rb.RUNTIME_POLL_HOOK_CONTINUATION_ADDRESS,
        "PRIME3_ENABLE_RECURRING_HOOK_DIAGNOSTICS": 1,
        "PRIME3_ENABLE_IOS_UDP_DIAGNOSTIC": 1,
        "PRIME3_IOS_UDP_DIAGNOSTIC_MODE": RUNTIME_MODE,
        "PRIME3_IOS_UDP_DIAGNOSTIC_LOOP_COUNT": 0,
        "PRIME3_NATIVE_BEACON_IPV4": 0,
        "PRIME3_NATIVE_BEACON_PORT": 43674,
        "PRIME3_CP3W_INVENTORY_COMMAND": 6,
        "PRIME3_CP3W_INVENTORY_CAPABILITY": 1 << 12,
        "PRIME3_CP3W_INVENTORY_SCHEMA_VERSION": rb.INVENTORY_SCHEMA_VERSION,
        "PRIME3_CP3W_INVENTORY_RECORD_COUNT": rb.INVENTORY_RECORD_COUNT,
        "PRIME3_CP3W_INVENTORY_RECORD_SIZE": rb.INVENTORY_RECORD_SIZE,
        "PRIME3_CP3W_INVENTORY_PAYLOAD_SIZE": rb.INVENTORY_PAYLOAD_SIZE,
    }
    for short, attr in {
        "OPEN_ASYNC": "IOS_OPEN_ASYNC",
        "CLOSE_ASYNC": "IOS_CLOSE_ASYNC",
        "READ_ASYNC": "IOS_READ_ASYNC",
        "WRITE_ASYNC": "IOS_WRITE_ASYNC",
        "IOCTL_ASYNC": "CONFIRMED_IOS_IOCTL_ASYNC",
        "IOCTLV_ASYNC": "CONFIRMED_IOS_IOCTLV_ASYNC",
        "IOCTLV_SYNC": "CONFIRMED_IOS_IOCTLV_SYNC",
    }.items():
        name = "PRIME3_RETAIL_IOS_" + short
        values[name + "_ADDRESS"] = getattr(rb, "PRIME3_NTSC_" + attr + "_ADDRESS")
    values.update(
        PRIME3_RETAIL_NWC24_OPEN_LIB_ADDRESS=rb.PRIME3_NTSC_NWC24_OPEN_LIB_ADDRESS,
        PRIME3_RETAIL_NETWORK_BOOTSTRAP_ADDRESS=rb.PRIME3_NTSC_NETWORK_BOOTSTRAP_ADDRESS,
        PRIME3_RETAIL_SO_FD_SDA_OFFSET=rb.PRIME3_NTSC_SO_FD_SDA_OFFSET,
    )
    return tuple(f"-D{k}={v}" for k, v in values.items())


def objects(run, toolchain, flags, source, output):
    defines = compiler_defines()
    paths = []
    for name in ("network_delivery.c", "network_transport.c"):
        obj = output / (Path(name).stem + ".o")
        options = (
            flags
            if name == "network_delivery.c"
            else tuple(f for f in flags if f not in {"-Wall", "-Wextra", "-Werror"})
        )
        run(toolchain.compiler_path, *options, *defines, "-c", source.with_name(name), "-o", obj)
        paths.append(obj)
    if "-DCP3W_OWNED_CP3W" in flags:
        for name in ("readiness", "udp_echo"):
            obj = output / f"{name}.o"
            run(
                toolchain.compiler_path,
                *flags,
                "-DCP3W_NETWORK_READINESS",
                "-DCP3W_KD_READINESS",
                "-DCP3W_IP_READINESS",
                "-DCP3W_UDP_ECHO",
                "-DCP3W_UDP_STARTUP",
                "-DCP3W_UDP_DWELL",
                "-DCP3W_UDP_PEER_LENGTH",
                "-c",
                source.with_name(f"{name}.c"),
                "-o",
                obj,
            )
            paths.append(obj)
    obj = output / "network_runtime_asm.o"
    run(
        toolchain.compiler_path,
        *flags,
        *defines,
        "-c",
        source.parent.parent / "prime3_wii_runtime/relocated_runtime.S",
        "-o",
        obj,
    )
    return [*paths, obj]
