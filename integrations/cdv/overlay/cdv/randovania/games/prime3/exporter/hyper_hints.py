# MP3-006--009: owner/region Hyper item hints on native lore/screens. Boundary names here:
# create_data, validate_data, patch_area, install.
"""MP3-006--009: owner/region Hyper item hints on native lore/screens.

Canonical metadata generation stays usable by the server without native tools.
The installer preserves every actor, connection and native scan-completion path.
"""
from __future__ import annotations

import json
from pathlib import Path
import struct

from randovania.games.prime3.exporter import item_location_hints

ITEMS = {
    'hypermode': ('HyperModeTank', 'Hypermode'),
    'hyper_ball': ('HyperModeBall', 'Hyper Ball'),
    'hyper_missile': ('HyperModeMissile', 'Hyper Missile'),
    'hyper_grapple': ('HyperModeGrapple', 'Hyper Grapple'),
}
# Exact supported native actor IDs, editor names and original SCAN references.
# All nine Barracks screens are alternatives of the same three projections.
TARGETS = {
    0x161F24A2D748EA44: ('Metroid1.pak', 'hypermode', 'Norion / Docking Hub Alpha', {
        0x0002067A: ('Lore 015 - Rundas', 0x52F11201D00AFFF2)}),
    0x89DF9C59CEF1CB98: ('Metroid3.pak', 'hyper_ball', 'Bryyo Fire / Main Lift', {
        0x0003023F: ('Bryyo Lore 003', 0xDB90F4D0EE9CA503)}),
    0x9B58B77568E1B50C: ('Metroid4.pak', 'hyper_missile', 'Elysia Main / Barracks Lift', {
        **{n: ('Screen - [AU]', 0xA0A23EF390C1AD33) for n in (0x14070010,0x1407014D,0x14070155)},
        **{n: ('Screen - [Ghor]', 0x906D75982B87FCF8) for n in (0x18070021,0x180700D1,0x18070159)},
        **{n: ('Screen - [Static]', 0x2D9C4AF5536EB166) for n in (0x1C0700BE,0x1C070149,0x1C070152)}}),
    0xCB13D4B0686995E7: ('Metroid5.pak', 'hyper_grapple', 'Pirate Homeworld Research / Transit Station 1-A', {
        0x000B00D6: ('Lore', 0xB3C782C86C58209E)}),
}


def create_data(factory):
    return item_location_hints.create_data(factory, items=ITEMS)


def validate_data(data):
    item_location_hints.validate_data(data, items=ITEMS)


def patch_area(raw, identity, lookup, text):
    from construct import Container
    from nullphaze_network.prime3_lua_service.mrea_build import SeedMrea
    from nullphaze_network.prime3_lua_service.probe import properties, replace_properties
    from randovania.games.prime3.exporter.main_menu import _decoded
    from randovania.games.prime3.exporter.seed_hints import private_scan
    from retro_data_structures.game_check import Game

    _, _, room, targets = TARGETS[identity]
    area = SeedMrea.parse(raw, Game.CORRUPTION)
    actors = {int(a.id): (li,a) for li,l in enumerate(area.script_layers) for a in l.instances}
    additions, records = {}, []
    for actor_id,(name,scan_id) in targets.items():
        if actor_id not in actors:
            raise ValueError(f'Hyper hints: {room} is missing native scan {actor_id:08X}; unsupported source')
        li,actor = actors[actor_id]
        if actor.type_name != 'POIN':
            raise ValueError(f'Hyper hints: wrong scan actor type at {room}/{actor_id:08X}')
        props = actor.get_properties()
        if props.editor_properties.name != name or props.scan_info.scannable_info0 != scan_id:
            raise ValueError(f'Hyper hints: native scan differs at {room}/{actor_id:08X}; use a fresh supported export')
        if scan_id not in lookup or lookup[scan_id].kind != b'SCAN':
            raise ValueError(f'Hyper hints: missing SCAN {scan_id:016X} for {room}')
        scan = lookup[scan_id]
        scan_raw = _decoded(scan)
        dep = 19+int.from_bytes(scan_raw[17:19],'big')
        if dep+4 > len(scan_raw):
            raise ValueError(f'Hyper hints: invalid SCAN dependency table in {room}')
        count = struct.unpack_from('>I',scan_raw,dep)[0]
        if dep+4+12*count > len(scan_raw):
            raise ValueError(f'Hyper hints: truncated SCAN dependency table in {room}')
        texts = [int.from_bytes(scan_raw[dep+8+12*i:dep+16+12*i],'big') for i in range(count)
                 if scan_raw[dep+4+12*i:dep+8+12*i] == b'STRG']
        if len(texts)!=1 or texts[0] not in lookup or lookup[texts[0]].kind != b'STRG':
            raise ValueError(f'Hyper hints: expected one native scan STRG in {room}')
        assets = private_scan(scan,lookup[texts[0]],text)
        # Change precisely the scan reference. Native ScanDone actions remain.
        root = dict(properties(actor._raw.base_property))
        nested = root[3183395477]
        wrapped = b'\xff'*4+len(nested).to_bytes(2,'big')+nested
        rewritten = replace_properties(wrapped,{0xB94E9BE7:assets[0].identity.to_bytes(8,'big')})[6:]
        actor._raw.base_property = replace_properties(actor._raw.base_property,{3183395477:rewritten})
        list(area.script_layers)[li].mark_modified()
        deps = area.get_section('dependencies_section')[0]
        pos = deps.offsets[li+1]
        existing = {d.asset_id for d in deps.dependencies[deps.offsets[li]:pos]}
        missing = [r for r in assets if r.identity not in existing]
        deps.dependencies[pos:pos] = [Container(asset_id=r.identity,type=r.kind.decode()) for r in missing]
        for j in range(li+1,len(deps.offsets)): deps.offsets[j]+=len(missing)
        for res in assets:
            if res.identity in lookup or (res.identity in additions and additions[res.identity].read()!=res.read()):
                raise ValueError(f'Hyper hints: resource ID collision in {room}')
            additions[res.identity] = res
        records.append({'actor':f'{actor_id:08X}','name':name,'layer':li,
                        'original_scan':f'{scan_id:016X}','scan':f'{assets[0].identity:016X}',
                        'text':text})
    return area.build(), list(additions.values()), records


def install(files, output, data):
    from nullphaze_core.archives import Archive
    validate_data(data)
    output = Path(output)
    output.mkdir(exist_ok=False)
    report = {'archives':{},'rooms':[],'addedObjects':0,'gameplayVerified':False}
    for name in sorted({v[0] for v in TARGETS.values()}):
        archive = Archive(Path(files)/name)
        lookup = {r.identity:r for r in archive.resources}
        expected = {i for i,s in TARGETS.items() if s[0]==name and data[s[1]] is not None}
        found, resources = set(), []
        for res in archive.resources:
            if res.identity in expected:
                _,key,room,_ = TARGETS[res.identity]
                raw,assets,records = patch_area(res.read(),res.identity,lookup,data[key])
                # Each room's private SCAN/STRG closure precedes its MREA.
                resources.extend(assets)
                resources.append(res.updated(raw))
                found.add(res.identity)
                report['rooms'].append({'area':f'{res.identity:016X}','room':room,'item':key,'scans':records})
            else: resources.append(res)
        if found!=expected:
            raise ValueError(f'Hyper hints: missing required room in {name}; unsupported export')
        destination = output/name
        archive.write(destination,resources)
        actual = Archive(destination).resources
        if len(actual)!=len(resources) or any((a.identity,a.kind,a.compressed,a.read()) !=
                (b.identity,b.kind,b.compressed,b.read()) for a,b in zip(actual,resources,strict=True)):
            raise ValueError(f'Hyper hints: archive readback mismatch in {name}')
        report['archives'][name] = str(destination)
    (output/'report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    return report
