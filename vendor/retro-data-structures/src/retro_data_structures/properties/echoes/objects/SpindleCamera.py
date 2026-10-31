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
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.SpindleCameraInterpolant import SpindleCameraInterpolant
from retro_data_structures.properties.common.archetypes.SplineType import SplineType
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SpindleCameraJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        flags: int
        angular_speed: json_util.JsonObject
        linear_speed: json_util.JsonObject
        motion_radius: json_util.JsonObject
        radial_offset: json_util.JsonObject
        desired_angular_offset: json_util.JsonObject
        min_angular_offset: json_util.JsonObject
        max_angular_offset: json_util.JsonObject
        look_at_angular_offset: json_util.JsonObject
        look_at_z_offset: json_util.JsonObject
        z_offset: json_util.JsonObject
        angular_constraint: json_util.JsonObject
        angular_dampening: json_util.JsonObject
        desired_angular_speed: json_util.JsonObject
        deactivate_radius: json_util.JsonObject
        constraint_flip_angle: json_util.JsonObject
        fov: json_util.JsonObject
        target_spline_type: json_util.JsonObject
        target_spline_loops: bool
        target_control_spline: json_util.JsonObject
        player_spline_type: json_util.JsonObject
        player_spline_loops: bool
    

class SpindleCameraFlags(enum.IntFlag):
    ProjectLookAtOntoAxis = 1
    LookFromAxis = 2
    Unknown3 = 4
    InstantAzimuth = 8
    Unknown5 = 16
    ClampAzimuth = 32
    RadiusFromBall = 64
    FollowBallAlongAxis = 128
    NoLinearSpeedLimit = 256
    BallCameraLookAt = 512
    TrackBallAzimuth = 2048
    EaseLookAtAngularOffset = 4096
    DeactivateOutsideRadius = 8192
    FixedAzimuthSide = 16384
    LookAtBall = 32768
    FixedPosition = 65536

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
class SpindleCamera(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    flags: SpindleCameraFlags = dataclasses.field(default=SpindleCameraFlags(6400), metadata={
        'reflection': FieldReflection[SpindleCameraFlags](
            SpindleCameraFlags, id=0x3bf4eba8, original_name='Flags', from_json=SpindleCameraFlags.from_json, to_json=SpindleCameraFlags.to_json
        ),
    })
    angular_speed: SpindleCameraInterpolant = dataclasses.field(default_factory=SpindleCameraInterpolant, metadata={
        'reflection': FieldReflection[SpindleCameraInterpolant](
            SpindleCameraInterpolant, id=0xe56495fb, original_name='AngularSpeed', from_json=SpindleCameraInterpolant.from_json, to_json=SpindleCameraInterpolant.to_json
        ),
    })
    linear_speed: SpindleCameraInterpolant = dataclasses.field(default_factory=SpindleCameraInterpolant, metadata={
        'reflection': FieldReflection[SpindleCameraInterpolant](
            SpindleCameraInterpolant, id=0x239debfc, original_name='LinearSpeed', from_json=SpindleCameraInterpolant.from_json, to_json=SpindleCameraInterpolant.to_json
        ),
    })
    motion_radius: SpindleCameraInterpolant = dataclasses.field(default_factory=SpindleCameraInterpolant, metadata={
        'reflection': FieldReflection[SpindleCameraInterpolant](
            SpindleCameraInterpolant, id=0x27e8d703, original_name='MotionRadius', from_json=SpindleCameraInterpolant.from_json, to_json=SpindleCameraInterpolant.to_json
        ),
    })
    radial_offset: SpindleCameraInterpolant = dataclasses.field(default_factory=SpindleCameraInterpolant, metadata={
        'reflection': FieldReflection[SpindleCameraInterpolant](
            SpindleCameraInterpolant, id=0x2f914525, original_name='RadialOffset', from_json=SpindleCameraInterpolant.from_json, to_json=SpindleCameraInterpolant.to_json
        ),
    })
    desired_angular_offset: SpindleCameraInterpolant = dataclasses.field(default_factory=SpindleCameraInterpolant, metadata={
        'reflection': FieldReflection[SpindleCameraInterpolant](
            SpindleCameraInterpolant, id=0x23aa31b7, original_name='DesiredAngularOffset', from_json=SpindleCameraInterpolant.from_json, to_json=SpindleCameraInterpolant.to_json
        ),
    })
    min_angular_offset: SpindleCameraInterpolant = dataclasses.field(default_factory=SpindleCameraInterpolant, metadata={
        'reflection': FieldReflection[SpindleCameraInterpolant](
            SpindleCameraInterpolant, id=0xe9e388af, original_name='MinAngularOffset', from_json=SpindleCameraInterpolant.from_json, to_json=SpindleCameraInterpolant.to_json
        ),
    })
    max_angular_offset: SpindleCameraInterpolant = dataclasses.field(default_factory=SpindleCameraInterpolant, metadata={
        'reflection': FieldReflection[SpindleCameraInterpolant](
            SpindleCameraInterpolant, id=0xde5a2c87, original_name='MaxAngularOffset', from_json=SpindleCameraInterpolant.from_json, to_json=SpindleCameraInterpolant.to_json
        ),
    })
    look_at_angular_offset: SpindleCameraInterpolant = dataclasses.field(default_factory=SpindleCameraInterpolant, metadata={
        'reflection': FieldReflection[SpindleCameraInterpolant](
            SpindleCameraInterpolant, id=0x1b3b2394, original_name='LookAtAngularOffset', from_json=SpindleCameraInterpolant.from_json, to_json=SpindleCameraInterpolant.to_json
        ),
    })
    look_at_z_offset: SpindleCameraInterpolant = dataclasses.field(default_factory=SpindleCameraInterpolant, metadata={
        'reflection': FieldReflection[SpindleCameraInterpolant](
            SpindleCameraInterpolant, id=0xf5666b6e, original_name='LookAtZOffset', from_json=SpindleCameraInterpolant.from_json, to_json=SpindleCameraInterpolant.to_json
        ),
    })
    z_offset: SpindleCameraInterpolant = dataclasses.field(default_factory=SpindleCameraInterpolant, metadata={
        'reflection': FieldReflection[SpindleCameraInterpolant](
            SpindleCameraInterpolant, id=0x66c618aa, original_name='ZOffset', from_json=SpindleCameraInterpolant.from_json, to_json=SpindleCameraInterpolant.to_json
        ),
    })
    angular_constraint: SpindleCameraInterpolant = dataclasses.field(default_factory=SpindleCameraInterpolant, metadata={
        'reflection': FieldReflection[SpindleCameraInterpolant](
            SpindleCameraInterpolant, id=0xb36d0fb6, original_name='AngularConstraint', from_json=SpindleCameraInterpolant.from_json, to_json=SpindleCameraInterpolant.to_json
        ),
    })
    angular_dampening: SpindleCameraInterpolant = dataclasses.field(default_factory=SpindleCameraInterpolant, metadata={
        'reflection': FieldReflection[SpindleCameraInterpolant](
            SpindleCameraInterpolant, id=0xcbb013cb, original_name='AngularDampening', from_json=SpindleCameraInterpolant.from_json, to_json=SpindleCameraInterpolant.to_json
        ),
    })
    desired_angular_speed: SpindleCameraInterpolant = dataclasses.field(default_factory=SpindleCameraInterpolant, metadata={
        'reflection': FieldReflection[SpindleCameraInterpolant](
            SpindleCameraInterpolant, id=0x4abfb789, original_name='DesiredAngularSpeed', from_json=SpindleCameraInterpolant.from_json, to_json=SpindleCameraInterpolant.to_json
        ),
    })
    deactivate_radius: SpindleCameraInterpolant = dataclasses.field(default_factory=SpindleCameraInterpolant, metadata={
        'reflection': FieldReflection[SpindleCameraInterpolant](
            SpindleCameraInterpolant, id=0xfb6a407a, original_name='DeactivateRadius', from_json=SpindleCameraInterpolant.from_json, to_json=SpindleCameraInterpolant.to_json
        ),
    })
    constraint_flip_angle: SpindleCameraInterpolant = dataclasses.field(default_factory=SpindleCameraInterpolant, metadata={
        'reflection': FieldReflection[SpindleCameraInterpolant](
            SpindleCameraInterpolant, id=0x3ae66f80, original_name='ConstraintFlipAngle', from_json=SpindleCameraInterpolant.from_json, to_json=SpindleCameraInterpolant.to_json
        ),
    })
    fov: SpindleCameraInterpolant = dataclasses.field(default_factory=SpindleCameraInterpolant, metadata={
        'reflection': FieldReflection[SpindleCameraInterpolant](
            SpindleCameraInterpolant, id=0x6654ae92, original_name='FOV', from_json=SpindleCameraInterpolant.from_json, to_json=SpindleCameraInterpolant.to_json
        ),
    })
    target_spline_type: SplineType = dataclasses.field(default_factory=SplineType, metadata={
        'reflection': FieldReflection[SplineType](
            SplineType, id=0x5604d304, original_name='TargetSplineType', from_json=SplineType.from_json, to_json=SplineType.to_json
        ),
    })
    target_spline_loops: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x33b4f106, original_name='TargetSplineLoops'
        ),
    })
    target_control_spline: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xc4dfbfa7, original_name='TargetControlSpline', from_json=Spline.from_json, to_json=Spline.to_json
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

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'SPND'

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
        if property_count != 23:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3bf4eba8
        flags = SpindleCameraFlags.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe56495fb
        angular_speed = SpindleCameraInterpolant.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x239debfc
        linear_speed = SpindleCameraInterpolant.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x27e8d703
        motion_radius = SpindleCameraInterpolant.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2f914525
        radial_offset = SpindleCameraInterpolant.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23aa31b7
        desired_angular_offset = SpindleCameraInterpolant.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe9e388af
        min_angular_offset = SpindleCameraInterpolant.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xde5a2c87
        max_angular_offset = SpindleCameraInterpolant.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1b3b2394
        look_at_angular_offset = SpindleCameraInterpolant.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf5666b6e
        look_at_z_offset = SpindleCameraInterpolant.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x66c618aa
        z_offset = SpindleCameraInterpolant.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb36d0fb6
        angular_constraint = SpindleCameraInterpolant.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcbb013cb
        angular_dampening = SpindleCameraInterpolant.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4abfb789
        desired_angular_speed = SpindleCameraInterpolant.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfb6a407a
        deactivate_radius = SpindleCameraInterpolant.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3ae66f80
        constraint_flip_angle = SpindleCameraInterpolant.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6654ae92
        fov = SpindleCameraInterpolant.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5604d304
        target_spline_type = SplineType.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33b4f106
        target_spline_loops = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc4dfbfa7
        target_control_spline = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33e4685b
        player_spline_type = SplineType.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x431769c6
        player_spline_loops = structs.BIG_bool_.unpack(data.read(1))[0]
    
        return cls(editor_properties, flags, angular_speed, linear_speed, motion_radius, radial_offset, desired_angular_offset, min_angular_offset, max_angular_offset, look_at_angular_offset, look_at_z_offset, z_offset, angular_constraint, angular_dampening, desired_angular_speed, deactivate_radius, constraint_flip_angle, fov, target_spline_type, target_spline_loops, target_control_spline, player_spline_type, player_spline_loops)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x17')  # 23 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b';\xf4\xeb\xa8')  # 0x3bf4eba8
        data.write(b'\x00\x04')  # size
        self.flags.to_stream(data, game)

        data.write(b'\xe5d\x95\xfb')  # 0xe56495fb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.angular_speed.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'#\x9d\xeb\xfc')  # 0x239debfc
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.linear_speed.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"'\xe8\xd7\x03")  # 0x27e8d703
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.motion_radius.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'/\x91E%')  # 0x2f914525
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.radial_offset.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'#\xaa1\xb7')  # 0x23aa31b7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.desired_angular_offset.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe9\xe3\x88\xaf')  # 0xe9e388af
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.min_angular_offset.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xdeZ,\x87')  # 0xde5a2c87
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.max_angular_offset.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x1b;#\x94')  # 0x1b3b2394
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.look_at_angular_offset.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf5fkn')  # 0xf5666b6e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.look_at_z_offset.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'f\xc6\x18\xaa')  # 0x66c618aa
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.z_offset.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb3m\x0f\xb6')  # 0xb36d0fb6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.angular_constraint.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xcb\xb0\x13\xcb')  # 0xcbb013cb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.angular_dampening.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'J\xbf\xb7\x89')  # 0x4abfb789
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.desired_angular_speed.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfbj@z')  # 0xfb6a407a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.deactivate_radius.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b':\xe6o\x80')  # 0x3ae66f80
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.constraint_flip_angle.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'fT\xae\x92')  # 0x6654ae92
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.fov.to_stream(data, game)
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

        data.write(b'3\xb4\xf1\x06')  # 0x33b4f106
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.target_spline_loops))

        data.write(b'\xc4\xdf\xbf\xa7')  # 0xc4dfbfa7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.target_control_spline.to_stream(data, game)
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

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SpindleCameraJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            flags=SpindleCameraFlags.from_json(json_data['flags']),
            angular_speed=SpindleCameraInterpolant.from_json(json_data['angular_speed']),
            linear_speed=SpindleCameraInterpolant.from_json(json_data['linear_speed']),
            motion_radius=SpindleCameraInterpolant.from_json(json_data['motion_radius']),
            radial_offset=SpindleCameraInterpolant.from_json(json_data['radial_offset']),
            desired_angular_offset=SpindleCameraInterpolant.from_json(json_data['desired_angular_offset']),
            min_angular_offset=SpindleCameraInterpolant.from_json(json_data['min_angular_offset']),
            max_angular_offset=SpindleCameraInterpolant.from_json(json_data['max_angular_offset']),
            look_at_angular_offset=SpindleCameraInterpolant.from_json(json_data['look_at_angular_offset']),
            look_at_z_offset=SpindleCameraInterpolant.from_json(json_data['look_at_z_offset']),
            z_offset=SpindleCameraInterpolant.from_json(json_data['z_offset']),
            angular_constraint=SpindleCameraInterpolant.from_json(json_data['angular_constraint']),
            angular_dampening=SpindleCameraInterpolant.from_json(json_data['angular_dampening']),
            desired_angular_speed=SpindleCameraInterpolant.from_json(json_data['desired_angular_speed']),
            deactivate_radius=SpindleCameraInterpolant.from_json(json_data['deactivate_radius']),
            constraint_flip_angle=SpindleCameraInterpolant.from_json(json_data['constraint_flip_angle']),
            fov=SpindleCameraInterpolant.from_json(json_data['fov']),
            target_spline_type=SplineType.from_json(json_data['target_spline_type']),
            target_spline_loops=json_data['target_spline_loops'],
            target_control_spline=Spline.from_json(json_data['target_control_spline']),
            player_spline_type=SplineType.from_json(json_data['player_spline_type']),
            player_spline_loops=json_data['player_spline_loops'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'flags': self.flags.to_json(),
            'angular_speed': self.angular_speed.to_json(),
            'linear_speed': self.linear_speed.to_json(),
            'motion_radius': self.motion_radius.to_json(),
            'radial_offset': self.radial_offset.to_json(),
            'desired_angular_offset': self.desired_angular_offset.to_json(),
            'min_angular_offset': self.min_angular_offset.to_json(),
            'max_angular_offset': self.max_angular_offset.to_json(),
            'look_at_angular_offset': self.look_at_angular_offset.to_json(),
            'look_at_z_offset': self.look_at_z_offset.to_json(),
            'z_offset': self.z_offset.to_json(),
            'angular_constraint': self.angular_constraint.to_json(),
            'angular_dampening': self.angular_dampening.to_json(),
            'desired_angular_speed': self.desired_angular_speed.to_json(),
            'deactivate_radius': self.deactivate_radius.to_json(),
            'constraint_flip_angle': self.constraint_flip_angle.to_json(),
            'fov': self.fov.to_json(),
            'target_spline_type': self.target_spline_type.to_json(),
            'target_spline_loops': self.target_spline_loops,
            'target_control_spline': self.target_control_spline.to_json(),
            'player_spline_type': self.player_spline_type.to_json(),
            'player_spline_loops': self.player_spline_loops,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_flags(data: typing.BinaryIO, game: Game, property_size: int) -> SpindleCameraFlags:
    return SpindleCameraFlags.from_stream(data, game)


def _decode_angular_speed(data: typing.BinaryIO, game: Game, property_size: int) -> SpindleCameraInterpolant:
    return SpindleCameraInterpolant.from_stream(data, game, property_size)


def _decode_linear_speed(data: typing.BinaryIO, game: Game, property_size: int) -> SpindleCameraInterpolant:
    return SpindleCameraInterpolant.from_stream(data, game, property_size)


def _decode_motion_radius(data: typing.BinaryIO, game: Game, property_size: int) -> SpindleCameraInterpolant:
    return SpindleCameraInterpolant.from_stream(data, game, property_size)


def _decode_radial_offset(data: typing.BinaryIO, game: Game, property_size: int) -> SpindleCameraInterpolant:
    return SpindleCameraInterpolant.from_stream(data, game, property_size)


def _decode_desired_angular_offset(data: typing.BinaryIO, game: Game, property_size: int) -> SpindleCameraInterpolant:
    return SpindleCameraInterpolant.from_stream(data, game, property_size)


def _decode_min_angular_offset(data: typing.BinaryIO, game: Game, property_size: int) -> SpindleCameraInterpolant:
    return SpindleCameraInterpolant.from_stream(data, game, property_size)


def _decode_max_angular_offset(data: typing.BinaryIO, game: Game, property_size: int) -> SpindleCameraInterpolant:
    return SpindleCameraInterpolant.from_stream(data, game, property_size)


def _decode_look_at_angular_offset(data: typing.BinaryIO, game: Game, property_size: int) -> SpindleCameraInterpolant:
    return SpindleCameraInterpolant.from_stream(data, game, property_size)


def _decode_look_at_z_offset(data: typing.BinaryIO, game: Game, property_size: int) -> SpindleCameraInterpolant:
    return SpindleCameraInterpolant.from_stream(data, game, property_size)


def _decode_z_offset(data: typing.BinaryIO, game: Game, property_size: int) -> SpindleCameraInterpolant:
    return SpindleCameraInterpolant.from_stream(data, game, property_size)


def _decode_angular_constraint(data: typing.BinaryIO, game: Game, property_size: int) -> SpindleCameraInterpolant:
    return SpindleCameraInterpolant.from_stream(data, game, property_size)


def _decode_angular_dampening(data: typing.BinaryIO, game: Game, property_size: int) -> SpindleCameraInterpolant:
    return SpindleCameraInterpolant.from_stream(data, game, property_size)


def _decode_desired_angular_speed(data: typing.BinaryIO, game: Game, property_size: int) -> SpindleCameraInterpolant:
    return SpindleCameraInterpolant.from_stream(data, game, property_size)


def _decode_deactivate_radius(data: typing.BinaryIO, game: Game, property_size: int) -> SpindleCameraInterpolant:
    return SpindleCameraInterpolant.from_stream(data, game, property_size)


def _decode_constraint_flip_angle(data: typing.BinaryIO, game: Game, property_size: int) -> SpindleCameraInterpolant:
    return SpindleCameraInterpolant.from_stream(data, game, property_size)


def _decode_fov(data: typing.BinaryIO, game: Game, property_size: int) -> SpindleCameraInterpolant:
    return SpindleCameraInterpolant.from_stream(data, game, property_size)


def _decode_target_spline_type(data: typing.BinaryIO, game: Game, property_size: int) -> SplineType:
    return SplineType.from_stream(data, game, property_size)


def _decode_target_control_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_player_spline_type(data: typing.BinaryIO, game: Game, property_size: int) -> SplineType:
    return SplineType.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0x3bf4eba8: ('flags', _decode_flags),
    0xe56495fb: ('angular_speed', _decode_angular_speed),
    0x239debfc: ('linear_speed', _decode_linear_speed),
    0x27e8d703: ('motion_radius', _decode_motion_radius),
    0x2f914525: ('radial_offset', _decode_radial_offset),
    0x23aa31b7: ('desired_angular_offset', _decode_desired_angular_offset),
    0xe9e388af: ('min_angular_offset', _decode_min_angular_offset),
    0xde5a2c87: ('max_angular_offset', _decode_max_angular_offset),
    0x1b3b2394: ('look_at_angular_offset', _decode_look_at_angular_offset),
    0xf5666b6e: ('look_at_z_offset', _decode_look_at_z_offset),
    0x66c618aa: ('z_offset', _decode_z_offset),
    0xb36d0fb6: ('angular_constraint', _decode_angular_constraint),
    0xcbb013cb: ('angular_dampening', _decode_angular_dampening),
    0x4abfb789: ('desired_angular_speed', _decode_desired_angular_speed),
    0xfb6a407a: ('deactivate_radius', _decode_deactivate_radius),
    0x3ae66f80: ('constraint_flip_angle', _decode_constraint_flip_angle),
    0x6654ae92: ('fov', _decode_fov),
    0x5604d304: ('target_spline_type', _decode_target_spline_type),
    0x33b4f106: ('target_spline_loops', structs.decode_BIG_bool_),
    0xc4dfbfa7: ('target_control_spline', _decode_target_control_spline),
    0x33e4685b: ('player_spline_type', _decode_player_spline_type),
    0x431769c6: ('player_spline_loops', structs.decode_BIG_bool_),
}
