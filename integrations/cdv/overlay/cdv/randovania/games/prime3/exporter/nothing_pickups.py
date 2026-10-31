# Native Friend Credit visuals for Nothing pickups, using the user's disc assets. Boundary
# names here: FriendCredit, normalize_area, nothing_indices, neutralize_area, install.
"""Native Friend Credit visuals for Nothing pickups, using the user's disc assets."""
from __future__ import annotations

import copy
import hashlib
import json
import struct
from pathlib import Path

from construct import Container
from nullphaze_core.archives import Archive, Resource
from nullphaze_core.resources import make_string_table
from nullphaze_core.rules import catalog
from nullphaze_network.prime3_lua_service.multiworld_areas import _disconnect_core_grants
from nullphaze_network.prime3_lua_service.multiworld_models import patch_area, visual_bindings
from nullphaze_network.prime3_lua_service.mrea_build import SeedMrea
from nullphaze_network.prime3_lua_service.probe import properties, replace_properties
from nullphaze_network.prime3_lua_service.runtime_export import pickup_map
from retro_data_structures.game_check import Game

from randovania.games.prime3.exporter.main_menu import _decoded
from randovania.patching.prime.corruption_model_scale import dimensions, match_scale

FRIEND_CHARACTER = 0xE21214EC80974A5A
FRIEND_MODEL = 0x0CC01181145BA08D
ZERO = bytes(4)


class FriendCredit:
    def __init__(self, files):
        manifest = json.loads(Path(__file__).with_name('friend_credit.json').read_text())
        archive = Archive(Path(files) / 'Logbook.pak')
        available = {r.identity: r for r in archive.resources}
        self.resources = []
        for row in manifest['resources']:
            resource = available.get(int(row['id'], 16))
            if (resource is None or resource.kind.decode() != row['type']
                    or resource.compressed != row['compressed']
                    or hashlib.sha256(resource.read()).hexdigest() != row['sha256']):
                raise ValueError(f"Friend Credit source asset differs from supported retail data: {row['id']}")
            self.resources.append(resource)
        normalization = manifest['normalization']
        model = next(r for r in self.resources if r.identity == FRIEND_MODEL)
        self.source_dimensions = dimensions(_decoded(model), (1.0, 1.0, 1.0))
        if list(self.source_dimensions) != normalization['source_dimensions']:
            raise ValueError('Friend Credit sizing metadata differs from the source model')
        self.reference_dimensions = tuple(normalization['reference_dimensions'])
        self.uniform_multiplier = match_scale(self.source_dimensions, self.reference_dimensions)[0]

    def entry(self, row):
        if row['name'] != 'Nothing':
            raise ValueError('Friend Credit is reserved for Nothing pickups')
        return {'native': {'CMDL': f'{FRIEND_MODEL:016X}', 'CHAR': f'{FRIEND_CHARACTER:016X}'}}

    def dependencies(self, entry):
        return self.resources


def normalize_area(raw, area_id, bindings, cache):
    """Match the native Missile Expansion footprint, retaining each actor's modifiers."""
    area = SeedMrea.parse(raw, Game.CORRUPTION)
    layers = list(area.script_layers)
    originals = {int(obj.id): copy.deepcopy(obj._raw) for layer in layers for obj in layer.instances}
    editors = {}
    for (identity, layer_index, instance), (row, _) in bindings.items():
        if identity != area_id:
            continue
        matches = [obj for obj in layers[layer_index].instances if obj.id.instance == instance]
        if len(matches) != 1 or row['name'] != 'Nothing':
            raise ValueError('Missing or ambiguous Nothing sizing actor')
        actor = matches[0]
        fields = dict(properties(actor._raw.base_property))
        editor = fields[0x255A4580]
        # EditorProperties is a nested TLV record. Wrap its existing count in a
        # root header to reuse the byte-preserving property reader/writer.
        wrapped = b'\xff'*4 + struct.pack('>H', len(editor)) + editor
        transform = dict(properties(wrapped))[0x5846524D]
        if len(transform) != 36:
            raise ValueError('Unsupported Nothing pickup transform')
        before = struct.unpack_from('>3f', transform, 24)
        scale = match_scale(cache.source_dimensions, cache.reference_dimensions, before)
        updated = transform[:24] + struct.pack('>3f', *scale)
        changed = replace_properties(wrapped, {0x5846524D: updated})[6:]
        actor._raw.base_property = replace_properties(actor._raw.base_property, {0x255A4580: changed})
        editors[int(actor.id)] = editor
        layers[layer_index].mark_modified()
    encoded = area.build()
    checked = SeedMrea.parse(encoded, Game.CORRUPTION)
    for layer in checked.script_layers:
        for actor in layer.instances:
            expected = copy.deepcopy(actor._raw)
            if int(actor.id) in editors:
                expected.base_property = replace_properties(expected.base_property,
                                                            {0x255A4580: editors[int(actor.id)]})
            if expected != originals[int(actor.id)]:
                raise ValueError('Nothing sizing changed an unrelated actor or property')
    return encoded


def nothing_indices(patch_data):
    if patch_data.get('multiworld') is not None:
        # Decode the authenticated pickup, rather than trusting its display label.
        from randovania.games.prime3.exporter.models import model_plan
        indices = [row['index'] for row in model_plan(patch_data['multiworld'])
                   if row['game'] == 'prime3' and row['name'] == 'Nothing']
    else:
        indices = patch_data.get('nothing_locations', [])
    if (not isinstance(indices, list) or any(type(i) is not int or not 0 <= i < 100 for i in indices)
            or len(set(indices)) != len(indices)):
        raise ValueError('Invalid Nothing pickup indices')
    if patch_data.get('exclude_olympus'):
        from randovania.games.prime3.olympus import OLYMPUS_PICKUP_INDICES
        indices = [i for i in indices if i not in OLYMPUS_PICKUP_INDICES]
    return indices


def neutralize_area(raw, area_id, indices, locations):
    """Remove placeholder inventory grants while keeping retail progression events."""
    area = SeedMrea.parse(raw, Game.CORRUPTION)
    layers = list(area.script_layers)
    objects = {int(obj.id): obj for layer in layers for obj in layer.instances}
    strings = []
    for index in indices:
        location = locations[index]
        aliases = [alias for alias in catalog()['fakePickups']
                   if alias['item_index'] == index and alias['mrea_id'] == area_id]
        if location['area'] != area_id and not aliases:
            continue
        _disconnect_core_grants(index, area_id, objects)
        primary = location['area'] == area_id
        neutral = []
        if primary:
            variant = location['variants'][0]['objects']
            actor = objects[variant['instance_id']['id']]
            if actor.type_name != variant['instance_id']['type']:
                raise ValueError('Nothing pickup actor differs from audited mapping')
            neutral.append(actor)
            if 'percentage_pickup_id' in variant:
                neutral.append(objects[variant['percentage_pickup_id']['id']])
        for alias in aliases:
            matches = [obj for obj in layers[alias['scly_section']].instances
                       if obj.id.instance == int(alias['instance_id']['$bytes'], 16)]
            if len(matches) != 1:
                raise ValueError('Missing Nothing pickup alias')
            if matches[0].type_name == 'PCKP':
                neutral.append(matches[0])
        for obj in neutral:
            if obj.type_name == 'PCKP':
                changes = {field: ZERO for field in (0x28C71B54, 0x94AF1445, 0x165AB069)}
            elif obj.type_name == 'SPFN':
                fields = dict(properties(obj._raw.base_property))
                if fields[0xB8AFCF21] != (2527813936).to_bytes(4, 'big'):
                    raise ValueError('Unexpected Nothing inventory function')
                changes = {0xB581574B: ZERO}
            else:
                raise ValueError('Unsupported Nothing grant actor')
            obj._raw.base_property = replace_properties(obj._raw.base_property, changes)
        if not primary:
            continue
        memo = objects[variant['memo_id']['id']]
        if memo.type_name != 'MEMO':
            raise ValueError('Missing Nothing pickup memo')
        identity = int.from_bytes(hashlib.sha256(f'NullPhaaze Nothing memo/{index}'.encode()).digest()[:8], 'big')
        payload = make_string_table(['Nothing acquired!'])
        strings.append(Resource(identity, b'STRG', 0, len(payload), data=payload))
        memo._raw.base_property = replace_properties(memo._raw.base_property, {
            2441225484: identity.to_bytes(8, 'big'), 0x64124219: ZERO})
        deps = area.get_section('dependencies_section')[0]
        deps.dependencies.insert(deps.offsets[1], Container(asset_id=identity, type='STRG'))
        for layer_index in range(1, len(deps.offsets)):
            deps.offsets[layer_index] += 1
    for layer in layers:
        layer.mark_modified()
    return area.build(), strings


def install(files: Path, output: Path, patch_data: dict) -> dict:
    indices = nothing_indices(patch_data)
    report = {'model': 'Friend_Credit', 'locations': indices, 'actors': 0, 'archives': {}}
    if not indices:
        return report
    cache = FriendCredit(files)
    report['size_normalization'] = {
        'reference': 'Missile Expansion',
        'source_dimensions': cache.source_dimensions,
        'reference_dimensions': cache.reference_dimensions,
        'uniform_multiplier': cache.uniform_multiplier,
    }
    rows = [{'index': i, 'game': 'prime1', 'name': 'Nothing'} for i in indices]
    bindings = visual_bindings(rows)
    locations = {row['index']: row for row in pickup_map()['pickups']}
    areas = {key[0] for key in bindings} | {locations[i]['area'] for i in indices}
    output.mkdir(exist_ok=False)
    remaining = set(areas)
    replaced = set()
    for path in sorted(files.glob('*.pak')):
        archive = Archive(path)
        targets = {r.identity for r in archive.resources if r.kind == b'MREA'} & areas
        if not targets:
            continue
        resources, added, changes = [], {}, []
        for resource in archive.resources:
            if resource.identity in targets:
                raw, dependencies, records = patch_area(resource.read(), resource.identity, bindings, cache)
                raw = normalize_area(raw, resource.identity, bindings, cache)
                if patch_data.get('multiworld') is None:
                    raw, memos = neutralize_area(raw, resource.identity, indices, locations)
                    dependencies += memos
                resources.append(resource.updated(raw))
                changes += records
                added.update((r.identity, r) for r in dependencies)
            else:
                resources.append(resource)
        originals = {r.identity: r for r in archive.resources}
        for identity, resource in added.items():
            if identity in originals:
                if originals[identity].kind != resource.kind or originals[identity].read() != resource.read():
                    raise ValueError('Nothing resource identity collision')
            else:
                resources.append(resource)
        destination = output / path.name
        archive.write(destination, resources)
        actual = {r.identity: r for r in Archive(destination).resources}
        if set(actual) != {r.identity for r in resources} or any(
                actual[r.identity].kind != r.kind or actual[r.identity].read() != r.read() for r in resources):
            raise ValueError('Nothing model archive readback mismatch')
        with destination.open('rb') as stream:
            report['archives'][path.name] = hashlib.file_digest(stream, 'sha256').hexdigest()
        report['actors'] += len(changes)
        replaced.update(row['location'] for row in changes)
        remaining -= targets
    if remaining:
        raise ValueError(f'Missing Nothing pickup areas: {sorted(remaining)}')
    report['scripted_rewards_without_model_slots'] = sorted(set(indices) - replaced)
    return report
