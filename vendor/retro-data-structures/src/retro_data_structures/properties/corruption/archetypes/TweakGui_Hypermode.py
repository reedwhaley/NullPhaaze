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
import retro_data_structures.enums.corruption as enums
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.corruption.archetypes.TweakGui_UnknownStruct5 import TweakGui_UnknownStruct5
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    class TweakGui_HypermodeJson(typing_extensions.TypedDict):
        invulnerable_color: json_util.JsonValue
        corrupted_color: json_util.JsonValue
        danger_color: json_util.JsonValue
        flash_color: json_util.JsonValue
        hypermode_transition_distortion: json_util.JsonObject
        hypermode_deco_fade_in_control: json_util.JsonObject
        hypermode_deco_fade_out_control: json_util.JsonObject
        hypermode_deco_chunk_out_control: json_util.JsonObject
        distortion_scalar: float
        unknown_0x4cc80933: int
        unknown_0x8d05ebe2: int
        distortion_brightness_increase: json_util.JsonValue
        unknown_0x59412843: float
        unknown_0xf07d9bac: float
        unknown_0x60bb24c7: json_util.JsonObject
        unknown_0x165e1dfa: json_util.JsonObject
        unknown_0x8d2df72e: json_util.JsonObject
    

@dataclasses.dataclass()
class TweakGui_Hypermode(BaseProperty):
    invulnerable_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=1.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf295d923, original_name='InvulnerableColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    corrupted_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.75, g=0.0, b=1.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xece48021, original_name='CorruptedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    danger_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.25, b=0.25, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x1b05214d, original_name='DangerColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    flash_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x27112d25, original_name='FlashColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    hypermode_transition_distortion: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xbc85e959, original_name='HypermodeTransitionDistortion', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    hypermode_deco_fade_in_control: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xfbd0fa9b, original_name='HypermodeDecoFadeInControl', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    hypermode_deco_fade_out_control: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x1eb39a1a, original_name='HypermodeDecoFadeOutControl', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    hypermode_deco_chunk_out_control: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xe0fd8966, original_name='HypermodeDecoChunkOutControl', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    distortion_scalar: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4e95e12a, original_name='DistortionScalar'
        ),
    })
    unknown_0x4cc80933: enums.TweakGui_UnknownEnum1Enum = dataclasses.field(default=enums.TweakGui_UnknownEnum1Enum.Unknown1, metadata={
        'reflection': FieldReflection[enums.TweakGui_UnknownEnum1Enum](
            enums.TweakGui_UnknownEnum1Enum, id=0x4cc80933, original_name='Unknown', from_json=enums.TweakGui_UnknownEnum1Enum.from_json, to_json=enums.TweakGui_UnknownEnum1Enum.to_json
        ),
    })
    unknown_0x8d05ebe2: enums.TweakGui_UnknownEnum1Enum = dataclasses.field(default=enums.TweakGui_UnknownEnum1Enum.Unknown2, metadata={
        'reflection': FieldReflection[enums.TweakGui_UnknownEnum1Enum](
            enums.TweakGui_UnknownEnum1Enum, id=0x8d05ebe2, original_name='Unknown', from_json=enums.TweakGui_UnknownEnum1Enum.from_json, to_json=enums.TweakGui_UnknownEnum1Enum.to_json
        ),
    })
    distortion_brightness_increase: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x2f2b9d19, original_name='DistortionBrightnessIncrease', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    unknown_0x59412843: float = dataclasses.field(default=12.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x59412843, original_name='Unknown'
        ),
    })
    unknown_0xf07d9bac: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf07d9bac, original_name='Unknown'
        ),
    })
    unknown_0x60bb24c7: TweakGui_UnknownStruct5 = dataclasses.field(default_factory=TweakGui_UnknownStruct5, metadata={
        'reflection': FieldReflection[TweakGui_UnknownStruct5](
            TweakGui_UnknownStruct5, id=0x60bb24c7, original_name='Unknown', from_json=TweakGui_UnknownStruct5.from_json, to_json=TweakGui_UnknownStruct5.to_json
        ),
    })
    unknown_0x165e1dfa: TweakGui_UnknownStruct5 = dataclasses.field(default_factory=TweakGui_UnknownStruct5, metadata={
        'reflection': FieldReflection[TweakGui_UnknownStruct5](
            TweakGui_UnknownStruct5, id=0x165e1dfa, original_name='Unknown', from_json=TweakGui_UnknownStruct5.from_json, to_json=TweakGui_UnknownStruct5.to_json
        ),
    })
    unknown_0x8d2df72e: TweakGui_UnknownStruct5 = dataclasses.field(default_factory=TweakGui_UnknownStruct5, metadata={
        'reflection': FieldReflection[TweakGui_UnknownStruct5](
            TweakGui_UnknownStruct5, id=0x8d2df72e, original_name='Unknown', from_json=TweakGui_UnknownStruct5.from_json, to_json=TweakGui_UnknownStruct5.to_json
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
        if property_count != 17:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf295d923
        invulnerable_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xece48021
        corrupted_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1b05214d
        danger_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x27112d25
        flash_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbc85e959
        hypermode_transition_distortion = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfbd0fa9b
        hypermode_deco_fade_in_control = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1eb39a1a
        hypermode_deco_fade_out_control = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe0fd8966
        hypermode_deco_chunk_out_control = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4e95e12a
        distortion_scalar = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4cc80933
        unknown_0x4cc80933 = enums.TweakGui_UnknownEnum1Enum.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8d05ebe2
        unknown_0x8d05ebe2 = enums.TweakGui_UnknownEnum1Enum.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2f2b9d19
        distortion_brightness_increase = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x59412843
        unknown_0x59412843 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf07d9bac
        unknown_0xf07d9bac = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x60bb24c7
        unknown_0x60bb24c7 = TweakGui_UnknownStruct5.from_stream(data, game, property_size, default_override={'position_percent': 33.33330154418945, 'texcoord_percent': 16.66659927368164, 'alpha_percent': 100.0, 'color_percent': 90.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x165e1dfa
        unknown_0x165e1dfa = TweakGui_UnknownStruct5.from_stream(data, game, property_size, default_override={'position_percent': 66.6666030883789, 'texcoord_percent': 20.0, 'alpha_percent': 100.0, 'color_percent': 70.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8d2df72e
        unknown_0x8d2df72e = TweakGui_UnknownStruct5.from_stream(data, game, property_size, default_override={'position_percent': 100.0, 'texcoord_percent': 25.0, 'alpha_percent': 100.0})
    
        return cls(invulnerable_color, corrupted_color, danger_color, flash_color, hypermode_transition_distortion, hypermode_deco_fade_in_control, hypermode_deco_fade_out_control, hypermode_deco_chunk_out_control, distortion_scalar, unknown_0x4cc80933, unknown_0x8d05ebe2, distortion_brightness_increase, unknown_0x59412843, unknown_0xf07d9bac, unknown_0x60bb24c7, unknown_0x165e1dfa, unknown_0x8d2df72e)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x11')  # 17 properties

        data.write(b'\xf2\x95\xd9#')  # 0xf295d923
        data.write(b'\x00\x10')  # size
        self.invulnerable_color.to_stream(data, game)

        data.write(b'\xec\xe4\x80!')  # 0xece48021
        data.write(b'\x00\x10')  # size
        self.corrupted_color.to_stream(data, game)

        data.write(b'\x1b\x05!M')  # 0x1b05214d
        data.write(b'\x00\x10')  # size
        self.danger_color.to_stream(data, game)

        data.write(b"'\x11-%")  # 0x27112d25
        data.write(b'\x00\x10')  # size
        self.flash_color.to_stream(data, game)

        data.write(b'\xbc\x85\xe9Y')  # 0xbc85e959
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hypermode_transition_distortion.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfb\xd0\xfa\x9b')  # 0xfbd0fa9b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hypermode_deco_fade_in_control.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x1e\xb3\x9a\x1a')  # 0x1eb39a1a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hypermode_deco_fade_out_control.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe0\xfd\x89f')  # 0xe0fd8966
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hypermode_deco_chunk_out_control.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'N\x95\xe1*')  # 0x4e95e12a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.distortion_scalar))

        data.write(b'L\xc8\t3')  # 0x4cc80933
        data.write(b'\x00\x04')  # size
        self.unknown_0x4cc80933.to_stream(data, game)

        data.write(b'\x8d\x05\xeb\xe2')  # 0x8d05ebe2
        data.write(b'\x00\x04')  # size
        self.unknown_0x8d05ebe2.to_stream(data, game)

        data.write(b'/+\x9d\x19')  # 0x2f2b9d19
        data.write(b'\x00\x10')  # size
        self.distortion_brightness_increase.to_stream(data, game)

        data.write(b'YA(C')  # 0x59412843
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x59412843))

        data.write(b'\xf0}\x9b\xac')  # 0xf07d9bac
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf07d9bac))

        data.write(b'`\xbb$\xc7')  # 0x60bb24c7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.unknown_0x60bb24c7.to_stream(data, game, default_override={'position_percent': 33.33330154418945, 'texcoord_percent': 16.66659927368164, 'alpha_percent': 100.0, 'color_percent': 90.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x16^\x1d\xfa')  # 0x165e1dfa
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.unknown_0x165e1dfa.to_stream(data, game, default_override={'position_percent': 66.6666030883789, 'texcoord_percent': 20.0, 'alpha_percent': 100.0, 'color_percent': 70.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8d-\xf7.')  # 0x8d2df72e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.unknown_0x8d2df72e.to_stream(data, game, default_override={'position_percent': 100.0, 'texcoord_percent': 25.0, 'alpha_percent': 100.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGui_HypermodeJson", data)
        return cls(
            invulnerable_color=Color.from_json(json_data['invulnerable_color']),
            corrupted_color=Color.from_json(json_data['corrupted_color']),
            danger_color=Color.from_json(json_data['danger_color']),
            flash_color=Color.from_json(json_data['flash_color']),
            hypermode_transition_distortion=Spline.from_json(json_data['hypermode_transition_distortion']),
            hypermode_deco_fade_in_control=Spline.from_json(json_data['hypermode_deco_fade_in_control']),
            hypermode_deco_fade_out_control=Spline.from_json(json_data['hypermode_deco_fade_out_control']),
            hypermode_deco_chunk_out_control=Spline.from_json(json_data['hypermode_deco_chunk_out_control']),
            distortion_scalar=json_data['distortion_scalar'],
            unknown_0x4cc80933=enums.TweakGui_UnknownEnum1Enum.from_json(json_data['unknown_0x4cc80933']),
            unknown_0x8d05ebe2=enums.TweakGui_UnknownEnum1Enum.from_json(json_data['unknown_0x8d05ebe2']),
            distortion_brightness_increase=Color.from_json(json_data['distortion_brightness_increase']),
            unknown_0x59412843=json_data['unknown_0x59412843'],
            unknown_0xf07d9bac=json_data['unknown_0xf07d9bac'],
            unknown_0x60bb24c7=TweakGui_UnknownStruct5.from_json(json_data['unknown_0x60bb24c7']),
            unknown_0x165e1dfa=TweakGui_UnknownStruct5.from_json(json_data['unknown_0x165e1dfa']),
            unknown_0x8d2df72e=TweakGui_UnknownStruct5.from_json(json_data['unknown_0x8d2df72e']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'invulnerable_color': self.invulnerable_color.to_json(),
            'corrupted_color': self.corrupted_color.to_json(),
            'danger_color': self.danger_color.to_json(),
            'flash_color': self.flash_color.to_json(),
            'hypermode_transition_distortion': self.hypermode_transition_distortion.to_json(),
            'hypermode_deco_fade_in_control': self.hypermode_deco_fade_in_control.to_json(),
            'hypermode_deco_fade_out_control': self.hypermode_deco_fade_out_control.to_json(),
            'hypermode_deco_chunk_out_control': self.hypermode_deco_chunk_out_control.to_json(),
            'distortion_scalar': self.distortion_scalar,
            'unknown_0x4cc80933': self.unknown_0x4cc80933.to_json(),
            'unknown_0x8d05ebe2': self.unknown_0x8d05ebe2.to_json(),
            'distortion_brightness_increase': self.distortion_brightness_increase.to_json(),
            'unknown_0x59412843': self.unknown_0x59412843,
            'unknown_0xf07d9bac': self.unknown_0xf07d9bac,
            'unknown_0x60bb24c7': self.unknown_0x60bb24c7.to_json(),
            'unknown_0x165e1dfa': self.unknown_0x165e1dfa.to_json(),
            'unknown_0x8d2df72e': self.unknown_0x8d2df72e.to_json(),
        }


def _decode_invulnerable_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_corrupted_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_danger_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_flash_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_hypermode_transition_distortion(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_hypermode_deco_fade_in_control(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_hypermode_deco_fade_out_control(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_hypermode_deco_chunk_out_control(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_unknown_0x4cc80933(data: typing.BinaryIO, game: Game, property_size: int) -> enums.TweakGui_UnknownEnum1Enum:
    return enums.TweakGui_UnknownEnum1Enum.from_stream(data, game)


def _decode_unknown_0x8d05ebe2(data: typing.BinaryIO, game: Game, property_size: int) -> enums.TweakGui_UnknownEnum1Enum:
    return enums.TweakGui_UnknownEnum1Enum.from_stream(data, game)


def _decode_distortion_brightness_increase(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x60bb24c7(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_UnknownStruct5:
    return TweakGui_UnknownStruct5.from_stream(data, game, property_size, default_override={'position_percent': 33.33330154418945, 'texcoord_percent': 16.66659927368164, 'alpha_percent': 100.0, 'color_percent': 90.0})


def _decode_unknown_0x165e1dfa(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_UnknownStruct5:
    return TweakGui_UnknownStruct5.from_stream(data, game, property_size, default_override={'position_percent': 66.6666030883789, 'texcoord_percent': 20.0, 'alpha_percent': 100.0, 'color_percent': 70.0})


def _decode_unknown_0x8d2df72e(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_UnknownStruct5:
    return TweakGui_UnknownStruct5.from_stream(data, game, property_size, default_override={'position_percent': 100.0, 'texcoord_percent': 25.0, 'alpha_percent': 100.0})


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xf295d923: ('invulnerable_color', _decode_invulnerable_color),
    0xece48021: ('corrupted_color', _decode_corrupted_color),
    0x1b05214d: ('danger_color', _decode_danger_color),
    0x27112d25: ('flash_color', _decode_flash_color),
    0xbc85e959: ('hypermode_transition_distortion', _decode_hypermode_transition_distortion),
    0xfbd0fa9b: ('hypermode_deco_fade_in_control', _decode_hypermode_deco_fade_in_control),
    0x1eb39a1a: ('hypermode_deco_fade_out_control', _decode_hypermode_deco_fade_out_control),
    0xe0fd8966: ('hypermode_deco_chunk_out_control', _decode_hypermode_deco_chunk_out_control),
    0x4e95e12a: ('distortion_scalar', structs.decode_BIG_f),
    0x4cc80933: ('unknown_0x4cc80933', _decode_unknown_0x4cc80933),
    0x8d05ebe2: ('unknown_0x8d05ebe2', _decode_unknown_0x8d05ebe2),
    0x2f2b9d19: ('distortion_brightness_increase', _decode_distortion_brightness_increase),
    0x59412843: ('unknown_0x59412843', structs.decode_BIG_f),
    0xf07d9bac: ('unknown_0xf07d9bac', structs.decode_BIG_f),
    0x60bb24c7: ('unknown_0x60bb24c7', _decode_unknown_0x60bb24c7),
    0x165e1dfa: ('unknown_0x165e1dfa', _decode_unknown_0x165e1dfa),
    0x8d2df72e: ('unknown_0x8d2df72e', _decode_unknown_0x8d2df72e),
}
