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
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.LaunchProjectileData import LaunchProjectileData
from retro_data_structures.properties.corruption.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.corruption.archetypes.ShockWaveInfo import ShockWaveInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class BerserkerDataJson(typing_extensions.TypedDict):
        turn_threshold: float
        should_play_alert_animation: bool
        melee_attack_range: float
        uses_ball_slam: bool
        ball_slam_damage: json_util.JsonObject
        damage_info: json_util.JsonObject
        ground_pound_damage: json_util.JsonObject
        pirate_as_projectile_damage: json_util.JsonObject
        phazon_cannon_beam_info: json_util.JsonObject
        phazon_cannon_damage_info: json_util.JsonObject
        phazon_cannon_min_range: float
        phazon_cannon_max_range: float
        phazon_cannon_cone_limit: float
        phazon_cannon_track_speed: float
        phazon_breath_projectile: json_util.JsonObject
        phazon_breath_track_speed: float
        phazon_breath_min_range: float
        phazon_breath_max_range: float
        phazon_breath_cone_limit: float
        phazon_breath_size_spline: json_util.JsonObject
        phazon_breath_destroy_missile_cone_limit: float
        phazon_breath_destroy_missile_range: float
        phazon_breath_destroy_missile_time: float
        phazon_breath_missile_turn_time: float
        phazon_breath_missile_turn_rate: float
        phazon_grapple_min_range: float
        phazon_grapple_max_range: float
        phazon_grapple_time: float
        phazon_grapple_suck_force: float
        phazon_grapple_suck_distance: float
        phazon_grapple_damage: json_util.JsonObject
        phazon_grapple_spit_force: float
        unknown_0xbc2f8f30: float
        unknown_0x910ad1e0: float
        unknown_0x4566b3ef: float
        approach_player_chance: float
        unknown_0x24f779ca: float
        armored_vulnerability: json_util.JsonObject
        armor_health: float
        armor_model1: int
        armor_model2: int
        armor_model3: int
        armor_model4: int
        armor_model5: int
        armor_gone_speed_up: float
        weak_spot_model: int
        provoked_head_vulnerability: json_util.JsonObject
        energy_orb_min_range: float
        energy_orb_max_range: float
        energy_orb_lob_projectile: json_util.JsonObject
        energy_orb_reflected_projectile: json_util.JsonObject
        energy_orb_charge_projectile: json_util.JsonObject
        energy_orb_slow_projectile: json_util.JsonObject
        energy_orb_fiery_projectile: json_util.JsonObject
        unknown_0x15d26d26: float
        unknown_0x81eaa9d4: float
        is_gandrayda: bool
        is_chieftain: bool
        shoulder_vulnerability: json_util.JsonObject
        shoulder_health: float
        unknown_0x268e5cb2: float
        left_shoulder_model: int
        right_shoulder_model: int
        weak_spot_armored_vulnerability: json_util.JsonObject
        nova_shoot_through_vulnerability: json_util.JsonObject
        damage_vulnerability: json_util.JsonObject
        unknown_0xedf1189f: bool
        minor_shockwave: json_util.JsonObject
        major_shockwave: json_util.JsonObject
        unknown_0x0c1a5644: float
        unknown_0xc6af2fd0: float
    

@dataclasses.dataclass()
class BerserkerData(BaseProperty):
    turn_threshold: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc0ac271e, original_name='TurnThreshold'
        ),
    })
    should_play_alert_animation: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x76ebc21a, original_name='ShouldPlayAlertAnimation'
        ),
    })
    melee_attack_range: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc3e43d0e, original_name='MeleeAttackRange'
        ),
    })
    uses_ball_slam: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xc4db42e3, original_name='UsesBallSlam'
        ),
    })
    ball_slam_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x74bffa78, original_name='BallSlamDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    damage_info: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xbb7977b9, original_name='DamageInfo', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    ground_pound_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x4738c321, original_name='GroundPoundDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    pirate_as_projectile_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xf4e003c1, original_name='PirateAsProjectileDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    phazon_cannon_beam_info: PlasmaBeamInfo = dataclasses.field(default_factory=PlasmaBeamInfo, metadata={
        'reflection': FieldReflection[PlasmaBeamInfo](
            PlasmaBeamInfo, id=0xe0dbf22f, original_name='PhazonCannonBeamInfo', from_json=PlasmaBeamInfo.from_json, to_json=PlasmaBeamInfo.to_json
        ),
    })
    phazon_cannon_damage_info: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x97321af1, original_name='PhazonCannonDamageInfo', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    phazon_cannon_min_range: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfd5e7062, original_name='PhazonCannonMinRange'
        ),
    })
    phazon_cannon_max_range: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbd110814, original_name='PhazonCannonMaxRange'
        ),
    })
    phazon_cannon_cone_limit: float = dataclasses.field(default=45.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3d947337, original_name='PhazonCannonConeLimit'
        ),
    })
    phazon_cannon_track_speed: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1a975a02, original_name='PhazonCannonTrackSpeed'
        ),
    })
    phazon_breath_projectile: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0x066bc855, original_name='PhazonBreathProjectile', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    phazon_breath_track_speed: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x67e0e4b4, original_name='PhazonBreathTrackSpeed'
        ),
    })
    phazon_breath_min_range: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb7ad7067, original_name='PhazonBreathMinRange'
        ),
    })
    phazon_breath_max_range: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf7e20811, original_name='PhazonBreathMaxRange'
        ),
    })
    phazon_breath_cone_limit: float = dataclasses.field(default=45.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4db474b8, original_name='PhazonBreathConeLimit'
        ),
    })
    phazon_breath_size_spline: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x68d3daa4, original_name='PhazonBreathSizeSpline', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    phazon_breath_destroy_missile_cone_limit: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1b359207, original_name='PhazonBreathDestroyMissileConeLimit'
        ),
    })
    phazon_breath_destroy_missile_range: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc12f397a, original_name='PhazonBreathDestroyMissileRange'
        ),
    })
    phazon_breath_destroy_missile_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4bfee56b, original_name='PhazonBreathDestroyMissileTime'
        ),
    })
    phazon_breath_missile_turn_time: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8f3be6e1, original_name='PhazonBreathMissileTurnTime'
        ),
    })
    phazon_breath_missile_turn_rate: float = dataclasses.field(default=180.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdd825dc3, original_name='PhazonBreathMissileTurnRate'
        ),
    })
    phazon_grapple_min_range: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x869415a3, original_name='PhazonGrappleMinRange'
        ),
    })
    phazon_grapple_max_range: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc6db6dd5, original_name='PhazonGrappleMaxRange'
        ),
    })
    phazon_grapple_time: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdc8d7887, original_name='PhazonGrappleTime'
        ),
    })
    phazon_grapple_suck_force: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x58e6d9b8, original_name='PhazonGrappleSuckForce'
        ),
    })
    phazon_grapple_suck_distance: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcf111a99, original_name='PhazonGrappleSuckDistance'
        ),
    })
    phazon_grapple_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x719fd06b, original_name='PhazonGrappleDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    phazon_grapple_spit_force: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x92f0b2c7, original_name='PhazonGrappleSpitForce'
        ),
    })
    unknown_0xbc2f8f30: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbc2f8f30, original_name='Unknown'
        ),
    })
    unknown_0x910ad1e0: float = dataclasses.field(default=0.699999988079071, metadata={
        'reflection': FieldReflection[float](
            float, id=0x910ad1e0, original_name='Unknown'
        ),
    })
    unknown_0x4566b3ef: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4566b3ef, original_name='Unknown'
        ),
    })
    approach_player_chance: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6fe50d32, original_name='ApproachPlayerChance'
        ),
    })
    unknown_0x24f779ca: float = dataclasses.field(default=0.800000011920929, metadata={
        'reflection': FieldReflection[float](
            float, id=0x24f779ca, original_name='Unknown'
        ),
    })
    armored_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xc6ba9753, original_name='ArmoredVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    armor_health: float = dataclasses.field(default=500.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x83439084, original_name='ArmorHealth'
        ),
    })
    armor_model1: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x04547d34, original_name='ArmorModel1'
        ),
    })
    armor_model2: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x82c00f9a, original_name='ArmorModel2'
        ),
    })
    armor_model3: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x499cdc3f, original_name='ArmorModel3'
        ),
    })
    armor_model4: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5499ec87, original_name='ArmorModel4'
        ),
    })
    armor_model5: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x9fc53f22, original_name='ArmorModel5'
        ),
    })
    armor_gone_speed_up: float = dataclasses.field(default=1.399999976158142, metadata={
        'reflection': FieldReflection[float](
            float, id=0x09e8c7fd, original_name='ArmorGoneSpeedUp'
        ),
    })
    weak_spot_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x4ae57feb, original_name='WeakSpotModel'
        ),
    })
    provoked_head_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x4e1d71a1, original_name='ProvokedHeadVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    energy_orb_min_range: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x69d66ec4, original_name='EnergyOrbMinRange'
        ),
    })
    energy_orb_max_range: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x299916b2, original_name='EnergyOrbMaxRange'
        ),
    })
    energy_orb_lob_projectile: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0xfe51924e, original_name='EnergyOrbLobProjectile', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    energy_orb_reflected_projectile: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0x9b9c702c, original_name='EnergyOrbReflectedProjectile', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    energy_orb_charge_projectile: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0x567ba94a, original_name='EnergyOrbChargeProjectile', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    energy_orb_slow_projectile: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0xf4d5150f, original_name='EnergyOrbSlowProjectile', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    energy_orb_fiery_projectile: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0x8647c581, original_name='EnergyOrbFieryProjectile', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    unknown_0x15d26d26: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0x15d26d26, original_name='Unknown'
        ),
    })
    unknown_0x81eaa9d4: float = dataclasses.field(default=250.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x81eaa9d4, original_name='Unknown'
        ),
    })
    is_gandrayda: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x531a8c85, original_name='IsGandrayda'
        ),
    })
    is_chieftain: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x677bd8ab, original_name='IsChieftain'
        ),
    })
    shoulder_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xc6e6300f, original_name='ShoulderVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    shoulder_health: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1520568a, original_name='ShoulderHealth'
        ),
    })
    unknown_0x268e5cb2: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x268e5cb2, original_name='Unknown'
        ),
    })
    left_shoulder_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x650ba238, original_name='LeftShoulderModel'
        ),
    })
    right_shoulder_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x68865410, original_name='RightShoulderModel'
        ),
    })
    weak_spot_armored_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x342dae7a, original_name='WeakSpotArmoredVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    nova_shoot_through_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x200545bd, original_name='NovaShootThroughVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    damage_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xf3ea94dc, original_name='DamageVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    unknown_0xedf1189f: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xedf1189f, original_name='Unknown'
        ),
    })
    minor_shockwave: ShockWaveInfo = dataclasses.field(default_factory=ShockWaveInfo, metadata={
        'reflection': FieldReflection[ShockWaveInfo](
            ShockWaveInfo, id=0x846533cc, original_name='MinorShockwave', from_json=ShockWaveInfo.from_json, to_json=ShockWaveInfo.to_json
        ),
    })
    major_shockwave: ShockWaveInfo = dataclasses.field(default_factory=ShockWaveInfo, metadata={
        'reflection': FieldReflection[ShockWaveInfo](
            ShockWaveInfo, id=0x2af1548b, original_name='MajorShockwave', from_json=ShockWaveInfo.from_json, to_json=ShockWaveInfo.to_json
        ),
    })
    unknown_0x0c1a5644: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0c1a5644, original_name='Unknown'
        ),
    })
    unknown_0xc6af2fd0: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc6af2fd0, original_name='Unknown'
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
        if property_count != 71:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc0ac271e
        turn_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76ebc21a
        should_play_alert_animation = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc3e43d0e
        melee_attack_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc4db42e3
        uses_ball_slam = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x74bffa78
        ball_slam_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbb7977b9
        damage_info = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4738c321
        ground_pound_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf4e003c1
        pirate_as_projectile_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe0dbf22f
        phazon_cannon_beam_info = PlasmaBeamInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x97321af1
        phazon_cannon_damage_info = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfd5e7062
        phazon_cannon_min_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbd110814
        phazon_cannon_max_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3d947337
        phazon_cannon_cone_limit = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1a975a02
        phazon_cannon_track_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x066bc855
        phazon_breath_projectile = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x67e0e4b4
        phazon_breath_track_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb7ad7067
        phazon_breath_min_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf7e20811
        phazon_breath_max_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4db474b8
        phazon_breath_cone_limit = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68d3daa4
        phazon_breath_size_spline = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1b359207
        phazon_breath_destroy_missile_cone_limit = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc12f397a
        phazon_breath_destroy_missile_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4bfee56b
        phazon_breath_destroy_missile_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8f3be6e1
        phazon_breath_missile_turn_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdd825dc3
        phazon_breath_missile_turn_rate = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x869415a3
        phazon_grapple_min_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc6db6dd5
        phazon_grapple_max_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdc8d7887
        phazon_grapple_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58e6d9b8
        phazon_grapple_suck_force = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcf111a99
        phazon_grapple_suck_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x719fd06b
        phazon_grapple_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x92f0b2c7
        phazon_grapple_spit_force = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbc2f8f30
        unknown_0xbc2f8f30 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x910ad1e0
        unknown_0x910ad1e0 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4566b3ef
        unknown_0x4566b3ef = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6fe50d32
        approach_player_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24f779ca
        unknown_0x24f779ca = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc6ba9753
        armored_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x83439084
        armor_health = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x04547d34
        armor_model1 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x82c00f9a
        armor_model2 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x499cdc3f
        armor_model3 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5499ec87
        armor_model4 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9fc53f22
        armor_model5 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x09e8c7fd
        armor_gone_speed_up = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4ae57feb
        weak_spot_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4e1d71a1
        provoked_head_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x69d66ec4
        energy_orb_min_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x299916b2
        energy_orb_max_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfe51924e
        energy_orb_lob_projectile = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9b9c702c
        energy_orb_reflected_projectile = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x567ba94a
        energy_orb_charge_projectile = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf4d5150f
        energy_orb_slow_projectile = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8647c581
        energy_orb_fiery_projectile = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x15d26d26
        unknown_0x15d26d26 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x81eaa9d4
        unknown_0x81eaa9d4 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x531a8c85
        is_gandrayda = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x677bd8ab
        is_chieftain = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc6e6300f
        shoulder_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1520568a
        shoulder_health = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x268e5cb2
        unknown_0x268e5cb2 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x650ba238
        left_shoulder_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68865410
        right_shoulder_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x342dae7a
        weak_spot_armored_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x200545bd
        nova_shoot_through_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf3ea94dc
        damage_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xedf1189f
        unknown_0xedf1189f = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x846533cc
        minor_shockwave = ShockWaveInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2af1548b
        major_shockwave = ShockWaveInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0c1a5644
        unknown_0x0c1a5644 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc6af2fd0
        unknown_0xc6af2fd0 = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(turn_threshold, should_play_alert_animation, melee_attack_range, uses_ball_slam, ball_slam_damage, damage_info, ground_pound_damage, pirate_as_projectile_damage, phazon_cannon_beam_info, phazon_cannon_damage_info, phazon_cannon_min_range, phazon_cannon_max_range, phazon_cannon_cone_limit, phazon_cannon_track_speed, phazon_breath_projectile, phazon_breath_track_speed, phazon_breath_min_range, phazon_breath_max_range, phazon_breath_cone_limit, phazon_breath_size_spline, phazon_breath_destroy_missile_cone_limit, phazon_breath_destroy_missile_range, phazon_breath_destroy_missile_time, phazon_breath_missile_turn_time, phazon_breath_missile_turn_rate, phazon_grapple_min_range, phazon_grapple_max_range, phazon_grapple_time, phazon_grapple_suck_force, phazon_grapple_suck_distance, phazon_grapple_damage, phazon_grapple_spit_force, unknown_0xbc2f8f30, unknown_0x910ad1e0, unknown_0x4566b3ef, approach_player_chance, unknown_0x24f779ca, armored_vulnerability, armor_health, armor_model1, armor_model2, armor_model3, armor_model4, armor_model5, armor_gone_speed_up, weak_spot_model, provoked_head_vulnerability, energy_orb_min_range, energy_orb_max_range, energy_orb_lob_projectile, energy_orb_reflected_projectile, energy_orb_charge_projectile, energy_orb_slow_projectile, energy_orb_fiery_projectile, unknown_0x15d26d26, unknown_0x81eaa9d4, is_gandrayda, is_chieftain, shoulder_vulnerability, shoulder_health, unknown_0x268e5cb2, left_shoulder_model, right_shoulder_model, weak_spot_armored_vulnerability, nova_shoot_through_vulnerability, damage_vulnerability, unknown_0xedf1189f, minor_shockwave, major_shockwave, unknown_0x0c1a5644, unknown_0xc6af2fd0)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00G')  # 71 properties

        data.write(b"\xc0\xac'\x1e")  # 0xc0ac271e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.turn_threshold))

        data.write(b'v\xeb\xc2\x1a')  # 0x76ebc21a
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.should_play_alert_animation))

        data.write(b'\xc3\xe4=\x0e')  # 0xc3e43d0e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.melee_attack_range))

        data.write(b'\xc4\xdbB\xe3')  # 0xc4db42e3
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.uses_ball_slam))

        data.write(b't\xbf\xfax')  # 0x74bffa78
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ball_slam_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbbyw\xb9')  # 0xbb7977b9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'G8\xc3!')  # 0x4738c321
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ground_pound_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf4\xe0\x03\xc1')  # 0xf4e003c1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.pirate_as_projectile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe0\xdb\xf2/')  # 0xe0dbf22f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.phazon_cannon_beam_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x972\x1a\xf1')  # 0x97321af1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.phazon_cannon_damage_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfd^pb')  # 0xfd5e7062
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_cannon_min_range))

        data.write(b'\xbd\x11\x08\x14')  # 0xbd110814
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_cannon_max_range))

        data.write(b'=\x94s7')  # 0x3d947337
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_cannon_cone_limit))

        data.write(b'\x1a\x97Z\x02')  # 0x1a975a02
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_cannon_track_speed))

        data.write(b'\x06k\xc8U')  # 0x66bc855
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.phazon_breath_projectile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'g\xe0\xe4\xb4')  # 0x67e0e4b4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_breath_track_speed))

        data.write(b'\xb7\xadpg')  # 0xb7ad7067
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_breath_min_range))

        data.write(b'\xf7\xe2\x08\x11')  # 0xf7e20811
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_breath_max_range))

        data.write(b'M\xb4t\xb8')  # 0x4db474b8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_breath_cone_limit))

        data.write(b'h\xd3\xda\xa4')  # 0x68d3daa4
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.phazon_breath_size_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x1b5\x92\x07')  # 0x1b359207
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_breath_destroy_missile_cone_limit))

        data.write(b'\xc1/9z')  # 0xc12f397a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_breath_destroy_missile_range))

        data.write(b'K\xfe\xe5k')  # 0x4bfee56b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_breath_destroy_missile_time))

        data.write(b'\x8f;\xe6\xe1')  # 0x8f3be6e1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_breath_missile_turn_time))

        data.write(b'\xdd\x82]\xc3')  # 0xdd825dc3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_breath_missile_turn_rate))

        data.write(b'\x86\x94\x15\xa3')  # 0x869415a3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_grapple_min_range))

        data.write(b'\xc6\xdbm\xd5')  # 0xc6db6dd5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_grapple_max_range))

        data.write(b'\xdc\x8dx\x87')  # 0xdc8d7887
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_grapple_time))

        data.write(b'X\xe6\xd9\xb8')  # 0x58e6d9b8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_grapple_suck_force))

        data.write(b'\xcf\x11\x1a\x99')  # 0xcf111a99
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_grapple_suck_distance))

        data.write(b'q\x9f\xd0k')  # 0x719fd06b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.phazon_grapple_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x92\xf0\xb2\xc7')  # 0x92f0b2c7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_grapple_spit_force))

        data.write(b'\xbc/\x8f0')  # 0xbc2f8f30
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbc2f8f30))

        data.write(b'\x91\n\xd1\xe0')  # 0x910ad1e0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x910ad1e0))

        data.write(b'Ef\xb3\xef')  # 0x4566b3ef
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4566b3ef))

        data.write(b'o\xe5\r2')  # 0x6fe50d32
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.approach_player_chance))

        data.write(b'$\xf7y\xca')  # 0x24f779ca
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x24f779ca))

        data.write(b'\xc6\xba\x97S')  # 0xc6ba9753
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.armored_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x83C\x90\x84')  # 0x83439084
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.armor_health))

        data.write(b'\x04T}4')  # 0x4547d34
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.armor_model1))

        data.write(b'\x82\xc0\x0f\x9a')  # 0x82c00f9a
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.armor_model2))

        data.write(b'I\x9c\xdc?')  # 0x499cdc3f
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.armor_model3))

        data.write(b'T\x99\xec\x87')  # 0x5499ec87
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.armor_model4))

        data.write(b'\x9f\xc5?"')  # 0x9fc53f22
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.armor_model5))

        data.write(b'\t\xe8\xc7\xfd')  # 0x9e8c7fd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.armor_gone_speed_up))

        data.write(b'J\xe5\x7f\xeb')  # 0x4ae57feb
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.weak_spot_model))

        data.write(b'N\x1dq\xa1')  # 0x4e1d71a1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.provoked_head_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'i\xd6n\xc4')  # 0x69d66ec4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.energy_orb_min_range))

        data.write(b')\x99\x16\xb2')  # 0x299916b2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.energy_orb_max_range))

        data.write(b'\xfeQ\x92N')  # 0xfe51924e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.energy_orb_lob_projectile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9b\x9cp,')  # 0x9b9c702c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.energy_orb_reflected_projectile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'V{\xa9J')  # 0x567ba94a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.energy_orb_charge_projectile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf4\xd5\x15\x0f')  # 0xf4d5150f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.energy_orb_slow_projectile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x86G\xc5\x81')  # 0x8647c581
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.energy_orb_fiery_projectile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x15\xd2m&')  # 0x15d26d26
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x15d26d26))

        data.write(b'\x81\xea\xa9\xd4')  # 0x81eaa9d4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x81eaa9d4))

        data.write(b'S\x1a\x8c\x85')  # 0x531a8c85
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_gandrayda))

        data.write(b'g{\xd8\xab')  # 0x677bd8ab
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_chieftain))

        data.write(b'\xc6\xe60\x0f')  # 0xc6e6300f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shoulder_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x15 V\x8a')  # 0x1520568a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.shoulder_health))

        data.write(b'&\x8e\\\xb2')  # 0x268e5cb2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x268e5cb2))

        data.write(b'e\x0b\xa28')  # 0x650ba238
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.left_shoulder_model))

        data.write(b'h\x86T\x10')  # 0x68865410
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.right_shoulder_model))

        data.write(b'4-\xaez')  # 0x342dae7a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.weak_spot_armored_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b' \x05E\xbd')  # 0x200545bd
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.nova_shoot_through_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf3\xea\x94\xdc')  # 0xf3ea94dc
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xed\xf1\x18\x9f')  # 0xedf1189f
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xedf1189f))

        data.write(b'\x84e3\xcc')  # 0x846533cc
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.minor_shockwave.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'*\xf1T\x8b')  # 0x2af1548b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.major_shockwave.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x0c\x1aVD')  # 0xc1a5644
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0c1a5644))

        data.write(b'\xc6\xaf/\xd0')  # 0xc6af2fd0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc6af2fd0))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("BerserkerDataJson", data)
        return cls(
            turn_threshold=json_data['turn_threshold'],
            should_play_alert_animation=json_data['should_play_alert_animation'],
            melee_attack_range=json_data['melee_attack_range'],
            uses_ball_slam=json_data['uses_ball_slam'],
            ball_slam_damage=DamageInfo.from_json(json_data['ball_slam_damage']),
            damage_info=DamageInfo.from_json(json_data['damage_info']),
            ground_pound_damage=DamageInfo.from_json(json_data['ground_pound_damage']),
            pirate_as_projectile_damage=DamageInfo.from_json(json_data['pirate_as_projectile_damage']),
            phazon_cannon_beam_info=PlasmaBeamInfo.from_json(json_data['phazon_cannon_beam_info']),
            phazon_cannon_damage_info=DamageInfo.from_json(json_data['phazon_cannon_damage_info']),
            phazon_cannon_min_range=json_data['phazon_cannon_min_range'],
            phazon_cannon_max_range=json_data['phazon_cannon_max_range'],
            phazon_cannon_cone_limit=json_data['phazon_cannon_cone_limit'],
            phazon_cannon_track_speed=json_data['phazon_cannon_track_speed'],
            phazon_breath_projectile=LaunchProjectileData.from_json(json_data['phazon_breath_projectile']),
            phazon_breath_track_speed=json_data['phazon_breath_track_speed'],
            phazon_breath_min_range=json_data['phazon_breath_min_range'],
            phazon_breath_max_range=json_data['phazon_breath_max_range'],
            phazon_breath_cone_limit=json_data['phazon_breath_cone_limit'],
            phazon_breath_size_spline=Spline.from_json(json_data['phazon_breath_size_spline']),
            phazon_breath_destroy_missile_cone_limit=json_data['phazon_breath_destroy_missile_cone_limit'],
            phazon_breath_destroy_missile_range=json_data['phazon_breath_destroy_missile_range'],
            phazon_breath_destroy_missile_time=json_data['phazon_breath_destroy_missile_time'],
            phazon_breath_missile_turn_time=json_data['phazon_breath_missile_turn_time'],
            phazon_breath_missile_turn_rate=json_data['phazon_breath_missile_turn_rate'],
            phazon_grapple_min_range=json_data['phazon_grapple_min_range'],
            phazon_grapple_max_range=json_data['phazon_grapple_max_range'],
            phazon_grapple_time=json_data['phazon_grapple_time'],
            phazon_grapple_suck_force=json_data['phazon_grapple_suck_force'],
            phazon_grapple_suck_distance=json_data['phazon_grapple_suck_distance'],
            phazon_grapple_damage=DamageInfo.from_json(json_data['phazon_grapple_damage']),
            phazon_grapple_spit_force=json_data['phazon_grapple_spit_force'],
            unknown_0xbc2f8f30=json_data['unknown_0xbc2f8f30'],
            unknown_0x910ad1e0=json_data['unknown_0x910ad1e0'],
            unknown_0x4566b3ef=json_data['unknown_0x4566b3ef'],
            approach_player_chance=json_data['approach_player_chance'],
            unknown_0x24f779ca=json_data['unknown_0x24f779ca'],
            armored_vulnerability=DamageVulnerability.from_json(json_data['armored_vulnerability']),
            armor_health=json_data['armor_health'],
            armor_model1=json_data['armor_model1'],
            armor_model2=json_data['armor_model2'],
            armor_model3=json_data['armor_model3'],
            armor_model4=json_data['armor_model4'],
            armor_model5=json_data['armor_model5'],
            armor_gone_speed_up=json_data['armor_gone_speed_up'],
            weak_spot_model=json_data['weak_spot_model'],
            provoked_head_vulnerability=DamageVulnerability.from_json(json_data['provoked_head_vulnerability']),
            energy_orb_min_range=json_data['energy_orb_min_range'],
            energy_orb_max_range=json_data['energy_orb_max_range'],
            energy_orb_lob_projectile=LaunchProjectileData.from_json(json_data['energy_orb_lob_projectile']),
            energy_orb_reflected_projectile=LaunchProjectileData.from_json(json_data['energy_orb_reflected_projectile']),
            energy_orb_charge_projectile=LaunchProjectileData.from_json(json_data['energy_orb_charge_projectile']),
            energy_orb_slow_projectile=LaunchProjectileData.from_json(json_data['energy_orb_slow_projectile']),
            energy_orb_fiery_projectile=LaunchProjectileData.from_json(json_data['energy_orb_fiery_projectile']),
            unknown_0x15d26d26=json_data['unknown_0x15d26d26'],
            unknown_0x81eaa9d4=json_data['unknown_0x81eaa9d4'],
            is_gandrayda=json_data['is_gandrayda'],
            is_chieftain=json_data['is_chieftain'],
            shoulder_vulnerability=DamageVulnerability.from_json(json_data['shoulder_vulnerability']),
            shoulder_health=json_data['shoulder_health'],
            unknown_0x268e5cb2=json_data['unknown_0x268e5cb2'],
            left_shoulder_model=json_data['left_shoulder_model'],
            right_shoulder_model=json_data['right_shoulder_model'],
            weak_spot_armored_vulnerability=DamageVulnerability.from_json(json_data['weak_spot_armored_vulnerability']),
            nova_shoot_through_vulnerability=DamageVulnerability.from_json(json_data['nova_shoot_through_vulnerability']),
            damage_vulnerability=DamageVulnerability.from_json(json_data['damage_vulnerability']),
            unknown_0xedf1189f=json_data['unknown_0xedf1189f'],
            minor_shockwave=ShockWaveInfo.from_json(json_data['minor_shockwave']),
            major_shockwave=ShockWaveInfo.from_json(json_data['major_shockwave']),
            unknown_0x0c1a5644=json_data['unknown_0x0c1a5644'],
            unknown_0xc6af2fd0=json_data['unknown_0xc6af2fd0'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'turn_threshold': self.turn_threshold,
            'should_play_alert_animation': self.should_play_alert_animation,
            'melee_attack_range': self.melee_attack_range,
            'uses_ball_slam': self.uses_ball_slam,
            'ball_slam_damage': self.ball_slam_damage.to_json(),
            'damage_info': self.damage_info.to_json(),
            'ground_pound_damage': self.ground_pound_damage.to_json(),
            'pirate_as_projectile_damage': self.pirate_as_projectile_damage.to_json(),
            'phazon_cannon_beam_info': self.phazon_cannon_beam_info.to_json(),
            'phazon_cannon_damage_info': self.phazon_cannon_damage_info.to_json(),
            'phazon_cannon_min_range': self.phazon_cannon_min_range,
            'phazon_cannon_max_range': self.phazon_cannon_max_range,
            'phazon_cannon_cone_limit': self.phazon_cannon_cone_limit,
            'phazon_cannon_track_speed': self.phazon_cannon_track_speed,
            'phazon_breath_projectile': self.phazon_breath_projectile.to_json(),
            'phazon_breath_track_speed': self.phazon_breath_track_speed,
            'phazon_breath_min_range': self.phazon_breath_min_range,
            'phazon_breath_max_range': self.phazon_breath_max_range,
            'phazon_breath_cone_limit': self.phazon_breath_cone_limit,
            'phazon_breath_size_spline': self.phazon_breath_size_spline.to_json(),
            'phazon_breath_destroy_missile_cone_limit': self.phazon_breath_destroy_missile_cone_limit,
            'phazon_breath_destroy_missile_range': self.phazon_breath_destroy_missile_range,
            'phazon_breath_destroy_missile_time': self.phazon_breath_destroy_missile_time,
            'phazon_breath_missile_turn_time': self.phazon_breath_missile_turn_time,
            'phazon_breath_missile_turn_rate': self.phazon_breath_missile_turn_rate,
            'phazon_grapple_min_range': self.phazon_grapple_min_range,
            'phazon_grapple_max_range': self.phazon_grapple_max_range,
            'phazon_grapple_time': self.phazon_grapple_time,
            'phazon_grapple_suck_force': self.phazon_grapple_suck_force,
            'phazon_grapple_suck_distance': self.phazon_grapple_suck_distance,
            'phazon_grapple_damage': self.phazon_grapple_damage.to_json(),
            'phazon_grapple_spit_force': self.phazon_grapple_spit_force,
            'unknown_0xbc2f8f30': self.unknown_0xbc2f8f30,
            'unknown_0x910ad1e0': self.unknown_0x910ad1e0,
            'unknown_0x4566b3ef': self.unknown_0x4566b3ef,
            'approach_player_chance': self.approach_player_chance,
            'unknown_0x24f779ca': self.unknown_0x24f779ca,
            'armored_vulnerability': self.armored_vulnerability.to_json(),
            'armor_health': self.armor_health,
            'armor_model1': self.armor_model1,
            'armor_model2': self.armor_model2,
            'armor_model3': self.armor_model3,
            'armor_model4': self.armor_model4,
            'armor_model5': self.armor_model5,
            'armor_gone_speed_up': self.armor_gone_speed_up,
            'weak_spot_model': self.weak_spot_model,
            'provoked_head_vulnerability': self.provoked_head_vulnerability.to_json(),
            'energy_orb_min_range': self.energy_orb_min_range,
            'energy_orb_max_range': self.energy_orb_max_range,
            'energy_orb_lob_projectile': self.energy_orb_lob_projectile.to_json(),
            'energy_orb_reflected_projectile': self.energy_orb_reflected_projectile.to_json(),
            'energy_orb_charge_projectile': self.energy_orb_charge_projectile.to_json(),
            'energy_orb_slow_projectile': self.energy_orb_slow_projectile.to_json(),
            'energy_orb_fiery_projectile': self.energy_orb_fiery_projectile.to_json(),
            'unknown_0x15d26d26': self.unknown_0x15d26d26,
            'unknown_0x81eaa9d4': self.unknown_0x81eaa9d4,
            'is_gandrayda': self.is_gandrayda,
            'is_chieftain': self.is_chieftain,
            'shoulder_vulnerability': self.shoulder_vulnerability.to_json(),
            'shoulder_health': self.shoulder_health,
            'unknown_0x268e5cb2': self.unknown_0x268e5cb2,
            'left_shoulder_model': self.left_shoulder_model,
            'right_shoulder_model': self.right_shoulder_model,
            'weak_spot_armored_vulnerability': self.weak_spot_armored_vulnerability.to_json(),
            'nova_shoot_through_vulnerability': self.nova_shoot_through_vulnerability.to_json(),
            'damage_vulnerability': self.damage_vulnerability.to_json(),
            'unknown_0xedf1189f': self.unknown_0xedf1189f,
            'minor_shockwave': self.minor_shockwave.to_json(),
            'major_shockwave': self.major_shockwave.to_json(),
            'unknown_0x0c1a5644': self.unknown_0x0c1a5644,
            'unknown_0xc6af2fd0': self.unknown_0xc6af2fd0,
        }

    def _dependencies_for_armor_model1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.armor_model1)

    def _dependencies_for_armor_model2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.armor_model2)

    def _dependencies_for_armor_model3(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.armor_model3)

    def _dependencies_for_armor_model4(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.armor_model4)

    def _dependencies_for_armor_model5(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.armor_model5)

    def _dependencies_for_weak_spot_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.weak_spot_model)

    def _dependencies_for_left_shoulder_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.left_shoulder_model)

    def _dependencies_for_right_shoulder_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.right_shoulder_model)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.phazon_cannon_beam_info.dependencies_for, "phazon_cannon_beam_info", "PlasmaBeamInfo"),
            (self.phazon_breath_projectile.dependencies_for, "phazon_breath_projectile", "LaunchProjectileData"),
            (self._dependencies_for_armor_model1, "armor_model1", "AssetId"),
            (self._dependencies_for_armor_model2, "armor_model2", "AssetId"),
            (self._dependencies_for_armor_model3, "armor_model3", "AssetId"),
            (self._dependencies_for_armor_model4, "armor_model4", "AssetId"),
            (self._dependencies_for_armor_model5, "armor_model5", "AssetId"),
            (self._dependencies_for_weak_spot_model, "weak_spot_model", "AssetId"),
            (self.energy_orb_lob_projectile.dependencies_for, "energy_orb_lob_projectile", "LaunchProjectileData"),
            (self.energy_orb_reflected_projectile.dependencies_for, "energy_orb_reflected_projectile", "LaunchProjectileData"),
            (self.energy_orb_charge_projectile.dependencies_for, "energy_orb_charge_projectile", "LaunchProjectileData"),
            (self.energy_orb_slow_projectile.dependencies_for, "energy_orb_slow_projectile", "LaunchProjectileData"),
            (self.energy_orb_fiery_projectile.dependencies_for, "energy_orb_fiery_projectile", "LaunchProjectileData"),
            (self._dependencies_for_left_shoulder_model, "left_shoulder_model", "AssetId"),
            (self._dependencies_for_right_shoulder_model, "right_shoulder_model", "AssetId"),
            (self.minor_shockwave.dependencies_for, "minor_shockwave", "ShockWaveInfo"),
            (self.major_shockwave.dependencies_for, "major_shockwave", "ShockWaveInfo"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for BerserkerData.{field_name} ({field_type}): {e}"
                )


def _decode_ball_slam_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_damage_info(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_ground_pound_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_pirate_as_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_phazon_cannon_beam_info(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size)


def _decode_phazon_cannon_damage_info(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_phazon_breath_projectile(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_phazon_breath_size_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_phazon_grapple_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_armored_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_provoked_head_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_energy_orb_lob_projectile(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_energy_orb_reflected_projectile(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_energy_orb_charge_projectile(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_energy_orb_slow_projectile(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_energy_orb_fiery_projectile(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_shoulder_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_weak_spot_armored_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_nova_shoot_through_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_damage_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_minor_shockwave(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


def _decode_major_shockwave(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xc0ac271e: ('turn_threshold', structs.decode_BIG_f),
    0x76ebc21a: ('should_play_alert_animation', structs.decode_BIG_bool_),
    0xc3e43d0e: ('melee_attack_range', structs.decode_BIG_f),
    0xc4db42e3: ('uses_ball_slam', structs.decode_BIG_bool_),
    0x74bffa78: ('ball_slam_damage', _decode_ball_slam_damage),
    0xbb7977b9: ('damage_info', _decode_damage_info),
    0x4738c321: ('ground_pound_damage', _decode_ground_pound_damage),
    0xf4e003c1: ('pirate_as_projectile_damage', _decode_pirate_as_projectile_damage),
    0xe0dbf22f: ('phazon_cannon_beam_info', _decode_phazon_cannon_beam_info),
    0x97321af1: ('phazon_cannon_damage_info', _decode_phazon_cannon_damage_info),
    0xfd5e7062: ('phazon_cannon_min_range', structs.decode_BIG_f),
    0xbd110814: ('phazon_cannon_max_range', structs.decode_BIG_f),
    0x3d947337: ('phazon_cannon_cone_limit', structs.decode_BIG_f),
    0x1a975a02: ('phazon_cannon_track_speed', structs.decode_BIG_f),
    0x066bc855: ('phazon_breath_projectile', _decode_phazon_breath_projectile),
    0x67e0e4b4: ('phazon_breath_track_speed', structs.decode_BIG_f),
    0xb7ad7067: ('phazon_breath_min_range', structs.decode_BIG_f),
    0xf7e20811: ('phazon_breath_max_range', structs.decode_BIG_f),
    0x4db474b8: ('phazon_breath_cone_limit', structs.decode_BIG_f),
    0x68d3daa4: ('phazon_breath_size_spline', _decode_phazon_breath_size_spline),
    0x1b359207: ('phazon_breath_destroy_missile_cone_limit', structs.decode_BIG_f),
    0xc12f397a: ('phazon_breath_destroy_missile_range', structs.decode_BIG_f),
    0x4bfee56b: ('phazon_breath_destroy_missile_time', structs.decode_BIG_f),
    0x8f3be6e1: ('phazon_breath_missile_turn_time', structs.decode_BIG_f),
    0xdd825dc3: ('phazon_breath_missile_turn_rate', structs.decode_BIG_f),
    0x869415a3: ('phazon_grapple_min_range', structs.decode_BIG_f),
    0xc6db6dd5: ('phazon_grapple_max_range', structs.decode_BIG_f),
    0xdc8d7887: ('phazon_grapple_time', structs.decode_BIG_f),
    0x58e6d9b8: ('phazon_grapple_suck_force', structs.decode_BIG_f),
    0xcf111a99: ('phazon_grapple_suck_distance', structs.decode_BIG_f),
    0x719fd06b: ('phazon_grapple_damage', _decode_phazon_grapple_damage),
    0x92f0b2c7: ('phazon_grapple_spit_force', structs.decode_BIG_f),
    0xbc2f8f30: ('unknown_0xbc2f8f30', structs.decode_BIG_f),
    0x910ad1e0: ('unknown_0x910ad1e0', structs.decode_BIG_f),
    0x4566b3ef: ('unknown_0x4566b3ef', structs.decode_BIG_f),
    0x6fe50d32: ('approach_player_chance', structs.decode_BIG_f),
    0x24f779ca: ('unknown_0x24f779ca', structs.decode_BIG_f),
    0xc6ba9753: ('armored_vulnerability', _decode_armored_vulnerability),
    0x83439084: ('armor_health', structs.decode_BIG_f),
    0x04547d34: ('armor_model1', structs.decode_BIG_Q),
    0x82c00f9a: ('armor_model2', structs.decode_BIG_Q),
    0x499cdc3f: ('armor_model3', structs.decode_BIG_Q),
    0x5499ec87: ('armor_model4', structs.decode_BIG_Q),
    0x9fc53f22: ('armor_model5', structs.decode_BIG_Q),
    0x09e8c7fd: ('armor_gone_speed_up', structs.decode_BIG_f),
    0x4ae57feb: ('weak_spot_model', structs.decode_BIG_Q),
    0x4e1d71a1: ('provoked_head_vulnerability', _decode_provoked_head_vulnerability),
    0x69d66ec4: ('energy_orb_min_range', structs.decode_BIG_f),
    0x299916b2: ('energy_orb_max_range', structs.decode_BIG_f),
    0xfe51924e: ('energy_orb_lob_projectile', _decode_energy_orb_lob_projectile),
    0x9b9c702c: ('energy_orb_reflected_projectile', _decode_energy_orb_reflected_projectile),
    0x567ba94a: ('energy_orb_charge_projectile', _decode_energy_orb_charge_projectile),
    0xf4d5150f: ('energy_orb_slow_projectile', _decode_energy_orb_slow_projectile),
    0x8647c581: ('energy_orb_fiery_projectile', _decode_energy_orb_fiery_projectile),
    0x15d26d26: ('unknown_0x15d26d26', structs.decode_BIG_f),
    0x81eaa9d4: ('unknown_0x81eaa9d4', structs.decode_BIG_f),
    0x531a8c85: ('is_gandrayda', structs.decode_BIG_bool_),
    0x677bd8ab: ('is_chieftain', structs.decode_BIG_bool_),
    0xc6e6300f: ('shoulder_vulnerability', _decode_shoulder_vulnerability),
    0x1520568a: ('shoulder_health', structs.decode_BIG_f),
    0x268e5cb2: ('unknown_0x268e5cb2', structs.decode_BIG_f),
    0x650ba238: ('left_shoulder_model', structs.decode_BIG_Q),
    0x68865410: ('right_shoulder_model', structs.decode_BIG_Q),
    0x342dae7a: ('weak_spot_armored_vulnerability', _decode_weak_spot_armored_vulnerability),
    0x200545bd: ('nova_shoot_through_vulnerability', _decode_nova_shoot_through_vulnerability),
    0xf3ea94dc: ('damage_vulnerability', _decode_damage_vulnerability),
    0xedf1189f: ('unknown_0xedf1189f', structs.decode_BIG_bool_),
    0x846533cc: ('minor_shockwave', _decode_minor_shockwave),
    0x2af1548b: ('major_shockwave', _decode_major_shockwave),
    0x0c1a5644: ('unknown_0x0c1a5644', structs.decode_BIG_f),
    0xc6af2fd0: ('unknown_0xc6af2fd0', structs.decode_BIG_f),
}
