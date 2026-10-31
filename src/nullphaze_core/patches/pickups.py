# Physical pickups and fake aliases share the catalog's location order. Reserve conversion
# helpers once per area and retain deterministic dependency ordering around each grant
# recipe. Boundary names here: apply_pickups.
"""Physical pickups, conversion helpers and deterministic dependency ordering.

Reserve each conversion helper once per area. Repeating it for every pickup
changes the actor graph and is not equivalent to the accepted patcher.
"""
from ..rules import recipe, decode, merge


def apply_pickups(plan, data, items, options, item_dependencies, dependency_order):
    flags = int(options.require_launcher)+2*int(options.require_ship_missile)
    seen = set()
    # Location ordering is a rule-table fact, not the archive or room order.
    for index in sorted(range(100), key=lambda i: data['pickups'][i]['item_index']):
        addition = recipe(data['pickupRecipes'][index][items[index]][flags])
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
