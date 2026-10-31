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
from retro_data_structures.properties.corruption.archetypes.FlyerMovementMode import FlyerMovementMode
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class MetroidHatcherDataJson(typing_extensions.TypedDict):
        hearing_range: float
        lose_interest_range: float
        lose_interest_time: float
        morphball_throw_force: float
        womb_open_close_time: float
        womb_attack_angle: float
        womb_vulnerability: json_util.JsonObject
        body_vulnerability: json_util.JsonObject
        brain_vulnerability: json_util.JsonObject
        brain_x_ray_radius: float
        brain_radius: float
        leg_vulnerability: json_util.JsonObject
        leg_damage_threshold: float
        tentacle_suck_in_time: float
        tentacle_regrow_time: float
        tentacle_grapple_out_time: float
        unknown_0xc550a481: float
        min_time_between_attacks: float
        max_time_between_attacks: float
        stab_damage_time_first_person: float
        stab_damage_first_person: float
        stab_damage_time_morphball: float
        stab_damage_morphball: float
        max_attack_height: float
        min_attack_height: float
        max_attack_forward: float
        min_attack_forward: float
        unknown_0x0978b98a: float
        unknown_0xcfcd32bb: float
        unknown_0x17d71349: float
        recheck_path_time: float
        recheck_path_distance: float
        max_num_metroids: int
        auto_spawn: bool
        max_spawn_delay: float
        min_spawn_delay: float
        unknown_0x6089191d: int
        unknown_0x258b5a9f: int
        min_spawn_point_distance: float
        hatch_chance: float
        hatch_chance2: float
        hatch_chance3: float
        spin_attack_damage: json_util.JsonObject
        max_spin_attack_delay: float
        min_spin_attack_delay: float
        unknown_0xbeaf2105: float
        womb_open_time_max: float
        womb_open_time_min: float
        dodge_chance: float
        dash_at_player_dist_max: float
        dash_at_player_dist_min: float
        unknown_0x248d3599: float
        unknown_0xbfd77e62: float
        random_move_dist_max: float
        random_move_dist_min: float
        patrol: json_util.JsonObject
        attack_path: json_util.JsonObject
        combat: json_util.JsonObject
        stab_attack: json_util.JsonObject
        spin_attack_out: json_util.JsonObject
        spin_attack_back: json_util.JsonObject
        out_of_spin: json_util.JsonObject
        spin_and_spawn: json_util.JsonObject
        out_of_spin_and_spawn: json_util.JsonObject
        stunned: json_util.JsonObject
        grappled: json_util.JsonObject
        dash: json_util.JsonObject
        retreat_and_spawn: json_util.JsonObject
        claw: json_util.JsonObject
        retracted_claw_lf: json_util.JsonObject
        retracted_claw_rf: json_util.JsonObject
        retracted_claw_lb: json_util.JsonObject
        retracted_claw_rb: json_util.JsonObject
        claw_open_weight_max: float
        claw_open_weight_min: float
        claw_open_delta_max: float
        claw_open_delta_min: float
        claw_closed_weight_max: float
        claw_closed_weight_min: float
        claw_close_delta_max: float
        claw_close_delta_min: float
        stun_threshold: float
        electric_ball_effect: int
        sound_ball_effect: int
        electric_visor_effect: int
        sound_visor_effect: int
        leg_hit_splash: int
    

@dataclasses.dataclass()
class MetroidHatcherData(BaseProperty):
    hearing_range: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x25474550, original_name='HearingRange'
        ),
    })
    lose_interest_range: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x474fa589, original_name='LoseInterestRange'
        ),
    })
    lose_interest_time: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf8b0c2bb, original_name='LoseInterestTime'
        ),
    })
    morphball_throw_force: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfe4588a1, original_name='MorphballThrowForce'
        ),
    })
    womb_open_close_time: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc2688b41, original_name='WombOpenCloseTime'
        ),
    })
    womb_attack_angle: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7b0cc30d, original_name='WombAttackAngle'
        ),
    })
    womb_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x742b3336, original_name='WombVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    body_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x0d9230d1, original_name='BodyVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    brain_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x243ab10d, original_name='BrainVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    brain_x_ray_radius: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x012115a2, original_name='BrainXRayRadius'
        ),
    })
    brain_radius: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa12a4409, original_name='BrainRadius'
        ),
    })
    leg_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x9f0ff852, original_name='LegVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    leg_damage_threshold: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb9e0c90d, original_name='LegDamageThreshold'
        ),
    })
    tentacle_suck_in_time: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x81d39802, original_name='TentacleSuckInTime'
        ),
    })
    tentacle_regrow_time: float = dataclasses.field(default=0.33329999446868896, metadata={
        'reflection': FieldReflection[float](
            float, id=0xba002dcb, original_name='TentacleRegrowTime'
        ),
    })
    tentacle_grapple_out_time: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf79a10b0, original_name='TentacleGrappleOutTime'
        ),
    })
    unknown_0xc550a481: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc550a481, original_name='Unknown'
        ),
    })
    min_time_between_attacks: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x95e7a2c2, original_name='MinTimeBetweenAttacks'
        ),
    })
    max_time_between_attacks: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x76ba1c18, original_name='MaxTimeBetweenAttacks'
        ),
    })
    stab_damage_time_first_person: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe08106ed, original_name='StabDamageTimeFirstPerson'
        ),
    })
    stab_damage_first_person: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x88d7c540, original_name='StabDamageFirstPerson'
        ),
    })
    stab_damage_time_morphball: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xace62367, original_name='StabDamageTimeMorphball'
        ),
    })
    stab_damage_morphball: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x620b1b3d, original_name='StabDamageMorphball'
        ),
    })
    max_attack_height: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe1ae51d8, original_name='MaxAttackHeight'
        ),
    })
    min_attack_height: float = dataclasses.field(default=9.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc8d0acc0, original_name='MinAttackHeight'
        ),
    })
    max_attack_forward: float = dataclasses.field(default=16.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf3e8012d, original_name='MaxAttackForward'
        ),
    })
    min_attack_forward: float = dataclasses.field(default=14.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe0ade786, original_name='MinAttackForward'
        ),
    })
    unknown_0x0978b98a: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0978b98a, original_name='Unknown'
        ),
    })
    unknown_0xcfcd32bb: float = dataclasses.field(default=-1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcfcd32bb, original_name='Unknown'
        ),
    })
    unknown_0x17d71349: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x17d71349, original_name='Unknown'
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
    max_num_metroids: int = dataclasses.field(default=3, metadata={
        'reflection': FieldReflection[int](
            int, id=0x7915e2b3, original_name='MaxNumMetroids'
        ),
    })
    auto_spawn: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xccc0cf92, original_name='AutoSpawn'
        ),
    })
    max_spawn_delay: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x75e0b0a7, original_name='MaxSpawnDelay'
        ),
    })
    min_spawn_delay: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2646a843, original_name='MinSpawnDelay'
        ),
    })
    unknown_0x6089191d: int = dataclasses.field(default=10, metadata={
        'reflection': FieldReflection[int](
            int, id=0x6089191d, original_name='Unknown'
        ),
    })
    unknown_0x258b5a9f: int = dataclasses.field(default=5, metadata={
        'reflection': FieldReflection[int](
            int, id=0x258b5a9f, original_name='Unknown'
        ),
    })
    min_spawn_point_distance: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2ae610e5, original_name='MinSpawnPointDistance'
        ),
    })
    hatch_chance: float = dataclasses.field(default=0.699999988079071, metadata={
        'reflection': FieldReflection[float](
            float, id=0x354bae31, original_name='HatchChance'
        ),
    })
    hatch_chance2: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf4b2c801, original_name='HatchChance2'
        ),
    })
    hatch_chance3: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3fee1ba4, original_name='HatchChance3'
        ),
    })
    spin_attack_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xcfacff53, original_name='SpinAttackDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    max_spin_attack_delay: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6cb6d8c7, original_name='MaxSpinAttackDelay'
        ),
    })
    min_spin_attack_delay: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x682ce9ed, original_name='MinSpinAttackDelay'
        ),
    })
    unknown_0xbeaf2105: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbeaf2105, original_name='Unknown'
        ),
    })
    womb_open_time_max: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x54ff4d38, original_name='WombOpenTimeMax'
        ),
    })
    womb_open_time_min: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb29fe2d9, original_name='WombOpenTimeMin'
        ),
    })
    dodge_chance: float = dataclasses.field(default=0.0010000000474974513, metadata={
        'reflection': FieldReflection[float](
            float, id=0x47be3298, original_name='DodgeChance'
        ),
    })
    dash_at_player_dist_max: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x42647ad7, original_name='DashAtPlayerDistMax'
        ),
    })
    dash_at_player_dist_min: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa404d536, original_name='DashAtPlayerDistMin'
        ),
    })
    unknown_0x248d3599: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x248d3599, original_name='Unknown'
        ),
    })
    unknown_0xbfd77e62: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbfd77e62, original_name='Unknown'
        ),
    })
    random_move_dist_max: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcdaa2c74, original_name='RandomMoveDistMax'
        ),
    })
    random_move_dist_min: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2bca8395, original_name='RandomMoveDistMin'
        ),
    })
    patrol: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0xccdd3aca, original_name='Patrol', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    attack_path: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0xc845d3c0, original_name='AttackPath', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    combat: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0xcc7d2e98, original_name='Combat', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    stab_attack: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0xb9c3db94, original_name='StabAttack', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    spin_attack_out: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0x6ca56014, original_name='SpinAttackOut', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    spin_attack_back: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0xe20e51c3, original_name='SpinAttackBack', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    out_of_spin: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0x25a68a0e, original_name='OutOfSpin', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    spin_and_spawn: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0xd9b5d506, original_name='SpinAndSpawn', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    out_of_spin_and_spawn: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0x8bb1c3a2, original_name='OutOfSpinAndSpawn', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    stunned: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0x389cb515, original_name='Stunned', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    grappled: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0xfb2ddfad, original_name='Grappled', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    dash: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0xc558bc0d, original_name='Dash', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    retreat_and_spawn: FlyerMovementMode = dataclasses.field(default_factory=FlyerMovementMode, metadata={
        'reflection': FieldReflection[FlyerMovementMode](
            FlyerMovementMode, id=0x5fe13a7b, original_name='RetreatAndSpawn', from_json=FlyerMovementMode.from_json, to_json=FlyerMovementMode.to_json
        ),
    })
    claw: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0xfd38a106, original_name='Claw', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    retracted_claw_lf: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0x4d7dbeab, original_name='RetractedClawLF', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    retracted_claw_rf: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0xa17c09bb, original_name='RetractedClawRF', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    retracted_claw_lb: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0x11dc2dab, original_name='RetractedClawLB', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    retracted_claw_rb: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0xfddd9abb, original_name='RetractedClawRB', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    claw_open_weight_max: float = dataclasses.field(default=0.6000000238418579, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc99cee00, original_name='ClawOpenWeightMax'
        ),
    })
    claw_open_weight_min: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2ffc41e1, original_name='ClawOpenWeightMin'
        ),
    })
    claw_open_delta_max: float = dataclasses.field(default=0.800000011920929, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7f5d9ab7, original_name='ClawOpenDeltaMax'
        ),
    })
    claw_open_delta_min: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x993d3556, original_name='ClawOpenDeltaMin'
        ),
    })
    claw_closed_weight_max: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x08efeb79, original_name='ClawClosedWeightMax'
        ),
    })
    claw_closed_weight_min: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xee8f4498, original_name='ClawClosedWeightMin'
        ),
    })
    claw_close_delta_max: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc24d8fbd, original_name='ClawCloseDeltaMax'
        ),
    })
    claw_close_delta_min: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x242d205c, original_name='ClawCloseDeltaMin'
        ),
    })
    stun_threshold: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5bdd1e4c, original_name='StunThreshold'
        ),
    })
    electric_ball_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['ELSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x6da4a3b0, original_name='ElectricBallEffect'
        ),
    })
    sound_ball_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3fcd8b66, original_name='Sound_BallEffect'
        ),
    })
    electric_visor_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['ELSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xcc0af287, original_name='ElectricVisorEffect'
        ),
    })
    sound_visor_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa3e8ec4e, original_name='Sound_VisorEffect'
        ),
    })
    leg_hit_splash: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xf40a9c9d, original_name='LegHitSplash'
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
        if property_count != 87:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x25474550
        hearing_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x474fa589
        lose_interest_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf8b0c2bb
        lose_interest_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfe4588a1
        morphball_throw_force = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc2688b41
        womb_open_close_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7b0cc30d
        womb_attack_angle = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x742b3336
        womb_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0d9230d1
        body_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x243ab10d
        brain_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x012115a2
        brain_x_ray_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa12a4409
        brain_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9f0ff852
        leg_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb9e0c90d
        leg_damage_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x81d39802
        tentacle_suck_in_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xba002dcb
        tentacle_regrow_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf79a10b0
        tentacle_grapple_out_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc550a481
        unknown_0xc550a481 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95e7a2c2
        min_time_between_attacks = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76ba1c18
        max_time_between_attacks = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe08106ed
        stab_damage_time_first_person = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x88d7c540
        stab_damage_first_person = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xace62367
        stab_damage_time_morphball = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x620b1b3d
        stab_damage_morphball = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe1ae51d8
        max_attack_height = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc8d0acc0
        min_attack_height = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf3e8012d
        max_attack_forward = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe0ade786
        min_attack_forward = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0978b98a
        unknown_0x0978b98a = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcfcd32bb
        unknown_0xcfcd32bb = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x17d71349
        unknown_0x17d71349 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9aa90b6b
        recheck_path_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7626ec89
        recheck_path_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7915e2b3
        max_num_metroids = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xccc0cf92
        auto_spawn = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x75e0b0a7
        max_spawn_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2646a843
        min_spawn_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6089191d
        unknown_0x6089191d = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x258b5a9f
        unknown_0x258b5a9f = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2ae610e5
        min_spawn_point_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x354bae31
        hatch_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf4b2c801
        hatch_chance2 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3fee1ba4
        hatch_chance3 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcfacff53
        spin_attack_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_damage': 30.0, 'di_knock_back_power': 20.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6cb6d8c7
        max_spin_attack_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x682ce9ed
        min_spin_attack_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbeaf2105
        unknown_0xbeaf2105 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x54ff4d38
        womb_open_time_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb29fe2d9
        womb_open_time_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47be3298
        dodge_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42647ad7
        dash_at_player_dist_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa404d536
        dash_at_player_dist_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x248d3599
        unknown_0x248d3599 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbfd77e62
        unknown_0xbfd77e62 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcdaa2c74
        random_move_dist_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2bca8395
        random_move_dist_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xccdd3aca
        patrol = FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 3.0, 'acceleration': 1.0, 'facing_turn_rate': 30.0, 'turn_threshold': 181.0, 'use_avoidance': False, 'height_above_player': 7.0, 'floor_buffer': 10.0, 'ceiling_buffer': 8.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc845d3c0
        attack_path = FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 3.0, 'turn_threshold': 181.0, 'use_avoidance': False, 'height_above_player': 7.0, 'floor_buffer': 10.0, 'ceiling_buffer': 8.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcc7d2e98
        combat = FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 3.0, 'acceleration': 10.0, 'turn_threshold': 181.0, 'height_above_player': 6.0, 'floor_buffer': 11.0, 'ceiling_buffer': 8.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb9c3db94
        stab_attack = FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 0.10000000149011612, 'acceleration': 10.0, 'turn_rate': 10800.0, 'facing_turn_rate': 120.0, 'turn_threshold': 181.0, 'use_avoidance': False, 'height_above_player': 9.0, 'height_variation_max': 0.0, 'floor_buffer': 8.0, 'ceiling_buffer': 8.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6ca56014
        spin_attack_out = FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 30.0, 'acceleration': 50.0, 'turn_threshold': 181.0, 'use_avoidance': False, 'height_above_player': 6.0, 'height_variation_max': 0.0, 'floor_buffer': 3.5, 'ceiling_buffer': 8.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe20e51c3
        spin_attack_back = FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 30.0, 'acceleration': 10.0, 'facing_turn_rate': 1.0, 'turn_threshold': 181.0, 'use_avoidance': False, 'height_above_player': 6.0, 'height_variation_max': 1.0, 'floor_buffer': 5.0, 'ceiling_buffer': 8.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x25a68a0e
        out_of_spin = FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 1.0, 'acceleration': 10.0, 'turn_threshold': 181.0, 'height_above_player': 4.0, 'height_variation_max': 0.0, 'floor_buffer': 10.0, 'ceiling_buffer': 8.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd9b5d506
        spin_and_spawn = FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 30.0, 'acceleration': 20.0, 'facing_turn_rate': 1.0, 'turn_threshold': 181.0, 'height_above_player': 4.0, 'height_variation_max': 1.0, 'floor_buffer': 10.0, 'ceiling_buffer': 8.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8bb1c3a2
        out_of_spin_and_spawn = FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 1.0, 'acceleration': 10.0, 'turn_threshold': 181.0, 'height_above_player': 4.0, 'height_variation_max': 1.0, 'floor_buffer': 10.0, 'ceiling_buffer': 8.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x389cb515
        stunned = FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 5.0, 'turn_threshold': 181.0, 'use_avoidance': False, 'height_above_player': 8.0, 'height_variation_max': 1.0, 'floor_buffer': 5.0, 'ceiling_buffer': 8.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfb2ddfad
        grappled = FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 5.0, 'acceleration': 10.0, 'facing_turn_rate': 15.0, 'turn_threshold': 181.0, 'use_avoidance': False, 'height_above_player': 12.0, 'height_variation_min': 1.0, 'floor_buffer': 10.0, 'ceiling_buffer': 8.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc558bc0d
        dash = FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 40.0, 'acceleration': 100.0, 'turn_rate': 360.0, 'turn_threshold': 181.0, 'avoidance_range': 1.0, 'height_above_player': 5.0, 'height_variation_max': 0.5, 'floor_buffer': 13.0, 'ceiling_buffer': 8.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5fe13a7b
        retreat_and_spawn = FlyerMovementMode.from_stream(data, game, property_size, default_override={'acceleration': 20.0, 'turn_threshold': 181.0, 'height_above_player': 6.0, 'floor_buffer': 12.0, 'ceiling_buffer': 12.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfd38a106
        claw = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4d7dbeab
        retracted_claw_lf = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa17c09bb
        retracted_claw_rf = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x11dc2dab
        retracted_claw_lb = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfddd9abb
        retracted_claw_rb = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc99cee00
        claw_open_weight_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2ffc41e1
        claw_open_weight_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7f5d9ab7
        claw_open_delta_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x993d3556
        claw_open_delta_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08efeb79
        claw_closed_weight_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xee8f4498
        claw_closed_weight_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc24d8fbd
        claw_close_delta_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x242d205c
        claw_close_delta_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5bdd1e4c
        stun_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6da4a3b0
        electric_ball_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3fcd8b66
        sound_ball_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcc0af287
        electric_visor_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa3e8ec4e
        sound_visor_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf40a9c9d
        leg_hit_splash = structs.BIG_Q.unpack(data.read(8))[0]
    
        return cls(hearing_range, lose_interest_range, lose_interest_time, morphball_throw_force, womb_open_close_time, womb_attack_angle, womb_vulnerability, body_vulnerability, brain_vulnerability, brain_x_ray_radius, brain_radius, leg_vulnerability, leg_damage_threshold, tentacle_suck_in_time, tentacle_regrow_time, tentacle_grapple_out_time, unknown_0xc550a481, min_time_between_attacks, max_time_between_attacks, stab_damage_time_first_person, stab_damage_first_person, stab_damage_time_morphball, stab_damage_morphball, max_attack_height, min_attack_height, max_attack_forward, min_attack_forward, unknown_0x0978b98a, unknown_0xcfcd32bb, unknown_0x17d71349, recheck_path_time, recheck_path_distance, max_num_metroids, auto_spawn, max_spawn_delay, min_spawn_delay, unknown_0x6089191d, unknown_0x258b5a9f, min_spawn_point_distance, hatch_chance, hatch_chance2, hatch_chance3, spin_attack_damage, max_spin_attack_delay, min_spin_attack_delay, unknown_0xbeaf2105, womb_open_time_max, womb_open_time_min, dodge_chance, dash_at_player_dist_max, dash_at_player_dist_min, unknown_0x248d3599, unknown_0xbfd77e62, random_move_dist_max, random_move_dist_min, patrol, attack_path, combat, stab_attack, spin_attack_out, spin_attack_back, out_of_spin, spin_and_spawn, out_of_spin_and_spawn, stunned, grappled, dash, retreat_and_spawn, claw, retracted_claw_lf, retracted_claw_rf, retracted_claw_lb, retracted_claw_rb, claw_open_weight_max, claw_open_weight_min, claw_open_delta_max, claw_open_delta_min, claw_closed_weight_max, claw_closed_weight_min, claw_close_delta_max, claw_close_delta_min, stun_threshold, electric_ball_effect, sound_ball_effect, electric_visor_effect, sound_visor_effect, leg_hit_splash)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00W')  # 87 properties

        data.write(b'%GEP')  # 0x25474550
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hearing_range))

        data.write(b'GO\xa5\x89')  # 0x474fa589
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.lose_interest_range))

        data.write(b'\xf8\xb0\xc2\xbb')  # 0xf8b0c2bb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.lose_interest_time))

        data.write(b'\xfeE\x88\xa1')  # 0xfe4588a1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.morphball_throw_force))

        data.write(b'\xc2h\x8bA')  # 0xc2688b41
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.womb_open_close_time))

        data.write(b'{\x0c\xc3\r')  # 0x7b0cc30d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.womb_attack_angle))

        data.write(b't+36')  # 0x742b3336
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.womb_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\r\x920\xd1')  # 0xd9230d1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.body_vulnerability.to_stream(data, game)
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

        data.write(b'\x01!\x15\xa2')  # 0x12115a2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.brain_x_ray_radius))

        data.write(b'\xa1*D\t')  # 0xa12a4409
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.brain_radius))

        data.write(b'\x9f\x0f\xf8R')  # 0x9f0ff852
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.leg_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb9\xe0\xc9\r')  # 0xb9e0c90d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.leg_damage_threshold))

        data.write(b'\x81\xd3\x98\x02')  # 0x81d39802
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.tentacle_suck_in_time))

        data.write(b'\xba\x00-\xcb')  # 0xba002dcb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.tentacle_regrow_time))

        data.write(b'\xf7\x9a\x10\xb0')  # 0xf79a10b0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.tentacle_grapple_out_time))

        data.write(b'\xc5P\xa4\x81')  # 0xc550a481
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc550a481))

        data.write(b'\x95\xe7\xa2\xc2')  # 0x95e7a2c2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_attacks))

        data.write(b'v\xba\x1c\x18')  # 0x76ba1c18
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_time_between_attacks))

        data.write(b'\xe0\x81\x06\xed')  # 0xe08106ed
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stab_damage_time_first_person))

        data.write(b'\x88\xd7\xc5@')  # 0x88d7c540
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stab_damage_first_person))

        data.write(b'\xac\xe6#g')  # 0xace62367
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stab_damage_time_morphball))

        data.write(b'b\x0b\x1b=')  # 0x620b1b3d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stab_damage_morphball))

        data.write(b'\xe1\xaeQ\xd8')  # 0xe1ae51d8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_attack_height))

        data.write(b'\xc8\xd0\xac\xc0')  # 0xc8d0acc0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_attack_height))

        data.write(b'\xf3\xe8\x01-')  # 0xf3e8012d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_attack_forward))

        data.write(b'\xe0\xad\xe7\x86')  # 0xe0ade786
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_attack_forward))

        data.write(b'\tx\xb9\x8a')  # 0x978b98a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0978b98a))

        data.write(b'\xcf\xcd2\xbb')  # 0xcfcd32bb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcfcd32bb))

        data.write(b'\x17\xd7\x13I')  # 0x17d71349
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x17d71349))

        data.write(b'\x9a\xa9\x0bk')  # 0x9aa90b6b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.recheck_path_time))

        data.write(b'v&\xec\x89')  # 0x7626ec89
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.recheck_path_distance))

        data.write(b'y\x15\xe2\xb3')  # 0x7915e2b3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_num_metroids))

        data.write(b'\xcc\xc0\xcf\x92')  # 0xccc0cf92
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.auto_spawn))

        data.write(b'u\xe0\xb0\xa7')  # 0x75e0b0a7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_spawn_delay))

        data.write(b'&F\xa8C')  # 0x2646a843
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_spawn_delay))

        data.write(b'`\x89\x19\x1d')  # 0x6089191d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x6089191d))

        data.write(b'%\x8bZ\x9f')  # 0x258b5a9f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x258b5a9f))

        data.write(b'*\xe6\x10\xe5')  # 0x2ae610e5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_spawn_point_distance))

        data.write(b'5K\xae1')  # 0x354bae31
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hatch_chance))

        data.write(b'\xf4\xb2\xc8\x01')  # 0xf4b2c801
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hatch_chance2))

        data.write(b'?\xee\x1b\xa4')  # 0x3fee1ba4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hatch_chance3))

        data.write(b'\xcf\xac\xffS')  # 0xcfacff53
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.spin_attack_damage.to_stream(data, game, default_override={'di_damage': 30.0, 'di_knock_back_power': 20.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'l\xb6\xd8\xc7')  # 0x6cb6d8c7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_spin_attack_delay))

        data.write(b'h,\xe9\xed')  # 0x682ce9ed
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_spin_attack_delay))

        data.write(b'\xbe\xaf!\x05')  # 0xbeaf2105
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbeaf2105))

        data.write(b'T\xffM8')  # 0x54ff4d38
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.womb_open_time_max))

        data.write(b'\xb2\x9f\xe2\xd9')  # 0xb29fe2d9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.womb_open_time_min))

        data.write(b'G\xbe2\x98')  # 0x47be3298
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dodge_chance))

        data.write(b'Bdz\xd7')  # 0x42647ad7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dash_at_player_dist_max))

        data.write(b'\xa4\x04\xd56')  # 0xa404d536
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dash_at_player_dist_min))

        data.write(b'$\x8d5\x99')  # 0x248d3599
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x248d3599))

        data.write(b'\xbf\xd7~b')  # 0xbfd77e62
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbfd77e62))

        data.write(b'\xcd\xaa,t')  # 0xcdaa2c74
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.random_move_dist_max))

        data.write(b'+\xca\x83\x95')  # 0x2bca8395
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.random_move_dist_min))

        data.write(b'\xcc\xdd:\xca')  # 0xccdd3aca
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.patrol.to_stream(data, game, default_override={'speed': 3.0, 'acceleration': 1.0, 'facing_turn_rate': 30.0, 'turn_threshold': 181.0, 'use_avoidance': False, 'height_above_player': 7.0, 'floor_buffer': 10.0, 'ceiling_buffer': 8.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc8E\xd3\xc0')  # 0xc845d3c0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.attack_path.to_stream(data, game, default_override={'speed': 3.0, 'turn_threshold': 181.0, 'use_avoidance': False, 'height_above_player': 7.0, 'floor_buffer': 10.0, 'ceiling_buffer': 8.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xcc}.\x98')  # 0xcc7d2e98
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.combat.to_stream(data, game, default_override={'speed': 3.0, 'acceleration': 10.0, 'turn_threshold': 181.0, 'height_above_player': 6.0, 'floor_buffer': 11.0, 'ceiling_buffer': 8.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb9\xc3\xdb\x94')  # 0xb9c3db94
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stab_attack.to_stream(data, game, default_override={'speed': 0.10000000149011612, 'acceleration': 10.0, 'turn_rate': 10800.0, 'facing_turn_rate': 120.0, 'turn_threshold': 181.0, 'use_avoidance': False, 'height_above_player': 9.0, 'height_variation_max': 0.0, 'floor_buffer': 8.0, 'ceiling_buffer': 8.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'l\xa5`\x14')  # 0x6ca56014
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.spin_attack_out.to_stream(data, game, default_override={'speed': 30.0, 'acceleration': 50.0, 'turn_threshold': 181.0, 'use_avoidance': False, 'height_above_player': 6.0, 'height_variation_max': 0.0, 'floor_buffer': 3.5, 'ceiling_buffer': 8.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe2\x0eQ\xc3')  # 0xe20e51c3
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.spin_attack_back.to_stream(data, game, default_override={'speed': 30.0, 'acceleration': 10.0, 'facing_turn_rate': 1.0, 'turn_threshold': 181.0, 'use_avoidance': False, 'height_above_player': 6.0, 'height_variation_max': 1.0, 'floor_buffer': 5.0, 'ceiling_buffer': 8.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'%\xa6\x8a\x0e')  # 0x25a68a0e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.out_of_spin.to_stream(data, game, default_override={'speed': 1.0, 'acceleration': 10.0, 'turn_threshold': 181.0, 'height_above_player': 4.0, 'height_variation_max': 0.0, 'floor_buffer': 10.0, 'ceiling_buffer': 8.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd9\xb5\xd5\x06')  # 0xd9b5d506
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.spin_and_spawn.to_stream(data, game, default_override={'speed': 30.0, 'acceleration': 20.0, 'facing_turn_rate': 1.0, 'turn_threshold': 181.0, 'height_above_player': 4.0, 'height_variation_max': 1.0, 'floor_buffer': 10.0, 'ceiling_buffer': 8.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8b\xb1\xc3\xa2')  # 0x8bb1c3a2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.out_of_spin_and_spawn.to_stream(data, game, default_override={'speed': 1.0, 'acceleration': 10.0, 'turn_threshold': 181.0, 'height_above_player': 4.0, 'height_variation_max': 1.0, 'floor_buffer': 10.0, 'ceiling_buffer': 8.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'8\x9c\xb5\x15')  # 0x389cb515
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stunned.to_stream(data, game, default_override={'speed': 5.0, 'turn_threshold': 181.0, 'use_avoidance': False, 'height_above_player': 8.0, 'height_variation_max': 1.0, 'floor_buffer': 5.0, 'ceiling_buffer': 8.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfb-\xdf\xad')  # 0xfb2ddfad
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grappled.to_stream(data, game, default_override={'speed': 5.0, 'acceleration': 10.0, 'facing_turn_rate': 15.0, 'turn_threshold': 181.0, 'use_avoidance': False, 'height_above_player': 12.0, 'height_variation_min': 1.0, 'floor_buffer': 10.0, 'ceiling_buffer': 8.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc5X\xbc\r')  # 0xc558bc0d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.dash.to_stream(data, game, default_override={'speed': 40.0, 'acceleration': 100.0, 'turn_rate': 360.0, 'turn_threshold': 181.0, 'avoidance_range': 1.0, 'height_above_player': 5.0, 'height_variation_max': 0.5, 'floor_buffer': 13.0, 'ceiling_buffer': 8.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'_\xe1:{')  # 0x5fe13a7b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.retreat_and_spawn.to_stream(data, game, default_override={'acceleration': 20.0, 'turn_threshold': 181.0, 'height_above_player': 6.0, 'floor_buffer': 12.0, 'ceiling_buffer': 12.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfd8\xa1\x06')  # 0xfd38a106
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.claw.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'M}\xbe\xab')  # 0x4d7dbeab
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.retracted_claw_lf.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa1|\t\xbb')  # 0xa17c09bb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.retracted_claw_rf.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x11\xdc-\xab')  # 0x11dc2dab
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.retracted_claw_lb.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfd\xdd\x9a\xbb')  # 0xfddd9abb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.retracted_claw_rb.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc9\x9c\xee\x00')  # 0xc99cee00
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.claw_open_weight_max))

        data.write(b'/\xfcA\xe1')  # 0x2ffc41e1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.claw_open_weight_min))

        data.write(b'\x7f]\x9a\xb7')  # 0x7f5d9ab7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.claw_open_delta_max))

        data.write(b'\x99=5V')  # 0x993d3556
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.claw_open_delta_min))

        data.write(b'\x08\xef\xeby')  # 0x8efeb79
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.claw_closed_weight_max))

        data.write(b'\xee\x8fD\x98')  # 0xee8f4498
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.claw_closed_weight_min))

        data.write(b'\xc2M\x8f\xbd')  # 0xc24d8fbd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.claw_close_delta_max))

        data.write(b'$- \\')  # 0x242d205c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.claw_close_delta_min))

        data.write(b'[\xdd\x1eL')  # 0x5bdd1e4c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stun_threshold))

        data.write(b'm\xa4\xa3\xb0')  # 0x6da4a3b0
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.electric_ball_effect))

        data.write(b'?\xcd\x8bf')  # 0x3fcd8b66
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_ball_effect))

        data.write(b'\xcc\n\xf2\x87')  # 0xcc0af287
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.electric_visor_effect))

        data.write(b'\xa3\xe8\xecN')  # 0xa3e8ec4e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_visor_effect))

        data.write(b'\xf4\n\x9c\x9d')  # 0xf40a9c9d
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.leg_hit_splash))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MetroidHatcherDataJson", data)
        return cls(
            hearing_range=json_data['hearing_range'],
            lose_interest_range=json_data['lose_interest_range'],
            lose_interest_time=json_data['lose_interest_time'],
            morphball_throw_force=json_data['morphball_throw_force'],
            womb_open_close_time=json_data['womb_open_close_time'],
            womb_attack_angle=json_data['womb_attack_angle'],
            womb_vulnerability=DamageVulnerability.from_json(json_data['womb_vulnerability']),
            body_vulnerability=DamageVulnerability.from_json(json_data['body_vulnerability']),
            brain_vulnerability=DamageVulnerability.from_json(json_data['brain_vulnerability']),
            brain_x_ray_radius=json_data['brain_x_ray_radius'],
            brain_radius=json_data['brain_radius'],
            leg_vulnerability=DamageVulnerability.from_json(json_data['leg_vulnerability']),
            leg_damage_threshold=json_data['leg_damage_threshold'],
            tentacle_suck_in_time=json_data['tentacle_suck_in_time'],
            tentacle_regrow_time=json_data['tentacle_regrow_time'],
            tentacle_grapple_out_time=json_data['tentacle_grapple_out_time'],
            unknown_0xc550a481=json_data['unknown_0xc550a481'],
            min_time_between_attacks=json_data['min_time_between_attacks'],
            max_time_between_attacks=json_data['max_time_between_attacks'],
            stab_damage_time_first_person=json_data['stab_damage_time_first_person'],
            stab_damage_first_person=json_data['stab_damage_first_person'],
            stab_damage_time_morphball=json_data['stab_damage_time_morphball'],
            stab_damage_morphball=json_data['stab_damage_morphball'],
            max_attack_height=json_data['max_attack_height'],
            min_attack_height=json_data['min_attack_height'],
            max_attack_forward=json_data['max_attack_forward'],
            min_attack_forward=json_data['min_attack_forward'],
            unknown_0x0978b98a=json_data['unknown_0x0978b98a'],
            unknown_0xcfcd32bb=json_data['unknown_0xcfcd32bb'],
            unknown_0x17d71349=json_data['unknown_0x17d71349'],
            recheck_path_time=json_data['recheck_path_time'],
            recheck_path_distance=json_data['recheck_path_distance'],
            max_num_metroids=json_data['max_num_metroids'],
            auto_spawn=json_data['auto_spawn'],
            max_spawn_delay=json_data['max_spawn_delay'],
            min_spawn_delay=json_data['min_spawn_delay'],
            unknown_0x6089191d=json_data['unknown_0x6089191d'],
            unknown_0x258b5a9f=json_data['unknown_0x258b5a9f'],
            min_spawn_point_distance=json_data['min_spawn_point_distance'],
            hatch_chance=json_data['hatch_chance'],
            hatch_chance2=json_data['hatch_chance2'],
            hatch_chance3=json_data['hatch_chance3'],
            spin_attack_damage=DamageInfo.from_json(json_data['spin_attack_damage']),
            max_spin_attack_delay=json_data['max_spin_attack_delay'],
            min_spin_attack_delay=json_data['min_spin_attack_delay'],
            unknown_0xbeaf2105=json_data['unknown_0xbeaf2105'],
            womb_open_time_max=json_data['womb_open_time_max'],
            womb_open_time_min=json_data['womb_open_time_min'],
            dodge_chance=json_data['dodge_chance'],
            dash_at_player_dist_max=json_data['dash_at_player_dist_max'],
            dash_at_player_dist_min=json_data['dash_at_player_dist_min'],
            unknown_0x248d3599=json_data['unknown_0x248d3599'],
            unknown_0xbfd77e62=json_data['unknown_0xbfd77e62'],
            random_move_dist_max=json_data['random_move_dist_max'],
            random_move_dist_min=json_data['random_move_dist_min'],
            patrol=FlyerMovementMode.from_json(json_data['patrol']),
            attack_path=FlyerMovementMode.from_json(json_data['attack_path']),
            combat=FlyerMovementMode.from_json(json_data['combat']),
            stab_attack=FlyerMovementMode.from_json(json_data['stab_attack']),
            spin_attack_out=FlyerMovementMode.from_json(json_data['spin_attack_out']),
            spin_attack_back=FlyerMovementMode.from_json(json_data['spin_attack_back']),
            out_of_spin=FlyerMovementMode.from_json(json_data['out_of_spin']),
            spin_and_spawn=FlyerMovementMode.from_json(json_data['spin_and_spawn']),
            out_of_spin_and_spawn=FlyerMovementMode.from_json(json_data['out_of_spin_and_spawn']),
            stunned=FlyerMovementMode.from_json(json_data['stunned']),
            grappled=FlyerMovementMode.from_json(json_data['grappled']),
            dash=FlyerMovementMode.from_json(json_data['dash']),
            retreat_and_spawn=FlyerMovementMode.from_json(json_data['retreat_and_spawn']),
            claw=AnimationParameters.from_json(json_data['claw']),
            retracted_claw_lf=AnimationParameters.from_json(json_data['retracted_claw_lf']),
            retracted_claw_rf=AnimationParameters.from_json(json_data['retracted_claw_rf']),
            retracted_claw_lb=AnimationParameters.from_json(json_data['retracted_claw_lb']),
            retracted_claw_rb=AnimationParameters.from_json(json_data['retracted_claw_rb']),
            claw_open_weight_max=json_data['claw_open_weight_max'],
            claw_open_weight_min=json_data['claw_open_weight_min'],
            claw_open_delta_max=json_data['claw_open_delta_max'],
            claw_open_delta_min=json_data['claw_open_delta_min'],
            claw_closed_weight_max=json_data['claw_closed_weight_max'],
            claw_closed_weight_min=json_data['claw_closed_weight_min'],
            claw_close_delta_max=json_data['claw_close_delta_max'],
            claw_close_delta_min=json_data['claw_close_delta_min'],
            stun_threshold=json_data['stun_threshold'],
            electric_ball_effect=json_data['electric_ball_effect'],
            sound_ball_effect=json_data['sound_ball_effect'],
            electric_visor_effect=json_data['electric_visor_effect'],
            sound_visor_effect=json_data['sound_visor_effect'],
            leg_hit_splash=json_data['leg_hit_splash'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'hearing_range': self.hearing_range,
            'lose_interest_range': self.lose_interest_range,
            'lose_interest_time': self.lose_interest_time,
            'morphball_throw_force': self.morphball_throw_force,
            'womb_open_close_time': self.womb_open_close_time,
            'womb_attack_angle': self.womb_attack_angle,
            'womb_vulnerability': self.womb_vulnerability.to_json(),
            'body_vulnerability': self.body_vulnerability.to_json(),
            'brain_vulnerability': self.brain_vulnerability.to_json(),
            'brain_x_ray_radius': self.brain_x_ray_radius,
            'brain_radius': self.brain_radius,
            'leg_vulnerability': self.leg_vulnerability.to_json(),
            'leg_damage_threshold': self.leg_damage_threshold,
            'tentacle_suck_in_time': self.tentacle_suck_in_time,
            'tentacle_regrow_time': self.tentacle_regrow_time,
            'tentacle_grapple_out_time': self.tentacle_grapple_out_time,
            'unknown_0xc550a481': self.unknown_0xc550a481,
            'min_time_between_attacks': self.min_time_between_attacks,
            'max_time_between_attacks': self.max_time_between_attacks,
            'stab_damage_time_first_person': self.stab_damage_time_first_person,
            'stab_damage_first_person': self.stab_damage_first_person,
            'stab_damage_time_morphball': self.stab_damage_time_morphball,
            'stab_damage_morphball': self.stab_damage_morphball,
            'max_attack_height': self.max_attack_height,
            'min_attack_height': self.min_attack_height,
            'max_attack_forward': self.max_attack_forward,
            'min_attack_forward': self.min_attack_forward,
            'unknown_0x0978b98a': self.unknown_0x0978b98a,
            'unknown_0xcfcd32bb': self.unknown_0xcfcd32bb,
            'unknown_0x17d71349': self.unknown_0x17d71349,
            'recheck_path_time': self.recheck_path_time,
            'recheck_path_distance': self.recheck_path_distance,
            'max_num_metroids': self.max_num_metroids,
            'auto_spawn': self.auto_spawn,
            'max_spawn_delay': self.max_spawn_delay,
            'min_spawn_delay': self.min_spawn_delay,
            'unknown_0x6089191d': self.unknown_0x6089191d,
            'unknown_0x258b5a9f': self.unknown_0x258b5a9f,
            'min_spawn_point_distance': self.min_spawn_point_distance,
            'hatch_chance': self.hatch_chance,
            'hatch_chance2': self.hatch_chance2,
            'hatch_chance3': self.hatch_chance3,
            'spin_attack_damage': self.spin_attack_damage.to_json(),
            'max_spin_attack_delay': self.max_spin_attack_delay,
            'min_spin_attack_delay': self.min_spin_attack_delay,
            'unknown_0xbeaf2105': self.unknown_0xbeaf2105,
            'womb_open_time_max': self.womb_open_time_max,
            'womb_open_time_min': self.womb_open_time_min,
            'dodge_chance': self.dodge_chance,
            'dash_at_player_dist_max': self.dash_at_player_dist_max,
            'dash_at_player_dist_min': self.dash_at_player_dist_min,
            'unknown_0x248d3599': self.unknown_0x248d3599,
            'unknown_0xbfd77e62': self.unknown_0xbfd77e62,
            'random_move_dist_max': self.random_move_dist_max,
            'random_move_dist_min': self.random_move_dist_min,
            'patrol': self.patrol.to_json(),
            'attack_path': self.attack_path.to_json(),
            'combat': self.combat.to_json(),
            'stab_attack': self.stab_attack.to_json(),
            'spin_attack_out': self.spin_attack_out.to_json(),
            'spin_attack_back': self.spin_attack_back.to_json(),
            'out_of_spin': self.out_of_spin.to_json(),
            'spin_and_spawn': self.spin_and_spawn.to_json(),
            'out_of_spin_and_spawn': self.out_of_spin_and_spawn.to_json(),
            'stunned': self.stunned.to_json(),
            'grappled': self.grappled.to_json(),
            'dash': self.dash.to_json(),
            'retreat_and_spawn': self.retreat_and_spawn.to_json(),
            'claw': self.claw.to_json(),
            'retracted_claw_lf': self.retracted_claw_lf.to_json(),
            'retracted_claw_rf': self.retracted_claw_rf.to_json(),
            'retracted_claw_lb': self.retracted_claw_lb.to_json(),
            'retracted_claw_rb': self.retracted_claw_rb.to_json(),
            'claw_open_weight_max': self.claw_open_weight_max,
            'claw_open_weight_min': self.claw_open_weight_min,
            'claw_open_delta_max': self.claw_open_delta_max,
            'claw_open_delta_min': self.claw_open_delta_min,
            'claw_closed_weight_max': self.claw_closed_weight_max,
            'claw_closed_weight_min': self.claw_closed_weight_min,
            'claw_close_delta_max': self.claw_close_delta_max,
            'claw_close_delta_min': self.claw_close_delta_min,
            'stun_threshold': self.stun_threshold,
            'electric_ball_effect': self.electric_ball_effect,
            'sound_ball_effect': self.sound_ball_effect,
            'electric_visor_effect': self.electric_visor_effect,
            'sound_visor_effect': self.sound_visor_effect,
            'leg_hit_splash': self.leg_hit_splash,
        }

    def _dependencies_for_electric_ball_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.electric_ball_effect)

    def _dependencies_for_sound_ball_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_ball_effect)

    def _dependencies_for_electric_visor_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.electric_visor_effect)

    def _dependencies_for_sound_visor_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_visor_effect)

    def _dependencies_for_leg_hit_splash(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.leg_hit_splash)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.claw.dependencies_for, "claw", "AnimationParameters"),
            (self.retracted_claw_lf.dependencies_for, "retracted_claw_lf", "AnimationParameters"),
            (self.retracted_claw_rf.dependencies_for, "retracted_claw_rf", "AnimationParameters"),
            (self.retracted_claw_lb.dependencies_for, "retracted_claw_lb", "AnimationParameters"),
            (self.retracted_claw_rb.dependencies_for, "retracted_claw_rb", "AnimationParameters"),
            (self._dependencies_for_electric_ball_effect, "electric_ball_effect", "AssetId"),
            (self._dependencies_for_sound_ball_effect, "sound_ball_effect", "AssetId"),
            (self._dependencies_for_electric_visor_effect, "electric_visor_effect", "AssetId"),
            (self._dependencies_for_sound_visor_effect, "sound_visor_effect", "AssetId"),
            (self._dependencies_for_leg_hit_splash, "leg_hit_splash", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for MetroidHatcherData.{field_name} ({field_type}): {e}"
                )


def _decode_womb_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_body_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_brain_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_leg_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_spin_attack_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_damage': 30.0, 'di_knock_back_power': 20.0})


def _decode_patrol(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 3.0, 'acceleration': 1.0, 'facing_turn_rate': 30.0, 'turn_threshold': 181.0, 'use_avoidance': False, 'height_above_player': 7.0, 'floor_buffer': 10.0, 'ceiling_buffer': 8.0})


def _decode_attack_path(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 3.0, 'turn_threshold': 181.0, 'use_avoidance': False, 'height_above_player': 7.0, 'floor_buffer': 10.0, 'ceiling_buffer': 8.0})


def _decode_combat(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 3.0, 'acceleration': 10.0, 'turn_threshold': 181.0, 'height_above_player': 6.0, 'floor_buffer': 11.0, 'ceiling_buffer': 8.0})


def _decode_stab_attack(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 0.10000000149011612, 'acceleration': 10.0, 'turn_rate': 10800.0, 'facing_turn_rate': 120.0, 'turn_threshold': 181.0, 'use_avoidance': False, 'height_above_player': 9.0, 'height_variation_max': 0.0, 'floor_buffer': 8.0, 'ceiling_buffer': 8.0})


def _decode_spin_attack_out(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 30.0, 'acceleration': 50.0, 'turn_threshold': 181.0, 'use_avoidance': False, 'height_above_player': 6.0, 'height_variation_max': 0.0, 'floor_buffer': 3.5, 'ceiling_buffer': 8.0})


def _decode_spin_attack_back(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 30.0, 'acceleration': 10.0, 'facing_turn_rate': 1.0, 'turn_threshold': 181.0, 'use_avoidance': False, 'height_above_player': 6.0, 'height_variation_max': 1.0, 'floor_buffer': 5.0, 'ceiling_buffer': 8.0})


def _decode_out_of_spin(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 1.0, 'acceleration': 10.0, 'turn_threshold': 181.0, 'height_above_player': 4.0, 'height_variation_max': 0.0, 'floor_buffer': 10.0, 'ceiling_buffer': 8.0})


def _decode_spin_and_spawn(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 30.0, 'acceleration': 20.0, 'facing_turn_rate': 1.0, 'turn_threshold': 181.0, 'height_above_player': 4.0, 'height_variation_max': 1.0, 'floor_buffer': 10.0, 'ceiling_buffer': 8.0})


def _decode_out_of_spin_and_spawn(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 1.0, 'acceleration': 10.0, 'turn_threshold': 181.0, 'height_above_player': 4.0, 'height_variation_max': 1.0, 'floor_buffer': 10.0, 'ceiling_buffer': 8.0})


def _decode_stunned(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 5.0, 'turn_threshold': 181.0, 'use_avoidance': False, 'height_above_player': 8.0, 'height_variation_max': 1.0, 'floor_buffer': 5.0, 'ceiling_buffer': 8.0})


def _decode_grappled(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 5.0, 'acceleration': 10.0, 'facing_turn_rate': 15.0, 'turn_threshold': 181.0, 'use_avoidance': False, 'height_above_player': 12.0, 'height_variation_min': 1.0, 'floor_buffer': 10.0, 'ceiling_buffer': 8.0})


def _decode_dash(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size, default_override={'speed': 40.0, 'acceleration': 100.0, 'turn_rate': 360.0, 'turn_threshold': 181.0, 'avoidance_range': 1.0, 'height_above_player': 5.0, 'height_variation_max': 0.5, 'floor_buffer': 13.0, 'ceiling_buffer': 8.0})


def _decode_retreat_and_spawn(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerMovementMode:
    return FlyerMovementMode.from_stream(data, game, property_size, default_override={'acceleration': 20.0, 'turn_threshold': 181.0, 'height_above_player': 6.0, 'floor_buffer': 12.0, 'ceiling_buffer': 12.0})


def _decode_claw(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_retracted_claw_lf(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_retracted_claw_rf(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_retracted_claw_lb(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_retracted_claw_rb(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x25474550: ('hearing_range', structs.decode_BIG_f),
    0x474fa589: ('lose_interest_range', structs.decode_BIG_f),
    0xf8b0c2bb: ('lose_interest_time', structs.decode_BIG_f),
    0xfe4588a1: ('morphball_throw_force', structs.decode_BIG_f),
    0xc2688b41: ('womb_open_close_time', structs.decode_BIG_f),
    0x7b0cc30d: ('womb_attack_angle', structs.decode_BIG_f),
    0x742b3336: ('womb_vulnerability', _decode_womb_vulnerability),
    0x0d9230d1: ('body_vulnerability', _decode_body_vulnerability),
    0x243ab10d: ('brain_vulnerability', _decode_brain_vulnerability),
    0x012115a2: ('brain_x_ray_radius', structs.decode_BIG_f),
    0xa12a4409: ('brain_radius', structs.decode_BIG_f),
    0x9f0ff852: ('leg_vulnerability', _decode_leg_vulnerability),
    0xb9e0c90d: ('leg_damage_threshold', structs.decode_BIG_f),
    0x81d39802: ('tentacle_suck_in_time', structs.decode_BIG_f),
    0xba002dcb: ('tentacle_regrow_time', structs.decode_BIG_f),
    0xf79a10b0: ('tentacle_grapple_out_time', structs.decode_BIG_f),
    0xc550a481: ('unknown_0xc550a481', structs.decode_BIG_f),
    0x95e7a2c2: ('min_time_between_attacks', structs.decode_BIG_f),
    0x76ba1c18: ('max_time_between_attacks', structs.decode_BIG_f),
    0xe08106ed: ('stab_damage_time_first_person', structs.decode_BIG_f),
    0x88d7c540: ('stab_damage_first_person', structs.decode_BIG_f),
    0xace62367: ('stab_damage_time_morphball', structs.decode_BIG_f),
    0x620b1b3d: ('stab_damage_morphball', structs.decode_BIG_f),
    0xe1ae51d8: ('max_attack_height', structs.decode_BIG_f),
    0xc8d0acc0: ('min_attack_height', structs.decode_BIG_f),
    0xf3e8012d: ('max_attack_forward', structs.decode_BIG_f),
    0xe0ade786: ('min_attack_forward', structs.decode_BIG_f),
    0x0978b98a: ('unknown_0x0978b98a', structs.decode_BIG_f),
    0xcfcd32bb: ('unknown_0xcfcd32bb', structs.decode_BIG_f),
    0x17d71349: ('unknown_0x17d71349', structs.decode_BIG_f),
    0x9aa90b6b: ('recheck_path_time', structs.decode_BIG_f),
    0x7626ec89: ('recheck_path_distance', structs.decode_BIG_f),
    0x7915e2b3: ('max_num_metroids', structs.decode_BIG_l),
    0xccc0cf92: ('auto_spawn', structs.decode_BIG_bool_),
    0x75e0b0a7: ('max_spawn_delay', structs.decode_BIG_f),
    0x2646a843: ('min_spawn_delay', structs.decode_BIG_f),
    0x6089191d: ('unknown_0x6089191d', structs.decode_BIG_l),
    0x258b5a9f: ('unknown_0x258b5a9f', structs.decode_BIG_l),
    0x2ae610e5: ('min_spawn_point_distance', structs.decode_BIG_f),
    0x354bae31: ('hatch_chance', structs.decode_BIG_f),
    0xf4b2c801: ('hatch_chance2', structs.decode_BIG_f),
    0x3fee1ba4: ('hatch_chance3', structs.decode_BIG_f),
    0xcfacff53: ('spin_attack_damage', _decode_spin_attack_damage),
    0x6cb6d8c7: ('max_spin_attack_delay', structs.decode_BIG_f),
    0x682ce9ed: ('min_spin_attack_delay', structs.decode_BIG_f),
    0xbeaf2105: ('unknown_0xbeaf2105', structs.decode_BIG_f),
    0x54ff4d38: ('womb_open_time_max', structs.decode_BIG_f),
    0xb29fe2d9: ('womb_open_time_min', structs.decode_BIG_f),
    0x47be3298: ('dodge_chance', structs.decode_BIG_f),
    0x42647ad7: ('dash_at_player_dist_max', structs.decode_BIG_f),
    0xa404d536: ('dash_at_player_dist_min', structs.decode_BIG_f),
    0x248d3599: ('unknown_0x248d3599', structs.decode_BIG_f),
    0xbfd77e62: ('unknown_0xbfd77e62', structs.decode_BIG_f),
    0xcdaa2c74: ('random_move_dist_max', structs.decode_BIG_f),
    0x2bca8395: ('random_move_dist_min', structs.decode_BIG_f),
    0xccdd3aca: ('patrol', _decode_patrol),
    0xc845d3c0: ('attack_path', _decode_attack_path),
    0xcc7d2e98: ('combat', _decode_combat),
    0xb9c3db94: ('stab_attack', _decode_stab_attack),
    0x6ca56014: ('spin_attack_out', _decode_spin_attack_out),
    0xe20e51c3: ('spin_attack_back', _decode_spin_attack_back),
    0x25a68a0e: ('out_of_spin', _decode_out_of_spin),
    0xd9b5d506: ('spin_and_spawn', _decode_spin_and_spawn),
    0x8bb1c3a2: ('out_of_spin_and_spawn', _decode_out_of_spin_and_spawn),
    0x389cb515: ('stunned', _decode_stunned),
    0xfb2ddfad: ('grappled', _decode_grappled),
    0xc558bc0d: ('dash', _decode_dash),
    0x5fe13a7b: ('retreat_and_spawn', _decode_retreat_and_spawn),
    0xfd38a106: ('claw', _decode_claw),
    0x4d7dbeab: ('retracted_claw_lf', _decode_retracted_claw_lf),
    0xa17c09bb: ('retracted_claw_rf', _decode_retracted_claw_rf),
    0x11dc2dab: ('retracted_claw_lb', _decode_retracted_claw_lb),
    0xfddd9abb: ('retracted_claw_rb', _decode_retracted_claw_rb),
    0xc99cee00: ('claw_open_weight_max', structs.decode_BIG_f),
    0x2ffc41e1: ('claw_open_weight_min', structs.decode_BIG_f),
    0x7f5d9ab7: ('claw_open_delta_max', structs.decode_BIG_f),
    0x993d3556: ('claw_open_delta_min', structs.decode_BIG_f),
    0x08efeb79: ('claw_closed_weight_max', structs.decode_BIG_f),
    0xee8f4498: ('claw_closed_weight_min', structs.decode_BIG_f),
    0xc24d8fbd: ('claw_close_delta_max', structs.decode_BIG_f),
    0x242d205c: ('claw_close_delta_min', structs.decode_BIG_f),
    0x5bdd1e4c: ('stun_threshold', structs.decode_BIG_f),
    0x6da4a3b0: ('electric_ball_effect', structs.decode_BIG_Q),
    0x3fcd8b66: ('sound_ball_effect', structs.decode_BIG_Q),
    0xcc0af287: ('electric_visor_effect', structs.decode_BIG_Q),
    0xa3e8ec4e: ('sound_visor_effect', structs.decode_BIG_Q),
    0xf40a9c9d: ('leg_hit_splash', structs.decode_BIG_Q),
}
