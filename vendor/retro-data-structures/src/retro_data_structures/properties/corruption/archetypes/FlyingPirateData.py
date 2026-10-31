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
from retro_data_structures.properties.corruption.archetypes.FlyingPirateArmorData import FlyingPirateArmorData
from retro_data_structures.properties.corruption.archetypes.FlyingPirateBlasterData import FlyingPirateBlasterData
from retro_data_structures.properties.corruption.archetypes.FlyingPirateFlipSwitchData import FlyingPirateFlipSwitchData
from retro_data_structures.properties.corruption.archetypes.FlyingPirateHelixMissileData import FlyingPirateHelixMissileData
from retro_data_structures.properties.corruption.archetypes.FlyingPirateHyperModeData import FlyingPirateHyperModeData
from retro_data_structures.properties.corruption.archetypes.FlyingPirateJetPackData import FlyingPirateJetPackData
from retro_data_structures.properties.corruption.archetypes.RagDollData import RagDollData
from retro_data_structures.properties.corruption.archetypes.SpacePirateWeaponData import SpacePirateWeaponData
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class FlyingPirateDataJson(typing_extensions.TypedDict):
        is_initially_on_ground: bool
        unknown_0xf37267ef: bool
        disable_particle_blaster: bool
        disable_weapon_pods: bool
        unknown_0x767f168e: bool
        keep_target_time: float
        max_select_target_distance: float
        select_target_distance_factor: float
        unknown_0x610c0165: float
        unknown_0x0d2531e7: float
        land_check_time: float
        land_check_chance: float
        flight_check_time: float
        flight_check_chance: float
        left_weapon_pod_model: int
        right_weapon_pod_model: int
        spin_death_flight_speed: float
        spin_death_turn_speed: float
        flight_max_speed: float
        flight_acceleration: float
        flight_deceleration: float
        flight_turn_speed: float
        flight_hover_height: float
        unknown_0x7bb971f1: float
        rotate_rolling_duration: float
        dip_check_time: float
        dip_chance: float
        dodge_chance: float
        min_attack_run_time: float
        max_attack_run_range: float
        attack_run_chance: float
        warp_jump_damage_threshold: float
        warp_jump_damage_window: float
        particle_blaster: json_util.JsonObject
        helix_missiles: json_util.JsonObject
        gel_bombs: json_util.JsonObject
        normal_hyper_mode: json_util.JsonObject
        hard_hyper_mode: json_util.JsonObject
        elite_hyper_mode: json_util.JsonObject
        armor: json_util.JsonObject
        jet_pack: json_util.JsonObject
        rag_doll: json_util.JsonObject
        is_gandrayda: bool
        unknown_0x516cb29d: bool
        flip_switch_data: json_util.JsonObject
        morph_health_threshold: float
    

@dataclasses.dataclass()
class FlyingPirateData(BaseProperty):
    is_initially_on_ground: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xa8b7379d, original_name='IsInitiallyOnGround'
        ),
    })
    unknown_0xf37267ef: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xf37267ef, original_name='Unknown'
        ),
    })
    disable_particle_blaster: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xf56589a6, original_name='DisableParticleBlaster'
        ),
    })
    disable_weapon_pods: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xcdd1db4f, original_name='DisableWeaponPods'
        ),
    })
    unknown_0x767f168e: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x767f168e, original_name='Unknown'
        ),
    })
    keep_target_time: float = dataclasses.field(default=7.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x89a5edc8, original_name='KeepTargetTime'
        ),
    })
    max_select_target_distance: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd73ec5bc, original_name='MaxSelectTargetDistance'
        ),
    })
    select_target_distance_factor: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x907f8e96, original_name='SelectTargetDistanceFactor'
        ),
    })
    unknown_0x610c0165: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x610c0165, original_name='Unknown'
        ),
    })
    unknown_0x0d2531e7: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0d2531e7, original_name='Unknown'
        ),
    })
    land_check_time: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7f7f8028, original_name='LandCheckTime'
        ),
    })
    land_check_chance: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd2046050, original_name='LandCheckChance'
        ),
    })
    flight_check_time: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2454fb04, original_name='FlightCheckTime'
        ),
    })
    flight_check_chance: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2ce2f861, original_name='FlightCheckChance'
        ),
    })
    left_weapon_pod_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x95c8719d, original_name='LeftWeaponPodModel'
        ),
    })
    right_weapon_pod_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa0705491, original_name='RightWeaponPodModel'
        ),
    })
    spin_death_flight_speed: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4fa0ea5c, original_name='SpinDeathFlightSpeed'
        ),
    })
    spin_death_turn_speed: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0263834d, original_name='SpinDeathTurnSpeed'
        ),
    })
    flight_max_speed: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd4dec629, original_name='FlightMaxSpeed'
        ),
    })
    flight_acceleration: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7a2bb377, original_name='FlightAcceleration'
        ),
    })
    flight_deceleration: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdd14361f, original_name='FlightDeceleration'
        ),
    })
    flight_turn_speed: float = dataclasses.field(default=90.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6c317b96, original_name='FlightTurnSpeed'
        ),
    })
    flight_hover_height: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7e7afdc2, original_name='FlightHoverHeight'
        ),
    })
    unknown_0x7bb971f1: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7bb971f1, original_name='Unknown'
        ),
    })
    rotate_rolling_duration: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3aae4e77, original_name='RotateRollingDuration'
        ),
    })
    dip_check_time: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9e156b9d, original_name='DipCheckTime'
        ),
    })
    dip_chance: float = dataclasses.field(default=80.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x357ed28d, original_name='DipChance'
        ),
    })
    dodge_chance: float = dataclasses.field(default=80.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x47be3298, original_name='DodgeChance'
        ),
    })
    min_attack_run_time: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xac2b567d, original_name='MinAttackRunTime'
        ),
    })
    max_attack_run_range: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x740b661e, original_name='MaxAttackRunRange'
        ),
    })
    attack_run_chance: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc50d5431, original_name='AttackRunChance'
        ),
    })
    warp_jump_damage_threshold: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc02bb7c5, original_name='WarpJumpDamageThreshold'
        ),
    })
    warp_jump_damage_window: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2b15406d, original_name='WarpJumpDamageWindow'
        ),
    })
    particle_blaster: FlyingPirateBlasterData = dataclasses.field(default_factory=FlyingPirateBlasterData, metadata={
        'reflection': FieldReflection[FlyingPirateBlasterData](
            FlyingPirateBlasterData, id=0x672b454d, original_name='ParticleBlaster', from_json=FlyingPirateBlasterData.from_json, to_json=FlyingPirateBlasterData.to_json
        ),
    })
    helix_missiles: FlyingPirateHelixMissileData = dataclasses.field(default_factory=FlyingPirateHelixMissileData, metadata={
        'reflection': FieldReflection[FlyingPirateHelixMissileData](
            FlyingPirateHelixMissileData, id=0x92b304ad, original_name='HelixMissiles', from_json=FlyingPirateHelixMissileData.from_json, to_json=FlyingPirateHelixMissileData.to_json
        ),
    })
    gel_bombs: SpacePirateWeaponData = dataclasses.field(default_factory=SpacePirateWeaponData, metadata={
        'reflection': FieldReflection[SpacePirateWeaponData](
            SpacePirateWeaponData, id=0x2263e77f, original_name='GelBombs', from_json=SpacePirateWeaponData.from_json, to_json=SpacePirateWeaponData.to_json
        ),
    })
    normal_hyper_mode: FlyingPirateHyperModeData = dataclasses.field(default_factory=FlyingPirateHyperModeData, metadata={
        'reflection': FieldReflection[FlyingPirateHyperModeData](
            FlyingPirateHyperModeData, id=0x3f07905e, original_name='NormalHyperMode', from_json=FlyingPirateHyperModeData.from_json, to_json=FlyingPirateHyperModeData.to_json
        ),
    })
    hard_hyper_mode: FlyingPirateHyperModeData = dataclasses.field(default_factory=FlyingPirateHyperModeData, metadata={
        'reflection': FieldReflection[FlyingPirateHyperModeData](
            FlyingPirateHyperModeData, id=0x097203ab, original_name='HardHyperMode', from_json=FlyingPirateHyperModeData.from_json, to_json=FlyingPirateHyperModeData.to_json
        ),
    })
    elite_hyper_mode: FlyingPirateHyperModeData = dataclasses.field(default_factory=FlyingPirateHyperModeData, metadata={
        'reflection': FieldReflection[FlyingPirateHyperModeData](
            FlyingPirateHyperModeData, id=0x4123a3b6, original_name='EliteHyperMode', from_json=FlyingPirateHyperModeData.from_json, to_json=FlyingPirateHyperModeData.to_json
        ),
    })
    armor: FlyingPirateArmorData = dataclasses.field(default_factory=FlyingPirateArmorData, metadata={
        'reflection': FieldReflection[FlyingPirateArmorData](
            FlyingPirateArmorData, id=0x70b96a25, original_name='Armor', from_json=FlyingPirateArmorData.from_json, to_json=FlyingPirateArmorData.to_json
        ),
    })
    jet_pack: FlyingPirateJetPackData = dataclasses.field(default_factory=FlyingPirateJetPackData, metadata={
        'reflection': FieldReflection[FlyingPirateJetPackData](
            FlyingPirateJetPackData, id=0xfbaa9f01, original_name='JetPack', from_json=FlyingPirateJetPackData.from_json, to_json=FlyingPirateJetPackData.to_json
        ),
    })
    rag_doll: RagDollData = dataclasses.field(default_factory=RagDollData, metadata={
        'reflection': FieldReflection[RagDollData](
            RagDollData, id=0xe39738ea, original_name='RagDoll', from_json=RagDollData.from_json, to_json=RagDollData.to_json
        ),
    })
    is_gandrayda: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x531a8c85, original_name='IsGandrayda'
        ),
    })
    unknown_0x516cb29d: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x516cb29d, original_name='Unknown'
        ),
    })
    flip_switch_data: FlyingPirateFlipSwitchData = dataclasses.field(default_factory=FlyingPirateFlipSwitchData, metadata={
        'reflection': FieldReflection[FlyingPirateFlipSwitchData](
            FlyingPirateFlipSwitchData, id=0xf82f61c9, original_name='FlipSwitchData', from_json=FlyingPirateFlipSwitchData.from_json, to_json=FlyingPirateFlipSwitchData.to_json
        ),
    })
    morph_health_threshold: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x97f7a52d, original_name='MorphHealthThreshold'
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
        if property_count != 46:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa8b7379d
        is_initially_on_ground = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf37267ef
        unknown_0xf37267ef = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf56589a6
        disable_particle_blaster = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcdd1db4f
        disable_weapon_pods = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x767f168e
        unknown_0x767f168e = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x89a5edc8
        keep_target_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd73ec5bc
        max_select_target_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x907f8e96
        select_target_distance_factor = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x610c0165
        unknown_0x610c0165 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0d2531e7
        unknown_0x0d2531e7 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7f7f8028
        land_check_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd2046050
        land_check_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2454fb04
        flight_check_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2ce2f861
        flight_check_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95c8719d
        left_weapon_pod_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa0705491
        right_weapon_pod_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4fa0ea5c
        spin_death_flight_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0263834d
        spin_death_turn_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd4dec629
        flight_max_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7a2bb377
        flight_acceleration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdd14361f
        flight_deceleration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6c317b96
        flight_turn_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e7afdc2
        flight_hover_height = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7bb971f1
        unknown_0x7bb971f1 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3aae4e77
        rotate_rolling_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9e156b9d
        dip_check_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x357ed28d
        dip_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47be3298
        dodge_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xac2b567d
        min_attack_run_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x740b661e
        max_attack_run_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc50d5431
        attack_run_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc02bb7c5
        warp_jump_damage_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2b15406d
        warp_jump_damage_window = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x672b454d
        particle_blaster = FlyingPirateBlasterData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x92b304ad
        helix_missiles = FlyingPirateHelixMissileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2263e77f
        gel_bombs = SpacePirateWeaponData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3f07905e
        normal_hyper_mode = FlyingPirateHyperModeData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x097203ab
        hard_hyper_mode = FlyingPirateHyperModeData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4123a3b6
        elite_hyper_mode = FlyingPirateHyperModeData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x70b96a25
        armor = FlyingPirateArmorData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfbaa9f01
        jet_pack = FlyingPirateJetPackData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe39738ea
        rag_doll = RagDollData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x531a8c85
        is_gandrayda = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x516cb29d
        unknown_0x516cb29d = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf82f61c9
        flip_switch_data = FlyingPirateFlipSwitchData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x97f7a52d
        morph_health_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(is_initially_on_ground, unknown_0xf37267ef, disable_particle_blaster, disable_weapon_pods, unknown_0x767f168e, keep_target_time, max_select_target_distance, select_target_distance_factor, unknown_0x610c0165, unknown_0x0d2531e7, land_check_time, land_check_chance, flight_check_time, flight_check_chance, left_weapon_pod_model, right_weapon_pod_model, spin_death_flight_speed, spin_death_turn_speed, flight_max_speed, flight_acceleration, flight_deceleration, flight_turn_speed, flight_hover_height, unknown_0x7bb971f1, rotate_rolling_duration, dip_check_time, dip_chance, dodge_chance, min_attack_run_time, max_attack_run_range, attack_run_chance, warp_jump_damage_threshold, warp_jump_damage_window, particle_blaster, helix_missiles, gel_bombs, normal_hyper_mode, hard_hyper_mode, elite_hyper_mode, armor, jet_pack, rag_doll, is_gandrayda, unknown_0x516cb29d, flip_switch_data, morph_health_threshold)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00.')  # 46 properties

        data.write(b'\xa8\xb77\x9d')  # 0xa8b7379d
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_initially_on_ground))

        data.write(b'\xf3rg\xef')  # 0xf37267ef
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xf37267ef))

        data.write(b'\xf5e\x89\xa6')  # 0xf56589a6
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.disable_particle_blaster))

        data.write(b'\xcd\xd1\xdbO')  # 0xcdd1db4f
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.disable_weapon_pods))

        data.write(b'v\x7f\x16\x8e')  # 0x767f168e
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x767f168e))

        data.write(b'\x89\xa5\xed\xc8')  # 0x89a5edc8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.keep_target_time))

        data.write(b'\xd7>\xc5\xbc')  # 0xd73ec5bc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_select_target_distance))

        data.write(b'\x90\x7f\x8e\x96')  # 0x907f8e96
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.select_target_distance_factor))

        data.write(b'a\x0c\x01e')  # 0x610c0165
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x610c0165))

        data.write(b'\r%1\xe7')  # 0xd2531e7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0d2531e7))

        data.write(b'\x7f\x7f\x80(')  # 0x7f7f8028
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.land_check_time))

        data.write(b'\xd2\x04`P')  # 0xd2046050
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.land_check_chance))

        data.write(b'$T\xfb\x04')  # 0x2454fb04
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flight_check_time))

        data.write(b',\xe2\xf8a')  # 0x2ce2f861
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flight_check_chance))

        data.write(b'\x95\xc8q\x9d')  # 0x95c8719d
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.left_weapon_pod_model))

        data.write(b'\xa0pT\x91')  # 0xa0705491
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.right_weapon_pod_model))

        data.write(b'O\xa0\xea\\')  # 0x4fa0ea5c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.spin_death_flight_speed))

        data.write(b'\x02c\x83M')  # 0x263834d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.spin_death_turn_speed))

        data.write(b'\xd4\xde\xc6)')  # 0xd4dec629
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flight_max_speed))

        data.write(b'z+\xb3w')  # 0x7a2bb377
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flight_acceleration))

        data.write(b'\xdd\x146\x1f')  # 0xdd14361f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flight_deceleration))

        data.write(b'l1{\x96')  # 0x6c317b96
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flight_turn_speed))

        data.write(b'~z\xfd\xc2')  # 0x7e7afdc2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flight_hover_height))

        data.write(b'{\xb9q\xf1')  # 0x7bb971f1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7bb971f1))

        data.write(b':\xaeNw')  # 0x3aae4e77
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotate_rolling_duration))

        data.write(b'\x9e\x15k\x9d')  # 0x9e156b9d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dip_check_time))

        data.write(b'5~\xd2\x8d')  # 0x357ed28d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dip_chance))

        data.write(b'G\xbe2\x98')  # 0x47be3298
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dodge_chance))

        data.write(b'\xac+V}')  # 0xac2b567d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_attack_run_time))

        data.write(b't\x0bf\x1e')  # 0x740b661e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_attack_run_range))

        data.write(b'\xc5\rT1')  # 0xc50d5431
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.attack_run_chance))

        data.write(b'\xc0+\xb7\xc5')  # 0xc02bb7c5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.warp_jump_damage_threshold))

        data.write(b'+\x15@m')  # 0x2b15406d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.warp_jump_damage_window))

        data.write(b'g+EM')  # 0x672b454d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.particle_blaster.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x92\xb3\x04\xad')  # 0x92b304ad
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.helix_missiles.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'"c\xe7\x7f')  # 0x2263e77f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.gel_bombs.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'?\x07\x90^')  # 0x3f07905e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.normal_hyper_mode.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\tr\x03\xab')  # 0x97203ab
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hard_hyper_mode.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'A#\xa3\xb6')  # 0x4123a3b6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.elite_hyper_mode.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'p\xb9j%')  # 0x70b96a25
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.armor.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfb\xaa\x9f\x01')  # 0xfbaa9f01
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.jet_pack.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe3\x978\xea')  # 0xe39738ea
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.rag_doll.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'S\x1a\x8c\x85')  # 0x531a8c85
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_gandrayda))

        data.write(b'Ql\xb2\x9d')  # 0x516cb29d
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x516cb29d))

        data.write(b'\xf8/a\xc9')  # 0xf82f61c9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.flip_switch_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x97\xf7\xa5-')  # 0x97f7a52d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.morph_health_threshold))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FlyingPirateDataJson", data)
        return cls(
            is_initially_on_ground=json_data['is_initially_on_ground'],
            unknown_0xf37267ef=json_data['unknown_0xf37267ef'],
            disable_particle_blaster=json_data['disable_particle_blaster'],
            disable_weapon_pods=json_data['disable_weapon_pods'],
            unknown_0x767f168e=json_data['unknown_0x767f168e'],
            keep_target_time=json_data['keep_target_time'],
            max_select_target_distance=json_data['max_select_target_distance'],
            select_target_distance_factor=json_data['select_target_distance_factor'],
            unknown_0x610c0165=json_data['unknown_0x610c0165'],
            unknown_0x0d2531e7=json_data['unknown_0x0d2531e7'],
            land_check_time=json_data['land_check_time'],
            land_check_chance=json_data['land_check_chance'],
            flight_check_time=json_data['flight_check_time'],
            flight_check_chance=json_data['flight_check_chance'],
            left_weapon_pod_model=json_data['left_weapon_pod_model'],
            right_weapon_pod_model=json_data['right_weapon_pod_model'],
            spin_death_flight_speed=json_data['spin_death_flight_speed'],
            spin_death_turn_speed=json_data['spin_death_turn_speed'],
            flight_max_speed=json_data['flight_max_speed'],
            flight_acceleration=json_data['flight_acceleration'],
            flight_deceleration=json_data['flight_deceleration'],
            flight_turn_speed=json_data['flight_turn_speed'],
            flight_hover_height=json_data['flight_hover_height'],
            unknown_0x7bb971f1=json_data['unknown_0x7bb971f1'],
            rotate_rolling_duration=json_data['rotate_rolling_duration'],
            dip_check_time=json_data['dip_check_time'],
            dip_chance=json_data['dip_chance'],
            dodge_chance=json_data['dodge_chance'],
            min_attack_run_time=json_data['min_attack_run_time'],
            max_attack_run_range=json_data['max_attack_run_range'],
            attack_run_chance=json_data['attack_run_chance'],
            warp_jump_damage_threshold=json_data['warp_jump_damage_threshold'],
            warp_jump_damage_window=json_data['warp_jump_damage_window'],
            particle_blaster=FlyingPirateBlasterData.from_json(json_data['particle_blaster']),
            helix_missiles=FlyingPirateHelixMissileData.from_json(json_data['helix_missiles']),
            gel_bombs=SpacePirateWeaponData.from_json(json_data['gel_bombs']),
            normal_hyper_mode=FlyingPirateHyperModeData.from_json(json_data['normal_hyper_mode']),
            hard_hyper_mode=FlyingPirateHyperModeData.from_json(json_data['hard_hyper_mode']),
            elite_hyper_mode=FlyingPirateHyperModeData.from_json(json_data['elite_hyper_mode']),
            armor=FlyingPirateArmorData.from_json(json_data['armor']),
            jet_pack=FlyingPirateJetPackData.from_json(json_data['jet_pack']),
            rag_doll=RagDollData.from_json(json_data['rag_doll']),
            is_gandrayda=json_data['is_gandrayda'],
            unknown_0x516cb29d=json_data['unknown_0x516cb29d'],
            flip_switch_data=FlyingPirateFlipSwitchData.from_json(json_data['flip_switch_data']),
            morph_health_threshold=json_data['morph_health_threshold'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'is_initially_on_ground': self.is_initially_on_ground,
            'unknown_0xf37267ef': self.unknown_0xf37267ef,
            'disable_particle_blaster': self.disable_particle_blaster,
            'disable_weapon_pods': self.disable_weapon_pods,
            'unknown_0x767f168e': self.unknown_0x767f168e,
            'keep_target_time': self.keep_target_time,
            'max_select_target_distance': self.max_select_target_distance,
            'select_target_distance_factor': self.select_target_distance_factor,
            'unknown_0x610c0165': self.unknown_0x610c0165,
            'unknown_0x0d2531e7': self.unknown_0x0d2531e7,
            'land_check_time': self.land_check_time,
            'land_check_chance': self.land_check_chance,
            'flight_check_time': self.flight_check_time,
            'flight_check_chance': self.flight_check_chance,
            'left_weapon_pod_model': self.left_weapon_pod_model,
            'right_weapon_pod_model': self.right_weapon_pod_model,
            'spin_death_flight_speed': self.spin_death_flight_speed,
            'spin_death_turn_speed': self.spin_death_turn_speed,
            'flight_max_speed': self.flight_max_speed,
            'flight_acceleration': self.flight_acceleration,
            'flight_deceleration': self.flight_deceleration,
            'flight_turn_speed': self.flight_turn_speed,
            'flight_hover_height': self.flight_hover_height,
            'unknown_0x7bb971f1': self.unknown_0x7bb971f1,
            'rotate_rolling_duration': self.rotate_rolling_duration,
            'dip_check_time': self.dip_check_time,
            'dip_chance': self.dip_chance,
            'dodge_chance': self.dodge_chance,
            'min_attack_run_time': self.min_attack_run_time,
            'max_attack_run_range': self.max_attack_run_range,
            'attack_run_chance': self.attack_run_chance,
            'warp_jump_damage_threshold': self.warp_jump_damage_threshold,
            'warp_jump_damage_window': self.warp_jump_damage_window,
            'particle_blaster': self.particle_blaster.to_json(),
            'helix_missiles': self.helix_missiles.to_json(),
            'gel_bombs': self.gel_bombs.to_json(),
            'normal_hyper_mode': self.normal_hyper_mode.to_json(),
            'hard_hyper_mode': self.hard_hyper_mode.to_json(),
            'elite_hyper_mode': self.elite_hyper_mode.to_json(),
            'armor': self.armor.to_json(),
            'jet_pack': self.jet_pack.to_json(),
            'rag_doll': self.rag_doll.to_json(),
            'is_gandrayda': self.is_gandrayda,
            'unknown_0x516cb29d': self.unknown_0x516cb29d,
            'flip_switch_data': self.flip_switch_data.to_json(),
            'morph_health_threshold': self.morph_health_threshold,
        }

    def _dependencies_for_left_weapon_pod_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.left_weapon_pod_model)

    def _dependencies_for_right_weapon_pod_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.right_weapon_pod_model)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_left_weapon_pod_model, "left_weapon_pod_model", "AssetId"),
            (self._dependencies_for_right_weapon_pod_model, "right_weapon_pod_model", "AssetId"),
            (self.particle_blaster.dependencies_for, "particle_blaster", "FlyingPirateBlasterData"),
            (self.helix_missiles.dependencies_for, "helix_missiles", "FlyingPirateHelixMissileData"),
            (self.gel_bombs.dependencies_for, "gel_bombs", "SpacePirateWeaponData"),
            (self.armor.dependencies_for, "armor", "FlyingPirateArmorData"),
            (self.jet_pack.dependencies_for, "jet_pack", "FlyingPirateJetPackData"),
            (self.rag_doll.dependencies_for, "rag_doll", "RagDollData"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for FlyingPirateData.{field_name} ({field_type}): {e}"
                )


def _decode_particle_blaster(data: typing.BinaryIO, game: Game, property_size: int) -> FlyingPirateBlasterData:
    return FlyingPirateBlasterData.from_stream(data, game, property_size)


def _decode_helix_missiles(data: typing.BinaryIO, game: Game, property_size: int) -> FlyingPirateHelixMissileData:
    return FlyingPirateHelixMissileData.from_stream(data, game, property_size)


def _decode_gel_bombs(data: typing.BinaryIO, game: Game, property_size: int) -> SpacePirateWeaponData:
    return SpacePirateWeaponData.from_stream(data, game, property_size)


def _decode_normal_hyper_mode(data: typing.BinaryIO, game: Game, property_size: int) -> FlyingPirateHyperModeData:
    return FlyingPirateHyperModeData.from_stream(data, game, property_size)


def _decode_hard_hyper_mode(data: typing.BinaryIO, game: Game, property_size: int) -> FlyingPirateHyperModeData:
    return FlyingPirateHyperModeData.from_stream(data, game, property_size)


def _decode_elite_hyper_mode(data: typing.BinaryIO, game: Game, property_size: int) -> FlyingPirateHyperModeData:
    return FlyingPirateHyperModeData.from_stream(data, game, property_size)


def _decode_armor(data: typing.BinaryIO, game: Game, property_size: int) -> FlyingPirateArmorData:
    return FlyingPirateArmorData.from_stream(data, game, property_size)


def _decode_jet_pack(data: typing.BinaryIO, game: Game, property_size: int) -> FlyingPirateJetPackData:
    return FlyingPirateJetPackData.from_stream(data, game, property_size)


def _decode_rag_doll(data: typing.BinaryIO, game: Game, property_size: int) -> RagDollData:
    return RagDollData.from_stream(data, game, property_size)


def _decode_flip_switch_data(data: typing.BinaryIO, game: Game, property_size: int) -> FlyingPirateFlipSwitchData:
    return FlyingPirateFlipSwitchData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xa8b7379d: ('is_initially_on_ground', structs.decode_BIG_bool_),
    0xf37267ef: ('unknown_0xf37267ef', structs.decode_BIG_bool_),
    0xf56589a6: ('disable_particle_blaster', structs.decode_BIG_bool_),
    0xcdd1db4f: ('disable_weapon_pods', structs.decode_BIG_bool_),
    0x767f168e: ('unknown_0x767f168e', structs.decode_BIG_bool_),
    0x89a5edc8: ('keep_target_time', structs.decode_BIG_f),
    0xd73ec5bc: ('max_select_target_distance', structs.decode_BIG_f),
    0x907f8e96: ('select_target_distance_factor', structs.decode_BIG_f),
    0x610c0165: ('unknown_0x610c0165', structs.decode_BIG_f),
    0x0d2531e7: ('unknown_0x0d2531e7', structs.decode_BIG_f),
    0x7f7f8028: ('land_check_time', structs.decode_BIG_f),
    0xd2046050: ('land_check_chance', structs.decode_BIG_f),
    0x2454fb04: ('flight_check_time', structs.decode_BIG_f),
    0x2ce2f861: ('flight_check_chance', structs.decode_BIG_f),
    0x95c8719d: ('left_weapon_pod_model', structs.decode_BIG_Q),
    0xa0705491: ('right_weapon_pod_model', structs.decode_BIG_Q),
    0x4fa0ea5c: ('spin_death_flight_speed', structs.decode_BIG_f),
    0x0263834d: ('spin_death_turn_speed', structs.decode_BIG_f),
    0xd4dec629: ('flight_max_speed', structs.decode_BIG_f),
    0x7a2bb377: ('flight_acceleration', structs.decode_BIG_f),
    0xdd14361f: ('flight_deceleration', structs.decode_BIG_f),
    0x6c317b96: ('flight_turn_speed', structs.decode_BIG_f),
    0x7e7afdc2: ('flight_hover_height', structs.decode_BIG_f),
    0x7bb971f1: ('unknown_0x7bb971f1', structs.decode_BIG_f),
    0x3aae4e77: ('rotate_rolling_duration', structs.decode_BIG_f),
    0x9e156b9d: ('dip_check_time', structs.decode_BIG_f),
    0x357ed28d: ('dip_chance', structs.decode_BIG_f),
    0x47be3298: ('dodge_chance', structs.decode_BIG_f),
    0xac2b567d: ('min_attack_run_time', structs.decode_BIG_f),
    0x740b661e: ('max_attack_run_range', structs.decode_BIG_f),
    0xc50d5431: ('attack_run_chance', structs.decode_BIG_f),
    0xc02bb7c5: ('warp_jump_damage_threshold', structs.decode_BIG_f),
    0x2b15406d: ('warp_jump_damage_window', structs.decode_BIG_f),
    0x672b454d: ('particle_blaster', _decode_particle_blaster),
    0x92b304ad: ('helix_missiles', _decode_helix_missiles),
    0x2263e77f: ('gel_bombs', _decode_gel_bombs),
    0x3f07905e: ('normal_hyper_mode', _decode_normal_hyper_mode),
    0x097203ab: ('hard_hyper_mode', _decode_hard_hyper_mode),
    0x4123a3b6: ('elite_hyper_mode', _decode_elite_hyper_mode),
    0x70b96a25: ('armor', _decode_armor),
    0xfbaa9f01: ('jet_pack', _decode_jet_pack),
    0xe39738ea: ('rag_doll', _decode_rag_doll),
    0x531a8c85: ('is_gandrayda', structs.decode_BIG_bool_),
    0x516cb29d: ('unknown_0x516cb29d', structs.decode_BIG_bool_),
    0xf82f61c9: ('flip_switch_data', _decode_flip_switch_data),
    0x97f7a52d: ('morph_health_threshold', structs.decode_BIG_f),
}
