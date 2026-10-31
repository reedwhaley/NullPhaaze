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
    class TweakGui_HudColorTypedefJson(typing_extensions.TypedDict):
        energy_bar_filled_color: json_util.JsonValue
        energy_bar_empty_color: json_util.JsonValue
        energy_bar_shadow_color: json_util.JsonValue
        energy_tanks_filled_color: json_util.JsonValue
        energy_tanks_empty_color: json_util.JsonValue
        energy_digits_foreground_color: json_util.JsonValue
        energy_digits_outline_color: json_util.JsonValue
        primary_energy_bar_filled_color: json_util.JsonValue
        primary_energy_bar_shadow_color: json_util.JsonValue
        primary_energy_tank_filled_color: json_util.JsonValue
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xacf62d93, 0x37e381c2, 0xb9a9fc6e, 0x4377e677, 0x63384f81, 0x1fd3d43a, 0xe1ff2a4f, 0x9cfb8a36, 0x89a45bcb, 0xc2a8ccc6)


@dataclasses.dataclass()
class TweakGui_HudColorTypedef(BaseProperty):
    energy_bar_filled_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xacf62d93, original_name='EnergyBarFilledColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    energy_bar_empty_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.17254899442195892, g=0.2901960015296936, b=0.37254899740219116, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x37e381c2, original_name='EnergyBarEmptyColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    energy_bar_shadow_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xb9a9fc6e, original_name='EnergyBarShadowColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    energy_tanks_filled_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x4377e677, original_name='EnergyTanksFilledColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    energy_tanks_empty_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=0.2541179955005646), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x63384f81, original_name='EnergyTanksEmptyColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    energy_digits_foreground_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.20000000298023224, g=0.33725500106811523, b=0.4392159879207611, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x1fd3d43a, original_name='EnergyDigitsForegroundColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    energy_digits_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xe1ff2a4f, original_name='EnergyDigitsOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    primary_energy_bar_filled_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x9cfb8a36, original_name='PrimaryEnergyBarFilledColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    primary_energy_bar_shadow_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x89a45bcb, original_name='PrimaryEnergyBarShadowColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    primary_energy_tank_filled_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xc2a8ccc6, original_name='PrimaryEnergyTankFilledColor', from_json=Color.from_json, to_json=Color.to_json
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
        if property_count != 10:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffff')
    
        dec = _FAST_FORMAT.unpack(data.read(220))
        assert (dec[0], dec[6], dec[12], dec[18], dec[24], dec[30], dec[36], dec[42], dec[48], dec[54]) == _FAST_IDS
        return cls(
            Color(*dec[2:6]),
            Color(*dec[8:12]),
            Color(*dec[14:18]),
            Color(*dec[20:24]),
            Color(*dec[26:30]),
            Color(*dec[32:36]),
            Color(*dec[38:42]),
            Color(*dec[44:48]),
            Color(*dec[50:54]),
            Color(*dec[56:60]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\n')  # 10 properties

        data.write(b'\xac\xf6-\x93')  # 0xacf62d93
        data.write(b'\x00\x10')  # size
        self.energy_bar_filled_color.to_stream(data, game)

        data.write(b'7\xe3\x81\xc2')  # 0x37e381c2
        data.write(b'\x00\x10')  # size
        self.energy_bar_empty_color.to_stream(data, game)

        data.write(b'\xb9\xa9\xfcn')  # 0xb9a9fc6e
        data.write(b'\x00\x10')  # size
        self.energy_bar_shadow_color.to_stream(data, game)

        data.write(b'Cw\xe6w')  # 0x4377e677
        data.write(b'\x00\x10')  # size
        self.energy_tanks_filled_color.to_stream(data, game)

        data.write(b'c8O\x81')  # 0x63384f81
        data.write(b'\x00\x10')  # size
        self.energy_tanks_empty_color.to_stream(data, game)

        data.write(b'\x1f\xd3\xd4:')  # 0x1fd3d43a
        data.write(b'\x00\x10')  # size
        self.energy_digits_foreground_color.to_stream(data, game)

        data.write(b'\xe1\xff*O')  # 0xe1ff2a4f
        data.write(b'\x00\x10')  # size
        self.energy_digits_outline_color.to_stream(data, game)

        data.write(b'\x9c\xfb\x8a6')  # 0x9cfb8a36
        data.write(b'\x00\x10')  # size
        self.primary_energy_bar_filled_color.to_stream(data, game)

        data.write(b'\x89\xa4[\xcb')  # 0x89a45bcb
        data.write(b'\x00\x10')  # size
        self.primary_energy_bar_shadow_color.to_stream(data, game)

        data.write(b'\xc2\xa8\xcc\xc6')  # 0xc2a8ccc6
        data.write(b'\x00\x10')  # size
        self.primary_energy_tank_filled_color.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGui_HudColorTypedefJson", data)
        return cls(
            energy_bar_filled_color=Color.from_json(json_data['energy_bar_filled_color']),
            energy_bar_empty_color=Color.from_json(json_data['energy_bar_empty_color']),
            energy_bar_shadow_color=Color.from_json(json_data['energy_bar_shadow_color']),
            energy_tanks_filled_color=Color.from_json(json_data['energy_tanks_filled_color']),
            energy_tanks_empty_color=Color.from_json(json_data['energy_tanks_empty_color']),
            energy_digits_foreground_color=Color.from_json(json_data['energy_digits_foreground_color']),
            energy_digits_outline_color=Color.from_json(json_data['energy_digits_outline_color']),
            primary_energy_bar_filled_color=Color.from_json(json_data['primary_energy_bar_filled_color']),
            primary_energy_bar_shadow_color=Color.from_json(json_data['primary_energy_bar_shadow_color']),
            primary_energy_tank_filled_color=Color.from_json(json_data['primary_energy_tank_filled_color']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'energy_bar_filled_color': self.energy_bar_filled_color.to_json(),
            'energy_bar_empty_color': self.energy_bar_empty_color.to_json(),
            'energy_bar_shadow_color': self.energy_bar_shadow_color.to_json(),
            'energy_tanks_filled_color': self.energy_tanks_filled_color.to_json(),
            'energy_tanks_empty_color': self.energy_tanks_empty_color.to_json(),
            'energy_digits_foreground_color': self.energy_digits_foreground_color.to_json(),
            'energy_digits_outline_color': self.energy_digits_outline_color.to_json(),
            'primary_energy_bar_filled_color': self.primary_energy_bar_filled_color.to_json(),
            'primary_energy_bar_shadow_color': self.primary_energy_bar_shadow_color.to_json(),
            'primary_energy_tank_filled_color': self.primary_energy_tank_filled_color.to_json(),
        }


def _decode_energy_bar_filled_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_bar_empty_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_bar_shadow_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_tanks_filled_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_tanks_empty_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_digits_foreground_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_digits_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_primary_energy_bar_filled_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_primary_energy_bar_shadow_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_primary_energy_tank_filled_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xacf62d93: ('energy_bar_filled_color', _decode_energy_bar_filled_color),
    0x37e381c2: ('energy_bar_empty_color', _decode_energy_bar_empty_color),
    0xb9a9fc6e: ('energy_bar_shadow_color', _decode_energy_bar_shadow_color),
    0x4377e677: ('energy_tanks_filled_color', _decode_energy_tanks_filled_color),
    0x63384f81: ('energy_tanks_empty_color', _decode_energy_tanks_empty_color),
    0x1fd3d43a: ('energy_digits_foreground_color', _decode_energy_digits_foreground_color),
    0xe1ff2a4f: ('energy_digits_outline_color', _decode_energy_digits_outline_color),
    0x9cfb8a36: ('primary_energy_bar_filled_color', _decode_primary_energy_bar_filled_color),
    0x89a45bcb: ('primary_energy_bar_shadow_color', _decode_primary_energy_bar_shadow_color),
    0xc2a8ccc6: ('primary_energy_tank_filled_color', _decode_primary_energy_tank_filled_color),
}
