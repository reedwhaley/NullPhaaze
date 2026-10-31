# Strict Corruption ANIM decoding and uniform-time GC animation encoding. Boundary names
# here: Reader, Bits, Track, Animation, decode.
"""Strict Corruption ANIM decoding and uniform-time GC animation encoding.

Format facts: https://wiki.axiodl.com/w/ANIM_(Metroid_Prime_3).
Source data stays outside the repository. No source animation bytes are bundled.
"""

from __future__ import annotations

import bisect
import math
import struct
from dataclasses import dataclass

from construct import Container, ListContainer
from retro_data_structures.formats.anim import Anim
from retro_data_structures.game_check import Game


class Reader:
    def __init__(self, data):
        self.data = data
        self.offset = 0

    def take(self, count):
        if count < 0 or self.offset + count > len(self.data):
            raise ValueError("Truncated animation")
        result = self.data[self.offset : self.offset + count]
        self.offset += count
        return result

    def number(self, fmt):
        return struct.unpack(fmt, self.take(struct.calcsize(fmt)))[0]

    def floats(self, count):
        if not 0 <= count <= 2_000_000:
            raise ValueError("Excessive animation array")
        values = struct.unpack(f">{count}f", self.take(count * 4))
        if not all(math.isfinite(v) for v in values):
            raise ValueError("Non-finite animation value")
        return values

    def finish(self):
        if any(v not in (0, 255) for v in self.take(len(self.data) - self.offset)):
            raise ValueError("Unrecognized animation tail")


class Bits:
    def __init__(self, data):
        if len(data) % 4:
            raise ValueError("Animation words are not aligned")
        self.words = struct.unpack(f">{len(data) // 4}I", data)
        self.offset = 0

    def read(self, count, signed=False):
        if not 0 <= count <= 16 or self.offset + count > len(self.words) * 32:
            raise ValueError("Invalid animation bit width")
        value = 0
        for index in range(count):
            value |= ((self.words[self.offset // 32] >> (self.offset % 32)) & 1) << index
            self.offset += 1
        if signed and count and value & (1 << (count - 1)):
            value -= 1 << count
        return value


@dataclass
class Track:
    rotation: list | None
    translation: list | None
    scale: list | None


@dataclass
class Animation:
    duration: float
    times: tuple
    tracks: dict[int, Track]


def decode(data):
    reader = Reader(data)
    version = reader.number(">I")
    if version == 0:
        result = decode_array(reader)
    elif version == 1:
        result = decode_bits(reader)
    else:
        raise ValueError("Unsupported Corruption animation version")
    reader.finish()
    if not result.times or result.times[0] < 0 or list(result.times) != sorted(set(result.times)):
        raise ValueError("Invalid animation times")
    if not math.isfinite(result.duration) or result.duration < result.times[-1] - 0.0001:
        raise ValueError("Invalid animation duration")
    return result


def decode_bits(reader):
    header = reader.take(65)
    multiplier = struct.unpack_from(">f", header, 10)[0]
    duration = struct.unpack_from(">f", header, 30)[0]
    keys = struct.unpack_from(">H", header, 34)[0]
    size, time_size, flag_size, init_size, stream_size, _, bones = (
        struct.unpack_from(">I", header, offset)[0] for offset in (36, 41, 45, 49, 53, 57, 61)
    )
    if not math.isfinite(multiplier) or not 0 < keys <= 65535 or time_size != keys * 4:
        raise ValueError("Invalid keyed animation header")
    blob = Reader(reader.take(size))
    times = blob.floats(keys)
    flags = blob.take(flag_size)
    if not flags or flags[0] != len(flags) - 1 or any(v & ~7 for v in flags[1:]):
        raise ValueError("Invalid animation channel flags")
    if len(flags) - 1 > bones or bones > 150:
        raise ValueError("Invalid animation bone count")
    components = sum((4 if f & 1 else 0) + (3 if f & 2 else 0) + (3 if f & 4 else 0) for f in flags[1:])
    if init_size != components * 2 or keys * components > 2_000_000:
        raise ValueError("Invalid animation component count")
    values = list(struct.unpack(f">{components}h", blob.take(init_size)))
    stream = Reader(blob.take(stream_size))
    count, words, decoded_count = (stream.number(">I") for _ in range(3))
    if count != components or decoded_count != components * (keys - 1):
        raise ValueError("Invalid animation stream counts")
    widths = stream.take(count)
    if any(v > 16 for v in widths):
        raise ValueError("Invalid animation component width")
    bits = Bits(stream.take(words * 4))
    if stream.offset != len(stream.data):
        raise ValueError("Unexpected animation stream remainder")
    tracks = {
        i: Track([] if f & 1 else None, [] if f & 2 else None, [] if f & 4 else None)
        for i, f in enumerate(flags[1:])
        if f
    }
    for frame in range(keys):
        if frame:
            bits.read(1)
            for i, width in enumerate(widths):
                # Corruption accumulates these quantized channels in signed
                # 16-bit storage. Leaving overflow in a Python integer turns
                # multi-turn rotations into non-unit quaternions and changes
                # both their direction and angular speed after interpolation.
                values[i] = ((values[i] + bits.read(width, signed=True) + 32768) & 65535) - 32768
        offset = 0
        for track in tracks.values():
            if track.rotation is not None:
                sign, x, y, z = values[offset : offset + 4]
                x, y, z = (v / 32767 for v in (x, y, z))
                w = math.sqrt(max(0.0, 1 - x * x - y * y - z * z))
                track.rotation.append((-w if sign & 1 else w, x, y, z))
                offset += 4
            if track.translation is not None:
                track.translation.append(tuple(v * multiplier for v in values[offset : offset + 3]))
                offset += 3
            if track.scale is not None:
                track.scale.append(tuple(v / 32767 for v in values[offset : offset + 3]))
                offset += 3
    while bits.offset < len(bits.words) * 32:
        if bits.read(1):
            raise ValueError("Nonzero animation bit padding")
    footer = blob.take(blob.number(">I"))
    if any(v not in (0, 1) for v in footer) or blob.offset != len(blob.data):
        raise ValueError("Unrecognized animation footer")
    return Animation(duration, times, tracks)


def decode_array(reader):
    reader.take(2)  # Corruption's additional u16 preceding the shared GC layout.
    duration = reader.number(">f")
    reader.take(4)
    interval = reader.number(">f")
    reader.take(4)
    keys = reader.number(">I")
    reader.take(4)
    if not 0 < keys <= 65535 or not math.isfinite(interval) or interval <= 0:
        raise ValueError("Invalid array animation header")
    maps = [reader.take(reader.number(">I")) for _ in range(4)]
    tables = []
    for width in (3, 4, 3):
        values = reader.floats(reader.number(">I") * width)
        tables.append([values[i : i + width] for i in range(0, len(values), width)])
    scale, rotation, translation = tables
    tracks = {}
    for bone, channel in enumerate(maps[0]):
        if channel == 255:
            continue
        channels = []
        for index_map, table in zip(maps[1:], (rotation, translation, scale)):
            if channel >= len(index_map):
                raise ValueError("Bone channel outside index map")
            index = index_map[channel]
            if index != 255 and (index + 1) * keys > len(table):
                raise ValueError("Bone channel outside key table")
            channels.append(None if index == 255 else table[index * keys : (index + 1) * keys])
        tracks[bone] = Track(*channels)
    return Animation(duration, tuple(i * interval for i in range(keys)), tracks)


def interpolate(values, times, timestamp, quaternion=False):
    right = bisect.bisect_right(times, timestamp)
    if right == 0:
        return values[0]
    if right == len(times):
        return values[-1]
    left = right - 1
    amount = (timestamp - times[left]) / (times[right] - times[left])
    a, b = values[left], values[right]
    if quaternion:
        dot = sum(x * y for x, y in zip(a, b))
        if dot < 0:
            b = tuple(-v for v in b)
            dot = -dot
        if dot < 0.9995:
            angle = math.acos(max(-1, min(1, dot)))
            weight_a, weight_b = math.sin((1 - amount) * angle), math.sin(amount * angle)
            values = [(x * weight_a + y * weight_b) / math.sin(angle) for x, y in zip(a, b)]
        else:
            values = [x * (1 - amount) + y * amount for x, y in zip(a, b)]
        length = math.sqrt(sum(v * v for v in values))
        if length < 0.000001:
            raise ValueError("Degenerate animation quaternion")
        return tuple(v / length for v in values)
    return tuple(x * (1 - amount) + y * amount for x, y in zip(a, b))


def encode(animation, game, event_id=0xFFFFFFFF):
    """Encode an uncompressed GC clip; reject unsupported Prime scale channels."""
    if game not in (Game.PRIME, Game.ECHOES):
        raise ValueError("Expected a GameCube target")
    if game == Game.PRIME and any(t.scale is not None for t in animation.tracks.values()):
        raise ValueError("Prime ANIM does not support scale channels")
    count = max(2, math.ceil(animation.duration * 60) + 1)
    if count > 36001 or len(animation.tracks) * count > 2_000_000:
        raise ValueError("Excessive resampled animation")
    interval = animation.duration / (count - 1)
    bone_map, rotations, translations, scales = [255] * 100, [], [], []
    rotation_map, translation_map, scale_map = [], [], []
    for bone, track in sorted(animation.tracks.items()):
        target_bone = bone + (3 if game == Game.PRIME else 0)
        if target_bone >= 100:
            raise ValueError("Bone exceeds GC array layout")
        bone_map[target_bone] = len(rotation_map)
        for values, table, index_map, width in (
            (track.rotation, rotations, rotation_map, 4),
            (track.translation, translations, translation_map, 3),
            (track.scale, scales, scale_map, 3),
        ):
            if values is None:
                if game == Game.PRIME and width == 4:
                    raise ValueError("Prime requires a rotation for every animated bone")
                index_map.append(255)
            else:
                index_map.append(len(table) // count)
                table.extend(interpolate(values, animation.times, i * interval, width == 4) for i in range(count))
    body = Container(
        duration=Container(time=animation.duration, differential_state=2),
        key_interval=Container(time=interval, differential_state=2),
        key_count=count,
        root_bone_id=3 if game == Game.PRIME else 0,
        bone_channel_index_array=ListContainer(bone_map),
        rotation_channel_index_array=ListContainer(rotation_map) if game == Game.ECHOES else None,
        translation_channel_index_array=ListContainer(translation_map),
        scale_channel_index_array=ListContainer(scale_map) if game == Game.ECHOES else None,
        scale_key_array=ListContainer(scales) if game == Game.ECHOES else None,
        rotation_key_array=ListContainer(rotations),
        translation_key_array=ListContainer(translations),
        event_id=event_id if game == Game.PRIME else None,
    )
    data = Anim(Container(anim_version=0, anim=body, trailing_bytes=[]), game).build()
    checked = Anim.parse(data, game).raw.anim
    if checked.key_count != count or len(checked.rotation_key_array) != len(rotations):
        raise ValueError("Animation serialization changed key layout")
    return data


def encode_compressed(animation, game, event_id=0xFFFFFFFF):
    """Encode the retail GC reader's version-2 format, including event support."""
    sampled = Anim.parse(encode(animation, game, event_id), game).raw.anim
    count = sampled.key_count
    maximum_translation = max((abs(v) for key in sampled.translation_key_array for v in key), default=0)
    translation_multiplier = max(0.000001, maximum_translation / 32760)
    scale_multiplier = 1 / 4096
    descriptors, quantized = [], []
    bones = [(bone, channel) for bone, channel in enumerate(sampled.bone_channel_index_array) if channel != 255]
    if game == Game.PRIME:
        bones.sort(key=lambda item: (item[0] == 3, item[0]))
    for bone, channel in bones:
        channel_values = {}
        descriptor = Container(bone_id=bone)
        for kind, index_map, table in (
            ("rotation", sampled.rotation_channel_index_array, sampled.rotation_key_array),
            ("translation", sampled.translation_channel_index_array, sampled.translation_key_array),
            ("scale", sampled.scale_channel_index_array, sampled.scale_key_array),
        ):
            if kind == "rotation" and game == Game.PRIME:
                index = channel
            elif index_map is None:
                index = 255
            else:
                index = index_map[channel]
            if index == 255:
                descriptor[kind + "_keys_count"] = None if kind == "scale" and game == Game.PRIME else 0
                descriptor[kind + "_keys"] = None
                channel_values[kind] = None
                continue
            values = table[index * count : (index + 1) * count]
            if kind == "rotation":
                flip = -1 if values[0][0] < 0 else 1
                signs = [int(q[0] * flip < 0) for q in values]
                keys = [
                    tuple(round(math.asin(max(-1, min(1, v * flip))) * 32767 / (math.pi / 2)) for v in q[1:])
                    for q in values
                ]
            else:
                multiplier = translation_multiplier if kind == "translation" else scale_multiplier
                keys = [tuple(round(v / multiplier) for v in key) for key in values]
                signs = None
            widths = []
            for axis in range(3):
                differences = [((b[axis] - a[axis] + 32768) % 65536) - 32768 for a, b in zip(keys, keys[1:])]
                width = next(w for w in range(1, 17) if all(-(1 << (w - 1)) <= v < (1 << (w - 1)) for v in differences))
                widths.append(width)
            descriptor[kind + "_keys_count"] = count - 1
            descriptor[kind + "_keys"] = Container(
                initial_x=keys[0][0] & 65535,
                delta_x=widths[0],
                initial_y=keys[0][1] & 65535,
                delta_y=widths[1],
                initial_z=keys[0][2] & 65535,
                delta_z=widths[2],
            )
            channel_values[kind] = (keys, widths, signs)
        descriptors.append(descriptor)
        quantized.append(channel_values)
    frames = ListContainer()
    for frame in range(1, count):
        channels = ListContainer()
        for channel in quantized:
            result = Container()
            for kind, data in channel.items():
                if data is None:
                    result[kind] = None
                else:
                    keys, widths, signs = data
                    delta = Container(
                        {
                            axis: reverse_field_bits(keys[frame][i] - keys[frame - 1][i], widths[i])
                            for i, axis in enumerate(("x", "y", "z"))
                        }
                    )
                    result[kind] = Container(wsign=signs[frame], data=delta) if signs is not None else delta
            channels.append(result)
        frames.append(Container(channels=channels))
    body = Container(
        scratch_size=0,
        event_id=event_id if game == Game.PRIME else None,
        unk_1=1 if game == Game.PRIME else None,
        unk_2=0x0101 if game == Game.ECHOES else None,
        duration=animation.duration,
        interval=sampled.key_interval.time,
        root_bone_id=3 if game == Game.PRIME else 0,
        looping_flag=0,
        rotation_divisor=32767,
        translation_multiplier=translation_multiplier,
        scale_multiplier=scale_multiplier if game == Game.ECHOES else None,
        unk_3=1,
        _key_bitmap_array=ListContainer([True] * count),
        bone_channel_descriptors=ListContainer(descriptors),
        animation_keys=frames,
    )
    encoded = Anim(Container(anim_version=2, anim=body, trailing_bytes=[]), game).build()
    checked = Anim.parse(encoded, game).raw.anim
    if len(checked.animation_keys) != count - 1:
        raise ValueError("Compressed animation key count changed")
    return encoded


def reverse_field_bits(value, width):
    """Bridge RDS's MSB-first integer fields to the retail LSB-first reader.

    Reversing each 32-bit block alone reverses the order of the fields, but
    BitsInteger still writes the most significant bit of each delta first.
    Retail CBitLevelLoader reads the least significant bit of the delta first.
    """
    value &= (1 << width) - 1
    result = 0
    for _ in range(width):
        result = (result << 1) | (value & 1)
        value >>= 1
    return result
