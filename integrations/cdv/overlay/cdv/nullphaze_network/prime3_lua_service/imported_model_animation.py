# Bounded animation conversion for the isolated Prime Ice Beam experiment. Boundary names
# here: signed, source_delta, quaternion, interpolate_rotation, decode_prime.
"""Bounded animation conversion for the isolated Prime Ice Beam experiment.

Corruption format zero was checked against its retail stream reader. This is
not the similarly named Prime/Echoes ANIM layout in retro-data-structures.
"""

import math

from construct import Array, Bytes, Const, Float32b, GreedyBytes, Int8ub, Int16ub, Int32ub, PrefixedArray, Struct, this

CORRUPTION_ANIM_ZERO = Struct(
    "compression" / Const(0, Int32ub),
    "version" / Int16ub,
    "duration" / Struct("time" / Float32b, "differential_state" / Int32ub),
    "key_interval" / Struct("time" / Float32b, "differential_state" / Int32ub),
    "key_count" / Int32ub,
    "root_bone_id" / Int32ub,
    "bone_channel_index_array" / PrefixedArray(Const(150, Int32ub), Int8ub),
    "rotation_channel_index_array" / PrefixedArray(Int32ub, Int8ub),
    "translation_channel_index_array" / PrefixedArray(Int32ub, Int8ub),
    "scale_channel_index_array" / PrefixedArray(Int32ub, Int8ub),
    "scale_key_array" / PrefixedArray(Int32ub, Array(3, Float32b)),
    "rotation_key_array" / PrefixedArray(Int32ub, Array(4, Float32b)),
    "translation_key_array" / PrefixedArray(Int32ub, Array(3, Float32b)),
    "auxiliary_count" / Int16ub,
    "auxiliary_stride" / Int8ub,
    "auxiliary_data" / Bytes(this.auxiliary_count * this.auxiliary_stride),
    "trailing_bytes" / GreedyBytes,
)


def signed(value, bits):
    return value - (1 << bits) if value & (1 << (bits - 1)) else value


def source_delta(value, bits):
    # RDS reverses each 32-bit block, then BitsInteger interprets a field MSB
    # first. Retro's reader assembles the consumed field LSB first as well.
    return signed(int(f"{value:0{bits}b}"[::-1], 2), bits)


def quaternion(values, divisor, negative=False):
    xyz = [math.sin(value * math.pi / (2 * divisor)) for value in values]
    w = math.sqrt(max(0, 1 - sum(value * value for value in xyz)))
    return [-w if negative else w, *xyz]


def interpolate_rotation(left, right, fraction):
    dot = sum(a * b for a, b in zip(left, right, strict=True))
    if dot < 0:
        right, dot = [-value for value in right], -dot
    if dot > 0.9995:
        result = [a + fraction * (b - a) for a, b in zip(left, right, strict=True)]
        norm = math.sqrt(sum(value * value for value in result))
        return [value / norm for value in result]
    angle = math.acos(max(-1, min(1, dot)))
    return [(a * math.sin((1 - fraction) * angle) + b * math.sin(fraction * angle)) / math.sin(angle)
            for a, b in zip(left, right, strict=True)]


def decode_prime(animation):
    """Expand signed delta keys and sparse frame interpolation, without resampling."""
    if animation.anim_version != 2:
        raise ValueError("Expected Prime compressed format two")
    data = animation.anim
    if data.root_bone_id != 3 or data.rotation_divisor <= 0:
        raise ValueError("Unexpected source animation skeleton")
    descriptors = data.bone_channel_descriptors
    tracks = {}
    states = []
    for descriptor in descriptors:
        state = {}
        track = {}
        for kind in ("rotation", "translation"):
            if descriptor[f"{kind}_keys_count"]:
                parameters = descriptor[f"{kind}_keys"]
                values = [signed(parameters[f"initial_{axis}"], 16) for axis in "xyz"]
                state[kind] = values
                track[kind] = [quaternion(values, data.rotation_divisor) if kind == "rotation"
                               else [value * data.translation_multiplier for value in values]]
        tracks[descriptor.bone_id] = track
        states.append(state)
    present = [0]
    for frame, key in enumerate(data.animation_keys, 1):
        if key.channels is not None:
            present.append(frame)
        for index, descriptor in enumerate(descriptors):
            track, state = tracks[descriptor.bone_id], states[index]
            for kind, values in state.items():
                negative = False
                if key.channels is not None:
                    delta = key.channels[index][kind]
                    if kind == "rotation":
                        negative, delta = bool(delta.wsign), delta.data
                    parameters = descriptor[f"{kind}_keys"]
                    for axis, name in enumerate("xyz"):
                        increment = source_delta(delta[name], parameters[f"delta_{name}"])
                        values[axis] = signed((values[axis] + increment) & 0xffff, 16)
                track[kind].append(quaternion(values, data.rotation_divisor, negative) if kind == "rotation"
                                   else [value * data.translation_multiplier for value in values])
    for left, right in zip(present, present[1:]):
        for frame in range(left + 1, right):
            fraction = (frame - left) / (right - left)
            for track in tracks.values():
                for kind, keys in track.items():
                    keys[frame] = (interpolate_rotation(keys[left], keys[right], fraction) if kind == "rotation"
                                   else [a + fraction * (b - a) for a, b in zip(keys[left], keys[right], strict=True)])
    if present[-1] != len(data.animation_keys):
        raise ValueError("Source has an unaudited trailing sparse interval")
    return tracks


def convert_prime(animation):
    """Map Prime bone IDs to native Corruption IDs; retain source-space motion."""
    tracks = decode_prime(animation)
    if set(tracks) != {3, 4, 5, 6, 7, 9}:
        raise ValueError("Only the audited Ice Beam skeleton is supported")
    bones = sorted(tracks)
    frames = len(animation.anim.animation_keys) + 1
    mapping = [255] * 150
    indices = {kind: [] for kind in ("rotation", "translation")}
    keys = {kind: [] for kind in indices}
    for channel, bone in enumerate(bones):
        mapping[bone - 3] = channel
        for kind, channel_indices in indices.items():
            track = tracks[bone].get(kind)
            channel_indices.append(len(keys[kind]) // frames if track is not None else 255)
            if track is not None:
                keys[kind].extend(track)
    value = {"version": 1, "duration": {"time": animation.anim.duration, "differential_state": 0},
             "key_interval": {"time": animation.anim.interval, "differential_state": 0}, "key_count": frames,
             "root_bone_id": 0, "bone_channel_index_array": mapping,
             "rotation_channel_index_array": indices["rotation"],
             "translation_channel_index_array": indices["translation"],
             "scale_channel_index_array": [255] * len(bones), "scale_key_array": [],
             "rotation_key_array": keys["rotation"], "translation_key_array": keys["translation"],
             "auxiliary_count": 0, "auxiliary_stride": 0, "auxiliary_data": b"", "trailing_bytes": b""}
    return CORRUPTION_ANIM_ZERO.build(value)
