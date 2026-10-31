# Source-authored Ice Beam particle conversion and isolated pickup wiring. Boundary names
# here: convert, rotated, attach.
"""Source-authored Ice Beam particle conversion and isolated pickup wiring."""

import copy
import math

from nullphaze_core.archives import Resource
from retro_data_structures.conversion.asset_converter import AssetConverter
from retro_data_structures.conversion.conversions import converter_for
from retro_data_structures.enums.corruption import Message, State
from retro_data_structures.formats import format_for
from retro_data_structures.formats.script_object import InstanceId, ScriptInstanceRaw
from retro_data_structures.game_check import Game
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.vector import Vector
from retro_data_structures.properties.corruption.objects.Effect import Effect

from nullphaze_network.prime3_lua_service import imported_model_probe as model
from nullphaze_network.prime3_lua_service import probe
from nullphaze_network.prime3_lua_service.mrea_build import SeedMrea

SOURCE_CHARACTER = 0x52A3B1A4
SOURCE_EFFECT = 0x09884086


def convert(prime):
    character = prime.get_parsed_asset(SOURCE_CHARACTER)._raw
    event = prime.get_parsed_asset(character.animation_set.animation_resources[0].event_id)._raw
    points = event.particle_poi_nodes
    if (len(points) != 1 or points[0].particle.id != SOURCE_EFFECT or points[0].bone_name != "Electric"
            or points[0].effect_scale != 1):
        raise ValueError("Source Ice Beam particle event changed")
    if points[0].base.timestamp.time != 0:
        raise ValueError("Unexpected delayed Ice Beam effect")
    skeleton = prime.get_parsed_asset(character.character_set.characters[0].skeleton_id)._raw
    bone_id = next(row.bone_id for row in skeleton.bone_names if row.name == "Electric")
    position = next(list(bone.position) for bone in skeleton.bones if bone.id == bone_id)
    converter = AssetConverter(Game.CORRUPTION, {Game.PRIME: prime},
                               lambda detail: model.asset_id(detail.asset_type.encode("ascii"), detail.asset_id),
                               converter_for)
    effect = converter.convert_asset_by_id(SOURCE_EFFECT, Game.PRIME)
    assets = []
    for resource in converter.converted_assets.values():
        if resource.type not in ("PART", "TXTR"):
            raise ValueError("Unaudited Ice Beam particle dependency type")
        construct = format_for(resource.type)
        encoded = construct.build(resource.resource, target_game=Game.CORRUPTION)
        checked = construct.parse(encoded, target_game=Game.CORRUPTION)
        if construct.build(checked, target_game=Game.CORRUPTION) != encoded:
            raise ValueError("Converted Ice Beam particle dependency is not reproducible")
        assets.append(Resource(resource.id, resource.type.encode("ascii"), 0, 0).updated(encoded))
    return assets, effect.id, {"source_character": f"{SOURCE_CHARACTER:08x}",
                              "source_effect": f"{SOURCE_EFFECT:08x}", "source_bone": "Electric",
                              "source_bone_position": position, "converted_effect": f"{effect.id:016x}",
                              "dependency_types": [resource.kind.decode("ascii") for resource in assets]}


def rotated(vector, degrees):
    x, y, z = vector
    a, b, c = [math.radians(value) for value in degrees]
    y, z = y * math.cos(a) - z * math.sin(a), y * math.sin(a) + z * math.cos(a)
    x, z = x * math.cos(b) + z * math.sin(b), -x * math.sin(b) + z * math.cos(b)
    return [x * math.cos(c) - y * math.sin(c), x * math.sin(c) + y * math.cos(c), z]


def attach(raw, particle, conversion, effect_metadata):
    area = SeedMrea.parse(raw, Game.CORRUPTION)
    layers = list(area.script_layers)
    original = {int(actor.id): copy.deepcopy(actor._raw) for layer in layers for actor in layer.instances}
    pickup = next(actor for layer in layers for actor in layer.instances if int(actor.id) == model.TARGET_PICKUP)
    editor = EditorProperties.from_bytes(dict(probe.properties(pickup._raw.base_property))[0x255A4580], Game.CORRUPTION)
    effect = Effect(particle_effect=particle)
    effect.editor_properties = copy.deepcopy(editor)
    effect.editor_properties.name = "Imported Prime Ice Beam source blue core"
    transform = effect.editor_properties.transform
    s = conversion["scale"]
    local = [(value - conversion["center"][axis]) * s
             for axis, value in enumerate(effect_metadata["source_bone_position"])]
    scale = editor.transform.scale
    local = [local[0] * scale.x, local[1] * scale.y, local[2] * scale.z]
    r = editor.transform.rotation
    offset = rotated(local, (r.x, r.y, r.z))
    transform.position = Vector(editor.transform.position.x + offset[0], editor.transform.position.y + offset[1],
                                editor.transform.position.z + offset[2])
    transform.scale = Vector(scale.x * s, scale.y * s, scale.z * s)
    highest = max(actor.id.instance for layer in layers for actor in layer.instances)
    if highest >= 65535:
        raise ValueError("No free Ice Beam effect actor ID")
    identity = InstanceId.new(0, pickup.id.area, highest + 1)
    layers[0]._raw.script_instances.append(ScriptInstanceRaw("EFCT", identity, (), effect.to_bytes(Game.CORRUPTION)))
    pickup.add_connection(State.Acquired, Message.Delete, identity)
    pickup.add_connection(State.Inactive, Message.Deactivate, identity)
    pickup.add_connection(State.Active, Message.Activate, identity)
    layers[0].mark_modified()
    output = area.build()
    checked = SeedMrea.parse(output, Game.CORRUPTION)
    objects = {int(actor.id): actor for layer in checked.script_layers for actor in layer.instances}
    if set(objects) != set(original) | {int(identity)}:
        raise ValueError("Unexpected particle actor population change")
    for actor_id, before in original.items():
        after = objects[actor_id]._raw
        if actor_id == model.TARGET_PICKUP:
            if (after.base_property != before.base_property
                    or after.connections[:len(before.connections)] != before.connections):
                raise ValueError("Particle wiring changed pickup properties or existing events")
        elif after != before:
            raise ValueError("Particle wiring changed an unrelated seed script")
    return output, {**effect_metadata, "effect_instance": int(identity), "pickup_instance": model.TARGET_PICKUP,
                    "cleanup": "Acquired/Delete; Inactive/Deactivate; Active/Activate",
                    "effect_position": [transform.position.x, transform.position.y, transform.position.z],
                    "effect_scale": [transform.scale.x, transform.scale.y, transform.scale.z],
                    "original_character_animation": False, "persistence_acceptance": "pending"}
