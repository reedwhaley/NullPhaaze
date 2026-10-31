# Wire the real pickup event and recipient text on the post-core seed. Disconnect only the
# audited core grant edges when the receipt-driven grant path owns that location. Boundary
# names here: patch_area, patch_archives.
"""GPL addon: actual pickup events and recipient text on seed-patched archives.

Works on the eleven-file core output. It never substitutes a retail test PAK.
"""
from __future__ import annotations

import copy
import hashlib
import struct
from functools import lru_cache
from pathlib import Path

from construct import Container
from nullphaze_core.archives import Archive, Resource
from nullphaze_core.resources import make_string_table
from nullphaze_core.rules import catalog, decode, recipe
from retro_data_structures.enums.corruption import Message, State
from nullphaze_network.prime3_lua_service.mrea_build import SeedMrea as Mrea
from retro_data_structures.formats.script_object import InstanceId, ScriptInstanceRaw
from retro_data_structures.game_check import Game
from retro_data_structures.properties.corruption.objects.LUAScript import LUAScript

from nullphaze_network.prime3_lua_service.probe import properties, replace_properties

ZERO = bytes(4)


@lru_cache(maxsize=100)
def _core_grant_edges(index, area):
    """Exact core-created relay entry edges; retail cutscene links stay intact."""
    data = catalog()
    roots = {ids[0] for raw in data['items'] for key in
             ('progressive_ids', 'conversion_start_ids', 'conversion_end_ids')
             if (ids := decode(raw).get(key))}
    recipes = [recipe(entry) for item in data['pickupRecipes'][index] for entry in item]
    recipes.extend(recipe(data['fakeRecipes'][alias_index][item])
                   for alias_index, alias in enumerate(data['fakePickups'])
                   if alias['item_index'] == index and alias['mrea_id'] == area
                   for item in range(len(data['items'])))
    edges = {}
    for rules in recipes:
        relays = {obj['id']: obj['script_data'] for operation in rules['object_addition_patches']
                  if area in operation['mrea_ids'] for obj in operation['script_objects']
                  if obj['id'] in roots and obj['type'] == 'CRLY'}
        for operation in rules['connection_addition_patches']:
            if area not in operation['mrea_ids']:
                continue
            for edge in operation['connections']:
                if edge['target'] not in roots:
                    continue
                if edge['target'] not in relays:
                    raise ValueError('Core grant entry lacks an audited relay definition')
                for source in operation['source_object_ids']:
                    key = source, edge['state'], edge['message'], edge['target']
                    edges.setdefault(key, set()).add(relays[edge['target']])
    return edges


def _disconnect_core_grants(index, area, objects):
    expected = _core_grant_edges(index, area)
    removed = []
    for obj in objects.values():
        retained = []
        for connection in obj.connections:
            key = obj.id.instance, connection.state.value, connection.message.value, connection.target.instance
            if key not in expected:
                retained.append(connection)
                continue
            target = objects.get(int(connection.target))
            if target is None or target.type_name != 'CRLY' or target._raw.base_property not in expected[key]:
                raise ValueError('Core pickup grant relay differs from its audited recipe')
            removed.append({'source': int(obj.id), 'target': int(connection.target),
                            'state': connection.state.value, 'message': connection.message.value})
        if len(retained) != len(obj.connections):
            obj._raw.connections = tuple(retained)
    return removed


def _text(row):
    def safe(value):
        return "".join(c if c.isprintable() and c != "&" else " " for c in value)[:120]

    name = safe(row["item_name"])
    return f"{name} acquired!" if row["local"] else f"{name} sent to {safe(row['recipient_name'])}!"


def _callback(index):
    return ("local pending=false\n"
            f"local function collect() if pending and CP3WLocation{index} then "
            f"if CP3WLocation{index}() then pending=false end end end\n"
            "function OnCollected(msg) pending=true collect() end\n"
            "function OnThink(dt) collect() end\n")


def patch_area(raw: bytes, rows: list[dict], locations: dict[int, dict]) -> tuple[bytes, list[Resource], dict]:
    area = Mrea.parse(raw, Game.CORRUPTION)
    layers = list(area.script_layers)
    objects = {int(o.id): o for layer in layers for o in layer.instances}
    if len(objects) != sum(len(list(layer.instances)) for layer in layers):
        raise ValueError("Duplicate script instance identity")
    originals = {identity: copy.deepcopy(obj._raw) for identity, obj in objects.items()}
    allowed = set()
    strings, events = [], []
    highest = max(obj.id.instance for layer in [*layers, area.generated_objects_layer]
                  for obj in layer.instances)
    for row in rows:
        location = locations[row["index"]]
        variant = location["variants"][0]["objects"]
        actor = objects[variant["instance_id"]["id"]]
        if actor.type_name != variant["instance_id"]["type"]:
            raise ValueError("Seed changed the audited pickup actor type")
        disconnected = _disconnect_core_grants(row['index'], location['area'], objects)
        allowed.update(edge['source'] for edge in disconnected)
        # A core placeholder must have its native effect removed, including
        # the separate percentage actor used by scripted item acquisitions.
        neutral = [actor]
        aliases = []
        for alias in catalog()["fakePickups"]:
            if alias["item_index"] != row["index"] or alias["mrea_id"] != location["area"]:
                continue
            matches = [obj for obj in layers[alias["scly_section"]].instances
                       if obj.id.instance == int(alias["instance_id"]["$bytes"], 16)]
            if len(matches) != 1:
                raise ValueError("Missing or ambiguous fake pickup alias")
            if matches[0].type_name == "PCKP":
                neutral.append(matches[0])
                aliases.append(matches[0])
            elif matches[0].type_name not in ("ACTR", "PLAT"):
                raise ValueError("Unaudited fake pickup actor type")
        if "percentage_pickup_id" in variant:
            neutral.append(objects[variant["percentage_pickup_id"]["id"]])
        for obj in neutral:
            if obj.type_name == "PCKP":
                changes = {0x28C71B54: ZERO, 0x94AF1445: ZERO, 0x165AB069: ZERO}
            elif obj.type_name == "SPFN":
                # Only the audited ModifyInventoryAmount percentage actor.
                fields = dict(properties(obj._raw.base_property))
                if fields[0xB8AFCF21] != struct.pack(">I", 2527813936):
                    raise ValueError("Unexpected scripted pickup function")
                changes = {0xB581574B: ZERO}
            else:
                raise ValueError("Unsupported pickup grant actor")
            obj._raw.base_property = replace_properties(obj._raw.base_property, changes)
            allowed.add(int(obj.id))
        if actor.type_name == "PCKP":
            endpoints = [(obj, State("ACQU")) for obj in (actor, *aliases)]
        else:
            incoming = variant["instance_id"]["incoming"]
            if not incoming or any(c["message"] != "ACTN" for c in incoming):
                raise ValueError("Unmapped scripted pickup grant event")
            endpoints = [(objects[c["source"]], State(c["state"])) for c in incoming]
        highest += 1
        if highest >= 65536:
            raise ValueError("No unused pickup callback instance IDs")
        from nullphaze_network.prime3_lua_service.mrea_build import next_instance_id
        script_id = next_instance_id(area, actor.id.area)
        highest = script_id.instance
        script = LUAScript(unknown_0xa1ecc54b=_callback(row["index"]))
        script.editor_properties.name = f"Nullphaze multiworld check {row['index']}"
        script.unknown_0x9facea01 = '"Collected" "InternalMessage0"'
        layers[0]._raw.script_instances.append(ScriptInstanceRaw("LUAX", script_id, (), script.to_bytes(Game.CORRUPTION)))
        for source, state in endpoints:
            source.add_connection(state, Message.InternalMessage00, script_id)
            allowed.add(int(source.id))
        memo = objects[variant["memo_id"]["id"]]
        if memo.type_name != "MEMO":
            raise ValueError("Missing pickup memo")
        string_id = int.from_bytes(hashlib.sha256(
            f"Nullphaze multiworld memo/{locations['world_uuid']}/{row['index']}".encode("ascii")
        ).digest()[:8], "big")
        text = make_string_table([_text(row)])
        strings.append(Resource(string_id, b"STRG", 0, len(text), data=text))
        memo._raw.base_property = replace_properties(memo._raw.base_property, {
            2441225484: string_id.to_bytes(8, "big"), 0x64124219: ZERO,
        })
        allowed.add(int(memo.id))
        dependency_section = area.get_section("dependencies_section")[0]
        dependencies = dependency_section.dependencies
        if any(dep.asset_id == string_id for dep in dependencies):
            raise ValueError("Multiworld memo asset ID collision")
        dependencies.insert(dependency_section.offsets[1], Container(asset_id=string_id, type="STRG"))
        for layer_index in range(1, len(dependency_section.offsets)):
            dependency_section.offsets[layer_index] += 1
        events.append({"index": row["index"], "script_id": int(script_id), "string_id": string_id,
                       "endpoints": [{"id": int(obj.id), "state": state.value} for obj, state in endpoints],
                       "local": row["local"], "text": _text(row), "neutralized_pickup_aliases": [int(obj.id) for obj in aliases],
                       "disconnected_core_grant_edges": disconnected})
    for layer in layers:
        layer.mark_modified()
    result = area.build()
    checked = Mrea.parse(result, Game.CORRUPTION)
    actual = {int(o.id): o for layer in checked.script_layers for o in layer.instances}
    for identity, original in originals.items():
        if identity not in allowed and actual[identity]._raw != original:
            raise ValueError(f"Unrelated randomized script changed: {identity:08x}")
    if set(actual) != set(originals) | {e["script_id"] for e in events}:
        raise ValueError("Unexpected script deletion/addition")
    return result, strings, {"checks": events, "unrelated_scripts_verified": len(originals) - len(allowed)}


def patch_archives(source: Path, output: Path, manifest: dict, audit: dict) -> dict:
    if output.exists() or source.resolve() == output.resolve():
        raise ValueError("Use a new owned addon output directory")
    output.mkdir(parents=True)
    locations = {row["index"]: row for row in audit["pickups"]}
    if sorted(locations) != list(range(100)):
        raise ValueError("Addon requires every pickup mapping")
    locations["world_uuid"] = manifest["world_uuid"]
    by_pak = {}
    present = {r.identity for p in source.glob('*.pak') for r in Archive(p).resources if r.kind == b'MREA'}
    skipped = []
    for row in manifest["locations"]:
        mapped = locations[row["index"]]
        if mapped['area'] not in present:
            from randovania.games.prime3.multiworld.seed_compiler import seed_tables
            recipes, _, _ = seed_tables(manifest)
            recipe = recipes.get(row['pickup_key']) if row['local'] else None
            if (row['index'] not in (0, 1, 2) or recipe is None or recipe.progression
                    or recipe.extra or recipe.lock is not None or recipe.unlocks):
                raise ValueError('A removed room contains an assigned pickup; regenerate with Olympus excluded.')
            skipped.append(row['index'])
            continue
        if len(mapped["variants"]) != 1:
            raise ValueError("Ambiguous pickup archive mapping")
        by_pak.setdefault(mapped["variants"][0]["pak"], {}).setdefault(mapped["area"], []).append(row)
    report = {"archives": {}, "checks": 0}
    for name, areas in sorted(by_pak.items()):
        archive = Archive(source / name)
        resources, records = [], []
        for resource in archive.resources:
            if resource.kind == b"MREA" and resource.identity in areas:
                if resource.compressed:
                    raise ValueError("Externally compressed pickup area is unsupported")
                changed, strings, record = patch_area(resource.read(), areas[resource.identity], locations)
                resources.extend(strings)
                resources.append(resource.updated(changed))
                records.append({"area": resource.identity, **record})
                report["checks"] += len(record["checks"])
            else:
                resources.append(resource)
        destination = output / name
        archive.write(destination, resources)
        verified = Archive(destination)
        originals = {(r.identity, r.kind): r for r in archive.resources}
        untouched = 0
        for resource in verified.resources:
            key = resource.identity, resource.kind
            if key in originals and resource.identity not in areas:
                if resource.read() != originals[key].read():
                    raise ValueError("Unrelated seed resource changed")
                untouched += 1
        report["archives"][name] = {"areas": records, "unrelated_resources_verified": untouched}
    if skipped and sorted(skipped) != [0, 1, 2]:
        raise ValueError('Partial Olympus pickup removal is unsupported')
    if report["checks"] + len(skipped) != 100:
        raise ValueError("Some pickup mappings were not applied")
    report['excluded_nothing_checks'] = skipped
    return report
