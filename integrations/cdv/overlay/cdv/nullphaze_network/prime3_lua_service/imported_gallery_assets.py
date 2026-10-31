# Experimental rigid pickup gallery conversion, not a production importer. Boundary names
# here: asset_id, parse_animation, normalize_empty_particle_references, GalleryAssets.
"""Experimental rigid pickup gallery conversion, not a production importer."""

import bisect
import copy
import hashlib
import io

from construct import Container, ListContainer, Struct
from nullphaze_core.archives import Resource
from retro_data_structures.conversion.asset_converter import AssetConverter
from retro_data_structures.conversion.conversions import converter_for
from retro_data_structures.formats import format_for
from retro_data_structures.formats.anim import ANIM
from retro_data_structures.game_check import Game

from nullphaze_network.prime3_lua_service import imported_model_animation as motion
from nullphaze_network.prime3_lua_service import imported_model_probe as model
from nullphaze_network.prime3_lua_service import imported_model_rig as rig
from nullphaze_network.prime3_lua_service.imported_gallery_presentation import (
    animated_bounds,
    gallery_effect_scale,
    material_flags,
    material_roles,
    native_uv,
    particle_sprite_bound,
)


def asset_id(kind, identity):
    raw = b"Nullphaze private model gallery v1\0" + kind.encode() + str(identity).encode()
    return int.from_bytes(hashlib.sha256(raw).digest()[:8], "big")


def parse_animation(raw):
    stream = io.BytesIO(raw)
    result = Struct(*ANIM.subcons[:2]).parse_stream(stream, target_game=Game.PRIME)
    padding = raw[stream.tell() :]
    if len(padding) > 31 or padding not in (bytes(len(padding)), b"\xff" * len(padding)):
        raise ValueError("Unknown source animation trailer")
    return result


def normalize_empty_particle_references(particle):
    """Prime permits CNST zero children; the native Wii reader requests ID zero."""
    for element in particle.elements:
        if element.type in ("SSWH", "PMDL", "SELC", "IDTS", "ICTS", "IITS"):
            if element.body.type != "NONE" and element.body.body in (0, 0xFFFFFFFF, 0xFFFFFFFFFFFFFFFF):
                element.body.type, element.body.body = "NONE", None


class GalleryAssets:
    def __init__(self, source, native):
        self.source, self.native = source, native
        self.resources = {}
        self.converter = AssetConverter(
            Game.CORRUPTION,
            {Game.PRIME: source},
            lambda detail: asset_id(detail.asset_type, detail.asset_id),
            converter_for,
        )
        self.template_mesh = native.get_parsed_asset(model.TEMPLATE_MODEL)._raw

    def add(self, identity, kind, value, codec=None):
        codec = codec or format_for(kind)
        raw = codec.build(value, target_game=Game.CORRUPTION)
        if codec.build(codec.parse(raw, target_game=Game.CORRUPTION), target_game=Game.CORRUPTION) != raw:
            raise ValueError(f"Gallery {kind} failed roundtrip")
        resource = Resource(identity, kind.encode(), False, 0).updated(raw)
        previous = self.resources.get(identity)
        if previous is not None and previous.read() != resource.read():
            raise ValueError("Gallery resource ID collision")
        self.resources[identity] = resource

    def texture(self, identity):
        return self.converter.convert_id(identity, Game.PRIME)

    def material(self, source, textures):
        result = copy.deepcopy(self.template_mesh.material_sets[0].materials[0])
        templates = [element for element in result.elements if element.type == "PASS"]
        passes = []
        roles = material_roles(source)
        blend = source.blend_source_factor, source.blend_destination_factor
        result.flags = material_flags(result.flags, blend)
        for role, slot, generator in roles:
            index = source.texture_indices[slot]
            element = copy.deepcopy(templates[0])
            element.body.subtype = role
            element.body.id = self.texture(textures[index])
            element.body.flags = 0
            uv, animation = native_uv(source, generator)
            if not animation and not (source.vertex_attribute_flags >> (8 + 2 * uv)) & 3:
                raise ValueError("Material references an absent UV channel")
            element.body.uv_source = uv
            element.body.uv_animation = ListContainer(animation)
            passes.append(element)
        if blend == (4, 5):
            opacity = copy.deepcopy(next(p for p in passes if p.body.subtype == "CLR "))
            opacity.body.subtype, opacity.body.flags = "TRAN", 3
            passes.append(opacity)
        result.elements = ListContainer(
            [e for e in result.elements if e.type not in ("PASS", "END ")]
            + passes
            + [Container(type="END ", body=None)]
        )
        for element in result.elements:
            if element.type == "INT " and element.body.subtype == "BNIF":
                element.body.value = 0
            if element.type == "CLR " and element.body.subtype == "CLR ":
                element.body.value = 0xFFFFFFFF if roles else 0
        if blend == (0, 1):
            result.elements.insert(0, Container(type="INT ", body=Container(subtype="OPAC", value=0)))
        result.vertex_attribute_flags = source.vertex_attribute_flags | 0x81000000
        result.group_index = source.group_index
        return result

    def mesh(self, row, source_skin, scale, center, bone_map, bounds):
        source = self.source.get_parsed_asset(row["model"])._raw
        mesh = copy.deepcopy(source)
        if len(source.material_sets) != 1:
            raise ValueError("Unreviewed material-set switching")
        groups = source_skin.vertex_groups
        if any(len(group.weights_array) != 1 or group.weights_array[0].weight != 1 for group in groups):
            raise ValueError("The gallery only supports rigid skin groups")
        limits, total = [], 0
        for group in groups:
            total += group.vertex_count
            limits.append(total)
        pairs = set()
        vertex_keys = []
        for surface in mesh.surfaces:
            for primitive in surface.primitives:
                for vertex in primitive.vertices:
                    if not 0 <= vertex.position < len(source.attrib_arrays.positions):
                        raise ValueError("Source vertex outside pool")
                    if not 0 <= vertex.normal < len(source.attrib_arrays.normals):
                        raise ValueError("Source normal outside pool")
                    group = 0 if len(groups) == 1 else bisect.bisect_right(limits, vertex.position)
                    if group >= len(groups):
                        raise ValueError("Multi-group source skin does not cover the mesh")
                    key = group, vertex.position, vertex.normal
                    pairs.add(key)
                    vertex_keys.append((vertex, key))
        ordered = sorted(pairs)
        indices = {key: index for index, key in enumerate(ordered)}
        active = sorted({key[0] for key in ordered})
        slots = {group: index for index, group in enumerate(active)}
        if len(active) > 10:
            raise ValueError("Rigid palette exceeds native ten-slot limit")
        mesh.attrib_arrays.positions = ListContainer(
            ListContainer(
                (value - origin) * scale
                for value, origin in zip(source.attrib_arrays.positions[p], center, strict=True)
            )
            for _, p, _ in ordered
        )
        mesh.attrib_arrays.normals = ListContainer(
            copy.deepcopy(source.attrib_arrays.normals[n]) for _, _, n in ordered
        )
        for vertex, key in vertex_keys:
            vertex.position = vertex.normal = indices[key]
            vertex.matrix.position = vertex.matrix.tex["6"] = 3 * slots[key[0]]
        native_groups = []
        for group in active:
            copied = copy.deepcopy(groups[group])
            copied.vertex_count = sum(key[0] == group for key in ordered)
            copied.weights_array[0].bone_id = bone_map[copied.weights_array[0].bone_id]
            native_groups.append(copied)
        mesh.version = 5
        mesh.flags &= ~4
        mesh.attrib_arrays.lightmap_uvs = None
        materials = source.material_sets[0]
        mesh.material_sets = ListContainer(
            [
                Container(
                    texture_file_ids=None,
                    materials=ListContainer(
                        self.material(material, materials.texture_file_ids) for material in materials.materials
                    ),
                )
            ]
        )
        for axis in range(3):
            mesh.aabox.min[axis] = (bounds[0][axis] - center[axis]) * scale
            mesh.aabox.max[axis] = (bounds[1][axis] - center[axis]) * scale
        for surface in mesh.surfaces:
            surface.header.center_point = ListContainer(
                (v - c) * scale for v, c in zip(surface.header.center_point, center, strict=True)
            )
            surface.header.unk_1, surface.header.unk_2, surface.header.extra_data = 0, 65535, b"\xff"
        remap = bytes(range(len(active)))
        skin = {
            "vertex_groups": native_groups,
            "pool_to_skin_idx": list(range(len(active))) + [65535] * (10 - len(active)),
            "remap_a": remap,
            "remap_b": b"",
            "optional_data": b"",
            "remap_c": b"",
            "remap_d": remap,
            "trailing_bytes": b"",
        }
        return mesh, skin

    def convert(self, row):
        source_mesh = self.source.get_parsed_asset(row["model"])._raw
        center = [(a + b) / 2 for a, b in zip(source_mesh.aabox.min, source_mesh.aabox.max, strict=True)]
        extent = max(b - a for a, b in zip(source_mesh.aabox.min, source_mesh.aabox.max, strict=True))
        if extent <= 0:
            raise ValueError("Empty gallery model bounds")
        scale = 0.8 / extent
        identity = row["game"] + ":" + row["name"]
        ids = {kind: asset_id(kind, identity) for kind in ("CMDL", "CSKR", "CINF", "ANIM", "CHAR", "SAND")}
        source_ancs = None
        if row["ancs"] != 0xFFFFFFFF:
            source_ancs = self.source.get_parsed_asset(row["ancs"])._raw
            source_skin = self.source.get_parsed_asset(row["skin"])._raw
            skeleton = copy.deepcopy(self.source.get_parsed_asset(row["skeleton"])._raw)
            meta = source_ancs.animation_set.animations[row["animation"]].meta
            if meta.type != 0:
                raise ValueError("Unreviewed animation blend graph")
            animation = parse_animation(self.source.get_raw_asset(meta.body.asset_id).data)
            tracks = motion.decode_prime(animation)
            frames, duration, interval = (
                len(animation.anim.animation_keys) + 1,
                animation.anim.duration,
                animation.anim.interval,
            )
            events = self.source.get_parsed_asset(animation.anim.event_id)._raw.particle_poi_nodes
        else:
            skeleton = copy.deepcopy(self.native.get_parsed_asset(0x6DBD70C08912B2EB)._raw)
            for bone in skeleton.bones:
                bone.id += 3
                bone.parent_id = 2 if bone.parent_id == 147 else bone.parent_id + 3
                bone.linked_bone_id_array = ListContainer(2 if i == 147 else i + 3 for i in bone.linked_bone_id_array)
            skeleton.build_order_id = ListContainer(i + 3 for i in skeleton.build_order_id)
            for name in skeleton.bone_names:
                name.bone_id += 3
            source_skin = Container(
                vertex_groups=ListContainer(
                    [
                        Container(
                            vertex_count=len(source_mesh.attrib_arrays.positions),
                            weights_array=ListContainer([Container(bone_id=3, weight=1.0)]),
                        )
                    ]
                )
            )
            tracks, frames, duration, interval, events = {}, 2, 1.0, 1.0, []
        bounds = animated_bounds(source_mesh, source_skin, skeleton, tracks, frames)
        center = [(a + b) / 2 for a, b in zip(*bounds, strict=True)]
        extent = max(b - a for a, b in zip(*bounds, strict=True))
        if extent <= 0:
            raise ValueError("Empty animated model bounds")
        scale = 0.8 / extent
        source_bones = {bone.id: copy.deepcopy(bone) for bone in skeleton.bones}
        count = len(source_bones)
        if min(source_bones) != 3 or count > 147:
            raise ValueError("Unreviewed source skeleton root")
        bone_map = {identity: index for index, identity in enumerate(sorted(source_bones))}
        mesh, skin = self.mesh(row, source_skin, scale, center, bone_map, bounds)
        keys = {kind: [] for kind in ("rotation", "translation", "scale")}
        for identity in sorted(source_bones):
            bone = source_bones[identity]
            parent = source_bones.get(bone.parent_id)
            for kind, output_keys in keys.items():
                fallback = (
                    [a - (parent.position[i] if parent else 0) for i, a in enumerate(bone.position)]
                    if kind == "translation"
                    else [1, 0, 0, 0]
                    if kind == "rotation"
                    else [1, 1, 1]
                )
                samples = tracks.get(identity, {}).get(kind, [fallback] * frames)
                if len(samples) != frames:
                    raise ValueError("Incomplete native pose bake")
                for sample in samples:
                    value = list(sample)
                    if kind == "translation":
                        value = [(v - (center[i] if identity == 3 else 0)) * scale for i, v in enumerate(value)]
                    output_keys.append(value)
        native_animation = {
            "version": 1,
            "duration": {"time": duration, "differential_state": 0},
            "key_interval": {"time": interval, "differential_state": 0},
            "key_count": frames,
            "root_bone_id": 0,
            "bone_channel_index_array": list(range(count)) + [255] * (150 - count),
            "auxiliary_count": 0,
            "auxiliary_stride": 0,
            "auxiliary_data": b"",
            "trailing_bytes": b"",
        }
        for kind, values in keys.items():
            native_animation[f"{kind}_channel_index_array"] = list(range(count))
            native_animation[f"{kind}_key_array"] = values
        for bone in skeleton.bones:
            bone.id = bone_map[bone.id]
            bone.parent_id = 147 if bone.parent_id == 2 else bone_map[bone.parent_id]
            bone.linked_bone_id_array = ListContainer(147 if i == 2 else bone_map[i] for i in bone.linked_bone_id_array)
            bone.position = ListContainer((v - c) * scale for v, c in zip(bone.position, center, strict=True))
            bone.rotation = bone.local_rotation = ListContainer([1, 0, 0, 0])
        skeleton.bones = ListContainer(sorted(skeleton.bones, key=lambda bone: bone.id))
        skeleton.build_order_id = ListContainer(bone_map[i] for i in skeleton.build_order_id)
        names = {name.name: bone_map[name.bone_id] for name in skeleton.bone_names}
        for name in skeleton.bone_names:
            name.bone_id = bone_map[name.bone_id]
        sand = rig.sand_codec().parse(self.native.get_raw_asset(rig.TEMPLATE_SAND).data, target_game=Game.CORRUPTION)
        event_set = sand.anim_events[0]
        template = copy.deepcopy(event_set.event_sets[0])
        event_set.id, event_set.event_sets, event_set.sound_sets = ids["ANIM"], ListContainer(), ListContainer()
        particles, effect_bounds = [], []
        for index, source_event in enumerate(events):
            if source_event.base.character_index not in (-1, row["character"]):
                continue
            if source_event.particle.type != "PART" or source_event.bone_name not in names:
                raise ValueError("Unreviewed particle attachment")
            event = copy.deepcopy(template)
            event.particle.id = self.converter.convert_id(source_event.particle.id, Game.PRIME)
            event.base.name = f"Gallery_core_{index}"
            event.base.timestamp = copy.deepcopy(source_event.base.timestamp)
            sprite_bound = particle_sprite_bound(
                event.particle.id, lambda identity: self.converter.converted_assets[identity].resource
            )
            effect_scale = gallery_effect_scale(scale, source_event.effect_scale, sprite_bound)
            rig.bind_particle_event(event, names[source_event.bone_name], effect_scale, source_event.transform_type)
            event_set.event_sets.append(event)
            particles.append(event.particle.id)
            effect_bounds.append(
                {
                    "particle": f"{event.particle.id:016x}",
                    "source_sprite_bound": sprite_bound,
                    "scale": effect_scale,
                    "maximum_quad_diagonal": 2 * 2**0.5 * sprite_bound * effect_scale,
                }
            )
        character = copy.deepcopy(self.native.get_parsed_asset(rig.TEMPLATE_CHARACTER)._raw)
        character.name = row["game"] + "_" + row["name"]
        character.model_id, character.skin_id = ids["CMDL"], ids["CSKR"]
        character.skeleton_id, character.sand_id = ids["CINF"], ids["SAND"]
        character.particle_resource_data.generic_particles = ListContainer(particles)
        character.sound_resources = ListContainer()
        character.animations[0].meta.body.asset_id = ids["ANIM"]
        character.animations[0].name = character.animations[0].meta.body.name = "Gallery_idle"
        character.animation_aabb_array[0].anim_id = ids["ANIM"]
        character.animation_aabb_array[0].bounding_box = copy.deepcopy(mesh.aabox)
        for kind, value, codec in (
            ("CMDL", mesh, None),
            ("CSKR", skin, rig.NATIVE_SKIN_V2),
            ("CINF", skeleton, None),
            ("ANIM", native_animation, motion.CORRUPTION_ANIM_ZERO),
            ("CHAR", character, None),
            ("SAND", sand, rig.sand_codec()),
        ):
            self.add(ids[kind], kind, value, codec)
        return {
            **row,
            "native": {kind: f"{value:016x}" for kind, value in ids.items()},
            "scale": scale,
            "center": center,
            "animated_source_bounds": bounds,
            "frames": frames,
            "bones": count,
            "particles": len(particles),
            "material_fidelity": "audited source TEV roles, blending and UV transforms; visual acceptance pending",
            "source_uv_animation_ported": True,
            "effect_sprite_bounds": effect_bounds,
            "live_acceptance": "pending",
        }

    def finish(self):
        for asset in self.converter.converted_assets.values():
            if asset.type not in ("PART", "TXTR"):
                raise ValueError("Unreviewed particle/texture dependency")
            if asset.type == "PART":
                normalize_empty_particle_references(asset.resource)
            self.add(asset.id, asset.type, asset.resource)
        return list(self.resources.values())
