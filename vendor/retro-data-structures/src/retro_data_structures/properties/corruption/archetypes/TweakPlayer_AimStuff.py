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

if typing.TYPE_CHECKING:
    class TweakPlayer_AimStuffJson(typing_extensions.TypedDict):
        aim_min_time: float
        aim_max_time: float
        aim_max_distance: float
        aim_max_angle_left: float
        aim_max_angle_right: float
        aim_max_angle_up: float
        aim_max_angle_down: float
        aim_angle_per_second: float
        aim_threshold_distance: float
        aim_turn_angle_per_second: float
        aim_new_target_radius: float
        aim_box_width: float
        aim_box_height: float
        aim_target_timer: float
        aim_assist_horizontal_angle: float
        aim_assist_vertical_angle: float
        rev_free_look_gun: bool
        rev_orbit_lock_gun: bool
        rev_orbit_tag_objects: bool
        rev_lock_cursor: bool
        rev_view_lock_disables_turn: bool
        rev_view_lock_type: int
        rev_free_look_velocity: bool
        rev_free_look_velocity_per_second: float
        unknown_0x21047226: bool
        unknown_0x95f112be: float
        unknown_0xb5d9e201: bool
        unknown_0x747a79cb: float
        unknown_0x189d7017: int
        unknown_0xa065b70c: bool
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x27c60d0a, 0xb7b51de0, 0xf77d0359, 0xde887cca, 0xb4b07d5d, 0xe5f8c567, 0x9774749d, 0x133f3002, 0x96fab602, 0x94164a2f, 0x54354c80, 0x5361ce18, 0x4b2e9260, 0x3b9a3789, 0x38dd0b85, 0x1157883e, 0x38ee6d6e, 0x9e3aceb5, 0x228a8def, 0x534a7b3c, 0xd2dfc16a, 0x60f08beb, 0xcca13e22, 0x85437c89, 0x21047226, 0x95f112be, 0xb5d9e201, 0x747a79cb, 0x189d7017, 0xa065b70c)


@dataclasses.dataclass()
class TweakPlayer_AimStuff(BaseProperty):
    aim_min_time: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x27c60d0a, original_name='AimMinTime'
        ),
    })
    aim_max_time: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb7b51de0, original_name='AimMaxTime'
        ),
    })
    aim_max_distance: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf77d0359, original_name='AimMaxDistance'
        ),
    })
    aim_max_angle_left: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xde887cca, original_name='AimMaxAngleLeft'
        ),
    })
    aim_max_angle_right: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb4b07d5d, original_name='AimMaxAngleRight'
        ),
    })
    aim_max_angle_up: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe5f8c567, original_name='AimMaxAngleUp'
        ),
    })
    aim_max_angle_down: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9774749d, original_name='AimMaxAngleDown'
        ),
    })
    aim_angle_per_second: float = dataclasses.field(default=110.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x133f3002, original_name='AimAnglePerSecond'
        ),
    })
    aim_threshold_distance: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x96fab602, original_name='AimThresholdDistance'
        ),
    })
    aim_turn_angle_per_second: float = dataclasses.field(default=360.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x94164a2f, original_name='AimTurnAnglePerSecond'
        ),
    })
    aim_new_target_radius: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x54354c80, original_name='AimNewTargetRadius'
        ),
    })
    aim_box_width: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5361ce18, original_name='AimBoxWidth'
        ),
    })
    aim_box_height: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4b2e9260, original_name='AimBoxHeight'
        ),
    })
    aim_target_timer: float = dataclasses.field(default=0.009999999776482582, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3b9a3789, original_name='AimTargetTimer'
        ),
    })
    aim_assist_horizontal_angle: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x38dd0b85, original_name='AimAssistHorizontalAngle'
        ),
    })
    aim_assist_vertical_angle: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1157883e, original_name='AimAssistVerticalAngle'
        ),
    })
    rev_free_look_gun: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x38ee6d6e, original_name='RevFreeLookGun'
        ),
    })
    rev_orbit_lock_gun: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x9e3aceb5, original_name='RevOrbitLockGun'
        ),
    })
    rev_orbit_tag_objects: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x228a8def, original_name='RevOrbitTagObjects'
        ),
    })
    rev_lock_cursor: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x534a7b3c, original_name='RevLockCursor'
        ),
    })
    rev_view_lock_disables_turn: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xd2dfc16a, original_name='RevViewLockDisablesTurn'
        ),
    })
    rev_view_lock_type: enums.RevViewLockTypeEnum = dataclasses.field(default=enums.RevViewLockTypeEnum.kVLT_HoldToLock, metadata={
        'reflection': FieldReflection[enums.RevViewLockTypeEnum](
            enums.RevViewLockTypeEnum, id=0x60f08beb, original_name='RevViewLockType', from_json=enums.RevViewLockTypeEnum.from_json, to_json=enums.RevViewLockTypeEnum.to_json
        ),
    })
    rev_free_look_velocity: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xcca13e22, original_name='RevFreeLookVelocity'
        ),
    })
    rev_free_look_velocity_per_second: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x85437c89, original_name='RevFreeLookVelocityPerSecond'
        ),
    })
    unknown_0x21047226: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x21047226, original_name='Unknown'
        ),
    })
    unknown_0x95f112be: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x95f112be, original_name='Unknown'
        ),
    })
    unknown_0xb5d9e201: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xb5d9e201, original_name='Unknown'
        ),
    })
    unknown_0x747a79cb: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x747a79cb, original_name='Unknown'
        ),
    })
    unknown_0x189d7017: enums.TweakPlayer_AimStuff_UnknownEnum2Enum = dataclasses.field(default=enums.TweakPlayer_AimStuff_UnknownEnum2Enum.kIRT_Both, metadata={
        'reflection': FieldReflection[enums.TweakPlayer_AimStuff_UnknownEnum2Enum](
            enums.TweakPlayer_AimStuff_UnknownEnum2Enum, id=0x189d7017, original_name='Unknown', from_json=enums.TweakPlayer_AimStuff_UnknownEnum2Enum.from_json, to_json=enums.TweakPlayer_AimStuff_UnknownEnum2Enum.to_json
        ),
    })
    unknown_0xa065b70c: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xa065b70c, original_name='Unknown'
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
        if property_count != 30:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLH?LH?LH?LH?LH?LHLLH?LHfLH?LHfLH?LHfLHLLH?')
    
        dec = _FAST_FORMAT.unpack(data.read(273))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24], dec[27], dec[30], dec[33], dec[36], dec[39], dec[42], dec[45], dec[48], dec[51], dec[54], dec[57], dec[60], dec[63], dec[66], dec[69], dec[72], dec[75], dec[78], dec[81], dec[84], dec[87]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
            dec[26],
            dec[29],
            dec[32],
            dec[35],
            dec[38],
            dec[41],
            dec[44],
            dec[47],
            dec[50],
            dec[53],
            dec[56],
            dec[59],
            dec[62],
            enums.RevViewLockTypeEnum(dec[65]),
            dec[68],
            dec[71],
            dec[74],
            dec[77],
            dec[80],
            dec[83],
            enums.TweakPlayer_AimStuff_UnknownEnum2Enum(dec[86]),
            dec[89],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x1e')  # 30 properties

        data.write(b"'\xc6\r\n")  # 0x27c60d0a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aim_min_time))

        data.write(b'\xb7\xb5\x1d\xe0')  # 0xb7b51de0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aim_max_time))

        data.write(b'\xf7}\x03Y')  # 0xf77d0359
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aim_max_distance))

        data.write(b'\xde\x88|\xca')  # 0xde887cca
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aim_max_angle_left))

        data.write(b'\xb4\xb0}]')  # 0xb4b07d5d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aim_max_angle_right))

        data.write(b'\xe5\xf8\xc5g')  # 0xe5f8c567
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aim_max_angle_up))

        data.write(b'\x97tt\x9d')  # 0x9774749d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aim_max_angle_down))

        data.write(b'\x13?0\x02')  # 0x133f3002
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aim_angle_per_second))

        data.write(b'\x96\xfa\xb6\x02')  # 0x96fab602
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aim_threshold_distance))

        data.write(b'\x94\x16J/')  # 0x94164a2f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aim_turn_angle_per_second))

        data.write(b'T5L\x80')  # 0x54354c80
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aim_new_target_radius))

        data.write(b'Sa\xce\x18')  # 0x5361ce18
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aim_box_width))

        data.write(b'K.\x92`')  # 0x4b2e9260
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aim_box_height))

        data.write(b';\x9a7\x89')  # 0x3b9a3789
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aim_target_timer))

        data.write(b'8\xdd\x0b\x85')  # 0x38dd0b85
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aim_assist_horizontal_angle))

        data.write(b'\x11W\x88>')  # 0x1157883e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aim_assist_vertical_angle))

        data.write(b'8\xeemn')  # 0x38ee6d6e
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.rev_free_look_gun))

        data.write(b'\x9e:\xce\xb5')  # 0x9e3aceb5
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.rev_orbit_lock_gun))

        data.write(b'"\x8a\x8d\xef')  # 0x228a8def
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.rev_orbit_tag_objects))

        data.write(b'SJ{<')  # 0x534a7b3c
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.rev_lock_cursor))

        data.write(b'\xd2\xdf\xc1j')  # 0xd2dfc16a
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.rev_view_lock_disables_turn))

        data.write(b'`\xf0\x8b\xeb')  # 0x60f08beb
        data.write(b'\x00\x04')  # size
        self.rev_view_lock_type.to_stream(data, game)

        data.write(b'\xcc\xa1>"')  # 0xcca13e22
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.rev_free_look_velocity))

        data.write(b'\x85C|\x89')  # 0x85437c89
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rev_free_look_velocity_per_second))

        data.write(b'!\x04r&')  # 0x21047226
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x21047226))

        data.write(b'\x95\xf1\x12\xbe')  # 0x95f112be
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x95f112be))

        data.write(b'\xb5\xd9\xe2\x01')  # 0xb5d9e201
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xb5d9e201))

        data.write(b'tzy\xcb')  # 0x747a79cb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x747a79cb))

        data.write(b'\x18\x9dp\x17')  # 0x189d7017
        data.write(b'\x00\x04')  # size
        self.unknown_0x189d7017.to_stream(data, game)

        data.write(b'\xa0e\xb7\x0c')  # 0xa065b70c
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xa065b70c))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayer_AimStuffJson", data)
        return cls(
            aim_min_time=json_data['aim_min_time'],
            aim_max_time=json_data['aim_max_time'],
            aim_max_distance=json_data['aim_max_distance'],
            aim_max_angle_left=json_data['aim_max_angle_left'],
            aim_max_angle_right=json_data['aim_max_angle_right'],
            aim_max_angle_up=json_data['aim_max_angle_up'],
            aim_max_angle_down=json_data['aim_max_angle_down'],
            aim_angle_per_second=json_data['aim_angle_per_second'],
            aim_threshold_distance=json_data['aim_threshold_distance'],
            aim_turn_angle_per_second=json_data['aim_turn_angle_per_second'],
            aim_new_target_radius=json_data['aim_new_target_radius'],
            aim_box_width=json_data['aim_box_width'],
            aim_box_height=json_data['aim_box_height'],
            aim_target_timer=json_data['aim_target_timer'],
            aim_assist_horizontal_angle=json_data['aim_assist_horizontal_angle'],
            aim_assist_vertical_angle=json_data['aim_assist_vertical_angle'],
            rev_free_look_gun=json_data['rev_free_look_gun'],
            rev_orbit_lock_gun=json_data['rev_orbit_lock_gun'],
            rev_orbit_tag_objects=json_data['rev_orbit_tag_objects'],
            rev_lock_cursor=json_data['rev_lock_cursor'],
            rev_view_lock_disables_turn=json_data['rev_view_lock_disables_turn'],
            rev_view_lock_type=enums.RevViewLockTypeEnum.from_json(json_data['rev_view_lock_type']),
            rev_free_look_velocity=json_data['rev_free_look_velocity'],
            rev_free_look_velocity_per_second=json_data['rev_free_look_velocity_per_second'],
            unknown_0x21047226=json_data['unknown_0x21047226'],
            unknown_0x95f112be=json_data['unknown_0x95f112be'],
            unknown_0xb5d9e201=json_data['unknown_0xb5d9e201'],
            unknown_0x747a79cb=json_data['unknown_0x747a79cb'],
            unknown_0x189d7017=enums.TweakPlayer_AimStuff_UnknownEnum2Enum.from_json(json_data['unknown_0x189d7017']),
            unknown_0xa065b70c=json_data['unknown_0xa065b70c'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'aim_min_time': self.aim_min_time,
            'aim_max_time': self.aim_max_time,
            'aim_max_distance': self.aim_max_distance,
            'aim_max_angle_left': self.aim_max_angle_left,
            'aim_max_angle_right': self.aim_max_angle_right,
            'aim_max_angle_up': self.aim_max_angle_up,
            'aim_max_angle_down': self.aim_max_angle_down,
            'aim_angle_per_second': self.aim_angle_per_second,
            'aim_threshold_distance': self.aim_threshold_distance,
            'aim_turn_angle_per_second': self.aim_turn_angle_per_second,
            'aim_new_target_radius': self.aim_new_target_radius,
            'aim_box_width': self.aim_box_width,
            'aim_box_height': self.aim_box_height,
            'aim_target_timer': self.aim_target_timer,
            'aim_assist_horizontal_angle': self.aim_assist_horizontal_angle,
            'aim_assist_vertical_angle': self.aim_assist_vertical_angle,
            'rev_free_look_gun': self.rev_free_look_gun,
            'rev_orbit_lock_gun': self.rev_orbit_lock_gun,
            'rev_orbit_tag_objects': self.rev_orbit_tag_objects,
            'rev_lock_cursor': self.rev_lock_cursor,
            'rev_view_lock_disables_turn': self.rev_view_lock_disables_turn,
            'rev_view_lock_type': self.rev_view_lock_type.to_json(),
            'rev_free_look_velocity': self.rev_free_look_velocity,
            'rev_free_look_velocity_per_second': self.rev_free_look_velocity_per_second,
            'unknown_0x21047226': self.unknown_0x21047226,
            'unknown_0x95f112be': self.unknown_0x95f112be,
            'unknown_0xb5d9e201': self.unknown_0xb5d9e201,
            'unknown_0x747a79cb': self.unknown_0x747a79cb,
            'unknown_0x189d7017': self.unknown_0x189d7017.to_json(),
            'unknown_0xa065b70c': self.unknown_0xa065b70c,
        }


def _decode_rev_view_lock_type(data: typing.BinaryIO, game: Game, property_size: int) -> enums.RevViewLockTypeEnum:
    return enums.RevViewLockTypeEnum.from_stream(data, game)


def _decode_unknown_0x189d7017(data: typing.BinaryIO, game: Game, property_size: int) -> enums.TweakPlayer_AimStuff_UnknownEnum2Enum:
    return enums.TweakPlayer_AimStuff_UnknownEnum2Enum.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x27c60d0a: ('aim_min_time', structs.decode_BIG_f),
    0xb7b51de0: ('aim_max_time', structs.decode_BIG_f),
    0xf77d0359: ('aim_max_distance', structs.decode_BIG_f),
    0xde887cca: ('aim_max_angle_left', structs.decode_BIG_f),
    0xb4b07d5d: ('aim_max_angle_right', structs.decode_BIG_f),
    0xe5f8c567: ('aim_max_angle_up', structs.decode_BIG_f),
    0x9774749d: ('aim_max_angle_down', structs.decode_BIG_f),
    0x133f3002: ('aim_angle_per_second', structs.decode_BIG_f),
    0x96fab602: ('aim_threshold_distance', structs.decode_BIG_f),
    0x94164a2f: ('aim_turn_angle_per_second', structs.decode_BIG_f),
    0x54354c80: ('aim_new_target_radius', structs.decode_BIG_f),
    0x5361ce18: ('aim_box_width', structs.decode_BIG_f),
    0x4b2e9260: ('aim_box_height', structs.decode_BIG_f),
    0x3b9a3789: ('aim_target_timer', structs.decode_BIG_f),
    0x38dd0b85: ('aim_assist_horizontal_angle', structs.decode_BIG_f),
    0x1157883e: ('aim_assist_vertical_angle', structs.decode_BIG_f),
    0x38ee6d6e: ('rev_free_look_gun', structs.decode_BIG_bool_),
    0x9e3aceb5: ('rev_orbit_lock_gun', structs.decode_BIG_bool_),
    0x228a8def: ('rev_orbit_tag_objects', structs.decode_BIG_bool_),
    0x534a7b3c: ('rev_lock_cursor', structs.decode_BIG_bool_),
    0xd2dfc16a: ('rev_view_lock_disables_turn', structs.decode_BIG_bool_),
    0x60f08beb: ('rev_view_lock_type', _decode_rev_view_lock_type),
    0xcca13e22: ('rev_free_look_velocity', structs.decode_BIG_bool_),
    0x85437c89: ('rev_free_look_velocity_per_second', structs.decode_BIG_f),
    0x21047226: ('unknown_0x21047226', structs.decode_BIG_bool_),
    0x95f112be: ('unknown_0x95f112be', structs.decode_BIG_f),
    0xb5d9e201: ('unknown_0xb5d9e201', structs.decode_BIG_bool_),
    0x747a79cb: ('unknown_0x747a79cb', structs.decode_BIG_f),
    0x189d7017: ('unknown_0x189d7017', _decode_unknown_0x189d7017),
    0xa065b70c: ('unknown_0xa065b70c', structs.decode_BIG_bool_),
}
