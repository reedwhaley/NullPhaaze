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
from retro_data_structures.properties.corruption.archetypes.FlyerMovementMode import FlyerMovementMode
from retro_data_structures.properties.corruption.archetypes.HyperModeData import HyperModeData
from retro_data_structures.properties.corruption.archetypes.LaunchProjectileData import LaunchProjectileData
from retro_data_structures.properties.corruption.archetypes.ScanBeamInfo import ScanBeamInfo

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class PirateDroneDataJson(typing_extensions.TypedDict):
        unknown_0xdfd70ccc: bool
        unknown_0x7e922362: bool
        new_hyper_mode: json_util.JsonObject
        new_hyper_mode_hard: json_util.JsonObject
        new_hyper_mode_elite: json_util.JsonObject
        new_hyper_flight_mode: json_util.JsonObject
        normal_shot_prediction: float
        unknown_0x46353d93: bool
        normal_shot_miss_pitch_max: float
        normal_shot_miss_pitch_min: float
        normal_shot_miss_yaw_max: float
        normal_shot_miss_yaw_min: float
        normal_projectile: json_util.JsonObject
        use_old_hyper_mode: bool
        hyper_shot_prediction: float
        hyper_projectile: json_util.JsonObject
        paint_target_projectile: json_util.JsonObject
        warning_projectile: json_util.JsonObject
        use_flyer_movement_mode: bool
        patrol: json_util.JsonObject
        attack: json_util.JsonObject
        cloak: json_util.JsonObject
        hyper: json_util.JsonObject
        cover: json_util.JsonObject
        side_scroll: json_util.JsonObject
        avoidance_range: float
        height_random_max: float
        height_random_min: float
        floor_buffer: float
        ceiling_buffer: float
        max_lerp: float
        patrol_speed: float
        patrol_acceleration: float
        attack_speed: float
        attack_acceleration: float
        cloak_speed: float
        cloak_acceleration: float
        hyper_speed: float
        hyper_acceleration: float
        cover_speed: float
        cover_acceleration: float
        side_scroller_speed: float
        side_scroller_acceleration: float
        can_strafe: bool
        strafe_burst_shots_max: int
        strafe_burst_shots_min: int
        add_damage_vulnerability: float
        strafe_burst_delay_min: float
        strafe_shot_delay_max: float
        strafe_shot_delay_min: float
        recheck_path_time: float
        recheck_path_distance: float
        path_finding_range: float
        unknown_0x8cd7444d: bool
        scan_delay: float
        side_scroller_mode_enabled: bool
        cloak_enabled: bool
        cloak_time: float
        visor_cloak_threshold: float
        advanced_hyper_mode: bool
        hyper_mode_death_time_max: float
        hyper_mode_death_time_min: float
        hyper_mode_shot_cost: float
        min_dodges_after_attack: int
        max_dodges_after_attack: int
        min_dodges_after_cloak: int
        max_dodges_after_cloak: int
        start_hunting_time: float
        stop_hunting_time: float
        scan_beam_info: json_util.JsonObject
    

@dataclasses.dataclass()
class PirateDroneData(BaseProperty):
    unknown_0xdfd70ccc: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xdfd70ccc, original_name='Unknown'
        ),
    })
    unknown_0x7e922362: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x7e922362, original_name='Unknown'
        ),
    })
    new_hyper_mode: HyperModeData = dataclasses.field(default_factory=HyperModeData, metadata={
        'reflection': FieldReflection[HyperModeData](
            HyperModeData, id=0x4d7f9852, original_name='NewHyperMode', from_json=HyperModeData.from_json, to_json=HyperModeData.to_json
        ),
    })
    new_hyper_mode_hard: HyperModeData = dataclasses.field(default_factory=HyperModeData, metadata={
        'reflection': FieldReflection[HyperModeData](
            HyperModeData, id=0x37b432d6, original_name='NewHyperModeHard', from_json=HyperModeData.from_json, to_json=HyperModeData.to_json
        ),
    })
    new_hyper_mode_elite: HyperModeData = dataclasses.field(default_factory=HyperModeData, metadata={
        'reflection': FieldReflection[HyperModeData](
            HyperModeData, id=0xae27b368, original_name='NewHyperModeElite', from_json=HyperModeData.from_json, to_json=HyperModeData.to_json
        ),
    })
    new_hyper_flight_mode: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0x4b1bc354, original_name='NewHyperFlightMode', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    normal_shot_prediction: float = dataclasses.field(default=0.699999988079071, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb740584d, original_name='NormalShotPrediction'
        ),
    })
    unknown_0x46353d93: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x46353d93, original_name='Unknown'
        ),
    })
    normal_shot_miss_pitch_max: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0b955d7d, original_name='NormalShotMissPitchMax'
        ),
    })
    normal_shot_miss_pitch_min: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xedf5f29c, original_name='NormalShotMissPitchMin'
        ),
    })
    normal_shot_miss_yaw_max: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa75a9e68, original_name='NormalShotMissYawMax'
        ),
    })
    normal_shot_miss_yaw_min: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x413a3189, original_name='NormalShotMissYawMin'
        ),
    })
    normal_projectile: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0x0d1dc128, original_name='NormalProjectile', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    use_old_hyper_mode: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xe37cdbad, original_name='UseOldHyperMode'
        ),
    })
    hyper_shot_prediction: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x08db3464, original_name='HyperShotPrediction'
        ),
    })
    hyper_projectile: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0x7c018c6c, original_name='HyperProjectile', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    paint_target_projectile: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0xd640cf23, original_name='PaintTargetProjectile', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    warning_projectile: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0x1d2c74a8, original_name='WarningProjectile', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    use_flyer_movement_mode: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xc3680c31, original_name='UseFlyerMovementMode'
        ),
    })
    patrol: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0xccdd3aca, original_name='Patrol', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    attack: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0xfa2a173f, original_name='Attack', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    cloak: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0xf9f1c1b1, original_name='Cloak', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    hyper: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0x1c9c4d2b, original_name='Hyper', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    cover: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0xa55d4c94, original_name='Cover', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    side_scroll: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0x89a18334, original_name='SideScroll', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    avoidance_range: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x50a9bd0d, original_name='AvoidanceRange'
        ),
    })
    height_random_max: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x49c38aaf, original_name='HeightRandomMax'
        ),
    })
    height_random_min: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xafa3254e, original_name='HeightRandomMin'
        ),
    })
    floor_buffer: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6581358c, original_name='FloorBuffer'
        ),
    })
    ceiling_buffer: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x115bb38c, original_name='CeilingBuffer'
        ),
    })
    max_lerp: float = dataclasses.field(default=1080.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x81dd389d, original_name='MaxLerp'
        ),
    })
    patrol_speed: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x765c3715, original_name='PatrolSpeed'
        ),
    })
    patrol_acceleration: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3fec085b, original_name='PatrolAcceleration'
        ),
    })
    attack_speed: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6c0a2bc8, original_name='AttackSpeed'
        ),
    })
    attack_acceleration: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x091b25ae, original_name='AttackAcceleration'
        ),
    })
    cloak_speed: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc3e41aaf, original_name='CloakSpeed'
        ),
    })
    cloak_acceleration: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0ac0f320, original_name='CloakAcceleration'
        ),
    })
    hyper_speed: float = dataclasses.field(default=12.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbacb5c8e, original_name='HyperSpeed'
        ),
    })
    hyper_acceleration: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xefad7fba, original_name='HyperAcceleration'
        ),
    })
    cover_speed: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5aaa5277, original_name='CoverSpeed'
        ),
    })
    cover_acceleration: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x566c7e05, original_name='CoverAcceleration'
        ),
    })
    side_scroller_speed: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xab67d302, original_name='SideScrollerSpeed'
        ),
    })
    side_scroller_acceleration: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x128f1b5c, original_name='SideScrollerAcceleration'
        ),
    })
    can_strafe: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x86fb5a9b, original_name='CanStrafe'
        ),
    })
    strafe_burst_shots_max: int = dataclasses.field(default=5, metadata={
        'reflection': FieldReflection[int](
            int, id=0x50e84e20, original_name='StrafeBurstShotsMax'
        ),
    })
    strafe_burst_shots_min: int = dataclasses.field(default=3, metadata={
        'reflection': FieldReflection[int](
            int, id=0x15ea0da2, original_name='StrafeBurstShotsMin'
        ),
    })
    add_damage_vulnerability: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8dd4e38a, original_name='AddDamageVulnerability'
        ),
    })
    strafe_burst_delay_min: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6bb44c6b, original_name='StrafeBurstDelayMin'
        ),
    })
    strafe_shot_delay_max: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0fa5da72, original_name='StrafeShotDelayMax'
        ),
    })
    strafe_shot_delay_min: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe9c57593, original_name='StrafeShotDelayMin'
        ),
    })
    recheck_path_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9aa90b6b, original_name='RecheckPathTime'
        ),
    })
    recheck_path_distance: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7626ec89, original_name='RecheckPathDistance'
        ),
    })
    path_finding_range: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1508b0b1, original_name='PathFindingRange'
        ),
    })
    unknown_0x8cd7444d: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x8cd7444d, original_name='Unknown'
        ),
    })
    scan_delay: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7fc827a2, original_name='ScanDelay'
        ),
    })
    side_scroller_mode_enabled: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x854e412d, original_name='SideScrollerModeEnabled'
        ),
    })
    cloak_enabled: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xfe6ad993, original_name='CloakEnabled'
        ),
    })
    cloak_time: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x388bc31f, original_name='CloakTime'
        ),
    })
    visor_cloak_threshold: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0xda888721, original_name='VisorCloakThreshold'
        ),
    })
    advanced_hyper_mode: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xafe26e84, original_name='AdvancedHyperMode'
        ),
    })
    hyper_mode_death_time_max: float = dataclasses.field(default=90.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0b1b1def, original_name='HyperModeDeathTimeMax'
        ),
    })
    hyper_mode_death_time_min: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xed7bb20e, original_name='HyperModeDeathTimeMin'
        ),
    })
    hyper_mode_shot_cost: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd2d94276, original_name='HyperModeShotCost'
        ),
    })
    min_dodges_after_attack: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x927ed6d8, original_name='MinDodgesAfterAttack'
        ),
    })
    max_dodges_after_attack: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x96e4e7f2, original_name='MaxDodgesAfterAttack'
        ),
    })
    min_dodges_after_cloak: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xa74ef708, original_name='MinDodgesAfterCloak'
        ),
    })
    max_dodges_after_cloak: int = dataclasses.field(default=2, metadata={
        'reflection': FieldReflection[int](
            int, id=0xe659c88e, original_name='MaxDodgesAfterCloak'
        ),
    })
    start_hunting_time: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x10bbdfd1, original_name='StartHuntingTime'
        ),
    })
    stop_hunting_time: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe201a83d, original_name='StopHuntingTime'
        ),
    })
    scan_beam_info: ScanBeamInfo = dataclasses.field(default_factory=ScanBeamInfo, metadata={
        'reflection': FieldReflection[ScanBeamInfo](
            ScanBeamInfo, id=0x79f06459, original_name='ScanBeamInfo', from_json=ScanBeamInfo.from_json, to_json=ScanBeamInfo.to_json
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
        if property_count != 70:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdfd70ccc
        unknown_0xdfd70ccc = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e922362
        unknown_0x7e922362 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4d7f9852
        new_hyper_mode = HyperModeData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x37b432d6
        new_hyper_mode_hard = HyperModeData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xae27b368
        new_hyper_mode_elite = HyperModeData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4b1bc354
        new_hyper_flight_mode = FlyerMovementMode.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb740584d
        normal_shot_prediction = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x46353d93
        unknown_0x46353d93 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0b955d7d
        normal_shot_miss_pitch_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xedf5f29c
        normal_shot_miss_pitch_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa75a9e68
        normal_shot_miss_yaw_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x413a3189
        normal_shot_miss_yaw_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0d1dc128
        normal_projectile = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe37cdbad
        use_old_hyper_mode = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08db3464
        hyper_shot_prediction = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7c018c6c
        hyper_projectile = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd640cf23
        paint_target_projectile = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1d2c74a8
        warning_projectile = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc3680c31
        use_flyer_movement_mode = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xccdd3aca
        patrol = FlyerMovementMode.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfa2a173f
        attack = FlyerMovementMode.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf9f1c1b1
        cloak = FlyerMovementMode.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1c9c4d2b
        hyper = FlyerMovementMode.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa55d4c94
        cover = FlyerMovementMode.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x89a18334
        side_scroll = FlyerMovementMode.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50a9bd0d
        avoidance_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49c38aaf
        height_random_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xafa3254e
        height_random_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6581358c
        floor_buffer = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x115bb38c
        ceiling_buffer = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x81dd389d
        max_lerp = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x765c3715
        patrol_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3fec085b
        patrol_acceleration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6c0a2bc8
        attack_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x091b25ae
        attack_acceleration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc3e41aaf
        cloak_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0ac0f320
        cloak_acceleration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbacb5c8e
        hyper_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xefad7fba
        hyper_acceleration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5aaa5277
        cover_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x566c7e05
        cover_acceleration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xab67d302
        side_scroller_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x128f1b5c
        side_scroller_acceleration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x86fb5a9b
        can_strafe = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50e84e20
        strafe_burst_shots_max = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x15ea0da2
        strafe_burst_shots_min = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8dd4e38a
        add_damage_vulnerability = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6bb44c6b
        strafe_burst_delay_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0fa5da72
        strafe_shot_delay_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe9c57593
        strafe_shot_delay_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9aa90b6b
        recheck_path_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7626ec89
        recheck_path_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1508b0b1
        path_finding_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8cd7444d
        unknown_0x8cd7444d = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7fc827a2
        scan_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x854e412d
        side_scroller_mode_enabled = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfe6ad993
        cloak_enabled = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x388bc31f
        cloak_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xda888721
        visor_cloak_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xafe26e84
        advanced_hyper_mode = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0b1b1def
        hyper_mode_death_time_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed7bb20e
        hyper_mode_death_time_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd2d94276
        hyper_mode_shot_cost = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x927ed6d8
        min_dodges_after_attack = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x96e4e7f2
        max_dodges_after_attack = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa74ef708
        min_dodges_after_cloak = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe659c88e
        max_dodges_after_cloak = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x10bbdfd1
        start_hunting_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe201a83d
        stop_hunting_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x79f06459
        scan_beam_info = ScanBeamInfo.from_stream(data, game, property_size)
    
        return cls(unknown_0xdfd70ccc, unknown_0x7e922362, new_hyper_mode, new_hyper_mode_hard, new_hyper_mode_elite, new_hyper_flight_mode, normal_shot_prediction, unknown_0x46353d93, normal_shot_miss_pitch_max, normal_shot_miss_pitch_min, normal_shot_miss_yaw_max, normal_shot_miss_yaw_min, normal_projectile, use_old_hyper_mode, hyper_shot_prediction, hyper_projectile, paint_target_projectile, warning_projectile, use_flyer_movement_mode, patrol, attack, cloak, hyper, cover, side_scroll, avoidance_range, height_random_max, height_random_min, floor_buffer, ceiling_buffer, max_lerp, patrol_speed, patrol_acceleration, attack_speed, attack_acceleration, cloak_speed, cloak_acceleration, hyper_speed, hyper_acceleration, cover_speed, cover_acceleration, side_scroller_speed, side_scroller_acceleration, can_strafe, strafe_burst_shots_max, strafe_burst_shots_min, add_damage_vulnerability, strafe_burst_delay_min, strafe_shot_delay_max, strafe_shot_delay_min, recheck_path_time, recheck_path_distance, path_finding_range, unknown_0x8cd7444d, scan_delay, side_scroller_mode_enabled, cloak_enabled, cloak_time, visor_cloak_threshold, advanced_hyper_mode, hyper_mode_death_time_max, hyper_mode_death_time_min, hyper_mode_shot_cost, min_dodges_after_attack, max_dodges_after_attack, min_dodges_after_cloak, max_dodges_after_cloak, start_hunting_time, stop_hunting_time, scan_beam_info)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00F')  # 70 properties

        data.write(b'\xdf\xd7\x0c\xcc')  # 0xdfd70ccc
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xdfd70ccc))

        data.write(b'~\x92#b')  # 0x7e922362
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x7e922362))

        data.write(b'M\x7f\x98R')  # 0x4d7f9852
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.new_hyper_mode.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'7\xb42\xd6')  # 0x37b432d6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.new_hyper_mode_hard.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xae'\xb3h")  # 0xae27b368
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.new_hyper_mode_elite.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'K\x1b\xc3T')  # 0x4b1bc354
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.new_hyper_flight_mode.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb7@XM')  # 0xb740584d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.normal_shot_prediction))

        data.write(b'F5=\x93')  # 0x46353d93
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x46353d93))

        data.write(b'\x0b\x95]}')  # 0xb955d7d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.normal_shot_miss_pitch_max))

        data.write(b'\xed\xf5\xf2\x9c')  # 0xedf5f29c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.normal_shot_miss_pitch_min))

        data.write(b'\xa7Z\x9eh')  # 0xa75a9e68
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.normal_shot_miss_yaw_max))

        data.write(b'A:1\x89')  # 0x413a3189
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.normal_shot_miss_yaw_min))

        data.write(b'\r\x1d\xc1(')  # 0xd1dc128
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.normal_projectile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe3|\xdb\xad')  # 0xe37cdbad
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.use_old_hyper_mode))

        data.write(b'\x08\xdb4d')  # 0x8db3464
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_shot_prediction))

        data.write(b'|\x01\x8cl')  # 0x7c018c6c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper_projectile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd6@\xcf#')  # 0xd640cf23
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.paint_target_projectile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x1d,t\xa8')  # 0x1d2c74a8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.warning_projectile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc3h\x0c1')  # 0xc3680c31
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.use_flyer_movement_mode))

        data.write(b'\xcc\xdd:\xca')  # 0xccdd3aca
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.patrol.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfa*\x17?')  # 0xfa2a173f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.attack.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf9\xf1\xc1\xb1')  # 0xf9f1c1b1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.cloak.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x1c\x9cM+')  # 0x1c9c4d2b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa5]L\x94')  # 0xa55d4c94
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.cover.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x89\xa1\x834')  # 0x89a18334
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.side_scroll.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'P\xa9\xbd\r')  # 0x50a9bd0d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.avoidance_range))

        data.write(b'I\xc3\x8a\xaf')  # 0x49c38aaf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.height_random_max))

        data.write(b'\xaf\xa3%N')  # 0xafa3254e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.height_random_min))

        data.write(b'e\x815\x8c')  # 0x6581358c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.floor_buffer))

        data.write(b'\x11[\xb3\x8c')  # 0x115bb38c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ceiling_buffer))

        data.write(b'\x81\xdd8\x9d')  # 0x81dd389d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_lerp))

        data.write(b'v\\7\x15')  # 0x765c3715
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.patrol_speed))

        data.write(b'?\xec\x08[')  # 0x3fec085b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.patrol_acceleration))

        data.write(b'l\n+\xc8')  # 0x6c0a2bc8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.attack_speed))

        data.write(b'\t\x1b%\xae')  # 0x91b25ae
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.attack_acceleration))

        data.write(b'\xc3\xe4\x1a\xaf')  # 0xc3e41aaf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.cloak_speed))

        data.write(b'\n\xc0\xf3 ')  # 0xac0f320
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.cloak_acceleration))

        data.write(b'\xba\xcb\\\x8e')  # 0xbacb5c8e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_speed))

        data.write(b'\xef\xad\x7f\xba')  # 0xefad7fba
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_acceleration))

        data.write(b'Z\xaaRw')  # 0x5aaa5277
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.cover_speed))

        data.write(b'Vl~\x05')  # 0x566c7e05
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.cover_acceleration))

        data.write(b'\xabg\xd3\x02')  # 0xab67d302
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.side_scroller_speed))

        data.write(b'\x12\x8f\x1b\\')  # 0x128f1b5c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.side_scroller_acceleration))

        data.write(b'\x86\xfbZ\x9b')  # 0x86fb5a9b
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.can_strafe))

        data.write(b'P\xe8N ')  # 0x50e84e20
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.strafe_burst_shots_max))

        data.write(b'\x15\xea\r\xa2')  # 0x15ea0da2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.strafe_burst_shots_min))

        data.write(b'\x8d\xd4\xe3\x8a')  # 0x8dd4e38a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.add_damage_vulnerability))

        data.write(b'k\xb4Lk')  # 0x6bb44c6b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.strafe_burst_delay_min))

        data.write(b'\x0f\xa5\xdar')  # 0xfa5da72
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.strafe_shot_delay_max))

        data.write(b'\xe9\xc5u\x93')  # 0xe9c57593
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.strafe_shot_delay_min))

        data.write(b'\x9a\xa9\x0bk')  # 0x9aa90b6b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.recheck_path_time))

        data.write(b'v&\xec\x89')  # 0x7626ec89
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.recheck_path_distance))

        data.write(b'\x15\x08\xb0\xb1')  # 0x1508b0b1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.path_finding_range))

        data.write(b'\x8c\xd7DM')  # 0x8cd7444d
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x8cd7444d))

        data.write(b"\x7f\xc8'\xa2")  # 0x7fc827a2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_delay))

        data.write(b'\x85NA-')  # 0x854e412d
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.side_scroller_mode_enabled))

        data.write(b'\xfej\xd9\x93')  # 0xfe6ad993
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.cloak_enabled))

        data.write(b'8\x8b\xc3\x1f')  # 0x388bc31f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.cloak_time))

        data.write(b'\xda\x88\x87!')  # 0xda888721
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.visor_cloak_threshold))

        data.write(b'\xaf\xe2n\x84')  # 0xafe26e84
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.advanced_hyper_mode))

        data.write(b'\x0b\x1b\x1d\xef')  # 0xb1b1def
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_death_time_max))

        data.write(b'\xed{\xb2\x0e')  # 0xed7bb20e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_death_time_min))

        data.write(b'\xd2\xd9Bv')  # 0xd2d94276
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_shot_cost))

        data.write(b'\x92~\xd6\xd8')  # 0x927ed6d8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.min_dodges_after_attack))

        data.write(b'\x96\xe4\xe7\xf2')  # 0x96e4e7f2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_dodges_after_attack))

        data.write(b'\xa7N\xf7\x08')  # 0xa74ef708
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.min_dodges_after_cloak))

        data.write(b'\xe6Y\xc8\x8e')  # 0xe659c88e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_dodges_after_cloak))

        data.write(b'\x10\xbb\xdf\xd1')  # 0x10bbdfd1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.start_hunting_time))

        data.write(b'\xe2\x01\xa8=')  # 0xe201a83d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stop_hunting_time))

        data.write(b'y\xf0dY')  # 0x79f06459
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.scan_beam_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PirateDroneDataJson", data)
        return cls(
            unknown_0xdfd70ccc=json_data['unknown_0xdfd70ccc'],
            unknown_0x7e922362=json_data['unknown_0x7e922362'],
            new_hyper_mode=HyperModeData.from_json(json_data['new_hyper_mode']),
            new_hyper_mode_hard=HyperModeData.from_json(json_data['new_hyper_mode_hard']),
            new_hyper_mode_elite=HyperModeData.from_json(json_data['new_hyper_mode_elite']),
            new_hyper_flight_mode=FlyerMovementMode.from_json(json_data['new_hyper_flight_mode']),
            normal_shot_prediction=json_data['normal_shot_prediction'],
            unknown_0x46353d93=json_data['unknown_0x46353d93'],
            normal_shot_miss_pitch_max=json_data['normal_shot_miss_pitch_max'],
            normal_shot_miss_pitch_min=json_data['normal_shot_miss_pitch_min'],
            normal_shot_miss_yaw_max=json_data['normal_shot_miss_yaw_max'],
            normal_shot_miss_yaw_min=json_data['normal_shot_miss_yaw_min'],
            normal_projectile=LaunchProjectileData.from_json(json_data['normal_projectile']),
            use_old_hyper_mode=json_data['use_old_hyper_mode'],
            hyper_shot_prediction=json_data['hyper_shot_prediction'],
            hyper_projectile=LaunchProjectileData.from_json(json_data['hyper_projectile']),
            paint_target_projectile=LaunchProjectileData.from_json(json_data['paint_target_projectile']),
            warning_projectile=LaunchProjectileData.from_json(json_data['warning_projectile']),
            use_flyer_movement_mode=json_data['use_flyer_movement_mode'],
            patrol=FlyerMovementMode.from_json(json_data['patrol']),
            attack=FlyerMovementMode.from_json(json_data['attack']),
            cloak=FlyerMovementMode.from_json(json_data['cloak']),
            hyper=FlyerMovementMode.from_json(json_data['hyper']),
            cover=FlyerMovementMode.from_json(json_data['cover']),
            side_scroll=FlyerMovementMode.from_json(json_data['side_scroll']),
            avoidance_range=json_data['avoidance_range'],
            height_random_max=json_data['height_random_max'],
            height_random_min=json_data['height_random_min'],
            floor_buffer=json_data['floor_buffer'],
            ceiling_buffer=json_data['ceiling_buffer'],
            max_lerp=json_data['max_lerp'],
            patrol_speed=json_data['patrol_speed'],
            patrol_acceleration=json_data['patrol_acceleration'],
            attack_speed=json_data['attack_speed'],
            attack_acceleration=json_data['attack_acceleration'],
            cloak_speed=json_data['cloak_speed'],
            cloak_acceleration=json_data['cloak_acceleration'],
            hyper_speed=json_data['hyper_speed'],
            hyper_acceleration=json_data['hyper_acceleration'],
            cover_speed=json_data['cover_speed'],
            cover_acceleration=json_data['cover_acceleration'],
            side_scroller_speed=json_data['side_scroller_speed'],
            side_scroller_acceleration=json_data['side_scroller_acceleration'],
            can_strafe=json_data['can_strafe'],
            strafe_burst_shots_max=json_data['strafe_burst_shots_max'],
            strafe_burst_shots_min=json_data['strafe_burst_shots_min'],
            add_damage_vulnerability=json_data['add_damage_vulnerability'],
            strafe_burst_delay_min=json_data['strafe_burst_delay_min'],
            strafe_shot_delay_max=json_data['strafe_shot_delay_max'],
            strafe_shot_delay_min=json_data['strafe_shot_delay_min'],
            recheck_path_time=json_data['recheck_path_time'],
            recheck_path_distance=json_data['recheck_path_distance'],
            path_finding_range=json_data['path_finding_range'],
            unknown_0x8cd7444d=json_data['unknown_0x8cd7444d'],
            scan_delay=json_data['scan_delay'],
            side_scroller_mode_enabled=json_data['side_scroller_mode_enabled'],
            cloak_enabled=json_data['cloak_enabled'],
            cloak_time=json_data['cloak_time'],
            visor_cloak_threshold=json_data['visor_cloak_threshold'],
            advanced_hyper_mode=json_data['advanced_hyper_mode'],
            hyper_mode_death_time_max=json_data['hyper_mode_death_time_max'],
            hyper_mode_death_time_min=json_data['hyper_mode_death_time_min'],
            hyper_mode_shot_cost=json_data['hyper_mode_shot_cost'],
            min_dodges_after_attack=json_data['min_dodges_after_attack'],
            max_dodges_after_attack=json_data['max_dodges_after_attack'],
            min_dodges_after_cloak=json_data['min_dodges_after_cloak'],
            max_dodges_after_cloak=json_data['max_dodges_after_cloak'],
            start_hunting_time=json_data['start_hunting_time'],
            stop_hunting_time=json_data['stop_hunting_time'],
            scan_beam_info=ScanBeamInfo.from_json(json_data['scan_beam_info']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'unknown_0xdfd70ccc': self.unknown_0xdfd70ccc,
            'unknown_0x7e922362': self.unknown_0x7e922362,
            'new_hyper_mode': self.new_hyper_mode.to_json(),
            'new_hyper_mode_hard': self.new_hyper_mode_hard.to_json(),
            'new_hyper_mode_elite': self.new_hyper_mode_elite.to_json(),
            'new_hyper_flight_mode': self.new_hyper_flight_mode.to_json(),
            'normal_shot_prediction': self.normal_shot_prediction,
            'unknown_0x46353d93': self.unknown_0x46353d93,
            'normal_shot_miss_pitch_max': self.normal_shot_miss_pitch_max,
            'normal_shot_miss_pitch_min': self.normal_shot_miss_pitch_min,
            'normal_shot_miss_yaw_max': self.normal_shot_miss_yaw_max,
            'normal_shot_miss_yaw_min': self.normal_shot_miss_yaw_min,
            'normal_projectile': self.normal_projectile.to_json(),
            'use_old_hyper_mode': self.use_old_hyper_mode,
            'hyper_shot_prediction': self.hyper_shot_prediction,
            'hyper_projectile': self.hyper_projectile.to_json(),
            'paint_target_projectile': self.paint_target_projectile.to_json(),
            'warning_projectile': self.warning_projectile.to_json(),
            'use_flyer_movement_mode': self.use_flyer_movement_mode,
            'patrol': self.patrol.to_json(),
            'attack': self.attack.to_json(),
            'cloak': self.cloak.to_json(),
            'hyper': self.hyper.to_json(),
            'cover': self.cover.to_json(),
            'side_scroll': self.side_scroll.to_json(),
            'avoidance_range': self.avoidance_range,
            'height_random_max': self.height_random_max,
            'height_random_min': self.height_random_min,
            'floor_buffer': self.floor_buffer,
            'ceiling_buffer': self.ceiling_buffer,
            'max_lerp': self.max_lerp,
            'patrol_speed': self.patrol_speed,
            'patrol_acceleration': self.patrol_acceleration,
            'attack_speed': self.attack_speed,
            'attack_acceleration': self.attack_acceleration,
            'cloak_speed': self.cloak_speed,
            'cloak_acceleration': self.cloak_acceleration,
            'hyper_speed': self.hyper_speed,
            'hyper_acceleration': self.hyper_acceleration,
            'cover_speed': self.cover_speed,
            'cover_acceleration': self.cover_acceleration,
            'side_scroller_speed': self.side_scroller_speed,
            'side_scroller_acceleration': self.side_scroller_acceleration,
            'can_strafe': self.can_strafe,
            'strafe_burst_shots_max': self.strafe_burst_shots_max,
            'strafe_burst_shots_min': self.strafe_burst_shots_min,
            'add_damage_vulnerability': self.add_damage_vulnerability,
            'strafe_burst_delay_min': self.strafe_burst_delay_min,
            'strafe_shot_delay_max': self.strafe_shot_delay_max,
            'strafe_shot_delay_min': self.strafe_shot_delay_min,
            'recheck_path_time': self.recheck_path_time,
            'recheck_path_distance': self.recheck_path_distance,
            'path_finding_range': self.path_finding_range,
            'unknown_0x8cd7444d': self.unknown_0x8cd7444d,
            'scan_delay': self.scan_delay,
            'side_scroller_mode_enabled': self.side_scroller_mode_enabled,
            'cloak_enabled': self.cloak_enabled,
            'cloak_time': self.cloak_time,
            'visor_cloak_threshold': self.visor_cloak_threshold,
            'advanced_hyper_mode': self.advanced_hyper_mode,
            'hyper_mode_death_time_max': self.hyper_mode_death_time_max,
            'hyper_mode_death_time_min': self.hyper_mode_death_time_min,
            'hyper_mode_shot_cost': self.hyper_mode_shot_cost,
            'min_dodges_after_attack': self.min_dodges_after_attack,
            'max_dodges_after_attack': self.max_dodges_after_attack,
            'min_dodges_after_cloak': self.min_dodges_after_cloak,
            'max_dodges_after_cloak': self.max_dodges_after_cloak,
            'start_hunting_time': self.start_hunting_time,
            'stop_hunting_time': self.stop_hunting_time,
            'scan_beam_info': self.scan_beam_info.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.new_hyper_mode.dependencies_for, "new_hyper_mode", "HyperModeData"),
            (self.new_hyper_mode_hard.dependencies_for, "new_hyper_mode_hard", "HyperModeData"),
            (self.new_hyper_mode_elite.dependencies_for, "new_hyper_mode_elite", "HyperModeData"),
            (self.normal_projectile.dependencies_for, "normal_projectile", "LaunchProjectileData"),
            (self.hyper_projectile.dependencies_for, "hyper_projectile", "LaunchProjectileData"),
            (self.paint_target_projectile.dependencies_for, "paint_target_projectile", "LaunchProjectileData"),
            (self.warning_projectile.dependencies_for, "warning_projectile", "LaunchProjectileData"),
            (self.scan_beam_info.dependencies_for, "scan_beam_info", "ScanBeamInfo"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for PirateDroneData.{field_name} ({field_type}): {e}"
                )


def _decode_new_hyper_mode(data: typing.BinaryIO, game: Game, property_size: int) -> HyperModeData:
    return HyperModeData.from_stream(data, game, property_size)


def _decode_new_hyper_mode_hard(data: typing.BinaryIO, game: Game, property_size: int) -> HyperModeData:
    return HyperModeData.from_stream(data, game, property_size)


def _decode_new_hyper_mode_elite(data: typing.BinaryIO, game: Game, property_size: int) -> HyperModeData:
    return HyperModeData.from_stream(data, game, property_size)


def _decode_new_hyper_flight_mode(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_normal_projectile(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_hyper_projectile(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_paint_target_projectile(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_warning_projectile(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_patrol(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_attack(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_cloak(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_hyper(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_cover(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_side_scroll(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_scan_beam_info(data: typing.BinaryIO, game: Game, property_size: int) -> ScanBeamInfo:
    return ScanBeamInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xdfd70ccc: ('unknown_0xdfd70ccc', structs.decode_BIG_bool_),
    0x7e922362: ('unknown_0x7e922362', structs.decode_BIG_bool_),
    0x4d7f9852: ('new_hyper_mode', _decode_new_hyper_mode),
    0x37b432d6: ('new_hyper_mode_hard', _decode_new_hyper_mode_hard),
    0xae27b368: ('new_hyper_mode_elite', _decode_new_hyper_mode_elite),
    0x4b1bc354: ('new_hyper_flight_mode', _decode_new_hyper_flight_mode),
    0xb740584d: ('normal_shot_prediction', structs.decode_BIG_f),
    0x46353d93: ('unknown_0x46353d93', structs.decode_BIG_bool_),
    0x0b955d7d: ('normal_shot_miss_pitch_max', structs.decode_BIG_f),
    0xedf5f29c: ('normal_shot_miss_pitch_min', structs.decode_BIG_f),
    0xa75a9e68: ('normal_shot_miss_yaw_max', structs.decode_BIG_f),
    0x413a3189: ('normal_shot_miss_yaw_min', structs.decode_BIG_f),
    0x0d1dc128: ('normal_projectile', _decode_normal_projectile),
    0xe37cdbad: ('use_old_hyper_mode', structs.decode_BIG_bool_),
    0x08db3464: ('hyper_shot_prediction', structs.decode_BIG_f),
    0x7c018c6c: ('hyper_projectile', _decode_hyper_projectile),
    0xd640cf23: ('paint_target_projectile', _decode_paint_target_projectile),
    0x1d2c74a8: ('warning_projectile', _decode_warning_projectile),
    0xc3680c31: ('use_flyer_movement_mode', structs.decode_BIG_bool_),
    0xccdd3aca: ('patrol', _decode_patrol),
    0xfa2a173f: ('attack', _decode_attack),
    0xf9f1c1b1: ('cloak', _decode_cloak),
    0x1c9c4d2b: ('hyper', _decode_hyper),
    0xa55d4c94: ('cover', _decode_cover),
    0x89a18334: ('side_scroll', _decode_side_scroll),
    0x50a9bd0d: ('avoidance_range', structs.decode_BIG_f),
    0x49c38aaf: ('height_random_max', structs.decode_BIG_f),
    0xafa3254e: ('height_random_min', structs.decode_BIG_f),
    0x6581358c: ('floor_buffer', structs.decode_BIG_f),
    0x115bb38c: ('ceiling_buffer', structs.decode_BIG_f),
    0x81dd389d: ('max_lerp', structs.decode_BIG_f),
    0x765c3715: ('patrol_speed', structs.decode_BIG_f),
    0x3fec085b: ('patrol_acceleration', structs.decode_BIG_f),
    0x6c0a2bc8: ('attack_speed', structs.decode_BIG_f),
    0x091b25ae: ('attack_acceleration', structs.decode_BIG_f),
    0xc3e41aaf: ('cloak_speed', structs.decode_BIG_f),
    0x0ac0f320: ('cloak_acceleration', structs.decode_BIG_f),
    0xbacb5c8e: ('hyper_speed', structs.decode_BIG_f),
    0xefad7fba: ('hyper_acceleration', structs.decode_BIG_f),
    0x5aaa5277: ('cover_speed', structs.decode_BIG_f),
    0x566c7e05: ('cover_acceleration', structs.decode_BIG_f),
    0xab67d302: ('side_scroller_speed', structs.decode_BIG_f),
    0x128f1b5c: ('side_scroller_acceleration', structs.decode_BIG_f),
    0x86fb5a9b: ('can_strafe', structs.decode_BIG_bool_),
    0x50e84e20: ('strafe_burst_shots_max', structs.decode_BIG_l),
    0x15ea0da2: ('strafe_burst_shots_min', structs.decode_BIG_l),
    0x8dd4e38a: ('add_damage_vulnerability', structs.decode_BIG_f),
    0x6bb44c6b: ('strafe_burst_delay_min', structs.decode_BIG_f),
    0x0fa5da72: ('strafe_shot_delay_max', structs.decode_BIG_f),
    0xe9c57593: ('strafe_shot_delay_min', structs.decode_BIG_f),
    0x9aa90b6b: ('recheck_path_time', structs.decode_BIG_f),
    0x7626ec89: ('recheck_path_distance', structs.decode_BIG_f),
    0x1508b0b1: ('path_finding_range', structs.decode_BIG_f),
    0x8cd7444d: ('unknown_0x8cd7444d', structs.decode_BIG_bool_),
    0x7fc827a2: ('scan_delay', structs.decode_BIG_f),
    0x854e412d: ('side_scroller_mode_enabled', structs.decode_BIG_bool_),
    0xfe6ad993: ('cloak_enabled', structs.decode_BIG_bool_),
    0x388bc31f: ('cloak_time', structs.decode_BIG_f),
    0xda888721: ('visor_cloak_threshold', structs.decode_BIG_f),
    0xafe26e84: ('advanced_hyper_mode', structs.decode_BIG_bool_),
    0x0b1b1def: ('hyper_mode_death_time_max', structs.decode_BIG_f),
    0xed7bb20e: ('hyper_mode_death_time_min', structs.decode_BIG_f),
    0xd2d94276: ('hyper_mode_shot_cost', structs.decode_BIG_f),
    0x927ed6d8: ('min_dodges_after_attack', structs.decode_BIG_l),
    0x96e4e7f2: ('max_dodges_after_attack', structs.decode_BIG_l),
    0xa74ef708: ('min_dodges_after_cloak', structs.decode_BIG_l),
    0xe659c88e: ('max_dodges_after_cloak', structs.decode_BIG_l),
    0x10bbdfd1: ('start_hunting_time', structs.decode_BIG_f),
    0xe201a83d: ('stop_hunting_time', structs.decode_BIG_f),
    0x79f06459: ('scan_beam_info', _decode_scan_beam_info),
}
