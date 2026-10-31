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
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.corruption.archetypes.HoverThenHomeProjectile import HoverThenHomeProjectile
from retro_data_structures.properties.corruption.archetypes.LaunchProjectileData import LaunchProjectileData
from retro_data_structures.properties.corruption.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.corruption.archetypes.ScannableParameters import ScannableParameters
from retro_data_structures.properties.corruption.archetypes.SeedBoss1HandData import SeedBoss1HandData
from retro_data_structures.properties.corruption.archetypes.SeedBoss1Shield import SeedBoss1Shield
from retro_data_structures.properties.corruption.archetypes.SeedBoss1Stage import SeedBoss1Stage
from retro_data_structures.properties.corruption.archetypes.ShockWaveInfo import ShockWaveInfo
from retro_data_structures.properties.corruption.archetypes.UnknownStruct60 import UnknownStruct60
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.spline import Spline
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SeedBoss1DataJson(typing_extensions.TypedDict):
        min_time_between_melee_attacks: float
        foot_health: json_util.JsonObject
        foot_vulnerability: json_util.JsonObject
        left_foot: int
        left_knee: int
        left_thigh: int
        right_foot: int
        right_knee: int
        right_thigh: int
        stomach_slot_intact: int
        stomach_slot_broken: int
        stomach_slot_cover: int
        back_slot_intact: int
        back_slot_broken: int
        back_slot_cover: int
        shoulder_left_slot_intact: int
        shoulder_left_slot_broken: int
        shoulder_left_slot_cover: int
        shoulder_right_slot_intact: int
        shoulder_right_slot_broken: int
        shoulder_right_slot_cover: int
        head_model: int
        jaw_model: int
        ice_model: int
        head_ice_model: int
        jaw_ice_model: int
        head_vulnerability: json_util.JsonObject
        head_frozen_time: float
        shockwave: json_util.JsonObject
        unknown_struct60: json_util.JsonObject
        beam_info: json_util.JsonObject
        beam_damage_info: json_util.JsonObject
        orb_slot_vulnerability: json_util.JsonObject
        foot_explosion: int
        foot_explosion_sound: int
        stalactite_weapon: int
        stalactite_damage: json_util.JsonObject
        stalactite_shockwave: json_util.JsonObject
        hyper_homing_projectile_data: json_util.JsonObject
        hyper_homing_hover_data: json_util.JsonObject
        hyper_homing_projectile_size: json_util.JsonValue
        hyper_homing_projectile_hp: float
        hyper_homing_projectile_stop_homing_dist: float
        hand_projectile_data: json_util.JsonObject
        hand_hover_data: json_util.JsonObject
        hand_projectile_size: json_util.JsonValue
        hand_projectile_hp: float
        hand_projectile_stop_homing_dist: float
        hand_projectile_damage_effect: int
        hand_projectile_damage_sound: int
        charge_player_damage: json_util.JsonObject
        phazon_drain_projectile_info: json_util.JsonObject
        hand_data: json_util.JsonObject
        color_hand_of_ur: json_util.JsonValue
        unknown_0x77d3b386: json_util.JsonValue
        color_hyper_shockwave: json_util.JsonValue
        color_hyper_homing_shots: json_util.JsonValue
        color_hyper_quake: json_util.JsonValue
        color_energized: json_util.JsonValue
        min_taunt_time: float
        max_taunt_time: float
        stage1_settings: json_util.JsonObject
        stage2_settings: json_util.JsonObject
        stage3_settings: json_util.JsonObject
        stage4_settings: json_util.JsonObject
        shield_info: json_util.JsonObject
        foot_contact_damage: json_util.JsonObject
        unknown_0x64588114: float
        approach_player_distance: float
        approach_player_delay: float
        approach_player_time: float
        orb_color_control: json_util.JsonObject
        orb_missing_scan: json_util.JsonObject
    

@dataclasses.dataclass()
class SeedBoss1Data(BaseProperty):
    min_time_between_melee_attacks: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd3ad55b6, original_name='MinTimeBetweenMeleeAttacks'
        ),
    })
    foot_health: HealthInfo = dataclasses.field(default_factory=HealthInfo, metadata={
        'reflection': FieldReflection[HealthInfo](
            HealthInfo, id=0xb33eb533, original_name='FootHealth', from_json=HealthInfo.from_json, to_json=HealthInfo.to_json
        ),
    })
    foot_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x26fa460b, original_name='FootVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    left_foot: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xad0de5ac, original_name='LeftFoot'
        ),
    })
    left_knee: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xfc128c15, original_name='LeftKnee'
        ),
    })
    left_thigh: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x299b8d33, original_name='LeftThigh'
        ),
    })
    right_foot: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa5bb98a6, original_name='RightFoot'
        ),
    })
    right_knee: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xf4a4f11f, original_name='RightKnee'
        ),
    })
    right_thigh: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc946d250, original_name='RightThigh'
        ),
    })
    stomach_slot_intact: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x50edae7f, original_name='StomachSlotIntact'
        ),
    })
    stomach_slot_broken: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x30969cfe, original_name='StomachSlotBroken'
        ),
    })
    stomach_slot_cover: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb25e271d, original_name='StomachSlotCover'
        ),
    })
    back_slot_intact: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5d71b85c, original_name='BackSlotIntact'
        ),
    })
    back_slot_broken: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3d0a8add, original_name='BackSlotBroken'
        ),
    })
    back_slot_cover: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x43223a97, original_name='BackSlotCover'
        ),
    })
    shoulder_left_slot_intact: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x9b76ad84, original_name='ShoulderLeftSlotIntact'
        ),
    })
    shoulder_left_slot_broken: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xfb0d9f05, original_name='ShoulderLeftSlotBroken'
        ),
    })
    shoulder_left_slot_cover: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x48ee50ad, original_name='ShoulderLeftSlotCover'
        ),
    })
    shoulder_right_slot_intact: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x85635b3b, original_name='ShoulderRightSlotIntact'
        ),
    })
    shoulder_right_slot_broken: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe51869ba, original_name='ShoulderRightSlotBroken'
        ),
    })
    shoulder_right_slot_cover: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5cea873f, original_name='ShoulderRightSlotCover'
        ),
    })
    head_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc288ae69, original_name='HeadModel'
        ),
    })
    jaw_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xcdbd44e1, original_name='JawModel'
        ),
    })
    ice_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x6ad6cbba, original_name='IceModel'
        ),
    })
    head_ice_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3ab79847, original_name='HeadIceModel'
        ),
    })
    jaw_ice_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x27b30d35, original_name='JawIceModel'
        ),
    })
    head_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xec37e2fa, original_name='HeadVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    head_frozen_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xccca3249, original_name='HeadFrozenTime'
        ),
    })
    shockwave: ShockWaveInfo = dataclasses.field(default_factory=ShockWaveInfo, metadata={
        'reflection': FieldReflection[ShockWaveInfo](
            ShockWaveInfo, id=0x3ce6e482, original_name='Shockwave', from_json=ShockWaveInfo.from_json, to_json=ShockWaveInfo.to_json
        ),
    })
    unknown_struct60: UnknownStruct60 = dataclasses.field(default_factory=UnknownStruct60, metadata={
        'reflection': FieldReflection[UnknownStruct60](
            UnknownStruct60, id=0x72e00501, original_name='UnknownStruct60', from_json=UnknownStruct60.from_json, to_json=UnknownStruct60.to_json
        ),
    })
    beam_info: PlasmaBeamInfo = dataclasses.field(default_factory=PlasmaBeamInfo, metadata={
        'reflection': FieldReflection[PlasmaBeamInfo](
            PlasmaBeamInfo, id=0x1598012a, original_name='BeamInfo', from_json=PlasmaBeamInfo.from_json, to_json=PlasmaBeamInfo.to_json
        ),
    })
    beam_damage_info: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x98821996, original_name='BeamDamageInfo', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    orb_slot_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xdd34c3c0, original_name='OrbSlotVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    foot_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x547b9a9a, original_name='FootExplosion'
        ),
    })
    foot_explosion_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xeaf93057, original_name='FootExplosionSound'
        ),
    })
    stalactite_weapon: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x36c067c2, original_name='StalactiteWeapon'
        ),
    })
    stalactite_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x261eefe7, original_name='StalactiteDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    stalactite_shockwave: ShockWaveInfo = dataclasses.field(default_factory=ShockWaveInfo, metadata={
        'reflection': FieldReflection[ShockWaveInfo](
            ShockWaveInfo, id=0x818f810b, original_name='StalactiteShockwave', from_json=ShockWaveInfo.from_json, to_json=ShockWaveInfo.to_json
        ),
    })
    hyper_homing_projectile_data: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0x7c9c3b51, original_name='HyperHomingProjectileData', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    hyper_homing_hover_data: HoverThenHomeProjectile = dataclasses.field(default_factory=HoverThenHomeProjectile, metadata={
        'reflection': FieldReflection[HoverThenHomeProjectile](
            HoverThenHomeProjectile, id=0x730fe427, original_name='HyperHomingHoverData', from_json=HoverThenHomeProjectile.from_json, to_json=HoverThenHomeProjectile.to_json
        ),
    })
    hyper_homing_projectile_size: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x050924d3, original_name='HyperHomingProjectileSize', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    hyper_homing_projectile_hp: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6414e848, original_name='HyperHomingProjectileHP'
        ),
    })
    hyper_homing_projectile_stop_homing_dist: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2a7a2da7, original_name='HyperHomingProjectileStopHomingDist'
        ),
    })
    hand_projectile_data: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0x4392c34a, original_name='HandProjectileData', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    hand_hover_data: HoverThenHomeProjectile = dataclasses.field(default_factory=HoverThenHomeProjectile, metadata={
        'reflection': FieldReflection[HoverThenHomeProjectile](
            HoverThenHomeProjectile, id=0x868e4192, original_name='HandHoverData', from_json=HoverThenHomeProjectile.from_json, to_json=HoverThenHomeProjectile.to_json
        ),
    })
    hand_projectile_size: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0xc8e16555, original_name='HandProjectileSize', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    hand_projectile_hp: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x153c001b, original_name='HandProjectileHP'
        ),
    })
    hand_projectile_stop_homing_dist: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x473b730b, original_name='HandProjectileStopHomingDist'
        ),
    })
    hand_projectile_damage_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xaea60f24, original_name='HandProjectileDamageEffect'
        ),
    })
    hand_projectile_damage_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x38786921, original_name='HandProjectileDamageSound'
        ),
    })
    charge_player_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x9e63065f, original_name='ChargePlayerDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    phazon_drain_projectile_info: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0x50ae6e55, original_name='PhazonDrainProjectileInfo', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    hand_data: SeedBoss1HandData = dataclasses.field(default_factory=SeedBoss1HandData, metadata={
        'reflection': FieldReflection[SeedBoss1HandData](
            SeedBoss1HandData, id=0xc69f691a, original_name='HandData', from_json=SeedBoss1HandData.from_json, to_json=SeedBoss1HandData.to_json
        ),
    })
    color_hand_of_ur: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x3196b2e7, original_name='ColorHandOfUr', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    unknown_0x77d3b386: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x77d3b386, original_name='Unknown', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    color_hyper_shockwave: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xa9be1081, original_name='ColorHyperShockwave', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    color_hyper_homing_shots: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x7ce5c47c, original_name='ColorHyperHomingShots', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    color_hyper_quake: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf9656c39, original_name='ColorHyperQuake', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    color_energized: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xd7142afe, original_name='ColorEnergized', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    min_taunt_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc3718ea0, original_name='MinTauntTime'
        ),
    })
    max_taunt_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd6fa5a52, original_name='MaxTauntTime'
        ),
    })
    stage1_settings: SeedBoss1Stage = dataclasses.field(default_factory=SeedBoss1Stage, metadata={
        'reflection': FieldReflection[SeedBoss1Stage](
            SeedBoss1Stage, id=0x45694db0, original_name='Stage1Settings', from_json=SeedBoss1Stage.from_json, to_json=SeedBoss1Stage.to_json
        ),
    })
    stage2_settings: SeedBoss1Stage = dataclasses.field(default_factory=SeedBoss1Stage, metadata={
        'reflection': FieldReflection[SeedBoss1Stage](
            SeedBoss1Stage, id=0x338c748d, original_name='Stage2Settings', from_json=SeedBoss1Stage.from_json, to_json=SeedBoss1Stage.to_json
        ),
    })
    stage3_settings: SeedBoss1Stage = dataclasses.field(default_factory=SeedBoss1Stage, metadata={
        'reflection': FieldReflection[SeedBoss1Stage](
            SeedBoss1Stage, id=0xa8ff9e59, original_name='Stage3Settings', from_json=SeedBoss1Stage.from_json, to_json=SeedBoss1Stage.to_json
        ),
    })
    stage4_settings: SeedBoss1Stage = dataclasses.field(default_factory=SeedBoss1Stage, metadata={
        'reflection': FieldReflection[SeedBoss1Stage](
            SeedBoss1Stage, id=0xde4606f7, original_name='Stage4Settings', from_json=SeedBoss1Stage.from_json, to_json=SeedBoss1Stage.to_json
        ),
    })
    shield_info: SeedBoss1Shield = dataclasses.field(default_factory=SeedBoss1Shield, metadata={
        'reflection': FieldReflection[SeedBoss1Shield](
            SeedBoss1Shield, id=0x2883f972, original_name='ShieldInfo', from_json=SeedBoss1Shield.from_json, to_json=SeedBoss1Shield.to_json
        ),
    })
    foot_contact_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x40ac1fd4, original_name='FootContactDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    unknown_0x64588114: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x64588114, original_name='Unknown'
        ),
    })
    approach_player_distance: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x712d3274, original_name='ApproachPlayerDistance'
        ),
    })
    approach_player_delay: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x50ec86c1, original_name='ApproachPlayerDelay'
        ),
    })
    approach_player_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x536b7493, original_name='ApproachPlayerTime'
        ),
    })
    orb_color_control: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xc2be328d, original_name='OrbColorControl', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    orb_missing_scan: ScannableParameters = dataclasses.field(default_factory=ScannableParameters, metadata={
        'reflection': FieldReflection[ScannableParameters](
            ScannableParameters, id=0x022fdca5, original_name='OrbMissingScan', from_json=ScannableParameters.from_json, to_json=ScannableParameters.to_json
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
        if property_count != 73:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd3ad55b6
        min_time_between_melee_attacks = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb33eb533
        foot_health = HealthInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x26fa460b
        foot_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xad0de5ac
        left_foot = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfc128c15
        left_knee = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x299b8d33
        left_thigh = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa5bb98a6
        right_foot = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf4a4f11f
        right_knee = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc946d250
        right_thigh = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50edae7f
        stomach_slot_intact = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x30969cfe
        stomach_slot_broken = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb25e271d
        stomach_slot_cover = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5d71b85c
        back_slot_intact = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3d0a8add
        back_slot_broken = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x43223a97
        back_slot_cover = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9b76ad84
        shoulder_left_slot_intact = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfb0d9f05
        shoulder_left_slot_broken = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x48ee50ad
        shoulder_left_slot_cover = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x85635b3b
        shoulder_right_slot_intact = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe51869ba
        shoulder_right_slot_broken = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5cea873f
        shoulder_right_slot_cover = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc288ae69
        head_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcdbd44e1
        jaw_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6ad6cbba
        ice_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3ab79847
        head_ice_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x27b30d35
        jaw_ice_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xec37e2fa
        head_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xccca3249
        head_frozen_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3ce6e482
        shockwave = ShockWaveInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x72e00501
        unknown_struct60 = UnknownStruct60.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1598012a
        beam_info = PlasmaBeamInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x98821996
        beam_damage_info = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdd34c3c0
        orb_slot_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x547b9a9a
        foot_explosion = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xeaf93057
        foot_explosion_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x36c067c2
        stalactite_weapon = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x261eefe7
        stalactite_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x818f810b
        stalactite_shockwave = ShockWaveInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7c9c3b51
        hyper_homing_projectile_data = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x730fe427
        hyper_homing_hover_data = HoverThenHomeProjectile.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x050924d3
        hyper_homing_projectile_size = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6414e848
        hyper_homing_projectile_hp = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2a7a2da7
        hyper_homing_projectile_stop_homing_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4392c34a
        hand_projectile_data = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x868e4192
        hand_hover_data = HoverThenHomeProjectile.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc8e16555
        hand_projectile_size = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x153c001b
        hand_projectile_hp = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x473b730b
        hand_projectile_stop_homing_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaea60f24
        hand_projectile_damage_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x38786921
        hand_projectile_damage_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9e63065f
        charge_player_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50ae6e55
        phazon_drain_projectile_info = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc69f691a
        hand_data = SeedBoss1HandData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3196b2e7
        color_hand_of_ur = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77d3b386
        unknown_0x77d3b386 = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa9be1081
        color_hyper_shockwave = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7ce5c47c
        color_hyper_homing_shots = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf9656c39
        color_hyper_quake = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd7142afe
        color_energized = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc3718ea0
        min_taunt_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd6fa5a52
        max_taunt_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x45694db0
        stage1_settings = SeedBoss1Stage.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x338c748d
        stage2_settings = SeedBoss1Stage.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa8ff9e59
        stage3_settings = SeedBoss1Stage.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xde4606f7
        stage4_settings = SeedBoss1Stage.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2883f972
        shield_info = SeedBoss1Shield.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x40ac1fd4
        foot_contact_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64588114
        unknown_0x64588114 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x712d3274
        approach_player_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50ec86c1
        approach_player_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x536b7493
        approach_player_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc2be328d
        orb_color_control = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x022fdca5
        orb_missing_scan = ScannableParameters.from_stream(data, game, property_size)
    
        return cls(min_time_between_melee_attacks, foot_health, foot_vulnerability, left_foot, left_knee, left_thigh, right_foot, right_knee, right_thigh, stomach_slot_intact, stomach_slot_broken, stomach_slot_cover, back_slot_intact, back_slot_broken, back_slot_cover, shoulder_left_slot_intact, shoulder_left_slot_broken, shoulder_left_slot_cover, shoulder_right_slot_intact, shoulder_right_slot_broken, shoulder_right_slot_cover, head_model, jaw_model, ice_model, head_ice_model, jaw_ice_model, head_vulnerability, head_frozen_time, shockwave, unknown_struct60, beam_info, beam_damage_info, orb_slot_vulnerability, foot_explosion, foot_explosion_sound, stalactite_weapon, stalactite_damage, stalactite_shockwave, hyper_homing_projectile_data, hyper_homing_hover_data, hyper_homing_projectile_size, hyper_homing_projectile_hp, hyper_homing_projectile_stop_homing_dist, hand_projectile_data, hand_hover_data, hand_projectile_size, hand_projectile_hp, hand_projectile_stop_homing_dist, hand_projectile_damage_effect, hand_projectile_damage_sound, charge_player_damage, phazon_drain_projectile_info, hand_data, color_hand_of_ur, unknown_0x77d3b386, color_hyper_shockwave, color_hyper_homing_shots, color_hyper_quake, color_energized, min_taunt_time, max_taunt_time, stage1_settings, stage2_settings, stage3_settings, stage4_settings, shield_info, foot_contact_damage, unknown_0x64588114, approach_player_distance, approach_player_delay, approach_player_time, orb_color_control, orb_missing_scan)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00I')  # 73 properties

        data.write(b'\xd3\xadU\xb6')  # 0xd3ad55b6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_melee_attacks))

        data.write(b'\xb3>\xb53')  # 0xb33eb533
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.foot_health.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'&\xfaF\x0b')  # 0x26fa460b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.foot_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xad\r\xe5\xac')  # 0xad0de5ac
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.left_foot))

        data.write(b'\xfc\x12\x8c\x15')  # 0xfc128c15
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.left_knee))

        data.write(b')\x9b\x8d3')  # 0x299b8d33
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.left_thigh))

        data.write(b'\xa5\xbb\x98\xa6')  # 0xa5bb98a6
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.right_foot))

        data.write(b'\xf4\xa4\xf1\x1f')  # 0xf4a4f11f
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.right_knee))

        data.write(b'\xc9F\xd2P')  # 0xc946d250
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.right_thigh))

        data.write(b'P\xed\xae\x7f')  # 0x50edae7f
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.stomach_slot_intact))

        data.write(b'0\x96\x9c\xfe')  # 0x30969cfe
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.stomach_slot_broken))

        data.write(b"\xb2^'\x1d")  # 0xb25e271d
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.stomach_slot_cover))

        data.write(b']q\xb8\\')  # 0x5d71b85c
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.back_slot_intact))

        data.write(b'=\n\x8a\xdd')  # 0x3d0a8add
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.back_slot_broken))

        data.write(b'C":\x97')  # 0x43223a97
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.back_slot_cover))

        data.write(b'\x9bv\xad\x84')  # 0x9b76ad84
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shoulder_left_slot_intact))

        data.write(b'\xfb\r\x9f\x05')  # 0xfb0d9f05
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shoulder_left_slot_broken))

        data.write(b'H\xeeP\xad')  # 0x48ee50ad
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shoulder_left_slot_cover))

        data.write(b'\x85c[;')  # 0x85635b3b
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shoulder_right_slot_intact))

        data.write(b'\xe5\x18i\xba')  # 0xe51869ba
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shoulder_right_slot_broken))

        data.write(b'\\\xea\x87?')  # 0x5cea873f
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shoulder_right_slot_cover))

        data.write(b'\xc2\x88\xaei')  # 0xc288ae69
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.head_model))

        data.write(b'\xcd\xbdD\xe1')  # 0xcdbd44e1
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.jaw_model))

        data.write(b'j\xd6\xcb\xba')  # 0x6ad6cbba
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ice_model))

        data.write(b':\xb7\x98G')  # 0x3ab79847
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.head_ice_model))

        data.write(b"'\xb3\r5")  # 0x27b30d35
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.jaw_ice_model))

        data.write(b'\xec7\xe2\xfa')  # 0xec37e2fa
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.head_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xcc\xca2I')  # 0xccca3249
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.head_frozen_time))

        data.write(b'<\xe6\xe4\x82')  # 0x3ce6e482
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shockwave.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'r\xe0\x05\x01')  # 0x72e00501
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.unknown_struct60.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x15\x98\x01*')  # 0x1598012a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.beam_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x98\x82\x19\x96')  # 0x98821996
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.beam_damage_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xdd4\xc3\xc0')  # 0xdd34c3c0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.orb_slot_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'T{\x9a\x9a')  # 0x547b9a9a
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.foot_explosion))

        data.write(b'\xea\xf90W')  # 0xeaf93057
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.foot_explosion_sound))

        data.write(b'6\xc0g\xc2')  # 0x36c067c2
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.stalactite_weapon))

        data.write(b'&\x1e\xef\xe7')  # 0x261eefe7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stalactite_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x81\x8f\x81\x0b')  # 0x818f810b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stalactite_shockwave.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'|\x9c;Q')  # 0x7c9c3b51
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper_homing_projectile_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"s\x0f\xe4'")  # 0x730fe427
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper_homing_hover_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x05\t$\xd3')  # 0x50924d3
        data.write(b'\x00\x0c')  # size
        self.hyper_homing_projectile_size.to_stream(data, game)

        data.write(b'd\x14\xe8H')  # 0x6414e848
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_homing_projectile_hp))

        data.write(b'*z-\xa7')  # 0x2a7a2da7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_homing_projectile_stop_homing_dist))

        data.write(b'C\x92\xc3J')  # 0x4392c34a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hand_projectile_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x86\x8eA\x92')  # 0x868e4192
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hand_hover_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc8\xe1eU')  # 0xc8e16555
        data.write(b'\x00\x0c')  # size
        self.hand_projectile_size.to_stream(data, game)

        data.write(b'\x15<\x00\x1b')  # 0x153c001b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hand_projectile_hp))

        data.write(b'G;s\x0b')  # 0x473b730b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hand_projectile_stop_homing_dist))

        data.write(b'\xae\xa6\x0f$')  # 0xaea60f24
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.hand_projectile_damage_effect))

        data.write(b'8xi!')  # 0x38786921
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.hand_projectile_damage_sound))

        data.write(b'\x9ec\x06_')  # 0x9e63065f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.charge_player_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'P\xaenU')  # 0x50ae6e55
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.phazon_drain_projectile_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc6\x9fi\x1a')  # 0xc69f691a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hand_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'1\x96\xb2\xe7')  # 0x3196b2e7
        data.write(b'\x00\x10')  # size
        self.color_hand_of_ur.to_stream(data, game)

        data.write(b'w\xd3\xb3\x86')  # 0x77d3b386
        data.write(b'\x00\x10')  # size
        self.unknown_0x77d3b386.to_stream(data, game)

        data.write(b'\xa9\xbe\x10\x81')  # 0xa9be1081
        data.write(b'\x00\x10')  # size
        self.color_hyper_shockwave.to_stream(data, game)

        data.write(b'|\xe5\xc4|')  # 0x7ce5c47c
        data.write(b'\x00\x10')  # size
        self.color_hyper_homing_shots.to_stream(data, game)

        data.write(b'\xf9el9')  # 0xf9656c39
        data.write(b'\x00\x10')  # size
        self.color_hyper_quake.to_stream(data, game)

        data.write(b'\xd7\x14*\xfe')  # 0xd7142afe
        data.write(b'\x00\x10')  # size
        self.color_energized.to_stream(data, game)

        data.write(b'\xc3q\x8e\xa0')  # 0xc3718ea0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_taunt_time))

        data.write(b'\xd6\xfaZR')  # 0xd6fa5a52
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_taunt_time))

        data.write(b'EiM\xb0')  # 0x45694db0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stage1_settings.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'3\x8ct\x8d')  # 0x338c748d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stage2_settings.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa8\xff\x9eY')  # 0xa8ff9e59
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stage3_settings.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xdeF\x06\xf7')  # 0xde4606f7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stage4_settings.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'(\x83\xf9r')  # 0x2883f972
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shield_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'@\xac\x1f\xd4')  # 0x40ac1fd4
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.foot_contact_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'dX\x81\x14')  # 0x64588114
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x64588114))

        data.write(b'q-2t')  # 0x712d3274
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.approach_player_distance))

        data.write(b'P\xec\x86\xc1')  # 0x50ec86c1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.approach_player_delay))

        data.write(b'Skt\x93')  # 0x536b7493
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.approach_player_time))

        data.write(b'\xc2\xbe2\x8d')  # 0xc2be328d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.orb_color_control.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x02/\xdc\xa5')  # 0x22fdca5
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.orb_missing_scan.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SeedBoss1DataJson", data)
        return cls(
            min_time_between_melee_attacks=json_data['min_time_between_melee_attacks'],
            foot_health=HealthInfo.from_json(json_data['foot_health']),
            foot_vulnerability=DamageVulnerability.from_json(json_data['foot_vulnerability']),
            left_foot=json_data['left_foot'],
            left_knee=json_data['left_knee'],
            left_thigh=json_data['left_thigh'],
            right_foot=json_data['right_foot'],
            right_knee=json_data['right_knee'],
            right_thigh=json_data['right_thigh'],
            stomach_slot_intact=json_data['stomach_slot_intact'],
            stomach_slot_broken=json_data['stomach_slot_broken'],
            stomach_slot_cover=json_data['stomach_slot_cover'],
            back_slot_intact=json_data['back_slot_intact'],
            back_slot_broken=json_data['back_slot_broken'],
            back_slot_cover=json_data['back_slot_cover'],
            shoulder_left_slot_intact=json_data['shoulder_left_slot_intact'],
            shoulder_left_slot_broken=json_data['shoulder_left_slot_broken'],
            shoulder_left_slot_cover=json_data['shoulder_left_slot_cover'],
            shoulder_right_slot_intact=json_data['shoulder_right_slot_intact'],
            shoulder_right_slot_broken=json_data['shoulder_right_slot_broken'],
            shoulder_right_slot_cover=json_data['shoulder_right_slot_cover'],
            head_model=json_data['head_model'],
            jaw_model=json_data['jaw_model'],
            ice_model=json_data['ice_model'],
            head_ice_model=json_data['head_ice_model'],
            jaw_ice_model=json_data['jaw_ice_model'],
            head_vulnerability=DamageVulnerability.from_json(json_data['head_vulnerability']),
            head_frozen_time=json_data['head_frozen_time'],
            shockwave=ShockWaveInfo.from_json(json_data['shockwave']),
            unknown_struct60=UnknownStruct60.from_json(json_data['unknown_struct60']),
            beam_info=PlasmaBeamInfo.from_json(json_data['beam_info']),
            beam_damage_info=DamageInfo.from_json(json_data['beam_damage_info']),
            orb_slot_vulnerability=DamageVulnerability.from_json(json_data['orb_slot_vulnerability']),
            foot_explosion=json_data['foot_explosion'],
            foot_explosion_sound=json_data['foot_explosion_sound'],
            stalactite_weapon=json_data['stalactite_weapon'],
            stalactite_damage=DamageInfo.from_json(json_data['stalactite_damage']),
            stalactite_shockwave=ShockWaveInfo.from_json(json_data['stalactite_shockwave']),
            hyper_homing_projectile_data=LaunchProjectileData.from_json(json_data['hyper_homing_projectile_data']),
            hyper_homing_hover_data=HoverThenHomeProjectile.from_json(json_data['hyper_homing_hover_data']),
            hyper_homing_projectile_size=Vector.from_json(json_data['hyper_homing_projectile_size']),
            hyper_homing_projectile_hp=json_data['hyper_homing_projectile_hp'],
            hyper_homing_projectile_stop_homing_dist=json_data['hyper_homing_projectile_stop_homing_dist'],
            hand_projectile_data=LaunchProjectileData.from_json(json_data['hand_projectile_data']),
            hand_hover_data=HoverThenHomeProjectile.from_json(json_data['hand_hover_data']),
            hand_projectile_size=Vector.from_json(json_data['hand_projectile_size']),
            hand_projectile_hp=json_data['hand_projectile_hp'],
            hand_projectile_stop_homing_dist=json_data['hand_projectile_stop_homing_dist'],
            hand_projectile_damage_effect=json_data['hand_projectile_damage_effect'],
            hand_projectile_damage_sound=json_data['hand_projectile_damage_sound'],
            charge_player_damage=DamageInfo.from_json(json_data['charge_player_damage']),
            phazon_drain_projectile_info=LaunchProjectileData.from_json(json_data['phazon_drain_projectile_info']),
            hand_data=SeedBoss1HandData.from_json(json_data['hand_data']),
            color_hand_of_ur=Color.from_json(json_data['color_hand_of_ur']),
            unknown_0x77d3b386=Color.from_json(json_data['unknown_0x77d3b386']),
            color_hyper_shockwave=Color.from_json(json_data['color_hyper_shockwave']),
            color_hyper_homing_shots=Color.from_json(json_data['color_hyper_homing_shots']),
            color_hyper_quake=Color.from_json(json_data['color_hyper_quake']),
            color_energized=Color.from_json(json_data['color_energized']),
            min_taunt_time=json_data['min_taunt_time'],
            max_taunt_time=json_data['max_taunt_time'],
            stage1_settings=SeedBoss1Stage.from_json(json_data['stage1_settings']),
            stage2_settings=SeedBoss1Stage.from_json(json_data['stage2_settings']),
            stage3_settings=SeedBoss1Stage.from_json(json_data['stage3_settings']),
            stage4_settings=SeedBoss1Stage.from_json(json_data['stage4_settings']),
            shield_info=SeedBoss1Shield.from_json(json_data['shield_info']),
            foot_contact_damage=DamageInfo.from_json(json_data['foot_contact_damage']),
            unknown_0x64588114=json_data['unknown_0x64588114'],
            approach_player_distance=json_data['approach_player_distance'],
            approach_player_delay=json_data['approach_player_delay'],
            approach_player_time=json_data['approach_player_time'],
            orb_color_control=Spline.from_json(json_data['orb_color_control']),
            orb_missing_scan=ScannableParameters.from_json(json_data['orb_missing_scan']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'min_time_between_melee_attacks': self.min_time_between_melee_attacks,
            'foot_health': self.foot_health.to_json(),
            'foot_vulnerability': self.foot_vulnerability.to_json(),
            'left_foot': self.left_foot,
            'left_knee': self.left_knee,
            'left_thigh': self.left_thigh,
            'right_foot': self.right_foot,
            'right_knee': self.right_knee,
            'right_thigh': self.right_thigh,
            'stomach_slot_intact': self.stomach_slot_intact,
            'stomach_slot_broken': self.stomach_slot_broken,
            'stomach_slot_cover': self.stomach_slot_cover,
            'back_slot_intact': self.back_slot_intact,
            'back_slot_broken': self.back_slot_broken,
            'back_slot_cover': self.back_slot_cover,
            'shoulder_left_slot_intact': self.shoulder_left_slot_intact,
            'shoulder_left_slot_broken': self.shoulder_left_slot_broken,
            'shoulder_left_slot_cover': self.shoulder_left_slot_cover,
            'shoulder_right_slot_intact': self.shoulder_right_slot_intact,
            'shoulder_right_slot_broken': self.shoulder_right_slot_broken,
            'shoulder_right_slot_cover': self.shoulder_right_slot_cover,
            'head_model': self.head_model,
            'jaw_model': self.jaw_model,
            'ice_model': self.ice_model,
            'head_ice_model': self.head_ice_model,
            'jaw_ice_model': self.jaw_ice_model,
            'head_vulnerability': self.head_vulnerability.to_json(),
            'head_frozen_time': self.head_frozen_time,
            'shockwave': self.shockwave.to_json(),
            'unknown_struct60': self.unknown_struct60.to_json(),
            'beam_info': self.beam_info.to_json(),
            'beam_damage_info': self.beam_damage_info.to_json(),
            'orb_slot_vulnerability': self.orb_slot_vulnerability.to_json(),
            'foot_explosion': self.foot_explosion,
            'foot_explosion_sound': self.foot_explosion_sound,
            'stalactite_weapon': self.stalactite_weapon,
            'stalactite_damage': self.stalactite_damage.to_json(),
            'stalactite_shockwave': self.stalactite_shockwave.to_json(),
            'hyper_homing_projectile_data': self.hyper_homing_projectile_data.to_json(),
            'hyper_homing_hover_data': self.hyper_homing_hover_data.to_json(),
            'hyper_homing_projectile_size': self.hyper_homing_projectile_size.to_json(),
            'hyper_homing_projectile_hp': self.hyper_homing_projectile_hp,
            'hyper_homing_projectile_stop_homing_dist': self.hyper_homing_projectile_stop_homing_dist,
            'hand_projectile_data': self.hand_projectile_data.to_json(),
            'hand_hover_data': self.hand_hover_data.to_json(),
            'hand_projectile_size': self.hand_projectile_size.to_json(),
            'hand_projectile_hp': self.hand_projectile_hp,
            'hand_projectile_stop_homing_dist': self.hand_projectile_stop_homing_dist,
            'hand_projectile_damage_effect': self.hand_projectile_damage_effect,
            'hand_projectile_damage_sound': self.hand_projectile_damage_sound,
            'charge_player_damage': self.charge_player_damage.to_json(),
            'phazon_drain_projectile_info': self.phazon_drain_projectile_info.to_json(),
            'hand_data': self.hand_data.to_json(),
            'color_hand_of_ur': self.color_hand_of_ur.to_json(),
            'unknown_0x77d3b386': self.unknown_0x77d3b386.to_json(),
            'color_hyper_shockwave': self.color_hyper_shockwave.to_json(),
            'color_hyper_homing_shots': self.color_hyper_homing_shots.to_json(),
            'color_hyper_quake': self.color_hyper_quake.to_json(),
            'color_energized': self.color_energized.to_json(),
            'min_taunt_time': self.min_taunt_time,
            'max_taunt_time': self.max_taunt_time,
            'stage1_settings': self.stage1_settings.to_json(),
            'stage2_settings': self.stage2_settings.to_json(),
            'stage3_settings': self.stage3_settings.to_json(),
            'stage4_settings': self.stage4_settings.to_json(),
            'shield_info': self.shield_info.to_json(),
            'foot_contact_damage': self.foot_contact_damage.to_json(),
            'unknown_0x64588114': self.unknown_0x64588114,
            'approach_player_distance': self.approach_player_distance,
            'approach_player_delay': self.approach_player_delay,
            'approach_player_time': self.approach_player_time,
            'orb_color_control': self.orb_color_control.to_json(),
            'orb_missing_scan': self.orb_missing_scan.to_json(),
        }

    def _dependencies_for_left_foot(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.left_foot)

    def _dependencies_for_left_knee(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.left_knee)

    def _dependencies_for_left_thigh(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.left_thigh)

    def _dependencies_for_right_foot(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.right_foot)

    def _dependencies_for_right_knee(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.right_knee)

    def _dependencies_for_right_thigh(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.right_thigh)

    def _dependencies_for_stomach_slot_intact(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.stomach_slot_intact)

    def _dependencies_for_stomach_slot_broken(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.stomach_slot_broken)

    def _dependencies_for_stomach_slot_cover(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.stomach_slot_cover)

    def _dependencies_for_back_slot_intact(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.back_slot_intact)

    def _dependencies_for_back_slot_broken(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.back_slot_broken)

    def _dependencies_for_back_slot_cover(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.back_slot_cover)

    def _dependencies_for_shoulder_left_slot_intact(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shoulder_left_slot_intact)

    def _dependencies_for_shoulder_left_slot_broken(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shoulder_left_slot_broken)

    def _dependencies_for_shoulder_left_slot_cover(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shoulder_left_slot_cover)

    def _dependencies_for_shoulder_right_slot_intact(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shoulder_right_slot_intact)

    def _dependencies_for_shoulder_right_slot_broken(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shoulder_right_slot_broken)

    def _dependencies_for_shoulder_right_slot_cover(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shoulder_right_slot_cover)

    def _dependencies_for_head_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.head_model)

    def _dependencies_for_jaw_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.jaw_model)

    def _dependencies_for_ice_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ice_model)

    def _dependencies_for_head_ice_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.head_ice_model)

    def _dependencies_for_jaw_ice_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.jaw_ice_model)

    def _dependencies_for_foot_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.foot_explosion)

    def _dependencies_for_foot_explosion_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.foot_explosion_sound)

    def _dependencies_for_stalactite_weapon(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.stalactite_weapon)

    def _dependencies_for_hand_projectile_damage_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.hand_projectile_damage_effect)

    def _dependencies_for_hand_projectile_damage_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.hand_projectile_damage_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_left_foot, "left_foot", "AssetId"),
            (self._dependencies_for_left_knee, "left_knee", "AssetId"),
            (self._dependencies_for_left_thigh, "left_thigh", "AssetId"),
            (self._dependencies_for_right_foot, "right_foot", "AssetId"),
            (self._dependencies_for_right_knee, "right_knee", "AssetId"),
            (self._dependencies_for_right_thigh, "right_thigh", "AssetId"),
            (self._dependencies_for_stomach_slot_intact, "stomach_slot_intact", "AssetId"),
            (self._dependencies_for_stomach_slot_broken, "stomach_slot_broken", "AssetId"),
            (self._dependencies_for_stomach_slot_cover, "stomach_slot_cover", "AssetId"),
            (self._dependencies_for_back_slot_intact, "back_slot_intact", "AssetId"),
            (self._dependencies_for_back_slot_broken, "back_slot_broken", "AssetId"),
            (self._dependencies_for_back_slot_cover, "back_slot_cover", "AssetId"),
            (self._dependencies_for_shoulder_left_slot_intact, "shoulder_left_slot_intact", "AssetId"),
            (self._dependencies_for_shoulder_left_slot_broken, "shoulder_left_slot_broken", "AssetId"),
            (self._dependencies_for_shoulder_left_slot_cover, "shoulder_left_slot_cover", "AssetId"),
            (self._dependencies_for_shoulder_right_slot_intact, "shoulder_right_slot_intact", "AssetId"),
            (self._dependencies_for_shoulder_right_slot_broken, "shoulder_right_slot_broken", "AssetId"),
            (self._dependencies_for_shoulder_right_slot_cover, "shoulder_right_slot_cover", "AssetId"),
            (self._dependencies_for_head_model, "head_model", "AssetId"),
            (self._dependencies_for_jaw_model, "jaw_model", "AssetId"),
            (self._dependencies_for_ice_model, "ice_model", "AssetId"),
            (self._dependencies_for_head_ice_model, "head_ice_model", "AssetId"),
            (self._dependencies_for_jaw_ice_model, "jaw_ice_model", "AssetId"),
            (self.shockwave.dependencies_for, "shockwave", "ShockWaveInfo"),
            (self.unknown_struct60.dependencies_for, "unknown_struct60", "UnknownStruct60"),
            (self.beam_info.dependencies_for, "beam_info", "PlasmaBeamInfo"),
            (self._dependencies_for_foot_explosion, "foot_explosion", "AssetId"),
            (self._dependencies_for_foot_explosion_sound, "foot_explosion_sound", "AssetId"),
            (self._dependencies_for_stalactite_weapon, "stalactite_weapon", "AssetId"),
            (self.stalactite_shockwave.dependencies_for, "stalactite_shockwave", "ShockWaveInfo"),
            (self.hyper_homing_projectile_data.dependencies_for, "hyper_homing_projectile_data", "LaunchProjectileData"),
            (self.hyper_homing_hover_data.dependencies_for, "hyper_homing_hover_data", "HoverThenHomeProjectile"),
            (self.hand_projectile_data.dependencies_for, "hand_projectile_data", "LaunchProjectileData"),
            (self.hand_hover_data.dependencies_for, "hand_hover_data", "HoverThenHomeProjectile"),
            (self._dependencies_for_hand_projectile_damage_effect, "hand_projectile_damage_effect", "AssetId"),
            (self._dependencies_for_hand_projectile_damage_sound, "hand_projectile_damage_sound", "AssetId"),
            (self.phazon_drain_projectile_info.dependencies_for, "phazon_drain_projectile_info", "LaunchProjectileData"),
            (self.hand_data.dependencies_for, "hand_data", "SeedBoss1HandData"),
            (self.shield_info.dependencies_for, "shield_info", "SeedBoss1Shield"),
            (self.orb_missing_scan.dependencies_for, "orb_missing_scan", "ScannableParameters"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for SeedBoss1Data.{field_name} ({field_type}): {e}"
                )


def _decode_foot_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_foot_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_head_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_shockwave(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


def _decode_unknown_struct60(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct60:
    return UnknownStruct60.from_stream(data, game, property_size)


def _decode_beam_info(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size)


def _decode_beam_damage_info(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_orb_slot_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_stalactite_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_stalactite_shockwave(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


def _decode_hyper_homing_projectile_data(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_hyper_homing_hover_data(data: typing.BinaryIO, game: Game, property_size: int) -> HoverThenHomeProjectile:
    return HoverThenHomeProjectile.from_stream(data, game, property_size)


def _decode_hyper_homing_projectile_size(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_hand_projectile_data(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_hand_hover_data(data: typing.BinaryIO, game: Game, property_size: int) -> HoverThenHomeProjectile:
    return HoverThenHomeProjectile.from_stream(data, game, property_size)


def _decode_hand_projectile_size(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_charge_player_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_phazon_drain_projectile_info(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_hand_data(data: typing.BinaryIO, game: Game, property_size: int) -> SeedBoss1HandData:
    return SeedBoss1HandData.from_stream(data, game, property_size)


def _decode_color_hand_of_ur(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x77d3b386(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_color_hyper_shockwave(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_color_hyper_homing_shots(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_color_hyper_quake(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_color_energized(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_stage1_settings(data: typing.BinaryIO, game: Game, property_size: int) -> SeedBoss1Stage:
    return SeedBoss1Stage.from_stream(data, game, property_size)


def _decode_stage2_settings(data: typing.BinaryIO, game: Game, property_size: int) -> SeedBoss1Stage:
    return SeedBoss1Stage.from_stream(data, game, property_size)


def _decode_stage3_settings(data: typing.BinaryIO, game: Game, property_size: int) -> SeedBoss1Stage:
    return SeedBoss1Stage.from_stream(data, game, property_size)


def _decode_stage4_settings(data: typing.BinaryIO, game: Game, property_size: int) -> SeedBoss1Stage:
    return SeedBoss1Stage.from_stream(data, game, property_size)


def _decode_shield_info(data: typing.BinaryIO, game: Game, property_size: int) -> SeedBoss1Shield:
    return SeedBoss1Shield.from_stream(data, game, property_size)


def _decode_foot_contact_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_orb_color_control(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_orb_missing_scan(data: typing.BinaryIO, game: Game, property_size: int) -> ScannableParameters:
    return ScannableParameters.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xd3ad55b6: ('min_time_between_melee_attacks', structs.decode_BIG_f),
    0xb33eb533: ('foot_health', _decode_foot_health),
    0x26fa460b: ('foot_vulnerability', _decode_foot_vulnerability),
    0xad0de5ac: ('left_foot', structs.decode_BIG_Q),
    0xfc128c15: ('left_knee', structs.decode_BIG_Q),
    0x299b8d33: ('left_thigh', structs.decode_BIG_Q),
    0xa5bb98a6: ('right_foot', structs.decode_BIG_Q),
    0xf4a4f11f: ('right_knee', structs.decode_BIG_Q),
    0xc946d250: ('right_thigh', structs.decode_BIG_Q),
    0x50edae7f: ('stomach_slot_intact', structs.decode_BIG_Q),
    0x30969cfe: ('stomach_slot_broken', structs.decode_BIG_Q),
    0xb25e271d: ('stomach_slot_cover', structs.decode_BIG_Q),
    0x5d71b85c: ('back_slot_intact', structs.decode_BIG_Q),
    0x3d0a8add: ('back_slot_broken', structs.decode_BIG_Q),
    0x43223a97: ('back_slot_cover', structs.decode_BIG_Q),
    0x9b76ad84: ('shoulder_left_slot_intact', structs.decode_BIG_Q),
    0xfb0d9f05: ('shoulder_left_slot_broken', structs.decode_BIG_Q),
    0x48ee50ad: ('shoulder_left_slot_cover', structs.decode_BIG_Q),
    0x85635b3b: ('shoulder_right_slot_intact', structs.decode_BIG_Q),
    0xe51869ba: ('shoulder_right_slot_broken', structs.decode_BIG_Q),
    0x5cea873f: ('shoulder_right_slot_cover', structs.decode_BIG_Q),
    0xc288ae69: ('head_model', structs.decode_BIG_Q),
    0xcdbd44e1: ('jaw_model', structs.decode_BIG_Q),
    0x6ad6cbba: ('ice_model', structs.decode_BIG_Q),
    0x3ab79847: ('head_ice_model', structs.decode_BIG_Q),
    0x27b30d35: ('jaw_ice_model', structs.decode_BIG_Q),
    0xec37e2fa: ('head_vulnerability', _decode_head_vulnerability),
    0xccca3249: ('head_frozen_time', structs.decode_BIG_f),
    0x3ce6e482: ('shockwave', _decode_shockwave),
    0x72e00501: ('unknown_struct60', _decode_unknown_struct60),
    0x1598012a: ('beam_info', _decode_beam_info),
    0x98821996: ('beam_damage_info', _decode_beam_damage_info),
    0xdd34c3c0: ('orb_slot_vulnerability', _decode_orb_slot_vulnerability),
    0x547b9a9a: ('foot_explosion', structs.decode_BIG_Q),
    0xeaf93057: ('foot_explosion_sound', structs.decode_BIG_Q),
    0x36c067c2: ('stalactite_weapon', structs.decode_BIG_Q),
    0x261eefe7: ('stalactite_damage', _decode_stalactite_damage),
    0x818f810b: ('stalactite_shockwave', _decode_stalactite_shockwave),
    0x7c9c3b51: ('hyper_homing_projectile_data', _decode_hyper_homing_projectile_data),
    0x730fe427: ('hyper_homing_hover_data', _decode_hyper_homing_hover_data),
    0x050924d3: ('hyper_homing_projectile_size', _decode_hyper_homing_projectile_size),
    0x6414e848: ('hyper_homing_projectile_hp', structs.decode_BIG_f),
    0x2a7a2da7: ('hyper_homing_projectile_stop_homing_dist', structs.decode_BIG_f),
    0x4392c34a: ('hand_projectile_data', _decode_hand_projectile_data),
    0x868e4192: ('hand_hover_data', _decode_hand_hover_data),
    0xc8e16555: ('hand_projectile_size', _decode_hand_projectile_size),
    0x153c001b: ('hand_projectile_hp', structs.decode_BIG_f),
    0x473b730b: ('hand_projectile_stop_homing_dist', structs.decode_BIG_f),
    0xaea60f24: ('hand_projectile_damage_effect', structs.decode_BIG_Q),
    0x38786921: ('hand_projectile_damage_sound', structs.decode_BIG_Q),
    0x9e63065f: ('charge_player_damage', _decode_charge_player_damage),
    0x50ae6e55: ('phazon_drain_projectile_info', _decode_phazon_drain_projectile_info),
    0xc69f691a: ('hand_data', _decode_hand_data),
    0x3196b2e7: ('color_hand_of_ur', _decode_color_hand_of_ur),
    0x77d3b386: ('unknown_0x77d3b386', _decode_unknown_0x77d3b386),
    0xa9be1081: ('color_hyper_shockwave', _decode_color_hyper_shockwave),
    0x7ce5c47c: ('color_hyper_homing_shots', _decode_color_hyper_homing_shots),
    0xf9656c39: ('color_hyper_quake', _decode_color_hyper_quake),
    0xd7142afe: ('color_energized', _decode_color_energized),
    0xc3718ea0: ('min_taunt_time', structs.decode_BIG_f),
    0xd6fa5a52: ('max_taunt_time', structs.decode_BIG_f),
    0x45694db0: ('stage1_settings', _decode_stage1_settings),
    0x338c748d: ('stage2_settings', _decode_stage2_settings),
    0xa8ff9e59: ('stage3_settings', _decode_stage3_settings),
    0xde4606f7: ('stage4_settings', _decode_stage4_settings),
    0x2883f972: ('shield_info', _decode_shield_info),
    0x40ac1fd4: ('foot_contact_damage', _decode_foot_contact_damage),
    0x64588114: ('unknown_0x64588114', structs.decode_BIG_f),
    0x712d3274: ('approach_player_distance', structs.decode_BIG_f),
    0x50ec86c1: ('approach_player_delay', structs.decode_BIG_f),
    0x536b7493: ('approach_player_time', structs.decode_BIG_f),
    0xc2be328d: ('orb_color_control', _decode_orb_color_control),
    0x022fdca5: ('orb_missing_scan', _decode_orb_missing_scan),
}
