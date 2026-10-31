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
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
import retro_data_structures.enums.echoes as enums
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.common.archetypes.SplineType import SplineType
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class PathCameraJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        flags: int
        spline_flags: int
        motion_spline_type: json_util.JsonObject
        motion_control_spline: json_util.JsonObject
        target_spline_type: json_util.JsonObject
        target_control_spline: json_util.JsonObject
        fov_spline: json_util.JsonObject
        speed_control_spline: json_util.JsonObject
        player_spline_type: json_util.JsonObject
        player_spline_loops: bool
        distance: float
        speed: float
        dampen_distance: float
        initial_position: int
        angular_speed: float
        perpendicular_distance_control_spline: json_util.JsonObject
        perpendicular_interp_control_spline: json_util.JsonObject
    

class PathCameraFlags(enum.IntFlag):
    NoDampening = 1
    Unknown2 = 2
    PerpendicularDistanceControl = 4
    LookAtHintHeight = 8
    AvoidDoorCollisions = 16
    BallCameraLookAt = 32
    LookAtPathHeight = 64
    PerpendicularLookInterpolation = 128

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
class PathCamera(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    flags: PathCameraFlags = dataclasses.field(default=PathCameraFlags(32), metadata={
        'reflection': FieldReflection[PathCameraFlags](
            PathCameraFlags, id=0x5cbd5bae, original_name='Flags', from_json=PathCameraFlags.from_json, to_json=PathCameraFlags.to_json
        ),
    })
    spline_flags: enums.CameraSplineFlags = dataclasses.field(default=enums.CameraSplineFlags(0), metadata={
        'reflection': FieldReflection[enums.CameraSplineFlags](
            enums.CameraSplineFlags, id=0xd4b29446, original_name='SplineFlags', from_json=enums.CameraSplineFlags.from_json, to_json=enums.CameraSplineFlags.to_json
        ),
    })
    motion_spline_type: SplineType = dataclasses.field(default_factory=SplineType, metadata={
        'reflection': FieldReflection[SplineType](
            SplineType, id=0x493d6a2d, original_name='MotionSplineType', from_json=SplineType.from_json, to_json=SplineType.to_json
        ),
    })
    motion_control_spline: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x27e5f874, original_name='MotionControlSpline', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    target_spline_type: SplineType = dataclasses.field(default_factory=SplineType, metadata={
        'reflection': FieldReflection[SplineType](
            SplineType, id=0x5604d304, original_name='TargetSplineType', from_json=SplineType.from_json, to_json=SplineType.to_json
        ),
    })
    target_control_spline: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xc4dfbfa7, original_name='TargetControlSpline', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    fov_spline: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x6868d4b3, original_name='FOVSpline', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    speed_control_spline: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xedd07160, original_name='SpeedControlSpline', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    player_spline_type: SplineType = dataclasses.field(default_factory=SplineType, metadata={
        'reflection': FieldReflection[SplineType](
            SplineType, id=0x33e4685b, original_name='PlayerSplineType', from_json=SplineType.from_json, to_json=SplineType.to_json
        ),
    })
    player_spline_loops: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x431769c6, original_name='PlayerSplineLoops'
        ),
    })
    distance: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc3bf43be, original_name='Distance'
        ),
    })
    speed: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6392404e, original_name='Speed'
        ),
    })
    dampen_distance: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x32f835ec, original_name='DampenDistance'
        ),
    })
    initial_position: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xe8fc72b6, original_name='InitialPosition'
        ),
    })  # Choice
    angular_speed: float = dataclasses.field(default=120.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbcd7333f, original_name='AngularSpeed'
        ),
    })
    perpendicular_distance_control_spline: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x12861f7d, original_name='PerpendicularDistanceControlSpline', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    perpendicular_interp_control_spline: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x96ac52b0, original_name='PerpendicularInterpControlSpline', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'PCAM'

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None) -> typing_extensions.Self:
        struct_id, size, property_count = structs.BIG_LHH.unpack(data.read(8))
        assert struct_id == 0xFFFFFFFF
        root_size_start = data.tell() - 2

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

        assert data.tell() - root_size_start == size
        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 18:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5cbd5bae
        flags = PathCameraFlags.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd4b29446
        spline_flags = enums.CameraSplineFlags.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x493d6a2d
        motion_spline_type = SplineType.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x27e5f874
        motion_control_spline = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5604d304
        target_spline_type = SplineType.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc4dfbfa7
        target_control_spline = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6868d4b3
        fov_spline = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xedd07160
        speed_control_spline = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33e4685b
        player_spline_type = SplineType.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x431769c6
        player_spline_loops = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc3bf43be
        distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6392404e
        speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32f835ec
        dampen_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe8fc72b6
        initial_position = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbcd7333f
        angular_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x12861f7d
        perpendicular_distance_control_spline = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x96ac52b0
        perpendicular_interp_control_spline = Spline.from_stream(data, game, property_size)
    
        return cls(editor_properties, flags, spline_flags, motion_spline_type, motion_control_spline, target_spline_type, target_control_spline, fov_spline, speed_control_spline, player_spline_type, player_spline_loops, distance, speed, dampen_distance, initial_position, angular_speed, perpendicular_distance_control_spline, perpendicular_interp_control_spline)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x12')  # 18 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\\\xbd[\xae')  # 0x5cbd5bae
        data.write(b'\x00\x04')  # size
        self.flags.to_stream(data, game)

        data.write(b'\xd4\xb2\x94F')  # 0xd4b29446
        data.write(b'\x00\x04')  # size
        self.spline_flags.to_stream(data, game)

        data.write(b'I=j-')  # 0x493d6a2d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.motion_spline_type.to_stream(data, game)
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

        data.write(b'V\x04\xd3\x04')  # 0x5604d304
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.target_spline_type.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc4\xdf\xbf\xa7')  # 0xc4dfbfa7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.target_control_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'hh\xd4\xb3')  # 0x6868d4b3
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.fov_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xed\xd0q`')  # 0xedd07160
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.speed_control_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'3\xe4h[')  # 0x33e4685b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.player_spline_type.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'C\x17i\xc6')  # 0x431769c6
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.player_spline_loops))

        data.write(b'\xc3\xbfC\xbe')  # 0xc3bf43be
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.distance))

        data.write(b'c\x92@N')  # 0x6392404e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.speed))

        data.write(b'2\xf85\xec')  # 0x32f835ec
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dampen_distance))

        data.write(b'\xe8\xfcr\xb6')  # 0xe8fc72b6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.initial_position))

        data.write(b'\xbc\xd73?')  # 0xbcd7333f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.angular_speed))

        data.write(b'\x12\x86\x1f}')  # 0x12861f7d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.perpendicular_distance_control_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x96\xacR\xb0')  # 0x96ac52b0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.perpendicular_interp_control_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PathCameraJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            flags=PathCameraFlags.from_json(json_data['flags']),
            spline_flags=enums.CameraSplineFlags.from_json(json_data['spline_flags']),
            motion_spline_type=SplineType.from_json(json_data['motion_spline_type']),
            motion_control_spline=Spline.from_json(json_data['motion_control_spline']),
            target_spline_type=SplineType.from_json(json_data['target_spline_type']),
            target_control_spline=Spline.from_json(json_data['target_control_spline']),
            fov_spline=Spline.from_json(json_data['fov_spline']),
            speed_control_spline=Spline.from_json(json_data['speed_control_spline']),
            player_spline_type=SplineType.from_json(json_data['player_spline_type']),
            player_spline_loops=json_data['player_spline_loops'],
            distance=json_data['distance'],
            speed=json_data['speed'],
            dampen_distance=json_data['dampen_distance'],
            initial_position=json_data['initial_position'],
            angular_speed=json_data['angular_speed'],
            perpendicular_distance_control_spline=Spline.from_json(json_data['perpendicular_distance_control_spline']),
            perpendicular_interp_control_spline=Spline.from_json(json_data['perpendicular_interp_control_spline']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'flags': self.flags.to_json(),
            'spline_flags': self.spline_flags.to_json(),
            'motion_spline_type': self.motion_spline_type.to_json(),
            'motion_control_spline': self.motion_control_spline.to_json(),
            'target_spline_type': self.target_spline_type.to_json(),
            'target_control_spline': self.target_control_spline.to_json(),
            'fov_spline': self.fov_spline.to_json(),
            'speed_control_spline': self.speed_control_spline.to_json(),
            'player_spline_type': self.player_spline_type.to_json(),
            'player_spline_loops': self.player_spline_loops,
            'distance': self.distance,
            'speed': self.speed,
            'dampen_distance': self.dampen_distance,
            'initial_position': self.initial_position,
            'angular_speed': self.angular_speed,
            'perpendicular_distance_control_spline': self.perpendicular_distance_control_spline.to_json(),
            'perpendicular_interp_control_spline': self.perpendicular_interp_control_spline.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_flags(data: typing.BinaryIO, game: Game, property_size: int) -> PathCameraFlags:
    return PathCameraFlags.from_stream(data, game)


def _decode_spline_flags(data: typing.BinaryIO, game: Game, property_size: int) -> enums.CameraSplineFlags:
    return enums.CameraSplineFlags.from_stream(data, game)


def _decode_motion_spline_type(data: typing.BinaryIO, game: Game, property_size: int) -> SplineType:
    return SplineType.from_stream(data, game, property_size)


def _decode_motion_control_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_target_spline_type(data: typing.BinaryIO, game: Game, property_size: int) -> SplineType:
    return SplineType.from_stream(data, game, property_size)


def _decode_target_control_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_fov_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_speed_control_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_player_spline_type(data: typing.BinaryIO, game: Game, property_size: int) -> SplineType:
    return SplineType.from_stream(data, game, property_size)


def _decode_perpendicular_distance_control_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_perpendicular_interp_control_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0x5cbd5bae: ('flags', _decode_flags),
    0xd4b29446: ('spline_flags', _decode_spline_flags),
    0x493d6a2d: ('motion_spline_type', _decode_motion_spline_type),
    0x27e5f874: ('motion_control_spline', _decode_motion_control_spline),
    0x5604d304: ('target_spline_type', _decode_target_spline_type),
    0xc4dfbfa7: ('target_control_spline', _decode_target_control_spline),
    0x6868d4b3: ('fov_spline', _decode_fov_spline),
    0xedd07160: ('speed_control_spline', _decode_speed_control_spline),
    0x33e4685b: ('player_spline_type', _decode_player_spline_type),
    0x431769c6: ('player_spline_loops', structs.decode_BIG_bool_),
    0xc3bf43be: ('distance', structs.decode_BIG_f),
    0x6392404e: ('speed', structs.decode_BIG_f),
    0x32f835ec: ('dampen_distance', structs.decode_BIG_f),
    0xe8fc72b6: ('initial_position', structs.decode_BIG_L),
    0xbcd7333f: ('angular_speed', structs.decode_BIG_f),
    0x12861f7d: ('perpendicular_distance_control_spline', _decode_perpendicular_distance_control_spline),
    0x96ac52b0: ('perpendicular_interp_control_spline', _decode_perpendicular_interp_control_spline),
}
