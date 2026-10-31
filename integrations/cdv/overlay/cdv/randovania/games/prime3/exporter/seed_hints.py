# Seed-aware Valhalla cell reports and Leviathan reward scans. Boundary names here:
# create_hint_data, validate_data, cell_text, core_text, text_resource.
"""Seed-aware Valhalla cell reports and Leviathan reward scans.

Data is resolved from canonical assignments, never the visual core layout.
No inventory, scan-completion, story, networking or polling scripts are added.
"""
from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path


from randovania.games.prime3.exporter.hint_text import _safe, label
from randovania.games.prime3.layout.hint_mode import CoreHintMode, HintMode, mode_for

CELL_STRINGS = {1:0x3E34A6A6C1261851, 2:0xC4816CC9408123D4, 3:0xEDFC15CF2776AEF2,
                4:0xD87C81AEE6B84424, 5:0xE1E10144127D531F, 6:0x60F6FAF4F96C4B16,
                7:0xE904C4C6AC7E8FA9, 8:0xB975321B8FBF8919, 9:0x88E668817A8CABC5}
CORE_NAMES = {98:'Bryyo', 97:'Elysian', 99:'Pirate Homeworld'}
# Reuse native, decorative scans. Generator online/offline and shield states
# all receive the same Bryyo reward; no progression consoles are replaced.
CORE_TARGETS = {
    0xF8AEE2471CB5F3AF:(98, (0x000E017F,0x000E0138,0x100E0254,0x000E031A,
                              0x140E0317,0x180E0316,0x180E0319,0x300E02BE)),
    0x6535F6B9FFA0D92E:(97, (0x001B00AC,)),
    0xE371C3D7E0937DA5:(99, (0x0007042C,0x0007042D)),
}
LANGUAGES = ('ENGL','JAPN','GERM','FREN','SPAN','ITAL')


def create_hint_data(factory):
    from randovania.game_description.resources.pickup_index import PickupIndex
    from randovania.games.prime3.exporter.item_location_hints import placement_text
    config = factory.players_config
    own = config.player_index
    cell_mode = mode_for(factory, 'energy_cell_hint')
    configuration = getattr(factory.description.get_preset(own), 'configuration', None)
    core_mode = getattr(configuration, 'core_hint', CoreHintMode.ITEM)
    cells = {str(i):[] for i in range(1,10)}
    for resource, quantity in factory.patches.starting_resources().as_resource_gain():
        if quantity > 0 and resource.short_name in {f'Fuse{i}' for i in range(1,10)}:
            cells[resource.short_name[4:]].append('your starting inventory')
    for provider, patches in sorted(factory.description.all_patches.items()):
        for index, target in sorted(patches.pickup_assignment.items(),key=lambda x:x[0].index):
            if target.player != own:
                continue
            # Distinguish all nine native resources, even if display names/models
            # are identical or the cell is located in a Prime/Echoes world.
            resources = {r.short_name for r,n in (*target.pickup.progression,*target.pickup.extra_resources) if n > 0}
            selected = [i for i in range(1,10) if f'Fuse{i}' in resources]
            if selected:
                location = placement_text(factory,provider,index,detailed=cell_mode == HintMode.AREA)
                for i in selected:
                    cells[str(i)].append(_safe(location))
    cores = {}
    for index in CORE_NAMES:
        target = factory.patches.pickup_assignment.get(PickupIndex(index))
        if target is None:
            # Match the exporter's defined empty-slot behavior: multiworld
            # neutralizes it as Nothing, while the legacy solo core uses Missile.
            cores[str(index)] = {'item_name':'Nothing' if config.is_multiworld else 'Missile Expansion',
                                 'local':True,'recipient_name':config.player_names[own]}
        else:
            cores[str(index)] = {'item_name':target.pickup.name,
                                'local':target.player == own,
                                'recipient_name':config.player_names[target.player]}
        if core_mode == CoreHintMode.CATEGORY:
            if target is not None:
                category = target.pickup.gui_category.long_name
            else:
                from randovania.game.game_enum import RandovaniaGame
                from randovania.game_description import default_database
                from randovania.generator.pickup_pool.pickup_creator import create_nothing_pickup
                game = RandovaniaGame.METROID_PRIME_CORRUPTION
                if config.is_multiworld:
                    category = create_nothing_pickup(default_database.resource_database_for(game)).gui_category.long_name
                else:
                    category = default_database.pickup_database_for_game(game).ammo_pickups['Missile Expansion'].gui_category.long_name
            cores[str(index)]['item_name'] = _safe(category)
    if cell_mode == HintMode.DISABLED:
        cells = {str(i): None for i in range(1,10)}
    if core_mode == CoreHintMode.DISABLED:
        cores = {key: None for key in cores}
    data = {'schema':1, 'cells':cells, 'cores':cores}
    validate_data(data)
    return data


def validate_data(data):
    if not isinstance(data,dict) or data.get('schema') != 1:
        raise ValueError('Unsupported seed hint data; regenerate export data from the matching seed')
    if set(data.get('cells',{})) != {str(i) for i in range(1,10)} or set(data.get('cores',{})) != {'97','98','99'}:
        raise ValueError('Seed hints require nine cells and all three Leviathan reward assignments')
    for places in data['cells'].values():
        if places is None:
            continue
        if not isinstance(places,list) or len(places)>100:
            raise ValueError('Invalid Energy Cell hint placements')
        for place in places:
            _safe(place)
    for row in data['cores'].values():
        if row is not None:
            label(row)


def cell_text(index, places):
    if places is None:
        return 'No hint available.'
    if not places:
        return f'Energy Cell {index} is not placed in this seed.'
    return f"Energy Cell {index} is in {'; '.join(_safe(p) for p in places)}."


def core_text(index,row):
    return f'{CORE_NAMES[index]} Leviathan Core reward:\n{label(row)}'


def text_resource(identity, texts, names=None):
    from construct import Container
    from nullphaze_core.archives import Resource
    from retro_data_structures.formats.strg import Strg
    from retro_data_structures.game_check import Game
    from randovania.games.prime3.exporter.main_menu import build_sequential_strings
    table = Strg(Container(languages={lang:list(texts) for lang in LANGUAGES},name_table=names or {}),Game.CORRUPTION)
    return Resource(identity,b'STRG',0,0).updated(build_sequential_strings(table))


def private_scan(scan, strings, text):
    from nullphaze_core.archives import Resource
    from retro_data_structures.formats.strg import Strg
    from retro_data_structures.game_check import Game
    from randovania.games.prime3.exporter.main_menu import _decoded, build_sequential_strings
    raw = bytearray(_decoded(scan))
    namespace = f'NullPhaaze core hint v2/{scan.identity:016X}/{text}'
    scan_id,text_id = [int.from_bytes(hashlib.sha256((namespace+s).encode()).digest()[:8],'big')
                       for s in ('/SCAN','/STRG')]
    marker = bytes.fromhex('2F5B64230008') + strings.identity.to_bytes(8,'big')
    if raw.count(marker) != 1:
        raise ValueError('Core hint SCAN string field differs from the supported native format')
    offset = raw.index(marker)+6
    raw[offset:offset+8] = text_id.to_bytes(8,'big')
    dep = 19+int.from_bytes(raw[17:19],'big')
    count = 0
    for i in range(struct.unpack_from('>I',raw,dep)[0]):
        offset=dep+4+12*i
        if raw[offset:offset+12] == b'STRG'+strings.identity.to_bytes(8,'big'):
            raw[offset+4:offset+12]=text_id.to_bytes(8,'big'); count+=1
    if count != 1:
        raise ValueError('Core hint SCAN has an unexpected native string dependency')
    # Replace every scan/logbook slot with only the randomized reward hint.
    table = Strg.parse(_decoded(strings),Game.CORRUPTION)
    if any(len(table.get_strings(lang)) != 3 for lang in table.get_language_list()):
        raise ValueError('Core hint expects a native three-slot scan STRG')
    for lang in table.get_language_list():
        table.set_string_list([text]*3,lang)
    return (Resource(scan_id,b'SCAN',0,0).updated(bytes(raw)),
            Resource(text_id,b'STRG',0,0).updated(build_sequential_strings(table)))


def install(files,output,data):
    from construct import Container
    from nullphaze_core.archives import Archive
    from nullphaze_network.prime3_lua_service.mrea_build import SeedMrea
    from nullphaze_network.prime3_lua_service.probe import properties, replace_properties
    from retro_data_structures.game_check import Game
    from randovania.games.prime3.exporter.main_menu import _decoded
    validate_data(data)
    output=Path(output); output.mkdir(exist_ok=False)
    report={'archives':{},'cells':[],'cores':[],'addedObjects':0,'gameplayVerified':False}
    remaining=set(CORE_TARGETS)
    found_cells=set()
    # Logbook carries a second copy of every cell report. Patch it as well as
    # the room archive so revisiting the entry cannot restore vanilla text.
    for name in ('Metroid1.pak','Metroid3.pak','Metroid4.pak','Metroid5.pak','Logbook.pak'):
        archive=Archive(Path(files)/name)
        lookup={r.identity:r for r in archive.resources}
        additions={}; replacements={}
        for i,identity in CELL_STRINGS.items():
            if identity in lookup:
                if lookup[identity].kind != b'STRG':
                    raise ValueError('Energy Cell bot resource has unexpected type')
                text=cell_text(i,data['cells'][str(i)])
                replacements[identity]=text_resource(identity,(text,text,text))
                found_cells.add(i)
                report['cells'].append({'cell':i,'archive':name,'string':f'{identity:016X}','text':text})
        for identity,(index,ids) in CORE_TARGETS.items():
            if identity not in lookup: continue
            if data['cores'][str(index)] is None:
                remaining.discard(identity)
                continue
            area=SeedMrea.parse(lookup[identity].read(),Game.CORRUPTION)
            actors={int(a.id):(li,a) for li,l in enumerate(area.script_layers) for a in l.instances}
            for key in ids:
                if key not in actors or actors[key][1].type_name != 'POIN':
                    raise ValueError(f'Core hint native scan actor {key:08X} is missing in {name}; unsupported source')
                li,actor=actors[key]
                props=actor.get_properties()
                scan=lookup[props.scan_info.scannable_info0]
                scan_raw=_decoded(scan); dep=19+int.from_bytes(scan_raw[17:19],'big')
                texts=[int.from_bytes(scan_raw[dep+8+12*i:dep+16+12*i],'big')
                       for i in range(struct.unpack_from('>I',scan_raw,dep)[0])
                       if scan_raw[dep+4+12*i:dep+8+12*i]==b'STRG']
                if len(texts)!=1: raise ValueError('Core hint native scan must have one STRG')
                assets=private_scan(scan,lookup[texts[0]],core_text(index,data['cores'][str(index)]))
                # Change only the scan resource reference, leaving all native
                # trigger/visibility/progression behavior and properties intact.
                root=dict(properties(actor._raw.base_property)); nested=root[3183395477]
                wrapped=b'\xff'*4+len(nested).to_bytes(2,'big')+nested
                rewritten=replace_properties(wrapped,{0xB94E9BE7:assets[0].identity.to_bytes(8,'big')})[6:]
                actor._raw.base_property=replace_properties(actor._raw.base_property,{3183395477:rewritten})
                list(area.script_layers)[li].mark_modified()
                deps=area.get_section('dependencies_section')[0]
                pos=deps.offsets[li+1]
                deps.dependencies[pos:pos]=[Container(asset_id=r.identity,type=r.kind.decode()) for r in assets]
                for j in range(li+1,len(deps.offsets)):deps.offsets[j]+=len(assets)
                additions.update((r.identity,r) for r in assets)
                report['cores'].append({'index':index,'area':f'{identity:016X}','actor':f'{key:08X}',
                                        'text':core_text(index,data['cores'][str(index)])})
            replacements[identity]=lookup[identity].updated(area.build()); remaining.discard(identity)
        resources=[replacements.get(r.identity,r) for r in archive.resources]
        for identity,r in additions.items():
            if identity in lookup:raise ValueError('Core hint resource ID collision')
            resources.append(r)
        destination=output/name
        archive.write(destination,resources)
        actual=Archive(destination).resources
        if len(actual)!=len(resources) or any(a.identity!=b.identity or a.kind!=b.kind or a.read()!=b.read()
                                             for a,b in zip(actual,resources,strict=True)):
            raise ValueError('Seed hint archive readback mismatch')
        report['archives'][name]=str(destination)
    if remaining or found_cells!=set(range(1,10)):
        raise ValueError('Seed hints are missing one or more native bot/core resources')
    (output/'report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    return report
