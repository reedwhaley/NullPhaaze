# Bounded, asset-only Corruption pickup backport for GC Prime/Echoes. Boundary names here:
# allocate, checked_material, convert_vertex_matrix, convert_mesh, build_mesh.
"""Bounded, asset-only Corruption pickup backport for GC Prime/Echoes.

Converts geometry and native GX materials for static or explicitly reindexed rigs.
Game data is read from user-provided extractions and is never bundled with code.
"""

from __future__ import annotations

import copy
import hashlib
import math
import struct

from construct import Container, Int32ub, ListContainer, Padding, Rebuild, Struct
from retro_data_structures.data_section import DataSection
from retro_data_structures.formats.cmdl import Cmdl
from retro_data_structures.game_check import Game

SOURCE_MODEL = 0x8F865363AED3AFE6
SOURCE_CHARACTER = 0x778E1ABA10D9B9E0
TEMPLATE_MODEL = 0x86908399
NAME = "prime3_EnergyTank_Static"
PROFILES = {
    "energy-tank": (SOURCE_MODEL, SOURCE_CHARACTER, NAME),
    "hyper-missile": (0x6FF70067566550DA, 0xA5534CB39EE8D90F, "prime3_HyperMissile_Static"),
}


def allocate(kind, identity, target, occupied):
    """Deterministic 32-bit ID; reject collisions, never truncate source IDs."""
    value = int.from_bytes(
        hashlib.sha256(f"corruption-backport-v1/{target.name}/{kind}/{identity:016X}".encode()).digest()[:4], "big"
    )
    if value in occupied or value in (0, 0xFFFFFFFF):
        raise ValueError(f"Asset ID collision: {value:08X}")
    occupied.add(value)
    return value


def checked_material(source, templates, texture_ids, game, index, profile="energy-tank"):
    if profile not in PROFILES:
        raise ValueError("Unsupported source profile")
    passes = [e.body for e in source.elements if e.type == "PASS"]
    roles = [p.subtype for p in passes]
    if roles == ["CLR ", "INCA"] and source.flags == 129:
        result = copy.deepcopy(templates[0])
    elif roles == ["INCA"] and source.flags == 161:
        result = copy.deepcopy(templates[1])
    else:
        raise ValueError("Unsupported source material roles/blending")
    if source.vertex_attribute_flags != 0x8100030F:
        raise ValueError("Unsupported source vertex layout")
    hyper = profile == "hyper-missile"
    expected = [("PASS", role) for role in roles] + [("INT ", "BNIF"), ("CLR ", "CLR "), ("END ", None)]
    if hyper:
        expected.insert(len(roles), ("INT ", "BLOD"))
    if [(e.type, e.body.subtype if e.body is not None else None) for e in source.elements] != expected:
        raise ValueError("Unknown material operation")
    integers = {e.body.subtype: e.body.value for e in source.elements if e.type == "INT "}
    if integers != ({"BLOD": 0, "BNIF": 153} if hyper else {"BNIF": 32}):
        raise ValueError("Unknown bloom configuration")
    for p in passes:
        if p.uv_animation or p.uv_source != 0 or p.flags != (0 if p.subtype == "CLR " else (6 if hyper else 4)):
            raise ValueError("Animated or unsupported source pass")
    result.group_index = index
    result.texture_indices = ListContainer(texture_ids.index(p.id) for p in passes)
    result.vertex_attribute_flags = 0x30F | (0x81000000 if game == Game.ECHOES else 0)
    result.flags = (result.flags | 0x3000) if game == Game.ECHOES else (result.flags | 1) & ~0x3000
    result.unk_1 = result.unk_2 = 0 if game == Game.ECHOES else None
    # Both source passes use UV0. Keep two generators for the two TEV stages,
    # but select UV0 for both instead of requiring an absent second UV stream.
    result.texgen_flags = ListContainer([templates[0].texgen_flags[0]] * len(passes))
    tint = next(e.body.value for e in source.elements if e.type == "CLR ")
    if roles == ["CLR ", "INCA"] and tint != 255:
        raise ValueError("Unsupported diffuse/emission tint")
    if roles == ["INCA"]:
        # GX_CC_KONST = 14, GX_KCSEL_K0 = 12. Multiply texture RGB by K0.
        result.flags = (result.flags | 8) & ~0x80
        result.konst_colors = ListContainer([tint])
        stage = result.tev_stages[0]
        stage.color_input_flags = (stage.color_input_flags & ~(31 << 5)) | (14 << 5)
        stage.konst_color_input = 12
    return result


def convert_vertex_matrix(vertex, game, preserve_skin_matrices):
    if game == Game.ECHOES:
        if not preserve_skin_matrices:
            vertex.matrix.position = 0
        vertex.matrix.tex["6"] = 0
    else:
        vertex.matrix.position = vertex.matrix.tex["6"] = None


def convert_mesh(
    source,
    templates,
    game,
    target_texture_ids,
    profile="energy-tank",
    *,
    skinned=False,
    animated_uv=False,
    preserve_skin_matrices=False,
    transparent_depth_write=False,
):
    if game not in (Game.PRIME, Game.ECHOES):
        raise ValueError("Target must be GameCube Prime or Echoes")
    accepted_flags = (0, 1, 2, 3) if profile == "catalog" else (1,)
    if source.version != 5 or source.flags not in accepted_flags or len(source.material_sets) != 1:
        raise ValueError("Unsupported source CMDL")
    raw = copy.deepcopy(source)
    textures = list(
        dict.fromkeys(p.body.id for m in source.material_sets[0].materials for p in m.elements if p.type == "PASS")
    )
    if set(textures) != set(target_texture_ids):
        raise ValueError("Incomplete texture mapping")
    raw.version = 2 if game == Game.PRIME else 4
    # The result is static: no external skin/skeleton and no matrix palette.
    if not skinned:
        raw.flags &= ~1
    raw.material_sets = ListContainer(
        [
            Container(
                texture_file_ids=ListContainer(target_texture_ids[t] for t in textures),
                materials=ListContainer(
                    (
                        catalog_material(
                            m,
                            templates,
                            textures,
                            game,
                            i,
                            animated_uv=animated_uv,
                            transparent_depth_write=transparent_depth_write,
                        )
                        if profile == "catalog"
                        else checked_material(m, templates, textures, game, i, profile)
                    )
                    for i, m in enumerate(source.material_sets[0].materials)
                ),
            )
        ]
    )
    for surface in raw.surfaces:
        if surface.header.material_index >= len(raw.material_sets[0].materials):
            raise ValueError("Surface material outside material set")
        if game == Game.ECHOES:
            surface.header.unk_1 = surface.header.unk_1 if preserve_skin_matrices else 0
            surface.header.unk_2 = 0
        else:
            surface.header.unk_1 = surface.header.unk_2 = None
        surface.header.extra_data = b""
        for primitive in surface.primitives:
            if primitive.type == 0 and not primitive.vertices:
                continue  # display-list alignment parsed as empty commands
            command = primitive.type & 0xF8 if profile == "catalog" else primitive.type
            if command not in (0x80, 0x90, 0x98, 0xA0):
                raise ValueError("Unsupported primitive command")
            for vertex in primitive.vertices:
                if profile != "catalog" and (vertex.matrix.position != 0 or vertex.matrix.tex["6"] != 0):
                    raise ValueError("Non-rigid matrix palette")
                if not (
                    0 <= vertex.position < len(raw.attrib_arrays.positions)
                    and 0 <= vertex.normal < len(raw.attrib_arrays.normals)
                    and (vertex.tex["0"] is None or 0 <= vertex.tex["0"] < len(raw.attrib_arrays.uvs))
                ):
                    raise ValueError("Vertex attribute index out of range")
                convert_vertex_matrix(vertex, game, preserve_skin_matrices)
    for points in (raw.attrib_arrays.positions, raw.attrib_arrays.normals, raw.attrib_arrays.uvs):
        if any(not math.isfinite(v) for p in points for v in p):
            raise ValueError("Non-finite mesh attribute")
    data = build_mesh(raw, game)
    checked = Cmdl.parse(data, game)._raw

    def geometry(m):
        return [
            (
                s.header.material_index,
                [
                    (p.type, [(v.position, v.normal, v.tex["0"]) for v in p.vertices])
                    for p in s.primitives
                    if p.vertices
                ],
            )
            for s in m.surfaces
        ]

    if geometry(checked) != geometry(source):

        def summary_diff():
            for i, (a, b) in enumerate(zip(geometry(source), geometry(checked))):
                if a == b:
                    continue
                for j, (pa, pb) in enumerate(zip(a[1], b[1])):
                    if pa != pb:
                        return i, j, pa[0], pb[0], len(pa[1]), len(pb[1]), pa[1][:2], pb[1][:2]
                return i, a[0], b[0], len(a[1]), len(b[1])
            return len(source.surfaces), len(checked.surfaces)

        raise ValueError(f"Display-list geometry changed: {summary_diff()}")
    for field in ("positions", "normals", "uvs"):
        original = raw.attrib_arrays[field]
        actual = checked.attrib_arrays[field]
        # Attribute sections contain alignment padding interpreted as extra values.
        if actual[: len(original)] != original:
            raise ValueError(f"{field} changed during serialization")
    return data


def build_mesh(raw, game):
    """Serialize with an explicitly allocated surface-offset table."""
    # RDS 0.44's Seek-only surface-offset reservation does not extend BytesIO.
    # With >7 surfaces its 32-byte section overlaps the first surface. Use a local
    # codec that writes the reservation, leaving the installed parser untouched.
    table = "_surface_header" / DataSection(
        Struct(
            num_surfaces=Rebuild(Int32ub, lambda ctx: len(ctx._.surfaces)),
            end_offsets=Padding(lambda ctx: 4 * ctx.num_surfaces),
        )
    )
    codec = Struct(*(table if s.name == "_surface_header" else s for s in Cmdl.construct_class(game).subcons))
    return codec.build(raw, target_game=game)


def pack_inputs(*values):
    return sum(value << (5 * i) for i, value in enumerate(values))


def catalog_material(source, templates, texture_ids, game, index, *, animated_uv=False, transparent_depth_write=False):
    """Approximate source materials with native GX stages and optional UV animation."""
    if source.vertex_attribute_flags not in (0x8100030F, 0x8100000F, 0x30F, 0xF):
        raise ValueError("Unaudited catalog vertex layout")
    if source.flags not in (1, 9, 33, 129, 161, 169, 65665, 65697):
        raise ValueError("Unaudited catalog blending flags")
    passes = []
    tint, opacity = 0xFFFFFFFF, 255
    for element in source.elements:
        body = element.body
        if element.type == "PASS":
            if body.subtype not in ("CLR ", "INCA", "RFLV", "RFLD", "XRAY"):
                raise ValueError("Unaudited catalog texture role")
            if body.uv_source != 0 or body.flags not in (0, 4, 5, 6):
                raise ValueError("Unaudited texture pass")
            if body.subtype in ("CLR ", "INCA") or (animated_uv and body.subtype in ("RFLV", "RFLD")):
                passes.append(body)
        elif element.type == "CLR " and body.subtype == "CLR ":
            tint = body.value
        elif element.type == "INT " and body.subtype in ("OPAC", "BNIF", "BLOD", "BLOI"):
            if not 0 <= body.value <= 255:
                raise ValueError("Invalid material parameter")
            if body.subtype == "OPAC":
                opacity = body.value
        elif element.type != "END ":
            raise ValueError("Unaudited material operation")
    # Catalog CLR=000000FF is an unused color operand when textured. Multiplying
    # it into diffuse/emission would turn the entire pickup black. Preserve the
    # explicit nonzero RGB tint used by the emission-only materials.
    if passes and (tint & 0xFFFFFF00) == 0:
        tint = 0xFFFFFFFF
    if len(passes) > (4 if animated_uv else 2) or len({p.subtype for p in passes}) != len(passes):
        raise ValueError("Duplicate diffuse/emission passes")
    result = copy.deepcopy(templates[0])
    result.flags = ((result.flags | 8) & 0xFBFF) | (((1 << len(passes)) - 1) << 16)
    result.unk_1 = result.unk_2 = 0 if game == Game.ECHOES else None
    result.flags = result.flags | 0x3000 if game == Game.ECHOES else (result.flags | 1) & ~0x3000
    result.group_index = index
    result.vertex_attribute_flags = (
        source.vertex_attribute_flags if game == Game.ECHOES else source.vertex_attribute_flags & 0xFFFFFF
    )
    result.konst_colors = ListContainer([(tint & 0xFFFFFF00) | (((tint & 255) * opacity) // 255)])
    result.blend_source_factor, result.blend_destination_factor = (1, 0)
    if source.flags & 8:
        result.flags |= 16
        result.blend_source_factor, result.blend_destination_factor = (4, 5)
    elif source.flags & 32:
        result.flags |= 16
        result.blend_source_factor, result.blend_destination_factor = (1, 1)
    if source.flags & (8 | 32) and not transparent_depth_write:
        # Transparent pickup shells and effect meshes must not occlude later
        # particles. The opaque template's depth-write bit is not a blend flag.
        result.flags &= ~0x80
    result.color_channel_flags = ListContainer([12288])
    result.texture_indices = ListContainer(texture_ids.index(p.id) for p in passes)
    result.tev_stages = ListContainer()
    result.tev_inputs = ListContainer()
    for i, p in enumerate(passes or [None]):
        stage = copy.deepcopy(templates[0].tev_stages[0])
        # (texture * K0) + previous; constants alone for an untextured surface.
        stage.color_input_flags = pack_inputs(15, 14, 8, 0 if i else 15) if p else pack_inputs(15, 15, 15, 14)
        stage.alpha_input_flags = pack_inputs(7, 4, 6, 7) if p else pack_inputs(7, 7, 7, 6)
        stage.konst_color_input, stage.konst_alpha_input = 12, 28
        stage.rasterized_color_input = 6
        if p is not None and p.subtype == "RFLV":
            # Store the reflectivity map in GX_TEVREG1 while preserving PREV.
            stage.color_input_flags = pack_inputs(15, 15, 15, 8)
            stage.color_combine_flags = 0x100 | (2 << 9)
            stage.alpha_input_flags = pack_inputs(7, 7, 7, 0)
        elif p is not None and p.subtype == "RFLD":
            # Add the reflection map, modulated by reflectivity where supplied.
            reflectivity = 4 if any(x.subtype == "RFLV" for x in passes) else 12
            stage.color_input_flags = pack_inputs(15, 8, reflectivity, 0 if i else 15)
            stage.alpha_input_flags = pack_inputs(7, 7, 7, 0)
        result.tev_stages.append(stage)
        result.tev_inputs.append(
            Container(padding=0, texture_tev_input=i if p else 255, tex_coord_tev_input=i if p else 255)
        )
    result.texgen_flags = ListContainer([templates[0].texgen_flags[0]] * len(passes))
    result.material_animations_section_size = 4
    result.uv_animations = ListContainer()
    if animated_uv:
        install_uv_animations(result, passes)
    return result


def install_uv_animations(result, passes):
    """Install source UV operations with verified native parameter layouts."""
    for pass_index, source_pass in enumerate(passes):
        data = bytes(source_pass.uv_animation)
        if not data:
            continue
        if len(data) < 8:
            raise ValueError("Truncated source UV animation")
        source_uv, matrix_config, kind = struct.unpack_from(">HHI", data)
        # The catalog's SRT operation is unit scale, zero rotation/offset and
        # pure translation. That restricted case is exactly native UV_SCROLL.
        if (source_uv, matrix_config, kind) == (2, 1, 8):
            if len(data) != 44:
                raise ValueError("Invalid source SRT animation size")
            transform, *srt = struct.unpack_from(">I8f", data, 8)
            if not all(math.isfinite(v) for v in srt):
                raise ValueError("Non-finite SRT animation")
            if transform != 0 or srt[:6] != [1.0, 1.0, 0.0, 0.0, 0.0, 0.0]:
                continue
            kind, parameters = 2, (0.0, 0.0, srt[6], srt[7])
        else:
            parameters = None
        reflection = (source_uv, matrix_config, kind) == (1, 3, 0)
        if not reflection and ((source_uv, matrix_config) != (2, 1) or kind not in (2, 3, 4, 5)):
            continue
        count = 0 if reflection else (2 if kind == 3 else 4)
        if parameters is None:
            if len(data) != 8 + count * 4:
                raise ValueError("Invalid source UV animation size")
            parameters = struct.unpack_from(f">{count}f", data, 8)
        if not all(math.isfinite(v) for v in parameters):
            raise ValueError("Non-finite UV animation")
        animation_index = len(result.uv_animations)
        result.texgen_flags[pass_index] = (result.texgen_flags[pass_index] & ~0x3E00) | (animation_index * 3 << 9)
        if reflection:
            result.texgen_flags[pass_index] = (result.texgen_flags[pass_index] & ~0x1F0) | (1 << 4)
        result.uv_animations.append(Container(animation_type=kind, parameters=ListContainer(parameters)))
        result.material_animations_section_size += 4 + count * 4


def native_templates():
    """GX material programs; contains no game textures or geometry."""
    stage = Container(
        color_input_flags=500047,
        alpha_input_flags=138471,
        color_combine_flags=256,
        alpha_combine_flags=256,
        padding=0,
        konst_alpha_input=0,
        konst_color_input=0,
        rasterized_color_input=4,
    )
    emission = copy.deepcopy(stage)
    emission.color_input_flags, emission.alpha_input_flags, emission.rasterized_color_input = 12559, 204007, 6
    first = Container(
        flags=200835,
        texture_indices=ListContainer([2, 1]),
        vertex_attribute_flags=3855,
        unk_1=None,
        unk_2=None,
        group_index=0,
        konst_colors=None,
        blend_destination_factor=0,
        blend_source_factor=1,
        reflection_indirect_texture_slot_index=None,
        color_channel_flags=ListContainer([12289]),
        tev_stages=ListContainer([stage, emission]),
        tev_inputs=ListContainer(
            [
                Container(padding=0, texture_tev_input=0, tex_coord_tev_input=0),
                Container(padding=0, texture_tev_input=1, tex_coord_tev_input=1),
            ]
        ),
        texgen_flags=ListContainer([2014272, 2014288]),
        material_animations_section_size=4,
        uv_animations=ListContainer(),
    )
    second = copy.deepcopy(first)
    second.flags, second.group_index, second.vertex_attribute_flags = 69651, 1, 783
    second.texture_indices = ListContainer([0])
    second.blend_destination_factor = 1
    second.color_channel_flags = ListContainer([12288])
    stage = copy.deepcopy(emission)
    stage.color_input_flags = 500111
    second.tev_stages = ListContainer([stage])
    second.tev_inputs = ListContainer([Container(padding=0, texture_tev_input=0, tex_coord_tev_input=0)])
    second.texgen_flags = ListContainer([2014272])
    return [first, second]
