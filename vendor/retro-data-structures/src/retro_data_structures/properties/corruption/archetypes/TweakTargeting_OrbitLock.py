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
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    class TweakTargeting_OrbitLockJson(typing_extensions.TypedDict):
        orbit_lock_indicator_scale: float
        orbit_lock_indicator_color: json_util.JsonValue
        orbit_lock_color: json_util.JsonValue
        orbit_lock_grapple_color: json_util.JsonValue
        orbit_lock_x_ray_color: json_util.JsonValue
        orbit_lock_indicator_position_offset: json_util.JsonValue
        orbit_lock_indicator_fade_time: float
        orbit_lock_indicator_transition_time: float
        orbit_lock_indicator_rotation: float
        orbit_lock_display_time: float
        orbit_lock_fade_time: float
        orbit_lock_min_alpha: float
        orbit_lock_gui_lock_color: json_util.JsonValue
        orbit_lock_gui_strafe_color: json_util.JsonValue
        orbit_lock_gui_rotation: float
        orbit_lock_gui_transition_time: float
        orbit_lock_gui_rotation_time: float
        unknown_0x26978c4b: float
        unknown_0x9d58f885: float
        unknown_0x99c2c9af: float
        unknown_0x326905f2: float
        orbit_lock_base_fly_in_start_time: float
        orbit_lock_base_fly_in_duration: float
        orbit_lock_base_start_scale: float
        orbit_lock_extras_color: json_util.JsonValue
        orbit_lock_bracket_fade_in_start_time: float
        orbit_lock_bracket_fade_in_duration: float
        orbit_lock_tech_open_start_time: float
        orbit_lock_tech_open_duration: float
        orbit_lock_rotation_start_time: float
        orbit_lock_tech_rotation_rate: float
        strafe_lock_max_alpha: float
        strafe_lock_fade_time: float
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x77feeef0, 0x6c68981b, 0x6d5bc9c5, 0x1b905dfe, 0x5ee18e2, 0x337e60a9, 0x4f635051, 0x20af6870, 0xa5848fb, 0x1b64bdf, 0xd4044569, 0xae6c5261, 0x84ac3eee, 0x396d001e, 0xe8008fa5, 0xe9c116bf, 0x79f18548, 0x26978c4b, 0x9d58f885, 0x99c2c9af, 0x326905f2, 0x3cf144d1, 0x7975982c, 0x460b2702, 0x43c8a56e, 0x83f19d56, 0xa9cd091f, 0xe589a4f9, 0xd7cf6cc5, 0x85e956d3, 0xa6f2b827, 0xca637bcd, 0xf04414b3)


@dataclasses.dataclass()
class TweakTargeting_OrbitLock(BaseProperty):
    orbit_lock_indicator_scale: float = dataclasses.field(default=0.15000000596046448, metadata={
        'reflection': FieldReflection[float](
            float, id=0x77feeef0, original_name='OrbitLockIndicatorScale'
        ),
    })
    orbit_lock_indicator_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x6c68981b, original_name='OrbitLockIndicatorColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    orbit_lock_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x6d5bc9c5, original_name='OrbitLockColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    orbit_lock_grapple_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x1b905dfe, original_name='OrbitLockGrappleColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    orbit_lock_x_ray_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x05ee18e2, original_name='OrbitLockXRayColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    orbit_lock_indicator_position_offset: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x337e60a9, original_name='OrbitLockIndicatorPositionOffset', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    orbit_lock_indicator_fade_time: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4f635051, original_name='OrbitLockIndicatorFadeTime'
        ),
    })
    orbit_lock_indicator_transition_time: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0x20af6870, original_name='OrbitLockIndicatorTransitionTime'
        ),
    })
    orbit_lock_indicator_rotation: float = dataclasses.field(default=120.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0a5848fb, original_name='OrbitLockIndicatorRotation'
        ),
    })
    orbit_lock_display_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x01b64bdf, original_name='OrbitLockDisplayTime'
        ),
    })
    orbit_lock_fade_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd4044569, original_name='OrbitLockFadeTime'
        ),
    })
    orbit_lock_min_alpha: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0xae6c5261, original_name='OrbitLockMinAlpha'
        ),
    })
    orbit_lock_gui_lock_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x84ac3eee, original_name='OrbitLockGUILockColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    orbit_lock_gui_strafe_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x396d001e, original_name='OrbitLockGUIStrafeColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    orbit_lock_gui_rotation: float = dataclasses.field(default=54.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe8008fa5, original_name='OrbitLockGUIRotation'
        ),
    })
    orbit_lock_gui_transition_time: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe9c116bf, original_name='OrbitLockGUITransitionTime'
        ),
    })
    orbit_lock_gui_rotation_time: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0x79f18548, original_name='OrbitLockGUIRotationTime'
        ),
    })
    unknown_0x26978c4b: float = dataclasses.field(default=0.15000000596046448, metadata={
        'reflection': FieldReflection[float](
            float, id=0x26978c4b, original_name='Unknown'
        ),
    })
    unknown_0x9d58f885: float = dataclasses.field(default=0.125, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9d58f885, original_name='Unknown'
        ),
    })
    unknown_0x99c2c9af: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0x99c2c9af, original_name='Unknown'
        ),
    })
    unknown_0x326905f2: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x326905f2, original_name='Unknown'
        ),
    })
    orbit_lock_base_fly_in_start_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3cf144d1, original_name='OrbitLockBaseFlyInStartTime'
        ),
    })
    orbit_lock_base_fly_in_duration: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7975982c, original_name='OrbitLockBaseFlyInDuration'
        ),
    })
    orbit_lock_base_start_scale: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x460b2702, original_name='OrbitLockBaseStartScale'
        ),
    })
    orbit_lock_extras_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x43c8a56e, original_name='OrbitLockExtrasColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    orbit_lock_bracket_fade_in_start_time: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0x83f19d56, original_name='OrbitLockBracketFadeInStartTime'
        ),
    })
    orbit_lock_bracket_fade_in_duration: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa9cd091f, original_name='OrbitLockBracketFadeInDuration'
        ),
    })
    orbit_lock_tech_open_start_time: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe589a4f9, original_name='OrbitLockTechOpenStartTime'
        ),
    })
    orbit_lock_tech_open_duration: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd7cf6cc5, original_name='OrbitLockTechOpenDuration'
        ),
    })
    orbit_lock_rotation_start_time: float = dataclasses.field(default=0.8999999761581421, metadata={
        'reflection': FieldReflection[float](
            float, id=0x85e956d3, original_name='OrbitLockRotationStartTime'
        ),
    })
    orbit_lock_tech_rotation_rate: float = dataclasses.field(default=135.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa6f2b827, original_name='OrbitLockTechRotationRate'
        ),
    })
    strafe_lock_max_alpha: float = dataclasses.field(default=0.3499999940395355, metadata={
        'reflection': FieldReflection[float](
            float, id=0xca637bcd, original_name='StrafeLockMaxAlpha'
        ),
    })
    strafe_lock_fade_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf04414b3, original_name='StrafeLockFadeTime'
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
        if property_count != 33:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHfLHffffLHffffLHffffLHffffLHfffLHfLHfLHfLHfLHfLHfLHffffLHffffLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHffffLHfLHfLHfLHfLHfLHfLHfLHf')
    
        dec = _FAST_FORMAT.unpack(data.read(422))
        assert (dec[0], dec[3], dec[9], dec[15], dec[21], dec[27], dec[32], dec[35], dec[38], dec[41], dec[44], dec[47], dec[50], dec[56], dec[62], dec[65], dec[68], dec[71], dec[74], dec[77], dec[80], dec[83], dec[86], dec[89], dec[92], dec[98], dec[101], dec[104], dec[107], dec[110], dec[113], dec[116], dec[119]) == _FAST_IDS
        return cls(
            dec[2],
            Color(*dec[5:9]),
            Color(*dec[11:15]),
            Color(*dec[17:21]),
            Color(*dec[23:27]),
            Vector(*dec[29:32]),
            dec[34],
            dec[37],
            dec[40],
            dec[43],
            dec[46],
            dec[49],
            Color(*dec[52:56]),
            Color(*dec[58:62]),
            dec[64],
            dec[67],
            dec[70],
            dec[73],
            dec[76],
            dec[79],
            dec[82],
            dec[85],
            dec[88],
            dec[91],
            Color(*dec[94:98]),
            dec[100],
            dec[103],
            dec[106],
            dec[109],
            dec[112],
            dec[115],
            dec[118],
            dec[121],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00!')  # 33 properties

        data.write(b'w\xfe\xee\xf0')  # 0x77feeef0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_indicator_scale))

        data.write(b'lh\x98\x1b')  # 0x6c68981b
        data.write(b'\x00\x10')  # size
        self.orbit_lock_indicator_color.to_stream(data, game)

        data.write(b'm[\xc9\xc5')  # 0x6d5bc9c5
        data.write(b'\x00\x10')  # size
        self.orbit_lock_color.to_stream(data, game)

        data.write(b'\x1b\x90]\xfe')  # 0x1b905dfe
        data.write(b'\x00\x10')  # size
        self.orbit_lock_grapple_color.to_stream(data, game)

        data.write(b'\x05\xee\x18\xe2')  # 0x5ee18e2
        data.write(b'\x00\x10')  # size
        self.orbit_lock_x_ray_color.to_stream(data, game)

        data.write(b'3~`\xa9')  # 0x337e60a9
        data.write(b'\x00\x0c')  # size
        self.orbit_lock_indicator_position_offset.to_stream(data, game)

        data.write(b'OcPQ')  # 0x4f635051
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_indicator_fade_time))

        data.write(b' \xafhp')  # 0x20af6870
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_indicator_transition_time))

        data.write(b'\nXH\xfb')  # 0xa5848fb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_indicator_rotation))

        data.write(b'\x01\xb6K\xdf')  # 0x1b64bdf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_display_time))

        data.write(b'\xd4\x04Ei')  # 0xd4044569
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_fade_time))

        data.write(b'\xaelRa')  # 0xae6c5261
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_min_alpha))

        data.write(b'\x84\xac>\xee')  # 0x84ac3eee
        data.write(b'\x00\x10')  # size
        self.orbit_lock_gui_lock_color.to_stream(data, game)

        data.write(b'9m\x00\x1e')  # 0x396d001e
        data.write(b'\x00\x10')  # size
        self.orbit_lock_gui_strafe_color.to_stream(data, game)

        data.write(b'\xe8\x00\x8f\xa5')  # 0xe8008fa5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_gui_rotation))

        data.write(b'\xe9\xc1\x16\xbf')  # 0xe9c116bf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_gui_transition_time))

        data.write(b'y\xf1\x85H')  # 0x79f18548
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_gui_rotation_time))

        data.write(b'&\x97\x8cK')  # 0x26978c4b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x26978c4b))

        data.write(b'\x9dX\xf8\x85')  # 0x9d58f885
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9d58f885))

        data.write(b'\x99\xc2\xc9\xaf')  # 0x99c2c9af
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x99c2c9af))

        data.write(b'2i\x05\xf2')  # 0x326905f2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x326905f2))

        data.write(b'<\xf1D\xd1')  # 0x3cf144d1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_base_fly_in_start_time))

        data.write(b'yu\x98,')  # 0x7975982c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_base_fly_in_duration))

        data.write(b"F\x0b'\x02")  # 0x460b2702
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_base_start_scale))

        data.write(b'C\xc8\xa5n')  # 0x43c8a56e
        data.write(b'\x00\x10')  # size
        self.orbit_lock_extras_color.to_stream(data, game)

        data.write(b'\x83\xf1\x9dV')  # 0x83f19d56
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_bracket_fade_in_start_time))

        data.write(b'\xa9\xcd\t\x1f')  # 0xa9cd091f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_bracket_fade_in_duration))

        data.write(b'\xe5\x89\xa4\xf9')  # 0xe589a4f9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_tech_open_start_time))

        data.write(b'\xd7\xcfl\xc5')  # 0xd7cf6cc5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_tech_open_duration))

        data.write(b'\x85\xe9V\xd3')  # 0x85e956d3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_rotation_start_time))

        data.write(b"\xa6\xf2\xb8'")  # 0xa6f2b827
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_tech_rotation_rate))

        data.write(b'\xcac{\xcd')  # 0xca637bcd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.strafe_lock_max_alpha))

        data.write(b'\xf0D\x14\xb3')  # 0xf04414b3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.strafe_lock_fade_time))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakTargeting_OrbitLockJson", data)
        return cls(
            orbit_lock_indicator_scale=json_data['orbit_lock_indicator_scale'],
            orbit_lock_indicator_color=Color.from_json(json_data['orbit_lock_indicator_color']),
            orbit_lock_color=Color.from_json(json_data['orbit_lock_color']),
            orbit_lock_grapple_color=Color.from_json(json_data['orbit_lock_grapple_color']),
            orbit_lock_x_ray_color=Color.from_json(json_data['orbit_lock_x_ray_color']),
            orbit_lock_indicator_position_offset=Vector.from_json(json_data['orbit_lock_indicator_position_offset']),
            orbit_lock_indicator_fade_time=json_data['orbit_lock_indicator_fade_time'],
            orbit_lock_indicator_transition_time=json_data['orbit_lock_indicator_transition_time'],
            orbit_lock_indicator_rotation=json_data['orbit_lock_indicator_rotation'],
            orbit_lock_display_time=json_data['orbit_lock_display_time'],
            orbit_lock_fade_time=json_data['orbit_lock_fade_time'],
            orbit_lock_min_alpha=json_data['orbit_lock_min_alpha'],
            orbit_lock_gui_lock_color=Color.from_json(json_data['orbit_lock_gui_lock_color']),
            orbit_lock_gui_strafe_color=Color.from_json(json_data['orbit_lock_gui_strafe_color']),
            orbit_lock_gui_rotation=json_data['orbit_lock_gui_rotation'],
            orbit_lock_gui_transition_time=json_data['orbit_lock_gui_transition_time'],
            orbit_lock_gui_rotation_time=json_data['orbit_lock_gui_rotation_time'],
            unknown_0x26978c4b=json_data['unknown_0x26978c4b'],
            unknown_0x9d58f885=json_data['unknown_0x9d58f885'],
            unknown_0x99c2c9af=json_data['unknown_0x99c2c9af'],
            unknown_0x326905f2=json_data['unknown_0x326905f2'],
            orbit_lock_base_fly_in_start_time=json_data['orbit_lock_base_fly_in_start_time'],
            orbit_lock_base_fly_in_duration=json_data['orbit_lock_base_fly_in_duration'],
            orbit_lock_base_start_scale=json_data['orbit_lock_base_start_scale'],
            orbit_lock_extras_color=Color.from_json(json_data['orbit_lock_extras_color']),
            orbit_lock_bracket_fade_in_start_time=json_data['orbit_lock_bracket_fade_in_start_time'],
            orbit_lock_bracket_fade_in_duration=json_data['orbit_lock_bracket_fade_in_duration'],
            orbit_lock_tech_open_start_time=json_data['orbit_lock_tech_open_start_time'],
            orbit_lock_tech_open_duration=json_data['orbit_lock_tech_open_duration'],
            orbit_lock_rotation_start_time=json_data['orbit_lock_rotation_start_time'],
            orbit_lock_tech_rotation_rate=json_data['orbit_lock_tech_rotation_rate'],
            strafe_lock_max_alpha=json_data['strafe_lock_max_alpha'],
            strafe_lock_fade_time=json_data['strafe_lock_fade_time'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'orbit_lock_indicator_scale': self.orbit_lock_indicator_scale,
            'orbit_lock_indicator_color': self.orbit_lock_indicator_color.to_json(),
            'orbit_lock_color': self.orbit_lock_color.to_json(),
            'orbit_lock_grapple_color': self.orbit_lock_grapple_color.to_json(),
            'orbit_lock_x_ray_color': self.orbit_lock_x_ray_color.to_json(),
            'orbit_lock_indicator_position_offset': self.orbit_lock_indicator_position_offset.to_json(),
            'orbit_lock_indicator_fade_time': self.orbit_lock_indicator_fade_time,
            'orbit_lock_indicator_transition_time': self.orbit_lock_indicator_transition_time,
            'orbit_lock_indicator_rotation': self.orbit_lock_indicator_rotation,
            'orbit_lock_display_time': self.orbit_lock_display_time,
            'orbit_lock_fade_time': self.orbit_lock_fade_time,
            'orbit_lock_min_alpha': self.orbit_lock_min_alpha,
            'orbit_lock_gui_lock_color': self.orbit_lock_gui_lock_color.to_json(),
            'orbit_lock_gui_strafe_color': self.orbit_lock_gui_strafe_color.to_json(),
            'orbit_lock_gui_rotation': self.orbit_lock_gui_rotation,
            'orbit_lock_gui_transition_time': self.orbit_lock_gui_transition_time,
            'orbit_lock_gui_rotation_time': self.orbit_lock_gui_rotation_time,
            'unknown_0x26978c4b': self.unknown_0x26978c4b,
            'unknown_0x9d58f885': self.unknown_0x9d58f885,
            'unknown_0x99c2c9af': self.unknown_0x99c2c9af,
            'unknown_0x326905f2': self.unknown_0x326905f2,
            'orbit_lock_base_fly_in_start_time': self.orbit_lock_base_fly_in_start_time,
            'orbit_lock_base_fly_in_duration': self.orbit_lock_base_fly_in_duration,
            'orbit_lock_base_start_scale': self.orbit_lock_base_start_scale,
            'orbit_lock_extras_color': self.orbit_lock_extras_color.to_json(),
            'orbit_lock_bracket_fade_in_start_time': self.orbit_lock_bracket_fade_in_start_time,
            'orbit_lock_bracket_fade_in_duration': self.orbit_lock_bracket_fade_in_duration,
            'orbit_lock_tech_open_start_time': self.orbit_lock_tech_open_start_time,
            'orbit_lock_tech_open_duration': self.orbit_lock_tech_open_duration,
            'orbit_lock_rotation_start_time': self.orbit_lock_rotation_start_time,
            'orbit_lock_tech_rotation_rate': self.orbit_lock_tech_rotation_rate,
            'strafe_lock_max_alpha': self.strafe_lock_max_alpha,
            'strafe_lock_fade_time': self.strafe_lock_fade_time,
        }


def _decode_orbit_lock_indicator_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_orbit_lock_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_orbit_lock_grapple_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_orbit_lock_x_ray_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_orbit_lock_indicator_position_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_orbit_lock_gui_lock_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_orbit_lock_gui_strafe_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_orbit_lock_extras_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x77feeef0: ('orbit_lock_indicator_scale', structs.decode_BIG_f),
    0x6c68981b: ('orbit_lock_indicator_color', _decode_orbit_lock_indicator_color),
    0x6d5bc9c5: ('orbit_lock_color', _decode_orbit_lock_color),
    0x1b905dfe: ('orbit_lock_grapple_color', _decode_orbit_lock_grapple_color),
    0x05ee18e2: ('orbit_lock_x_ray_color', _decode_orbit_lock_x_ray_color),
    0x337e60a9: ('orbit_lock_indicator_position_offset', _decode_orbit_lock_indicator_position_offset),
    0x4f635051: ('orbit_lock_indicator_fade_time', structs.decode_BIG_f),
    0x20af6870: ('orbit_lock_indicator_transition_time', structs.decode_BIG_f),
    0x0a5848fb: ('orbit_lock_indicator_rotation', structs.decode_BIG_f),
    0x01b64bdf: ('orbit_lock_display_time', structs.decode_BIG_f),
    0xd4044569: ('orbit_lock_fade_time', structs.decode_BIG_f),
    0xae6c5261: ('orbit_lock_min_alpha', structs.decode_BIG_f),
    0x84ac3eee: ('orbit_lock_gui_lock_color', _decode_orbit_lock_gui_lock_color),
    0x396d001e: ('orbit_lock_gui_strafe_color', _decode_orbit_lock_gui_strafe_color),
    0xe8008fa5: ('orbit_lock_gui_rotation', structs.decode_BIG_f),
    0xe9c116bf: ('orbit_lock_gui_transition_time', structs.decode_BIG_f),
    0x79f18548: ('orbit_lock_gui_rotation_time', structs.decode_BIG_f),
    0x26978c4b: ('unknown_0x26978c4b', structs.decode_BIG_f),
    0x9d58f885: ('unknown_0x9d58f885', structs.decode_BIG_f),
    0x99c2c9af: ('unknown_0x99c2c9af', structs.decode_BIG_f),
    0x326905f2: ('unknown_0x326905f2', structs.decode_BIG_f),
    0x3cf144d1: ('orbit_lock_base_fly_in_start_time', structs.decode_BIG_f),
    0x7975982c: ('orbit_lock_base_fly_in_duration', structs.decode_BIG_f),
    0x460b2702: ('orbit_lock_base_start_scale', structs.decode_BIG_f),
    0x43c8a56e: ('orbit_lock_extras_color', _decode_orbit_lock_extras_color),
    0x83f19d56: ('orbit_lock_bracket_fade_in_start_time', structs.decode_BIG_f),
    0xa9cd091f: ('orbit_lock_bracket_fade_in_duration', structs.decode_BIG_f),
    0xe589a4f9: ('orbit_lock_tech_open_start_time', structs.decode_BIG_f),
    0xd7cf6cc5: ('orbit_lock_tech_open_duration', structs.decode_BIG_f),
    0x85e956d3: ('orbit_lock_rotation_start_time', structs.decode_BIG_f),
    0xa6f2b827: ('orbit_lock_tech_rotation_rate', structs.decode_BIG_f),
    0xca637bcd: ('strafe_lock_max_alpha', structs.decode_BIG_f),
    0xf04414b3: ('strafe_lock_fade_time', structs.decode_BIG_f),
}
