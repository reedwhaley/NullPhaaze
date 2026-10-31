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
from retro_data_structures.properties.echoes.archetypes.CameraAngleConstraint import CameraAngleConstraint
from retro_data_structures.properties.echoes.archetypes.CameraBehaviour import CameraBehaviour
from retro_data_structures.properties.echoes.archetypes.CameraDistance import CameraDistance
from retro_data_structures.properties.echoes.archetypes.CameraFOV import CameraFOV
from retro_data_structures.properties.echoes.archetypes.CameraOffset import CameraOffset
from retro_data_structures.properties.echoes.archetypes.CameraSpeed import CameraSpeed
from retro_data_structures.properties.echoes.archetypes.CameraZOffset import CameraZOffset
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.InterpolationOrientationType import InterpolationOrientationType
from retro_data_structures.properties.echoes.archetypes.InterpolationType import InterpolationType
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class CameraHintJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        priority: int
        timer: float
        behaviour: json_util.JsonObject
        flags: int
        min_speed_distance: json_util.JsonObject
        max_speed_distance: json_util.JsonObject
        backwards_distance: json_util.JsonObject
        look_at_offset: json_util.JsonObject
        world_offset: json_util.JsonValue
        field_of_view: json_util.JsonObject
        pitch_constraint: json_util.JsonObject
        yaw_constraint: json_util.JsonObject
        angular_speed: json_util.JsonObject
        z_offset: json_util.JsonObject
        interpolate_off_time: float
        interpolate_on_time: float
        interpolate_control_time: float
        interpolation_on_type: json_util.JsonObject
        interpolation_on_orientation_type: json_util.JsonObject
        interpolation_off_type: json_util.JsonObject
    

class CameraHintFlags(enum.IntFlag):
    CalculateCameraPosition = 1
    ChaseAllowed = 2
    BoostAllowed = 4
    ObscureAvoidance = 8
    VolumeCollider = 16
    ApplyImmediately = 32
    LookAtBall = 64
    HintDistanceSelection = 128
    HintDistanceSelfPosition = 256
    ControlInterpolation = 512
    UseExistingTransform = 1024
    FreezeTargetPosition = 2048
    ClampVelocity = 4096
    SkipCinematic = 8192
    NoElevationInterpolation = 16384
    DirectElevation = 32768
    OverrideLookDirection = 65536
    NoElevationVelocityClamp = 131072
    CalculateTransformFromPreviousCamera = 262144
    NoSpline = 524288
    Unknown21 = 1048576
    InterpolateRotation = 2097152
    UseHintHeight = 4194304
    NoElevationAndDistanceConstraint = 8388608
    NoScreenFlash = 16777216
    AcrossAreas = 33554432
    InstantUnmorph = 67108864
    InstantMorph = 134217728

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
class CameraHint(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    priority: int = dataclasses.field(default=50, metadata={
        'reflection': FieldReflection[int](
            int, id=0x42087650, original_name='Priority'
        ),
    })
    timer: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8747552e, original_name='Timer'
        ),
    })
    behaviour: CameraBehaviour = dataclasses.field(default_factory=CameraBehaviour, metadata={
        'reflection': FieldReflection[CameraBehaviour](
            CameraBehaviour, id=0x380585ec, original_name='Behaviour', from_json=CameraBehaviour.from_json, to_json=CameraBehaviour.to_json
        ),
    })
    flags: CameraHintFlags = dataclasses.field(default=CameraHintFlags(286), metadata={
        'reflection': FieldReflection[CameraHintFlags](
            CameraHintFlags, id=0x21d720a9, original_name='Flags', from_json=CameraHintFlags.from_json, to_json=CameraHintFlags.to_json
        ),
    })
    min_speed_distance: CameraDistance = dataclasses.field(default_factory=CameraDistance, metadata={
        'reflection': FieldReflection[CameraDistance](
            CameraDistance, id=0x456d05c6, original_name='MinSpeedDistance', from_json=CameraDistance.from_json, to_json=CameraDistance.to_json
        ),
    })
    max_speed_distance: CameraDistance = dataclasses.field(default_factory=CameraDistance, metadata={
        'reflection': FieldReflection[CameraDistance](
            CameraDistance, id=0xf5521ffa, original_name='MaxSpeedDistance', from_json=CameraDistance.from_json, to_json=CameraDistance.to_json
        ),
    })
    backwards_distance: CameraDistance = dataclasses.field(default_factory=CameraDistance, metadata={
        'reflection': FieldReflection[CameraDistance](
            CameraDistance, id=0x89658a06, original_name='BackwardsDistance', from_json=CameraDistance.from_json, to_json=CameraDistance.to_json
        ),
    })
    look_at_offset: CameraOffset = dataclasses.field(default_factory=CameraOffset, metadata={
        'reflection': FieldReflection[CameraOffset](
            CameraOffset, id=0x8d0a9113, original_name='LookAtOffset', from_json=CameraOffset.from_json, to_json=CameraOffset.to_json
        ),
    })
    world_offset: Vector = dataclasses.field(default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0xefebe838, original_name='WorldOffset', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    field_of_view: CameraFOV = dataclasses.field(default_factory=CameraFOV, metadata={
        'reflection': FieldReflection[CameraFOV](
            CameraFOV, id=0xf71c36f2, original_name='FieldOfView', from_json=CameraFOV.from_json, to_json=CameraFOV.to_json
        ),
    })
    pitch_constraint: CameraAngleConstraint = dataclasses.field(default_factory=CameraAngleConstraint, metadata={
        'reflection': FieldReflection[CameraAngleConstraint](
            CameraAngleConstraint, id=0x664c450a, original_name='PitchConstraint', from_json=CameraAngleConstraint.from_json, to_json=CameraAngleConstraint.to_json
        ),
    })
    yaw_constraint: CameraAngleConstraint = dataclasses.field(default_factory=CameraAngleConstraint, metadata={
        'reflection': FieldReflection[CameraAngleConstraint](
            CameraAngleConstraint, id=0xc82395fa, original_name='YawConstraint', from_json=CameraAngleConstraint.from_json, to_json=CameraAngleConstraint.to_json
        ),
    })
    angular_speed: CameraSpeed = dataclasses.field(default_factory=CameraSpeed, metadata={
        'reflection': FieldReflection[CameraSpeed](
            CameraSpeed, id=0x645eb009, original_name='AngularSpeed', from_json=CameraSpeed.from_json, to_json=CameraSpeed.to_json
        ),
    })
    z_offset: CameraZOffset = dataclasses.field(default_factory=CameraZOffset, metadata={
        'reflection': FieldReflection[CameraZOffset](
            CameraZOffset, id=0x80cfbb54, original_name='ZOffset', from_json=CameraZOffset.from_json, to_json=CameraZOffset.to_json
        ),
    })
    interpolate_off_time: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2ae08be1, original_name='InterpolateOffTime'
        ),
    })
    interpolate_on_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4361d075, original_name='InterpolateOnTime'
        ),
    })
    interpolate_control_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc91ef813, original_name='InterpolateControlTime'
        ),
    })
    interpolation_on_type: InterpolationType = dataclasses.field(default_factory=InterpolationType, metadata={
        'reflection': FieldReflection[InterpolationType](
            InterpolationType, id=0x934e392c, original_name='InterpolationOnType', from_json=InterpolationType.from_json, to_json=InterpolationType.to_json
        ),
    })
    interpolation_on_orientation_type: InterpolationOrientationType = dataclasses.field(default_factory=InterpolationOrientationType, metadata={
        'reflection': FieldReflection[InterpolationOrientationType](
            InterpolationOrientationType, id=0x9e8631f1, original_name='InterpolationOnOrientationType', from_json=InterpolationOrientationType.from_json, to_json=InterpolationOrientationType.to_json
        ),
    })
    interpolation_off_type: InterpolationType = dataclasses.field(default_factory=InterpolationType, metadata={
        'reflection': FieldReflection[InterpolationType](
            InterpolationType, id=0x138729a7, original_name='InterpolationOffType', from_json=InterpolationType.from_json, to_json=InterpolationType.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'CAMH'

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
        if property_count != 21:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42087650
        priority = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8747552e
        timer = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x380585ec
        behaviour = CameraBehaviour.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21d720a9
        flags = CameraHintFlags.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x456d05c6
        min_speed_distance = CameraDistance.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf5521ffa
        max_speed_distance = CameraDistance.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x89658a06
        backwards_distance = CameraDistance.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8d0a9113
        look_at_offset = CameraOffset.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xefebe838
        world_offset = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf71c36f2
        field_of_view = CameraFOV.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x664c450a
        pitch_constraint = CameraAngleConstraint.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc82395fa
        yaw_constraint = CameraAngleConstraint.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x645eb009
        angular_speed = CameraSpeed.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x80cfbb54
        z_offset = CameraZOffset.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2ae08be1
        interpolate_off_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4361d075
        interpolate_on_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc91ef813
        interpolate_control_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x934e392c
        interpolation_on_type = InterpolationType.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9e8631f1
        interpolation_on_orientation_type = InterpolationOrientationType.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x138729a7
        interpolation_off_type = InterpolationType.from_stream(data, game, property_size)
    
        return cls(editor_properties, priority, timer, behaviour, flags, min_speed_distance, max_speed_distance, backwards_distance, look_at_offset, world_offset, field_of_view, pitch_constraint, yaw_constraint, angular_speed, z_offset, interpolate_off_time, interpolate_on_time, interpolate_control_time, interpolation_on_type, interpolation_on_orientation_type, interpolation_off_type)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x15')  # 21 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game, default_override={'misc_flags': 3})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'B\x08vP')  # 0x42087650
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.priority))

        data.write(b'\x87GU.')  # 0x8747552e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.timer))

        data.write(b'8\x05\x85\xec')  # 0x380585ec
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.behaviour.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'!\xd7 \xa9')  # 0x21d720a9
        data.write(b'\x00\x04')  # size
        self.flags.to_stream(data, game)

        data.write(b'Em\x05\xc6')  # 0x456d05c6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.min_speed_distance.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf5R\x1f\xfa')  # 0xf5521ffa
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.max_speed_distance.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x89e\x8a\x06')  # 0x89658a06
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.backwards_distance.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8d\n\x91\x13')  # 0x8d0a9113
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.look_at_offset.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xef\xeb\xe88')  # 0xefebe838
        data.write(b'\x00\x0c')  # size
        self.world_offset.to_stream(data, game)

        data.write(b'\xf7\x1c6\xf2')  # 0xf71c36f2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.field_of_view.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'fLE\n')  # 0x664c450a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.pitch_constraint.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc8#\x95\xfa')  # 0xc82395fa
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.yaw_constraint.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'd^\xb0\t')  # 0x645eb009
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.angular_speed.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x80\xcf\xbbT')  # 0x80cfbb54
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.z_offset.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'*\xe0\x8b\xe1')  # 0x2ae08be1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.interpolate_off_time))

        data.write(b'Ca\xd0u')  # 0x4361d075
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.interpolate_on_time))

        data.write(b'\xc9\x1e\xf8\x13')  # 0xc91ef813
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.interpolate_control_time))

        data.write(b'\x93N9,')  # 0x934e392c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.interpolation_on_type.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9e\x861\xf1')  # 0x9e8631f1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.interpolation_on_orientation_type.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x13\x87)\xa7')  # 0x138729a7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.interpolation_off_type.to_stream(data, game)
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
        json_data = typing.cast("CameraHintJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            priority=json_data['priority'],
            timer=json_data['timer'],
            behaviour=CameraBehaviour.from_json(json_data['behaviour']),
            flags=CameraHintFlags.from_json(json_data['flags']),
            min_speed_distance=CameraDistance.from_json(json_data['min_speed_distance']),
            max_speed_distance=CameraDistance.from_json(json_data['max_speed_distance']),
            backwards_distance=CameraDistance.from_json(json_data['backwards_distance']),
            look_at_offset=CameraOffset.from_json(json_data['look_at_offset']),
            world_offset=Vector.from_json(json_data['world_offset']),
            field_of_view=CameraFOV.from_json(json_data['field_of_view']),
            pitch_constraint=CameraAngleConstraint.from_json(json_data['pitch_constraint']),
            yaw_constraint=CameraAngleConstraint.from_json(json_data['yaw_constraint']),
            angular_speed=CameraSpeed.from_json(json_data['angular_speed']),
            z_offset=CameraZOffset.from_json(json_data['z_offset']),
            interpolate_off_time=json_data['interpolate_off_time'],
            interpolate_on_time=json_data['interpolate_on_time'],
            interpolate_control_time=json_data['interpolate_control_time'],
            interpolation_on_type=InterpolationType.from_json(json_data['interpolation_on_type']),
            interpolation_on_orientation_type=InterpolationOrientationType.from_json(json_data['interpolation_on_orientation_type']),
            interpolation_off_type=InterpolationType.from_json(json_data['interpolation_off_type']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'priority': self.priority,
            'timer': self.timer,
            'behaviour': self.behaviour.to_json(),
            'flags': self.flags.to_json(),
            'min_speed_distance': self.min_speed_distance.to_json(),
            'max_speed_distance': self.max_speed_distance.to_json(),
            'backwards_distance': self.backwards_distance.to_json(),
            'look_at_offset': self.look_at_offset.to_json(),
            'world_offset': self.world_offset.to_json(),
            'field_of_view': self.field_of_view.to_json(),
            'pitch_constraint': self.pitch_constraint.to_json(),
            'yaw_constraint': self.yaw_constraint.to_json(),
            'angular_speed': self.angular_speed.to_json(),
            'z_offset': self.z_offset.to_json(),
            'interpolate_off_time': self.interpolate_off_time,
            'interpolate_on_time': self.interpolate_on_time,
            'interpolate_control_time': self.interpolate_control_time,
            'interpolation_on_type': self.interpolation_on_type.to_json(),
            'interpolation_on_orientation_type': self.interpolation_on_orientation_type.to_json(),
            'interpolation_off_type': self.interpolation_off_type.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})


def _decode_behaviour(data: typing.BinaryIO, game: Game, property_size: int) -> CameraBehaviour:
    return CameraBehaviour.from_stream(data, game, property_size)


def _decode_flags(data: typing.BinaryIO, game: Game, property_size: int) -> CameraHintFlags:
    return CameraHintFlags.from_stream(data, game)


def _decode_min_speed_distance(data: typing.BinaryIO, game: Game, property_size: int) -> CameraDistance:
    return CameraDistance.from_stream(data, game, property_size)


def _decode_max_speed_distance(data: typing.BinaryIO, game: Game, property_size: int) -> CameraDistance:
    return CameraDistance.from_stream(data, game, property_size)


def _decode_backwards_distance(data: typing.BinaryIO, game: Game, property_size: int) -> CameraDistance:
    return CameraDistance.from_stream(data, game, property_size)


def _decode_look_at_offset(data: typing.BinaryIO, game: Game, property_size: int) -> CameraOffset:
    return CameraOffset.from_stream(data, game, property_size)


def _decode_world_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_field_of_view(data: typing.BinaryIO, game: Game, property_size: int) -> CameraFOV:
    return CameraFOV.from_stream(data, game, property_size)


def _decode_pitch_constraint(data: typing.BinaryIO, game: Game, property_size: int) -> CameraAngleConstraint:
    return CameraAngleConstraint.from_stream(data, game, property_size)


def _decode_yaw_constraint(data: typing.BinaryIO, game: Game, property_size: int) -> CameraAngleConstraint:
    return CameraAngleConstraint.from_stream(data, game, property_size)


def _decode_angular_speed(data: typing.BinaryIO, game: Game, property_size: int) -> CameraSpeed:
    return CameraSpeed.from_stream(data, game, property_size)


def _decode_z_offset(data: typing.BinaryIO, game: Game, property_size: int) -> CameraZOffset:
    return CameraZOffset.from_stream(data, game, property_size)


def _decode_interpolation_on_type(data: typing.BinaryIO, game: Game, property_size: int) -> InterpolationType:
    return InterpolationType.from_stream(data, game, property_size)


def _decode_interpolation_on_orientation_type(data: typing.BinaryIO, game: Game, property_size: int) -> InterpolationOrientationType:
    return InterpolationOrientationType.from_stream(data, game, property_size)


def _decode_interpolation_off_type(data: typing.BinaryIO, game: Game, property_size: int) -> InterpolationType:
    return InterpolationType.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0x42087650: ('priority', structs.decode_BIG_l),
    0x8747552e: ('timer', structs.decode_BIG_f),
    0x380585ec: ('behaviour', _decode_behaviour),
    0x21d720a9: ('flags', _decode_flags),
    0x456d05c6: ('min_speed_distance', _decode_min_speed_distance),
    0xf5521ffa: ('max_speed_distance', _decode_max_speed_distance),
    0x89658a06: ('backwards_distance', _decode_backwards_distance),
    0x8d0a9113: ('look_at_offset', _decode_look_at_offset),
    0xefebe838: ('world_offset', _decode_world_offset),
    0xf71c36f2: ('field_of_view', _decode_field_of_view),
    0x664c450a: ('pitch_constraint', _decode_pitch_constraint),
    0xc82395fa: ('yaw_constraint', _decode_yaw_constraint),
    0x645eb009: ('angular_speed', _decode_angular_speed),
    0x80cfbb54: ('z_offset', _decode_z_offset),
    0x2ae08be1: ('interpolate_off_time', structs.decode_BIG_f),
    0x4361d075: ('interpolate_on_time', structs.decode_BIG_f),
    0xc91ef813: ('interpolate_control_time', structs.decode_BIG_f),
    0x934e392c: ('interpolation_on_type', _decode_interpolation_on_type),
    0x9e8631f1: ('interpolation_on_orientation_type', _decode_interpolation_on_orientation_type),
    0x138729a7: ('interpolation_off_type', _decode_interpolation_off_type),
}
