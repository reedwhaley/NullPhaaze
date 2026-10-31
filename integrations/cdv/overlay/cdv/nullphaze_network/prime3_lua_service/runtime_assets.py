# Template receipts bind every native source hash and output payload. At seed export, change
# only the declared seed/profile data regions and retain the accepted runtime instructions.
# Boundary names here: source_hashes, sha, default_directory, load, bind_seed.
"""GPL runtime templates: compile once, bind only verified seed data at export."""
from __future__ import annotations

import base64
import copy
import hashlib
import json
from pathlib import Path

from nullphaze_network.prime3_lua_service import seed_data

ASSET_NAMES = ("bridge.bin", "bridge.json", "payload.bin", "payload.json")


def source_hashes():
    """Build provenance for the complete authored native source, not game data."""
    root = Path(__file__).resolve().parents[1]
    suffixes = {'.c', '.h', '.S', '.s', '.ld', '.inc'}
    return {path.relative_to(root).as_posix(): sha(path.read_bytes())
            for directory in ('prime3_lua_service', 'prime3_wii_runtime')
            for path in sorted((root / directory).rglob('*'))
            if path.is_file() and path.suffix in suffixes}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def default_directory():
    return Path(__file__).resolve().parents[1] / "data/prime3_multiworld"


def load(directory=None):
    root = Path(directory) if directory is not None else default_directory()
    receipt = json.loads((root / "assets.json").read_text())
    if receipt.get("schema") != 1 or set(receipt.get("files", {})) != set(ASSET_NAMES):
        raise ValueError("Unknown Corruption multiworld runtime asset manifest")
    files = {name: (root / name).read_bytes() for name in ASSET_NAMES}
    if any(sha(data) != receipt["files"][name] for name, data in files.items()):
        raise ValueError("Corruption multiworld runtime asset hash mismatch")
    native = json.loads(files["bridge.json"])
    if "owned_cp3w_claim_connection_notice" not in native.get("symbols", {}):
        raise ValueError("Corruption runtime lacks multiworld connection notices; rebuild runtime assets")
    from nullphaze_network.prime3_lua_service import frame_poll

    if (native.get("network_frame_service") != frame_poll.CONTRACT
            or not frame_poll.SYMBOLS <= native.get("symbols", {}).keys()):
        raise ValueError("Corruption runtime lacks independent native networking; rebuild runtime assets")
    boot = json.loads(files["payload.json"])
    binary, payload = files["bridge.bin"], files["payload.bin"]
    data = native["multiworld"]["patchable_seed_data"]
    if (native["address"] != 0x817c1000 or native["reserved_high"] != 0x817c0000
            or native["size"] != len(binary) or native["binary_sha256"] != sha(binary)
            or data["size"] != seed_data.SIZE or data["checkpoint_size"] != 80
            or boot["bootstrap_address"] != 0x806843c0 or boot["bootstrap_sha256"] != sha(payload)
            or boot["cache_range_start"] != native["address"] or boot["cache_range_size"] != len(binary)
            or payload.count(binary) != 1):
        raise ValueError("Corruption multiworld runtime template layout differs")
    ranges = [(data["address"] - native["address"], seed_data.SIZE),
              (data["checkpoint_address"] - native["address"], 80)]
    if any(start < 0 or start + size > len(binary) for start, size in ranges):
        raise ValueError("Corruption multiworld template data lies outside its runtime")
    if max(ranges[0][0], ranges[1][0]) < min(*(start + size for start, size in ranges)):
        raise ValueError("Corruption multiworld template data ranges overlap")
    start = ranges[0][0]
    if (binary[start:start + 8] != seed_data.MAGIC
            or sha(binary[start:start + seed_data.SIZE]) != data["sha256"]):
        raise ValueError("Corruption multiworld template seed data differs")
    return root, files, native, boot


def bind_seed(manifest, mapping, output, *, directory=None):
    root, files, native, _ = load(directory)
    data = seed_data.compile_data(manifest, mapping)
    profile = bytes.fromhex(manifest["checkpoint_profile"])
    binary = bytearray(files["bridge.bin"])
    layout = native["multiworld"]["patchable_seed_data"]
    for address, replacement in ((layout["address"], data), (layout["checkpoint_address"], profile)):
        start = address - native["address"]
        binary[start:start + len(replacement)] = replacement
    metadata = copy.deepcopy(native)
    metadata["binary_sha256"] = sha(binary)
    metadata["network_profile_hex"] = profile.hex()
    metadata["network_profile_sha256"] = sha(profile)
    metadata["template_native_sha256"] = sha(files["bridge.bin"])
    metadata["multiworld"].update(world_uuid=manifest["world_uuid"], seed_fingerprint=manifest["seed_fingerprint"],
                                  save_slot=manifest["save_slot"], seed_data_sha256=sha(data),
                                  save_filename=base64.b32encode(hashlib.sha256(data + profile).digest()).decode()[:8])
    metadata["multiworld"]["patchable_seed_data"]["sha256"] = sha(data)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    (output / "bridge.bin").write_bytes(binary)
    (output / "bridge.json").write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")
    return metadata


def bind_bootstrap(directory, binary, metadata):
    _, files, native, boot = load(directory)
    if (len(binary) != native["size"] or metadata.get("template_native_sha256") != sha(files["bridge.bin"])
            or sha(binary) != metadata["binary_sha256"]):
        raise ValueError("Personalized runtime does not match its bootstrap template")
    # Independently reject changes outside the two declared data regions.
    original = files["bridge.bin"]
    allowed = bytearray(len(binary))
    layout = native["multiworld"]["patchable_seed_data"]
    for address, size in ((layout["address"], seed_data.SIZE), (layout["checkpoint_address"], 80)):
        start = address - native["address"]
        allowed[start:start + size] = b"\1" * size
    if any(a != b and not allowed[i] for i, (a, b) in enumerate(zip(original, binary, strict=True))):
        raise ValueError("Seed personalization changed runtime instructions")
    offset = files["payload.bin"].find(original)
    payload = files["payload.bin"][:offset] + binary + files["payload.bin"][offset + len(binary):]
    report = dict(boot, bootstrap_sha256=sha(payload), template_bootstrap_sha256=sha(files["payload.bin"]),
                  native_personalization="bounded_seed_table_and_checkpoint_identity_only")
    return payload, report


def build_assets(output, manifest, mapping):
    """Build-time operation only. Distributed clients never invoke a compiler."""
    from nullphaze_network.prime3_lua_service import bridge

    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    (output / "seed.h").write_text(seed_data.HEADER)
    (output / "seed.bin").write_bytes(seed_data.compile_data(manifest, mapping))
    (output / "profile.bin").write_bytes(bytes.fromhex(manifest["checkpoint_profile"]))
    options = dict(save_trace=True, network_profile=output / "profile.bin", receipt_lifecycle=True,
                   receipt_coupling=True, receipt_delivery=True, network_delivery=True,
                   owned_network_delivery=True, owned_receive_mem2=True,
                   multiworld_header=output / "seed.h", multiworld_data=output / "seed.bin")
    first = bridge.compile_bridge(output / "native", **options)
    second = bridge.compile_bridge(output / "native-repeat", **options)
    if first != second:
        raise ValueError("Corruption multiworld runtime is not reproducible")
    bridge.compile_bootstrap(output / "bootstrap", output / "native", first)
    for name in ("bridge.bin", "bridge.json"):
        (output / name).write_bytes((output / "native" / name).read_bytes())
    for name in ("payload.bin", "payload.json"):
        (output / name).write_bytes((output / "bootstrap" / name).read_bytes())
    receipt = {"schema": 1, "compiler": first["compiler"], "reproducible_native": True,
               "native_sources": source_hashes(),
               "files": {name: sha((output / name).read_bytes()) for name in ASSET_NAMES}}
    (output / "assets.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    load(output)
    return receipt
