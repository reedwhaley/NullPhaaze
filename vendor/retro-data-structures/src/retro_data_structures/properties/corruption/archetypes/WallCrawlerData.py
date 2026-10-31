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

if typing.TYPE_CHECKING:
    class WallCrawlerDataJson(typing_extensions.TypedDict):
        collision_radius: float
        stick_radius: float
        floor_turn_speed: float
        waypoint_approach_distance: float
        visible_distance: float
        projectile_bounds_multiplier: float
        floor_snap_lerp_factor: float
        unknown_0x1431157a: float
        unknown_0x2d5bfae8: float
        unknown_0x79e70805: float
        unknown_0xed8c4058: float
        is_paused: bool
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x8a6ab139, 0x5a3a30f4, 0x8e4f7b29, 0x733bd27c, 0xa72530e8, 0x742eab20, 0x519c7197, 0x1431157a, 0x2d5bfae8, 0x79e70805, 0xed8c4058, 0xc5526004)


@dataclasses.dataclass()
class WallCrawlerData(BaseProperty):
    collision_radius: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8a6ab139, original_name='CollisionRadius'
        ),
    })
    stick_radius: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5a3a30f4, original_name='StickRadius'
        ),
    })
    floor_turn_speed: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8e4f7b29, original_name='FloorTurnSpeed'
        ),
    })
    waypoint_approach_distance: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x733bd27c, original_name='WaypointApproachDistance'
        ),
    })
    visible_distance: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa72530e8, original_name='VisibleDistance'
        ),
    })
    projectile_bounds_multiplier: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x742eab20, original_name='ProjectileBoundsMultiplier'
        ),
    })
    floor_snap_lerp_factor: float = dataclasses.field(default=0.16699999570846558, metadata={
        'reflection': FieldReflection[float](
            float, id=0x519c7197, original_name='FloorSnapLerpFactor'
        ),
    })
    unknown_0x1431157a: float = dataclasses.field(default=0.6000000238418579, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1431157a, original_name='Unknown'
        ),
    })
    unknown_0x2d5bfae8: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2d5bfae8, original_name='Unknown'
        ),
    })
    unknown_0x79e70805: float = dataclasses.field(default=0.6000000238418579, metadata={
        'reflection': FieldReflection[float](
            float, id=0x79e70805, original_name='Unknown'
        ),
    })
    unknown_0xed8c4058: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xed8c4058, original_name='Unknown'
        ),
    })
    is_paused: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xc5526004, original_name='IsPaused'
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
        if property_count != 12:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLH?')
    
        dec = _FAST_FORMAT.unpack(data.read(117))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24], dec[27], dec[30], dec[33]) == _FAST_IDS
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
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x0c')  # 12 properties

        data.write(b'\x8aj\xb19')  # 0x8a6ab139
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.collision_radius))

        data.write(b'Z:0\xf4')  # 0x5a3a30f4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stick_radius))

        data.write(b'\x8eO{)')  # 0x8e4f7b29
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.floor_turn_speed))

        data.write(b's;\xd2|')  # 0x733bd27c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.waypoint_approach_distance))

        data.write(b'\xa7%0\xe8')  # 0xa72530e8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.visible_distance))

        data.write(b't.\xab ')  # 0x742eab20
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.projectile_bounds_multiplier))

        data.write(b'Q\x9cq\x97')  # 0x519c7197
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.floor_snap_lerp_factor))

        data.write(b'\x141\x15z')  # 0x1431157a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1431157a))

        data.write(b'-[\xfa\xe8')  # 0x2d5bfae8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2d5bfae8))

        data.write(b'y\xe7\x08\x05')  # 0x79e70805
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x79e70805))

        data.write(b'\xed\x8c@X')  # 0xed8c4058
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xed8c4058))

        data.write(b'\xc5R`\x04')  # 0xc5526004
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_paused))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("WallCrawlerDataJson", data)
        return cls(
            collision_radius=json_data['collision_radius'],
            stick_radius=json_data['stick_radius'],
            floor_turn_speed=json_data['floor_turn_speed'],
            waypoint_approach_distance=json_data['waypoint_approach_distance'],
            visible_distance=json_data['visible_distance'],
            projectile_bounds_multiplier=json_data['projectile_bounds_multiplier'],
            floor_snap_lerp_factor=json_data['floor_snap_lerp_factor'],
            unknown_0x1431157a=json_data['unknown_0x1431157a'],
            unknown_0x2d5bfae8=json_data['unknown_0x2d5bfae8'],
            unknown_0x79e70805=json_data['unknown_0x79e70805'],
            unknown_0xed8c4058=json_data['unknown_0xed8c4058'],
            is_paused=json_data['is_paused'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'collision_radius': self.collision_radius,
            'stick_radius': self.stick_radius,
            'floor_turn_speed': self.floor_turn_speed,
            'waypoint_approach_distance': self.waypoint_approach_distance,
            'visible_distance': self.visible_distance,
            'projectile_bounds_multiplier': self.projectile_bounds_multiplier,
            'floor_snap_lerp_factor': self.floor_snap_lerp_factor,
            'unknown_0x1431157a': self.unknown_0x1431157a,
            'unknown_0x2d5bfae8': self.unknown_0x2d5bfae8,
            'unknown_0x79e70805': self.unknown_0x79e70805,
            'unknown_0xed8c4058': self.unknown_0xed8c4058,
            'is_paused': self.is_paused,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x8a6ab139: ('collision_radius', structs.decode_BIG_f),
    0x5a3a30f4: ('stick_radius', structs.decode_BIG_f),
    0x8e4f7b29: ('floor_turn_speed', structs.decode_BIG_f),
    0x733bd27c: ('waypoint_approach_distance', structs.decode_BIG_f),
    0xa72530e8: ('visible_distance', structs.decode_BIG_f),
    0x742eab20: ('projectile_bounds_multiplier', structs.decode_BIG_f),
    0x519c7197: ('floor_snap_lerp_factor', structs.decode_BIG_f),
    0x1431157a: ('unknown_0x1431157a', structs.decode_BIG_f),
    0x2d5bfae8: ('unknown_0x2d5bfae8', structs.decode_BIG_f),
    0x79e70805: ('unknown_0x79e70805', structs.decode_BIG_f),
    0xed8c4058: ('unknown_0xed8c4058', structs.decode_BIG_f),
    0xc5526004: ('is_paused', structs.decode_BIG_bool_),
}
