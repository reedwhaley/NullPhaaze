# Generated File
from __future__ import annotations

import dataclasses
import struct
import typing
import typing_extensions

from retro_data_structures import json_util
from retro_data_structures.game_check import Game
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.corruption.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.corruption.archetypes.PlatformMotionProperties import PlatformMotionProperties
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class PlatformJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        collision_box: json_util.JsonValue
        collision_offset: json_util.JsonValue
        model: int
        animation: json_util.JsonObject
        actor_information: json_util.JsonObject
        collision_model: int
        health: json_util.JsonObject
        vulnerability: json_util.JsonObject
        x_ray_transparency: float
        maximum_splashes: int
        splash_generation_rate: int
        render_rain_splashes: bool
        exclude_from_line_of_sight_test: bool
        motion_properties: json_util.JsonObject
        conveyor_belt_velocity: json_util.JsonValue
        random_animation_offset: float
        orbit_offset_local: bool
        orbit_offset: json_util.JsonValue
        track_object_velocity: float
        look_at_velocity: float
    

@dataclasses.dataclass()
class Platform(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    collision_box: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0xf344c0b0, original_name='CollisionBox', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    collision_offset: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x2e686c2a, original_name='CollisionOffset', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc27ffa8f, original_name='Model'
        ),
    })
    animation: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0xa3d63f44, original_name='Animation', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    actor_information: ActorParameters = dataclasses.field(default_factory=ActorParameters, metadata={
        'reflection': FieldReflection[ActorParameters](
            ActorParameters, id=0x7e397fed, original_name='ActorInformation', from_json=ActorParameters.from_json, to_json=ActorParameters.to_json
        ),
    })
    collision_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['DCLN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x0fc966dc, original_name='CollisionModel'
        ),
    })
    health: HealthInfo = dataclasses.field(default_factory=HealthInfo, metadata={
        'reflection': FieldReflection[HealthInfo](
            HealthInfo, id=0xcf90d15e, original_name='Health', from_json=HealthInfo.from_json, to_json=HealthInfo.to_json
        ),
    })
    vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x7b71ae90, original_name='Vulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    x_ray_transparency: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6150d687, original_name='XRayTransparency'
        ),
    })
    maximum_splashes: int = dataclasses.field(default=200, metadata={
        'reflection': FieldReflection[int](
            int, id=0xdcd56fe8, original_name='MaximumSplashes'
        ),
    })
    splash_generation_rate: int = dataclasses.field(default=20, metadata={
        'reflection': FieldReflection[int](
            int, id=0x682de15c, original_name='SplashGenerationRate'
        ),
    })
    render_rain_splashes: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xac3adda6, original_name='RenderRainSplashes'
        ),
    })
    exclude_from_line_of_sight_test: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xf203bc81, original_name='ExcludeFromLineOfSightTest'
        ),
    })
    motion_properties: PlatformMotionProperties = dataclasses.field(default_factory=PlatformMotionProperties, metadata={
        'reflection': FieldReflection[PlatformMotionProperties](
            PlatformMotionProperties, id=0x0a9dbf91, original_name='MotionProperties', from_json=PlatformMotionProperties.from_json, to_json=PlatformMotionProperties.to_json
        ),
    })
    conveyor_belt_velocity: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.15000000596046448, z=0.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x24fdeea1, original_name='ConveyorBeltVelocity', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    random_animation_offset: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbf69c03e, original_name='RandomAnimationOffset'
        ),
    })
    orbit_offset_local: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xe73f123d, original_name='OrbitOffsetLocal'
        ),
    })
    orbit_offset: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x850115e4, original_name='OrbitOffset', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    track_object_velocity: float = dataclasses.field(default=1800.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6b5e87a7, original_name='TrackObjectVelocity'
        ),
    })
    look_at_velocity: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3dc75733, original_name='LookAtVelocity'
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'PLAT'

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
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf344c0b0
        collision_box = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2e686c2a
        collision_offset = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc27ffa8f
        model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa3d63f44
        animation = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0fc966dc
        collision_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcf90d15e
        health = HealthInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7b71ae90
        vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6150d687
        x_ray_transparency = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdcd56fe8
        maximum_splashes = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x682de15c
        splash_generation_rate = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xac3adda6
        render_rain_splashes = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf203bc81
        exclude_from_line_of_sight_test = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0a9dbf91
        motion_properties = PlatformMotionProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24fdeea1
        conveyor_belt_velocity = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbf69c03e
        random_animation_offset = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe73f123d
        orbit_offset_local = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x850115e4
        orbit_offset = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6b5e87a7
        track_object_velocity = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3dc75733
        look_at_velocity = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(editor_properties, collision_box, collision_offset, model, animation, actor_information, collision_model, health, vulnerability, x_ray_transparency, maximum_splashes, splash_generation_rate, render_rain_splashes, exclude_from_line_of_sight_test, motion_properties, conveyor_belt_velocity, random_animation_offset, orbit_offset_local, orbit_offset, track_object_velocity, look_at_velocity)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x15')  # 21 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf3D\xc0\xb0')  # 0xf344c0b0
        data.write(b'\x00\x0c')  # size
        self.collision_box.to_stream(data, game)

        data.write(b'.hl*')  # 0x2e686c2a
        data.write(b'\x00\x0c')  # size
        self.collision_offset.to_stream(data, game)

        data.write(b'\xc2\x7f\xfa\x8f')  # 0xc27ffa8f
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.model))

        data.write(b'\xa3\xd6?D')  # 0xa3d63f44
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.animation.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'~9\x7f\xed')  # 0x7e397fed
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.actor_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x0f\xc9f\xdc')  # 0xfc966dc
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.collision_model))

        data.write(b'\xcf\x90\xd1^')  # 0xcf90d15e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.health.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'{q\xae\x90')  # 0x7b71ae90
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'aP\xd6\x87')  # 0x6150d687
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.x_ray_transparency))

        data.write(b'\xdc\xd5o\xe8')  # 0xdcd56fe8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.maximum_splashes))

        data.write(b'h-\xe1\\')  # 0x682de15c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.splash_generation_rate))

        data.write(b'\xac:\xdd\xa6')  # 0xac3adda6
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.render_rain_splashes))

        data.write(b'\xf2\x03\xbc\x81')  # 0xf203bc81
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.exclude_from_line_of_sight_test))

        data.write(b'\n\x9d\xbf\x91')  # 0xa9dbf91
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.motion_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'$\xfd\xee\xa1')  # 0x24fdeea1
        data.write(b'\x00\x0c')  # size
        self.conveyor_belt_velocity.to_stream(data, game)

        data.write(b'\xbfi\xc0>')  # 0xbf69c03e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.random_animation_offset))

        data.write(b'\xe7?\x12=')  # 0xe73f123d
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.orbit_offset_local))

        data.write(b'\x85\x01\x15\xe4')  # 0x850115e4
        data.write(b'\x00\x0c')  # size
        self.orbit_offset.to_stream(data, game)

        data.write(b'k^\x87\xa7')  # 0x6b5e87a7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.track_object_velocity))

        data.write(b'=\xc7W3')  # 0x3dc75733
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.look_at_velocity))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlatformJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            collision_box=Vector.from_json(json_data['collision_box']),
            collision_offset=Vector.from_json(json_data['collision_offset']),
            model=json_data['model'],
            animation=AnimationParameters.from_json(json_data['animation']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
            collision_model=json_data['collision_model'],
            health=HealthInfo.from_json(json_data['health']),
            vulnerability=DamageVulnerability.from_json(json_data['vulnerability']),
            x_ray_transparency=json_data['x_ray_transparency'],
            maximum_splashes=json_data['maximum_splashes'],
            splash_generation_rate=json_data['splash_generation_rate'],
            render_rain_splashes=json_data['render_rain_splashes'],
            exclude_from_line_of_sight_test=json_data['exclude_from_line_of_sight_test'],
            motion_properties=PlatformMotionProperties.from_json(json_data['motion_properties']),
            conveyor_belt_velocity=Vector.from_json(json_data['conveyor_belt_velocity']),
            random_animation_offset=json_data['random_animation_offset'],
            orbit_offset_local=json_data['orbit_offset_local'],
            orbit_offset=Vector.from_json(json_data['orbit_offset']),
            track_object_velocity=json_data['track_object_velocity'],
            look_at_velocity=json_data['look_at_velocity'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'collision_box': self.collision_box.to_json(),
            'collision_offset': self.collision_offset.to_json(),
            'model': self.model,
            'animation': self.animation.to_json(),
            'actor_information': self.actor_information.to_json(),
            'collision_model': self.collision_model,
            'health': self.health.to_json(),
            'vulnerability': self.vulnerability.to_json(),
            'x_ray_transparency': self.x_ray_transparency,
            'maximum_splashes': self.maximum_splashes,
            'splash_generation_rate': self.splash_generation_rate,
            'render_rain_splashes': self.render_rain_splashes,
            'exclude_from_line_of_sight_test': self.exclude_from_line_of_sight_test,
            'motion_properties': self.motion_properties.to_json(),
            'conveyor_belt_velocity': self.conveyor_belt_velocity.to_json(),
            'random_animation_offset': self.random_animation_offset,
            'orbit_offset_local': self.orbit_offset_local,
            'orbit_offset': self.orbit_offset.to_json(),
            'track_object_velocity': self.track_object_velocity,
            'look_at_velocity': self.look_at_velocity,
        }

    def _dependencies_for_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model)

    def _dependencies_for_collision_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.collision_model)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_model, "model", "AssetId"),
            (self.animation.dependencies_for, "animation", "AnimationParameters"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_collision_model, "collision_model", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for Platform.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_collision_box(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_collision_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_animation(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_motion_properties(data: typing.BinaryIO, game: Game, property_size: int) -> PlatformMotionProperties:
    return PlatformMotionProperties.from_stream(data, game, property_size)


def _decode_conveyor_belt_velocity(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_orbit_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xf344c0b0: ('collision_box', _decode_collision_box),
    0x2e686c2a: ('collision_offset', _decode_collision_offset),
    0xc27ffa8f: ('model', structs.decode_BIG_Q),
    0xa3d63f44: ('animation', _decode_animation),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0x0fc966dc: ('collision_model', structs.decode_BIG_Q),
    0xcf90d15e: ('health', _decode_health),
    0x7b71ae90: ('vulnerability', _decode_vulnerability),
    0x6150d687: ('x_ray_transparency', structs.decode_BIG_f),
    0xdcd56fe8: ('maximum_splashes', structs.decode_BIG_l),
    0x682de15c: ('splash_generation_rate', structs.decode_BIG_l),
    0xac3adda6: ('render_rain_splashes', structs.decode_BIG_bool_),
    0xf203bc81: ('exclude_from_line_of_sight_test', structs.decode_BIG_bool_),
    0x0a9dbf91: ('motion_properties', _decode_motion_properties),
    0x24fdeea1: ('conveyor_belt_velocity', _decode_conveyor_belt_velocity),
    0xbf69c03e: ('random_animation_offset', structs.decode_BIG_f),
    0xe73f123d: ('orbit_offset_local', structs.decode_BIG_bool_),
    0x850115e4: ('orbit_offset', _decode_orbit_offset),
    0x6b5e87a7: ('track_object_velocity', structs.decode_BIG_f),
    0x3dc75733: ('look_at_velocity', structs.decode_BIG_f),
}
