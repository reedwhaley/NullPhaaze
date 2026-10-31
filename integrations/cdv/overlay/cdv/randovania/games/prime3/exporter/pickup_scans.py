# Placement-specific scan labels, using private copies of a native pickup scan. Boundary
# names here: scan_rows, ScanTemplate, patch_area, install.
"""Placement-specific scan labels, using private copies of a native pickup scan."""
from __future__ import annotations

import hashlib
import json
import struct
import uuid
from pathlib import Path

from construct import Container
from nullphaze_core.archives import Archive, Resource
from nullphaze_core.planner import decode_layout, dependency_closure
from nullphaze_core.rules import catalog, decode
from nullphaze_network.prime3_lua_service.mrea_build import SeedMrea
from nullphaze_network.prime3_lua_service.multiworld_models import visual_bindings
from nullphaze_network.prime3_lua_service.probe import properties, replace_properties
from retro_data_structures.formats.strg import Strg
from retro_data_structures.game_check import Game

from randovania.games.prime3.exporter.main_menu import _decoded, build_sequential_strings

TEMPLATE_SCAN = 0x16D79F823362174F
TEMPLATE_TEXT = 0xBCD11F7BD2BA87C5
TEMPLATE_SHA256 = 'bdbd6264c43ae0c3c0fe200f07ad2d2661ed128e817c85ebbb1ed6a973c86c1c'
SCAN_FIELD = 0xB94E9BE7


from randovania.games.prime3.exporter.hint_text import _safe, label


def scan_rows(patch_data):
    manifest = patch_data.get('multiworld')
    rows = manifest['locations'] if manifest is not None else patch_data.get('pickup_scan_text')
    if rows is None:
        # Old stored single-player layouts have no display metadata. Their
        # acquisition labels provide the established human-readable item names.
        data = catalog()
        memos = {r['resource_id']: r['language_modifications'][0]['strings'][0]
                 for r in data['strings']}
        nothing = set(patch_data.get('nothing_locations', []))
        rows = []
        for index, item in enumerate(decode_layout(patch_data['seed'])):
            memo = int.from_bytes(decode(data['items'][item])['memo'], 'big')
            rows.append({'index': index, 'item_name': 'Nothing' if index in nothing else
                         memos[memo].removesuffix(' acquired!'), 'local': True})
    if (not isinstance(rows, list) or len(rows) != 100 or
            [r.get('index') for r in rows] != list(range(100)) or
            any(type(r.get('index')) is not int for r in rows)):
        raise ValueError('Pickup scan text requires all 100 ordered locations')
    for row in rows:
        label(row)
        if manifest is not None and row['local'] != (uuid.UUID(row['recipient_world']) == uuid.UUID(manifest['world_uuid'])):
            raise ValueError('Pickup scan ownership differs from the exported world')
        if manifest is None and not row['local']:
            raise ValueError('Single-player pickup scan cannot have a remote recipient')
    return [r for r in rows if not patch_data.get('exclude_olympus', False) or r['index'] >= 3]


class ScanTemplate:
    def __init__(self, files):
        resources = {r.identity: r for r in Archive(Path(files) / 'Logbook.pak').resources}
        resource = resources[TEMPLATE_SCAN]
        self.raw = _decoded(resource)
        if resource.kind != b'SCAN' or hashlib.sha256(self.raw).hexdigest() != TEMPLATE_SHA256:
            raise ValueError('Unsupported native pickup SCAN template in Logbook.pak')
        self.dependencies = []
        for entry in dependency_closure(TEMPLATE_SCAN, b'SCAN'):
            identity = entry['file_id']
            if identity in (TEMPLATE_SCAN, TEMPLATE_TEXT):
                continue
            dependency = resources[identity]
            if dependency.kind != entry['resource_type']:
                raise ValueError('Pickup SCAN dependency type differs from supported retail data')
            self.dependencies.append(dependency)

    def create(self, row):
        text = label(row)
        namespace = f"NullPhaaze pickup scan v1/{row['index']}/{text}"
        scan_id, text_id = [int.from_bytes(hashlib.sha256((namespace + suffix).encode()).digest()[:8], 'big')
                            for suffix in ('/SCAN', '/STRG')]
        raw = bytearray(self.raw)
        # SNFO's string pointer and its explicit dependency table are separate.
        marker = bytes.fromhex('2F5B64230008') + TEMPLATE_TEXT.to_bytes(8, 'big')
        if raw.count(marker) != 1:
            raise ValueError('Native pickup SCAN string field differs from supported layout')
        offset = raw.index(marker) + 6
        raw[offset:offset+8] = text_id.to_bytes(8, 'big')
        deps = 19 + int.from_bytes(raw[17:19], 'big')
        changed = 0
        for i in range(struct.unpack_from('>I', raw, deps)[0]):
            offset = deps + 4 + 12*i
            if raw[offset:offset+12] == b'STRG' + TEMPLATE_TEXT.to_bytes(8, 'big'):
                raw[offset+4:offset+12] = text_id.to_bytes(8, 'big')
                changed += 1
        if changed != 1:
            raise ValueError('Native pickup SCAN string dependency differs from supported layout')
        # Populate the scan slots as well as the equipment/logbook slot. Keep
        # forward-only offsets: RDS's deduplicating writer is not retail-safe.
        table = Strg(Container(languages={lang: [text, text, text] for lang in
                     ('ENGL', 'JAPN', 'GERM', 'FREN', 'SPAN', 'ITAL')}, name_table={}), Game.CORRUPTION)
        strings = build_sequential_strings(table)
        return [Resource(scan_id, b'SCAN', 0, 0).updated(bytes(raw)),
                Resource(text_id, b'STRG', 0, 0).updated(strings), *self.dependencies]


def patch_area(raw, identity, bindings, template):
    area = SeedMrea.parse(raw, Game.CORRUPTION)
    layers = list(area.script_layers)
    additions, records = {}, []
    originals = {int(o.id): o._raw.base_property for l in layers for o in l.instances}
    for (target, layer_index, instance), (row, _) in bindings.items():
        if target != identity:
            continue
        matches = [o for o in layers[layer_index].instances if o.id.instance == instance]
        if len(matches) != 1:
            raise ValueError(f"Missing or ambiguous pickup scan actor for location {row['index']}")
        actor = matches[0]
        # Walk only the known ActorParameters -> ScannableParameters path.
        root = dict(properties(actor._raw.base_property))
        actor_fields = properties(b'\xff'*4 + len(root[0x7E397FED]).to_bytes(2, 'big') + root[0x7E397FED])
        nested = dict(actor_fields)[0x375BFD7C]
        scan_fields = properties(b'\xff'*4 + len(nested).to_bytes(2, 'big') + nested)
        if len(dict(scan_fields).get(SCAN_FIELD, b'')) != 8:
            raise ValueError(f"Unsupported pickup scan field at location {row['index']}")
        assets = template.create(row)
        scan_id = assets[0].identity
        def rewrite(data, field, value):
            return replace_properties(b'\xff'*4 + len(data).to_bytes(2, 'big') + data, {field: value})[6:]
        nested = rewrite(nested, SCAN_FIELD, scan_id.to_bytes(8, 'big'))
        actor_data = rewrite(root[0x7E397FED], 0x375BFD7C, nested)
        actor._raw.base_property = replace_properties(actor._raw.base_property, {0x7E397FED: actor_data})
        deps = area.get_section('dependencies_section')[0]
        existing = {d.asset_id for d in deps.dependencies[deps.offsets[layer_index]:deps.offsets[layer_index+1]]}
        new = [Container(asset_id=r.identity, type=r.kind.decode()) for r in assets if r.identity not in existing]
        deps.dependencies[deps.offsets[layer_index+1]:deps.offsets[layer_index+1]] = new
        for i in range(layer_index+1, len(deps.offsets)):
            deps.offsets[i] += len(new)
        additions.update((r.identity, r) for r in assets)
        layers[layer_index].mark_modified()
        records.append({'location': row['index'], 'actor': int(actor.id), 'label': label(row), 'scan': scan_id})
    encoded = area.build()
    check = SeedMrea.parse(encoded, Game.CORRUPTION)
    actual = {int(o.id): o._raw.base_property for l in check.script_layers for o in l.instances}
    changed = {r['actor'] for r in records}
    if actual.keys() != originals.keys() or any(actual[k] != v for k, v in originals.items() if k not in changed):
        raise ValueError('Pickup scan patch changed unrelated actors or object counts')
    return encoded, list(additions.values()), records


def install(files, output, patch_data):
    rows = scan_rows(patch_data)
    bindings = visual_bindings([{**r, 'game': 'prime1'} for r in rows])
    template = ScanTemplate(files)
    output.mkdir(exist_ok=False)
    remaining = {k[0] for k in bindings}
    report = {'actors': [], 'archives': {}, 'addedObjects': 0,
              'scriptedLocationsWithoutVisualActor': sorted({r['index'] for r in rows} -
                                                          {r[0]['index'] for r in bindings.values()})}
    for path in sorted(Path(files).glob('*.pak')):
        archive = Archive(path)
        targets = {r.identity for r in archive.resources if r.kind == b'MREA'} & remaining
        if not targets:
            continue
        resources, added = [], {}
        for resource in archive.resources:
            if resource.identity in targets:
                raw, assets, records = patch_area(resource.read(), resource.identity, bindings, template)
                resources.append(resource.updated(raw))
                added.update((r.identity, r) for r in assets)
                report['actors'].extend(records)
            else:
                resources.append(resource)
        existing = {r.identity: r for r in resources}
        for identity, resource in added.items():
            if identity in existing:
                if resource.kind != existing[identity].kind or resource.read() != existing[identity].read():
                    raise ValueError('Pickup scan resource identity collision')
            else:
                resources.append(resource)
        destination = output / path.name
        archive.write(destination, resources)
        actual = Archive(destination).resources
        if len(actual) != len(resources) or any(a.identity != b.identity or a.kind != b.kind or
                a.compressed != b.compressed or a.read() != b.read() for a, b in zip(actual, resources, strict=True)):
            raise ValueError('Pickup scan archive readback mismatch')
        report['archives'][path.name] = str(destination)
        remaining -= targets
    if remaining:
        raise ValueError(f'Missing pickup scan areas: {sorted(remaining)}')
    (output / 'report.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    return report
