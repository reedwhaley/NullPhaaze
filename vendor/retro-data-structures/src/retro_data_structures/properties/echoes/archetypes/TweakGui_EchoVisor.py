# Generated File
from __future__ import annotations

import dataclasses
import struct
import typing
import typing_extensions

from retro_data_structures import json_util
from retro_data_structures.game_check import Game
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.color import Color

if typing.TYPE_CHECKING:
    class TweakGui_EchoVisorJson(typing_extensions.TypedDict):
        echo_base_color: json_util.JsonValue
        echo_outline_color: json_util.JsonValue
        echo_damage_color: json_util.JsonValue
        echo_yellow_damage_color: json_util.JsonValue
        echo_fog_mode: int
        echo_fog_near_z: float
        echo_fog_far_z: float
        echo_big_ring_scale: float
        unknown: float
        echo_big_ring_scan_time: float
        echo_big_ring_fade_start: float
        echo_ring_color: json_util.JsonValue
        echo_aura_small_size: float
        echo_aura_big_size: float
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x905fa7e4, 0x62ca2ddd, 0xdc4c2a5f, 0xa288fe51, 0xf316c617, 0xb56d2286, 0xc5c2d8fc, 0x47d948b1, 0x5708b903, 0xafc8c571, 0x28bffdc5, 0x66351d36, 0x99a65ca7, 0x51f19dea)


@dataclasses.dataclass()
class TweakGui_EchoVisor(BaseProperty):
    echo_base_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x905fa7e4, original_name='EchoBaseColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    echo_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.6352940201759338, g=0.7882350087165833, b=0.9411759972572327, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x62ca2ddd, original_name='EchoOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    echo_damage_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xdc4c2a5f, original_name='EchoDamageColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    echo_yellow_damage_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xa288fe51, original_name='EchoYellowDamageColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    echo_fog_mode: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0xf316c617, original_name='EchoFogMode'
        ),
    })  # Choice
    echo_fog_near_z: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb56d2286, original_name='EchoFogNearZ'
        ),
    })
    echo_fog_far_z: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc5c2d8fc, original_name='EchoFogFarZ'
        ),
    })
    echo_big_ring_scale: float = dataclasses.field(default=800.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x47d948b1, original_name='EchoBigRingScale'
        ),
    })
    unknown: float = dataclasses.field(default=500.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5708b903, original_name='Unknown'
        ),
    })
    echo_big_ring_scan_time: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xafc8c571, original_name='EchoBigRingScanTime'
        ),
    })
    echo_big_ring_fade_start: float = dataclasses.field(default=0.8999999761581421, metadata={
        'reflection': FieldReflection[float](
            float, id=0x28bffdc5, original_name='EchoBigRingFadeStart'
        ),
    })
    echo_ring_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.6352940201759338, g=0.7882350087165833, b=0.9411759972572327, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x66351d36, original_name='EchoRingColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    echo_aura_small_size: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x99a65ca7, original_name='EchoAuraSmallSize'
        ),
    })
    echo_aura_big_size: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x51f19dea, original_name='EchoAuraBigSize'
        ),
    })

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None) -> typing_extensions.Self:
        property_count = structs.BIG_H.unpack(data.read(2))[0]
        if (result := cls._fast_decode(data, game, property_count)) is not None:
            return result

        present_fields = default_override or {}
        for _ in range(property_count):
            property_id, property_size = structs.BIG_LH.unpack(data.read(6))
            start = data.tell()
            try:
                property_name, decoder = _property_decoder[property_id]
                present_fields[property_name] = decoder(data, game, property_size)
            except KeyError:
                raise RuntimeError(f"Unknown property: 0x{property_id:08x}")
            assert data.tell() - start == property_size

        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 14:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHffffLHffffLHffffLHffffLHLLHfLHfLHfLHfLHfLHfLHffffLHfLHf')
    
        dec = _FAST_FORMAT.unpack(data.read(200))
        assert (dec[0], dec[6], dec[12], dec[18], dec[24], dec[27], dec[30], dec[33], dec[36], dec[39], dec[42], dec[45], dec[51], dec[54]) == _FAST_IDS
        return cls(
            Color(*dec[2:6]),
            Color(*dec[8:12]),
            Color(*dec[14:18]),
            Color(*dec[20:24]),
            dec[26],
            dec[29],
            dec[32],
            dec[35],
            dec[38],
            dec[41],
            dec[44],
            Color(*dec[47:51]),
            dec[53],
            dec[56],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x0e')  # 14 properties

        data.write(b'\x90_\xa7\xe4')  # 0x905fa7e4
        data.write(b'\x00\x10')  # size
        self.echo_base_color.to_stream(data, game)

        data.write(b'b\xca-\xdd')  # 0x62ca2ddd
        data.write(b'\x00\x10')  # size
        self.echo_outline_color.to_stream(data, game)

        data.write(b'\xdcL*_')  # 0xdc4c2a5f
        data.write(b'\x00\x10')  # size
        self.echo_damage_color.to_stream(data, game)

        data.write(b'\xa2\x88\xfeQ')  # 0xa288fe51
        data.write(b'\x00\x10')  # size
        self.echo_yellow_damage_color.to_stream(data, game)

        data.write(b'\xf3\x16\xc6\x17')  # 0xf316c617
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.echo_fog_mode))

        data.write(b'\xb5m"\x86')  # 0xb56d2286
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.echo_fog_near_z))

        data.write(b'\xc5\xc2\xd8\xfc')  # 0xc5c2d8fc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.echo_fog_far_z))

        data.write(b'G\xd9H\xb1')  # 0x47d948b1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.echo_big_ring_scale))

        data.write(b'W\x08\xb9\x03')  # 0x5708b903
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b'\xaf\xc8\xc5q')  # 0xafc8c571
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.echo_big_ring_scan_time))

        data.write(b'(\xbf\xfd\xc5')  # 0x28bffdc5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.echo_big_ring_fade_start))

        data.write(b'f5\x1d6')  # 0x66351d36
        data.write(b'\x00\x10')  # size
        self.echo_ring_color.to_stream(data, game)

        data.write(b'\x99\xa6\\\xa7')  # 0x99a65ca7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.echo_aura_small_size))

        data.write(b'Q\xf1\x9d\xea')  # 0x51f19dea
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.echo_aura_big_size))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGui_EchoVisorJson", data)
        return cls(
            echo_base_color=Color.from_json(json_data['echo_base_color']),
            echo_outline_color=Color.from_json(json_data['echo_outline_color']),
            echo_damage_color=Color.from_json(json_data['echo_damage_color']),
            echo_yellow_damage_color=Color.from_json(json_data['echo_yellow_damage_color']),
            echo_fog_mode=json_data['echo_fog_mode'],
            echo_fog_near_z=json_data['echo_fog_near_z'],
            echo_fog_far_z=json_data['echo_fog_far_z'],
            echo_big_ring_scale=json_data['echo_big_ring_scale'],
            unknown=json_data['unknown'],
            echo_big_ring_scan_time=json_data['echo_big_ring_scan_time'],
            echo_big_ring_fade_start=json_data['echo_big_ring_fade_start'],
            echo_ring_color=Color.from_json(json_data['echo_ring_color']),
            echo_aura_small_size=json_data['echo_aura_small_size'],
            echo_aura_big_size=json_data['echo_aura_big_size'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'echo_base_color': self.echo_base_color.to_json(),
            'echo_outline_color': self.echo_outline_color.to_json(),
            'echo_damage_color': self.echo_damage_color.to_json(),
            'echo_yellow_damage_color': self.echo_yellow_damage_color.to_json(),
            'echo_fog_mode': self.echo_fog_mode,
            'echo_fog_near_z': self.echo_fog_near_z,
            'echo_fog_far_z': self.echo_fog_far_z,
            'echo_big_ring_scale': self.echo_big_ring_scale,
            'unknown': self.unknown,
            'echo_big_ring_scan_time': self.echo_big_ring_scan_time,
            'echo_big_ring_fade_start': self.echo_big_ring_fade_start,
            'echo_ring_color': self.echo_ring_color.to_json(),
            'echo_aura_small_size': self.echo_aura_small_size,
            'echo_aura_big_size': self.echo_aura_big_size,
        }


def _decode_echo_base_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_echo_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_echo_damage_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_echo_yellow_damage_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_echo_ring_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x905fa7e4: ('echo_base_color', _decode_echo_base_color),
    0x62ca2ddd: ('echo_outline_color', _decode_echo_outline_color),
    0xdc4c2a5f: ('echo_damage_color', _decode_echo_damage_color),
    0xa288fe51: ('echo_yellow_damage_color', _decode_echo_yellow_damage_color),
    0xf316c617: ('echo_fog_mode', structs.decode_BIG_L),
    0xb56d2286: ('echo_fog_near_z', structs.decode_BIG_f),
    0xc5c2d8fc: ('echo_fog_far_z', structs.decode_BIG_f),
    0x47d948b1: ('echo_big_ring_scale', structs.decode_BIG_f),
    0x5708b903: ('unknown', structs.decode_BIG_f),
    0xafc8c571: ('echo_big_ring_scan_time', structs.decode_BIG_f),
    0x28bffdc5: ('echo_big_ring_fade_start', structs.decode_BIG_f),
    0x66351d36: ('echo_ring_color', _decode_echo_ring_color),
    0x99a65ca7: ('echo_aura_small_size', structs.decode_BIG_f),
    0x51f19dea: ('echo_aura_big_size', structs.decode_BIG_f),
}
