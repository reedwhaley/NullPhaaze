# Starting position, reveal state and inventory use the existing templates and encoding.
# Unfinished starting-item requests remain separate from this migration. Boundary names
# here: apply_start.
"""Starting spawn, reveal state and inventory recipes.

I keep the existing inventory encoding here. The spreadsheet's unresolved
starting-item requests are separate behavior changes, not migration fixes.
"""
from ..rules import recipe, instantiate, merge


def apply_start(plan, data, options, area, world, inventory_values):
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
