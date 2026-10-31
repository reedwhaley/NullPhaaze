"""Build neutral runtime templates and compare all non-personalized bytes."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import struct
import sys
import uuid

ROOT = Path(__file__).resolve().parents[1]


def normalized(raw, regions):
    result = bytearray(raw)
    for start, size in regions:
        if start < 0 or start + size > len(result):
            raise ValueError('Personalization range escaped the runtime image')
        result[start:start + size] = bytes(size)
    return hashlib.sha256(result).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cdv-root', type=Path, required=True, help='Repository root after applying the guarded overlay')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--install', action='store_true')
    args = parser.parse_args()
    target = args.cdv_root.resolve()
    output = args.output.resolve()
    for source in (ROOT, target):
        if output.is_relative_to(source) or source.is_relative_to(output):
            raise ValueError('Native build output must be disjoint from package and target source')
    # The frontend is intentionally external. Check its exact overlay before
    # importing its compilation helpers, then use this package's backend first.
    from apply_cdv_overlay import preflight
    if preflight(target):
        raise ValueError('Apply the complete recognized overlay before compiling native templates')
    sys.dont_write_bytecode = True
    sys.path[:0] = [str(ROOT / 'src'), str(target / 'cdv')]
    from nullphaze_network.prime3_lua_service import bridge, network_save, runtime_assets, seed_data
    output.mkdir(parents=True, exist_ok=False)
    world = uuid.uuid5(uuid.NAMESPACE_DNS, 'nullphaze.source-template.invalid')
    lineage = uuid.uuid5(world, 'neutral-build-template')
    profile = world.bytes + lineage.bytes + b''.join(network_save.slot_identity(lineage, i).bytes for i in range(3))
    network_save.validate_profile(profile)
    # These are inert build identities. Export replaces only the bounded seed
    # and checkpoint-profile regions after validating a real seed's manifest.
    values = bytearray(seed_data.SIZE)
    values[:16] = seed_data.MAGIC + struct.pack('>II', 1, seed_data.SIZE)
    values[16:32] = world.bytes
    values[32:64] = hashlib.sha256(b'neutral build template; replaced before export').digest()
    (output / 'seed.h').write_text(seed_data.HEADER, encoding='utf-8')
    (output / 'seed.bin').write_bytes(values)
    (output / 'profile.bin').write_bytes(profile)
    flags = dict(save_trace=True, network_profile=output / 'profile.bin', receipt_lifecycle=True,
                 receipt_coupling=True, receipt_delivery=True, network_delivery=True,
                 owned_network_delivery=True, owned_receive_mem2=True,
                 multiworld_header=output / 'seed.h', multiworld_data=output / 'seed.bin')
    first = bridge.compile_bridge(output / 'native', **flags)
    second = bridge.compile_bridge(output / 'native-repeat', **flags)
    if first != second:
        raise ValueError('Repeated native builds differ')
    bridge.compile_bootstrap(output / 'bootstrap', output / 'native', first)
    for folder, names in [('native', ('bridge.bin', 'bridge.json')), ('bootstrap', ('payload.bin', 'payload.json'))]:
        for name in names:
            shutil.copyfile(output / folder / name, output / name)
    binary = (output / 'bridge.bin').read_bytes()
    payload = (output / 'payload.bin').read_bytes()
    baseline = json.loads((ROOT / 'build/native-code-baseline.json').read_text(encoding='utf-8'))
    layout = first['multiworld']['patchable_seed_data']
    regions = [(layout['address'] - first['address'], seed_data.SIZE),
               (layout['checkpoint_address'] - first['address'], 80)]
    if (first['address'] != baseline['bridge_address'] or len(binary) != baseline['bridge_size']
            or len(payload) != baseline['bootstrap_size']
            or [list(value) for value in regions] != baseline['personalization_ranges']
            or payload.count(binary) != 1):
        raise ValueError('Runtime layout differs from the accepted .14r2 build')
    offset = payload.find(binary)
    # Normalize data, not instructions. An equal size or successful link is not
    # sufficient proof that this build retained the accepted native behavior.
    if (offset != baseline['bootstrap_bridge_offset']
            or normalized(binary, regions) != baseline['normalized_bridge_sha256']
            or normalized(payload, [(offset + start, size) for start, size in regions])
            != baseline['normalized_bootstrap_sha256']):
        raise ValueError('Native/bootstrap bytes changed outside personalization regions')
    receipt = dict(schema=1, compiler=first['compiler'], reproducible_native=True,
                   native_sources=runtime_assets.source_hashes(),
                   files={name: runtime_assets.sha((output / name).read_bytes()) for name in runtime_assets.ASSET_NAMES})
    (output / 'assets.json').write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    runtime_assets.load(output)
    if args.install:
        destination = runtime_assets.default_directory()
        destination.mkdir(parents=True, exist_ok=True)
        for name in (*runtime_assets.ASSET_NAMES, 'assets.json'):
            shutil.copyfile(output / name, destination / name)
        runtime_assets.load(destination)
    print('Native templates built twice; all accepted bytes outside personalization regions match.')


if __name__ == '__main__':
    main()
