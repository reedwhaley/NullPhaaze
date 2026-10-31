# Source-semantic materials and bounded rigid animation for the private gallery. Boundary
# names here: material_flags, material_roles, native_uv, scalar_bound,
# particle_sprite_bound.
"""Source-semantic materials and bounded rigid animation for the private gallery."""

import math
import struct

import numpy as np


def material_flags(template_flags, blend):
    """Change blend selection without discarding native vertex capabilities."""
    selection = {(1, 0): 0, (1, 1): 0x20, (4, 5): 0x8, (0, 1): 0x8}
    if blend not in selection:
        raise ValueError("Unreviewed source blending")
    return (template_flags & ~0x38) | selection[blend]


def material_roles(source):
    """Translate the catalog's audited GX combine operations, not texture order."""
    roles = []
    for stage, inputs in zip(source.tev_stages, source.tev_inputs, strict=True):
        color = tuple((stage.color_input_flags >> (5 * i)) & 15 for i in range(4))
        slot = inputs.texture_tev_input
        if slot == 255:
            if color != (15, 15, 15, 15):
                raise ValueError("Unreviewed untextured gallery combiner")
            continue
        role = {
            (15, 10, 8, 15): "CLR ",  # texture multiplied by raster lighting
            (15, 12, 8, 15): "INCA",  # unlit additive texture
            (15, 8, 12, 0): "INCA",  # emission added to previous color
            (15, 15, 15, 8): "RFLV",  # reflection mask stored in register two
            (15, 6, 8, 0): "RFLD",  # mask times environment added to previous
        }.get(color)
        if role is None or not 0 <= slot < len(source.texture_indices):
            raise ValueError(f"Unreviewed gallery combiner {color}")
        if role == "CLR " and not any(flags & 1 for flags in source.color_channel_flags):
            role = "INCA"
        if role in [r[0] for r in roles]:
            raise ValueError("Native semantic shader cannot represent duplicate roles")
        roles.append((role, slot, inputs.tex_coord_tev_input))
    return roles


def native_uv(source, generator):
    if not 0 <= generator < len(source.texgen_flags):
        return 0, []
    flags = source.texgen_flags[generator]
    coordinate = (flags >> 4) & 31
    uv = coordinate - 4 if 4 <= coordinate < 12 else 0
    matrix = ((flags >> 9) & 31) // 3
    if matrix == 10:
        return uv, []
    if matrix >= len(source.uv_animations):
        raise ValueError("Source texture animation matrix is absent")
    animation = source.uv_animations[matrix]
    if animation.animation_type not in range(8):
        raise ValueError("Unreviewed source texture animation")
    origin = 1 if coordinate == 1 else 0 if coordinate == 0 else 2
    configuration = 3 if animation.animation_type in (0, 1, 6, 7) else 1
    data = struct.pack(">HHI", origin, configuration, animation.animation_type)
    data += struct.pack(">" + "f" * len(animation.parameters), *animation.parameters)
    return uv, list(data)


def scalar_bound(element, frames):
    """Conservative magnitude bound for the catalog's particle size expressions."""
    kind, body = element.type, element.body
    if kind == "NONE":
        return 0.0
    if kind == "CNST":
        return abs(float(body))
    if kind in ("KEYE", "KEYP"):
        return max(map(abs, body["keys"]), default=0.0)
    if kind == "PSLL":
        return float(frames)
    if kind == "SCAL":
        return frames * scalar_bound(body, frames)
    if kind in ("IRND", "RAND", "LFTW", "ISWT"):
        return max(scalar_bound(body.a, frames), scalar_bound(body.b, frames))
    if kind == "ADD_":
        return scalar_bound(body.a, frames) + scalar_bound(body.b, frames)
    if kind == "MULT":
        return scalar_bound(body.a, frames) * scalar_bound(body.b, frames)
    raise ValueError(f"Unreviewed particle size expression {kind}")


def particle_sprite_bound(identity, lookup, cache=None):
    cache = {} if cache is None else cache
    if identity in cache:
        return cache[identity]
    particle = lookup(identity)
    fields = {e.type: e.body for e in particle.elements}
    frames = scalar_bound(fields["LTME"], 1)
    size = scalar_bound(fields["SIZE"], frames)
    if fields.get("LINE") and fields["LINE"].value:
        size = max(size, *(scalar_bound(fields[k], frames) for k in ("LENG", "WIDT") if k in fields))
    children = []
    for key in ("IDTS", "ICTS", "IITS"):
        if key in fields and fields[key].type != "NONE" and fields[key].body not in (0, 0xFFFFFFFFFFFFFFFF):
            children.append(fields[key].body)
    if "KSSM" in fields and fields["KSSM"].magic != "NONE":
        children.extend(c.id for s in fields["KSSM"].value.spawns for c in s.v2)
    for child in children:
        size = max(size, particle_sprite_bound(child, lookup, cache))
    if not math.isfinite(size) or size < 0:
        raise ValueError("Invalid particle display bound")
    cache[identity] = size
    return size


def gallery_effect_scale(model_scale, source_scale, sprite_bound):
    # The live paired controls showed that independently shrinking particles
    # removes visible components. Preserve their scale relative to the mesh.
    if not all(math.isfinite(v) and v >= 0 for v in (model_scale, source_scale, sprite_bound)):
        raise ValueError("Invalid particle scale input")
    result = model_scale * source_scale
    if not math.isfinite(result):
        raise ValueError("Invalid particle scale product")
    return result


def animated_bounds(mesh, skin, skeleton, tracks, frames):
    """Enclose every rendered rigid vertex at every baked animation key."""
    bones = {b.id: b for b in skeleton.bones}
    points = np.array(mesh.attrib_arrays.positions, dtype=float)
    referenced = sorted({v.position for s in mesh.surfaces for p in s.primitives for v in p.vertices})
    groups = []
    start = 0
    for group in skin.vertex_groups:
        end = start + group.vertex_count
        indices = referenced if len(skin.vertex_groups) == 1 else [i for i in referenced if start <= i < end]
        if indices:
            bone = group.weights_array[0].bone_id
            groups.append((bone, points[indices] - np.array(bones[bone].position)))
        start = end
    if sum(len(p) for _, p in groups) != len(referenced):
        raise ValueError("Rigid pose bounds do not cover rendered vertices")
    minimum, maximum = np.full(3, math.inf), np.full(3, -math.inf)
    for frame in range(frames):
        matrices = {}

        def matrix(identity):
            if identity in matrices:
                return matrices[identity]
            bone = bones[identity]
            parent = bones.get(bone.parent_id)
            channels = tracks.get(identity, {})
            translation = channels.get("translation")
            t = (
                translation[frame]
                if translation
                else [value - (parent.position[i] if parent else 0) for i, value in enumerate(bone.position)]
            )
            rotations = channels.get("rotation")
            w, x, y, z = rotations[frame] if rotations else (1, 0, 0, 0)
            scales = channels.get("scale")
            scale = scales[frame] if scales else (1, 1, 1)
            local = np.eye(4)
            local[:3, :3] = np.array(
                [
                    [1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
                    [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
                    [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)],
                ]
            ) @ np.diag(scale)
            local[:3, 3] = t
            result = matrix(parent.id) @ local if parent else local
            matrices[identity] = result
            return result

        for bone, vertices in groups:
            transform = matrix(bone)
            posed = vertices @ transform[:3, :3].T + transform[:3, 3]
            minimum = np.minimum(minimum, posed.min(axis=0))
            maximum = np.maximum(maximum, posed.max(axis=0))
    if not np.isfinite([minimum, maximum]).all():
        raise ValueError("Invalid posed gallery bounds")
    return minimum.tolist(), maximum.tolist()
