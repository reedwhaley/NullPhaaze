"""New layout, inventory and rule-composition planner. No managed dependency."""
from dataclasses import dataclass
import hashlib
import re
from functools import lru_cache
from .binary import FormatError
from .rules import catalog, decode, recipe, empty_plan, merge, instantiate


@dataclass(frozen=True)
class Options:
    layout: str
    inventory: str = 'original-with-command'
    start: str = 'norion'
    world: int = 0
    area: int = 0
    require_launcher: bool = False
    require_ship_missile: bool = False
    hyper_hints: bool = False
    fast_flying: bool = False
    phaaze_skip: bool = False
    random_door_colors: bool = False
    random_welding_colors: bool = False


def decode_layout(text):
    data = catalog()
    alphabet = data['alphabet']
    if not isinstance(text, str) or not 7 <= len(text) <= 107:
        raise FormatError('Layout must encode exactly 100 placements')
    body, checksum = text[:-5], text[-5:]
    if not re.fullmatch('[0-9a-fA-F]{5}', checksum) or any(ch not in alphabet for ch in body):
        raise FormatError('Invalid layout alphabet or checksum')
    if hashlib.sha256(body.encode('ascii')).hexdigest()[:5].lower() != checksum.lower():
        raise FormatError('Layout checksum mismatch')
    rotation, step = map(alphabet.index, body[:2])
    result = []
    for character in body[2:]:
        token = alphabet[(alphabet.index(character)-rotation) % len(alphabet)]
        if token not in data['tokens']:
            raise FormatError(f'Unsupported layout token: {token}')
        result.extend(data['tokens'][token])
        if len(result) > 100:
            raise FormatError('Layout exceeds 100 placements')
        rotation = (rotation+step) % len(alphabet)
    if len(result) != 100:
        raise FormatError('Layout must encode exactly 100 placements')
    return result


def inventory_values(text):
    data = catalog()
    if text == 'original-with-command':
        return decode(data['originalInventory'])
    if text == 'post-norion-no-lasso':
        return decode(data['postNorionInventory'])
    if not re.fullmatch('[0-9a-fA-F]{43}', text):
        raise FormatError('Custom starting inventory must contain 43 hexadecimal characters')
    result = {binding['field']: 0 for binding in data['inventoryBindings']}
    for position, slot in data['customInventoryPositions'].items():
        result[slot['field']] += int(text[int(position)], 16)*slot['weight']
    for binding in data['inventoryBindings']:
        if binding['boolean']:
            result[binding['field']] = result[binding['field']] == 1
    return result


def starting_ids(options):
    starts = {'olympus': (4010992506757754735, 3586057064387876334),
              'norion': (8050447300094575427, 1594033074927626820),
              'valhalla': (0xC133F919C108BDF9, 0xD8CF355D3E9E3741)}
    if options.start == 'custom':
        if not 0 <= options.world < 2**64 or not 0 <= options.area < 2**64:
            raise FormatError('Custom start IDs must fit 64 bits')
        return options.world, options.area
    try:
        return starts[options.start]
    except KeyError as error:
        raise FormatError('Unsupported starting location') from error


@lru_cache(maxsize=1)
def dependency_graph():
    return decode(catalog()['dependencies'])


@lru_cache(maxsize=None)
def dependency_closure(identity, kind):
    graph = dependency_graph()
    result = [{'file_id': identity, 'resource_type': kind, 'kind': 'Dependency'}]
    seen = {identity}
    for entry in result:
        try:
            children = graph[str(entry['file_id'])]
        except KeyError as error:
            raise FormatError(f"Unknown dependency {entry['file_id']:016X}") from error
        for child in children:
            if child['file_id'] not in seen:
                seen.add(child['file_id'])
                result.append(child)
    return result


@lru_cache(maxsize=None)
def item_dependencies(item_index, physical):
    item = presentation_item(item_index)
    roots = [('streamed_audio', b'STRM'), ('memo', b'STRG')]
    if physical:
        roots += [('model', b'CMDL'), ('pickup_effect', b'PART'), ('character', b'CHAR'), ('scan', b'SCAN')]
    result, seen = [], set()
    for field, kind in roots:
        identity = int.from_bytes(item[field], 'big')
        if identity == 2**64-1:
            continue
        for entry in dependency_closure(identity, kind):
            if entry['file_id'] not in seen:
                seen.add(entry['file_id'])
                result.append(entry)
    return result


def presentation_item(item_index):
    """Correct the ship pickup visuals without changing recovered grants/text."""
    data = catalog()
    item = decode(data['items'][item_index])
    other = {
        'ShipMissile': 'ShipMissileExpansion',
        'ConverterShipMissile': 'ShipMissileExpansion',
        'ShipMissileExpansion': 'ShipMissile',
        'MainRequiredShipMissileExpansion': 'ShipMissile',
    }.get(data['itemNames'][item_index])
    if other is not None:
        visual = decode(data['items'][data['itemNames'].index(other)])
        for field in ('model', 'character', 'default_animation'):
            item[field] = visual[field]
    return item


def correct_ship_presentation(addition, item_index, *, fake=False):
    original = decode(catalog()['items'][item_index])
    visual = presentation_item(item_index)
    if original['character'] == visual['character']:
        return
    before = original['character'] + original['default_animation']
    after = visual['character'] + visual['default_animation']
    changed = 0
    for operation in addition['object_modification_patches']:
        for prop in operation['property_modifications']:
            if prop['property_id'] == bytes.fromhex('A244C9D8'):
                value = prop['property_value']
                if value.get('kind') == 'BPropertyValue' and value.get('value') == before:
                    value['value'] = after
                    changed += 1
    if fake and changed:
        old = {d['file_id'] for d in dependency_closure(int.from_bytes(original['character'], 'big'), b'CHAR')}
        new = dependency_closure(int.from_bytes(visual['character'], 'big'), b'CHAR')
        for area, dependencies in addition['dependency_patches'].items():
            # Shared scan/effect resources can still need part of the old closure.
            protected = set()
            for dep in dependencies:
                if dep['file_id'] not in old:
                    protected.update(d['file_id'] for d in dependency_closure(dep['file_id'], dep['resource_type']))
            retained = [d for d in dependencies if d['file_id'] not in old or d['file_id'] in protected]
            seen = {d['file_id'] for d in retained}
            retained.extend(d for d in new if d['file_id'] not in seen)
            addition['dependency_patches'][area] = dependency_order(retained)


def dependency_order(requested):
    graph = dependency_graph()
    types = {}
    for dependency in requested:
        identity, kind = dependency['file_id'], dependency['resource_type']
        if identity in types and types[identity] != kind:
            raise FormatError('Conflicting dependency types')
        types[identity] = kind
    pending = {dependency['file_id']: dependency for dependency in requested}
    ordered, ready = [], set()
    while pending:
        progress = False
        for identity, dependency in list(pending.items()):
            if str(identity) not in graph:
                raise FormatError(f'Unknown dependency {identity:016X}')
            prerequisites = {item['file_id'] for item in graph[str(identity)] if item['file_id'] != identity}
            if prerequisites <= ready:
                ordered.append(dependency)
                ready.add(identity)
                del pending[identity]
                progress = True
        if not progress:
            raise FormatError('Dependency cycle or missing prerequisite')
    return ordered


def build_plan(options, placements=None):
    data = catalog()
    items = list(decode_layout(options.layout) if placements is None else placements)
    if len(items) != 100 or any(type(item) is not int or not 0 <= item < 44 for item in items):
        raise FormatError('Expected 100 supported item IDs')
    names = data['itemNames']
    transforms = {}
    if options.require_launcher:
        transforms.update(MissileExpansion='MainRequiredMissileExpansion', MissileLauncher='ConverterMissileLauncher')
    if options.require_ship_missile:
        transforms.update(ShipMissileExpansion='MainRequiredShipMissileExpansion', ShipMissile='ConverterShipMissile')
    items = [names.index(transforms[names[item]]) if names[item] in transforms else item for item in items]
    world, area = starting_ids(options)
    plan = empty_plan()
    statics = data['static']
    def add_static(name):
        merge(plan, recipe(statics[name]))
    add_static('FrontEndPatches.patch_attract_videos')
    reveal = data['specialRevealTemplate'] if area in data['specialRevealAreas'] else data['revealTemplate']
    merge(plan, instantiate(recipe(reveal), area, world))
    inv = instantiate(recipe(data['inventoryTemplate']), area, world)
    values = inventory_values(options.inventory)
    modifications = inv['object_modification_patches'][0]['property_modifications']
    for binding in data['inventoryBindings']:
        for slot in binding['slots']:
            target = modifications[slot['property']]['property_value']
            raw = int(values[binding['field']]).to_bytes(slot['size'], 'big')
            if target['kind'] == 'RepeatPropertyValue':
                target['property_values'][slot['part']] = raw
            else:
                target['value'] = raw
    merge(plan, inv)
    merge(plan, instantiate(recipe(data['locationTemplate']), area, world))
    excluded = {'FrontEndPatches.patch_attract_videos', 'PickupPatches.add_special_pickup_patches'}
    conditional = {'NorionPatches.add_control_tower_norion_layer_change_patches': options.start != 'olympus',
                   'GeneralPatches.add_fast_flying_patches': options.fast_flying,
                   'GeneralPatches.add_phaaze_skip_patches': options.phaaze_skip,
                   'CosmeticPatches.add_random_door_color_patch': False,
                   'CosmeticPatches.add_context_welding_color_patch': False}
    for name in statics:
        if name not in excluded and conditional.get(name, True):
            add_static(name)
    flags = int(options.require_launcher)+2*int(options.require_ship_missile)
    seen = set()
    # Location ordering is a rule-table fact, not the archive or room order.
    for index in sorted(range(100), key=lambda i: data['pickups'][i]['item_index']):
        addition = recipe(data['pickupRecipes'][index][items[index]][flags])
        correct_ship_presentation(addition, items[index])
        for identity in addition['dependency_patches']:
            addition['dependency_patches'][identity] = item_dependencies(items[index], data['pickups'][index]['type'] == 'Pickup')
        item = decode(data['items'][items[index]])
        converter_ids = {tuple(item.get(key) or ()) for key in ('conversion_start_ids', 'conversion_end_ids')}
        retained = []
        for operation in addition['object_addition_patches']:
            ids = tuple(obj['id'] for obj in operation['script_objects'])
            identity = (tuple(operation['mrea_ids']), tuple(operation['layer_indexes']), ids)
            if any(values and ids == values[:len(ids)] for values in converter_ids):
                if identity in seen:
                    continue
                seen.add(identity)
            retained.append(operation)
        addition['object_addition_patches'] = retained
        merge(plan, addition)
        for identity in addition['dependency_patches']:
            plan['dependency_patches'][identity] = dependency_order(plan['dependency_patches'][identity])
    for index, pickup in enumerate(data['fakePickups']):
        addition = recipe(data['fakeRecipes'][index][items[pickup['item_index']]])
        correct_ship_presentation(addition, items[pickup['item_index']], fake=True)
        merge(plan, addition)
    add_static('PickupPatches.add_special_pickup_patches')
    if options.random_door_colors:
        add_static('CosmeticPatches.add_random_door_color_patch')
    if options.random_welding_colors:
        add_static('CosmeticPatches.add_context_welding_color_patch')
    return plan, items


def planet(index):
    if index < 0: return 'an unknown location.'
    if index <= 2: return 'Olympus'
    if index <= 10: return 'Norion'
    if index <= 16: return 'Valhalla'
    if index <= 50 or index == 98: return 'Bryyo'
    if index <= 74 or index == 97: return 'Elysia'
    return 'the Pirate Homeworld'
