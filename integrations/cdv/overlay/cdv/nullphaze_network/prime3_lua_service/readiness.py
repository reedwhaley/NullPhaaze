# Build a socket-free hardware readiness diagnostic, never a delivery runtime. Boundary
# names here: inspect_retail_contract, validate_retail_contract, instrument_lua,
# validate_kd_contract, compile_native.
"""Build a socket-free hardware readiness diagnostic, never a delivery runtime."""

from __future__ import annotations

import ipaddress
import json
import os
import re
import struct
import subprocess
from pathlib import Path

from randovania.games.prime3.exporter.dol_patcher import parse_dol_header
from randovania.games.prime3.exporter.runtime_toolchain import resolve_prime3_runtime_toolchain
from nullphaze_network.prime3_lua_service import probe
from nullphaze_network.prime3_lua_service.inventory_profile import RETAIL_HASH
from nullphaze_network.prime3_wii_runtime.analyze_ios_wrappers import (
    PRIME3_NTSC_RETAIL_WRAPPER_SPECS,
    validate_function_fingerprints,
)

BASE = 0x817C1000
RESERVED_HIGH = 0x817C0000
SYMBOLS = {
    "bridge_install",
    "bridge_boot",
    "bridge_read_location",
    "readiness_tick",
    "readiness_state",
    "readiness_draw",
}


def inspect_retail_contract(original: bytes) -> dict:
    """Attribute the inherited constants against the exact executable, not IOS stubs."""
    if probe.sha256(original) != RETAIL_HASH:
        raise ValueError("Readiness contract requires the supported retail DOL")
    header = parse_dol_header(original)

    def word(address):
        return struct.unpack_from(">I", original, header.offset_for_address(address))[0]

    def text(address):
        start = header.offset_for_address(address)
        return original[start : start + 32].split(b"\0", 1)[0].decode("ascii")

    # Exact PPC: addi r3,r13,-0x6538; bl IOS_Open. The descriptor writer
    # follows a different path: addi r4,r13,-0x65a0, IOS_Open, stw r3,-0x65a8(r13).
    guards = {
        0x80508E5C: 0x386D9AC8,
        0x80508E64: 0x4BFFB91D,
        0x805006FC: 0x388D9A60,
        0x80500714: 0x906D9A58,
    }
    for address, expected in guards.items():
        if word(address) != expected:
            raise ValueError(f"Retail contract instruction mismatch at {address:#x}")
    sda = 0x806801C0
    bootstrap_path = text(sda - 0x6538)
    descriptor_path = text(sda - 0x65A0)
    return {
        "dol_sha256": RETAIL_HASH,
        "claimed_bootstrap_address": 0x80508DD4,
        "observed_bootstrap_device": bootstrap_path,
        "claimed_so_sda_offset": -26024,
        "descriptor_writer_address": 0x80500714,
        "observed_descriptor_device": descriptor_path,
        "valid_network_contract": False,
        "reason": "Inherited bootstrap and descriptor constants are ES and filesystem, not IP services",
    }


def validate_retail_contract(original: bytes) -> None:
    result = inspect_retail_contract(original)
    raise ValueError(
        "WITHDRAWN readiness image: inherited bootstrap opens "
        f"{result['observed_bootstrap_device']}; descriptor belongs to "
        f"{result['observed_descriptor_device']}. No verified retail IP lifecycle is available."
    )


def instrument_lua(source: str) -> str:
    native_hash = probe.file_hash(Path(__file__).with_suffix(".c"))
    return (
        source
        + f"\n-- Hardware readiness native SHA256 {native_hash}\n"
        + Path(__file__).with_suffix(".lua").read_text(encoding="utf-8")
    )


def validate_kd_contract(original: bytes) -> None:
    if probe.sha256(original) != RETAIL_HASH:
        raise ValueError("KD diagnostic requires the exact supported retail DOL")
    # Verify complete wrapper instruction fingerprints, not guessed role names.
    validate_function_fingerprints(original, PRIME3_NTSC_RETAIL_WRAPPER_SPECS)
    if b"/dev/net/kd/request\0" not in original:
        raise ValueError("Retail KD device identity missing")


def _transmit_destination(host, nonce, dwell, nonblock):
    if (host is None) != (nonce is None):
        raise ValueError("UDP transmit control requires host and nonce together")
    if host is None:
        return None
    if not dwell or nonblock:
        raise ValueError("UDP transmit control requires timed blocking diagnostic")
    address = ipaddress.IPv4Address(host)
    if address.is_unspecified or address.is_multicast or int(address) == 0xFFFFFFFF:
        raise ValueError("UDP transmit control requires a unicast destination")
    if not isinstance(nonce, bytes) or len(nonce) != 16:
        raise ValueError("UDP transmit control requires a 16-byte nonce")
    return address


def _peer_length_flags(enabled, dwell, nonblock, tx_host):
    if not enabled:
        return ()
    if not dwell or nonblock or tx_host is not None:
        raise ValueError("UDP peer-length comparison requires timed blocking receive only")
    return ("-DCP3W_UDP_PEER_LENGTH",)


def compile_native(
    output: Path,
    *,
    kd_only: bool = False,
    ip_only: bool = False,
    udp_echo: bool = False,
    udp_startup: bool = False,
    udp_dwell: bool = False,
    udp_nonblock: bool = False,
    udp_tx_host: str | None = None,
    udp_tx_nonce: bytes | None = None,
    udp_peer_length: bool = False,
    udp_rearm: bool = False,
) -> dict:
    if kd_only and ip_only:
        raise ValueError("Select one readiness backend")
    if udp_echo and not ip_only:
        raise ValueError("UDP echo requires owned IP readiness")
    if udp_startup and not udp_echo:
        raise ValueError("UDP startup diagnostic requires UDP echo")
    if udp_dwell and not udp_startup:
        raise ValueError("UDP dwell diagnostic requires explicit startup")
    if udp_nonblock and not udp_dwell:
        raise ValueError("UDP nonblocking comparison requires timed diagnostic")
    address = _transmit_destination(udp_tx_host, udp_tx_nonce, udp_dwell, udp_nonblock)
    peer_flags = _peer_length_flags(udp_peer_length, udp_dwell, udp_nonblock, udp_tx_host)
    if udp_rearm and not udp_peer_length:
        raise ValueError("UDP rearm diagnostic requires the verified peer-length control")
    toolchain = resolve_prime3_runtime_toolchain()
    output.mkdir(parents=True, exist_ok=False)
    root = Path(__file__).resolve().parent

    def run(*args):
        result = subprocess.run([os.fspath(a) for a in args], capture_output=True, text=True, check=False)
        if result.returncode:
            raise RuntimeError(result.stderr or result.stdout)
        return result.stdout

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
        "-DCP3W_NETWORK_READINESS",
        f"-DCP3W_MEM1_RESERVED_HIGH={RESERVED_HIGH}",
        *peer_flags,
        *(("-DCP3W_UDP_REARM",) if udp_rearm else ()),
    )
    if kd_only or ip_only:
        flags += ("-DCP3W_KD_READINESS",)
    if ip_only:
        flags += ("-DCP3W_IP_READINESS",)
    if udp_echo:
        flags += ("-DCP3W_UDP_ECHO",)
    if udp_startup:
        flags += ("-DCP3W_UDP_STARTUP",)
    if udp_dwell:
        flags += ("-DCP3W_UDP_DWELL",)
    if udp_nonblock:
        flags += ("-DCP3W_UDP_NONBLOCK",)
    if udp_tx_host is not None:
        flags += ("-DCP3W_UDP_TX_ONLY", f"-DCP3W_UDP_TX_HOST={int(address)}u")
        flags += tuple(
            f"-DCP3W_UDP_TX_NONCE_{index}={word}u" for index, word in enumerate(struct.unpack(">4I", udp_tx_nonce))
        )
    sources = ("bridge", "readiness", "udp_echo") if udp_echo else ("bridge", "readiness")
    for source in sources:
        run(toolchain.compiler_path, *flags, "-c", root / f"{source}.c", "-o", output / f"{source}.o")
    elf, binary = output / "bridge.elf", output / "bridge.bin"
    run(
        toolchain.linker_path,
        "-EB",
        "--build-id=none",
        "--gc-sections",
        "--no-undefined",
        "-T",
        root / "readiness.ld",
        *(output / f"{source}.o" for source in sources),
        "-o",
        elf,
    )
    run(toolchain.objcopy_path, "-O", "binary", elf, binary)
    header = run(toolchain.readelf_path, "-h", elf)
    if not all(value in header for value in ("ELF32", "big endian", "PowerPC")):
        raise ValueError("Invalid readiness ELF")
    symbols = {}
    wanted = SYMBOLS | ({"kd_output"} if kd_only or ip_only else set())
    if udp_echo:
        wanted |= {
            "udp_probe_state",
            "udp_probe_tick",
            "udp_create",
            "udp_bind",
            "udp_recv_params",
            "udp_send_params",
            "udp_vectors",
            "udp_rx",
            "udp_peer",
        }
    for line in run(toolchain.readelf_path, "-sW", elf).splitlines():
        fields = line.split()
        if len(fields) == 8 and fields[6] == "UND":
            raise ValueError("Undefined readiness symbol")
        if len(fields) == 8 and fields[-1] in wanted:
            symbols[fields[-1]] = int(fields[1], 16)
    if set(symbols) != wanted or re.search(r"\bR_PPC_", run(toolchain.readelf_path, "-rW", elf)):
        raise ValueError("Invalid readiness symbols/relocations")
    size = binary.stat().st_size
    if not 0 < size < 0xE000 or size % 32 or any(not BASE <= a < BASE + size for a in symbols.values()):
        raise ValueError("Readiness layout or cache alignment mismatch")
    (output / "bridge.disassembly.txt").write_text(run(toolchain.objdump_path, "-dr", elf), encoding="utf-8")
    result = {
        "schema": 1,
        "address": BASE,
        "reserved_high": RESERVED_HIGH,
        "size": size,
        "symbols": symbols,
        "experimental_network_readiness": True,
        "udp_startup_diagnostic": udp_startup,
        "udp_dwell_halfsecond_ticks": 60 if udp_dwell else 0,
        "udp_nonblocking_receive": udp_nonblock,
        "udp_peer_address_length": 8 if udp_peer_length else 0,
        "udp_echo_limit": 32 if udp_rearm else 1,
        "udp_transmit_control": None
        if udp_tx_host is None
        else {"host": str(address), "port": 43675, "nonce_hex": udp_tx_nonce.hex(), "receive_calls_max": 0},
        "readiness_backend": "owned_udp_echo"
        if udp_echo
        else "owned_ip"
        if ip_only
        else "kd_only"
        if kd_only
        else "withdrawn_legacy",
        "source_sha256": probe.file_hash(root / "bridge.c"),
        "readiness_sources": {
            name: probe.file_hash(root / name)
            for name in (
                "readiness.c",
                "readiness.ld",
                "readiness.lua",
                "readiness.py",
                *(("udp_echo.c",) if udp_echo else ()),
            )
        },
        "linker_sha256": probe.file_hash(root / "readiness.ld"),
        "binary_sha256": probe.file_hash(binary),
        "elf_sha256": probe.file_hash(elf),
        "compiler": toolchain.compiler_version,
        "binutils": toolchain.binutils_version,
        "devkitppc": toolchain.devkitppc_release,
        "target": toolchain.target_triple,
    }
    (output / "bridge.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result
