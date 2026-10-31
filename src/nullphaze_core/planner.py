# Recipe order determines the final value when edits meet on one object. I keep item grants,
# visual selection, dependency closure and starting-state options distinct while assembling
# the plan. Boundary names here: Options, decode_layout, inventory_values, starting_ids,
# dependency_graph.
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
    exclude_olympus: bool = False
    retain_space_assets: bool = False


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
    if options.exclude_olympus and (options.start == 'olympus' or
                                    (options.start == 'custom' and options.world == starts['olympus'][0])):
        raise FormatError('G.F.S. Olympus cannot be a starting location')
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
    """Use the catalog's native visuals, including both ship missile variants."""
    return decode(catalog()['items'][item_index])


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
    if options.exclude_olympus:
        # No converters or progressive grant relays may be created in Olympus.
        items[:3] = [names.index('ScanVisor')] * 3
    world, area = starting_ids(options)
    plan = empty_plan()
    statics = data['static']
    def add_static(name):
        merge(plan, recipe(statics[name]))
    from .patches.frontend import apply_frontend
    apply_frontend(add_static)
    from .patches.starting_items import apply_start
    apply_start(plan, data, options, area, world, inventory_values)
    from .patches.worlds import apply_worlds
    apply_worlds(options, statics, add_static)
    from .patches.pickups import apply_pickups
    apply_pickups(plan, data, items, options, item_dependencies, dependency_order)
    if options.exclude_olympus:
        # Index 0 is the virtual introductory grant and has no physical recipe.
        # Keep native actors/links intact, but hide and neutralize the two pickups.
        for index in (1, 2):
            pickup = data['pickups'][index]
            plan['object_modification_patches'].append({
                'mrea_ids': [pickup['mrea_id']], 'layer_indexes': [pickup['scly_section']],
                'object_ids': [int(pickup['instance_id']['$bytes'], 16)], 'script_types': ['PCKP'],
                'property_modifications': [
                    {'property_id': field.to_bytes(4, 'big'),
                     'property_value': {'kind': 'BPropertyValue', 'value': value}}
                    for field, value in ((0x41435456, b'\0'), (0x28C71B54, bytes(4)),
                                         (0x94AF1445, bytes(4)), (0x165AB069, bytes(4)))]})
    for index, pickup in enumerate(data['fakePickups']):
        addition = recipe(data['fakeRecipes'][index][items[pickup['item_index']]])
        merge(plan, addition)
    add_static('PickupPatches.add_special_pickup_patches')
    from .patches.cosmetics import apply_cosmetics
    apply_cosmetics(options, add_static)
    return plan, items


def planet(index):
    if index < 0: return 'an unknown location.'
    if index <= 2: return 'Olympus'
    if index <= 10: return 'Norion'
    if index <= 16: return 'Valhalla'
    if index <= 50 or index == 98: return 'Bryyo'
    if index <= 74 or index == 97: return 'Elysia'
    return 'the Pirate Homeworld'
