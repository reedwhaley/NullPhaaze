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
from retro_data_structures.properties.echoes.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.archetypes.PowerBombGuardianStageProperties import PowerBombGuardianStageProperties
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SporbBaseJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        min_time_between_attacks: float
        max_time_between_attacks: float
        min_time_between_shots: float
        max_time_between_shots: float
        min_shots_in_a_burst: int
        max_shots_in_a_burst: int
        shot_angle_variance: float
        attack_aim_offset: json_util.JsonValue
        tendril_particle_effect: int
        unknown_0x35557a83: float
        grabber_out_acceleration: float
        grabber_in_acceleration: float
        initial_grabber_out_speed: float
        initial_grabber_in_speed: float
        grabber_attach_time: float
        min_grabber_grab_time: float
        max_grabber_grab_time: float
        spit_force: float
        spit_damage: float
        grab_damage: float
        flail_damage: float
        min_grabber_grab_range: float
        max_grabber_grab_range: float
        is_power_bomb_guardian: bool
        power_bomb_projectile_particle_effect: int
        power_bomb_projectile_damage: json_util.JsonObject
        max_power_bomb_projectile_height: float
        power_bomb_projectile_fuse_time: float
        power_bomb_projectile_start_damage_time: float
        power_bomb_projectile_end_damage_time: float
        power_bomb_projectile_damage_wait_time: float
        power_bomb_projectile_sound: int
        unknown_0x48df4182: float
        unknown_0xe39482ad: float
        unknown_0xdd8502cc: float
        unknown_0x4ab8cf7d: float
        unknown_0xf5e28404: float
        grabber_fire_sound: int
        grabber_flight_sound: int
        grabber_hit_player_sound: int
        grabber_hit_world_sound: int
        grabber_retract_sound: int
        grabber_retract_missed_player_sound: int
        morphball_spit_sound: int
        grabber_explosion_sound: int
        ball_escape_sound: int
        needle_telegraph_sound: int
        grabber_telegraph_sound: int
        stage1_data: json_util.JsonObject
        stage2_data: json_util.JsonObject
        stage3_data: json_util.JsonObject
        stage4_data: json_util.JsonObject
    

@dataclasses.dataclass()
class SporbBase(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    patterned: PatternedAITypedef = dataclasses.field(default_factory=PatternedAITypedef, metadata={
        'reflection': FieldReflection[PatternedAITypedef](
            PatternedAITypedef, id=0xb3774750, original_name='Patterned', from_json=PatternedAITypedef.from_json, to_json=PatternedAITypedef.to_json
        ),
    })
    actor_information: ActorParameters = dataclasses.field(default_factory=ActorParameters, metadata={
        'reflection': FieldReflection[ActorParameters](
            ActorParameters, id=0x7e397fed, original_name='ActorInformation', from_json=ActorParameters.from_json, to_json=ActorParameters.to_json
        ),
    })
    min_time_between_attacks: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x95e7a2c2, original_name='MinTimeBetweenAttacks'
        ),
    })
    max_time_between_attacks: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x76ba1c18, original_name='MaxTimeBetweenAttacks'
        ),
    })
    min_time_between_shots: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3eb2de35, original_name='MinTimeBetweenShots'
        ),
    })
    max_time_between_shots: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe50d8dd2, original_name='MaxTimeBetweenShots'
        ),
    })
    min_shots_in_a_burst: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x64d482d5, original_name='MinShotsInABurst'
        ),
    })
    max_shots_in_a_burst: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0xc3e002ac, original_name='MaxShotsInABurst'
        ),
    })
    shot_angle_variance: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd75f9cf2, original_name='ShotAngleVariance'
        ),
    })
    attack_aim_offset: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x540c1f87, original_name='AttackAimOffset', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    tendril_particle_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x33868c8f, original_name='TendrilParticleEffect'
        ),
    })
    unknown_0x35557a83: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x35557a83, original_name='Unknown'
        ),
    })
    grabber_out_acceleration: float = dataclasses.field(default=-10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x23bd3943, original_name='GrabberOutAcceleration'
        ),
    })
    grabber_in_acceleration: float = dataclasses.field(default=-100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd92f485d, original_name='GrabberInAcceleration'
        ),
    })
    initial_grabber_out_speed: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbfddabd4, original_name='InitialGrabberOutSpeed'
        ),
    })
    initial_grabber_in_speed: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x62bfaa35, original_name='InitialGrabberInSpeed'
        ),
    })
    grabber_attach_time: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x433b5e30, original_name='GrabberAttachTime'
        ),
    })
    min_grabber_grab_time: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xed82c56a, original_name='MinGrabberGrabTime'
        ),
    })
    max_grabber_grab_time: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe918f440, original_name='MaxGrabberGrabTime'
        ),
    })
    spit_force: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2731ad74, original_name='SpitForce'
        ),
    })
    spit_damage: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x03fb2dd4, original_name='SpitDamage'
        ),
    })
    grab_damage: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x95ad8824, original_name='GrabDamage'
        ),
    })
    flail_damage: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2cfade2c, original_name='FlailDamage'
        ),
    })
    min_grabber_grab_range: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb68e75cc, original_name='MinGrabberGrabRange'
        ),
    })
    max_grabber_grab_range: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6d31262b, original_name='MaxGrabberGrabRange'
        ),
    })
    is_power_bomb_guardian: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xb628855a, original_name='IsPowerBombGuardian'
        ),
    })
    power_bomb_projectile_particle_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x990745dd, original_name='PowerBombProjectileParticleEffect'
        ),
    })
    power_bomb_projectile_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x5f3c27c6, original_name='PowerBombProjectileDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    max_power_bomb_projectile_height: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x03a76d35, original_name='MaxPowerBombProjectileHeight'
        ),
    })
    power_bomb_projectile_fuse_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6d4e0f5a, original_name='PowerBombProjectileFuseTime'
        ),
    })
    power_bomb_projectile_start_damage_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3538d49b, original_name='PowerBombProjectileStartDamageTime'
        ),
    })
    power_bomb_projectile_end_damage_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe89c7707, original_name='PowerBombProjectileEndDamageTime'
        ),
    })
    power_bomb_projectile_damage_wait_time: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x738d1f51, original_name='PowerBombProjectileDamageWaitTime'
        ),
    })
    power_bomb_projectile_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x9480c6d7, original_name='PowerBombProjectileSound'
        ),
    })
    unknown_0x48df4182: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x48df4182, original_name='Unknown'
        ),
    })
    unknown_0xe39482ad: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe39482ad, original_name='Unknown'
        ),
    })
    unknown_0xdd8502cc: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdd8502cc, original_name='Unknown'
        ),
    })
    unknown_0x4ab8cf7d: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4ab8cf7d, original_name='Unknown'
        ),
    })
    unknown_0xf5e28404: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf5e28404, original_name='Unknown'
        ),
    })
    grabber_fire_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xa87d72fc, original_name='GrabberFireSound'
        ),
    })
    grabber_flight_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x8661285e, original_name='GrabberFlightSound'
        ),
    })
    grabber_hit_player_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x4123323a, original_name='GrabberHitPlayerSound'
        ),
    })
    grabber_hit_world_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x4d2ec538, original_name='GrabberHitWorldSound'
        ),
    })
    grabber_retract_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xd51ca051, original_name='GrabberRetractSound'
        ),
    })
    grabber_retract_missed_player_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x64e9152d, original_name='GrabberRetractMissedPlayerSound'
        ),
    })
    morphball_spit_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x3acd0ecc, original_name='MorphballSpitSound'
        ),
    })
    grabber_explosion_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xfeb67317, original_name='GrabberExplosionSound'
        ),
    })
    ball_escape_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x88a20db0, original_name='BallEscapeSound'
        ),
    })
    needle_telegraph_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x95c1257f, original_name='NeedleTelegraphSound'
        ),
    })
    grabber_telegraph_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x2690e216, original_name='GrabberTelegraphSound'
        ),
    })
    stage1_data: PowerBombGuardianStageProperties = dataclasses.field(default_factory=PowerBombGuardianStageProperties, metadata={
        'reflection': FieldReflection[PowerBombGuardianStageProperties](
            PowerBombGuardianStageProperties, id=0x510dba97, original_name='Stage1Data', from_json=PowerBombGuardianStageProperties.from_json, to_json=PowerBombGuardianStageProperties.to_json
        ),
    })
    stage2_data: PowerBombGuardianStageProperties = dataclasses.field(default_factory=PowerBombGuardianStageProperties, metadata={
        'reflection': FieldReflection[PowerBombGuardianStageProperties](
            PowerBombGuardianStageProperties, id=0x0b6c85f7, original_name='Stage2Data', from_json=PowerBombGuardianStageProperties.from_json, to_json=PowerBombGuardianStageProperties.to_json
        ),
    })
    stage3_data: PowerBombGuardianStageProperties = dataclasses.field(default_factory=PowerBombGuardianStageProperties, metadata={
        'reflection': FieldReflection[PowerBombGuardianStageProperties](
            PowerBombGuardianStageProperties, id=0x8b9c92e8, original_name='Stage3Data', from_json=PowerBombGuardianStageProperties.from_json, to_json=PowerBombGuardianStageProperties.to_json
        ),
    })
    stage4_data: PowerBombGuardianStageProperties = dataclasses.field(default_factory=PowerBombGuardianStageProperties, metadata={
        'reflection': FieldReflection[PowerBombGuardianStageProperties](
            PowerBombGuardianStageProperties, id=0xbfaefb37, original_name='Stage4Data', from_json=PowerBombGuardianStageProperties.from_json, to_json=PowerBombGuardianStageProperties.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'SPBB'

    @classmethod
    def modules(cls) -> list[str]:
        return ['Sporb.rel']

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
        if property_count != 55:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95e7a2c2
        min_time_between_attacks = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76ba1c18
        max_time_between_attacks = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3eb2de35
        min_time_between_shots = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe50d8dd2
        max_time_between_shots = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64d482d5
        min_shots_in_a_burst = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc3e002ac
        max_shots_in_a_burst = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd75f9cf2
        shot_angle_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x540c1f87
        attack_aim_offset = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33868c8f
        tendril_particle_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x35557a83
        unknown_0x35557a83 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23bd3943
        grabber_out_acceleration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd92f485d
        grabber_in_acceleration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbfddabd4
        initial_grabber_out_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x62bfaa35
        initial_grabber_in_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x433b5e30
        grabber_attach_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed82c56a
        min_grabber_grab_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe918f440
        max_grabber_grab_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2731ad74
        spit_force = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03fb2dd4
        spit_damage = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95ad8824
        grab_damage = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2cfade2c
        flail_damage = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb68e75cc
        min_grabber_grab_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6d31262b
        max_grabber_grab_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb628855a
        is_power_bomb_guardian = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x990745dd
        power_bomb_projectile_particle_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5f3c27c6
        power_bomb_projectile_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0, 'di_knock_back_power': 2.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03a76d35
        max_power_bomb_projectile_height = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6d4e0f5a
        power_bomb_projectile_fuse_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3538d49b
        power_bomb_projectile_start_damage_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe89c7707
        power_bomb_projectile_end_damage_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x738d1f51
        power_bomb_projectile_damage_wait_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9480c6d7
        power_bomb_projectile_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x48df4182
        unknown_0x48df4182 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe39482ad
        unknown_0xe39482ad = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdd8502cc
        unknown_0xdd8502cc = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4ab8cf7d
        unknown_0x4ab8cf7d = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf5e28404
        unknown_0xf5e28404 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa87d72fc
        grabber_fire_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8661285e
        grabber_flight_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4123323a
        grabber_hit_player_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4d2ec538
        grabber_hit_world_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd51ca051
        grabber_retract_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64e9152d
        grabber_retract_missed_player_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3acd0ecc
        morphball_spit_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfeb67317
        grabber_explosion_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x88a20db0
        ball_escape_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95c1257f
        needle_telegraph_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2690e216
        grabber_telegraph_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x510dba97
        stage1_data = PowerBombGuardianStageProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0b6c85f7
        stage2_data = PowerBombGuardianStageProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8b9c92e8
        stage3_data = PowerBombGuardianStageProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbfaefb37
        stage4_data = PowerBombGuardianStageProperties.from_stream(data, game, property_size)
    
        return cls(editor_properties, patterned, actor_information, min_time_between_attacks, max_time_between_attacks, min_time_between_shots, max_time_between_shots, min_shots_in_a_burst, max_shots_in_a_burst, shot_angle_variance, attack_aim_offset, tendril_particle_effect, unknown_0x35557a83, grabber_out_acceleration, grabber_in_acceleration, initial_grabber_out_speed, initial_grabber_in_speed, grabber_attach_time, min_grabber_grab_time, max_grabber_grab_time, spit_force, spit_damage, grab_damage, flail_damage, min_grabber_grab_range, max_grabber_grab_range, is_power_bomb_guardian, power_bomb_projectile_particle_effect, power_bomb_projectile_damage, max_power_bomb_projectile_height, power_bomb_projectile_fuse_time, power_bomb_projectile_start_damage_time, power_bomb_projectile_end_damage_time, power_bomb_projectile_damage_wait_time, power_bomb_projectile_sound, unknown_0x48df4182, unknown_0xe39482ad, unknown_0xdd8502cc, unknown_0x4ab8cf7d, unknown_0xf5e28404, grabber_fire_sound, grabber_flight_sound, grabber_hit_player_sound, grabber_hit_world_sound, grabber_retract_sound, grabber_retract_missed_player_sound, morphball_spit_sound, grabber_explosion_sound, ball_escape_sound, needle_telegraph_sound, grabber_telegraph_sound, stage1_data, stage2_data, stage3_data, stage4_data)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x007')  # 55 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game, default_override={'misc_flags': 3})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb3wGP')  # 0xb3774750
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.patterned.to_stream(data, game)
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

        data.write(b'\x95\xe7\xa2\xc2')  # 0x95e7a2c2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_attacks))

        data.write(b'v\xba\x1c\x18')  # 0x76ba1c18
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_time_between_attacks))

        data.write(b'>\xb2\xde5')  # 0x3eb2de35
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_shots))

        data.write(b'\xe5\r\x8d\xd2')  # 0xe50d8dd2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_time_between_shots))

        data.write(b'd\xd4\x82\xd5')  # 0x64d482d5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.min_shots_in_a_burst))

        data.write(b'\xc3\xe0\x02\xac')  # 0xc3e002ac
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_shots_in_a_burst))

        data.write(b'\xd7_\x9c\xf2')  # 0xd75f9cf2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.shot_angle_variance))

        data.write(b'T\x0c\x1f\x87')  # 0x540c1f87
        data.write(b'\x00\x0c')  # size
        self.attack_aim_offset.to_stream(data, game)

        data.write(b'3\x86\x8c\x8f')  # 0x33868c8f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.tendril_particle_effect))

        data.write(b'5Uz\x83')  # 0x35557a83
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x35557a83))

        data.write(b'#\xbd9C')  # 0x23bd3943
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grabber_out_acceleration))

        data.write(b'\xd9/H]')  # 0xd92f485d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grabber_in_acceleration))

        data.write(b'\xbf\xdd\xab\xd4')  # 0xbfddabd4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.initial_grabber_out_speed))

        data.write(b'b\xbf\xaa5')  # 0x62bfaa35
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.initial_grabber_in_speed))

        data.write(b'C;^0')  # 0x433b5e30
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grabber_attach_time))

        data.write(b'\xed\x82\xc5j')  # 0xed82c56a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_grabber_grab_time))

        data.write(b'\xe9\x18\xf4@')  # 0xe918f440
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_grabber_grab_time))

        data.write(b"'1\xadt")  # 0x2731ad74
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.spit_force))

        data.write(b'\x03\xfb-\xd4')  # 0x3fb2dd4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.spit_damage))

        data.write(b'\x95\xad\x88$')  # 0x95ad8824
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grab_damage))

        data.write(b',\xfa\xde,')  # 0x2cfade2c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flail_damage))

        data.write(b'\xb6\x8eu\xcc')  # 0xb68e75cc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_grabber_grab_range))

        data.write(b'm1&+')  # 0x6d31262b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_grabber_grab_range))

        data.write(b'\xb6(\x85Z')  # 0xb628855a
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_power_bomb_guardian))

        data.write(b'\x99\x07E\xdd')  # 0x990745dd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.power_bomb_projectile_particle_effect))

        data.write(b"_<'\xc6")  # 0x5f3c27c6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.power_bomb_projectile_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 5.0, 'di_knock_back_power': 2.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x03\xa7m5')  # 0x3a76d35
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_power_bomb_projectile_height))

        data.write(b'mN\x0fZ')  # 0x6d4e0f5a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.power_bomb_projectile_fuse_time))

        data.write(b'58\xd4\x9b')  # 0x3538d49b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.power_bomb_projectile_start_damage_time))

        data.write(b'\xe8\x9cw\x07')  # 0xe89c7707
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.power_bomb_projectile_end_damage_time))

        data.write(b's\x8d\x1fQ')  # 0x738d1f51
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.power_bomb_projectile_damage_wait_time))

        data.write(b'\x94\x80\xc6\xd7')  # 0x9480c6d7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.power_bomb_projectile_sound))

        data.write(b'H\xdfA\x82')  # 0x48df4182
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x48df4182))

        data.write(b'\xe3\x94\x82\xad')  # 0xe39482ad
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe39482ad))

        data.write(b'\xdd\x85\x02\xcc')  # 0xdd8502cc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xdd8502cc))

        data.write(b'J\xb8\xcf}')  # 0x4ab8cf7d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4ab8cf7d))

        data.write(b'\xf5\xe2\x84\x04')  # 0xf5e28404
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf5e28404))

        data.write(b'\xa8}r\xfc')  # 0xa87d72fc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.grabber_fire_sound))

        data.write(b'\x86a(^')  # 0x8661285e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.grabber_flight_sound))

        data.write(b'A#2:')  # 0x4123323a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.grabber_hit_player_sound))

        data.write(b'M.\xc58')  # 0x4d2ec538
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.grabber_hit_world_sound))

        data.write(b'\xd5\x1c\xa0Q')  # 0xd51ca051
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.grabber_retract_sound))

        data.write(b'd\xe9\x15-')  # 0x64e9152d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.grabber_retract_missed_player_sound))

        data.write(b':\xcd\x0e\xcc')  # 0x3acd0ecc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.morphball_spit_sound))

        data.write(b'\xfe\xb6s\x17')  # 0xfeb67317
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.grabber_explosion_sound))

        data.write(b'\x88\xa2\r\xb0')  # 0x88a20db0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.ball_escape_sound))

        data.write(b'\x95\xc1%\x7f')  # 0x95c1257f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.needle_telegraph_sound))

        data.write(b'&\x90\xe2\x16')  # 0x2690e216
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.grabber_telegraph_sound))

        data.write(b'Q\r\xba\x97')  # 0x510dba97
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stage1_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x0bl\x85\xf7')  # 0xb6c85f7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stage2_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8b\x9c\x92\xe8')  # 0x8b9c92e8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stage3_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbf\xae\xfb7')  # 0xbfaefb37
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stage4_data.to_stream(data, game)
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
        json_data = typing.cast("SporbBaseJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            patterned=PatternedAITypedef.from_json(json_data['patterned']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
            min_time_between_attacks=json_data['min_time_between_attacks'],
            max_time_between_attacks=json_data['max_time_between_attacks'],
            min_time_between_shots=json_data['min_time_between_shots'],
            max_time_between_shots=json_data['max_time_between_shots'],
            min_shots_in_a_burst=json_data['min_shots_in_a_burst'],
            max_shots_in_a_burst=json_data['max_shots_in_a_burst'],
            shot_angle_variance=json_data['shot_angle_variance'],
            attack_aim_offset=Vector.from_json(json_data['attack_aim_offset']),
            tendril_particle_effect=json_data['tendril_particle_effect'],
            unknown_0x35557a83=json_data['unknown_0x35557a83'],
            grabber_out_acceleration=json_data['grabber_out_acceleration'],
            grabber_in_acceleration=json_data['grabber_in_acceleration'],
            initial_grabber_out_speed=json_data['initial_grabber_out_speed'],
            initial_grabber_in_speed=json_data['initial_grabber_in_speed'],
            grabber_attach_time=json_data['grabber_attach_time'],
            min_grabber_grab_time=json_data['min_grabber_grab_time'],
            max_grabber_grab_time=json_data['max_grabber_grab_time'],
            spit_force=json_data['spit_force'],
            spit_damage=json_data['spit_damage'],
            grab_damage=json_data['grab_damage'],
            flail_damage=json_data['flail_damage'],
            min_grabber_grab_range=json_data['min_grabber_grab_range'],
            max_grabber_grab_range=json_data['max_grabber_grab_range'],
            is_power_bomb_guardian=json_data['is_power_bomb_guardian'],
            power_bomb_projectile_particle_effect=json_data['power_bomb_projectile_particle_effect'],
            power_bomb_projectile_damage=DamageInfo.from_json(json_data['power_bomb_projectile_damage']),
            max_power_bomb_projectile_height=json_data['max_power_bomb_projectile_height'],
            power_bomb_projectile_fuse_time=json_data['power_bomb_projectile_fuse_time'],
            power_bomb_projectile_start_damage_time=json_data['power_bomb_projectile_start_damage_time'],
            power_bomb_projectile_end_damage_time=json_data['power_bomb_projectile_end_damage_time'],
            power_bomb_projectile_damage_wait_time=json_data['power_bomb_projectile_damage_wait_time'],
            power_bomb_projectile_sound=json_data['power_bomb_projectile_sound'],
            unknown_0x48df4182=json_data['unknown_0x48df4182'],
            unknown_0xe39482ad=json_data['unknown_0xe39482ad'],
            unknown_0xdd8502cc=json_data['unknown_0xdd8502cc'],
            unknown_0x4ab8cf7d=json_data['unknown_0x4ab8cf7d'],
            unknown_0xf5e28404=json_data['unknown_0xf5e28404'],
            grabber_fire_sound=json_data['grabber_fire_sound'],
            grabber_flight_sound=json_data['grabber_flight_sound'],
            grabber_hit_player_sound=json_data['grabber_hit_player_sound'],
            grabber_hit_world_sound=json_data['grabber_hit_world_sound'],
            grabber_retract_sound=json_data['grabber_retract_sound'],
            grabber_retract_missed_player_sound=json_data['grabber_retract_missed_player_sound'],
            morphball_spit_sound=json_data['morphball_spit_sound'],
            grabber_explosion_sound=json_data['grabber_explosion_sound'],
            ball_escape_sound=json_data['ball_escape_sound'],
            needle_telegraph_sound=json_data['needle_telegraph_sound'],
            grabber_telegraph_sound=json_data['grabber_telegraph_sound'],
            stage1_data=PowerBombGuardianStageProperties.from_json(json_data['stage1_data']),
            stage2_data=PowerBombGuardianStageProperties.from_json(json_data['stage2_data']),
            stage3_data=PowerBombGuardianStageProperties.from_json(json_data['stage3_data']),
            stage4_data=PowerBombGuardianStageProperties.from_json(json_data['stage4_data']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'patterned': self.patterned.to_json(),
            'actor_information': self.actor_information.to_json(),
            'min_time_between_attacks': self.min_time_between_attacks,
            'max_time_between_attacks': self.max_time_between_attacks,
            'min_time_between_shots': self.min_time_between_shots,
            'max_time_between_shots': self.max_time_between_shots,
            'min_shots_in_a_burst': self.min_shots_in_a_burst,
            'max_shots_in_a_burst': self.max_shots_in_a_burst,
            'shot_angle_variance': self.shot_angle_variance,
            'attack_aim_offset': self.attack_aim_offset.to_json(),
            'tendril_particle_effect': self.tendril_particle_effect,
            'unknown_0x35557a83': self.unknown_0x35557a83,
            'grabber_out_acceleration': self.grabber_out_acceleration,
            'grabber_in_acceleration': self.grabber_in_acceleration,
            'initial_grabber_out_speed': self.initial_grabber_out_speed,
            'initial_grabber_in_speed': self.initial_grabber_in_speed,
            'grabber_attach_time': self.grabber_attach_time,
            'min_grabber_grab_time': self.min_grabber_grab_time,
            'max_grabber_grab_time': self.max_grabber_grab_time,
            'spit_force': self.spit_force,
            'spit_damage': self.spit_damage,
            'grab_damage': self.grab_damage,
            'flail_damage': self.flail_damage,
            'min_grabber_grab_range': self.min_grabber_grab_range,
            'max_grabber_grab_range': self.max_grabber_grab_range,
            'is_power_bomb_guardian': self.is_power_bomb_guardian,
            'power_bomb_projectile_particle_effect': self.power_bomb_projectile_particle_effect,
            'power_bomb_projectile_damage': self.power_bomb_projectile_damage.to_json(),
            'max_power_bomb_projectile_height': self.max_power_bomb_projectile_height,
            'power_bomb_projectile_fuse_time': self.power_bomb_projectile_fuse_time,
            'power_bomb_projectile_start_damage_time': self.power_bomb_projectile_start_damage_time,
            'power_bomb_projectile_end_damage_time': self.power_bomb_projectile_end_damage_time,
            'power_bomb_projectile_damage_wait_time': self.power_bomb_projectile_damage_wait_time,
            'power_bomb_projectile_sound': self.power_bomb_projectile_sound,
            'unknown_0x48df4182': self.unknown_0x48df4182,
            'unknown_0xe39482ad': self.unknown_0xe39482ad,
            'unknown_0xdd8502cc': self.unknown_0xdd8502cc,
            'unknown_0x4ab8cf7d': self.unknown_0x4ab8cf7d,
            'unknown_0xf5e28404': self.unknown_0xf5e28404,
            'grabber_fire_sound': self.grabber_fire_sound,
            'grabber_flight_sound': self.grabber_flight_sound,
            'grabber_hit_player_sound': self.grabber_hit_player_sound,
            'grabber_hit_world_sound': self.grabber_hit_world_sound,
            'grabber_retract_sound': self.grabber_retract_sound,
            'grabber_retract_missed_player_sound': self.grabber_retract_missed_player_sound,
            'morphball_spit_sound': self.morphball_spit_sound,
            'grabber_explosion_sound': self.grabber_explosion_sound,
            'ball_escape_sound': self.ball_escape_sound,
            'needle_telegraph_sound': self.needle_telegraph_sound,
            'grabber_telegraph_sound': self.grabber_telegraph_sound,
            'stage1_data': self.stage1_data.to_json(),
            'stage2_data': self.stage2_data.to_json(),
            'stage3_data': self.stage3_data.to_json(),
            'stage4_data': self.stage4_data.to_json(),
        }

    def _dependencies_for_tendril_particle_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.tendril_particle_effect)

    def _dependencies_for_power_bomb_projectile_particle_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.power_bomb_projectile_particle_effect)

    def _dependencies_for_power_bomb_projectile_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.power_bomb_projectile_sound)

    def _dependencies_for_grabber_fire_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.grabber_fire_sound)

    def _dependencies_for_grabber_flight_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.grabber_flight_sound)

    def _dependencies_for_grabber_hit_player_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.grabber_hit_player_sound)

    def _dependencies_for_grabber_hit_world_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.grabber_hit_world_sound)

    def _dependencies_for_grabber_retract_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.grabber_retract_sound)

    def _dependencies_for_grabber_retract_missed_player_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.grabber_retract_missed_player_sound)

    def _dependencies_for_morphball_spit_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.morphball_spit_sound)

    def _dependencies_for_grabber_explosion_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.grabber_explosion_sound)

    def _dependencies_for_ball_escape_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.ball_escape_sound)

    def _dependencies_for_needle_telegraph_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.needle_telegraph_sound)

    def _dependencies_for_grabber_telegraph_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.grabber_telegraph_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_tendril_particle_effect, "tendril_particle_effect", "AssetId"),
            (self._dependencies_for_power_bomb_projectile_particle_effect, "power_bomb_projectile_particle_effect", "AssetId"),
            (self._dependencies_for_power_bomb_projectile_sound, "power_bomb_projectile_sound", "int"),
            (self._dependencies_for_grabber_fire_sound, "grabber_fire_sound", "int"),
            (self._dependencies_for_grabber_flight_sound, "grabber_flight_sound", "int"),
            (self._dependencies_for_grabber_hit_player_sound, "grabber_hit_player_sound", "int"),
            (self._dependencies_for_grabber_hit_world_sound, "grabber_hit_world_sound", "int"),
            (self._dependencies_for_grabber_retract_sound, "grabber_retract_sound", "int"),
            (self._dependencies_for_grabber_retract_missed_player_sound, "grabber_retract_missed_player_sound", "int"),
            (self._dependencies_for_morphball_spit_sound, "morphball_spit_sound", "int"),
            (self._dependencies_for_grabber_explosion_sound, "grabber_explosion_sound", "int"),
            (self._dependencies_for_ball_escape_sound, "ball_escape_sound", "int"),
            (self._dependencies_for_needle_telegraph_sound, "needle_telegraph_sound", "int"),
            (self._dependencies_for_grabber_telegraph_sound, "grabber_telegraph_sound", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for SporbBase.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_attack_aim_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_power_bomb_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0, 'di_knock_back_power': 2.0})


def _decode_stage1_data(data: typing.BinaryIO, game: Game, property_size: int) -> PowerBombGuardianStageProperties:
    return PowerBombGuardianStageProperties.from_stream(data, game, property_size)


def _decode_stage2_data(data: typing.BinaryIO, game: Game, property_size: int) -> PowerBombGuardianStageProperties:
    return PowerBombGuardianStageProperties.from_stream(data, game, property_size)


def _decode_stage3_data(data: typing.BinaryIO, game: Game, property_size: int) -> PowerBombGuardianStageProperties:
    return PowerBombGuardianStageProperties.from_stream(data, game, property_size)


def _decode_stage4_data(data: typing.BinaryIO, game: Game, property_size: int) -> PowerBombGuardianStageProperties:
    return PowerBombGuardianStageProperties.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xb3774750: ('patterned', _decode_patterned),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0x95e7a2c2: ('min_time_between_attacks', structs.decode_BIG_f),
    0x76ba1c18: ('max_time_between_attacks', structs.decode_BIG_f),
    0x3eb2de35: ('min_time_between_shots', structs.decode_BIG_f),
    0xe50d8dd2: ('max_time_between_shots', structs.decode_BIG_f),
    0x64d482d5: ('min_shots_in_a_burst', structs.decode_BIG_l),
    0xc3e002ac: ('max_shots_in_a_burst', structs.decode_BIG_l),
    0xd75f9cf2: ('shot_angle_variance', structs.decode_BIG_f),
    0x540c1f87: ('attack_aim_offset', _decode_attack_aim_offset),
    0x33868c8f: ('tendril_particle_effect', structs.decode_BIG_L),
    0x35557a83: ('unknown_0x35557a83', structs.decode_BIG_f),
    0x23bd3943: ('grabber_out_acceleration', structs.decode_BIG_f),
    0xd92f485d: ('grabber_in_acceleration', structs.decode_BIG_f),
    0xbfddabd4: ('initial_grabber_out_speed', structs.decode_BIG_f),
    0x62bfaa35: ('initial_grabber_in_speed', structs.decode_BIG_f),
    0x433b5e30: ('grabber_attach_time', structs.decode_BIG_f),
    0xed82c56a: ('min_grabber_grab_time', structs.decode_BIG_f),
    0xe918f440: ('max_grabber_grab_time', structs.decode_BIG_f),
    0x2731ad74: ('spit_force', structs.decode_BIG_f),
    0x03fb2dd4: ('spit_damage', structs.decode_BIG_f),
    0x95ad8824: ('grab_damage', structs.decode_BIG_f),
    0x2cfade2c: ('flail_damage', structs.decode_BIG_f),
    0xb68e75cc: ('min_grabber_grab_range', structs.decode_BIG_f),
    0x6d31262b: ('max_grabber_grab_range', structs.decode_BIG_f),
    0xb628855a: ('is_power_bomb_guardian', structs.decode_BIG_bool_),
    0x990745dd: ('power_bomb_projectile_particle_effect', structs.decode_BIG_L),
    0x5f3c27c6: ('power_bomb_projectile_damage', _decode_power_bomb_projectile_damage),
    0x03a76d35: ('max_power_bomb_projectile_height', structs.decode_BIG_f),
    0x6d4e0f5a: ('power_bomb_projectile_fuse_time', structs.decode_BIG_f),
    0x3538d49b: ('power_bomb_projectile_start_damage_time', structs.decode_BIG_f),
    0xe89c7707: ('power_bomb_projectile_end_damage_time', structs.decode_BIG_f),
    0x738d1f51: ('power_bomb_projectile_damage_wait_time', structs.decode_BIG_f),
    0x9480c6d7: ('power_bomb_projectile_sound', structs.decode_BIG_l),
    0x48df4182: ('unknown_0x48df4182', structs.decode_BIG_f),
    0xe39482ad: ('unknown_0xe39482ad', structs.decode_BIG_f),
    0xdd8502cc: ('unknown_0xdd8502cc', structs.decode_BIG_f),
    0x4ab8cf7d: ('unknown_0x4ab8cf7d', structs.decode_BIG_f),
    0xf5e28404: ('unknown_0xf5e28404', structs.decode_BIG_f),
    0xa87d72fc: ('grabber_fire_sound', structs.decode_BIG_l),
    0x8661285e: ('grabber_flight_sound', structs.decode_BIG_l),
    0x4123323a: ('grabber_hit_player_sound', structs.decode_BIG_l),
    0x4d2ec538: ('grabber_hit_world_sound', structs.decode_BIG_l),
    0xd51ca051: ('grabber_retract_sound', structs.decode_BIG_l),
    0x64e9152d: ('grabber_retract_missed_player_sound', structs.decode_BIG_l),
    0x3acd0ecc: ('morphball_spit_sound', structs.decode_BIG_l),
    0xfeb67317: ('grabber_explosion_sound', structs.decode_BIG_l),
    0x88a20db0: ('ball_escape_sound', structs.decode_BIG_l),
    0x95c1257f: ('needle_telegraph_sound', structs.decode_BIG_l),
    0x2690e216: ('grabber_telegraph_sound', structs.decode_BIG_l),
    0x510dba97: ('stage1_data', _decode_stage1_data),
    0x0b6c85f7: ('stage2_data', _decode_stage2_data),
    0x8b9c92e8: ('stage3_data', _decode_stage3_data),
    0xbfaefb37: ('stage4_data', _decode_stage4_data),
}
