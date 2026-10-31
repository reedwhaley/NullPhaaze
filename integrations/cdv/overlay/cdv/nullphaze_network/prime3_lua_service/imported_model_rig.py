# Audited rigid two-shell Ice Beam rig; not a general cross-game skin converter. Boundary
# names here: sand_codec, bind_particle_event, complete_pose, convert.
"""Audited rigid two-shell Ice Beam rig; not a general cross-game skin converter."""

import copy
import struct

from construct import Bytes, Const, GreedyBytes, Int16ub, Int32ub, ListContainer, Prefixed, PrefixedArray, Struct
from nullphaze_core.archives import Resource
from retro_data_structures.formats import format_for
from retro_data_structures.formats.cmdl import Cmdl
from retro_data_structures.formats.cskr import VertexGroup
from retro_data_structures.game_check import Game

from nullphaze_network.prime3_lua_service import imported_model_animation as motion
from nullphaze_network.prime3_lua_service import imported_model_probe as model

SOURCE_ANIMATION = 0x846B0326
SOURCE_SKELETON = 0xC1B0421D
SOURCE_SKIN = 0xB10A1E68
SOURCE_CHARACTER = 0x52A3B1A4
TEMPLATE_CHARACTER = 0x308B5A3B94899037
TEMPLATE_SAND = 0xB6305E4946B98F4E

NATIVE_SKIN_V2 = Struct(
    "magic" / Const(b"SKIN"),
    "version" / Const(2, Int32ub),
    "vertex_groups" / PrefixedArray(Int32ub, VertexGroup),
    "pool_to_skin_idx" / PrefixedArray(Int32ub, Int16ub),
    "remap_a" / Prefixed(Int32ub, GreedyBytes),
    "remap_b" / Prefixed(Int32ub, GreedyBytes),
    "optional_data" / Prefixed(Int32ub, GreedyBytes),
    "remap_c" / Prefixed(Int32ub, GreedyBytes),
    "remap_d" / Prefixed(Int32ub, GreedyBytes),
    "trailing_bytes" / GreedyBytes,
)


def sand_codec():
    """Preserve event metadata discarded by RDS 0.44's anonymous Struct."""
    memo = {}

    def clone(node):
        if id(node) in memo:
            return memo[id(node)]
        result = copy.copy(node)
        memo[id(node)] = result
        if getattr(node, "name", None) == "unk_extra":
            result.subcon = Bytes(20)
            return result
        if hasattr(node, "subcons"):
            result.subcons = [clone(child) for child in node.subcons]
        for name in ("subcon", "thensubcon", "elsesubcon"):
            child = getattr(node, name, None)
            if child is not None:
                setattr(result, name, clone(child))
        if hasattr(node, "cases"):
            result.cases = {key: clone(value) for key, value in node.cases.items()}
        return result

    return clone(format_for("SAND"))


def bind_particle_event(event, bone, scale, transform_mode):
    """Set fields verified in the retail particle reader and update switch.

    80393538 reads the metadata bone ID into the base node's byte at +34.
    8048ce64 carries the final integer into generator-info +34; 8048e6f8
    handles only transform modes 0/1/2. The two fields are not interchangeable.
    """
    if not 0 <= bone < 147 or transform_mode not in (0, 1, 2):
        raise ValueError("Invalid native particle bone or transform mode")
    metadata = event.base.unk_extra
    if not isinstance(metadata, bytes) or len(metadata) != 20:
        raise ValueError("Expected preserved native event attachment metadata")
    event.base.unk_extra = metadata[:4] + struct.pack(">I", bone) + metadata[8:]
    event.unk_float = scale
    event.unk_id = transform_mode


def complete_pose(animation, skeleton):
    """Bake sparse Prime tracks against this rig's identity bind rotations."""
    bones = {bone.id: bone for bone in skeleton.bones}
    if set(bones) != set(range(7)) or any(
        list(bone.rotation) != [1, 0, 0, 0] for bone in bones.values()
    ):
        raise ValueError("Pose completion supports only the audited Ice Beam bind pose")
    before = copy.deepcopy(animation)
    frames = animation.key_count
    for kind in ("rotation", "translation", "scale"):
        keys = ListContainer()
        for identity in range(7):
            channel = before.bone_channel_index_array[identity]
            index = before[f"{kind}_channel_index_array"][channel] if channel != 255 else 255
            if index != 255:
                track = before[f"{kind}_key_array"][index * frames:(index + 1) * frames]
                if len(track) != frames:
                    raise ValueError("Incomplete source channel")
            else:
                if kind == "translation":
                    bone = bones[identity]
                    parent = bones.get(bone.parent_id)
                    fallback = [value - (parent.position[axis] if parent else 0)
                                for axis, value in enumerate(bone.position)]
                else:
                    fallback = [1, 0, 0, 0] if kind == "rotation" else [1, 1, 1]
                track = [ListContainer(fallback) for _ in range(frames)]
            keys.extend(track)
        animation[f"{kind}_channel_index_array"] = ListContainer(range(7))
        animation[f"{kind}_key_array"] = keys
    animation.bone_channel_index_array = ListContainer(list(range(7)) + [255] * 143)
    return animation


def convert(prime, corruption, texture_ids, particle):
    source = prime.get_parsed_asset(model.SOURCE_MODEL)
    encoded, geometry = model.convert_model(source, corruption.get_parsed_asset(model.TEMPLATE_MODEL), texture_ids)
    mesh = Cmdl.parse(encoded, Game.CORRUPTION)._raw
    scale, center = geometry["scale"], geometry["center"]
    skin = copy.deepcopy(prime.get_parsed_asset(SOURCE_SKIN)._raw)
    if [(group.vertex_count, [(w.bone_id, w.weight) for w in group.weights_array])
            for group in skin.vertex_groups] != [(492, [(7, 1.0)]), (495, [(6, 1.0)])]:
        raise ValueError("Source no longer has the audited rigid two-shell skin")
    if len(mesh.surfaces) != 1:
        raise ValueError("Expected one source palette")
    for primitive in mesh.surfaces[0].primitives:
        for vertex in primitive.vertices:
            if not 0 <= vertex.position < 987 or vertex.normal != vertex.position:
                raise ValueError("Source vertex/normal skin association changed")
            slot = 0 if vertex.position < 492 else 3
            vertex.matrix.position = slot
            vertex.matrix.tex["6"] = slot
    mesh.attrib_arrays.positions = mesh.attrib_arrays.positions[:987]
    mesh.attrib_arrays.normals = mesh.attrib_arrays.normals[:987]
    passes = [element.body for element in mesh.material_sets[0].materials[0].elements if element.type == "PASS"]
    passes[0].uv_source, passes[1].uv_source = 0, 1
    # Prime's second stage contributes RGB, not the native missile's bloom alpha.
    passes[1].flags = 0
    for element in mesh.material_sets[0].materials[0].elements:
        if element.type == "INT " and element.body.subtype == "BNIF":
            element.body.value = 0
    for group in skin.vertex_groups:
        group.weights_array[0].bone_id -= 3
    # Native SP_APC_front (30b90c6617730805) confirms a ten-slot palette,
    # matrix selectors 0/3, and the byte-sized group remap for this rigid case.
    skin = {"vertex_groups": skin.vertex_groups, "pool_to_skin_idx": [0, 1] + [65535] * 8,
            "remap_a": b"\0\1", "remap_b": b"", "optional_data": b"", "remap_c": b"",
            "remap_d": b"\0\1", "trailing_bytes": b""}
    skeleton = copy.deepcopy(prime.get_parsed_asset(SOURCE_SKELETON)._raw)
    if {bone.id for bone in skeleton.bones} != set(range(3, 10)):
        raise ValueError("Source skeleton changed")
    for bone in skeleton.bones:
        bone.id -= 3
        bone.parent_id = 147 if bone.parent_id == 2 else bone.parent_id - 3
        bone.linked_bone_id_array = ListContainer(147 if value == 2 else value - 3
                                                 for value in bone.linked_bone_id_array)
        bone.position = ListContainer((value - origin) * scale
                                       for value, origin in zip(bone.position, center, strict=True))
        bone.rotation = bone.local_rotation = ListContainer([1.0, 0.0, 0.0, 0.0])
    skeleton.build_order_id = ListContainer(value - 3 for value in skeleton.build_order_id)
    for name in skeleton.bone_names:
        name.bone_id -= 3
    # Corruption's 657 retail skeletons use dense, ID-ordered bone storage.
    # Prime's Ice Beam instead stores its root last; preserve IDs, not that layout.
    skeleton.bones = ListContainer(sorted(skeleton.bones, key=lambda bone: bone.id))
    animation = motion.CORRUPTION_ANIM_ZERO.parse(motion.convert_prime(prime.get_parsed_asset(SOURCE_ANIMATION)._raw))
    for key in animation.translation_key_array:
        for axis in range(3):
            key[axis] *= scale
    root_channel = animation.bone_channel_index_array[0]
    root_translation = animation.translation_channel_index_array[root_channel]
    root_start = root_translation * animation.key_count
    for key in animation.translation_key_array[root_start:root_start + animation.key_count]:
        for axis in range(3):
            key[axis] -= center[axis] * scale
    animation = complete_pose(animation, skeleton)
    ids = {kind: model.asset_id(kind.encode(), source_id) for kind, source_id in
           (("CMDL", model.SOURCE_MODEL), ("CSKR", SOURCE_SKIN), ("CINF", SOURCE_SKELETON),
            ("ANIM", SOURCE_ANIMATION), ("CHAR", SOURCE_CHARACTER), ("SAND", SOURCE_CHARACTER))}
    character = copy.deepcopy(corruption.get_parsed_asset(TEMPLATE_CHARACTER)._raw)
    character.name = "Prime_Ice_Beam"
    character.model_id, character.skin_id = ids["CMDL"], ids["CSKR"]
    character.skeleton_id, character.sand_id = ids["CINF"], ids["SAND"]
    character.particle_resource_data.generic_particles = ListContainer([particle])
    character.sound_resources = ListContainer()
    character.animations[0].name = "Prime_Ice_Beam_idle"
    body = character.animations[0].meta.body
    body.asset_id, body.name = ids["ANIM"], "Prime_Ice_Beam_idle"
    character.animation_aabb_array[0].anim_id = ids["ANIM"]
    character.animation_aabb_array[0].bounding_box = copy.deepcopy(mesh.aabox)
    sand = sand_codec().parse(corruption.get_raw_asset(TEMPLATE_SAND).data, target_game=Game.CORRUPTION)
    events = sand.anim_events[0]
    events.id = ids["ANIM"]
    events.sound_sets = ListContainer()
    event = copy.deepcopy(events.event_sets[0])
    event.base.name = "Prime_Ice_Beam_core"
    event.particle.id = particle
    bind_particle_event(event, bone=6, scale=scale, transform_mode=2)
    events.event_sets = ListContainer([event])
    values = {"CMDL": mesh, "CSKR": skin, "CINF": skeleton, "CHAR": character, "SAND": sand}
    assets = []
    for kind, value in values.items():
        codec = {"SAND": sand_codec(), "CSKR": NATIVE_SKIN_V2}.get(kind, format_for(kind))
        try:
            raw = codec.build(value, target_game=Game.CORRUPTION)
        except Exception as exc:
            raise ValueError(f"Could not encode converted {kind}") from exc
        if codec.build(codec.parse(raw, target_game=Game.CORRUPTION), target_game=Game.CORRUPTION) != raw:
            raise ValueError(f"{kind} roundtrip changed the converted rig")
        assets.append(Resource(ids[kind], kind.encode(), False, 0).updated(raw))
    raw = motion.CORRUPTION_ANIM_ZERO.build(animation)
    assets.append(Resource(ids["ANIM"], b"ANIM", False, 0).updated(raw))
    return assets, ids, geometry
