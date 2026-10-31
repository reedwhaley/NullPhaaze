# Selective native zipline port from MP3Update v7.3 (MrMiguel211, MIT). Boundary names here:
# recipe, patch_area, install.
"""Selective native zipline port from MP3Update v7.3 (MrMiguel211, MIT).

The four original platforms in each room are reused in their original layers.
Only the collision/reposition/timing support and zipline gate removal are
ported. No ship, enemy, world-layer, polling or full-overlay changes are made.
"""
from __future__ import annotations

import base64
import hashlib
import json
from pathlib import Path

from nullphaze_core.archives import Archive
from nullphaze_network.prime3_lua_service.mrea_build import SeedMrea, next_instance_id
from nullphaze_network.prime3_lua_service.probe import properties, replace_properties
from retro_data_structures.enums.corruption import State, Message
from retro_data_structures.formats.script_object import Connection, ScriptInstanceRaw, InstanceId, _try_quick_get_name
from retro_data_structures.game_check import Game


def recipe():
    return json.loads(Path(__file__).with_suffix('.json').read_text(encoding='utf-8'))


def patch_area(raw, spec):
    area = SeedMrea.parse(raw, Game.CORRUPTION)
    layers = list(area.script_layers)
    actors = {int(a.id): (i, a) for i, l in enumerate(layers) for a in l.instances}
    if len(actors) != sum(len(list(l.instances)) for l in layers):
        raise ValueError(f"Fast Ziplines: duplicate actor IDs in {spec['name']}")
    before = {k: (i, a._raw.base_property, tuple(a.connections)) for k, (i,a) in actors.items()}
    # Allocate above all live/generated actors and dangling links, including core
    # and network additions. Never import MP3Update's reused ID collisions.
    remap = {}
    for item in spec['add']:
        identity = next_instance_id(area, int(next(iter(actors))) >> 16 & 0x3FF)
        identity = InstanceId.new(item['layer'], identity.area, identity.instance)
        remap[item['source_id']] = int(identity)
        layers[item['layer']]._raw.script_instances.append(ScriptInstanceRaw(
            item['type'], identity, (), base64.b64decode(item['properties'])))
        layers[item['layer']].mark_modified()
    def link(values):
        state, message, target = values
        return Connection(State(state), Message(message), InstanceId(remap.get(target, int(target,16)) & 0x03FFFFFF))
    def equivalent(a,b):
        # The core serializes targets without their six physical-layer bits;
        # retail and MP3Update often retain them. Runtime object lookup uses the
        # area/instance portion. Accept both without creating duplicate starts.
        return (a.state,a.message,int(a.target)&0x03FFFFFF)==(b.state,b.message,int(b.target)&0x03FFFFFF)
    for item in spec['add']:
        actor = next(a for a in layers[item['layer']].instances if int(a.id) == remap[item['source_id']])
        actor.connections = tuple(link(c) for c in item['links'])
    def expected(item):
        key = int(item['id'],16)
        if key not in actors or actors[key][0] != item['layer'] or actors[key][1].type_name != item['type']:
            raise ValueError(f"Fast Ziplines: unsupported {spec['name']} actor {item['id']} ({item['name']})")
        if _try_quick_get_name(actors[key][1]._raw.base_property) != item['name']:
            raise ValueError(f"Fast Ziplines: unexpected native actor name in {spec['name']} {item['id']}")
        return actors[key][1]
    for item in spec['patches']:
        actor = expected(item)
        current = dict(properties(actor._raw.base_property))
        updates = {}
        for change in item['fields']:
            key = int(change['field'],16)
            if current.get(key) != bytes.fromhex(change['old']):
                raise ValueError(f"Fast Ziplines: {spec['name']} actor {item['id']} field {key:08X} "
                                 'differs from supported retail/core data')
            updates[key] = bytes.fromhex(change['new'])
        actor._raw.base_property = replace_properties(actor._raw.base_property, updates)
        connections = list(actor.connections)
        for value in item['remove_links']:
            old = link(value)
            matches = [c for c in connections if equivalent(c,old)]
            if len(matches) != 1:
                raise ValueError(f"Fast Ziplines: missing native connection on {spec['name']} {item['id']}")
            connections.remove(matches[0])
        for value in item['add_links']:
            new = link(value)
            if not any(equivalent(new,c) for c in connections):
                connections.append(new)
        actor.connections = tuple(connections)
        layers[item['layer']].mark_modified()
    deleted = set()
    for item in spec['remove']:
        expected(item)
        deleted.add(int(item['id'],16))
    # Remove links into the deleted ride gates, including untouched sound and
    # reset actors. Everything else retains its native connections.
    deleted_targets = {key & 0x03FFFFFF for key in deleted}
    for layer in layers:
        layer._raw.script_instances[:] = [a for a in layer._raw.script_instances if int(a.id) not in deleted]
        for actor in layer.instances:
            if any(int(c.target)&0x03FFFFFF in deleted_targets for c in actor.connections):
                actor.connections = tuple(c for c in actor.connections if int(c.target)&0x03FFFFFF not in deleted_targets)
        layer.mark_modified()
    encoded = area.build()
    check = SeedMrea.parse(encoded, Game.CORRUPTION)
    after = {int(a.id): (i,a) for i,l in enumerate(check.script_layers) for a in l.instances}
    if set(after) != (set(before)-deleted) | set(remap.values()):
        raise ValueError('Fast Ziplines object-count/readback mismatch')
    original_targets = {int(c.target)&0x03FFFFFF for _, _, links in before.values() for c in links}
    live_targets = {key&0x03FFFFFF for key in after}
    new_missing = {int(c.target)&0x03FFFFFF for _,a in after.values() for c in a.connections if int(c.target)&0x03FFFFFF not in live_targets}
    if new_missing-original_targets or new_missing & deleted_targets:
        raise ValueError(f"Fast Ziplines: unresolved new links in {spec['name']}")
    return encoded, {'room':spec['name'], 'addedObjects':len(remap), 'removedObjects':len(deleted),
                     'netObjects':len(remap)-len(deleted), 'reusedPlatforms':4,
                     'supportIDs':remap, 'gameplayVerified':False}


def install(files, output):
    output = Path(output)
    output.mkdir(exist_ok=False)
    archive = Archive(Path(files)/'Metroid4.pak')
    targets = {int(r['mrea'],16):r for r in recipe()['rooms']}
    resources, rooms = [], []
    for resource in archive.resources:
        if resource.identity in targets:
            raw, report = patch_area(resource.read(), targets.pop(resource.identity))
            resource = resource.updated(raw)
            rooms.append(report)
        resources.append(resource)
    if targets:
        raise ValueError('Fast Ziplines: expected all four native zipline rooms in Metroid4.pak')
    destination = output/'Metroid4.pak'
    archive.write(destination, resources)
    actual = Archive(destination).resources
    if len(actual) != len(resources) or any(a.identity != b.identity or a.kind != b.kind or
            a.read() != b.read() for a,b in zip(actual,resources,strict=True)):
        raise ValueError('Fast Ziplines archive readback mismatch')
    result = {'rooms':rooms,'archives':{'Metroid4.pak':str(destination)},
              'excludedRooms':['Zipline Station Charlie','Spire Dock'], 'gameplayVerified':False,
              'recipeSha256':hashlib.sha256(Path(__file__).with_suffix('.json').read_bytes()).hexdigest(),
              'upstream':recipe()['source_url'], 'upstreamSha256':recipe()['source_sha256']}
    (output/'report.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    return result
