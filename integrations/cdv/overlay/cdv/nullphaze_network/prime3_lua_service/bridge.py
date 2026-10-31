# The bridge compiler selects bounded native backends and constructs the matching bootstrap.
# Compile-time diagnostic modes remain explicit; a helper being present does not enable its
# grant or network path. Boundary names here: probe_source, compile_bridge,
# compile_bootstrap, patch_dol, build.
"""Build an isolated, read-only retail Lua location bridge and GXLoader image."""

from __future__ import annotations

import argparse
import base64
import hashlib
import dataclasses
import importlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

if __package__ in {None, ""}:
    _repository_root = os.fspath(Path(__file__).resolve().parents[2])
    if _repository_root not in sys.path:
        sys.path.insert(0, _repository_root)

from retro_data_structures.enums.corruption import State

from randovania.games.prime3.exporter.dol_patcher import (
    append_executable_text_section,
    encode_ppc_unconditional_branch,
    parse_dol_header,
    patch_guarded_instruction_word,
)
from randovania.games.prime3.exporter.runtime_toolchain import resolve_prime3_runtime_toolchain
from nullphaze_network.prime3_lua_service import location, network_save, probe
from nullphaze_network.prime3_lua_service.inventory_profile import RETAIL_HASH

BASE = 0x817E1000
RESERVED_HIGH = 0x817E0000
HOOK = 0x80225998
HOOK_WORD = 0x482287D1
STAGING = 0x806843C0
APPLOADER_HASH = "da82187b082803d6eb8b0dfdcc8f9525ec85e4f8d2ee523d4f6a9bab664ddc53"
MESSAGES = probe.MESSAGES + (
    ("ProbeLocationReady", State.InternalState07, "LOCATION READS PASS"),
    ("ProbeLocationChanged", State.InternalState08, "ROOM CHANGE OBSERVED"),
    ("ProbeLocationUnavailable", State.InternalState09, "LOCATION UNAVAILABLE"),
)


def probe_source() -> str:
    source = probe.probe_source("full")
    changes = {
        "    records = {},": "    records = {},\n    location = {available = false},\n    location_changes = 0,",
        '"ProbeRecovered", "ProbeHeartbeat", "ProbeChanged"}': (
            '"ProbeRecovered", "ProbeHeartbeat", "ProbeChanged", "ProbeLocationReady",\n'
            '        "ProbeLocationChanged", "ProbeLocationUnavailable"}'
        ),
        "local function sample_inventory()": Path(__file__).with_name("location_probe.lua").read_text(encoding="utf-8")
        + "\nlocal function sample_inventory()",
        "return records, changed": "return records, changed, CP3WReadLocationSnapshot()",
        "local ok, records, changed = pcall(sample_inventory)": (
            "local ok, records, changed, location = pcall(sample_inventory)"
        ),
        "    CP3WProbe.records = records": "    CP3WProbe.records = records\n    CP3WPublishLocation(location)",
        "        CP3WProbe.available = false": (
            "        CP3WProbe.available = false\n        CP3WPublishLocation({available = false})"
        ),
    }
    for old, new in changes.items():
        if source.count(old) != 1:
            raise ValueError("Bridge Lua template drift")
        source = source.replace(old, new)
    return source


def _compile_optional_objects(
    run,
    toolchain,
    flags,
    source,
    output,
    grant_probe,
    save_trace,
    network_profile,
    lifecycle,
    coupling=False,
    delivery=False,
    networking=False,
    multiworld_data=None,
    frame_service=False,
):
    objects = []
    sources = []
    if grant_probe:
        sources.append(("grant_probe.c", "grant.o", ()))
    if save_trace:
        defines = ("-DCP3W_NETWORK_SAVE_ADAPTER",) if network_profile is not None else ()
        if lifecycle:
            defines += ("-DCP3W_RECEIPT_LIFECYCLE_TRACE",)
        sources.append(("save_native_trace.c", "save_native_trace.o", defines))
    if network_profile is not None:
        for name in ("network_save_codec.c", "network_save_adapter.c", "network_save_profile.S"):
            defines = (f'-DNETWORK_SAVE_PROFILE_BINARY="{network_profile.resolve().as_posix()}"',)
            sources.append((name, Path(name).stem + ".o", defines))
    if lifecycle:
        sources.append(("receipt_lifecycle.c", "receipt_lifecycle.o", ()))
    if coupling:
        sources.append(("receipt_coupling.c", "receipt_coupling.o", ()))
    if delivery:
        sources.append(("receipt_delivery.c", "receipt_delivery.o", ()))
    if frame_service:
        sources.extend((("frame_poll.c", "frame_poll.o", ()), ("frame_poll.S", "frame_poll_hook.o", ())))
    if multiworld_data is not None:
        sources.append(("multiworld_seed_data.S", "multiworld_seed_data.o",
                        (f'-DMULTIWORLD_SEED_DATA_BINARY="{multiworld_data.resolve().as_posix()}"',)))
    for name, object_name, defines in sources:
        obj = output / object_name
        extra = ("-DCP3W_RECEIPT_COUPLING",) if coupling else ()
        if delivery:
            extra += ("-DCP3W_RECEIPT_DELIVERY",)
        run(toolchain.compiler_path, *flags, *defines, *extra, "-c", source.with_name(name), "-o", obj)
        objects.append(obj)
    if networking:
        module = importlib.import_module("nullphaze_network.prime3_lua_service.network_delivery")
        objects.extend(module.objects(run, toolchain, flags, source, output))
    return objects


def _validate_bridge_options(grant_probe, save_trace, network_profile, receipt_lifecycle, receipt_coupling):
    if receipt_coupling and not receipt_lifecycle:
        raise ValueError("Synthetic receipt coupling requires lifecycle container diagnostics")
    if grant_probe and save_trace:
        raise ValueError("Save diagnostics must not include the grant experiment")
    if receipt_lifecycle and (not save_trace or network_profile is None or grant_probe):
        raise ValueError("Receipt lifecycle diagnostics require grant-free container tracing")
    if network_profile is not None:
        if not save_trace or grant_probe:
            raise ValueError("Networking container experiment requires grant-free save tracing")
        profile = network_profile.read_bytes()
        network_save.validate_profile(profile)
        return profile
    return None


def _coupling_symbols(coupling, delivery):
    if not coupling:
        return set()
    hooks = importlib.import_module("nullphaze_network.prime3_lua_service.receipt_coupling").HOOKS
    symbols = {name for _, _, name in hooks} | {
        "receipt_coupling_state",
        "coupling_loaded",
        "coupling_checkpoint",
        "coupling_before_install",
        "coupling_selected_slot",
        "coupling_source",
        "coupling_begin_construct",
        "coupling_load_begin",
        "coupling_load_end",
        "coupling_stored",
        "coupling_prepare_save",
    }
    if delivery:
        return symbols | {
            "receipt_delivery_state",
            "receipt_delivery_tick",
            "coupling_delivery_view",
            "coupling_delivery_commit",
        }
    return symbols | {"coupling_test_tick"}


def _delivery_metadata(enabled, symbols, source):
    if not enabled:
        return {}
    return {
        "experimental_receipt_delivery": True,
        "delivery_state_address": symbols["receipt_delivery_state"],
        "delivery_state_size": 64,
        "delivery_source_sha256": probe.file_hash(source.with_name("receipt_delivery.c")),
    }


def _bridge_linker(source, grant, trace, profile, coupling, delivery, networking):
    choices = (
        (networking, "network_delivery.ld"),
        (delivery, "receipt_delivery.ld"),
        (coupling, "receipt_coupling.ld"),
        (profile is not None, "network_save_adapter.ld"),
        (trace, "save_native_trace.ld"),
        (grant, "grant_probe.ld"),
        (True, "bridge.ld"),
    )
    return source.with_name(next(name for enabled, name in choices if enabled))


def _network_lua(lua, enabled):
    return lua + (
        "\n-- EXPERIMENTAL CP3W fixed UDP delivery v4: no automatic grant, no durable ACK.\n" if enabled else ""
    )


def _owned_transport_lua(lua, enabled, receive_audit_only=False, receive_audit_prefill=0xA5, receive_audit_mem2=False):
    if not enabled:
        return lua
    lua = importlib.import_module("nullphaze_network.prime3_lua_service.readiness").instrument_lua(lua)
    if receive_audit_only:
        lua += "\n-- RX contract audit v1: cached/uncached snapshots; DELIVER blocked.\n"
        if receive_audit_prefill == 0:
            lua += "-- RX ownership zero-prefill address-matched control; snapshots unchanged.\n"
        if receive_audit_mem2:
            lua += "\n-- Read-only MEM2 receive placement comparison; native DELIVER blocked.\n"
    return importlib.import_module("nullphaze_network.prime3_lua_service.presentation").instrument_lua(lua)


def _patch_sequence_presentation(pak, report, source, enabled):
    if enabled is None:
        return pak
    presentation = importlib.import_module("nullphaze_network.prime3_lua_service.sequence_presentation")
    items = importlib.import_module("nullphaze_network.prime3_lua_service.item_sequence")
    first, pickup_report = presentation.patch_pickups(pak, report, source, items.plan()["steps"])
    if first != presentation.patch_pickups(pak, report, source, items.plan()["steps"])[0]:
        raise ValueError("Sequence pickup presentation is not reproducible")
    report["pickup_presentation"] = pickup_report
    report["output_pak_sha256"] = probe.sha256(first)
    return first


def _patch_owned_presentation(pak, report, source, enabled):
    if not enabled:
        return pak
    presentation = importlib.import_module("nullphaze_network.prime3_lua_service.presentation")
    first, pickup_report = presentation.patch_pickup(pak, report, source)
    if first != presentation.patch_pickup(pak, report, source)[0]:
        raise ValueError("Retail pickup presentation is not reproducible")
    report["pickup_presentation"] = pickup_report
    report["output_pak_sha256"] = probe.sha256(first)
    return first


def _owned_messages(messages, enabled):
    if enabled:
        return messages + importlib.import_module("nullphaze_network.prime3_lua_service.presentation").NETWORK_MESSAGES
    return messages


def _receive_audit_flags(enabled, owned, prefill=0xA5):
    if enabled and not owned:
        raise ValueError("Receive audit requires the owned transport")
    if type(prefill) is not int or prefill not in (0, 0xA5) or (not enabled and prefill != 0xA5):
        raise ValueError("Receive audit prefill requires an explicit audit and byte0 or165")
    return ("-DCP3W_RX_AUDIT", f"-DCP3W_RX_PREFILL={prefill}") if enabled else ()


def _receive_audit_metadata(enabled, prefill=0xA5):
    return {"receive_audit_read_only": True, "receive_audit_prefill": prefill} if enabled else {}


def _receive_mem2_flags(enabled, audit, prefill):
    if type(enabled) is not bool or (enabled and (not audit or prefill != 0)):
        raise ValueError("MEM2 receive requires an explicit zero-prefill read-only audit")
    return ("-DCP3W_RX_MEM2",) if enabled else ()


def _receive_mem2_symbols(enabled):
    return {"udp_mem2_reservation", "udp_reserve_mem2"} if enabled else set()


def _receive_mem2_metadata(enabled):
    return {"receive_audit_mem2": True} if enabled else {}


def _owned_receive_mem2_flags(enabled, owned, audit, receipt, profile):
    if type(enabled) is not bool or (enabled and (not owned or audit or not receipt or profile is None)):
        raise ValueError("Owned MEM2 delivery requires the separate fixed receipt/profile experiment, not an audit")
    return ("-DCP3W_RX_MEM2",) if enabled else ()


def _owned_receive_mem2_metadata(enabled):
    return {"owned_receive_mem2": True} if enabled else {}


def _owned_mem2_manifest(report, native):
    if native.get("owned_receive_mem2"):
        report["owned_receive_memory"] = {
            "schema": 1,
            "kind": "checked_boot_mem2_reservation",
            "address": native["symbols"]["udp_mem2_reservation"],
            "size": 32,
            "reserved_bytes": 4096,
            "payload_bytes": 512,
            "before_os_init": True,
        }


def _owned_mem2_lua(lua, enabled):
    return lua + ("\n-- Fixed disposable CP3W grant with checked MEM2 receive reservation.\n" if enabled else "")


def _receive_audit_manifest(report, native):
    if native.get("receive_audit_read_only"):
        report["receive_audit_probe"] = {
            "schema": 1,
            "address": native["symbols"]["udp_receive_audit"],
            "size": 64,
            "cached_and_uncached": True,
            "delivery_requests_blocked": True,
            "prefill_byte": native["receive_audit_prefill"],
            "callback_snapshot": native["symbols"]["udp_callback_snapshot"],
            "dispatch_snapshot": native["symbols"]["udp_dispatch_snapshot"],
            "snapshot_size": 512,
        }
        report["services"]["grant"] = "disabled_receive_contract_audit"
        if native.get("receive_audit_mem2"):
            report["receive_audit_probe"]["mem2_reservation"] = {
                "address": native["symbols"]["udp_mem2_reservation"],
                "size": 32,
                "reserved_bytes": 4096,
                "payload_bytes": 512,
                "before_os_init": True,
            }
        report["network_save_adapter"]["grants_enabled"] = False
        report["network_save_adapter"]["receipt_advancement_enabled"] = False


def _network_manifest(report, native, metadata, enabled):
    if enabled:
        module = importlib.import_module("nullphaze_network.prime3_lua_service.network_delivery")
        report["network_delivery_probe"] = {
            **module.SPEC,
            "state_address": native["network_delivery_state_address"],
            "poll_hook": metadata["network_poll_hook"],
        }
        report["network_operations"] = "experimental_udp_service"
        report["services"]["network"] = "fixed_receipted_udp_disposable_only"
        if native.get("owned_network_delivery"):
            report["owned_transport_probe"] = {
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
                "state_address": native["symbols"]["owned_cp3w_state"],
                "udp_state_address": native["symbols"]["udp_probe_state"],
            }


def _readiness_compile(output, readiness_only, features, kd_only=False, ip_only=False, udp_only=False):
    if not (readiness_only or kd_only or ip_only or udp_only):
        return None
    if any(features) or sum((readiness_only, kd_only, ip_only, udp_only)) != 1:
        raise ValueError("Readiness diagnostic must not include grants, saves or socket transport")
    return importlib.import_module("nullphaze_network.prime3_lua_service.readiness").compile_native(
        output, kd_only=kd_only, ip_only=ip_only or udp_only, udp_echo=udp_only
    )


def _readiness_manifest(report, native, enabled):
    if enabled:
        report["network_readiness_probe"] = {
            "schema": 1,
            "bootstrap_calls_max": 1,
            "host_queries_max": 120,
            "sockets": False,
            "grants": False,
            "save_hooks": False,
            "state_address": native["symbols"]["readiness_state"],
        }
        report["network_operations"] = "retail_bootstrap_and_host_id_only"
        report["production_grants_enabled"] = False
        if native.get("readiness_backend") in {"kd_only", "owned_ip", "owned_udp_echo"}:
            report["network_readiness_probe"].update(
                backend="kd_only",
                bootstrap_calls_max=0,
                host_queries_max=0,
                kd_open_calls_max=1,
                kd_startup_calls_max=1,
                retained_owned_kd=True,
            )
            report["network_operations"] = "owned_kd_open_and_startup_only"
            if native["readiness_backend"] in {"owned_ip", "owned_udp_echo"}:
                report["network_readiness_probe"].update(
                    backend="owned_ip",
                    ip_open_calls_max=1,
                    host_queries_max=12,
                    host_query_interval_active_samples=10,
                    retained_owned_ip=True,
                )
                report["network_operations"] = "owned_kd_startup_then_owned_ip_host_id_only"
                if native["readiness_backend"] == "owned_udp_echo":
                    report["network_readiness_probe"].update(
                        backend="owned_udp_echo",
                        sockets=True,
                        udp_echo=True,
                        socket_create_max=1,
                        bind_max=1,
                        receive_max=1,
                        send_max=1,
                        port=43674,
                        udp_state_address=native["symbols"]["udp_probe_state"],
                    )
                    report["network_operations"] = "owned_one_shot_udp_echo_only"


def _readiness_lua(lua, enabled, kd_only=False, ip_only=False):
    if ip_only:
        lua += "\n-- Owned IP readiness v2: bounded zero-result polling; no sockets or grants.\n"
    if kd_only:
        lua += "\n-- KD-only owned startup probe v1; no library calls or IP descriptor.\n"
    return (
        importlib.import_module("nullphaze_network.prime3_lua_service.readiness").instrument_lua(lua)
        if enabled or kd_only or ip_only
        else lua
    )


def _readiness_contract(original, enabled, kd_only=False):
    if kd_only:
        importlib.import_module("nullphaze_network.prime3_lua_service.readiness").validate_kd_contract(original)
    elif enabled:
        importlib.import_module("nullphaze_network.prime3_lua_service.readiness").validate_retail_contract(original)


def _validate_delivery_options(network_delivery, receipt_delivery, receipt_coupling, grant_probe):
    if network_delivery and not receipt_delivery:
        raise ValueError("Network delivery requires the fixed receipt experiment")
    if receipt_delivery and (not receipt_coupling or grant_probe):
        raise ValueError("Fixed receipt delivery requires coupled container tracing, not the old grant probe")


def _owned_transport_flags(enabled, networking):
    if enabled and not networking:
        raise ValueError("Owned CP3W transport requires the fixed network delivery experiment")
    return ("-DCP3W_OWNED_CP3W",) if enabled else ()


def _owned_transport_symbols(enabled):
    return (
        {
            "readiness_state",
            "udp_probe_state",
            "owned_cp3w_state",
            "owned_cp3w_diagnostic",
            "bridge_network_status",
            "owned_cp3w_request",
            "udp_probe_tick",
            "readiness_tick",
            "udp_vectors",
            "udp_rx",
            "udp_peer",
            "udp_tx",
            "kd_output",
            "udp_recv_params",
            "udp_send_params",
            "udp_reply_length",
        }
        if enabled
        else set()
    )


def compile_bridge(
    output: Path,
    *,
    grant_probe: bool = False,
    save_trace: bool = False,
    network_profile: Path | None = None,
    receipt_lifecycle: bool = False,
    receipt_coupling: bool = False,
    receipt_delivery: bool = False,
    network_delivery: bool = False,
    owned_network_delivery: bool = False,
    receive_audit_only: bool = False,
    receive_audit_prefill: int = 0xA5,
    receive_audit_mem2: bool = False,
    owned_receive_mem2: bool = False,
    tracker_read_only: bool = False,
    quiet_tracker: bool = False,
    item_sequence_test: Path | None = None,
    multiworld_header: Path | None = None,
    multiworld_data: Path | None = None,
    readiness_only: bool = False,
    kd_readiness_only: bool = False,
    ip_readiness_only: bool = False,
    udp_echo_only: bool = False,
) -> dict:
    if multiworld_data is not None and multiworld_header is None:
        raise ValueError("Seed data requires the multiworld runtime header")
    if multiworld_header is not None and (not all((save_trace, network_profile, receipt_lifecycle,
                                                  receipt_coupling, receipt_delivery, network_delivery,
                                                  owned_network_delivery, owned_receive_mem2))
                                          or any((grant_probe, tracker_read_only, item_sequence_test,
                                                  receive_audit_only, quiet_tracker))):
        raise ValueError("Multiworld requires its own bound, coupled MEM2 delivery runtime")
    tracker = importlib.import_module("nullphaze_network.prime3_lua_service.tracker")
    tracker_flags = tracker.compile_flags(
        tracker_read_only, owned_network_delivery, owned_receive_mem2, receipt_delivery, network_profile
    )
    tracker_flags += importlib.import_module("nullphaze_network.prime3_lua_service.quiet").flags(quiet_tracker, tracker_read_only)
    owned_flags = _owned_transport_flags(owned_network_delivery, network_delivery)
    owned_flags += _receive_audit_flags(receive_audit_only, owned_network_delivery, receive_audit_prefill)
    owned_flags += _receive_mem2_flags(receive_audit_mem2, receive_audit_only, receive_audit_prefill)
    owned_flags += _owned_receive_mem2_flags(
        owned_receive_mem2, owned_network_delivery, receive_audit_only, receipt_delivery, network_profile
    )
    diagnostic = _readiness_compile(
        output,
        readiness_only,
        (
            grant_probe,
            save_trace,
            network_profile,
            receipt_lifecycle,
            receipt_coupling,
            receipt_delivery,
            network_delivery,
        ),
        kd_only=kd_readiness_only,
        ip_only=ip_readiness_only,
        udp_only=udp_echo_only,
    )
    if diagnostic is not None:
        return diagnostic
    _validate_delivery_options(network_delivery, receipt_delivery, receipt_coupling, grant_probe)
    profile = _validate_bridge_options(grant_probe, save_trace, network_profile, receipt_lifecycle, receipt_coupling)
    toolchain = resolve_prime3_runtime_toolchain()
    output.mkdir(parents=True, exist_ok=False)
    sequence_flags = importlib.import_module("nullphaze_network.prime3_lua_service.item_sequence").compile_flags(
        item_sequence_test,
        output,
        owned=owned_network_delivery,
        mem2=owned_receive_mem2,
        receipt=receipt_delivery,
        tracker=tracker_read_only,
    )
    source = Path(__file__).with_name("bridge.c").resolve()
    linker = _bridge_linker(
        source, grant_probe, save_trace, network_profile, receipt_coupling, receipt_delivery, network_delivery
    )
    if multiworld_header is not None:
        linker = source.with_name("multiworld.ld")
    layout = importlib.import_module("nullphaze_network.prime3_lua_service.network_delivery") if network_delivery else None
    base, reserved = (layout.BASE, layout.RESERVED_HIGH) if layout else (BASE, RESERVED_HIGH)

    def run(*args) -> str:
        result = subprocess.run([os.fspath(arg) for arg in args], capture_output=True, text=True, check=False)
        if result.returncode:
            raise RuntimeError(f"Bridge tool failed: {result.stderr or result.stdout}")
        return result.stdout

    obj, elf, binary = (output / name for name in ("bridge.o", "bridge.elf", "bridge.bin"))
    flags = (
        *toolchain.required_machine_flags,
        "-msdata=none",
        "-ffreestanding",
        "-fno-builtin",
        "-fno-pic",
        "-fno-stack-protector",
        "-fno-common",
        "-fno-unwind-tables",
        "-fno-asynchronous-unwind-tables",
        "-ffunction-sections",
        "-fdata-sections",
        "-O2",
        "-Wall",
        "-Wextra",
        "-Werror",
    )
    if network_delivery:
        flags += ("-DCP3W_NETWORK_DELIVERY", f"-DCP3W_MEM1_RESERVED_HIGH={reserved}")
    flags += owned_flags
    flags += tracker_flags
    flags += sequence_flags
    if multiworld_header is not None:
        flags += ("-I", str(source.parent), "-include", str(multiworld_header.resolve()))
    rename = ("-Dbridge_install=bridge_read_only_install",) if grant_probe else ()
    coupling_flags = ("-DCP3W_RECEIPT_COUPLING",) if receipt_coupling else ()
    if receipt_delivery:
        coupling_flags += ("-DCP3W_RECEIPT_DELIVERY",)
    run(toolchain.compiler_path, *flags, *rename, *coupling_flags, "-c", source, "-o", obj)
    objects = [
        obj,
        *_compile_optional_objects(
            run,
            toolchain,
            flags,
            source,
            output,
            grant_probe,
            save_trace,
            network_profile,
            receipt_lifecycle,
            receipt_coupling,
            receipt_delivery,
            network_delivery,
            multiworld_data,
            frame_service=multiworld_header is not None,
        ),
    ]
    run(
        toolchain.linker_path,
        "-EB",
        "--build-id=none",
        "--gc-sections",
        "--no-undefined",
        "-T",
        linker,
        *objects,
        "-o",
        elf,
    )
    run(toolchain.objcopy_path, "-O", "binary", elf, binary)
    header = run(toolchain.readelf_path, "-h", elf)
    if not all(value in header for value in ("ELF32", "big endian", "PowerPC")):
        raise ValueError("Bridge is not ELF32 big-endian PowerPC")
    symbol_text = run(toolchain.readelf_path, "-sW", elf)
    symbols = {}
    wanted_symbols = {"bridge_install", "bridge_read_location", "bridge_boot"}
    if grant_probe:
        wanted_symbols |= {"grant_probe_once", "grant_probe_receipt"}
    if save_trace:
        hooks = importlib.import_module("nullphaze_network.prime3_lua_service.save_native_trace").HOOKS
        wanted_symbols |= {name for _, _, name in hooks} | {"save_trace_data"}
    if network_profile is not None:
        wanted_symbols |= {
            "network_save_read",
            "network_save_read_complete",
            "network_save_write",
            "network_save_state",
        }
    if receipt_lifecycle:
        hooks = importlib.import_module("nullphaze_network.prime3_lua_service.receipt_lifecycle").HOOKS
        wanted_symbols |= {name for _, _, name in hooks}
    wanted_symbols |= _coupling_symbols(receipt_coupling, receipt_delivery)
    if layout:
        wanted_symbols |= layout.SYMBOLS
    wanted_symbols |= _owned_transport_symbols(owned_network_delivery)
    if receive_audit_only:
        wanted_symbols.add("udp_receive_audit")
        wanted_symbols.update(("udp_callback_snapshot", "udp_dispatch_snapshot"))
    wanted_symbols |= _receive_mem2_symbols(receive_audit_mem2 or owned_receive_mem2)
    wanted_symbols = tracker.symbols(wanted_symbols, tracker_read_only)
    wanted_symbols |= importlib.import_module("nullphaze_network.prime3_lua_service.item_sequence").symbols(item_sequence_test)
    if multiworld_header is not None:
        wanted_symbols |= importlib.import_module("nullphaze_network.prime3_lua_service.frame_poll").SYMBOLS
        wanted_symbols |= {"bridge_tracker_snapshot", "bridge_area_matches", "mw_collect_location",
                           "coupling_saved_cursor", "owned_cp3w_claim_connection_notice"}
    if multiworld_data is not None:
        wanted_symbols |= {"mw_seed_data", "network_save_profile"}
    for line in symbol_text.splitlines():
        fields = line.split()
        if len(fields) == 8 and fields[6] == "UND":
            raise ValueError("Bridge has undefined symbols")
        if len(fields) == 8 and fields[-1] in wanted_symbols:
            symbols[fields[-1]] = int(fields[1], 16)
    if set(symbols) != wanted_symbols:
        raise ValueError(f"Missing bridge entry symbols: {sorted(wanted_symbols - set(symbols))}")
    size = binary.stat().st_size
    limit = 0x3E000 if layout else (0x1E000 if network_profile is not None else 0xE000)
    if not 0 < size < limit or any(not base <= value < base + size for value in symbols.values()):
        raise ValueError("Bridge code outside reserved range")
    if re.search(r"\bR_PPC_", run(toolchain.readelf_path, "-rW", elf)):
        raise ValueError("Bridge has unresolved relocations")
    (output / "bridge.disassembly.txt").write_text(run(toolchain.objdump_path, "-dr", elf), encoding="utf-8")
    result = {
        "schema": 1,
        "address": base,
        "size": size,
        "symbols": symbols,
        "reserved_high": reserved,
        "source_sha256": probe.file_hash(source),
        "linker_sha256": probe.file_hash(linker),
        "binary_sha256": probe.file_hash(binary),
        "elf_sha256": probe.file_hash(elf),
        "compiler": toolchain.compiler_version,
        "binutils": toolchain.binutils_version,
        "devkitppc": toolchain.devkitppc_release,
        "target": toolchain.target_triple,
    }
    if multiworld_header is not None:
        result["multiworld"] = {"schema": 1, "seed_header_sha256": probe.file_hash(multiworld_header),
                                "save_format": "NPMWSV01", "wire_bytes": 65868,
                                "status_command": 10, "delivery_command": 11,
                                "native_saved_ack": "validated_disk_read_only"}
        result["multiworld"]["save_filename"] = base64.b32encode(
            hashlib.sha256(multiworld_header.read_bytes()).digest()
        ).decode("ascii")[:8]
    if multiworld_header is not None:
        result["network_frame_service"] = importlib.import_module(
            "nullphaze_network.prime3_lua_service.frame_poll").CONTRACT
    if multiworld_data is not None:
        result["multiworld"]["patchable_seed_data"] = {
            "address": symbols["mw_seed_data"], "size": multiworld_data.stat().st_size,
            "sha256": probe.file_hash(multiworld_data),
            "checkpoint_address": symbols["network_save_profile"], "checkpoint_size": 80,
        }
    result.update(_receive_audit_metadata(receive_audit_only, receive_audit_prefill))
    result.update(_receive_mem2_metadata(receive_audit_mem2))
    result.update(_owned_receive_mem2_metadata(owned_receive_mem2))
    result.update(tracker.native_metadata(tracker_read_only, source))
    result.update(importlib.import_module("nullphaze_network.prime3_lua_service.item_sequence").metadata(item_sequence_test))
    result.update(importlib.import_module("nullphaze_network.prime3_lua_service.quiet").metadata(quiet_tracker))
    if grant_probe:
        immutable_size = symbols["grant_probe_receipt"] - BASE
        result.update(
            grant_probe_source_sha256=probe.file_hash(source.with_name("grant_probe.c")),
            immutable_size=immutable_size,
            immutable_sha256=probe.sha256(binary.read_bytes()[:immutable_size]),
            mutable_receipt_address=symbols["grant_probe_receipt"],
            mutable_receipt_size=32,
            experimental_grant_probe=True,
        )
    if save_trace:
        immutable_size = symbols["save_trace_data"] - base
        result.update(
            save_trace_source_sha256=probe.file_hash(source.with_name("save_native_trace.c")),
            immutable_size=immutable_size,
            immutable_sha256=probe.sha256(binary.read_bytes()[:immutable_size]),
            mutable_trace_address=symbols["save_trace_data"],
            mutable_trace_size=8224,
            experimental_save_trace=True,
        )
    if network_profile is not None:
        result.update(
            experimental_network_save_adapter=True,
            network_profile_hex=profile.hex(),
            network_profile_sha256=probe.sha256(profile),
            network_adapter_address=symbols["network_save_state"],
            network_adapter_size=66144 if multiworld_header is not None else 66016,
            network_adapter_sources={
                name: probe.file_hash(source.with_name(name))
                for name in ("network_save_codec.c", "network_save_adapter.c", "network_save_profile.S")
            },
        )
    if receipt_lifecycle:
        result.update(
            experimental_receipt_lifecycle=True,
            receipt_lifecycle_source_sha256=probe.file_hash(source.with_name("receipt_lifecycle.c")),
        )
    if receipt_coupling:
        result.update(
            experimental_receipt_coupling=True,
            coupling_state_address=symbols["receipt_coupling_state"],
            coupling_state_size=5724 if multiworld_header is not None else 4500,
            coupling_source_sha256=probe.file_hash(source.with_name("receipt_coupling.c")),
        )
    result.update(_delivery_metadata(receipt_delivery, symbols, source))
    if layout:
        result.update(
            experimental_network_delivery=True,
            owned_network_delivery=owned_network_delivery,
            network_delivery_state_address=symbols["network_delivery_state"],
            network_delivery_state_size=64,
            network_sources={
                **{
                    name: probe.file_hash(source.with_name(name))
                    for name in (
                        "network_delivery.c",
                        "network_transport.c",
                        *(("readiness.c", "udp_echo.c") if owned_network_delivery else ()),
                    )
                },
                **{
                    f"../prime3_wii_runtime/{name}": probe.file_hash(source.parent.parent / "prime3_wii_runtime" / name)
                    for name in ("relocated_runtime.c", "relocated_runtime.S")
                },
            },
        )
    (output / "bridge.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


def compile_bootstrap(output: Path, native: Path, metadata: dict) -> tuple[bytes, dict]:
    if metadata["address"] % 32 or metadata["size"] % 32:
        raise ValueError("Relocation cache range must be cache-line aligned")
    toolchain = resolve_prime3_runtime_toolchain()
    output.mkdir(parents=True, exist_ok=False)
    source_root = Path(__file__).resolve().parent
    shared_source = source_root.parent / "prime3_wii_runtime/payload.S"
    linker = source_root / "bootstrap.ld"
    base, reserved = metadata["address"], metadata["reserved_high"]
    defines = {
        "PRIME3_RUNTIME_RELOCATED_MODE": 1,
        "PRIME3_BOOTSTRAP_RESERVED_HIGH": reserved,
        "PRIME3_BOOTSTRAP_DIAGNOSTIC_ADDRESS": reserved,
        "PRIME3_RELOCATED_RUNTIME_DESTINATION_ADDRESS": base,
        "PRIME3_RELOCATED_RUNTIME_ENTRY_ADDRESS": metadata["symbols"]["bridge_boot"],
        "PRIME3_RELOCATED_CACHE_RANGE_START": base,
        "PRIME3_RELOCATED_CACHE_RANGE_END": base + metadata["size"],
        "PRIME3_RUNTIME_CACHE_LINE_SIZE": 32,
        "PRIME3_RUNTIME_COPY_COMPLETE_MARKER_ADDRESS": reserved + 0x2C,
        "PRIME3_RUNTIME_COPY_COMPLETE_MARKER_VALUE": 0x4C554143,
        "PRIME3_RUNTIME_BOOTSTRAP_RETURN_MARKER_ADDRESS": reserved + 0x30,
        "PRIME3_RUNTIME_BOOTSTRAP_RETURN_MARKER_VALUE": 0x4C554152,
        "PRIME3_BOOTSTRAP_STATUS_VALUE": 1,
    }
    commands = [
        [
            toolchain.compiler_path,
            *toolchain.required_machine_flags,
            *(f"-D{key}={value}" for key, value in defines.items()),
            "-c",
            shared_source,
            "-o",
            output / "bootstrap.o",
        ],
        [
            toolchain.compiler_path,
            *toolchain.required_machine_flags,
            '-DBRIDGE_BINARY="' + (native / "bridge.bin").resolve().as_posix() + '"',
            "-c",
            source_root / "bridge_blob.S",
            "-o",
            output / "blob.o",
        ],
        [
            toolchain.linker_path,
            "-EB",
            "--build-id=none",
            "--no-undefined",
            "-T",
            linker,
            output / "bootstrap.o",
            output / "blob.o",
            "-o",
            output / "payload.elf",
        ],
        [toolchain.objcopy_path, "-O", "binary", output / "payload.elf", output / "payload.bin"],
    ]
    for command in commands:
        completed = subprocess.run([os.fspath(arg) for arg in command], check=False, capture_output=True, text=True)
        if completed.returncode:
            raise RuntimeError("Bootstrap tool failed: " + completed.stderr)
    payload = (output / "payload.bin").read_bytes()
    binary = (native / "bridge.bin").read_bytes()
    if payload.count(binary) != 1 or STAGING + len(payload) >= 0x81100000:
        raise ValueError("Relocation bootstrap does not contain exactly the bounded bridge")
    result = {
        "bootstrap_mode": "read_only_bridge_relocated_continue",
        "bootstrap_address": STAGING,
        "bootstrap_size": len(payload),
        "bootstrap_sha256": probe.sha256(payload),
        "bootstrap_elf_sha256": probe.file_hash(output / "payload.elf"),
        "shared_source_sha256": probe.file_hash(shared_source),
        "linker_sha256": probe.file_hash(linker),
        "blob_source_sha256": probe.file_hash(source_root / "bridge_blob.S"),
        "reserved_high": reserved,
        "runtime_destination": base,
        "cache_range_start": base,
        "cache_range_size": len(binary),
        "copy_marker_address": reserved + 0x2C,
        "return_marker_address": reserved + 0x30,
        "original_branch_target": 0x8000648C,
        "original_continuation_address": 0x80006324,
    }
    (output / "payload.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return payload, result


def patch_dol(original: bytes, native: Path, bootstrap: Path, *, bootstrap_template=None) -> tuple[bytes, dict]:
    # Explicit imports keep every export-time guard in frozen clients. Build-only
    # helpers elsewhere in this module can remain lazily loaded.
    from nullphaze_network.prime3_lua_service import (
        mem2_contract, network_delivery, receipt_coupling, receipt_lifecycle,
        save_native_trace, readiness as readiness_module,
    )
    if probe.sha256(original) != RETAIL_HASH:
        raise ValueError("Bridge requires the exact supported original DOL")
    metadata = json.loads((native / "bridge.json").read_text(encoding="utf-8"))
    if metadata.get("receive_audit_mem2") or metadata.get("owned_receive_mem2"):
        mem2_contract.validate(original)
    binary = (native / "bridge.bin").read_bytes()
    network = metadata.get("experimental_network_delivery") is True
    readiness = metadata.get("experimental_network_readiness") is True
    _readiness_contract(
        original, readiness, metadata.get("readiness_backend") in {"kd_only", "owned_ip", "owned_udp_echo"}
    )
    layout = (readiness_module if readiness else network_delivery) if network or readiness else None
    base, reserved = (layout.BASE, layout.RESERVED_HIGH) if layout else (BASE, RESERVED_HIGH)
    if (
        metadata["address"] != base
        or metadata["reserved_high"] != reserved
        or (probe.sha256(binary) != metadata["binary_sha256"] or len(binary) != metadata["size"])
    ):
        raise ValueError("Bridge artifact mismatch")
    if bootstrap_template is None:
        payload, boot = compile_bootstrap(bootstrap, native, metadata)
    else:
        from nullphaze_network.prime3_lua_service.runtime_assets import bind_bootstrap
        payload, boot = bind_bootstrap(bootstrap_template, binary, metadata)
    result, section = append_executable_text_section(
        original,
        payload_bytes=payload,
        payload_virtual_address=STAGING,
        required_alignment=32,
        entry_symbol_offset=0,
    )
    result, _ = patch_guarded_instruction_word(
        result,
        address=0x80006320,
        expected_original_word=0x4800016D,
        replacement_word=encode_ppc_unconditional_branch(0x80006320, STAGING, link=True),
    )
    result, hook = patch_guarded_instruction_word(
        result,
        address=HOOK,
        expected_original_word=HOOK_WORD,
        replacement_word=encode_ppc_unconditional_branch(HOOK, metadata["symbols"]["bridge_install"], link=True),
    )
    if network:
        result, poll_hook = patch_guarded_instruction_word(
            result,
            address=0x800BB71C,
            expected_original_word=0x80630024,
            replacement_word=encode_ppc_unconditional_branch(
                0x800BB71C, metadata["symbols"]["runtime_poll_hook_wrapper"]
            ),
        )
    frame_hook = None
    if metadata.get("multiworld"):
        frame_module = importlib.import_module("nullphaze_network.prime3_lua_service.frame_poll")
        if metadata.get("network_frame_service") != frame_module.CONTRACT:
            raise ValueError("Multiworld runtime requires an independent native network pump")
        result, frame_hook = frame_module.patch(original, result, metadata["symbols"])
    trace_hooks = []
    if metadata.get("experimental_save_trace"):
        hooks = save_native_trace.HOOKS
        for address, target, symbol in hooks:
            result, changed = patch_guarded_instruction_word(
                result,
                address=address,
                expected_original_word=encode_ppc_unconditional_branch(address, target, link=True),
                replacement_word=encode_ppc_unconditional_branch(address, metadata["symbols"][symbol], link=True),
            )
            trace_hooks.append(dataclasses.asdict(changed))
    adapter_hooks = []
    filename_patch = None
    save_filename = metadata.get("multiworld", {}).get("save_filename", "cp3w.bin")
    if len(save_filename) != 8 or not save_filename.isascii() or not all(c.isalnum() or c == "." for c in save_filename):
        raise ValueError("Invalid private save filename")
    save_name_bytes = save_filename.encode("ascii") + b"\0"
    if metadata.get("experimental_network_save_adapter"):
        extra_hooks = (
            (0x801D68E8, 0x803FA414, "network_save_read"),
            (0x801D5FAC, 0x801D606C, "network_save_read_complete"),
        )
        if metadata.get("experimental_receipt_lifecycle"):
            extra_hooks += receipt_lifecycle.HOOKS
        if metadata.get("experimental_receipt_coupling"):
            extra_hooks += receipt_coupling.HOOKS
        for address, target, symbol in extra_hooks:
            result, changed = patch_guarded_instruction_word(
                result,
                address=address,
                expected_original_word=encode_ppc_unconditional_branch(address, target, link=True),
                replacement_word=encode_ppc_unconditional_branch(address, metadata["symbols"][symbol], link=True),
            )
            adapter_hooks.append(dataclasses.asdict(changed))
        offset = parse_dol_header(original).offset_for_address(0x8057D898)
        if original[offset : offset + 9] != b"save.bin\0":
            raise ValueError("Private networking filename guard failed")
        result = result[:offset] + save_name_bytes + result[offset + 9 :]
        filename_patch = offset
    # Original bytes outside explicitly guarded instructions and filename stay intact.
    header = parse_dol_header(original)
    permitted = {header.offset_for_address(address) for address in (0x80006320, HOOK)}
    if network:
        permitted.add(header.offset_for_address(0x800BB71C))
    if frame_hook is not None:
        permitted.add(header.offset_for_address(frame_hook.address))
    permitted |= {header.offset_for_address(changed["address"]) for changed in trace_hooks}
    permitted |= {header.offset_for_address(changed["address"]) for changed in adapter_hooks}
    for original_section in header.sections:
        start, size = original_section.file_offset, original_section.size
        expected = bytearray(original[start : start + size])
        for offset in permitted:
            if start <= offset < start + size:
                expected[offset - start : offset - start + 4] = result[offset : offset + 4]
        if filename_patch is not None and start <= filename_patch < start + size:
            expected[filename_patch - start : filename_patch - start + 9] = save_name_bytes
        if result[start : start + size] != expected:
            raise ValueError("Unrelated retail DOL section changed")
    updated = parse_dol_header(result)
    if any(section.size and section.end_address > 0x81200000 for section in updated.sections):
        raise ValueError("DOL section exceeds the retail apploader production boundary")
    if (header.bss_address, header.bss_size, header.entry_point) != (
        updated.bss_address,
        updated.bss_size,
        updated.entry_point,
    ):
        raise ValueError("Retail BSS or entrypoint changed")
    report = {
        **metadata,
        "hook": dataclasses.asdict(hook),
        "section": dataclasses.asdict(section),
        "bootstrap": boot,
        "patched_dol_sha256": probe.sha256(result),
        "network_operations": "experimental_udp_service" if network else 0,
        "grant": "disposable_save_test_only"
        if metadata.get("experimental_grant_probe") or metadata.get("experimental_receipt_delivery")
        else "disabled",
    }
    if trace_hooks:
        report["save_trace_hooks"] = trace_hooks
    if adapter_hooks:
        report["network_save_hooks"] = adapter_hooks
        report["network_save_filename"] = save_filename
    if network:
        report["network_poll_hook"] = dataclasses.asdict(poll_hook)
    if frame_hook is not None:
        report["network_frame_hook"] = dataclasses.asdict(frame_hook)
    return result, report


def build(
    source: Path,
    output: Path,
    wit: Path,
    *,
    grant_probe: bool = False,
    save_trace: bool = False,
    network_profile: Path | None = None,
    receipt_lifecycle: bool = False,
    receipt_coupling: bool = False,
    receipt_delivery: bool = False,
    network_delivery: bool = False,
    owned_network_delivery: bool = False,
    receive_audit_only: bool = False,
    receive_audit_prefill: int = 0xA5,
    receive_audit_mem2: bool = False,
    owned_receive_mem2: bool = False,
    tracker_read_only: bool = False,
    quiet_tracker: bool = False,
    item_sequence_test: Path | None = None,
    readiness_only: bool = False,
    kd_readiness_only: bool = False,
    ip_readiness_only: bool = False,
    udp_echo_only: bool = False,
) -> dict:
    if grant_probe and save_trace:
        raise ValueError("Save diagnostics must not include the grant experiment")
    source, output, wit = (path.resolve() for path in (source, output, wit))
    if output.exists() or source == output or source in output.parents or output in source.parents:
        raise ValueError("Use a new output tree disjoint from original media")
    original = (source / "sys/main.dol").read_bytes()
    _readiness_contract(original, readiness_only, kd_readiness_only or ip_readiness_only or udp_echo_only)
    profile = location.extract_profile(original, (source / "files/Worlds.pak").read_bytes())
    if probe.file_hash(source / "files/UniverseArea.pak") != probe.RETAIL_UNIVERSE_HASH:
        raise ValueError("Original UniverseArea.pak mismatch")
    if probe.file_hash(source / "sys/apploader.img") != APPLOADER_HASH:
        raise ValueError("Original retail apploader mismatch")
    output.mkdir(parents=True)
    native = compile_bridge(
        output / "native",
        grant_probe=grant_probe,
        save_trace=save_trace,
        network_profile=network_profile,
        receipt_lifecycle=receipt_lifecycle,
        receipt_coupling=receipt_coupling,
        receipt_delivery=receipt_delivery,
        network_delivery=network_delivery,
        owned_network_delivery=owned_network_delivery,
        receive_audit_only=receive_audit_only,
        receive_audit_prefill=receive_audit_prefill,
        receive_audit_mem2=receive_audit_mem2,
        owned_receive_mem2=owned_receive_mem2,
        tracker_read_only=tracker_read_only,
        quiet_tracker=quiet_tracker,
        item_sequence_test=item_sequence_test,
        readiness_only=readiness_only,
        kd_readiness_only=kd_readiness_only,
        ip_readiness_only=ip_readiness_only,
        udp_echo_only=udp_echo_only,
    )
    repeated = compile_bridge(
        output / "native-repeat",
        grant_probe=grant_probe,
        save_trace=save_trace,
        network_profile=network_profile,
        receipt_lifecycle=receipt_lifecycle,
        receipt_coupling=receipt_coupling,
        receipt_delivery=receipt_delivery,
        network_delivery=network_delivery,
        owned_network_delivery=owned_network_delivery,
        receive_audit_only=receive_audit_only,
        receive_audit_prefill=receive_audit_prefill,
        receive_audit_mem2=receive_audit_mem2,
        owned_receive_mem2=owned_receive_mem2,
        tracker_read_only=tracker_read_only,
        quiet_tracker=quiet_tracker,
        item_sequence_test=item_sequence_test,
        readiness_only=readiness_only,
        kd_readiness_only=kd_readiness_only,
        ip_readiness_only=ip_readiness_only,
        udp_echo_only=udp_echo_only,
    )
    if native != repeated:
        raise ValueError("Native bridge is not reproducible")
    patched_dol, bridge = patch_dol(original, output / "native", output / "bootstrap")
    repeated_dol, repeated_bridge = patch_dol(original, output / "native-repeat", output / "bootstrap-repeat")
    if patched_dol != repeated_dol or bridge != repeated_bridge:
        raise ValueError("Patched DOL is not reproducible")
    diagnostic_dol = output / "patched.dol"
    diagnostic_dol.write_bytes(patched_dol)
    recognized = subprocess.run(
        [os.fspath(wit), "FILETYPE", os.fspath(diagnostic_dol)], check=True, capture_output=True, text=True
    )
    (output / "dol-filetype.txt").write_text(recognized.stdout + recognized.stderr, encoding="utf-8")
    if not re.search(r"^DOL\s", recognized.stdout, re.MULTILINE):
        raise ValueError("WIT does not recognize the patched executable as DOL")
    variant = importlib.import_module("nullphaze_network.prime3_lua_service.grant_probe") if grant_probe else None
    lua = variant.probe_source() if variant is not None else probe_source()
    if save_trace:
        lua += "\n-- CP3W native save-event diagnostic v1; no grants or save-format changes.\n"
    if network_profile is not None:
        lua += "\n-- CP3W experimental migrated networking container v1; grants disabled.\n"
    if receipt_lifecycle:
        lua += "\n-- CP3W checkpoint ownership and SHA256 lifecycle diagnostic v1; no receipt advancement.\n"
    if receipt_coupling:
        old = "    local was_available = CP3WProbe.available"
        if lua.count(old) != 1:
            raise ValueError("Receipt tick Lua template drift")
        lua = lua.replace(old, "    CP3WReceiptProbeTick()\n" + old)
        lua += "\n-- SYNTHETIC RECEIPTS ONLY v4: complete slot lifetimes; no guessed save receipts or GRANTS.\n"
    if receipt_delivery:
        lua = lua.replace(
            "-- SYNTHETIC RECEIPTS ONLY v4: complete slot lifetimes; no guessed save receipts or GRANTS.",
            "-- FIXED RECEIPTED MISSILE DELIVERY v1: disposable save, no network input.",
        )
    lua = _network_lua(lua, network_delivery)
    lua = importlib.import_module("nullphaze_network.prime3_lua_service.tracker").instrument_lua(lua, tracker_read_only)
    lua = _owned_transport_lua(
        lua, owned_network_delivery, receive_audit_only, receive_audit_prefill, receive_audit_mem2
    )
    lua = _owned_mem2_lua(lua, owned_receive_mem2)
    lua = _readiness_lua(lua, readiness_only, kd_readiness_only, ip_readiness_only or udp_echo_only)
    messages = variant.MESSAGES if variant is not None else MESSAGES
    messages = _owned_messages(messages, owned_network_delivery)
    lua, messages = importlib.import_module("nullphaze_network.prime3_lua_service.quiet").presentation(
        lua, messages, native["binary_sha256"], quiet_tracker
    )
    original_pak = (source / "files/UniverseArea.pak").read_bytes()
    lua, messages = importlib.import_module("nullphaze_network.prime3_lua_service.item_sequence").presentation(
        lua, messages, item_sequence_test, native["binary_sha256"]
    )
    labels = not (quiet_tracker or item_sequence_test is not None)
    pak, report = probe.patch_pak(original_pak, lua, messages=messages, diagnostic_labels=labels)
    if pak != probe.patch_pak(original_pak, lua, messages=messages, diagnostic_labels=labels)[0]:
        raise ValueError("Bridge PAK is not reproducible")
    pak = _patch_owned_presentation(pak, report, source, owned_network_delivery and item_sequence_test is None)
    pak = _patch_sequence_presentation(pak, report, source, item_sequence_test)
    image_root = output / "image"
    base = probe.build(source, image_root, None, inventory_scope="full")
    copied = image_root / "DATA"
    (copied / "sys/main.dol").write_bytes(patched_dol)
    (copied / "files/UniverseArea.pak").write_bytes(pak)
    report.update(
        files=base["files"],
        inventory_profile=base["inventory_profile"],
        location_profile=profile,
        lua_location_bridge=bridge,
        dol_sha256=probe.sha256(patched_dol),
        original_dol_sha256=RETAIL_HASH,
        deterministic_pak=True,
        deterministic_bridge=True,
        deterministic_dol=True,
    )
    report["services"]["location"] = "native_lua_read_only_probe"
    _readiness_manifest(report, native, readiness_only or kd_readiness_only or ip_readiness_only or udp_echo_only)
    if variant is not None:
        report["services"]["grant"] = "disposable_save_one_shot_MissileExpansion_only"
        report["inventory_write_probe"] = variant.PROFILE
        report["production_grants_enabled"] = False
    if save_trace:
        report["native_save_trace"] = {
            "schema": 1,
            "address": bridge["mutable_trace_address"],
            "size": bridge["mutable_trace_size"],
            "hooks": bridge["save_trace_hooks"],
            "changes_save_format": False,
        }
        report["services"]["grant"] = "disabled"
        report["services"]["save_trace"] = "diagnostic_pass_through_only"
        report["production_grants_enabled"] = False
    if network_profile is not None:
        report["native_save_trace"]["changes_save_format"] = True
        report["services"]["save_trace"] = "experimental_container_preserve_receipts_only"
        report["network_save_adapter"] = {
            "experimental": True,
            "filename": "cp3w.bin",
            "wire_size": 65796,
            "profile_hex": native["network_profile_hex"],
            "hooks": bridge["network_save_hooks"],
            "grants_enabled": False,
            "receipt_advancement_enabled": False,
        }
    if receipt_lifecycle:
        report["receipt_lifecycle_trace"] = {"schema": 1, "receipt_advancement_enabled": False, "grants_enabled": False}
    if receipt_coupling:
        report["receipt_coupling_probe"] = {
            "schema": 1,
            "synthetic_receipts_only": True,
            "inventory_writes": False,
            "state_address": native["coupling_state_address"],
            "state_size": native["coupling_state_size"],
            "cursors": [0x101, 0x202, 0x303],
            "production_receipt_advancement": False,
        }
        report["services"]["save_trace"] = "synthetic_receipt_checkpoint_coupling"
    if receipt_delivery:
        delivery = importlib.import_module("nullphaze_network.prime3_lua_service.receipt_delivery")
        report["receipt_delivery_probe"] = delivery.spec(native)
        report["receipt_coupling_probe"].update(synthetic_receipts_only=False, inventory_writes=True, cursors=[0, 1])
        report["services"]["grant"] = "fixed_receipted_disposable_missile_only"
        report["services"]["save_trace"] = "fixed_receipt_delivery_checkpoint_coupling"
        report["network_save_adapter"].update(grants_enabled=True, receipt_advancement_enabled=True)
        report["receipt_lifecycle_trace"].update(grants_enabled=True, receipt_advancement_enabled=True)
    _network_manifest(report, native, bridge, network_delivery)
    _receive_audit_manifest(report, native)
    _owned_mem2_manifest(report, native)
    importlib.import_module("nullphaze_network.prime3_lua_service.tracker").configure_manifest(report, tracker_read_only)
    importlib.import_module("nullphaze_network.prime3_lua_service.quiet").configure_manifest(report, quiet_tracker)
    importlib.import_module("nullphaze_network.prime3_lua_service.item_sequence").configure_manifest(report, item_sequence_test)
    for relative, expected in base["files"].items():
        wanted = {"sys/main.dol": report["dol_sha256"], "files/UniverseArea.pak": report["output_pak_sha256"]}.get(
            relative, expected
        )
        if probe.file_hash(copied / relative) != wanted or probe.file_hash(source / relative) != expected:
            raise ValueError(f"Original/copy verification failed: {relative}")
    report["extraction_verified"] = True
    image = image_root / probe.DISC_IMAGE_NAME
    for command, arguments in (
        ("COPY", ["-B", "-z", "--trunc", os.fspath(copied), os.fspath(image)]),
        ("VERIFY", [os.fspath(image)]),
    ):
        completed = subprocess.run([os.fspath(wit), command, *arguments], check=False, capture_output=True, text=True)
        (output / f"wit-{command.lower()}.txt").write_text(completed.stdout + completed.stderr, encoding="utf-8")
        if completed.returncode or "!!" in completed.stderr:
            raise ValueError(f"WIT {command} failed; see the preserved build log")
    report["image"] = {**probe.image_manifest(image), "wit_verified": True}
    report["disc_roundtrip"] = verify_roundtrip(image, output / "roundtrip", wit, report)
    (image_root / "build.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def verify_roundtrip(image: Path, output: Path, wit: Path, report: dict) -> dict:
    if output.exists():
        raise ValueError("Disc roundtrip output must be a new directory")
    completed = subprocess.run(
        [os.fspath(wit), "EXTRACT", "--psel", "DATA", os.fspath(image), os.fspath(output)],
        check=False,
        capture_output=True,
        text=True,
    )
    (output.parent / "wit-extract.txt").write_text(completed.stdout + completed.stderr, encoding="utf-8")
    if completed.returncode or "!!" in completed.stderr:
        raise ValueError("Final disc extraction failed")
    return verify_extracted(output, image.parent / "DATA", report)


def verify_extracted(output: Path, copied: Path, report: dict) -> dict:
    candidates = list(output.rglob("main.dol"))
    if len(candidates) != 1 or candidates[0].parent.name != "sys":
        raise ValueError("Final disc does not have one main executable")
    extracted = candidates[0].parent.parent
    regenerated = {}
    for relative, original_hash in report["files"].items():
        expected = {"sys/main.dol": report["dol_sha256"], "files/UniverseArea.pak": report["output_pak_sha256"]}.get(
            relative, original_hash
        )
        actual = probe.file_hash(extracted / relative)
        if actual != expected:
            original = (copied / relative).read_bytes()
            if probe.sha256(original) != expected:
                raise ValueError("Copied metadata no longer matches the input manifest")
            verify_container_metadata(relative, original, (extracted / relative).read_bytes())
            regenerated[relative] = {"input_sha256": expected, "repacked_sha256": actual}
    return {
        "passed": True,
        "exact_files_verified": len(report["files"]) - len(regenerated),
        "patched_dol_verified": True,
        "repacked_container_metadata": regenerated,
        "container_integrity": "WIT VERIFY required separately; game files compared byte-for-byte",
    }


def verify_container_metadata(relative: str, original: bytes, repacked: bytes) -> None:
    # WIT rebuilds filesystem offsets, partition hashes and fake signatures.
    # These are container metadata, not permission to change game resources.
    ranges = {
        "sys/boot.bin": ((0x420, 0x430),),
        "ticket.bin": ((4, 0x104), (0x248, 0x250)),
        "tmd.bin": ((4, 0x104), (0x19A, 0x19C), (0x1F4, 0x208)),
        "disc/region.bin": ((0x10, 0x20),),
    }
    if relative in {"sys/fst.bin", "h3.bin"}:
        if not original or not repacked:
            raise ValueError("Empty regenerated filesystem/hash metadata")
        return
    if relative not in ranges or len(original) != len(repacked):
        raise ValueError(f"Final disc content mismatch: {relative}")
    if relative == "disc/region.bin" and repacked[0x10:0x20] != bytes(16):
        raise ValueError("Unexpected region rating normalization")
    for offset, (before, after) in enumerate(zip(original, repacked, strict=True)):
        if before != after and not any(start <= offset < end for start, end in ranges[relative]):
            raise ValueError(f"Unexpected container metadata change: {relative}+{offset:x}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-data", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--wit", type=Path, required=True)
    parser.add_argument("--save-trace", action="store_true", help="Enable bounded native save diagnostics, no grants")
    parser.add_argument(
        "--kd-readiness-only", action="store_true", help="Owned KD open/startup only; no IP service or sockets"
    )
    parser.add_argument(
        "--ip-readiness-only", action="store_true", help="Owned KD startup then owned IP host-ID query; no sockets"
    )
    parser.add_argument("--udp-echo-only", action="store_true", help="One owned UDP socket and one echo; no grants")
    parser.add_argument(
        "--network-readiness-only",
        action="store_true",
        help="One retail bootstrap, host-ID telemetry; no sockets or grants",
    )
    parser.add_argument(
        "--experimental-network-profile", type=Path, help="Explicit bound profile; requires --save-trace"
    )
    parser.add_argument("--receipt-lifecycle-trace", action="store_true", help="Fingerprint native checkpoint handoffs")
    parser.add_argument(
        "--receipt-coupling-probe", action="store_true", help="Synthetic receipts only; grants disabled"
    )
    parser.add_argument(
        "--fixed-receipt-delivery-test", action="store_true", help="Disposable fixed missile grant; no networking"
    )
    parser.add_argument(
        "--network-delivery-test", action="store_true", help="Opt-in typed UDP fixed delivery; disposable save only"
    )
    args = parser.parse_args()
    result = build(
        args.source_data,
        args.output,
        args.wit,
        save_trace=args.save_trace,
        network_profile=args.experimental_network_profile,
        receipt_lifecycle=args.receipt_lifecycle_trace,
        receipt_coupling=args.receipt_coupling_probe,
        receipt_delivery=args.fixed_receipt_delivery_test,
        network_delivery=args.network_delivery_test,
        readiness_only=args.network_readiness_only,
        kd_readiness_only=args.kd_readiness_only,
        ip_readiness_only=args.ip_readiness_only,
        udp_echo_only=args.udp_echo_only,
    )
    print(
        f"Built Lua bridge {result['probe_id']}; grant service: {result['services']['grant']}; live acceptance pending."
    )


if __name__ == "__main__":
    main()
