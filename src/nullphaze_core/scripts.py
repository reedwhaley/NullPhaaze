# The compatibility records preserve the existing patch API while RDS frames layers and
# resolves property fields. Keep connection order and untouched raw property bytes intact.
# Boundary names here: Connection, Instance, Evaluator, parse_layer, encode_layer.
"""Bounded script records and declarative operations, authored for NullPhaaze."""
from dataclasses import dataclass
from .binary import Reader, FormatError, pad, pack
from .rds_scripts import RdsEvaluator


@dataclass
class Connection:
    state: str
    message: str
    target: int


@dataclass
class Instance:
    kind: str
    identity: int
    connections: list
    properties: bytes


from .rule_values import selected


class Evaluator(RdsEvaluator):
    """Compatibility name for the schema-resolved evaluator used by exports."""


def parse_layer(data):
    from .rds_formats import SCRIPT_LAYER, parse_exact
    raw = parse_exact(SCRIPT_LAYER, data, padding=(0,))
    objects = [Instance(obj.type, int(obj.id) & 0xFFFF,
        [Connection(c.state.value, c.message.value, int(c.target) & 0xFFFF)
         for c in obj.connections], obj.base_property) for obj in raw.script_instances]
    return data[:10], objects


def encode_layer(header, objects, area_index):
    import construct as cs
    from retro_data_structures.formats.script_object import ScriptInstanceRaw, InstanceId
    from retro_data_structures.formats.script_object import Connection as RdsConnection
    from .rds_formats import SCRIPT_LAYER, Signal, GAME
    if len(header) != 10 or not 0 <= area_index <= 255 or header[8] > 63:
        raise FormatError('Script instance address exceeds supported bit fields')
    instances = []
    for instance in objects:
        if len(instance.kind) != 4 or not 0 <= instance.identity <= 65535:
            raise FormatError('Invalid script object identity')
        links = []
        for c in instance.connections:
            if len(c.state) != 4 or len(c.message) != 4 or not 0 <= c.target <= 65535:
                raise FormatError('Invalid script connection')
            links.append(RdsConnection(Signal(c.state), Signal(c.message),
                InstanceId.new(0, area_index, c.target)))
        instances.append(ScriptInstanceRaw(instance.kind,
            InstanceId.new(header[8], area_index, instance.identity), tuple(links), instance.properties))
    raw = cs.Container(unknown=header[4], layer_index=int.from_bytes(header[5:9], 'big'),
        script_instances=instances)
    try:
        return pad(SCRIPT_LAYER.build(raw, target_game=GAME), 32)
    except (cs.ConstructError, ValueError, AssertionError) as error:
        raise FormatError(f'RDS could not build script layer: {error}') from error


def apply_layer(data, plan, area_id, area_index, evaluator):
    if data[:4] == b'SGEN':
        return data
    header, objects = parse_layer(data)
    layer = header[8]
    plan = {key: [rule for rule in values if selected(rule, area_id, layer)]
            for key, values in plan.items() if key != 'dependency_patches'}
    if any(selected(rule, area_id, layer) for rule in plan['layer_clear_patches']):
        objects = []
    objects = [obj for obj in objects if not any(selected(rule, area_id, layer, obj) for rule in plan['object_deletion_patches'])]
    for rule in plan['object_addition_patches']:
        if selected(rule, area_id, layer):
            for obj in rule['script_objects']:
                objects.append(Instance(obj['type'], obj['id'],
                    [Connection(c['state'], c['message'], c['target']) for c in obj['connections']], obj['script_data']))
    for obj in objects:
        for rule in plan['object_modification_patches']:
            if selected(rule, area_id, layer, obj):
                obj.properties = evaluator.properties_for(obj.kind, obj.properties, rule['property_modifications'])
    for obj in objects:
        obj.connections = [connection for connection in obj.connections if not any(
            selected(rule, area_id, layer, obj, connection) for rule in plan['connection_deletion_patches'])]
    for obj in objects:
        for rule in plan['connection_addition_patches']:
            if selected(rule, area_id, layer, obj):
                obj.connections.extend(Connection(c['state'], c['message'], c['target']) for c in rule['connections'])
    for obj in objects:
        for rule in plan['connection_modification_patches']:
            for connection in obj.connections:
                if selected(rule, area_id, layer, obj, connection):
                    # Existing exported behavior retains the original signal
                    # tags in the two rewiring rules; only their target changes.
                    # Changing those tags requires a separate gameplay decision.
                    if rule['new_target']:
                        connection.target = rule['new_target'][0]
    return encode_layer(header, objects, area_index)
