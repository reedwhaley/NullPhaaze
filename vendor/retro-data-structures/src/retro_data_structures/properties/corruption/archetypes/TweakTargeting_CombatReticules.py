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
from retro_data_structures.properties.spline import Spline
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    class TweakTargeting_CombatReticulesJson(typing_extensions.TypedDict):
        reticule_scale: float
        reticule_color: json_util.JsonValue
        reticule_hostile_color: json_util.JsonValue
        reticule_x_ray_color: json_util.JsonValue
        unknown_0x175644c7: json_util.JsonValue
        unknown_0xf31d0434: json_util.JsonObject
        unknown_0x5d0f883c: json_util.JsonObject
        hostile_adjustment_time: float
        csi_scale: float
        csi_color: json_util.JsonValue
        csi_active_alpha: float
        csi_transition_time: float
        off_screen_indicator_alpha: float
    

@dataclasses.dataclass()
class TweakTargeting_CombatReticules(BaseProperty):
    reticule_scale: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdad62eb0, original_name='ReticuleScale'
        ),
    })
    reticule_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xc140585b, original_name='ReticuleColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    reticule_hostile_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x8de5d7b2, original_name='ReticuleHostileColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    reticule_x_ray_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xd2f678eb, original_name='ReticuleXRayColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    unknown_0x175644c7: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x175644c7, original_name='Unknown', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    unknown_0xf31d0434: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xf31d0434, original_name='Unknown', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    unknown_0x5d0f883c: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x5d0f883c, original_name='Unknown', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    hostile_adjustment_time: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0x42a67658, original_name='HostileAdjustmentTime'
        ),
    })
    csi_scale: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2608da71, original_name='CSIScale'
        ),
    })
    csi_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x3d9eac9a, original_name='CSIColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    csi_active_alpha: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd9fc0e1e, original_name='CSIActiveAlpha'
        ),
    })
    csi_transition_time: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x907af54a, original_name='CSITransitionTime'
        ),
    })
    off_screen_indicator_alpha: float = dataclasses.field(default=0.6000000238418579, metadata={
        'reflection': FieldReflection[float](
            float, id=0xff156449, original_name='OffScreenIndicatorAlpha'
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
        if property_count != 13:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdad62eb0
        reticule_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc140585b
        reticule_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8de5d7b2
        reticule_hostile_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd2f678eb
        reticule_x_ray_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x175644c7
        unknown_0x175644c7 = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf31d0434
        unknown_0xf31d0434 = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5d0f883c
        unknown_0x5d0f883c = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42a67658
        hostile_adjustment_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2608da71
        csi_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3d9eac9a
        csi_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd9fc0e1e
        csi_active_alpha = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x907af54a
        csi_transition_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xff156449
        off_screen_indicator_alpha = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(reticule_scale, reticule_color, reticule_hostile_color, reticule_x_ray_color, unknown_0x175644c7, unknown_0xf31d0434, unknown_0x5d0f883c, hostile_adjustment_time, csi_scale, csi_color, csi_active_alpha, csi_transition_time, off_screen_indicator_alpha)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\r')  # 13 properties

        data.write(b'\xda\xd6.\xb0')  # 0xdad62eb0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.reticule_scale))

        data.write(b'\xc1@X[')  # 0xc140585b
        data.write(b'\x00\x10')  # size
        self.reticule_color.to_stream(data, game)

        data.write(b'\x8d\xe5\xd7\xb2')  # 0x8de5d7b2
        data.write(b'\x00\x10')  # size
        self.reticule_hostile_color.to_stream(data, game)

        data.write(b'\xd2\xf6x\xeb')  # 0xd2f678eb
        data.write(b'\x00\x10')  # size
        self.reticule_x_ray_color.to_stream(data, game)

        data.write(b'\x17VD\xc7')  # 0x175644c7
        data.write(b'\x00\x0c')  # size
        self.unknown_0x175644c7.to_stream(data, game)

        data.write(b'\xf3\x1d\x044')  # 0xf31d0434
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.unknown_0xf31d0434.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b']\x0f\x88<')  # 0x5d0f883c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.unknown_0x5d0f883c.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'B\xa6vX')  # 0x42a67658
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hostile_adjustment_time))

        data.write(b'&\x08\xdaq')  # 0x2608da71
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.csi_scale))

        data.write(b'=\x9e\xac\x9a')  # 0x3d9eac9a
        data.write(b'\x00\x10')  # size
        self.csi_color.to_stream(data, game)

        data.write(b'\xd9\xfc\x0e\x1e')  # 0xd9fc0e1e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.csi_active_alpha))

        data.write(b'\x90z\xf5J')  # 0x907af54a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.csi_transition_time))

        data.write(b'\xff\x15dI')  # 0xff156449
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.off_screen_indicator_alpha))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakTargeting_CombatReticulesJson", data)
        return cls(
            reticule_scale=json_data['reticule_scale'],
            reticule_color=Color.from_json(json_data['reticule_color']),
            reticule_hostile_color=Color.from_json(json_data['reticule_hostile_color']),
            reticule_x_ray_color=Color.from_json(json_data['reticule_x_ray_color']),
            unknown_0x175644c7=Vector.from_json(json_data['unknown_0x175644c7']),
            unknown_0xf31d0434=Spline.from_json(json_data['unknown_0xf31d0434']),
            unknown_0x5d0f883c=Spline.from_json(json_data['unknown_0x5d0f883c']),
            hostile_adjustment_time=json_data['hostile_adjustment_time'],
            csi_scale=json_data['csi_scale'],
            csi_color=Color.from_json(json_data['csi_color']),
            csi_active_alpha=json_data['csi_active_alpha'],
            csi_transition_time=json_data['csi_transition_time'],
            off_screen_indicator_alpha=json_data['off_screen_indicator_alpha'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'reticule_scale': self.reticule_scale,
            'reticule_color': self.reticule_color.to_json(),
            'reticule_hostile_color': self.reticule_hostile_color.to_json(),
            'reticule_x_ray_color': self.reticule_x_ray_color.to_json(),
            'unknown_0x175644c7': self.unknown_0x175644c7.to_json(),
            'unknown_0xf31d0434': self.unknown_0xf31d0434.to_json(),
            'unknown_0x5d0f883c': self.unknown_0x5d0f883c.to_json(),
            'hostile_adjustment_time': self.hostile_adjustment_time,
            'csi_scale': self.csi_scale,
            'csi_color': self.csi_color.to_json(),
            'csi_active_alpha': self.csi_active_alpha,
            'csi_transition_time': self.csi_transition_time,
            'off_screen_indicator_alpha': self.off_screen_indicator_alpha,
        }


def _decode_reticule_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_reticule_hostile_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_reticule_x_ray_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x175644c7(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_unknown_0xf31d0434(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_unknown_0x5d0f883c(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_csi_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xdad62eb0: ('reticule_scale', structs.decode_BIG_f),
    0xc140585b: ('reticule_color', _decode_reticule_color),
    0x8de5d7b2: ('reticule_hostile_color', _decode_reticule_hostile_color),
    0xd2f678eb: ('reticule_x_ray_color', _decode_reticule_x_ray_color),
    0x175644c7: ('unknown_0x175644c7', _decode_unknown_0x175644c7),
    0xf31d0434: ('unknown_0xf31d0434', _decode_unknown_0xf31d0434),
    0x5d0f883c: ('unknown_0x5d0f883c', _decode_unknown_0x5d0f883c),
    0x42a67658: ('hostile_adjustment_time', structs.decode_BIG_f),
    0x2608da71: ('csi_scale', structs.decode_BIG_f),
    0x3d9eac9a: ('csi_color', _decode_csi_color),
    0xd9fc0e1e: ('csi_active_alpha', structs.decode_BIG_f),
    0x907af54a: ('csi_transition_time', structs.decode_BIG_f),
    0xff156449: ('off_screen_indicator_alpha', structs.decode_BIG_f),
}
