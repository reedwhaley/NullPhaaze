# Corruption rigid pickup rigs and animation events for the native GC engines. Boundary
# names here: align_pickup_internals, fit_hyper_presentation, fit_pickup_internals,
# prepare_pickup_skeleton, rotate.
"""Corruption rigid pickup rigs and animation events for the native GC engines."""

import copy
import math
import struct
from collections import defaultdict

from construct import Container, ListContainer
from retro_data_structures.formats.ancs import Ancs
from retro_data_structures.formats.cinf import Cinf
from retro_data_structures.formats.cskr import Cskr
from retro_data_structures.formats.evnt import Evnt
from retro_data_structures.formats.meta_transition import MetaTransitionType
from retro_data_structures.game_check import Game

from randovania.patching.prime.corruption_animation import Track, decode, encode_compressed
from randovania.patching.prime.corruption_static_mesh import allocate, convert_mesh, native_templates

CHARGE_BEAM_CHARACTER = 0x59CC7F339B6BBF68
HYPERMODE_CHARACTER = 0x1E75BF6DE7531D5E
HYPER_BARE_CHARACTERS = frozenset((0x6DEE19A2C7BA110B, 0xA5534CB39EE8D90F, 0xF69C66580F14E646))
PICKUP_CARRIER_MODEL = 0x07DED1554A4348C6
BOOST_BALL_CHARACTER = 0x017ADBB0E5F48915
HAZARD_SHIELD_CHARACTER = 0x267753B8F16FE297
BOOST_TRAIL_BONE = 6
BOOST_TRAIL_NAME = "Backport_BoostTrail"
BOOST_TRAIL_EFFECTS = frozenset((0xE7B3A9D14D971AEB, 0xE8BE99572D6174CC))


def align_pickup_internals(animation, character):
    """Apply the bounded, visually reviewed pickup presentation adjustments."""
    if character not in (CHARGE_BEAM_CHARACTER, HYPERMODE_CHARACTER, BOOST_BALL_CHARACTER):
        return animation
    result = copy.deepcopy(animation)
    if character == BOOST_BALL_CHARACTER:
        # The source icon adds a second Y rotation below the rolling ball.
        # Keep its bind orientation relative to the ball so both inner meshes
        # roll together; the ball, orbit and canister retain their source tracks.
        icon = result.tracks[5]
        if not icon.rotation:
            raise ValueError("Boost Ball's audited icon rotation track is missing")
        icon.rotation = [icon.rotation[0]] * len(icon.rotation)
        # Follow the ball's orbit and position without inheriting its rapid roll.
        # Both trail systems use this same locator, rather than the oppositely
        # rotating canister/root attachments in the source event set.
        ball = result.tracks[4]
        result.tracks[BOOST_TRAIL_BONE] = Track(
            [(1.0, 0.0, 0.0, 0.0)] * len(ball.rotation), copy.deepcopy(ball.translation), copy.deepcopy(ball.scale)
        )
        return result
    internal, canister = result.tracks[2], result.tracks[3]
    if internal.translation is None or canister.translation is None:
        raise ValueError("Audited beam internal/canister tracks are missing")
    lift = canister.translation[0][2] - internal.translation[0][2]
    internal.translation = [(x, y, z + lift) for x, y, z in internal.translation]
    return result


def fit_hyper_presentation(mesh, character, carrier_bounds):
    """Size bare Hyper cores by their surrounding presentation, like a canister pickup.

    The source cores share the canister pickups' model units. Normalizing their
    small solid meshes to a full canister height enlarged both cores and effects.
    A conservative spherical carrier envelope keeps these source proportions and
    encompasses the Hyper Ball's 2.1-unit rim glow, without changing geometry.
    """
    if character not in HYPER_BARE_CHARACTERS:
        return mesh
    result = copy.deepcopy(mesh)
    radius = max(abs(v) for vector in (carrier_bounds.min, carrier_bounds.max) for v in vector)
    result.aabox = Container(
        min=ListContainer(min(v, -radius) for v in result.aabox.min),
        max=ListContainer(max(v, radius) for v in result.aabox.max),
    )
    return result


def fit_pickup_internals(mesh, skin, character, game):
    """Fit Hazard Shield's rigid interior while retaining the replacement shell size."""
    if character != HAZARD_SHIELD_CHARACTER:
        return mesh
    result = copy.deepcopy(mesh)
    parsed_skin = Cskr.parse(skin, game).raw
    offset = 0
    interior_bone = 2 + (3 if game == Game.PRIME else 0)
    found = False
    for group in parsed_skin.vertex_groups:
        if group.weights_array[0].bone_id == interior_bone:
            found = True
            for index in range(offset, offset + group.vertex_count):
                result.attrib_arrays.positions[index] = list(
                    struct.unpack(">3f", struct.pack(">3f", *(v * 0.75 for v in result.attrib_arrays.positions[index])))
                )
        offset += group.vertex_count
    if not found:
        raise ValueError("Hazard Shield's audited interior weight group is missing")
    return result


def prepare_pickup_skeleton(skeleton, character):
    """Give Boost Ball's two trail systems a shared orbit-space attachment."""
    if character != BOOST_BALL_CHARACTER:
        return skeleton
    result = copy.deepcopy(skeleton)
    bones = {b.id: b for b in result.bones}
    if BOOST_TRAIL_BONE in bones:
        raise ValueError("Boost Ball trail locator would overwrite a source bone")
    locator = copy.deepcopy(bones[4])
    locator.id, locator.parent_id = BOOST_TRAIL_BONE, 3
    locator.rotation = copy.deepcopy(bones[3].rotation)
    locator.local_rotation = [1.0, 0.0, 0.0, 0.0]
    locator.linked_bone_id_array = ListContainer([3])
    bones[3].linked_bone_id_array.append(BOOST_TRAIL_BONE)
    result.bones.append(locator)
    result.build_order_id.insert(0, BOOST_TRAIL_BONE)
    result.bone_names.append(Container(name=BOOST_TRAIL_NAME, bone_id=BOOST_TRAIL_BONE))
    return result


def rotate(quaternion, vector):
    w, x, y, z = quaternion
    a, b, c = vector
    # Unit quaternion vector transform, expressed without a matrix dependency.
    tx, ty, tz = 2 * (y * c - z * b), 2 * (z * a - x * c), 2 * (x * b - y * a)
    return [a + w * tx + y * tz - z * ty, b + w * ty + z * tx - x * tz, c + w * tz + x * ty - y * tx]


def character_template(game):
    """Numeric native ANCS structure; no borrowed game assets are required."""
    character = Container(
        id=0,
        version=6 if game == Game.PRIME else 10,
        name="",
        model_id=0,
        skin_id=0,
        skeleton_id=0,
        animation_names=ListContainer(),
        pas_database=Container(
            magic=b"PAS4", anim_state_count=0, default_anim_state=0xFFFFFFFF, anim_states=ListContainer()
        ),
        particle_resource_data=Container(
            generic_particles=ListContainer(),
            swoosh_particles=ListContainer(),
            unknown=0,
            electric_particles=ListContainer(),
            spawn_particles=None if game == Game.PRIME else ListContainer(),
        ),
        unknown_1=1 if game == Game.PRIME else 0,
        unknown_2=None if game == Game.PRIME else 0,
        animation_aabb_array=ListContainer(),
        effect_array=ListContainer(),
        frozen_model=0,
        frozen_skin=0,
        animation_id_map=ListContainer(),
        spatial_primitives_id=None if game == Game.PRIME else 0xFFFFFFFF,
        unknown_3=None if game == Game.PRIME else 0,
        indexed_animation_aabb_array=None if game == Game.PRIME else ListContainer(),
    )
    return Container(version=1, character_set=Container(version=1, characters=ListContainer([character])))


def reindex_mesh(source, skin, skeleton, game, *, preserve_skin_matrices=False):
    """Expand GPU palette assignments into explicit GC weight-group attributes."""
    mesh = copy.deepcopy(source)
    assignments = defaultdict(dict)
    bones = {b.id: b for b in skeleton.bones}
    for surface in mesh.surfaces:
        bank = surface.header.unk_1
        if not isinstance(bank, int) or bank < 0:
            raise ValueError("Invalid source matrix bank")
        for primitive in surface.primitives:
            for vertex in primitive.vertices:
                matrix = vertex.matrix.position
                if matrix < 0 or matrix % 3 or matrix >= 30:
                    raise ValueError("Unsupported source matrix index")
                palette = bank * 10 + matrix // 3
                if palette >= len(skin.footer.pool_to_skin_idx):
                    raise ValueError("Matrix bank outside source skin")
                group = skin.footer.pool_to_skin_idx[palette]
                if group < 0 or group >= len(skin.vertex_groups):
                    raise ValueError("Matrix palette refers outside source skin")
                weights = skin.vertex_groups[group].weights_array
                if len(weights) != 1 or abs(weights[0].weight - 1) > 0.00001:
                    raise ValueError("Only source-proven rigid weight groups are supported")
                key = (vertex.position, vertex.normal)
                if not (0 <= key[0] < len(source.attrib_arrays.positions)) or not (
                    0 <= key[1] < len(source.attrib_arrays.normals)
                ):
                    raise ValueError("Source vertex attribute outside array")
                assignments[group].setdefault(key, []).append(vertex)
    positions, normals, groups = [], [], []
    for source_group, vertices in sorted(assignments.items()):
        group = copy.deepcopy(skin.vertex_groups[source_group])
        group.vertex_count = len(vertices)
        bone = bones[group.weights_array[0].bone_id]
        for (position, normal), references in vertices.items():
            p = list(source.attrib_arrays.positions[position])
            n = list(source.attrib_arrays.normals[normal])
            if game == Game.PRIME:
                # Prime's CINF lacks inverse-bind orientation. Bake it into the
                # rigid group's vertices and normals; native animation supplies pose rotation.
                inverse = [bone.rotation[0], *(-v for v in bone.rotation[1:])]
                p = [v - origin for v, origin in zip(p, bone.position)]
                p = [v + origin for v, origin in zip(rotate(inverse, p), bone.position)]
                n = rotate(inverse, n)
            index = len(positions)
            positions.append(list(struct.unpack(">3f", struct.pack(">3f", *p))))
            normals.append(list(struct.unpack(">3f", struct.pack(">3f", *n))))
            for vertex in references:
                vertex.position = vertex.normal = index
        group.weights_array[0].bone_id += 3 if game == Game.PRIME else 0
        groups.append(group)
    mesh.attrib_arrays.positions = ListContainer(positions)
    mesh.attrib_arrays.normals = ListContainer(normals)
    if len(positions) >= 65536:
        raise ValueError("Expanded mesh exceeds GX index range")
    if game == Game.PRIME:
        footer = Container(
            unk_a=Container(first=0xFFFFFFFF, other=len(positions)),
            unk_b=Container(first=0xFFFFFFFF, other=len(normals)),
            trailing_bytes=b"",
        )
    else:
        # Keep each surface's original ten-slot bank. The expanded weight groups
        # may omit unused source groups, so remap palette entries to their new
        # indices instead of assuming that every surface uses the first bank.
        if preserve_skin_matrices:
            group_indices = {source_group: index for index, source_group in enumerate(sorted(assignments))}
            pool = [group_indices.get(group, 65535) for group in skin.footer.pool_to_skin_idx]
        else:
            pool = list(range(len(groups)))
        pool += [65535] * ((-len(pool)) % 10)
        footer = Container(
            pool_to_skin_idx=ListContainer(pool),
            trailing_bytes=b"".join(bytes([i]) * g.vertex_count for i, g in enumerate(groups)),
        )
    new_skin = Container(unk=None, vertex_groups=ListContainer(groups), footer=footer)
    return mesh, Cskr(new_skin, game).build()


def attached_particle_event(event, converted_id, index, duration, bone_names, game, character=None):
    target = copy.deepcopy(event)
    target.base.unk_1 = 1
    target.base.unique = 1
    target.base.index = index
    target.base.unk_2 = target.base.unk_extra = None
    target.duration = max(1, math.ceil(duration * 60) - 1)
    target.particle.id = converted_id
    bone = (
        BOOST_TRAIL_BONE
        if character == BOOST_BALL_CHARACTER and event.particle.id in BOOST_TRAIL_EFFECTS
        else event.unk_id
    )
    if game == Game.PRIME:
        target.bone_name = bone_names[bone]
        target.bone_id = None
    else:
        target.bone_id = bone
    target.effect_scale = event.unk_float
    # ContinuousSystem moves existing particles with the animated bone.
    # ContinuousEmitter leaves previously emitted particles in world space.
    target.transform_type = 2
    target.unk_float = target.unk_id = None
    return target


def convert(source, template, model, character, textures, game, occupied, particles=None):
    # A Wii CHAR is not a GC ANCS with a new extension. Convert its mesh/skin,
    # skeleton indices, animation and event references into the destination
    # layouts, then bind them through a native character template.
    char = source.get_parsed_asset(character).raw
    skeleton = prepare_pickup_skeleton(copy.deepcopy(source.get_parsed_asset(char.skeleton_id).raw), character)
    bone_names = {b.bone_id: b.name for b in skeleton.bone_names}
    skin = source.get_parsed_asset(char.skin_id).raw
    mesh = source.get_parsed_asset(model).raw
    preserve_skin_matrices = game == Game.ECHOES and character in (CHARGE_BEAM_CHARACTER, HYPERMODE_CHARACTER)
    mesh, encoded_skin = reindex_mesh(mesh, skin, skeleton, game, preserve_skin_matrices=preserve_skin_matrices)
    mesh = fit_pickup_internals(mesh, encoded_skin, character, game)
    if character in HYPER_BARE_CHARACTERS:
        carrier_bounds = source.get_parsed_asset(PICKUP_CARRIER_MODEL).raw.aabox
        mesh = fit_hyper_presentation(mesh, character, carrier_bounds)
    encoded_mesh = convert_mesh(
        mesh,
        native_templates(),
        game,
        textures,
        "catalog",
        skinned=True,
        animated_uv=True,
        preserve_skin_matrices=preserve_skin_matrices,
    )
    offset, parent_marker = (3, 2) if game == Game.PRIME else (0, 97)
    # Bone IDs, parent sentinels, build order and names must move together.
    # Adjusting only CINF would leave CSKR/animation references on the old rig.
    for bone in skeleton.bones:
        bone.id += offset
        bone.parent_id = parent_marker if bone.parent_id == 147 else bone.parent_id + offset
        bone.linked_bone_id_array = ListContainer(
            parent_marker if b == 147 else b + offset for b in bone.linked_bone_id_array
        )
    skeleton.build_order_id = ListContainer(b + offset for b in skeleton.build_order_id)
    for bone_name in skeleton.bone_names:
        bone_name.bone_id += offset
    animation = next((a for a in char.animations if "spin" in a.name and "nospin" not in a.name), char.animations[0])
    # This is a pickup presentation converter. Select its spin clip when present
    # and require a direct animation leaf; arbitrary character state machines
    # are outside the supported conversion, even if their CHAR parses in RDS.
    if animation.meta.type != 0:
        raise ValueError("Unsupported pickup animation tree")
    animation_id = animation.meta.body.asset_id
    ids = {
        kind: allocate(kind, identity, game, occupied)
        for kind, identity in (
            ("ANCS", character),
            ("CINF", char.skeleton_id),
            ("CSKR", char.skin_id),
            ("ANIM", animation_id),
            ("EVNT", animation_id),
        )
    }
    clip = align_pickup_internals(decode(source.get_raw_asset(animation_id).data), character)
    encoded_animation = encode_compressed(clip, game, event_id=ids["EVNT"])
    root = copy.deepcopy(template) if template is not None else character_template(game)
    target_char = root.character_set.characters[0]
    root.character_set.characters = ListContainer([target_char])
    target_char.id, target_char.name = 0, char.name
    target_char.model_id = allocate("CMDL", model, game, set())
    target_char.skin_id, target_char.skeleton_id = ids["CSKR"], ids["CINF"]
    target_char.frozen_model = target_char.frozen_skin = 0 if game == Game.PRIME else 0xFFFFFFFF
    target_char.animation_names = ListContainer(
        [Container(animation_id=0, unknown="" if game == Game.PRIME else None, name=animation.name)]
    )
    aabb = next(a.bounding_box for a in char.animation_aabb_array if a.anim_id == animation_id)
    if character in HYPER_BARE_CHARACTERS:
        aabb = Container(
            min=ListContainer(min(a, b) for a, b in zip(aabb.min, mesh.aabox.min)),
            max=ListContainer(max(a, b) for a, b in zip(aabb.max, mesh.aabox.max)),
        )
    target_char.animation_aabb_array = ListContainer([Container(name=animation.name, bounding_box=copy.deepcopy(aabb))])
    if game == Game.ECHOES:
        target_char.indexed_animation_aabb_array = ListContainer([Container(id=0, bounding_box=copy.deepcopy(aabb))])
    target_char.effect_array = ListContainer()
    target_char.animation_id_map = ListContainer([0])
    psd = target_char.particle_resource_data
    psd.generic_particles = ListContainer()
    psd.swoosh_particles = ListContainer()
    psd.electric_particles = ListContainer()
    psd.spawn_particles = ListContainer() if game == Game.ECHOES else None
    target_char.pas_database = copy.deepcopy(char.pas_database)
    meta = copy.deepcopy(animation.meta)
    meta.body.asset_id = ids["ANIM"]
    meta.body.primitive_id = 0
    root.animation_set = Container(
        table_count=4 if game == Game.ECHOES else 1,
        animations=ListContainer([Container(name=animation.name, meta=meta)]),
        transitions=ListContainer(),
        default_transition=Container(type=MetaTransitionType.Snap, body=Container()),
        additive=Container(additive_animations=ListContainer(), default_fade_in_time=0.0, default_fade_out_time=0.0)
        if game == Game.ECHOES
        else None,
        half_transitions=ListContainer() if game == Game.ECHOES else None,
        animation_resources=ListContainer([Container(anim_id=ids["ANIM"], event_id=ids["EVNT"])])
        if game == Game.PRIME
        else None,
        event_sets=ListContainer() if game == Game.ECHOES else None,
    )
    events = Container(
        version=2,
        bool_poi_nodes=ListContainer(),
        int32_poi_nodes=ListContainer(),
        particle_poi_nodes=ListContainer(),
        sound_poi_nodes=ListContainer(),
    )
    for timestamp, state in ((0.0, 2), (clip.duration, 0)):
        base = Container(
            unk_1=1,
            name="Loop",
            type=0,
            timestamp=Container(time=timestamp, differential_state=state),
            index=0,
            unk_2=None,
            unique=1,
            weight=1.0,
            character_index=-1,
            flags=0,
            unk_extra=None,
        )
        events.bool_poi_nodes.append(Container(base=base, value=1))
    if particles is not None:
        sand = source.get_parsed_asset(char.sand_id).raw
        event_set = next((e for e in sand.anim_events if e.id == animation_id), None)
        if event_set is not None:
            for event in event_set.event_sets:
                identity = event.particle.id
                try:
                    converted_id = particles.convert_id(identity)
                except Exception as error:
                    particles.approximations[f"{identity:016X}"] = {
                        "type": event.particle.type,
                        "omitted_effect": str(error)[-400:],
                    }
                    continue
                target_event = attached_particle_event(
                    event, converted_id, len(events.particle_poi_nodes), clip.duration, bone_names, game, character
                )
                events.particle_poi_nodes.append(target_event)
                kinds = {"PART": psd.generic_particles, "ELSC": psd.electric_particles, "SWHC": psd.swoosh_particles}
                if converted_id not in kinds[event.particle.type]:
                    kinds[event.particle.type].append(converted_id)
    if game == Game.ECHOES:
        root.animation_set.event_sets = ListContainer([events])
    resources = {
        ids["ANCS"]: ("ANCS", Ancs(root, game).build()),
        ids["CINF"]: ("CINF", Cinf(skeleton, game).build()),
        ids["CSKR"]: ("CSKR", encoded_skin),
        ids["ANIM"]: ("ANIM", encoded_animation),
        ids["EVNT"]: ("EVNT", Evnt(events, game).build()),
        target_char.model_id: ("CMDL", encoded_mesh),
    }
    return ids, resources
