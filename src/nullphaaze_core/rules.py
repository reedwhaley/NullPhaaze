"""Declarative rule decoding; reference data never invokes reference code."""
import copy
import json
from functools import lru_cache
from pathlib import Path
from .binary import FormatError


@lru_cache(maxsize=1)
def catalog():
    path = Path(__file__).parent/'data/rules.json'
    data = json.loads(path.read_text(encoding='utf-8'))
    if data['schema'] != 'nullphaaze-rules-1':
        raise FormatError('Unsupported rule catalog')
    return data


def decode(value):
    if isinstance(value, dict):
        if set(value) == {'$bytes'}:
            return bytes.fromhex(value['$bytes'])
        return {key: decode(item) for key, item in value.items() if key != '$type'} | (
            {'kind': value['$type']} if '$type' in value else {})
    if isinstance(value, list):
        return [decode(item) for item in value]
    return value


def recipe(key):
    return decode(catalog()['recipes'][key])


def empty_plan():
    return {key: {} if key == 'dependency_patches' else [] for key in (
        'layer_toggle_patches', 'layer_clear_patches', 'object_deletion_patches',
        'object_addition_patches', 'object_modification_patches', 'connection_deletion_patches',
        'connection_addition_patches', 'connection_modification_patches', 'dependency_patches')}


def instantiate(value, area, world):
    """Substitute documented sentinel parameters in a newly cloned recipe."""
    if isinstance(value, int):
        return area if value == 0xE011223344556677 else world if value == 0xD088776655443322 else value
    if isinstance(value, bytes):
        return value.replace(bytes.fromhex('E011223344556677'), area.to_bytes(8, 'big')).replace(
            bytes.fromhex('D088776655443322'), world.to_bytes(8, 'big'))
    if isinstance(value, list):
        return [instantiate(item, area, world) for item in value]
    if isinstance(value, dict):
        return {key: instantiate(item, area, world) for key, item in value.items()}
    return value


def merge(destination, source, unique_additions=None):
    for key, values in source.items():
        if key == 'kind':
            continue
        if key == 'dependency_patches':
            for identity, dependencies in values.items():
                old = destination[key].setdefault(identity, [])
                seen = {item['file_id'] for item in old}
                for item in dependencies:
                    if item['file_id'] not in seen:
                        old.append(copy.deepcopy(item))
                        seen.add(item['file_id'])
            continue
        for operation in values:
            if key == 'object_addition_patches' and unique_additions is not None:
                identity = (tuple(operation['mrea_ids']), tuple(operation['layer_indexes']),
                            tuple(obj['id'] for obj in operation['script_objects']))
                if identity in unique_additions:
                    continue
                unique_additions.add(identity)
            destination[key].append(copy.deepcopy(operation))
