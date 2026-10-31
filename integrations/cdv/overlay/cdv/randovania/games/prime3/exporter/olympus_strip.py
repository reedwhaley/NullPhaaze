# Remove audited, unreachable Olympus bundles while retaining shared assets. Boundary names
# here: prune, install.
"""Remove audited, unreachable Olympus bundles while retaining shared assets."""
from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

from nullphaze_core.archives import Archive
from nullphaze_network.prime3_lua_service.mrea_build import SeedMrea
from retro_data_structures.game_check import Game

from randovania.games.prime3.exporter.warp_to_space import _actor, _name


def prune(resources, audit):
    rooms = {int(n, 16) for n in audit['rooms']}
    exclusive = {int(n, 16) for n in audit['exclusive_ids']}
    candidates = {int(n, 16): {tuple(row) for row in rows} for n, rows in audit['candidates'].items()}
    bundles, pending, found = set(), [], set()
    for index, resource in enumerate(resources):
        pending.append(index)
        if resource.kind in (b'MREA', b'MLVL'):
            if resource.identity in rooms:
                bundles.update(pending)
                found.add(resource.identity)
            pending = []
    if found != rooms:
        raise ValueError('Olympus removal: expected all 28 supported Olympus room bundles; recheck source image.')
    # A seed may import an originally Olympus-only asset into a playable room.
    # Keep its original copies too; never let stripping invalidate that closure.
    reused = {r.identity for i, r in enumerate(resources) if i not in bundles}
    removed, survivors = [], []
    for index, resource in enumerate(resources):
        matches = False
        if index in bundles and resource.identity in candidates:
            matches = (resource.kind.decode(), hashlib.sha256(resource.read()).hexdigest()) in candidates[resource.identity]
        if resource.identity in rooms and not matches:
            raise ValueError(f'Olympus removal: unsupported room preimage {resource.identity:016X}; no files published.')
        if matches and not (resource.identity in exclusive and resource.identity in reused):
            removed.append(resource)
        else:
            survivors.append(resource)
    retained = {r.identity for r in survivors}
    if retained & rooms:
        raise ValueError('Olympus removal: a room survived outside its expected bundle.')
    for resource in removed:
        if resource.identity not in exclusive and resource.identity not in retained:
            raise ValueError(f'Olympus removal: shared asset {resource.identity:016X} has no retained copy.')
    return survivors, {'rooms_removed': len(rooms), 'occurrences_removed': len(removed),
                       'stored_payload_bytes_removed': sum(r.size for r in removed),
                       'seed_reused_assets_preserved': sorted(f'{n:016X}' for n in exclusive & reused)}


def install(files: Path, output: Path) -> dict:
    files, output = Path(files), Path(output)
    output.mkdir(exist_ok=False)
    audit = json.loads(Path(__file__).with_suffix('.json').read_text())
    archive = Archive(files/'Metroid1.pak')
    rows, report = prune(archive.resources, audit)
    source = next(r for r in rows if r.identity == 0x139F234E0EB5EDA5)
    area = SeedMrea.parse(source.read(), Game.CORRUPTION)
    teleporter = _actor(area, 0x001800DA, 'TEL1')
    if _name(teleporter) != 'Text Teleport to 05_GFShip':
        raise ValueError('Olympus removal: unsupported Norion transporter; recheck source image.')
    incoming = []
    for layer in [*area.script_layers, area.generated_objects_layer]:
        for actor in layer.instances:
            incoming.extend((int(actor.id), c.state.name, c.message.name)
                            for c in actor.connections if int(c.target) == int(teleporter.id))
            actor.connections = tuple(c for c in actor.connections if int(c.target) != int(teleporter.id))
        layer._raw.script_instances = [a for a in layer._raw.script_instances if int(a.id) != int(teleporter.id)]
        layer.mark_modified()
    if incoming != [(0x00180162, 'Relay', 'SetToZero')]:
        raise ValueError('Olympus removal: Norion transporter trigger differs from audited source.')
    raw = area.build()
    if bytes.fromhex('0D887EA494D559D5') in raw:
        raise ValueError('Olympus removal: Norion still refers to Medical Bay.')
    rows = [source.updated(raw) if r.identity == source.identity else r for r in rows]
    destination = output/'Metroid1.pak'
    archive.write(destination, rows)
    check = Archive(destination)
    if len(check.resources) != len(rows) or any(
            (a.identity, a.kind, a.read()) != (b.identity, b.kind, b.read())
            for a, b in zip(rows, check.resources, strict=True)):
        raise ValueError('Olympus removal: archive readback mismatch.')
    report.update(native_transporter_removed=True, archive_readback=True,
                  world_save_map_metadata_preserved=True, shared_virtual_area_preserved=True)
    (output/'report.json').write_text(json.dumps(report, indent=2)+'\n')
    shutil.copyfile(destination, files/'Metroid1.pak')
    return report
