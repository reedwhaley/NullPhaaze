"""Corruption ANIM framing. Quantized key words are preserved, not resampled.

Format facts cross-checked against the read-only Nullphaze animation inspector
(tools/animation_formats.py) and its 47 retail catalog animation fixtures.
This module exposes header/channel framing without claiming pose evaluation.
"""

from __future__ import annotations

import math

import construct as c


def _valid_payload(value):
    payload = value.payload
    components = sum(
        (4 if flag & 1 else 0) + (3 if flag & 2 else 0) + (3 if flag & 4 else 0) for flag in payload.channel_flags
    )
    bits = (value.key_count - 1) * (1 + sum(payload.stream.widths))
    return (
        value.flag_size == len(payload.channel_flags) + 1
        and components == payload.stream.component_count
        and payload.stream.word_count in {(bits + 31) // 32, bits // 32 + 1}
        and math.isfinite(value.duration)
        and math.isfinite(value.translation_multiplier)
        and all(math.isfinite(t) for t in payload.times)
        and list(payload.times) == sorted(payload.times)
        and payload.times[0] >= 0
        and payload.times[-1] <= value.duration + 0.0001
    )


_stream = c.Struct(
    "component_count" / c.Int32ub,
    "word_count" / c.Int32ub,
    "decoded_count" / c.Int32ub,
    c.Check(lambda x: x.component_count <= 1500 and x.word_count <= 16 * 1024 * 1024),
    "widths" / c.Bytes(c.this.component_count),
    c.Check(lambda x: all(v <= 16 for v in x.widths)),
    "words" / c.Bytes(c.this.word_count * 4),
    c.Terminated,
)

Compressed = c.Struct(
    "unknown_prefix" / c.Bytes(10),
    "translation_multiplier" / c.Float32b,
    "unknown_middle" / c.Bytes(16),
    "duration" / c.Float32b,
    "key_count" / c.Int16ub,
    "blob_size" / c.Int32ub,
    "unknown_byte" / c.Int8ub,
    "time_size" / c.Int32ub,
    "flag_size" / c.Int32ub,
    "initial_size" / c.Int32ub,
    "stream_size" / c.Int32ub,
    "unknown_word" / c.Int32ub,
    "bone_count" / c.Int32ub,
    c.Check(
        lambda x: (
            0 < x.key_count
            and x.blob_size <= 64 * 1024 * 1024
            and x.time_size == x.key_count * 4
            and x.initial_size % 2 == 0
        )
    ),
    "payload"
    / c.FixedSized(
        c.this.blob_size,
        c.Struct(
            "times" / c.Array(c.this._.key_count, c.Float32b),
            "channel_flags" / c.FixedSized(c.this._.flag_size, c.PrefixedArray(c.Int8ub, c.Int8ub)),
            c.Check(lambda x: all(v & ~7 == 0 for v in x.channel_flags)),
            "initial_values" / c.Array(c.this._.initial_size // 2, c.Int16sb),
            "stream" / c.FixedSized(c.this._.stream_size, _stream),
            "footer_flags" / c.PrefixedArray(c.Int32ub, c.Int8ub),
            c.Check(lambda x: all(v in (0, 1) for v in x.footer_flags)),
            c.Terminated,
        ),
    ),
    c.Check(lambda x: x.payload.stream.component_count * 2 == x.initial_size),
    c.Check(lambda x: x.payload.stream.decoded_count == x.payload.stream.component_count * (x.key_count - 1)),
    c.Check(_valid_payload),
)

Uncompressed = c.Struct(
    "unknown_prefix" / c.Int16ub,
    "duration" / c.Struct("time" / c.Float32b, "differential_state" / c.Int32ub),
    "key_interval" / c.Struct("time" / c.Float32b, "differential_state" / c.Int32ub),
    "key_count" / c.Int32ub,
    "root_bone_id" / c.Int32ub,
    "bone_channel_index_array" / c.PrefixedArray(c.Int32ub, c.Int8ub),
    "rotation_channel_index_array" / c.PrefixedArray(c.Int32ub, c.Int8ub),
    "translation_channel_index_array" / c.PrefixedArray(c.Int32ub, c.Int8ub),
    "scale_channel_index_array" / c.PrefixedArray(c.Int32ub, c.Int8ub),
    "scale_key_array" / c.PrefixedArray(c.Int32ub, c.Array(3, c.Float32b)),
    "rotation_key_array" / c.PrefixedArray(c.Int32ub, c.Array(4, c.Float32b)),
    "translation_key_array" / c.PrefixedArray(c.Int32ub, c.Array(3, c.Float32b)),
    "auxiliary_count" / c.Int16ub,
    "auxiliary_stride" / c.Int8ub,
    "auxiliary_data" / c.Bytes(c.this.auxiliary_count * c.this.auxiliary_stride),
)

ANIM_CORRUPTION = c.Struct(
    "anim_version" / c.Int32ub,
    "anim" / c.Switch(c.this.anim_version, {0: Uncompressed, 1: Compressed}, default=c.Error),
    "trailing_bytes" / c.GreedyRange(c.Const(b"\xff")),
    c.Terminated,
)
