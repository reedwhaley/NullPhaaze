# Keep the native ship navigation without the unused Space mission briefings. Boundary names
# here: resource_references, compact_space.
"""Keep the native ship navigation without the unused Space mission briefings."""
from __future__ import annotations

from nullphaze_network.prime3_lua_service.mrea_build import SeedMrea
from retro_data_structures.game_check import Game

from randovania.games.prime3.exporter.main_menu import _decoded

# The Skytown layer supplies the native transport selected by the cockpit.
# Its other actors are the post-Elysian mission briefing, not navigation.
NAVIGATION_TYPES = {
    0x08020003: 'REAA', 0x08020004: 'SPWN', 0x0802003C: 'TEL1',
    0x08020096: 'SPFN', 0x08020099: 'ATRN', 0x080200CE: 'CLRM',
    0x080200E3: 'SPDC', 0x080200F0: 'SPDC', 0x0802037E: 'SPFN',
    0x0802037F: 'TEL1', 0x08020380: 'TEL1', 0x08020381: 'SRLY',
    0x08020382: 'DLHT', 0x08020383: 'CINE', 0x08020384: 'ACTR',
    0x08020385: 'ACTR', 0x08020386: 'CINE', 0x08020387: 'DLHT',
    0x08020388: 'WTAT', 0x080203BA: 'TEL1',
}
NAVIGATION_ACTORS = frozenset(NAVIGATION_TYPES)
LAYER_COUNTS = (23, 0, 102, 47, 84, 108, 480, 21, 15)


def resource_references(data, pattern):
    """Scan every byte: property records do not align their 64-bit asset IDs."""
    return {int.from_bytes(word, 'big') for i in range(max(0, len(data)-7))
            if (word := data[i:i+8]) in pattern}


def compact_space(resources, area_id):
    """Prune dormant briefing/demo actors and their exclusive resource closure.

    Layer indices and all cockpit/native transport properties stay intact.
    The source is this export's private Space archive, never a planetary PAK.
    """
    by_id = {r.identity: r for r in resources}
    if len(by_id) != len(resources) or area_id not in by_id:
        raise ValueError('Warp to Space: unexpected Space archive aliases or missing cockpit')
    source = by_id[area_id]
    area = SeedMrea.parse(source.read(), Game.CORRUPTION)
    layers = list(area.script_layers)
    if tuple(len(list(l.instances)) for l in layers) != LAYER_COUNTS:
        raise ValueError('Warp to Space: unsupported Space script layers; cannot safely remove briefings')
    actors = [a for l in layers for a in l.instances]
    original = {int(a.id): a._raw for a in actors}
    if not NAVIGATION_ACTORS <= set(original) or any(
            original[n].type != kind for n, kind in NAVIGATION_TYPES.items()):
        raise ValueError('Warp to Space: native ship navigation actors are missing')
    removed = {int(a.id) for i, l in enumerate(layers) for a in l.instances
               if i not in (0, 6) and not (i == 2 and int(a.id) in NAVIGATION_ACTORS)}
    for i, layer in enumerate(layers):
        layer._raw.script_instances = [a for a in layer._raw.script_instances if int(a.id) not in removed]
        layer.mark_modified()
    generated = area.generated_objects_layer
    for layer in [*layers, generated]:
        for actor in layer.instances:
            actor.connections = tuple(c for c in actor.connections if int(c.target) not in removed)

    deps = area.get_section('dependencies_section')[0]
    if len(deps.offsets) != 10 or deps.offsets[0] != 0 or deps.offsets[-1] > len(deps.dependencies):
        raise ValueError('Warp to Space: unsupported Space dependency layers')
    groups = [list(deps.dependencies[deps.offsets[i]:deps.offsets[i+1]]) for i in range(9)]
    common = list(deps.dependencies[deps.offsets[-1]:])
    pattern = frozenset(n.to_bytes(8, 'big') for n in by_id)
    # Retail bundles select the material/animation variants for this cockpit.
    # PlayerActor and sky models also name variants belonging to other layers;
    # treating every such reference as active restores those unused planets.
    allowed = {d.asset_id for i in (0, 2, 6) for d in groups[i]}
    allowed.update(d.asset_id for d in common)
    keep = {d.asset_id for i in (0, 6) for d in groups[i]}
    keep.update(d.asset_id for d in common)
    # Preserve the other area and world/save/map metadata. These are not actor
    # dependencies, and must remain available to the native world loader.
    keep.update(r.identity for r in resources if r.kind in (b'MREA', b'MLVL', b'MAPW', b'MAPA', b'SAVW'))
    for resource in resources:
        if resource.kind == b'MREA' and resource.identity != area_id:
            other = SeedMrea.parse(resource.read(), Game.CORRUPTION)
            keep.update(d.asset_id for d in other.get_section('dependencies_section')[0].dependencies)
    for layer in [*layers, generated]:
        for actor in layer.instances:
            keep.update(resource_references(actor._raw.base_property, pattern) & allowed)
    pending = list(keep)
    visited = set()
    while pending:
        identity = pending.pop()
        if identity in visited or identity not in by_id:
            continue
        visited.add(identity)
        resource = by_id[identity]
        if resource.kind == b'MREA':
            continue  # Script/geometry dependencies were selected explicitly.
        references = resource_references(_decoded(resource), pattern)
        # Audio's synchronous loader resolves both sample choices, including
        # fallback samples omitted from retail's prefetch bundle.
        references = {n for n in references if n in allowed or (
            resource.kind == b'CAUD' and by_id[n].kind == b'CSMP')}
        pending.extend(references - keep)
        keep.update(references)
    # The native layer bundles keep their original ordering. Keep every default
    # and cockpit dependency, even if it has no explicit script property owner.
    selected = [groups[0], [], [d for d in groups[2] if d.asset_id in keep], [], [], [], groups[6], [], []]
    deps.dependencies = []
    deps.offsets = []
    for group in selected:
        deps.offsets.append(len(deps.dependencies))
        deps.dependencies.extend(group)
    deps.offsets.append(len(deps.dependencies))
    deps.dependencies.extend(common)
    output = area.build()
    checked = SeedMrea.parse(output, Game.CORRUPTION)
    for layer in [*checked.script_layers, checked.generated_objects_layer]:
        for actor in layer.instances:
            if any(int(c.target) in removed for c in actor.connections):
                raise ValueError('Warp to Space: dangling briefing connection after compaction')
            if int(actor.id) in original and actor._raw.base_property != original[int(actor.id)].base_property:
                raise ValueError('Warp to Space: compaction changed native cockpit properties')
    result = [source.updated(output) if r.identity == area_id else r for r in resources if r.identity in keep]
    return result, {'resources_before': len(resources), 'resources_after': len(result),
                    'payload_bytes_before': sum(r.size for r in resources),
                    'payload_bytes_after': sum(r.size for r in result),
                    'actors_removed': len(removed), 'navigation_actors_preserved': len(NAVIGATION_ACTORS),
                    'layer_indices_preserved': True, 'default_cockpit_dependencies_preserved': True}
