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

if typing.TYPE_CHECKING:
    class TweakGui_ScanVisorJson(typing_extensions.TypedDict):
        non_scannable_modulation: json_util.JsonValue
        inactive_color: json_util.JsonValue
        inactive_external_color: json_util.JsonValue
        non_critical_color: json_util.JsonValue
        critical_color: json_util.JsonValue
        burn_in_color: json_util.JsonValue
        highlight_color: json_util.JsonValue
        unknown_0x84badf82: json_util.JsonValue
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
        scan_clamp_scale: float
        unknown_0x58bc9d5d: float
        fly_in_spline0: json_util.JsonObject
        fly_in_spline1: json_util.JsonObject
        fly_in_spline2: json_util.JsonObject
        fly_in_spline3: json_util.JsonObject
        fly_in_spline4: json_util.JsonObject
        fly_in_spline5: json_util.JsonObject
    

@dataclasses.dataclass()
class TweakGui_ScanVisor(BaseProperty):
    non_scannable_modulation: Color = dataclasses.field(default_factory=lambda: Color(r=0.5, g=0.5, b=0.5, a=0.875), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x5d750eef, original_name='NonScannableModulation', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
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
    unknown_0x84badf82: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=1.0, b=0.0, a=0.25), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x84badf82, original_name='Unknown', from_json=Color.from_json, to_json=Color.to_json
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
    scan_clamp_scale: float = dataclasses.field(default=0.6000000238418579, metadata={
        'reflection': FieldReflection[float](
            float, id=0xee169779, original_name='ScanClampScale'
        ),
    })
    unknown_0x58bc9d5d: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0x58bc9d5d, original_name='Unknown'
        ),
    })
    fly_in_spline0: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xf4f19c8b, original_name='FlyInSpline0', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    fly_in_spline1: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x5286973f, original_name='FlyInSpline1', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    fly_in_spline2: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x636e8da2, original_name='FlyInSpline2', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    fly_in_spline3: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xc5198616, original_name='FlyInSpline3', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    fly_in_spline4: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x00beb898, original_name='FlyInSpline4', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    fly_in_spline5: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xa6c9b32c, original_name='FlyInSpline5', from_json=Spline.from_json, to_json=Spline.to_json
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
        if property_count != 26:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5d750eef
        non_scannable_modulation = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x972271b9
        inactive_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa908c775
        inactive_external_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xee1f1df6
        non_critical_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x43445ae7
        critical_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf48fd559
        burn_in_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7a6412f6
        highlight_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x84badf82
        unknown_0x84badf82 = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf45f7d17
        critical_highlight_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe8f5018b
        previously_scanned_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xba1ae1e5
        critical_previously_scanned_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb39d450e
        previously_scanned_highlight_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1042455b
        critical_previously_scanned_highlight_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd72435ad
        hacked_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x75cdc913
        hacked_highlighted_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x997ec38d
        sweep_bar_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x00b83f02
        burn_in_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7c269ebc
        fade_out_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xee169779
        scan_clamp_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58bc9d5d
        unknown_0x58bc9d5d = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf4f19c8b
        fly_in_spline0 = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5286973f
        fly_in_spline1 = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x636e8da2
        fly_in_spline2 = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc5198616
        fly_in_spline3 = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x00beb898
        fly_in_spline4 = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa6c9b32c
        fly_in_spline5 = Spline.from_stream(data, game, property_size)
    
        return cls(non_scannable_modulation, inactive_color, inactive_external_color, non_critical_color, critical_color, burn_in_color, highlight_color, unknown_0x84badf82, critical_highlight_color, previously_scanned_color, critical_previously_scanned_color, previously_scanned_highlight_color, critical_previously_scanned_highlight_color, hacked_color, hacked_highlighted_color, sweep_bar_color, burn_in_time, fade_out_time, scan_clamp_scale, unknown_0x58bc9d5d, fly_in_spline0, fly_in_spline1, fly_in_spline2, fly_in_spline3, fly_in_spline4, fly_in_spline5)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x1a')  # 26 properties

        data.write(b']u\x0e\xef')  # 0x5d750eef
        data.write(b'\x00\x10')  # size
        self.non_scannable_modulation.to_stream(data, game)

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

        data.write(b'\x84\xba\xdf\x82')  # 0x84badf82
        data.write(b'\x00\x10')  # size
        self.unknown_0x84badf82.to_stream(data, game)

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

        data.write(b'\xee\x16\x97y')  # 0xee169779
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_clamp_scale))

        data.write(b'X\xbc\x9d]')  # 0x58bc9d5d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x58bc9d5d))

        data.write(b'\xf4\xf1\x9c\x8b')  # 0xf4f19c8b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.fly_in_spline0.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'R\x86\x97?')  # 0x5286973f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.fly_in_spline1.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'cn\x8d\xa2')  # 0x636e8da2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.fly_in_spline2.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc5\x19\x86\x16')  # 0xc5198616
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.fly_in_spline3.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x00\xbe\xb8\x98')  # 0xbeb898
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.fly_in_spline4.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa6\xc9\xb3,')  # 0xa6c9b32c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.fly_in_spline5.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGui_ScanVisorJson", data)
        return cls(
            non_scannable_modulation=Color.from_json(json_data['non_scannable_modulation']),
            inactive_color=Color.from_json(json_data['inactive_color']),
            inactive_external_color=Color.from_json(json_data['inactive_external_color']),
            non_critical_color=Color.from_json(json_data['non_critical_color']),
            critical_color=Color.from_json(json_data['critical_color']),
            burn_in_color=Color.from_json(json_data['burn_in_color']),
            highlight_color=Color.from_json(json_data['highlight_color']),
            unknown_0x84badf82=Color.from_json(json_data['unknown_0x84badf82']),
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
            scan_clamp_scale=json_data['scan_clamp_scale'],
            unknown_0x58bc9d5d=json_data['unknown_0x58bc9d5d'],
            fly_in_spline0=Spline.from_json(json_data['fly_in_spline0']),
            fly_in_spline1=Spline.from_json(json_data['fly_in_spline1']),
            fly_in_spline2=Spline.from_json(json_data['fly_in_spline2']),
            fly_in_spline3=Spline.from_json(json_data['fly_in_spline3']),
            fly_in_spline4=Spline.from_json(json_data['fly_in_spline4']),
            fly_in_spline5=Spline.from_json(json_data['fly_in_spline5']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'non_scannable_modulation': self.non_scannable_modulation.to_json(),
            'inactive_color': self.inactive_color.to_json(),
            'inactive_external_color': self.inactive_external_color.to_json(),
            'non_critical_color': self.non_critical_color.to_json(),
            'critical_color': self.critical_color.to_json(),
            'burn_in_color': self.burn_in_color.to_json(),
            'highlight_color': self.highlight_color.to_json(),
            'unknown_0x84badf82': self.unknown_0x84badf82.to_json(),
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
            'scan_clamp_scale': self.scan_clamp_scale,
            'unknown_0x58bc9d5d': self.unknown_0x58bc9d5d,
            'fly_in_spline0': self.fly_in_spline0.to_json(),
            'fly_in_spline1': self.fly_in_spline1.to_json(),
            'fly_in_spline2': self.fly_in_spline2.to_json(),
            'fly_in_spline3': self.fly_in_spline3.to_json(),
            'fly_in_spline4': self.fly_in_spline4.to_json(),
            'fly_in_spline5': self.fly_in_spline5.to_json(),
        }


def _decode_non_scannable_modulation(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


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


def _decode_unknown_0x84badf82(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
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


def _decode_fly_in_spline0(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_fly_in_spline1(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_fly_in_spline2(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_fly_in_spline3(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_fly_in_spline4(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_fly_in_spline5(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x5d750eef: ('non_scannable_modulation', _decode_non_scannable_modulation),
    0x972271b9: ('inactive_color', _decode_inactive_color),
    0xa908c775: ('inactive_external_color', _decode_inactive_external_color),
    0xee1f1df6: ('non_critical_color', _decode_non_critical_color),
    0x43445ae7: ('critical_color', _decode_critical_color),
    0xf48fd559: ('burn_in_color', _decode_burn_in_color),
    0x7a6412f6: ('highlight_color', _decode_highlight_color),
    0x84badf82: ('unknown_0x84badf82', _decode_unknown_0x84badf82),
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
    0xee169779: ('scan_clamp_scale', structs.decode_BIG_f),
    0x58bc9d5d: ('unknown_0x58bc9d5d', structs.decode_BIG_f),
    0xf4f19c8b: ('fly_in_spline0', _decode_fly_in_spline0),
    0x5286973f: ('fly_in_spline1', _decode_fly_in_spline1),
    0x636e8da2: ('fly_in_spline2', _decode_fly_in_spline2),
    0xc5198616: ('fly_in_spline3', _decode_fly_in_spline3),
    0x00beb898: ('fly_in_spline4', _decode_fly_in_spline4),
    0xa6c9b32c: ('fly_in_spline5', _decode_fly_in_spline5),
}
