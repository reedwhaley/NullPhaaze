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
    class TweakGui_ScanVisorJson(typing_extensions.TypedDict):
        inactive_color: json_util.JsonValue
        inactive_external_color: json_util.JsonValue
        non_critical_color: json_util.JsonValue
        critical_color: json_util.JsonValue
        burn_in_color: json_util.JsonValue
        highlight_color: json_util.JsonValue
        critical_highlight_color: json_util.JsonValue
        previously_scanned_color: json_util.JsonValue
        critical_previously_scanned_color: json_util.JsonValue
        previously_scanned_highlight_color: json_util.JsonValue
        critical_previously_scanned_highlight_color: json_util.JsonValue
        hacked_color: json_util.JsonValue
        hacked_highlighted_color: json_util.JsonValue
        sweep_bar_color: json_util.JsonValue
        burn_in_time: float
        fade_out_time: float
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x972271b9, 0xa908c775, 0xee1f1df6, 0x43445ae7, 0xf48fd559, 0x7a6412f6, 0xf45f7d17, 0xe8f5018b, 0xba1ae1e5, 0xb39d450e, 0x1042455b, 0xd72435ad, 0x75cdc913, 0x997ec38d, 0xb83f02, 0x7c269ebc)


@dataclasses.dataclass()
class TweakGui_ScanVisor(BaseProperty):
    inactive_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.20000000298023224, g=0.20000000298023224, b=0.20000000298023224, a=0.5), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x972271b9, original_name='InactiveColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    inactive_external_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.20000000298023224, g=0.20000000298023224, b=0.20000000298023224, a=0.5), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xa908c775, original_name='InactiveExternalColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    non_critical_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.11999999731779099, b=0.25, a=0.5), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xee1f1df6, original_name='NonCriticalColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    critical_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.25, g=0.25, b=0.0, a=0.5), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x43445ae7, original_name='CriticalColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    burn_in_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf48fd559, original_name='BurnInColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    highlight_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.5, g=0.0, b=0.0, a=0.5), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x7a6412f6, original_name='HighlightColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    critical_highlight_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=1.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf45f7d17, original_name='CriticalHighlightColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    previously_scanned_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.25, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xe8f5018b, original_name='PreviouslyScannedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    critical_previously_scanned_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xba1ae1e5, original_name='CriticalPreviouslyScannedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    previously_scanned_highlight_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.5, g=0.0, b=0.0, a=0.5), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xb39d450e, original_name='PreviouslyScannedHighlightColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    critical_previously_scanned_highlight_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=1.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x1042455b, original_name='CriticalPreviouslyScannedHighlightColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    hacked_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xd72435ad, original_name='HackedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    hacked_highlighted_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x75cdc913, original_name='HackedHighlightedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    sweep_bar_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.20000000298023224, g=0.20000000298023224, b=0.20000000298023224, a=0.5), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x997ec38d, original_name='SweepBarColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    burn_in_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x00b83f02, original_name='BurnInTime'
        ),
    })
    fade_out_time: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7c269ebc, original_name='FadeOutTime'
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
        if property_count != 16:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHfLHf')
    
        dec = _FAST_FORMAT.unpack(data.read(328))
        assert (dec[0], dec[6], dec[12], dec[18], dec[24], dec[30], dec[36], dec[42], dec[48], dec[54], dec[60], dec[66], dec[72], dec[78], dec[84], dec[87]) == _FAST_IDS
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
            Color(*dec[62:66]),
            Color(*dec[68:72]),
            Color(*dec[74:78]),
            Color(*dec[80:84]),
            dec[86],
            dec[89],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x10')  # 16 properties

        data.write(b'\x97"q\xb9')  # 0x972271b9
        data.write(b'\x00\x10')  # size
        self.inactive_color.to_stream(data, game)

        data.write(b'\xa9\x08\xc7u')  # 0xa908c775
        data.write(b'\x00\x10')  # size
        self.inactive_external_color.to_stream(data, game)

        data.write(b'\xee\x1f\x1d\xf6')  # 0xee1f1df6
        data.write(b'\x00\x10')  # size
        self.non_critical_color.to_stream(data, game)

        data.write(b'CDZ\xe7')  # 0x43445ae7
        data.write(b'\x00\x10')  # size
        self.critical_color.to_stream(data, game)

        data.write(b'\xf4\x8f\xd5Y')  # 0xf48fd559
        data.write(b'\x00\x10')  # size
        self.burn_in_color.to_stream(data, game)

        data.write(b'zd\x12\xf6')  # 0x7a6412f6
        data.write(b'\x00\x10')  # size
        self.highlight_color.to_stream(data, game)

        data.write(b'\xf4_}\x17')  # 0xf45f7d17
        data.write(b'\x00\x10')  # size
        self.critical_highlight_color.to_stream(data, game)

        data.write(b'\xe8\xf5\x01\x8b')  # 0xe8f5018b
        data.write(b'\x00\x10')  # size
        self.previously_scanned_color.to_stream(data, game)

        data.write(b'\xba\x1a\xe1\xe5')  # 0xba1ae1e5
        data.write(b'\x00\x10')  # size
        self.critical_previously_scanned_color.to_stream(data, game)

        data.write(b'\xb3\x9dE\x0e')  # 0xb39d450e
        data.write(b'\x00\x10')  # size
        self.previously_scanned_highlight_color.to_stream(data, game)

        data.write(b'\x10BE[')  # 0x1042455b
        data.write(b'\x00\x10')  # size
        self.critical_previously_scanned_highlight_color.to_stream(data, game)

        data.write(b'\xd7$5\xad')  # 0xd72435ad
        data.write(b'\x00\x10')  # size
        self.hacked_color.to_stream(data, game)

        data.write(b'u\xcd\xc9\x13')  # 0x75cdc913
        data.write(b'\x00\x10')  # size
        self.hacked_highlighted_color.to_stream(data, game)

        data.write(b'\x99~\xc3\x8d')  # 0x997ec38d
        data.write(b'\x00\x10')  # size
        self.sweep_bar_color.to_stream(data, game)

        data.write(b'\x00\xb8?\x02')  # 0xb83f02
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.burn_in_time))

        data.write(b'|&\x9e\xbc')  # 0x7c269ebc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fade_out_time))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGui_ScanVisorJson", data)
        return cls(
            inactive_color=Color.from_json(json_data['inactive_color']),
            inactive_external_color=Color.from_json(json_data['inactive_external_color']),
            non_critical_color=Color.from_json(json_data['non_critical_color']),
            critical_color=Color.from_json(json_data['critical_color']),
            burn_in_color=Color.from_json(json_data['burn_in_color']),
            highlight_color=Color.from_json(json_data['highlight_color']),
            critical_highlight_color=Color.from_json(json_data['critical_highlight_color']),
            previously_scanned_color=Color.from_json(json_data['previously_scanned_color']),
            critical_previously_scanned_color=Color.from_json(json_data['critical_previously_scanned_color']),
            previously_scanned_highlight_color=Color.from_json(json_data['previously_scanned_highlight_color']),
            critical_previously_scanned_highlight_color=Color.from_json(json_data['critical_previously_scanned_highlight_color']),
            hacked_color=Color.from_json(json_data['hacked_color']),
            hacked_highlighted_color=Color.from_json(json_data['hacked_highlighted_color']),
            sweep_bar_color=Color.from_json(json_data['sweep_bar_color']),
            burn_in_time=json_data['burn_in_time'],
            fade_out_time=json_data['fade_out_time'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'inactive_color': self.inactive_color.to_json(),
            'inactive_external_color': self.inactive_external_color.to_json(),
            'non_critical_color': self.non_critical_color.to_json(),
            'critical_color': self.critical_color.to_json(),
            'burn_in_color': self.burn_in_color.to_json(),
            'highlight_color': self.highlight_color.to_json(),
            'critical_highlight_color': self.critical_highlight_color.to_json(),
            'previously_scanned_color': self.previously_scanned_color.to_json(),
            'critical_previously_scanned_color': self.critical_previously_scanned_color.to_json(),
            'previously_scanned_highlight_color': self.previously_scanned_highlight_color.to_json(),
            'critical_previously_scanned_highlight_color': self.critical_previously_scanned_highlight_color.to_json(),
            'hacked_color': self.hacked_color.to_json(),
            'hacked_highlighted_color': self.hacked_highlighted_color.to_json(),
            'sweep_bar_color': self.sweep_bar_color.to_json(),
            'burn_in_time': self.burn_in_time,
            'fade_out_time': self.fade_out_time,
        }


def _decode_inactive_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_inactive_external_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_non_critical_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_critical_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_burn_in_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_highlight_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_critical_highlight_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_previously_scanned_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_critical_previously_scanned_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_previously_scanned_highlight_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_critical_previously_scanned_highlight_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_hacked_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_hacked_highlighted_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_sweep_bar_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x972271b9: ('inactive_color', _decode_inactive_color),
    0xa908c775: ('inactive_external_color', _decode_inactive_external_color),
    0xee1f1df6: ('non_critical_color', _decode_non_critical_color),
    0x43445ae7: ('critical_color', _decode_critical_color),
    0xf48fd559: ('burn_in_color', _decode_burn_in_color),
    0x7a6412f6: ('highlight_color', _decode_highlight_color),
    0xf45f7d17: ('critical_highlight_color', _decode_critical_highlight_color),
    0xe8f5018b: ('previously_scanned_color', _decode_previously_scanned_color),
    0xba1ae1e5: ('critical_previously_scanned_color', _decode_critical_previously_scanned_color),
    0xb39d450e: ('previously_scanned_highlight_color', _decode_previously_scanned_highlight_color),
    0x1042455b: ('critical_previously_scanned_highlight_color', _decode_critical_previously_scanned_highlight_color),
    0xd72435ad: ('hacked_color', _decode_hacked_color),
    0x75cdc913: ('hacked_highlighted_color', _decode_hacked_highlighted_color),
    0x997ec38d: ('sweep_bar_color', _decode_sweep_bar_color),
    0x00b83f02: ('burn_in_time', structs.decode_BIG_f),
    0x7c269ebc: ('fade_out_time', structs.decode_BIG_f),
}
