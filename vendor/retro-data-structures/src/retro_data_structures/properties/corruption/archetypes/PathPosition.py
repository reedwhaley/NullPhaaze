# Generated File
from __future__ import annotations

import dataclasses
import enum
import struct
import typing
import typing_extensions

from retro_data_structures import json_util
from retro_data_structures.game_check import Game
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.corruption.archetypes.Convergence import Convergence
from retro_data_structures.properties.corruption.archetypes.PathDetermination import PathDetermination
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    class PathPositionJson(typing_extensions.TypedDict):
        flags: int
        initial_position: int
        path_position_determination: json_util.JsonObject
        distance: float
        dampen_distance: float
        desired_position_motion: json_util.JsonObject
        motion_control_spline: json_util.JsonObject
        perpendicular_distance_control_spline: json_util.JsonObject
    

class InitialPosition(enum.IntEnum):
    kIP_Game = 3529489810
    kIP_Start = 3079009261
    kIP_End = 2952273734
    kIP_Closest = 237832937
    kIP_GameViewAngle = 635227635

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


@dataclasses.dataclass()
class PathPosition(BaseProperty):
    flags: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x259d3279, original_name='Flags'
        ),
    })  # Flagset
    initial_position: InitialPosition = dataclasses.field(default=InitialPosition.kIP_Game, metadata={
        'reflection': FieldReflection[InitialPosition](
            InitialPosition, id=0x340e4ca3, original_name='InitialPosition', from_json=InitialPosition.from_json, to_json=InitialPosition.to_json
        ),
    })
    path_position_determination: PathDetermination = dataclasses.field(default_factory=PathDetermination, metadata={
        'reflection': FieldReflection[PathDetermination](
            PathDetermination, id=0x0aed5c7d, original_name='PathPositionDetermination', from_json=PathDetermination.from_json, to_json=PathDetermination.to_json
        ),
    })
    distance: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc3bf43be, original_name='Distance'
        ),
    })
    dampen_distance: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x32f835ec, original_name='DampenDistance'
        ),
    })
    desired_position_motion: Convergence = dataclasses.field(default_factory=Convergence, metadata={
        'reflection': FieldReflection[Convergence](
            Convergence, id=0x959108a5, original_name='DesiredPositionMotion', from_json=Convergence.from_json, to_json=Convergence.to_json
        ),
    })
    motion_control_spline: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x27e5f874, original_name='MotionControlSpline', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    perpendicular_distance_control_spline: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x12861f7d, original_name='PerpendicularDistanceControlSpline', from_json=Spline.from_json, to_json=Spline.to_json
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
        if property_count != 8:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x259d3279
        flags = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x340e4ca3
        initial_position = InitialPosition.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0aed5c7d
        path_position_determination = PathDetermination.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc3bf43be
        distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32f835ec
        dampen_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x959108a5
        desired_position_motion = Convergence.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x27e5f874
        motion_control_spline = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x12861f7d
        perpendicular_distance_control_spline = Spline.from_stream(data, game, property_size)
    
        return cls(flags, initial_position, path_position_determination, distance, dampen_distance, desired_position_motion, motion_control_spline, perpendicular_distance_control_spline)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x08')  # 8 properties

        data.write(b'%\x9d2y')  # 0x259d3279
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.flags))

        data.write(b'4\x0eL\xa3')  # 0x340e4ca3
        data.write(b'\x00\x04')  # size
        self.initial_position.to_stream(data, game)

        data.write(b'\n\xed\\}')  # 0xaed5c7d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.path_position_determination.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc3\xbfC\xbe')  # 0xc3bf43be
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.distance))

        data.write(b'2\xf85\xec')  # 0x32f835ec
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dampen_distance))

        data.write(b'\x95\x91\x08\xa5')  # 0x959108a5
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.desired_position_motion.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"'\xe5\xf8t")  # 0x27e5f874
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.motion_control_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x12\x86\x1f}')  # 0x12861f7d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.perpendicular_distance_control_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PathPositionJson", data)
        return cls(
            flags=json_data['flags'],
            initial_position=InitialPosition.from_json(json_data['initial_position']),
            path_position_determination=PathDetermination.from_json(json_data['path_position_determination']),
            distance=json_data['distance'],
            dampen_distance=json_data['dampen_distance'],
            desired_position_motion=Convergence.from_json(json_data['desired_position_motion']),
            motion_control_spline=Spline.from_json(json_data['motion_control_spline']),
            perpendicular_distance_control_spline=Spline.from_json(json_data['perpendicular_distance_control_spline']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'flags': self.flags,
            'initial_position': self.initial_position.to_json(),
            'path_position_determination': self.path_position_determination.to_json(),
            'distance': self.distance,
            'dampen_distance': self.dampen_distance,
            'desired_position_motion': self.desired_position_motion.to_json(),
            'motion_control_spline': self.motion_control_spline.to_json(),
            'perpendicular_distance_control_spline': self.perpendicular_distance_control_spline.to_json(),
        }


def _decode_initial_position(data: typing.BinaryIO, game: Game, property_size: int) -> InitialPosition:
    return InitialPosition.from_stream(data, game)


def _decode_path_position_determination(data: typing.BinaryIO, game: Game, property_size: int) -> PathDetermination:
    return PathDetermination.from_stream(data, game, property_size)


def _decode_desired_position_motion(data: typing.BinaryIO, game: Game, property_size: int) -> Convergence:
    return Convergence.from_stream(data, game, property_size)


def _decode_motion_control_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_perpendicular_distance_control_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x259d3279: ('flags', structs.decode_BIG_L),
    0x340e4ca3: ('initial_position', _decode_initial_position),
    0x0aed5c7d: ('path_position_determination', _decode_path_position_determination),
    0xc3bf43be: ('distance', structs.decode_BIG_f),
    0x32f835ec: ('dampen_distance', structs.decode_BIG_f),
    0x959108a5: ('desired_position_motion', _decode_desired_position_motion),
    0x27e5f874: ('motion_control_spline', _decode_motion_control_spline),
    0x12861f7d: ('perpendicular_distance_control_spline', _decode_perpendicular_distance_control_spline),
}
