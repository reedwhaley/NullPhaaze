# RDS owns resource framing while the established recipes own behavior. Preserve opaque
# sections, native string ordering and layer dependency slices around the targeted edits.
# Boundary names here: add_dependencies, patch_mrea, patch_world, make_string_table,
# patch_tweaks.
"""RDS resource framing with explicit compatibility-preserving game edits."""
import construct as cs
from retro_data_structures.formats.mrea import _CATEGORY_ENCODINGS
from retro_data_structures.formats.strg import STRG_V3
from .binary import FormatError, pad
from .scripts import apply_layer
from .rds_formats import GAME, MREA, MLVL, parse_exact, read_world


def add_dependencies(data, dependencies):
    schema = _CATEGORY_ENCODINGS['dependencies_section']
    raw = parse_exact(schema, data)
    # Append to the common tail; the existing per-layer offsets stay intact.
    raw.dependencies.extend(cs.Container(asset_id=item['file_id'],
        type=item['resource_type'].decode('ascii')) for item in dependencies
        if item['resource_type'] != b'STRM')
    return schema.build(raw, target_game=GAME)


def patch_mrea(data, identity, area_index, plan, codec, evaluator):
    try:
        raw = parse_exact(MREA, data)
        if int(raw.version) != 30:
            raise FormatError('Expected Corruption MREA version 30')
        known_categories = set(MREA._get_categories(raw.version))
        if set(raw.header.section_index) - known_categories:
            raise FormatError('Unknown MREA section category; refusing to discard its identity')
        layers = raw.raw_sections.get('script_layers_section')
        deps = raw.raw_sections.get('dependencies_section')
        if layers is None or deps is None:
            raise FormatError('Required MREA section index missing')
        for index, layer in enumerate(layers):
            layers[index] = apply_layer(layer, plan, identity, area_index, evaluator)
        additions = plan['dependency_patches'].get(str(identity), [])
        if additions:
            deps[0] = add_dependencies(deps[0], additions)
        return pad(MREA.build(raw, target_game=GAME), 64, 255)
    except (cs.ConstructError, ValueError, KeyError, IndexError, AssertionError) as error:
        raise FormatError(f'RDS could not patch MREA {identity:016X}: {error}') from error


def patch_world(data, identity, operations):
    raw, envelope = read_world(data)
    for operation in operations:
        if operation['mlvl_id'] != identity:
            continue
        index = operation['area_index']
        if not 0 <= index < len(raw.area_layer_flags):
            raise FormatError('World-layer rule targets a missing area')
        flags = raw.area_layer_flags[index]
        for state, key in ((True, 'bits_to_activate'), (False, 'bits_to_deactivate')):
            for bit in operation[key]:
                if not 0 <= bit < 64:
                    raise FormatError('Layer bit exceeds 64-bit mask')
                flags.original[bit] = state
                if bit < len(flags):
                    flags[bit] = state
    return pad(MLVL.build(raw, target_game=GAME) + b'\xff' * envelope, 64, 255)


def make_string_table(strings):
    # Keep every occurrence in forward order. The native STRG loader streams
    # these records; RDS's general Strg writer deduplicates repeated strings
    # into backward offsets, which already caused a frontend crash here.
    strings = list(strings)
    offsets, offset = [], 0
    for text in strings:
        offsets.append(offset)
        offset += 4 + len(text.encode('utf-8')) + 1
    raw = cs.Container(header=cs.Container(version='prime3', language_count=1,
        string_count=len(strings)), name_table={}, language_ids=['ENGL'],
        language_table=[cs.Container(strings_size=sum(len(s.encode('utf-8'))+1 for s in strings),
                                     string_offsets=offsets)], strings=strings)
    built = STRG_V3.build(raw, target_game=GAME)
    logical = 32 + 4 * len(strings) + offset
    return pad(built[:logical], 64, 255)


def patch_tweaks(data, evaluator):
    from retro_data_structures.formats.ntwk import Ntwk
    # NTWK is a script container too. Resolve the tweak through its generated
    # property schema instead of finding a matching four-byte sequence.
    obj = Ntwk.parse(data, GAME)
    rule = [{'property_id': bytes.fromhex('19686BF6'), 'property_value':
             {'kind': 'BPropertyValue', 'value': bytes.fromhex('42200000')}}]
    for instance in obj.raw.script_instances:
        instance.base_property = evaluator.properties_for(instance.type, instance.base_property, rule)
    return obj.build()
