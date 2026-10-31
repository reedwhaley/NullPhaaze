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
from retro_data_structures.properties.corruption.archetypes.FrameObjectsOrientation import FrameObjectsOrientation
from retro_data_structures.properties.corruption.archetypes.OffsetSplines import OffsetSplines
from retro_data_structures.properties.corruption.archetypes.PathDetermination import PathDetermination
from retro_data_structures.properties.corruption.archetypes.SpindleOrientation import SpindleOrientation
from retro_data_structures.properties.corruption.archetypes.SurfaceOrientation import SurfaceOrientation
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    class CameraOrientationJson(typing_extensions.TypedDict):
        orientation_type: int
        flags: int
        look_at_type: int
        locator_name: str
        pitch_angle: float
        target_path_determination: json_util.JsonObject
        distance: float
        distance_direction_method: int
        look_at_motion: json_util.JsonObject
        look_at_offset: json_util.JsonObject
        target_control_spline: json_util.JsonObject
        spindle_orientation: json_util.JsonObject
        surface_orientation: json_util.JsonObject
        frame_objects_orientation: json_util.JsonObject
    

class LookAtType(enum.IntEnum):
    kLAT_LookAtPosition = 869408558
    kLAT_OrbitPosition = 3208351709
    kLAT_AimPosition = 3923417272
    kLAT_RenderBoundsCentre = 1224849172
    kLAT_Origin = 3331078636
    kLAT_Locator = 4226777021

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


class DistanceDirectionMethod(enum.IntEnum):
    kDDM_Start = 1531303199
    kDDM_End = 3341593124
    kDDM_Closest = 4205502699
    kDDM_Farthest = 3784644380

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
class CameraOrientation(BaseProperty):
    orientation_type: int = dataclasses.field(default=1973921119, metadata={
        'reflection': FieldReflection[int](
            int, id=0x5c72a964, original_name='OrientationType'
        ),
    })  # Choice
    flags: int = dataclasses.field(default=8, metadata={
        'reflection': FieldReflection[int](
            int, id=0x6219022e, original_name='Flags'
        ),
    })  # Flagset
    look_at_type: LookAtType = dataclasses.field(default=LookAtType.kLAT_LookAtPosition, metadata={
        'reflection': FieldReflection[LookAtType](
            LookAtType, id=0x44191fb8, original_name='LookAtType', from_json=LookAtType.from_json, to_json=LookAtType.to_json
        ),
    })
    locator_name: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xfbc6c110, original_name='LocatorName'
        ),
    })
    pitch_angle: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6ff7392e, original_name='PitchAngle'
        ),
    })
    target_path_determination: PathDetermination = dataclasses.field(default_factory=PathDetermination, metadata={
        'reflection': FieldReflection[PathDetermination](
            PathDetermination, id=0x32468c89, original_name='TargetPathDetermination', from_json=PathDetermination.from_json, to_json=PathDetermination.to_json
        ),
    })
    distance: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc3bf43be, original_name='Distance'
        ),
    })
    distance_direction_method: DistanceDirectionMethod = dataclasses.field(default=DistanceDirectionMethod.kDDM_Start, metadata={
        'reflection': FieldReflection[DistanceDirectionMethod](
            DistanceDirectionMethod, id=0x10e7121b, original_name='DistanceDirectionMethod', from_json=DistanceDirectionMethod.from_json, to_json=DistanceDirectionMethod.to_json
        ),
    })
    look_at_motion: Convergence = dataclasses.field(default_factory=Convergence, metadata={
        'reflection': FieldReflection[Convergence](
            Convergence, id=0xda54b3e9, original_name='LookAtMotion', from_json=Convergence.from_json, to_json=Convergence.to_json
        ),
    })
    look_at_offset: OffsetSplines = dataclasses.field(default_factory=OffsetSplines, metadata={
        'reflection': FieldReflection[OffsetSplines](
            OffsetSplines, id=0x091f2936, original_name='LookAtOffset', from_json=OffsetSplines.from_json, to_json=OffsetSplines.to_json
        ),
    })
    target_control_spline: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xc4dfbfa7, original_name='TargetControlSpline', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    spindle_orientation: SpindleOrientation = dataclasses.field(default_factory=SpindleOrientation, metadata={
        'reflection': FieldReflection[SpindleOrientation](
            SpindleOrientation, id=0x86bc03d3, original_name='SpindleOrientation', from_json=SpindleOrientation.from_json, to_json=SpindleOrientation.to_json
        ),
    })
    surface_orientation: SurfaceOrientation = dataclasses.field(default_factory=SurfaceOrientation, metadata={
        'reflection': FieldReflection[SurfaceOrientation](
            SurfaceOrientation, id=0xe1deee27, original_name='SurfaceOrientation', from_json=SurfaceOrientation.from_json, to_json=SurfaceOrientation.to_json
        ),
    })
    frame_objects_orientation: FrameObjectsOrientation = dataclasses.field(default_factory=FrameObjectsOrientation, metadata={
        'reflection': FieldReflection[FrameObjectsOrientation](
            FrameObjectsOrientation, id=0xf6bb44ea, original_name='FrameObjectsOrientation', from_json=FrameObjectsOrientation.from_json, to_json=FrameObjectsOrientation.to_json
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
        if property_count != 14:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5c72a964
        orientation_type = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6219022e
        flags = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x44191fb8
        look_at_type = LookAtType.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfbc6c110
        locator_name = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6ff7392e
        pitch_angle = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32468c89
        target_path_determination = PathDetermination.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc3bf43be
        distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x10e7121b
        distance_direction_method = DistanceDirectionMethod.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xda54b3e9
        look_at_motion = Convergence.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x091f2936
        look_at_offset = OffsetSplines.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc4dfbfa7
        target_control_spline = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x86bc03d3
        spindle_orientation = SpindleOrientation.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe1deee27
        surface_orientation = SurfaceOrientation.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf6bb44ea
        frame_objects_orientation = FrameObjectsOrientation.from_stream(data, game, property_size)
    
        return cls(orientation_type, flags, look_at_type, locator_name, pitch_angle, target_path_determination, distance, distance_direction_method, look_at_motion, look_at_offset, target_control_spline, spindle_orientation, surface_orientation, frame_objects_orientation)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x0e')  # 14 properties

        data.write(b'\\r\xa9d')  # 0x5c72a964
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.orientation_type))

        data.write(b'b\x19\x02.')  # 0x6219022e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.flags))

        data.write(b'D\x19\x1f\xb8')  # 0x44191fb8
        data.write(b'\x00\x04')  # size
        self.look_at_type.to_stream(data, game)

        data.write(b'\xfb\xc6\xc1\x10')  # 0xfbc6c110
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.locator_name.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'o\xf79.')  # 0x6ff7392e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.pitch_angle))

        data.write(b'2F\x8c\x89')  # 0x32468c89
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.target_path_determination.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc3\xbfC\xbe')  # 0xc3bf43be
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.distance))

        data.write(b'\x10\xe7\x12\x1b')  # 0x10e7121b
        data.write(b'\x00\x04')  # size
        self.distance_direction_method.to_stream(data, game)

        data.write(b'\xdaT\xb3\xe9')  # 0xda54b3e9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.look_at_motion.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\t\x1f)6')  # 0x91f2936
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.look_at_offset.to_stream(data, game)
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

        data.write(b'\x86\xbc\x03\xd3')  # 0x86bc03d3
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.spindle_orientation.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xe1\xde\xee'")  # 0xe1deee27
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.surface_orientation.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf6\xbbD\xea')  # 0xf6bb44ea
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.frame_objects_orientation.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CameraOrientationJson", data)
        return cls(
            orientation_type=json_data['orientation_type'],
            flags=json_data['flags'],
            look_at_type=LookAtType.from_json(json_data['look_at_type']),
            locator_name=json_data['locator_name'],
            pitch_angle=json_data['pitch_angle'],
            target_path_determination=PathDetermination.from_json(json_data['target_path_determination']),
            distance=json_data['distance'],
            distance_direction_method=DistanceDirectionMethod.from_json(json_data['distance_direction_method']),
            look_at_motion=Convergence.from_json(json_data['look_at_motion']),
            look_at_offset=OffsetSplines.from_json(json_data['look_at_offset']),
            target_control_spline=Spline.from_json(json_data['target_control_spline']),
            spindle_orientation=SpindleOrientation.from_json(json_data['spindle_orientation']),
            surface_orientation=SurfaceOrientation.from_json(json_data['surface_orientation']),
            frame_objects_orientation=FrameObjectsOrientation.from_json(json_data['frame_objects_orientation']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'orientation_type': self.orientation_type,
            'flags': self.flags,
            'look_at_type': self.look_at_type.to_json(),
            'locator_name': self.locator_name,
            'pitch_angle': self.pitch_angle,
            'target_path_determination': self.target_path_determination.to_json(),
            'distance': self.distance,
            'distance_direction_method': self.distance_direction_method.to_json(),
            'look_at_motion': self.look_at_motion.to_json(),
            'look_at_offset': self.look_at_offset.to_json(),
            'target_control_spline': self.target_control_spline.to_json(),
            'spindle_orientation': self.spindle_orientation.to_json(),
            'surface_orientation': self.surface_orientation.to_json(),
            'frame_objects_orientation': self.frame_objects_orientation.to_json(),
        }


def _decode_look_at_type(data: typing.BinaryIO, game: Game, property_size: int) -> LookAtType:
    return LookAtType.from_stream(data, game)


def _decode_locator_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_target_path_determination(data: typing.BinaryIO, game: Game, property_size: int) -> PathDetermination:
    return PathDetermination.from_stream(data, game, property_size)


def _decode_distance_direction_method(data: typing.BinaryIO, game: Game, property_size: int) -> DistanceDirectionMethod:
    return DistanceDirectionMethod.from_stream(data, game)


def _decode_look_at_motion(data: typing.BinaryIO, game: Game, property_size: int) -> Convergence:
    return Convergence.from_stream(data, game, property_size)


def _decode_look_at_offset(data: typing.BinaryIO, game: Game, property_size: int) -> OffsetSplines:
    return OffsetSplines.from_stream(data, game, property_size)


def _decode_target_control_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_spindle_orientation(data: typing.BinaryIO, game: Game, property_size: int) -> SpindleOrientation:
    return SpindleOrientation.from_stream(data, game, property_size)


def _decode_surface_orientation(data: typing.BinaryIO, game: Game, property_size: int) -> SurfaceOrientation:
    return SurfaceOrientation.from_stream(data, game, property_size)


def _decode_frame_objects_orientation(data: typing.BinaryIO, game: Game, property_size: int) -> FrameObjectsOrientation:
    return FrameObjectsOrientation.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x5c72a964: ('orientation_type', structs.decode_BIG_L),
    0x6219022e: ('flags', structs.decode_BIG_L),
    0x44191fb8: ('look_at_type', _decode_look_at_type),
    0xfbc6c110: ('locator_name', _decode_locator_name),
    0x6ff7392e: ('pitch_angle', structs.decode_BIG_f),
    0x32468c89: ('target_path_determination', _decode_target_path_determination),
    0xc3bf43be: ('distance', structs.decode_BIG_f),
    0x10e7121b: ('distance_direction_method', _decode_distance_direction_method),
    0xda54b3e9: ('look_at_motion', _decode_look_at_motion),
    0x091f2936: ('look_at_offset', _decode_look_at_offset),
    0xc4dfbfa7: ('target_control_spline', _decode_target_control_spline),
    0x86bc03d3: ('spindle_orientation', _decode_spindle_orientation),
    0xe1deee27: ('surface_orientation', _decode_surface_orientation),
    0xf6bb44ea: ('frame_objects_orientation', _decode_frame_objects_orientation),
}
