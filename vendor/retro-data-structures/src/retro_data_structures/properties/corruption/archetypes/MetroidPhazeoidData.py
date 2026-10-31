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
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.ElectricBeamInfo import ElectricBeamInfo
from retro_data_structures.properties.corruption.archetypes.FlyerMovementMode import FlyerMovementMode
from retro_data_structures.properties.corruption.archetypes.MetroidPhazeoidStruct import MetroidPhazeoidStruct
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class MetroidPhazeoidDataJson(typing_extensions.TypedDict):
        disable_player_grab: bool
        disable_pirate_grab: bool
        disable_hungry_mode: bool
        post_hatch_scale: float
        post_hatch_scale_speed: float
        post_hatch_rotation_speed: float
        recheck_path_time: float
        recheck_path_distance: float
        scan_delay: float
        patrol: json_util.JsonObject
        attack: json_util.JsonObject
        hungry: json_util.JsonObject
        face_lunge: json_util.JsonObject
        ball_lunge: json_util.JsonObject
        ball_lift: json_util.JsonObject
        initial_vulnerability: json_util.JsonObject
        hungry_vulnerability: json_util.JsonObject
        ball_lift_vulnerability: json_util.JsonObject
        phase_out_vulnerability: json_util.JsonObject
        phase_out_radius_missile: float
        metroid_phazeoid_struct_0x7c187bd0: json_util.JsonObject
        metroid_phazeoid_struct_0x0c7b243d: json_util.JsonObject
        metroid_phazeoid_struct_0x33b1809f: json_util.JsonObject
        metroid_phazeoid_struct_0x0ec6856a: json_util.JsonObject
        metroid_phazeoid_struct_0x61fab47a: json_util.JsonObject
        metroid_phazeoid_struct_0x26aac761: json_util.JsonObject
        brain_vulnerability: json_util.JsonObject
        x_ray_brain_radius: float
        normal_brain_radius: float
        phase_out_time_min: float
        phase_out_time_max: float
        phase_in_time_min: float
        phase_in_time_max: float
        target_phase_opacity_min: float
        target_phase_opacity_max: float
        unknown_0xa77f2fe5: float
        unknown_0x411f8004: float
        hungry_phase_out_chance_max: float
        hungry_phase_out_chance_min: float
        hungry_phase_out_chance_reduction: float
        hungry_phase_out_chance_regen: float
        arc_range_min: float
        arc_range_max: float
        arc_range_ball_lift_min: float
        arc_range_ball_lift_max: float
        arc_attack: json_util.JsonObject
        lunge_range_min: float
        lunge_range_max: float
        hug_radius_multiplier: float
        energy_drain: json_util.JsonObject
        max_energy_drain_allowed: float
        max_static_intensity: float
        ball_lift_delay_min: float
        ball_lift_delay_max: float
        ball_lift_zap_delay_min: float
        ball_lift_zap_delay_max: float
        hug_attack_delay_min: float
        hug_attack_delay_max: float
        hungry_damage_threshold: float
        unknown_0x677e48ea: bool
        unknown_0x7edf931d: bool
        unknown_0x15283674: bool
        unknown_0x1ae10f78: float
        unknown_0x93f9240c: float
        max_dist_off_mesh: float
        phase_out_dist_off_mesh: float
        arc_effect: int
        arc_explosion: int
        sound_arc_explosion: int
        arc_number: int
        arc_length: float
        arc_move_time_max: float
        arc_move_time_min: float
        arc_on_time_max: float
        arc_on_time_min: float
        path_find_height: float
        unknown_0x6fc4508c: float
        unknown_0x7de8da8d: float
        unknown_0xf67dbaab: float
        blur_radius: float
        blur_duration: float
    

@dataclasses.dataclass()
class MetroidPhazeoidData(BaseProperty):
    disable_player_grab: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x74288ef3, original_name='DisablePlayerGrab'
        ),
    })
    disable_pirate_grab: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x0679e20c, original_name='DisablePirateGrab'
        ),
    })
    disable_hungry_mode: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xae46d80e, original_name='DisableHungryMode'
        ),
    })
    post_hatch_scale: float = dataclasses.field(default=0.6600000262260437, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbd62d02e, original_name='PostHatchScale'
        ),
    })
    post_hatch_scale_speed: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0xef6d8c96, original_name='PostHatchScaleSpeed'
        ),
    })
    post_hatch_rotation_speed: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x763e71ae, original_name='PostHatchRotationSpeed'
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
    scan_delay: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7fc827a2, original_name='ScanDelay'
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
    hungry: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0x97eed1f6, original_name='Hungry', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    face_lunge: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0x7b6c604a, original_name='FaceLunge', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    ball_lunge: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0x292754af, original_name='BallLunge', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    ball_lift: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0x18b5143a, original_name='BallLift', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    initial_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xedd0d40d, original_name='InitialVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    hungry_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x8d7e81d6, original_name='HungryVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    ball_lift_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xf68eadc9, original_name='BallLiftVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    phase_out_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xdc020da7, original_name='PhaseOutVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    phase_out_radius_missile: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa438a3cd, original_name='PhaseOutRadiusMissile'
        ),
    })
    metroid_phazeoid_struct_0x7c187bd0: MetroidPhazeoidStruct = dataclasses.field(default_factory=MetroidPhazeoidStruct, metadata={
        'reflection': FieldReflection[MetroidPhazeoidStruct](
            MetroidPhazeoidStruct, id=0x7c187bd0, original_name='MetroidPhazeoidStruct', from_json=MetroidPhazeoidStruct.from_json, to_json=MetroidPhazeoidStruct.to_json
        ),
    })
    metroid_phazeoid_struct_0x0c7b243d: MetroidPhazeoidStruct = dataclasses.field(default_factory=MetroidPhazeoidStruct, metadata={
        'reflection': FieldReflection[MetroidPhazeoidStruct](
            MetroidPhazeoidStruct, id=0x0c7b243d, original_name='MetroidPhazeoidStruct', from_json=MetroidPhazeoidStruct.from_json, to_json=MetroidPhazeoidStruct.to_json
        ),
    })
    metroid_phazeoid_struct_0x33b1809f: MetroidPhazeoidStruct = dataclasses.field(default_factory=MetroidPhazeoidStruct, metadata={
        'reflection': FieldReflection[MetroidPhazeoidStruct](
            MetroidPhazeoidStruct, id=0x33b1809f, original_name='MetroidPhazeoidStruct', from_json=MetroidPhazeoidStruct.from_json, to_json=MetroidPhazeoidStruct.to_json
        ),
    })
    metroid_phazeoid_struct_0x0ec6856a: MetroidPhazeoidStruct = dataclasses.field(default_factory=MetroidPhazeoidStruct, metadata={
        'reflection': FieldReflection[MetroidPhazeoidStruct](
            MetroidPhazeoidStruct, id=0x0ec6856a, original_name='MetroidPhazeoidStruct', from_json=MetroidPhazeoidStruct.from_json, to_json=MetroidPhazeoidStruct.to_json
        ),
    })
    metroid_phazeoid_struct_0x61fab47a: MetroidPhazeoidStruct = dataclasses.field(default_factory=MetroidPhazeoidStruct, metadata={
        'reflection': FieldReflection[MetroidPhazeoidStruct](
            MetroidPhazeoidStruct, id=0x61fab47a, original_name='MetroidPhazeoidStruct', from_json=MetroidPhazeoidStruct.from_json, to_json=MetroidPhazeoidStruct.to_json
        ),
    })
    metroid_phazeoid_struct_0x26aac761: MetroidPhazeoidStruct = dataclasses.field(default_factory=MetroidPhazeoidStruct, metadata={
        'reflection': FieldReflection[MetroidPhazeoidStruct](
            MetroidPhazeoidStruct, id=0x26aac761, original_name='MetroidPhazeoidStruct', from_json=MetroidPhazeoidStruct.from_json, to_json=MetroidPhazeoidStruct.to_json
        ),
    })
    brain_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x243ab10d, original_name='BrainVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    x_ray_brain_radius: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2dc4ac9c, original_name='XRayBrainRadius'
        ),
    })
    normal_brain_radius: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7cb760a5, original_name='NormalBrainRadius'
        ),
    })
    phase_out_time_min: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x06a2bbb8, original_name='PhaseOutTimeMin'
        ),
    })
    phase_out_time_max: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe0c21459, original_name='PhaseOutTimeMax'
        ),
    })
    phase_in_time_min: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x544fa232, original_name='PhaseInTimeMin'
        ),
    })
    phase_in_time_max: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb22f0dd3, original_name='PhaseInTimeMax'
        ),
    })
    target_phase_opacity_min: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0xacdacc80, original_name='TargetPhaseOpacityMin'
        ),
    })
    target_phase_opacity_max: float = dataclasses.field(default=0.6000000238418579, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4aba6361, original_name='TargetPhaseOpacityMax'
        ),
    })
    unknown_0xa77f2fe5: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa77f2fe5, original_name='Unknown'
        ),
    })
    unknown_0x411f8004: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x411f8004, original_name='Unknown'
        ),
    })
    hungry_phase_out_chance_max: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd14fc373, original_name='HungryPhaseOutChanceMax'
        ),
    })
    hungry_phase_out_chance_min: float = dataclasses.field(default=-50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x372f6c92, original_name='HungryPhaseOutChanceMin'
        ),
    })
    hungry_phase_out_chance_reduction: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf67d89b1, original_name='HungryPhaseOutChanceReduction'
        ),
    })
    hungry_phase_out_chance_regen: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x900a62f6, original_name='HungryPhaseOutChanceRegen'
        ),
    })
    arc_range_min: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa1b7cf27, original_name='ArcRangeMin'
        ),
    })
    arc_range_max: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x47d760c6, original_name='ArcRangeMax'
        ),
    })
    arc_range_ball_lift_min: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9aab0b9a, original_name='ArcRangeBallLiftMin'
        ),
    })
    arc_range_ball_lift_max: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7ccba47b, original_name='ArcRangeBallLiftMax'
        ),
    })
    arc_attack: ElectricBeamInfo = dataclasses.field(default_factory=ElectricBeamInfo, metadata={
        'reflection': FieldReflection[ElectricBeamInfo](
            ElectricBeamInfo, id=0x6d417f4c, original_name='ArcAttack', from_json=ElectricBeamInfo.from_json, to_json=ElectricBeamInfo.to_json
        ),
    })
    lunge_range_min: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0a8b169f, original_name='LungeRangeMin'
        ),
    })
    lunge_range_max: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xecebb97e, original_name='LungeRangeMax'
        ),
    })
    hug_radius_multiplier: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2b53dc0d, original_name='HugRadiusMultiplier'
        ),
    })
    energy_drain: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x79ccc5b8, original_name='EnergyDrain', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    max_energy_drain_allowed: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3af75fcc, original_name='MaxEnergyDrainAllowed'
        ),
    })
    max_static_intensity: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe7b4922a, original_name='MaxStaticIntensity'
        ),
    })
    ball_lift_delay_min: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4f4842a3, original_name='BallLiftDelayMin'
        ),
    })
    ball_lift_delay_max: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa928ed42, original_name='BallLiftDelayMax'
        ),
    })
    ball_lift_zap_delay_min: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x283f2238, original_name='BallLiftZapDelayMin'
        ),
    })
    ball_lift_zap_delay_max: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xce5f8dd9, original_name='BallLiftZapDelayMax'
        ),
    })
    hug_attack_delay_min: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x638d46ce, original_name='HugAttackDelayMin'
        ),
    })
    hug_attack_delay_max: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x85ede92f, original_name='HugAttackDelayMax'
        ),
    })
    hungry_damage_threshold: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x62fb47a5, original_name='HungryDamageThreshold'
        ),
    })
    unknown_0x677e48ea: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x677e48ea, original_name='Unknown'
        ),
    })
    unknown_0x7edf931d: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x7edf931d, original_name='Unknown'
        ),
    })
    unknown_0x15283674: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x15283674, original_name='Unknown'
        ),
    })
    unknown_0x1ae10f78: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1ae10f78, original_name='Unknown'
        ),
    })
    unknown_0x93f9240c: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x93f9240c, original_name='Unknown'
        ),
    })
    max_dist_off_mesh: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x50b079ed, original_name='MaxDistOffMesh'
        ),
    })
    phase_out_dist_off_mesh: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb15b41fa, original_name='PhaseOutDistOffMesh'
        ),
    })
    arc_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['ELSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5562c40d, original_name='ArcEffect'
        ),
    })
    arc_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x11f74e71, original_name='ArcExplosion'
        ),
    })
    sound_arc_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3509cdd9, original_name='Sound_ArcExplosion'
        ),
    })
    arc_number: int = dataclasses.field(default=5, metadata={
        'reflection': FieldReflection[int](
            int, id=0x953bc1d2, original_name='ArcNumber'
        ),
    })
    arc_length: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x21828087, original_name='ArcLength'
        ),
    })
    arc_move_time_max: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x328b3e6e, original_name='ArcMoveTimeMax'
        ),
    })
    arc_move_time_min: float = dataclasses.field(default=0.020999999716877937, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd4eb918f, original_name='ArcMoveTimeMin'
        ),
    })
    arc_on_time_max: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x55ebb850, original_name='ArcOnTimeMax'
        ),
    })
    arc_on_time_min: float = dataclasses.field(default=0.020999999716877937, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb38b17b1, original_name='ArcOnTimeMin'
        ),
    })
    path_find_height: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6dc77716, original_name='PathFindHeight'
        ),
    })
    unknown_0x6fc4508c: float = dataclasses.field(default=-3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6fc4508c, original_name='Unknown'
        ),
    })
    unknown_0x7de8da8d: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7de8da8d, original_name='Unknown'
        ),
    })
    unknown_0xf67dbaab: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf67dbaab, original_name='Unknown'
        ),
    })
    blur_radius: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6f6eb1f4, original_name='BlurRadius'
        ),
    })
    blur_duration: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6409edb3, original_name='BlurDuration'
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
        if property_count != 81:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x74288ef3
        disable_player_grab = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0679e20c
        disable_pirate_grab = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xae46d80e
        disable_hungry_mode = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbd62d02e
        post_hatch_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xef6d8c96
        post_hatch_scale_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x763e71ae
        post_hatch_rotation_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9aa90b6b
        recheck_path_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7626ec89
        recheck_path_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7fc827a2
        scan_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xccdd3aca
        patrol = FlyerMovementMode.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfa2a173f
        attack = FlyerMovementMode.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x97eed1f6
        hungry = FlyerMovementMode.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7b6c604a
        face_lunge = FlyerMovementMode.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x292754af
        ball_lunge = FlyerMovementMode.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x18b5143a
        ball_lift = FlyerMovementMode.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xedd0d40d
        initial_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8d7e81d6
        hungry_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf68eadc9
        ball_lift_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdc020da7
        phase_out_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa438a3cd
        phase_out_radius_missile = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7c187bd0
        metroid_phazeoid_struct_0x7c187bd0 = MetroidPhazeoidStruct.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0c7b243d
        metroid_phazeoid_struct_0x0c7b243d = MetroidPhazeoidStruct.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33b1809f
        metroid_phazeoid_struct_0x33b1809f = MetroidPhazeoidStruct.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0ec6856a
        metroid_phazeoid_struct_0x0ec6856a = MetroidPhazeoidStruct.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x61fab47a
        metroid_phazeoid_struct_0x61fab47a = MetroidPhazeoidStruct.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x26aac761
        metroid_phazeoid_struct_0x26aac761 = MetroidPhazeoidStruct.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x243ab10d
        brain_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2dc4ac9c
        x_ray_brain_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7cb760a5
        normal_brain_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x06a2bbb8
        phase_out_time_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe0c21459
        phase_out_time_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x544fa232
        phase_in_time_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb22f0dd3
        phase_in_time_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xacdacc80
        target_phase_opacity_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4aba6361
        target_phase_opacity_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa77f2fe5
        unknown_0xa77f2fe5 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x411f8004
        unknown_0x411f8004 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd14fc373
        hungry_phase_out_chance_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x372f6c92
        hungry_phase_out_chance_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf67d89b1
        hungry_phase_out_chance_reduction = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x900a62f6
        hungry_phase_out_chance_regen = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa1b7cf27
        arc_range_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47d760c6
        arc_range_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9aab0b9a
        arc_range_ball_lift_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7ccba47b
        arc_range_ball_lift_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6d417f4c
        arc_attack = ElectricBeamInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0a8b169f
        lunge_range_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xecebb97e
        lunge_range_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2b53dc0d
        hug_radius_multiplier = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x79ccc5b8
        energy_drain = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3af75fcc
        max_energy_drain_allowed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe7b4922a
        max_static_intensity = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4f4842a3
        ball_lift_delay_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa928ed42
        ball_lift_delay_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x283f2238
        ball_lift_zap_delay_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xce5f8dd9
        ball_lift_zap_delay_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x638d46ce
        hug_attack_delay_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x85ede92f
        hug_attack_delay_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x62fb47a5
        hungry_damage_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x677e48ea
        unknown_0x677e48ea = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7edf931d
        unknown_0x7edf931d = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x15283674
        unknown_0x15283674 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1ae10f78
        unknown_0x1ae10f78 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x93f9240c
        unknown_0x93f9240c = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50b079ed
        max_dist_off_mesh = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb15b41fa
        phase_out_dist_off_mesh = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5562c40d
        arc_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x11f74e71
        arc_explosion = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3509cdd9
        sound_arc_explosion = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x953bc1d2
        arc_number = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21828087
        arc_length = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x328b3e6e
        arc_move_time_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd4eb918f
        arc_move_time_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x55ebb850
        arc_on_time_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb38b17b1
        arc_on_time_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6dc77716
        path_find_height = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6fc4508c
        unknown_0x6fc4508c = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7de8da8d
        unknown_0x7de8da8d = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf67dbaab
        unknown_0xf67dbaab = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6f6eb1f4
        blur_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6409edb3
        blur_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(disable_player_grab, disable_pirate_grab, disable_hungry_mode, post_hatch_scale, post_hatch_scale_speed, post_hatch_rotation_speed, recheck_path_time, recheck_path_distance, scan_delay, patrol, attack, hungry, face_lunge, ball_lunge, ball_lift, initial_vulnerability, hungry_vulnerability, ball_lift_vulnerability, phase_out_vulnerability, phase_out_radius_missile, metroid_phazeoid_struct_0x7c187bd0, metroid_phazeoid_struct_0x0c7b243d, metroid_phazeoid_struct_0x33b1809f, metroid_phazeoid_struct_0x0ec6856a, metroid_phazeoid_struct_0x61fab47a, metroid_phazeoid_struct_0x26aac761, brain_vulnerability, x_ray_brain_radius, normal_brain_radius, phase_out_time_min, phase_out_time_max, phase_in_time_min, phase_in_time_max, target_phase_opacity_min, target_phase_opacity_max, unknown_0xa77f2fe5, unknown_0x411f8004, hungry_phase_out_chance_max, hungry_phase_out_chance_min, hungry_phase_out_chance_reduction, hungry_phase_out_chance_regen, arc_range_min, arc_range_max, arc_range_ball_lift_min, arc_range_ball_lift_max, arc_attack, lunge_range_min, lunge_range_max, hug_radius_multiplier, energy_drain, max_energy_drain_allowed, max_static_intensity, ball_lift_delay_min, ball_lift_delay_max, ball_lift_zap_delay_min, ball_lift_zap_delay_max, hug_attack_delay_min, hug_attack_delay_max, hungry_damage_threshold, unknown_0x677e48ea, unknown_0x7edf931d, unknown_0x15283674, unknown_0x1ae10f78, unknown_0x93f9240c, max_dist_off_mesh, phase_out_dist_off_mesh, arc_effect, arc_explosion, sound_arc_explosion, arc_number, arc_length, arc_move_time_max, arc_move_time_min, arc_on_time_max, arc_on_time_min, path_find_height, unknown_0x6fc4508c, unknown_0x7de8da8d, unknown_0xf67dbaab, blur_radius, blur_duration)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00Q')  # 81 properties

        data.write(b't(\x8e\xf3')  # 0x74288ef3
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.disable_player_grab))

        data.write(b'\x06y\xe2\x0c')  # 0x679e20c
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.disable_pirate_grab))

        data.write(b'\xaeF\xd8\x0e')  # 0xae46d80e
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.disable_hungry_mode))

        data.write(b'\xbdb\xd0.')  # 0xbd62d02e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.post_hatch_scale))

        data.write(b'\xefm\x8c\x96')  # 0xef6d8c96
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.post_hatch_scale_speed))

        data.write(b'v>q\xae')  # 0x763e71ae
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.post_hatch_rotation_speed))

        data.write(b'\x9a\xa9\x0bk')  # 0x9aa90b6b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.recheck_path_time))

        data.write(b'v&\xec\x89')  # 0x7626ec89
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.recheck_path_distance))

        data.write(b"\x7f\xc8'\xa2")  # 0x7fc827a2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_delay))

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

        data.write(b'\x97\xee\xd1\xf6')  # 0x97eed1f6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hungry.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'{l`J')  # 0x7b6c604a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.face_lunge.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b")'T\xaf")  # 0x292754af
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ball_lunge.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x18\xb5\x14:')  # 0x18b5143a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ball_lift.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xed\xd0\xd4\r')  # 0xedd0d40d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.initial_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8d~\x81\xd6')  # 0x8d7e81d6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hungry_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf6\x8e\xad\xc9')  # 0xf68eadc9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ball_lift_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xdc\x02\r\xa7')  # 0xdc020da7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.phase_out_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa48\xa3\xcd')  # 0xa438a3cd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phase_out_radius_missile))

        data.write(b'|\x18{\xd0')  # 0x7c187bd0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.metroid_phazeoid_struct_0x7c187bd0.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x0c{$=')  # 0xc7b243d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.metroid_phazeoid_struct_0x0c7b243d.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'3\xb1\x80\x9f')  # 0x33b1809f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.metroid_phazeoid_struct_0x33b1809f.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x0e\xc6\x85j')  # 0xec6856a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.metroid_phazeoid_struct_0x0ec6856a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'a\xfa\xb4z')  # 0x61fab47a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.metroid_phazeoid_struct_0x61fab47a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'&\xaa\xc7a')  # 0x26aac761
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.metroid_phazeoid_struct_0x26aac761.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'$:\xb1\r')  # 0x243ab10d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.brain_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'-\xc4\xac\x9c')  # 0x2dc4ac9c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.x_ray_brain_radius))

        data.write(b'|\xb7`\xa5')  # 0x7cb760a5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.normal_brain_radius))

        data.write(b'\x06\xa2\xbb\xb8')  # 0x6a2bbb8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phase_out_time_min))

        data.write(b'\xe0\xc2\x14Y')  # 0xe0c21459
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phase_out_time_max))

        data.write(b'TO\xa22')  # 0x544fa232
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phase_in_time_min))

        data.write(b'\xb2/\r\xd3')  # 0xb22f0dd3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phase_in_time_max))

        data.write(b'\xac\xda\xcc\x80')  # 0xacdacc80
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.target_phase_opacity_min))

        data.write(b'J\xbaca')  # 0x4aba6361
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.target_phase_opacity_max))

        data.write(b'\xa7\x7f/\xe5')  # 0xa77f2fe5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa77f2fe5))

        data.write(b'A\x1f\x80\x04')  # 0x411f8004
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x411f8004))

        data.write(b'\xd1O\xc3s')  # 0xd14fc373
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hungry_phase_out_chance_max))

        data.write(b'7/l\x92')  # 0x372f6c92
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hungry_phase_out_chance_min))

        data.write(b'\xf6}\x89\xb1')  # 0xf67d89b1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hungry_phase_out_chance_reduction))

        data.write(b'\x90\nb\xf6')  # 0x900a62f6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hungry_phase_out_chance_regen))

        data.write(b"\xa1\xb7\xcf'")  # 0xa1b7cf27
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.arc_range_min))

        data.write(b'G\xd7`\xc6')  # 0x47d760c6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.arc_range_max))

        data.write(b'\x9a\xab\x0b\x9a')  # 0x9aab0b9a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.arc_range_ball_lift_min))

        data.write(b'|\xcb\xa4{')  # 0x7ccba47b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.arc_range_ball_lift_max))

        data.write(b'mA\x7fL')  # 0x6d417f4c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.arc_attack.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\n\x8b\x16\x9f')  # 0xa8b169f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.lunge_range_min))

        data.write(b'\xec\xeb\xb9~')  # 0xecebb97e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.lunge_range_max))

        data.write(b'+S\xdc\r')  # 0x2b53dc0d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hug_radius_multiplier))

        data.write(b'y\xcc\xc5\xb8')  # 0x79ccc5b8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.energy_drain.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b':\xf7_\xcc')  # 0x3af75fcc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_energy_drain_allowed))

        data.write(b'\xe7\xb4\x92*')  # 0xe7b4922a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_static_intensity))

        data.write(b'OHB\xa3')  # 0x4f4842a3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ball_lift_delay_min))

        data.write(b'\xa9(\xedB')  # 0xa928ed42
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ball_lift_delay_max))

        data.write(b'(?"8')  # 0x283f2238
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ball_lift_zap_delay_min))

        data.write(b'\xce_\x8d\xd9')  # 0xce5f8dd9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ball_lift_zap_delay_max))

        data.write(b'c\x8dF\xce')  # 0x638d46ce
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hug_attack_delay_min))

        data.write(b'\x85\xed\xe9/')  # 0x85ede92f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hug_attack_delay_max))

        data.write(b'b\xfbG\xa5')  # 0x62fb47a5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hungry_damage_threshold))

        data.write(b'g~H\xea')  # 0x677e48ea
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x677e48ea))

        data.write(b'~\xdf\x93\x1d')  # 0x7edf931d
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x7edf931d))

        data.write(b'\x15(6t')  # 0x15283674
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x15283674))

        data.write(b'\x1a\xe1\x0fx')  # 0x1ae10f78
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1ae10f78))

        data.write(b'\x93\xf9$\x0c')  # 0x93f9240c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x93f9240c))

        data.write(b'P\xb0y\xed')  # 0x50b079ed
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_dist_off_mesh))

        data.write(b'\xb1[A\xfa')  # 0xb15b41fa
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phase_out_dist_off_mesh))

        data.write(b'Ub\xc4\r')  # 0x5562c40d
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.arc_effect))

        data.write(b'\x11\xf7Nq')  # 0x11f74e71
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.arc_explosion))

        data.write(b'5\t\xcd\xd9')  # 0x3509cdd9
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_arc_explosion))

        data.write(b'\x95;\xc1\xd2')  # 0x953bc1d2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.arc_number))

        data.write(b'!\x82\x80\x87')  # 0x21828087
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.arc_length))

        data.write(b'2\x8b>n')  # 0x328b3e6e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.arc_move_time_max))

        data.write(b'\xd4\xeb\x91\x8f')  # 0xd4eb918f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.arc_move_time_min))

        data.write(b'U\xeb\xb8P')  # 0x55ebb850
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.arc_on_time_max))

        data.write(b'\xb3\x8b\x17\xb1')  # 0xb38b17b1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.arc_on_time_min))

        data.write(b'm\xc7w\x16')  # 0x6dc77716
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.path_find_height))

        data.write(b'o\xc4P\x8c')  # 0x6fc4508c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6fc4508c))

        data.write(b'}\xe8\xda\x8d')  # 0x7de8da8d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7de8da8d))

        data.write(b'\xf6}\xba\xab')  # 0xf67dbaab
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf67dbaab))

        data.write(b'on\xb1\xf4')  # 0x6f6eb1f4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.blur_radius))

        data.write(b'd\t\xed\xb3')  # 0x6409edb3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.blur_duration))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MetroidPhazeoidDataJson", data)
        return cls(
            disable_player_grab=json_data['disable_player_grab'],
            disable_pirate_grab=json_data['disable_pirate_grab'],
            disable_hungry_mode=json_data['disable_hungry_mode'],
            post_hatch_scale=json_data['post_hatch_scale'],
            post_hatch_scale_speed=json_data['post_hatch_scale_speed'],
            post_hatch_rotation_speed=json_data['post_hatch_rotation_speed'],
            recheck_path_time=json_data['recheck_path_time'],
            recheck_path_distance=json_data['recheck_path_distance'],
            scan_delay=json_data['scan_delay'],
            patrol=FlyerMovementMode.from_json(json_data['patrol']),
            attack=FlyerMovementMode.from_json(json_data['attack']),
            hungry=FlyerMovementMode.from_json(json_data['hungry']),
            face_lunge=FlyerMovementMode.from_json(json_data['face_lunge']),
            ball_lunge=FlyerMovementMode.from_json(json_data['ball_lunge']),
            ball_lift=FlyerMovementMode.from_json(json_data['ball_lift']),
            initial_vulnerability=DamageVulnerability.from_json(json_data['initial_vulnerability']),
            hungry_vulnerability=DamageVulnerability.from_json(json_data['hungry_vulnerability']),
            ball_lift_vulnerability=DamageVulnerability.from_json(json_data['ball_lift_vulnerability']),
            phase_out_vulnerability=DamageVulnerability.from_json(json_data['phase_out_vulnerability']),
            phase_out_radius_missile=json_data['phase_out_radius_missile'],
            metroid_phazeoid_struct_0x7c187bd0=MetroidPhazeoidStruct.from_json(json_data['metroid_phazeoid_struct_0x7c187bd0']),
            metroid_phazeoid_struct_0x0c7b243d=MetroidPhazeoidStruct.from_json(json_data['metroid_phazeoid_struct_0x0c7b243d']),
            metroid_phazeoid_struct_0x33b1809f=MetroidPhazeoidStruct.from_json(json_data['metroid_phazeoid_struct_0x33b1809f']),
            metroid_phazeoid_struct_0x0ec6856a=MetroidPhazeoidStruct.from_json(json_data['metroid_phazeoid_struct_0x0ec6856a']),
            metroid_phazeoid_struct_0x61fab47a=MetroidPhazeoidStruct.from_json(json_data['metroid_phazeoid_struct_0x61fab47a']),
            metroid_phazeoid_struct_0x26aac761=MetroidPhazeoidStruct.from_json(json_data['metroid_phazeoid_struct_0x26aac761']),
            brain_vulnerability=DamageVulnerability.from_json(json_data['brain_vulnerability']),
            x_ray_brain_radius=json_data['x_ray_brain_radius'],
            normal_brain_radius=json_data['normal_brain_radius'],
            phase_out_time_min=json_data['phase_out_time_min'],
            phase_out_time_max=json_data['phase_out_time_max'],
            phase_in_time_min=json_data['phase_in_time_min'],
            phase_in_time_max=json_data['phase_in_time_max'],
            target_phase_opacity_min=json_data['target_phase_opacity_min'],
            target_phase_opacity_max=json_data['target_phase_opacity_max'],
            unknown_0xa77f2fe5=json_data['unknown_0xa77f2fe5'],
            unknown_0x411f8004=json_data['unknown_0x411f8004'],
            hungry_phase_out_chance_max=json_data['hungry_phase_out_chance_max'],
            hungry_phase_out_chance_min=json_data['hungry_phase_out_chance_min'],
            hungry_phase_out_chance_reduction=json_data['hungry_phase_out_chance_reduction'],
            hungry_phase_out_chance_regen=json_data['hungry_phase_out_chance_regen'],
            arc_range_min=json_data['arc_range_min'],
            arc_range_max=json_data['arc_range_max'],
            arc_range_ball_lift_min=json_data['arc_range_ball_lift_min'],
            arc_range_ball_lift_max=json_data['arc_range_ball_lift_max'],
            arc_attack=ElectricBeamInfo.from_json(json_data['arc_attack']),
            lunge_range_min=json_data['lunge_range_min'],
            lunge_range_max=json_data['lunge_range_max'],
            hug_radius_multiplier=json_data['hug_radius_multiplier'],
            energy_drain=Spline.from_json(json_data['energy_drain']),
            max_energy_drain_allowed=json_data['max_energy_drain_allowed'],
            max_static_intensity=json_data['max_static_intensity'],
            ball_lift_delay_min=json_data['ball_lift_delay_min'],
            ball_lift_delay_max=json_data['ball_lift_delay_max'],
            ball_lift_zap_delay_min=json_data['ball_lift_zap_delay_min'],
            ball_lift_zap_delay_max=json_data['ball_lift_zap_delay_max'],
            hug_attack_delay_min=json_data['hug_attack_delay_min'],
            hug_attack_delay_max=json_data['hug_attack_delay_max'],
            hungry_damage_threshold=json_data['hungry_damage_threshold'],
            unknown_0x677e48ea=json_data['unknown_0x677e48ea'],
            unknown_0x7edf931d=json_data['unknown_0x7edf931d'],
            unknown_0x15283674=json_data['unknown_0x15283674'],
            unknown_0x1ae10f78=json_data['unknown_0x1ae10f78'],
            unknown_0x93f9240c=json_data['unknown_0x93f9240c'],
            max_dist_off_mesh=json_data['max_dist_off_mesh'],
            phase_out_dist_off_mesh=json_data['phase_out_dist_off_mesh'],
            arc_effect=json_data['arc_effect'],
            arc_explosion=json_data['arc_explosion'],
            sound_arc_explosion=json_data['sound_arc_explosion'],
            arc_number=json_data['arc_number'],
            arc_length=json_data['arc_length'],
            arc_move_time_max=json_data['arc_move_time_max'],
            arc_move_time_min=json_data['arc_move_time_min'],
            arc_on_time_max=json_data['arc_on_time_max'],
            arc_on_time_min=json_data['arc_on_time_min'],
            path_find_height=json_data['path_find_height'],
            unknown_0x6fc4508c=json_data['unknown_0x6fc4508c'],
            unknown_0x7de8da8d=json_data['unknown_0x7de8da8d'],
            unknown_0xf67dbaab=json_data['unknown_0xf67dbaab'],
            blur_radius=json_data['blur_radius'],
            blur_duration=json_data['blur_duration'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'disable_player_grab': self.disable_player_grab,
            'disable_pirate_grab': self.disable_pirate_grab,
            'disable_hungry_mode': self.disable_hungry_mode,
            'post_hatch_scale': self.post_hatch_scale,
            'post_hatch_scale_speed': self.post_hatch_scale_speed,
            'post_hatch_rotation_speed': self.post_hatch_rotation_speed,
            'recheck_path_time': self.recheck_path_time,
            'recheck_path_distance': self.recheck_path_distance,
            'scan_delay': self.scan_delay,
            'patrol': self.patrol.to_json(),
            'attack': self.attack.to_json(),
            'hungry': self.hungry.to_json(),
            'face_lunge': self.face_lunge.to_json(),
            'ball_lunge': self.ball_lunge.to_json(),
            'ball_lift': self.ball_lift.to_json(),
            'initial_vulnerability': self.initial_vulnerability.to_json(),
            'hungry_vulnerability': self.hungry_vulnerability.to_json(),
            'ball_lift_vulnerability': self.ball_lift_vulnerability.to_json(),
            'phase_out_vulnerability': self.phase_out_vulnerability.to_json(),
            'phase_out_radius_missile': self.phase_out_radius_missile,
            'metroid_phazeoid_struct_0x7c187bd0': self.metroid_phazeoid_struct_0x7c187bd0.to_json(),
            'metroid_phazeoid_struct_0x0c7b243d': self.metroid_phazeoid_struct_0x0c7b243d.to_json(),
            'metroid_phazeoid_struct_0x33b1809f': self.metroid_phazeoid_struct_0x33b1809f.to_json(),
            'metroid_phazeoid_struct_0x0ec6856a': self.metroid_phazeoid_struct_0x0ec6856a.to_json(),
            'metroid_phazeoid_struct_0x61fab47a': self.metroid_phazeoid_struct_0x61fab47a.to_json(),
            'metroid_phazeoid_struct_0x26aac761': self.metroid_phazeoid_struct_0x26aac761.to_json(),
            'brain_vulnerability': self.brain_vulnerability.to_json(),
            'x_ray_brain_radius': self.x_ray_brain_radius,
            'normal_brain_radius': self.normal_brain_radius,
            'phase_out_time_min': self.phase_out_time_min,
            'phase_out_time_max': self.phase_out_time_max,
            'phase_in_time_min': self.phase_in_time_min,
            'phase_in_time_max': self.phase_in_time_max,
            'target_phase_opacity_min': self.target_phase_opacity_min,
            'target_phase_opacity_max': self.target_phase_opacity_max,
            'unknown_0xa77f2fe5': self.unknown_0xa77f2fe5,
            'unknown_0x411f8004': self.unknown_0x411f8004,
            'hungry_phase_out_chance_max': self.hungry_phase_out_chance_max,
            'hungry_phase_out_chance_min': self.hungry_phase_out_chance_min,
            'hungry_phase_out_chance_reduction': self.hungry_phase_out_chance_reduction,
            'hungry_phase_out_chance_regen': self.hungry_phase_out_chance_regen,
            'arc_range_min': self.arc_range_min,
            'arc_range_max': self.arc_range_max,
            'arc_range_ball_lift_min': self.arc_range_ball_lift_min,
            'arc_range_ball_lift_max': self.arc_range_ball_lift_max,
            'arc_attack': self.arc_attack.to_json(),
            'lunge_range_min': self.lunge_range_min,
            'lunge_range_max': self.lunge_range_max,
            'hug_radius_multiplier': self.hug_radius_multiplier,
            'energy_drain': self.energy_drain.to_json(),
            'max_energy_drain_allowed': self.max_energy_drain_allowed,
            'max_static_intensity': self.max_static_intensity,
            'ball_lift_delay_min': self.ball_lift_delay_min,
            'ball_lift_delay_max': self.ball_lift_delay_max,
            'ball_lift_zap_delay_min': self.ball_lift_zap_delay_min,
            'ball_lift_zap_delay_max': self.ball_lift_zap_delay_max,
            'hug_attack_delay_min': self.hug_attack_delay_min,
            'hug_attack_delay_max': self.hug_attack_delay_max,
            'hungry_damage_threshold': self.hungry_damage_threshold,
            'unknown_0x677e48ea': self.unknown_0x677e48ea,
            'unknown_0x7edf931d': self.unknown_0x7edf931d,
            'unknown_0x15283674': self.unknown_0x15283674,
            'unknown_0x1ae10f78': self.unknown_0x1ae10f78,
            'unknown_0x93f9240c': self.unknown_0x93f9240c,
            'max_dist_off_mesh': self.max_dist_off_mesh,
            'phase_out_dist_off_mesh': self.phase_out_dist_off_mesh,
            'arc_effect': self.arc_effect,
            'arc_explosion': self.arc_explosion,
            'sound_arc_explosion': self.sound_arc_explosion,
            'arc_number': self.arc_number,
            'arc_length': self.arc_length,
            'arc_move_time_max': self.arc_move_time_max,
            'arc_move_time_min': self.arc_move_time_min,
            'arc_on_time_max': self.arc_on_time_max,
            'arc_on_time_min': self.arc_on_time_min,
            'path_find_height': self.path_find_height,
            'unknown_0x6fc4508c': self.unknown_0x6fc4508c,
            'unknown_0x7de8da8d': self.unknown_0x7de8da8d,
            'unknown_0xf67dbaab': self.unknown_0xf67dbaab,
            'blur_radius': self.blur_radius,
            'blur_duration': self.blur_duration,
        }

    def _dependencies_for_arc_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.arc_effect)

    def _dependencies_for_arc_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.arc_explosion)

    def _dependencies_for_sound_arc_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_arc_explosion)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.arc_attack.dependencies_for, "arc_attack", "ElectricBeamInfo"),
            (self._dependencies_for_arc_effect, "arc_effect", "AssetId"),
            (self._dependencies_for_arc_explosion, "arc_explosion", "AssetId"),
            (self._dependencies_for_sound_arc_explosion, "sound_arc_explosion", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for MetroidPhazeoidData.{field_name} ({field_type}): {e}"
                )


def _decode_patrol(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_attack(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_hungry(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_face_lunge(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_ball_lunge(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_ball_lift(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size)


def _decode_initial_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_hungry_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_ball_lift_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_phase_out_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_metroid_phazeoid_struct_0x7c187bd0(data: typing.BinaryIO, game: Game, property_size: int) -> MetroidPhazeoidStruct:
    return MetroidPhazeoidStruct.from_stream(data, game, property_size)


def _decode_metroid_phazeoid_struct_0x0c7b243d(data: typing.BinaryIO, game: Game, property_size: int) -> MetroidPhazeoidStruct:
    return MetroidPhazeoidStruct.from_stream(data, game, property_size)


def _decode_metroid_phazeoid_struct_0x33b1809f(data: typing.BinaryIO, game: Game, property_size: int) -> MetroidPhazeoidStruct:
    return MetroidPhazeoidStruct.from_stream(data, game, property_size)


def _decode_metroid_phazeoid_struct_0x0ec6856a(data: typing.BinaryIO, game: Game, property_size: int) -> MetroidPhazeoidStruct:
    return MetroidPhazeoidStruct.from_stream(data, game, property_size)


def _decode_metroid_phazeoid_struct_0x61fab47a(data: typing.BinaryIO, game: Game, property_size: int) -> MetroidPhazeoidStruct:
    return MetroidPhazeoidStruct.from_stream(data, game, property_size)


def _decode_metroid_phazeoid_struct_0x26aac761(data: typing.BinaryIO, game: Game, property_size: int) -> MetroidPhazeoidStruct:
    return MetroidPhazeoidStruct.from_stream(data, game, property_size)


def _decode_brain_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_arc_attack(data: typing.BinaryIO, game: Game, property_size: int) -> ElectricBeamInfo:
    return ElectricBeamInfo.from_stream(data, game, property_size)


def _decode_energy_drain(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x74288ef3: ('disable_player_grab', structs.decode_BIG_bool_),
    0x0679e20c: ('disable_pirate_grab', structs.decode_BIG_bool_),
    0xae46d80e: ('disable_hungry_mode', structs.decode_BIG_bool_),
    0xbd62d02e: ('post_hatch_scale', structs.decode_BIG_f),
    0xef6d8c96: ('post_hatch_scale_speed', structs.decode_BIG_f),
    0x763e71ae: ('post_hatch_rotation_speed', structs.decode_BIG_f),
    0x9aa90b6b: ('recheck_path_time', structs.decode_BIG_f),
    0x7626ec89: ('recheck_path_distance', structs.decode_BIG_f),
    0x7fc827a2: ('scan_delay', structs.decode_BIG_f),
    0xccdd3aca: ('patrol', _decode_patrol),
    0xfa2a173f: ('attack', _decode_attack),
    0x97eed1f6: ('hungry', _decode_hungry),
    0x7b6c604a: ('face_lunge', _decode_face_lunge),
    0x292754af: ('ball_lunge', _decode_ball_lunge),
    0x18b5143a: ('ball_lift', _decode_ball_lift),
    0xedd0d40d: ('initial_vulnerability', _decode_initial_vulnerability),
    0x8d7e81d6: ('hungry_vulnerability', _decode_hungry_vulnerability),
    0xf68eadc9: ('ball_lift_vulnerability', _decode_ball_lift_vulnerability),
    0xdc020da7: ('phase_out_vulnerability', _decode_phase_out_vulnerability),
    0xa438a3cd: ('phase_out_radius_missile', structs.decode_BIG_f),
    0x7c187bd0: ('metroid_phazeoid_struct_0x7c187bd0', _decode_metroid_phazeoid_struct_0x7c187bd0),
    0x0c7b243d: ('metroid_phazeoid_struct_0x0c7b243d', _decode_metroid_phazeoid_struct_0x0c7b243d),
    0x33b1809f: ('metroid_phazeoid_struct_0x33b1809f', _decode_metroid_phazeoid_struct_0x33b1809f),
    0x0ec6856a: ('metroid_phazeoid_struct_0x0ec6856a', _decode_metroid_phazeoid_struct_0x0ec6856a),
    0x61fab47a: ('metroid_phazeoid_struct_0x61fab47a', _decode_metroid_phazeoid_struct_0x61fab47a),
    0x26aac761: ('metroid_phazeoid_struct_0x26aac761', _decode_metroid_phazeoid_struct_0x26aac761),
    0x243ab10d: ('brain_vulnerability', _decode_brain_vulnerability),
    0x2dc4ac9c: ('x_ray_brain_radius', structs.decode_BIG_f),
    0x7cb760a5: ('normal_brain_radius', structs.decode_BIG_f),
    0x06a2bbb8: ('phase_out_time_min', structs.decode_BIG_f),
    0xe0c21459: ('phase_out_time_max', structs.decode_BIG_f),
    0x544fa232: ('phase_in_time_min', structs.decode_BIG_f),
    0xb22f0dd3: ('phase_in_time_max', structs.decode_BIG_f),
    0xacdacc80: ('target_phase_opacity_min', structs.decode_BIG_f),
    0x4aba6361: ('target_phase_opacity_max', structs.decode_BIG_f),
    0xa77f2fe5: ('unknown_0xa77f2fe5', structs.decode_BIG_f),
    0x411f8004: ('unknown_0x411f8004', structs.decode_BIG_f),
    0xd14fc373: ('hungry_phase_out_chance_max', structs.decode_BIG_f),
    0x372f6c92: ('hungry_phase_out_chance_min', structs.decode_BIG_f),
    0xf67d89b1: ('hungry_phase_out_chance_reduction', structs.decode_BIG_f),
    0x900a62f6: ('hungry_phase_out_chance_regen', structs.decode_BIG_f),
    0xa1b7cf27: ('arc_range_min', structs.decode_BIG_f),
    0x47d760c6: ('arc_range_max', structs.decode_BIG_f),
    0x9aab0b9a: ('arc_range_ball_lift_min', structs.decode_BIG_f),
    0x7ccba47b: ('arc_range_ball_lift_max', structs.decode_BIG_f),
    0x6d417f4c: ('arc_attack', _decode_arc_attack),
    0x0a8b169f: ('lunge_range_min', structs.decode_BIG_f),
    0xecebb97e: ('lunge_range_max', structs.decode_BIG_f),
    0x2b53dc0d: ('hug_radius_multiplier', structs.decode_BIG_f),
    0x79ccc5b8: ('energy_drain', _decode_energy_drain),
    0x3af75fcc: ('max_energy_drain_allowed', structs.decode_BIG_f),
    0xe7b4922a: ('max_static_intensity', structs.decode_BIG_f),
    0x4f4842a3: ('ball_lift_delay_min', structs.decode_BIG_f),
    0xa928ed42: ('ball_lift_delay_max', structs.decode_BIG_f),
    0x283f2238: ('ball_lift_zap_delay_min', structs.decode_BIG_f),
    0xce5f8dd9: ('ball_lift_zap_delay_max', structs.decode_BIG_f),
    0x638d46ce: ('hug_attack_delay_min', structs.decode_BIG_f),
    0x85ede92f: ('hug_attack_delay_max', structs.decode_BIG_f),
    0x62fb47a5: ('hungry_damage_threshold', structs.decode_BIG_f),
    0x677e48ea: ('unknown_0x677e48ea', structs.decode_BIG_bool_),
    0x7edf931d: ('unknown_0x7edf931d', structs.decode_BIG_bool_),
    0x15283674: ('unknown_0x15283674', structs.decode_BIG_bool_),
    0x1ae10f78: ('unknown_0x1ae10f78', structs.decode_BIG_f),
    0x93f9240c: ('unknown_0x93f9240c', structs.decode_BIG_f),
    0x50b079ed: ('max_dist_off_mesh', structs.decode_BIG_f),
    0xb15b41fa: ('phase_out_dist_off_mesh', structs.decode_BIG_f),
    0x5562c40d: ('arc_effect', structs.decode_BIG_Q),
    0x11f74e71: ('arc_explosion', structs.decode_BIG_Q),
    0x3509cdd9: ('sound_arc_explosion', structs.decode_BIG_Q),
    0x953bc1d2: ('arc_number', structs.decode_BIG_l),
    0x21828087: ('arc_length', structs.decode_BIG_f),
    0x328b3e6e: ('arc_move_time_max', structs.decode_BIG_f),
    0xd4eb918f: ('arc_move_time_min', structs.decode_BIG_f),
    0x55ebb850: ('arc_on_time_max', structs.decode_BIG_f),
    0xb38b17b1: ('arc_on_time_min', structs.decode_BIG_f),
    0x6dc77716: ('path_find_height', structs.decode_BIG_f),
    0x6fc4508c: ('unknown_0x6fc4508c', structs.decode_BIG_f),
    0x7de8da8d: ('unknown_0x7de8da8d', structs.decode_BIG_f),
    0xf67dbaab: ('unknown_0xf67dbaab', structs.decode_BIG_f),
    0x6f6eb1f4: ('blur_radius', structs.decode_BIG_f),
    0x6409edb3: ('blur_duration', structs.decode_BIG_f),
}
