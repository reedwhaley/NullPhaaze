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
from retro_data_structures.properties.corruption.archetypes.DebrisPropertiesOrientationEnum import DebrisPropertiesOrientationEnum
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class DebrisPropertiesJson(typing_extensions.TypedDict):
        cone_spread_yaw: float
        cone_spread_pitch: float
        initial_direction: json_util.JsonValue
        position_offset: json_util.JsonValue
        transform_position_offset: bool
        minimum_speed: float
        maximum_speed: float
        minimum_spin_speed: json_util.JsonValue
        maximum_spin_speed: json_util.JsonValue
        minimum_lifetime: float
        maximum_lifetime: float
        disable_collision_time: float
        fade_in_end_percentage: float
        fade_out_start_percentage: float
        start_color: json_util.JsonValue
        middle_color: json_util.JsonValue
        end_color: json_util.JsonValue
        color_add_from_start: bool
        color_add_to_end: bool
        scale_start_percentage: float
        final_scale: json_util.JsonValue
        bounciness: float
        friction: float
        gravity: float
        disable_physics_threshold: float
        model: int
        model_pivot_point: json_util.JsonValue
        bounce_sound: int
        max_bounce_sounds: int
        bounce_sound_volume_decay: float
        bounce_sound_speed_threshold: float
        unknown_0x5e9f5215: float
        unknown_0x39743618: float
        unknown_0x33e0fbb4: float
        min_speed_for_collided_event: float
        min_time_between_collided_events: float
        particle_system1: int
        particle_system1_scale: json_util.JsonValue
        particle_system1_uses_global_translation: bool
        particle_system1_uses_global_orientation: bool
        particle_system1_wait_for_particles_to_die: bool
        particle_system1_orientation: json_util.JsonObject
        particle_system2: int
        particle_system2_scale: json_util.JsonValue
        particle_system2_uses_global_translation: bool
        particle_system2_uses_global_orientation: bool
        particle_system2_wait_for_particles_to_die: bool
        particle_system2_orientation: json_util.JsonObject
        is_collider: bool
        collide_with_ai_block: bool
        is_shootable: bool
        touch_bounds_scalar: json_util.JsonValue
        die_on_collision: bool
        flicker_on_fade_out: bool
        use_cached_collision_geometry: bool
        do_not_delete_attached_object: bool
        delete_debris_on_attached_object_deletion: bool
        dragged_objects_use_debris_orientation: bool
        recenter_model_pivot: bool
    

@dataclasses.dataclass()
class DebrisProperties(BaseProperty):
    cone_spread_yaw: float = dataclasses.field(default=180.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5c3c4a57, original_name='ConeSpreadYaw'
        ),
    })
    cone_spread_pitch: float = dataclasses.field(default=180.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa79fc55f, original_name='ConeSpreadPitch'
        ),
    })
    initial_direction: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=1.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x01a0dfe6, original_name='InitialDirection', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    position_offset: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0xef90f09d, original_name='PositionOffset', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    transform_position_offset: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xc4b1e6a1, original_name='TransformPositionOffset'
        ),
    })
    minimum_speed: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0185263e, original_name='MinimumSpeed'
        ),
    })
    maximum_speed: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x140ef2cc, original_name='MaximumSpeed'
        ),
    })
    minimum_spin_speed: Vector = dataclasses.field(default_factory=lambda: Vector(x=-1.0, y=-1.0, z=-1.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0xf78c8ac7, original_name='MinimumSpinSpeed', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    maximum_spin_speed: Vector = dataclasses.field(default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0xb69bb541, original_name='MaximumSpinSpeed', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    minimum_lifetime: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd6594622, original_name='MinimumLifetime'
        ),
    })
    maximum_lifetime: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xff27bb3a, original_name='MaximumLifetime'
        ),
    })
    disable_collision_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6b571ba5, original_name='DisableCollisionTime'
        ),
    })
    fade_in_end_percentage: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x50051a17, original_name='FadeInEndPercentage'
        ),
    })
    fade_out_start_percentage: float = dataclasses.field(default=80.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6353c409, original_name='FadeOutStartPercentage'
        ),
    })
    start_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x3a5634d8, original_name='StartColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    middle_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x7c6ebe98, original_name='MiddleColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    end_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x5af5867d, original_name='EndColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    color_add_from_start: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xd79690b4, original_name='ColorAddFromStart'
        ),
    })
    color_add_to_end: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x0145d02d, original_name='ColorAddToEnd'
        ),
    })
    scale_start_percentage: float = dataclasses.field(default=80.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x886e7c9f, original_name='ScaleStartPercentage'
        ),
    })
    final_scale: Vector = dataclasses.field(default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x80c22a0a, original_name='FinalScale', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    bounciness: float = dataclasses.field(default=0.375, metadata={
        'reflection': FieldReflection[float](
            float, id=0x417f4a91, original_name='Bounciness'
        ),
    })
    friction: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x16b72d49, original_name='Friction'
        ),
    })
    gravity: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2f2ae3e5, original_name='Gravity'
        ),
    })
    disable_physics_threshold: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x295f05b7, original_name='DisablePhysicsThreshold'
        ),
    })
    model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc27ffa8f, original_name='Model'
        ),
    })
    model_pivot_point: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0xeedbb07e, original_name='ModelPivotPoint', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    bounce_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xf1925576, original_name='BounceSound'
        ),
    })
    max_bounce_sounds: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x991202c3, original_name='MaxBounceSounds'
        ),
    })
    bounce_sound_volume_decay: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x76c79503, original_name='BounceSoundVolumeDecay'
        ),
    })
    bounce_sound_speed_threshold: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x310dfac8, original_name='BounceSoundSpeedThreshold'
        ),
    })
    unknown_0x5e9f5215: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5e9f5215, original_name='Unknown'
        ),
    })
    unknown_0x39743618: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x39743618, original_name='Unknown'
        ),
    })
    unknown_0x33e0fbb4: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x33e0fbb4, original_name='Unknown'
        ),
    })
    min_speed_for_collided_event: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe82e7ed7, original_name='MinSpeedForCollidedEvent'
        ),
    })
    min_time_between_collided_events: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x855ee21b, original_name='MinTimeBetweenCollidedEvents'
        ),
    })
    particle_system1: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x478d0aa3, original_name='ParticleSystem1'
        ),
    })
    particle_system1_scale: Vector = dataclasses.field(default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x19a6f71f, original_name='ParticleSystem1Scale', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    particle_system1_uses_global_translation: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x3b03a01e, original_name='ParticleSystem1UsesGlobalTranslation'
        ),
    })
    particle_system1_uses_global_orientation: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xdb1fa61c, original_name='ParticleSystem1UsesGlobalOrientation'
        ),
    })
    particle_system1_wait_for_particles_to_die: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x3bdd2fed, original_name='ParticleSystem1WaitForParticlesToDie'
        ),
    })
    particle_system1_orientation: DebrisPropertiesOrientationEnum = dataclasses.field(default_factory=DebrisPropertiesOrientationEnum, metadata={
        'reflection': FieldReflection[DebrisPropertiesOrientationEnum](
            DebrisPropertiesOrientationEnum, id=0xf5dd4690, original_name='ParticleSystem1Orientation', from_json=DebrisPropertiesOrientationEnum.from_json, to_json=DebrisPropertiesOrientationEnum.to_json
        ),
    })
    particle_system2: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc119780d, original_name='ParticleSystem2'
        ),
    })
    particle_system2_scale: Vector = dataclasses.field(default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x6e3825ef, original_name='ParticleSystem2Scale', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    particle_system2_uses_global_translation: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xc9544de6, original_name='ParticleSystem2UsesGlobalTranslation'
        ),
    })
    particle_system2_uses_global_orientation: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x29484be4, original_name='ParticleSystem2UsesGlobalOrientation'
        ),
    })
    particle_system2_wait_for_particles_to_die: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xc98ac215, original_name='ParticleSystem2WaitForParticlesToDie'
        ),
    })
    particle_system2_orientation: DebrisPropertiesOrientationEnum = dataclasses.field(default_factory=DebrisPropertiesOrientationEnum, metadata={
        'reflection': FieldReflection[DebrisPropertiesOrientationEnum](
            DebrisPropertiesOrientationEnum, id=0x3ce95d9d, original_name='ParticleSystem2Orientation', from_json=DebrisPropertiesOrientationEnum.from_json, to_json=DebrisPropertiesOrientationEnum.to_json
        ),
    })
    is_collider: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x2c7b18dd, original_name='IsCollider'
        ),
    })
    collide_with_ai_block: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xe73b9eb0, original_name='CollideWithAiBlock'
        ),
    })
    is_shootable: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x8c73cb7c, original_name='IsShootable'
        ),
    })
    touch_bounds_scalar: Vector = dataclasses.field(default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x0e8a3f95, original_name='TouchBoundsScalar', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    die_on_collision: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x0d7fad55, original_name='DieOnCollision'
        ),
    })
    flicker_on_fade_out: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xbfd82a19, original_name='FlickerOnFadeOut'
        ),
    })
    use_cached_collision_geometry: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x723d42d6, original_name='UseCachedCollisionGeometry'
        ),
    })
    do_not_delete_attached_object: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x4edb1d0e, original_name='DoNotDeleteAttachedObject'
        ),
    })
    delete_debris_on_attached_object_deletion: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xbf496273, original_name='DeleteDebrisOnAttachedObjectDeletion'
        ),
    })
    dragged_objects_use_debris_orientation: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xf83c1c1f, original_name='DraggedObjectsUseDebrisOrientation'
        ),
    })
    recenter_model_pivot: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x88b1af46, original_name='RecenterModelPivot'
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
        if property_count != 59:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5c3c4a57
        cone_spread_yaw = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa79fc55f
        cone_spread_pitch = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x01a0dfe6
        initial_direction = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xef90f09d
        position_offset = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc4b1e6a1
        transform_position_offset = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0185263e
        minimum_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x140ef2cc
        maximum_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf78c8ac7
        minimum_spin_speed = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb69bb541
        maximum_spin_speed = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd6594622
        minimum_lifetime = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xff27bb3a
        maximum_lifetime = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6b571ba5
        disable_collision_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50051a17
        fade_in_end_percentage = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6353c409
        fade_out_start_percentage = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3a5634d8
        start_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7c6ebe98
        middle_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5af5867d
        end_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd79690b4
        color_add_from_start = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0145d02d
        color_add_to_end = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x886e7c9f
        scale_start_percentage = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x80c22a0a
        final_scale = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x417f4a91
        bounciness = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x16b72d49
        friction = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2f2ae3e5
        gravity = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x295f05b7
        disable_physics_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc27ffa8f
        model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xeedbb07e
        model_pivot_point = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf1925576
        bounce_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x991202c3
        max_bounce_sounds = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76c79503
        bounce_sound_volume_decay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x310dfac8
        bounce_sound_speed_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5e9f5215
        unknown_0x5e9f5215 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x39743618
        unknown_0x39743618 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33e0fbb4
        unknown_0x33e0fbb4 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe82e7ed7
        min_speed_for_collided_event = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x855ee21b
        min_time_between_collided_events = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x478d0aa3
        particle_system1 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19a6f71f
        particle_system1_scale = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3b03a01e
        particle_system1_uses_global_translation = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdb1fa61c
        particle_system1_uses_global_orientation = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3bdd2fed
        particle_system1_wait_for_particles_to_die = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf5dd4690
        particle_system1_orientation = DebrisPropertiesOrientationEnum.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc119780d
        particle_system2 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6e3825ef
        particle_system2_scale = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc9544de6
        particle_system2_uses_global_translation = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x29484be4
        particle_system2_uses_global_orientation = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc98ac215
        particle_system2_wait_for_particles_to_die = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3ce95d9d
        particle_system2_orientation = DebrisPropertiesOrientationEnum.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2c7b18dd
        is_collider = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe73b9eb0
        collide_with_ai_block = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8c73cb7c
        is_shootable = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0e8a3f95
        touch_bounds_scalar = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0d7fad55
        die_on_collision = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbfd82a19
        flicker_on_fade_out = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x723d42d6
        use_cached_collision_geometry = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4edb1d0e
        do_not_delete_attached_object = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbf496273
        delete_debris_on_attached_object_deletion = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf83c1c1f
        dragged_objects_use_debris_orientation = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x88b1af46
        recenter_model_pivot = structs.BIG_bool_.unpack(data.read(1))[0]
    
        return cls(cone_spread_yaw, cone_spread_pitch, initial_direction, position_offset, transform_position_offset, minimum_speed, maximum_speed, minimum_spin_speed, maximum_spin_speed, minimum_lifetime, maximum_lifetime, disable_collision_time, fade_in_end_percentage, fade_out_start_percentage, start_color, middle_color, end_color, color_add_from_start, color_add_to_end, scale_start_percentage, final_scale, bounciness, friction, gravity, disable_physics_threshold, model, model_pivot_point, bounce_sound, max_bounce_sounds, bounce_sound_volume_decay, bounce_sound_speed_threshold, unknown_0x5e9f5215, unknown_0x39743618, unknown_0x33e0fbb4, min_speed_for_collided_event, min_time_between_collided_events, particle_system1, particle_system1_scale, particle_system1_uses_global_translation, particle_system1_uses_global_orientation, particle_system1_wait_for_particles_to_die, particle_system1_orientation, particle_system2, particle_system2_scale, particle_system2_uses_global_translation, particle_system2_uses_global_orientation, particle_system2_wait_for_particles_to_die, particle_system2_orientation, is_collider, collide_with_ai_block, is_shootable, touch_bounds_scalar, die_on_collision, flicker_on_fade_out, use_cached_collision_geometry, do_not_delete_attached_object, delete_debris_on_attached_object_deletion, dragged_objects_use_debris_orientation, recenter_model_pivot)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00;')  # 59 properties

        data.write(b'\\<JW')  # 0x5c3c4a57
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.cone_spread_yaw))

        data.write(b'\xa7\x9f\xc5_')  # 0xa79fc55f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.cone_spread_pitch))

        data.write(b'\x01\xa0\xdf\xe6')  # 0x1a0dfe6
        data.write(b'\x00\x0c')  # size
        self.initial_direction.to_stream(data, game)

        data.write(b'\xef\x90\xf0\x9d')  # 0xef90f09d
        data.write(b'\x00\x0c')  # size
        self.position_offset.to_stream(data, game)

        data.write(b'\xc4\xb1\xe6\xa1')  # 0xc4b1e6a1
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.transform_position_offset))

        data.write(b'\x01\x85&>')  # 0x185263e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.minimum_speed))

        data.write(b'\x14\x0e\xf2\xcc')  # 0x140ef2cc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.maximum_speed))

        data.write(b'\xf7\x8c\x8a\xc7')  # 0xf78c8ac7
        data.write(b'\x00\x0c')  # size
        self.minimum_spin_speed.to_stream(data, game)

        data.write(b'\xb6\x9b\xb5A')  # 0xb69bb541
        data.write(b'\x00\x0c')  # size
        self.maximum_spin_speed.to_stream(data, game)

        data.write(b'\xd6YF"')  # 0xd6594622
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.minimum_lifetime))

        data.write(b"\xff'\xbb:")  # 0xff27bb3a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.maximum_lifetime))

        data.write(b'kW\x1b\xa5')  # 0x6b571ba5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.disable_collision_time))

        data.write(b'P\x05\x1a\x17')  # 0x50051a17
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fade_in_end_percentage))

        data.write(b'cS\xc4\t')  # 0x6353c409
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fade_out_start_percentage))

        data.write(b':V4\xd8')  # 0x3a5634d8
        data.write(b'\x00\x10')  # size
        self.start_color.to_stream(data, game)

        data.write(b'|n\xbe\x98')  # 0x7c6ebe98
        data.write(b'\x00\x10')  # size
        self.middle_color.to_stream(data, game)

        data.write(b'Z\xf5\x86}')  # 0x5af5867d
        data.write(b'\x00\x10')  # size
        self.end_color.to_stream(data, game)

        data.write(b'\xd7\x96\x90\xb4')  # 0xd79690b4
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.color_add_from_start))

        data.write(b'\x01E\xd0-')  # 0x145d02d
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.color_add_to_end))

        data.write(b'\x88n|\x9f')  # 0x886e7c9f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scale_start_percentage))

        data.write(b'\x80\xc2*\n')  # 0x80c22a0a
        data.write(b'\x00\x0c')  # size
        self.final_scale.to_stream(data, game)

        data.write(b'A\x7fJ\x91')  # 0x417f4a91
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.bounciness))

        data.write(b'\x16\xb7-I')  # 0x16b72d49
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.friction))

        data.write(b'/*\xe3\xe5')  # 0x2f2ae3e5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.gravity))

        data.write(b')_\x05\xb7')  # 0x295f05b7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.disable_physics_threshold))

        data.write(b'\xc2\x7f\xfa\x8f')  # 0xc27ffa8f
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.model))

        data.write(b'\xee\xdb\xb0~')  # 0xeedbb07e
        data.write(b'\x00\x0c')  # size
        self.model_pivot_point.to_stream(data, game)

        data.write(b'\xf1\x92Uv')  # 0xf1925576
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.bounce_sound))

        data.write(b'\x99\x12\x02\xc3')  # 0x991202c3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_bounce_sounds))

        data.write(b'v\xc7\x95\x03')  # 0x76c79503
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.bounce_sound_volume_decay))

        data.write(b'1\r\xfa\xc8')  # 0x310dfac8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.bounce_sound_speed_threshold))

        data.write(b'^\x9fR\x15')  # 0x5e9f5215
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5e9f5215))

        data.write(b'9t6\x18')  # 0x39743618
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x39743618))

        data.write(b'3\xe0\xfb\xb4')  # 0x33e0fbb4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x33e0fbb4))

        data.write(b'\xe8.~\xd7')  # 0xe82e7ed7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_speed_for_collided_event))

        data.write(b'\x85^\xe2\x1b')  # 0x855ee21b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_collided_events))

        data.write(b'G\x8d\n\xa3')  # 0x478d0aa3
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.particle_system1))

        data.write(b'\x19\xa6\xf7\x1f')  # 0x19a6f71f
        data.write(b'\x00\x0c')  # size
        self.particle_system1_scale.to_stream(data, game)

        data.write(b';\x03\xa0\x1e')  # 0x3b03a01e
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.particle_system1_uses_global_translation))

        data.write(b'\xdb\x1f\xa6\x1c')  # 0xdb1fa61c
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.particle_system1_uses_global_orientation))

        data.write(b';\xdd/\xed')  # 0x3bdd2fed
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.particle_system1_wait_for_particles_to_die))

        data.write(b'\xf5\xddF\x90')  # 0xf5dd4690
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.particle_system1_orientation.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc1\x19x\r')  # 0xc119780d
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.particle_system2))

        data.write(b'n8%\xef')  # 0x6e3825ef
        data.write(b'\x00\x0c')  # size
        self.particle_system2_scale.to_stream(data, game)

        data.write(b'\xc9TM\xe6')  # 0xc9544de6
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.particle_system2_uses_global_translation))

        data.write(b')HK\xe4')  # 0x29484be4
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.particle_system2_uses_global_orientation))

        data.write(b'\xc9\x8a\xc2\x15')  # 0xc98ac215
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.particle_system2_wait_for_particles_to_die))

        data.write(b'<\xe9]\x9d')  # 0x3ce95d9d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.particle_system2_orientation.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b',{\x18\xdd')  # 0x2c7b18dd
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_collider))

        data.write(b'\xe7;\x9e\xb0')  # 0xe73b9eb0
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.collide_with_ai_block))

        data.write(b'\x8cs\xcb|')  # 0x8c73cb7c
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_shootable))

        data.write(b'\x0e\x8a?\x95')  # 0xe8a3f95
        data.write(b'\x00\x0c')  # size
        self.touch_bounds_scalar.to_stream(data, game)

        data.write(b'\r\x7f\xadU')  # 0xd7fad55
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.die_on_collision))

        data.write(b'\xbf\xd8*\x19')  # 0xbfd82a19
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.flicker_on_fade_out))

        data.write(b'r=B\xd6')  # 0x723d42d6
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.use_cached_collision_geometry))

        data.write(b'N\xdb\x1d\x0e')  # 0x4edb1d0e
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.do_not_delete_attached_object))

        data.write(b'\xbfIbs')  # 0xbf496273
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.delete_debris_on_attached_object_deletion))

        data.write(b'\xf8<\x1c\x1f')  # 0xf83c1c1f
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.dragged_objects_use_debris_orientation))

        data.write(b'\x88\xb1\xafF')  # 0x88b1af46
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.recenter_model_pivot))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DebrisPropertiesJson", data)
        return cls(
            cone_spread_yaw=json_data['cone_spread_yaw'],
            cone_spread_pitch=json_data['cone_spread_pitch'],
            initial_direction=Vector.from_json(json_data['initial_direction']),
            position_offset=Vector.from_json(json_data['position_offset']),
            transform_position_offset=json_data['transform_position_offset'],
            minimum_speed=json_data['minimum_speed'],
            maximum_speed=json_data['maximum_speed'],
            minimum_spin_speed=Vector.from_json(json_data['minimum_spin_speed']),
            maximum_spin_speed=Vector.from_json(json_data['maximum_spin_speed']),
            minimum_lifetime=json_data['minimum_lifetime'],
            maximum_lifetime=json_data['maximum_lifetime'],
            disable_collision_time=json_data['disable_collision_time'],
            fade_in_end_percentage=json_data['fade_in_end_percentage'],
            fade_out_start_percentage=json_data['fade_out_start_percentage'],
            start_color=Color.from_json(json_data['start_color']),
            middle_color=Color.from_json(json_data['middle_color']),
            end_color=Color.from_json(json_data['end_color']),
            color_add_from_start=json_data['color_add_from_start'],
            color_add_to_end=json_data['color_add_to_end'],
            scale_start_percentage=json_data['scale_start_percentage'],
            final_scale=Vector.from_json(json_data['final_scale']),
            bounciness=json_data['bounciness'],
            friction=json_data['friction'],
            gravity=json_data['gravity'],
            disable_physics_threshold=json_data['disable_physics_threshold'],
            model=json_data['model'],
            model_pivot_point=Vector.from_json(json_data['model_pivot_point']),
            bounce_sound=json_data['bounce_sound'],
            max_bounce_sounds=json_data['max_bounce_sounds'],
            bounce_sound_volume_decay=json_data['bounce_sound_volume_decay'],
            bounce_sound_speed_threshold=json_data['bounce_sound_speed_threshold'],
            unknown_0x5e9f5215=json_data['unknown_0x5e9f5215'],
            unknown_0x39743618=json_data['unknown_0x39743618'],
            unknown_0x33e0fbb4=json_data['unknown_0x33e0fbb4'],
            min_speed_for_collided_event=json_data['min_speed_for_collided_event'],
            min_time_between_collided_events=json_data['min_time_between_collided_events'],
            particle_system1=json_data['particle_system1'],
            particle_system1_scale=Vector.from_json(json_data['particle_system1_scale']),
            particle_system1_uses_global_translation=json_data['particle_system1_uses_global_translation'],
            particle_system1_uses_global_orientation=json_data['particle_system1_uses_global_orientation'],
            particle_system1_wait_for_particles_to_die=json_data['particle_system1_wait_for_particles_to_die'],
            particle_system1_orientation=DebrisPropertiesOrientationEnum.from_json(json_data['particle_system1_orientation']),
            particle_system2=json_data['particle_system2'],
            particle_system2_scale=Vector.from_json(json_data['particle_system2_scale']),
            particle_system2_uses_global_translation=json_data['particle_system2_uses_global_translation'],
            particle_system2_uses_global_orientation=json_data['particle_system2_uses_global_orientation'],
            particle_system2_wait_for_particles_to_die=json_data['particle_system2_wait_for_particles_to_die'],
            particle_system2_orientation=DebrisPropertiesOrientationEnum.from_json(json_data['particle_system2_orientation']),
            is_collider=json_data['is_collider'],
            collide_with_ai_block=json_data['collide_with_ai_block'],
            is_shootable=json_data['is_shootable'],
            touch_bounds_scalar=Vector.from_json(json_data['touch_bounds_scalar']),
            die_on_collision=json_data['die_on_collision'],
            flicker_on_fade_out=json_data['flicker_on_fade_out'],
            use_cached_collision_geometry=json_data['use_cached_collision_geometry'],
            do_not_delete_attached_object=json_data['do_not_delete_attached_object'],
            delete_debris_on_attached_object_deletion=json_data['delete_debris_on_attached_object_deletion'],
            dragged_objects_use_debris_orientation=json_data['dragged_objects_use_debris_orientation'],
            recenter_model_pivot=json_data['recenter_model_pivot'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'cone_spread_yaw': self.cone_spread_yaw,
            'cone_spread_pitch': self.cone_spread_pitch,
            'initial_direction': self.initial_direction.to_json(),
            'position_offset': self.position_offset.to_json(),
            'transform_position_offset': self.transform_position_offset,
            'minimum_speed': self.minimum_speed,
            'maximum_speed': self.maximum_speed,
            'minimum_spin_speed': self.minimum_spin_speed.to_json(),
            'maximum_spin_speed': self.maximum_spin_speed.to_json(),
            'minimum_lifetime': self.minimum_lifetime,
            'maximum_lifetime': self.maximum_lifetime,
            'disable_collision_time': self.disable_collision_time,
            'fade_in_end_percentage': self.fade_in_end_percentage,
            'fade_out_start_percentage': self.fade_out_start_percentage,
            'start_color': self.start_color.to_json(),
            'middle_color': self.middle_color.to_json(),
            'end_color': self.end_color.to_json(),
            'color_add_from_start': self.color_add_from_start,
            'color_add_to_end': self.color_add_to_end,
            'scale_start_percentage': self.scale_start_percentage,
            'final_scale': self.final_scale.to_json(),
            'bounciness': self.bounciness,
            'friction': self.friction,
            'gravity': self.gravity,
            'disable_physics_threshold': self.disable_physics_threshold,
            'model': self.model,
            'model_pivot_point': self.model_pivot_point.to_json(),
            'bounce_sound': self.bounce_sound,
            'max_bounce_sounds': self.max_bounce_sounds,
            'bounce_sound_volume_decay': self.bounce_sound_volume_decay,
            'bounce_sound_speed_threshold': self.bounce_sound_speed_threshold,
            'unknown_0x5e9f5215': self.unknown_0x5e9f5215,
            'unknown_0x39743618': self.unknown_0x39743618,
            'unknown_0x33e0fbb4': self.unknown_0x33e0fbb4,
            'min_speed_for_collided_event': self.min_speed_for_collided_event,
            'min_time_between_collided_events': self.min_time_between_collided_events,
            'particle_system1': self.particle_system1,
            'particle_system1_scale': self.particle_system1_scale.to_json(),
            'particle_system1_uses_global_translation': self.particle_system1_uses_global_translation,
            'particle_system1_uses_global_orientation': self.particle_system1_uses_global_orientation,
            'particle_system1_wait_for_particles_to_die': self.particle_system1_wait_for_particles_to_die,
            'particle_system1_orientation': self.particle_system1_orientation.to_json(),
            'particle_system2': self.particle_system2,
            'particle_system2_scale': self.particle_system2_scale.to_json(),
            'particle_system2_uses_global_translation': self.particle_system2_uses_global_translation,
            'particle_system2_uses_global_orientation': self.particle_system2_uses_global_orientation,
            'particle_system2_wait_for_particles_to_die': self.particle_system2_wait_for_particles_to_die,
            'particle_system2_orientation': self.particle_system2_orientation.to_json(),
            'is_collider': self.is_collider,
            'collide_with_ai_block': self.collide_with_ai_block,
            'is_shootable': self.is_shootable,
            'touch_bounds_scalar': self.touch_bounds_scalar.to_json(),
            'die_on_collision': self.die_on_collision,
            'flicker_on_fade_out': self.flicker_on_fade_out,
            'use_cached_collision_geometry': self.use_cached_collision_geometry,
            'do_not_delete_attached_object': self.do_not_delete_attached_object,
            'delete_debris_on_attached_object_deletion': self.delete_debris_on_attached_object_deletion,
            'dragged_objects_use_debris_orientation': self.dragged_objects_use_debris_orientation,
            'recenter_model_pivot': self.recenter_model_pivot,
        }

    def _dependencies_for_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.model)

    def _dependencies_for_bounce_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.bounce_sound)

    def _dependencies_for_particle_system1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_system1)

    def _dependencies_for_particle_system2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.particle_system2)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_model, "model", "AssetId"),
            (self._dependencies_for_bounce_sound, "bounce_sound", "AssetId"),
            (self._dependencies_for_particle_system1, "particle_system1", "AssetId"),
            (self._dependencies_for_particle_system2, "particle_system2", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for DebrisProperties.{field_name} ({field_type}): {e}"
                )


def _decode_initial_direction(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_position_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_minimum_spin_speed(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_maximum_spin_speed(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_start_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_middle_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_end_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_final_scale(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_model_pivot_point(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_particle_system1_scale(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_particle_system1_orientation(data: typing.BinaryIO, game: Game, property_size: int) -> DebrisPropertiesOrientationEnum:
    return DebrisPropertiesOrientationEnum.from_stream(data, game, property_size)


def _decode_particle_system2_scale(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_particle_system2_orientation(data: typing.BinaryIO, game: Game, property_size: int) -> DebrisPropertiesOrientationEnum:
    return DebrisPropertiesOrientationEnum.from_stream(data, game, property_size)


def _decode_touch_bounds_scalar(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x5c3c4a57: ('cone_spread_yaw', structs.decode_BIG_f),
    0xa79fc55f: ('cone_spread_pitch', structs.decode_BIG_f),
    0x01a0dfe6: ('initial_direction', _decode_initial_direction),
    0xef90f09d: ('position_offset', _decode_position_offset),
    0xc4b1e6a1: ('transform_position_offset', structs.decode_BIG_bool_),
    0x0185263e: ('minimum_speed', structs.decode_BIG_f),
    0x140ef2cc: ('maximum_speed', structs.decode_BIG_f),
    0xf78c8ac7: ('minimum_spin_speed', _decode_minimum_spin_speed),
    0xb69bb541: ('maximum_spin_speed', _decode_maximum_spin_speed),
    0xd6594622: ('minimum_lifetime', structs.decode_BIG_f),
    0xff27bb3a: ('maximum_lifetime', structs.decode_BIG_f),
    0x6b571ba5: ('disable_collision_time', structs.decode_BIG_f),
    0x50051a17: ('fade_in_end_percentage', structs.decode_BIG_f),
    0x6353c409: ('fade_out_start_percentage', structs.decode_BIG_f),
    0x3a5634d8: ('start_color', _decode_start_color),
    0x7c6ebe98: ('middle_color', _decode_middle_color),
    0x5af5867d: ('end_color', _decode_end_color),
    0xd79690b4: ('color_add_from_start', structs.decode_BIG_bool_),
    0x0145d02d: ('color_add_to_end', structs.decode_BIG_bool_),
    0x886e7c9f: ('scale_start_percentage', structs.decode_BIG_f),
    0x80c22a0a: ('final_scale', _decode_final_scale),
    0x417f4a91: ('bounciness', structs.decode_BIG_f),
    0x16b72d49: ('friction', structs.decode_BIG_f),
    0x2f2ae3e5: ('gravity', structs.decode_BIG_f),
    0x295f05b7: ('disable_physics_threshold', structs.decode_BIG_f),
    0xc27ffa8f: ('model', structs.decode_BIG_Q),
    0xeedbb07e: ('model_pivot_point', _decode_model_pivot_point),
    0xf1925576: ('bounce_sound', structs.decode_BIG_Q),
    0x991202c3: ('max_bounce_sounds', structs.decode_BIG_l),
    0x76c79503: ('bounce_sound_volume_decay', structs.decode_BIG_f),
    0x310dfac8: ('bounce_sound_speed_threshold', structs.decode_BIG_f),
    0x5e9f5215: ('unknown_0x5e9f5215', structs.decode_BIG_f),
    0x39743618: ('unknown_0x39743618', structs.decode_BIG_f),
    0x33e0fbb4: ('unknown_0x33e0fbb4', structs.decode_BIG_f),
    0xe82e7ed7: ('min_speed_for_collided_event', structs.decode_BIG_f),
    0x855ee21b: ('min_time_between_collided_events', structs.decode_BIG_f),
    0x478d0aa3: ('particle_system1', structs.decode_BIG_Q),
    0x19a6f71f: ('particle_system1_scale', _decode_particle_system1_scale),
    0x3b03a01e: ('particle_system1_uses_global_translation', structs.decode_BIG_bool_),
    0xdb1fa61c: ('particle_system1_uses_global_orientation', structs.decode_BIG_bool_),
    0x3bdd2fed: ('particle_system1_wait_for_particles_to_die', structs.decode_BIG_bool_),
    0xf5dd4690: ('particle_system1_orientation', _decode_particle_system1_orientation),
    0xc119780d: ('particle_system2', structs.decode_BIG_Q),
    0x6e3825ef: ('particle_system2_scale', _decode_particle_system2_scale),
    0xc9544de6: ('particle_system2_uses_global_translation', structs.decode_BIG_bool_),
    0x29484be4: ('particle_system2_uses_global_orientation', structs.decode_BIG_bool_),
    0xc98ac215: ('particle_system2_wait_for_particles_to_die', structs.decode_BIG_bool_),
    0x3ce95d9d: ('particle_system2_orientation', _decode_particle_system2_orientation),
    0x2c7b18dd: ('is_collider', structs.decode_BIG_bool_),
    0xe73b9eb0: ('collide_with_ai_block', structs.decode_BIG_bool_),
    0x8c73cb7c: ('is_shootable', structs.decode_BIG_bool_),
    0x0e8a3f95: ('touch_bounds_scalar', _decode_touch_bounds_scalar),
    0x0d7fad55: ('die_on_collision', structs.decode_BIG_bool_),
    0xbfd82a19: ('flicker_on_fade_out', structs.decode_BIG_bool_),
    0x723d42d6: ('use_cached_collision_geometry', structs.decode_BIG_bool_),
    0x4edb1d0e: ('do_not_delete_attached_object', structs.decode_BIG_bool_),
    0xbf496273: ('delete_debris_on_attached_object_deletion', structs.decode_BIG_bool_),
    0xf83c1c1f: ('dragged_objects_use_debris_orientation', structs.decode_BIG_bool_),
    0x88b1af46: ('recenter_model_pivot', structs.decode_BIG_bool_),
}
