"""Bounded script records and declarative operations, authored for NullPhaaze."""
from dataclasses import dataclass
import random
import struct
from .binary import Reader, FormatError, pad, pack


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


def selected(operation, area, layer, instance=None, connection=None):
    criteria = [('mrea_ids', area), ('layer_indexes', layer)]
    if instance is not None:
        criteria += [('script_types', instance.kind),
                     ('source_object_ids' if 'source_object_ids' in operation else 'object_ids', instance.identity)]
    if connection is not None:
        criteria += [('states', connection.state), ('messages', connection.message), ('target_ids', connection.target)]
    return all(not operation.get(key) or value in operation[key] for key, value in criteria)


class Evaluator:
    def __init__(self, seed=None):
        self.random = random.Random(seed)
        self.cursors = {}
        self.propertyWrites = 0

    def value(self, expression, original):
        kind = expression['kind']
        if kind == 'BPropertyValue':
            return expression['value']
        if kind == 'U32AdditionPropertyValue':
            if len(original) < 4:
                raise FormatError('Truncated arithmetic property')
            return pack('I', (int.from_bytes(original[:4], 'big')+int.from_bytes(expression['value'], 'big')) & 0xFFFFFFFF)
        if kind == 'RandomColorPropertyValue':
            return pack('4f', *(self.random.randrange(256)/255 for _ in range(4)))
        if kind == 'RepeatPropertyValue':
            values = expression['property_values']
            if not values:
                raise FormatError('Empty repeating property rule')
            identity = id(expression)
            cursor = self.cursors.get(identity, 0)
            result = values[cursor]
            self.cursors[identity] = (cursor+1) % len(values)
            return result
        raise FormatError('Unknown property expression: '+kind)

    def properties(self, data, operations):
        if not operations:
            return data
        result = bytearray(data)
        # Script properties include nested typed arrays and structures. Match
        # declared field headers within this bounded object, never beyond its
        # record. Require a declared payload size before applying any prefix.
        for offset in range(max(0, len(result)-6)):
            for operation in operations:
                if result[offset:offset+4] != operation['property_id']:
                    continue
                size = int.from_bytes(result[offset+4:offset+6], 'big')
                start, end = offset+6, offset+6+size
                if end > len(result):
                    raise FormatError('Property payload exceeds containing record')
                value = self.value(operation['property_value'], bytes(result[start:end]))
                if len(value) > size:
                    raise FormatError('Property replacement exceeds declared field size')
                result[start:start+len(value)] = value
                self.propertyWrites += 1
        return bytes(result)


def parse_layer(data):
    reader = Reader(data)
    header = reader.read(10)
    if header[:4] != b'SCLY':
        raise FormatError('Expected SCLY record')
    count = reader.count(12)
    objects = []
    for _ in range(count):
        kind = reader.read(4).decode('ascii')
        record = Reader(reader.read(reader.u16()))
        identity = record.u32() & 0xFFFF
        connections = [Connection(record.read(4).decode('ascii'), record.read(4).decode('ascii'), record.u32() & 0xFFFF)
                       for _ in range(record.count(12, width=2))]
        objects.append(Instance(kind, identity, connections, record.read(record.remaining)))
    if any(reader.read(reader.remaining)):
        raise FormatError('Nonzero SCLY padding')
    return header, objects


def encode_layer(header, objects, area_index):
    layer = header[8]
    if area_index > 255 or layer > 63:
        raise FormatError('Script instance address exceeds supported bit fields')
    result = bytearray(header+pack('I', len(objects)))
    for instance in objects:
        if len(instance.kind) != 4 or not 0 <= instance.identity <= 65535:
            raise FormatError('Invalid script object identity')
        body = bytearray(pack('IH', layer << 26 | area_index << 16 | instance.identity, len(instance.connections)))
        for connection in instance.connections:
            if len(connection.state) != 4 or len(connection.message) != 4:
                raise FormatError('Connection tags must contain four characters')
            body.extend(connection.state.encode('ascii')+connection.message.encode('ascii')+
                        pack('I', area_index << 16 | connection.target))
        body.extend(instance.properties)
        result.extend(instance.kind.encode('ascii')+pack('H', len(body))+body)
    return pad(result, 32)


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
                obj.properties = evaluator.properties(obj.properties, rule['property_modifications'])
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
