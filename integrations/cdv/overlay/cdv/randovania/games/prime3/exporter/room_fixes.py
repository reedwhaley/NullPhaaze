# MP3-012: prevent the Valhalla Aurora Chamber upper-door fall skip. Boundary names here:
# patch_area, install.
"""MP3-012: prevent the Valhalla Aurora Chamber upper-door fall skip."""
from __future__ import annotations

import json
from pathlib import Path

from nullphaze_core.archives import Archive
from nullphaze_network.prime3_lua_service.mrea_build import SeedMrea
from retro_data_structures.game_check import Game

AREA = 0x58F7034E868C50E7
TARGET = 0x00070190  # Death Fall Spawn 009, beside Control Room Access.
ENTRANCE = 0x00070024
SOURCE_TRANSFORM = bytes.fromhex('c2b658c4426573e44272584e0000000000000000c2b400003fe666673fe666673fe66667')
ENTRANCE_TRANSFORM = bytes.fromhex('c1836314426573e34219f8d4000000000000000042b400003fe666673fe666673fe66667')


def patch_area(raw):
    area = SeedMrea.parse(raw, Game.CORRUPTION)
    actors = {int(a.id):(li,a) for li,l in enumerate(area.script_layers) for a in l.instances}
    def required(identity, name):
        if identity not in actors or actors[identity][1].type_name != 'SPWN':
            raise ValueError(f'MP3-012: missing Aurora Chamber spawn {identity:08X}; unsupported source')
        actor = actors[identity][1]
        props = actor.get_properties()
        if props.editor_properties.name != name:
            raise ValueError(f'MP3-012: unexpected Aurora Chamber spawn {identity:08X}; unsupported source')
        return actor, props
    actor, props = required(TARGET, 'Death Fall Spawn 009')
    _, entrance = required(ENTRANCE, 'ABANDONED SHIP')
    current = props.editor_properties.transform.to_bytes(Game.CORRUPTION)
    if (current not in (SOURCE_TRANSFORM, ENTRANCE_TRANSFORM)
            or entrance.editor_properties.transform.to_bytes(Game.CORRUPTION) != ENTRANCE_TRANSFORM
            or not props.death_fall or props.first_spawn or entrance.death_fall or not entrance.first_spawn):
        raise ValueError('MP3-012: Aurora Chamber respawn/entrance differs from supported data; cannot safely move Spawn 009')
    # Replace precisely the native transform block. All flags, inventories,
    # connections and the other nine death-fall actors remain byte-identical.
    if actor._raw.base_property.count(current) != 1:
        raise ValueError('MP3-012: ambiguous Aurora Chamber respawn transform; unsupported source')
    actor._raw.base_property = actor._raw.base_property.replace(current, ENTRANCE_TRANSFORM, 1)
    if current != ENTRANCE_TRANSFORM:
        list(area.script_layers)[actors[TARGET][0]].mark_modified()
    return area.build(), {'room':'Valhalla / Aurora Chamber', 'actor':f'{TARGET:08X}',
                          'destinationSpawn':f'{ENTRANCE:08X}', 'movedRespawns':1,
                          'otherRespawnsChanged':0, 'addedObjects':0}


def install(files, output):
    output = Path(output)
    output.mkdir(exist_ok=False)
    archive = Archive(Path(files)/'Metroid1.pak')
    resources=[]; report=None
    for resource in archive.resources:
        if resource.identity == AREA:
            raw, report = patch_area(resource.read())
            resource = resource.updated(raw)
        resources.append(resource)
    if report is None:
        raise ValueError('MP3-012: Valhalla Aurora Chamber missing from Metroid1.pak; unsupported source')
    destination=output/'Metroid1.pak'
    archive.write(destination,resources)
    actual=Archive(destination).resources
    if len(actual)!=len(resources) or any(a.identity!=b.identity or a.kind!=b.kind or a.read()!=b.read()
                                         for a,b in zip(actual,resources,strict=True)):
        raise ValueError('MP3-012: room-fix archive readback mismatch')
    report['archives']={'Metroid1.pak':str(destination)}
    report['gameplayVerified']=False
    (output/'report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    return report
