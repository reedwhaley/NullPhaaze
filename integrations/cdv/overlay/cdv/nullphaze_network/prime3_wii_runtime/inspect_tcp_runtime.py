# Inspect the explicitly supplied runtime/DOL and canonical asset directory. This legacy TCP
# inspection path is separate from the current CP3W UDP delivery session. Boundary names
# here: inspect_tcp_runtime, main.
from __future__ import annotations

import argparse
import json
import os
import sys
from ipaddress import IPv4Address
from pathlib import Path

if __package__ in (None, ""):
    repository_root = Path(__file__).resolve().parents[2]
    repository_root_text = os.fspath(repository_root)
    if repository_root_text not in sys.path:
        sys.path.insert(0, repository_root_text)

import randovania
from randovania.games.prime3.exporter.hardware_runtime import (
    Prime3DolPatchError,
    load_validated_production_runtime_assets,
    patch_cp3w_tcp_endpoint,
    verify_prime3_tcp_runtime_dol,
)
from randovania.games.prime3.exporter.runtime_payload import Prime3RuntimeTransportMetadata


def _resolve_dol_path(input_path: Path) -> Path:
    if input_path.is_file() and input_path.name.lower() == "main.dol":
        return input_path
    if input_path.is_dir():
        for relative_path in (Path("DATA/sys/main.dol"), Path("sys/main.dol")):
            candidate = input_path.joinpath(relative_path)
            if candidate.is_file():
                return candidate
    raise ValueError("Input must be an extracted main.dol or an export staging directory containing DATA/sys/main.dol.")


def _canonical_asset_directory() -> Path:
    return randovania.get_data_path().parents[1].joinpath("build", "prime3_wii_runtime", "production")


def inspect_tcp_runtime(dol_path: Path, asset_directory: Path) -> dict[str, object]:
    assets = load_validated_production_runtime_assets(asset_directory, require_elf=False)
    relocated = assets.manifest.relocated_runtime
    assert relocated is not None
    transport = relocated.transport
    if not isinstance(transport, Prime3RuntimeTransportMetadata):
        raise Prime3DolPatchError("Production manifest does not contain TCP/CP3C metadata.")

    dol = dol_path.read_bytes()
    endpoint_offset = relocated.embedded_runtime_blob_offset + transport.server_ipv4_offset
    payload_prefix = assets.payload[:endpoint_offset]
    occurrences: list[int] = []
    search_offset = 0
    while (offset := dol.find(payload_prefix, search_offset)) >= 0:
        occurrences.append(offset)
        search_offset = offset + 1
    if len(occurrences) != 1:
        raise Prime3DolPatchError(f"Expected one canonical TCP payload prefix in {dol_path}, found {len(occurrences)}.")
    payload_offset = occurrences[0]
    actual_ipv4_offset = payload_offset + endpoint_offset
    actual_ipv4 = IPv4Address(dol[actual_ipv4_offset : actual_ipv4_offset + transport.server_ipv4_size])
    payload, manifest = patch_cp3w_tcp_endpoint(assets.payload, assets.manifest, actual_ipv4)
    verification = verify_prime3_tcp_runtime_dol(
        dol,
        payload=payload,
        manifest=manifest,
        cp3w_server_ipv4=actual_ipv4,
        dol_path=dol_path,
    )
    return {
        "dol_path": os.fspath(dol_path),
        "runtime_present": True,
        "payload_sha256": verification.payload_sha256,
        "runtime_section_address": f"0x{verification.runtime_section_address:08X}",
        "entry_hook_word": f"0x{verification.entry_hook_word:08X}",
        "recurring_hook_word": f"0x{verification.recurring_hook_word:08X}",
        "cp3c_config_offset": f"0x{verification.cp3c_config_offset:X}",
        "cp3c_config_address": f"0x{verification.cp3c_config_address:08X}",
        "server": f"{verification.server_ipv4}:{verification.server_port}",
        "server_ipv4_bytes": verification.server_ipv4_bytes.hex(" "),
        "server_port_bytes": verification.server_port_bytes.hex(" "),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect the final CP3C TCP runtime in an extracted Prime 3 DOL.")
    parser.add_argument("input_path", type=Path, help="main.dol or an export staging directory")
    parser.add_argument("--runtime-assets", type=Path, default=_canonical_asset_directory())
    args = parser.parse_args()
    dol_path = _resolve_dol_path(args.input_path)
    try:
        report = inspect_tcp_runtime(dol_path, args.runtime_assets)
    except Prime3DolPatchError as exception:
        report = {
            "dol_path": os.fspath(dol_path),
            "runtime_present": False,
            "error": str(exception),
        }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
