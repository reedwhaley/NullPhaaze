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
from retro_data_structures.properties.corruption.archetypes.LaunchProjectileData import LaunchProjectileData
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class BlinkWolfDataJson(typing_extensions.TypedDict):
        unknown_0x2b3109a6: bool
        start_invisible: bool
        max_hop_range: float
        turn_prediction: float
        spit_prediction: float
        approach_dist: float
        jump_approach_dist: float
        jump_apex: float
        min_spit_range: float
        max_spit_range: float
        min_spits: int
        spit_starting: json_util.JsonObject
        spit_full_speed: json_util.JsonObject
        spit_slowing: json_util.JsonObject
        spit_stopping: json_util.JsonObject
        sound_gel_stream: int
        sound_teleport_end: int
        max_head_rotation: float
        head_rotation_speed: float
        max_head_rotation_running: float
        unknown_0x190d9fc8: float
        unknown_0xfcae3411: float
        unknown_0x7ecb92ca: float
        burn_damage: float
        burn_damage_duration: float
        shockwave_range: float
        shockwave_damage: json_util.JsonObject
        shockwave_intensity: float
        unknown_0xb39833c0: float
        min_hud_disable_time: float
        max_hud_disable_time: float
        blink_out: int
        blink_bubble: int
        min_bubble_time: float
        max_bubble_time: float
        min_blink_range: float
        warp_increase_start_time: float
        warp_increase_intensity: float
        warp_intensity_max: float
        warp_decrease_start_time: float
        warp_decrease_intensity: float
        warp_duration_max: float
        frozen_gib_time: float
        avoidance_range: float
        hearing_radius: float
        recheck_path_time: float
        recheck_path_distance: float
        pain_threshold: float
        pain_threshold_mod: float
        pain_threshold2: float
        pain_threshold_mod2: float
        player_scan_delay: float
        unknown_0x108e8ed8: float
        max_fall_time: float
        unknown_0xc34bffca: float
        initial_turn_threshold: float
        path_find_turn_threshold: float
        initial_turn_threshold_running: float
        path_find_turn_threshold_running: float
    

@dataclasses.dataclass()
class BlinkWolfData(BaseProperty):
    unknown_0x2b3109a6: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x2b3109a6, original_name='Unknown'
        ),
    })
    start_invisible: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xbb5c37e0, original_name='StartInvisible'
        ),
    })
    max_hop_range: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7fdee42c, original_name='MaxHopRange'
        ),
    })
    turn_prediction: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x983954ae, original_name='TurnPrediction'
        ),
    })
    spit_prediction: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x86b2b7d7, original_name='SpitPrediction'
        ),
    })
    approach_dist: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa1d7e06b, original_name='ApproachDist'
        ),
    })
    jump_approach_dist: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6d6c84cb, original_name='JumpApproachDist'
        ),
    })
    jump_apex: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf2782501, original_name='JumpApex'
        ),
    })
    min_spit_range: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0236c750, original_name='MinSpitRange'
        ),
    })
    max_spit_range: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x17bd13a2, original_name='MaxSpitRange'
        ),
    })
    min_spits: int = dataclasses.field(default=5, metadata={
        'reflection': FieldReflection[int](
            int, id=0xb6055f35, original_name='MinSpits'
        ),
    })
    spit_starting: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0x6dac116a, original_name='SpitStarting', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    spit_full_speed: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0x9aab30f1, original_name='SpitFullSpeed', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    spit_slowing: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0x76b1b8e0, original_name='SpitSlowing', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    spit_stopping: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0xfe3b5965, original_name='SpitStopping', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    sound_gel_stream: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x95eaaacb, original_name='Sound_GelStream'
        ),
    })
    sound_teleport_end: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd4c88dd1, original_name='Sound_TeleportEnd'
        ),
    })
    max_head_rotation: float = dataclasses.field(default=70.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe68cebb0, original_name='MaxHeadRotation'
        ),
    })
    head_rotation_speed: float = dataclasses.field(default=180.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8b7fcf8c, original_name='HeadRotationSpeed'
        ),
    })
    max_head_rotation_running: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0f5a3164, original_name='MaxHeadRotationRunning'
        ),
    })
    unknown_0x190d9fc8: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x190d9fc8, original_name='Unknown'
        ),
    })
    unknown_0xfcae3411: float = dataclasses.field(default=24.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfcae3411, original_name='Unknown'
        ),
    })
    unknown_0x7ecb92ca: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7ecb92ca, original_name='Unknown'
        ),
    })
    burn_damage: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcf201bfa, original_name='BurnDamage'
        ),
    })
    burn_damage_duration: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcf495aab, original_name='BurnDamageDuration'
        ),
    })
    shockwave_range: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8d518fd5, original_name='ShockwaveRange'
        ),
    })
    shockwave_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x0f2fa713, original_name='ShockwaveDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    shockwave_intensity: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa42dbd9e, original_name='ShockwaveIntensity'
        ),
    })
    unknown_0xb39833c0: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb39833c0, original_name='Unknown'
        ),
    })
    min_hud_disable_time: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x96bd6426, original_name='MinHudDisableTime'
        ),
    })
    max_hud_disable_time: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd7aa5ba0, original_name='MaxHudDisableTime'
        ),
    })
    blink_out: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2050f248, original_name='BlinkOut'
        ),
    })
    blink_bubble: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x9cb2109a, original_name='BlinkBubble'
        ),
    })
    min_bubble_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4ce0d7e5, original_name='MinBubbleTime'
        ),
    })
    max_bubble_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1f46cf01, original_name='MaxBubbleTime'
        ),
    })
    min_blink_range: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0fc0b9e3, original_name='MinBlinkRange'
        ),
    })
    warp_increase_start_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8e5f1638, original_name='WarpIncreaseStartTime'
        ),
    })
    warp_increase_intensity: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf7ba9e21, original_name='WarpIncreaseIntensity'
        ),
    })
    warp_intensity_max: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1e501419, original_name='WarpIntensityMax'
        ),
    })
    warp_decrease_start_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x22794c6d, original_name='WarpDecreaseStartTime'
        ),
    })
    warp_decrease_intensity: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5b9cc474, original_name='WarpDecreaseIntensity'
        ),
    })
    warp_duration_max: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x08f1e9d3, original_name='WarpDurationMax'
        ),
    })
    frozen_gib_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x51bb4b6f, original_name='FrozenGibTime'
        ),
    })
    avoidance_range: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x50a9bd0d, original_name='AvoidanceRange'
        ),
    })
    hearing_radius: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xed69488f, original_name='HearingRadius'
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
    pain_threshold: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x13a15b89, original_name='PainThreshold'
        ),
    })
    pain_threshold_mod: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa6c1631d, original_name='PainThresholdMod'
        ),
    })
    pain_threshold2: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x312e194a, original_name='PainThreshold2'
        ),
    })
    pain_threshold_mod2: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc6f92e2f, original_name='PainThresholdMod2'
        ),
    })
    player_scan_delay: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1f844b33, original_name='PlayerScanDelay'
        ),
    })
    unknown_0x108e8ed8: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x108e8ed8, original_name='Unknown'
        ),
    })
    max_fall_time: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x74cc0ccf, original_name='MaxFallTime'
        ),
    })
    unknown_0xc34bffca: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc34bffca, original_name='Unknown'
        ),
    })
    initial_turn_threshold: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf5aa6363, original_name='InitialTurnThreshold'
        ),
    })
    path_find_turn_threshold: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd40c2b10, original_name='PathFindTurnThreshold'
        ),
    })
    initial_turn_threshold_running: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6bbf9cdc, original_name='InitialTurnThresholdRunning'
        ),
    })
    path_find_turn_threshold_running: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb2dd7c06, original_name='PathFindTurnThresholdRunning'
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
        assert property_id == 0x2b3109a6
        unknown_0x2b3109a6 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbb5c37e0
        start_invisible = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7fdee42c
        max_hop_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x983954ae
        turn_prediction = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x86b2b7d7
        spit_prediction = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa1d7e06b
        approach_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6d6c84cb
        jump_approach_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf2782501
        jump_apex = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0236c750
        min_spit_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x17bd13a2
        max_spit_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb6055f35
        min_spits = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6dac116a
        spit_starting = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9aab30f1
        spit_full_speed = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76b1b8e0
        spit_slowing = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfe3b5965
        spit_stopping = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95eaaacb
        sound_gel_stream = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd4c88dd1
        sound_teleport_end = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe68cebb0
        max_head_rotation = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8b7fcf8c
        head_rotation_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0f5a3164
        max_head_rotation_running = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x190d9fc8
        unknown_0x190d9fc8 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfcae3411
        unknown_0xfcae3411 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7ecb92ca
        unknown_0x7ecb92ca = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcf201bfa
        burn_damage = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcf495aab
        burn_damage_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8d518fd5
        shockwave_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0f2fa713
        shockwave_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa42dbd9e
        shockwave_intensity = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb39833c0
        unknown_0xb39833c0 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x96bd6426
        min_hud_disable_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd7aa5ba0
        max_hud_disable_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2050f248
        blink_out = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9cb2109a
        blink_bubble = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4ce0d7e5
        min_bubble_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1f46cf01
        max_bubble_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0fc0b9e3
        min_blink_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8e5f1638
        warp_increase_start_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf7ba9e21
        warp_increase_intensity = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1e501419
        warp_intensity_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x22794c6d
        warp_decrease_start_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5b9cc474
        warp_decrease_intensity = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08f1e9d3
        warp_duration_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x51bb4b6f
        frozen_gib_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50a9bd0d
        avoidance_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed69488f
        hearing_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9aa90b6b
        recheck_path_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7626ec89
        recheck_path_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13a15b89
        pain_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa6c1631d
        pain_threshold_mod = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x312e194a
        pain_threshold2 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc6f92e2f
        pain_threshold_mod2 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1f844b33
        player_scan_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x108e8ed8
        unknown_0x108e8ed8 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x74cc0ccf
        max_fall_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc34bffca
        unknown_0xc34bffca = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf5aa6363
        initial_turn_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd40c2b10
        path_find_turn_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6bbf9cdc
        initial_turn_threshold_running = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb2dd7c06
        path_find_turn_threshold_running = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(unknown_0x2b3109a6, start_invisible, max_hop_range, turn_prediction, spit_prediction, approach_dist, jump_approach_dist, jump_apex, min_spit_range, max_spit_range, min_spits, spit_starting, spit_full_speed, spit_slowing, spit_stopping, sound_gel_stream, sound_teleport_end, max_head_rotation, head_rotation_speed, max_head_rotation_running, unknown_0x190d9fc8, unknown_0xfcae3411, unknown_0x7ecb92ca, burn_damage, burn_damage_duration, shockwave_range, shockwave_damage, shockwave_intensity, unknown_0xb39833c0, min_hud_disable_time, max_hud_disable_time, blink_out, blink_bubble, min_bubble_time, max_bubble_time, min_blink_range, warp_increase_start_time, warp_increase_intensity, warp_intensity_max, warp_decrease_start_time, warp_decrease_intensity, warp_duration_max, frozen_gib_time, avoidance_range, hearing_radius, recheck_path_time, recheck_path_distance, pain_threshold, pain_threshold_mod, pain_threshold2, pain_threshold_mod2, player_scan_delay, unknown_0x108e8ed8, max_fall_time, unknown_0xc34bffca, initial_turn_threshold, path_find_turn_threshold, initial_turn_threshold_running, path_find_turn_threshold_running)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00;')  # 59 properties

        data.write(b'+1\t\xa6')  # 0x2b3109a6
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x2b3109a6))

        data.write(b'\xbb\\7\xe0')  # 0xbb5c37e0
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.start_invisible))

        data.write(b'\x7f\xde\xe4,')  # 0x7fdee42c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_hop_range))

        data.write(b'\x989T\xae')  # 0x983954ae
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.turn_prediction))

        data.write(b'\x86\xb2\xb7\xd7')  # 0x86b2b7d7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.spit_prediction))

        data.write(b'\xa1\xd7\xe0k')  # 0xa1d7e06b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.approach_dist))

        data.write(b'ml\x84\xcb')  # 0x6d6c84cb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_approach_dist))

        data.write(b'\xf2x%\x01')  # 0xf2782501
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_apex))

        data.write(b'\x026\xc7P')  # 0x236c750
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_spit_range))

        data.write(b'\x17\xbd\x13\xa2')  # 0x17bd13a2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_spit_range))

        data.write(b'\xb6\x05_5')  # 0xb6055f35
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.min_spits))

        data.write(b'm\xac\x11j')  # 0x6dac116a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.spit_starting.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9a\xab0\xf1')  # 0x9aab30f1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.spit_full_speed.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'v\xb1\xb8\xe0')  # 0x76b1b8e0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.spit_slowing.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfe;Ye')  # 0xfe3b5965
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.spit_stopping.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x95\xea\xaa\xcb')  # 0x95eaaacb
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_gel_stream))

        data.write(b'\xd4\xc8\x8d\xd1')  # 0xd4c88dd1
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_teleport_end))

        data.write(b'\xe6\x8c\xeb\xb0')  # 0xe68cebb0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_head_rotation))

        data.write(b'\x8b\x7f\xcf\x8c')  # 0x8b7fcf8c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.head_rotation_speed))

        data.write(b'\x0fZ1d')  # 0xf5a3164
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_head_rotation_running))

        data.write(b'\x19\r\x9f\xc8')  # 0x190d9fc8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x190d9fc8))

        data.write(b'\xfc\xae4\x11')  # 0xfcae3411
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfcae3411))

        data.write(b'~\xcb\x92\xca')  # 0x7ecb92ca
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7ecb92ca))

        data.write(b'\xcf \x1b\xfa')  # 0xcf201bfa
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.burn_damage))

        data.write(b'\xcfIZ\xab')  # 0xcf495aab
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.burn_damage_duration))

        data.write(b'\x8dQ\x8f\xd5')  # 0x8d518fd5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.shockwave_range))

        data.write(b'\x0f/\xa7\x13')  # 0xf2fa713
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shockwave_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa4-\xbd\x9e')  # 0xa42dbd9e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.shockwave_intensity))

        data.write(b'\xb3\x983\xc0')  # 0xb39833c0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb39833c0))

        data.write(b'\x96\xbdd&')  # 0x96bd6426
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_hud_disable_time))

        data.write(b'\xd7\xaa[\xa0')  # 0xd7aa5ba0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_hud_disable_time))

        data.write(b' P\xf2H')  # 0x2050f248
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.blink_out))

        data.write(b'\x9c\xb2\x10\x9a')  # 0x9cb2109a
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.blink_bubble))

        data.write(b'L\xe0\xd7\xe5')  # 0x4ce0d7e5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_bubble_time))

        data.write(b'\x1fF\xcf\x01')  # 0x1f46cf01
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_bubble_time))

        data.write(b'\x0f\xc0\xb9\xe3')  # 0xfc0b9e3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_blink_range))

        data.write(b'\x8e_\x168')  # 0x8e5f1638
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.warp_increase_start_time))

        data.write(b'\xf7\xba\x9e!')  # 0xf7ba9e21
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.warp_increase_intensity))

        data.write(b'\x1eP\x14\x19')  # 0x1e501419
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.warp_intensity_max))

        data.write(b'"yLm')  # 0x22794c6d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.warp_decrease_start_time))

        data.write(b'[\x9c\xc4t')  # 0x5b9cc474
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.warp_decrease_intensity))

        data.write(b'\x08\xf1\xe9\xd3')  # 0x8f1e9d3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.warp_duration_max))

        data.write(b'Q\xbbKo')  # 0x51bb4b6f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.frozen_gib_time))

        data.write(b'P\xa9\xbd\r')  # 0x50a9bd0d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.avoidance_range))

        data.write(b'\xediH\x8f')  # 0xed69488f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hearing_radius))

        data.write(b'\x9a\xa9\x0bk')  # 0x9aa90b6b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.recheck_path_time))

        data.write(b'v&\xec\x89')  # 0x7626ec89
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.recheck_path_distance))

        data.write(b'\x13\xa1[\x89')  # 0x13a15b89
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.pain_threshold))

        data.write(b'\xa6\xc1c\x1d')  # 0xa6c1631d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.pain_threshold_mod))

        data.write(b'1.\x19J')  # 0x312e194a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.pain_threshold2))

        data.write(b'\xc6\xf9./')  # 0xc6f92e2f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.pain_threshold_mod2))

        data.write(b'\x1f\x84K3')  # 0x1f844b33
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.player_scan_delay))

        data.write(b'\x10\x8e\x8e\xd8')  # 0x108e8ed8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x108e8ed8))

        data.write(b't\xcc\x0c\xcf')  # 0x74cc0ccf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_fall_time))

        data.write(b'\xc3K\xff\xca')  # 0xc34bffca
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc34bffca))

        data.write(b'\xf5\xaacc')  # 0xf5aa6363
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.initial_turn_threshold))

        data.write(b'\xd4\x0c+\x10')  # 0xd40c2b10
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.path_find_turn_threshold))

        data.write(b'k\xbf\x9c\xdc')  # 0x6bbf9cdc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.initial_turn_threshold_running))

        data.write(b'\xb2\xdd|\x06')  # 0xb2dd7c06
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.path_find_turn_threshold_running))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("BlinkWolfDataJson", data)
        return cls(
            unknown_0x2b3109a6=json_data['unknown_0x2b3109a6'],
            start_invisible=json_data['start_invisible'],
            max_hop_range=json_data['max_hop_range'],
            turn_prediction=json_data['turn_prediction'],
            spit_prediction=json_data['spit_prediction'],
            approach_dist=json_data['approach_dist'],
            jump_approach_dist=json_data['jump_approach_dist'],
            jump_apex=json_data['jump_apex'],
            min_spit_range=json_data['min_spit_range'],
            max_spit_range=json_data['max_spit_range'],
            min_spits=json_data['min_spits'],
            spit_starting=LaunchProjectileData.from_json(json_data['spit_starting']),
            spit_full_speed=LaunchProjectileData.from_json(json_data['spit_full_speed']),
            spit_slowing=LaunchProjectileData.from_json(json_data['spit_slowing']),
            spit_stopping=LaunchProjectileData.from_json(json_data['spit_stopping']),
            sound_gel_stream=json_data['sound_gel_stream'],
            sound_teleport_end=json_data['sound_teleport_end'],
            max_head_rotation=json_data['max_head_rotation'],
            head_rotation_speed=json_data['head_rotation_speed'],
            max_head_rotation_running=json_data['max_head_rotation_running'],
            unknown_0x190d9fc8=json_data['unknown_0x190d9fc8'],
            unknown_0xfcae3411=json_data['unknown_0xfcae3411'],
            unknown_0x7ecb92ca=json_data['unknown_0x7ecb92ca'],
            burn_damage=json_data['burn_damage'],
            burn_damage_duration=json_data['burn_damage_duration'],
            shockwave_range=json_data['shockwave_range'],
            shockwave_damage=DamageInfo.from_json(json_data['shockwave_damage']),
            shockwave_intensity=json_data['shockwave_intensity'],
            unknown_0xb39833c0=json_data['unknown_0xb39833c0'],
            min_hud_disable_time=json_data['min_hud_disable_time'],
            max_hud_disable_time=json_data['max_hud_disable_time'],
            blink_out=json_data['blink_out'],
            blink_bubble=json_data['blink_bubble'],
            min_bubble_time=json_data['min_bubble_time'],
            max_bubble_time=json_data['max_bubble_time'],
            min_blink_range=json_data['min_blink_range'],
            warp_increase_start_time=json_data['warp_increase_start_time'],
            warp_increase_intensity=json_data['warp_increase_intensity'],
            warp_intensity_max=json_data['warp_intensity_max'],
            warp_decrease_start_time=json_data['warp_decrease_start_time'],
            warp_decrease_intensity=json_data['warp_decrease_intensity'],
            warp_duration_max=json_data['warp_duration_max'],
            frozen_gib_time=json_data['frozen_gib_time'],
            avoidance_range=json_data['avoidance_range'],
            hearing_radius=json_data['hearing_radius'],
            recheck_path_time=json_data['recheck_path_time'],
            recheck_path_distance=json_data['recheck_path_distance'],
            pain_threshold=json_data['pain_threshold'],
            pain_threshold_mod=json_data['pain_threshold_mod'],
            pain_threshold2=json_data['pain_threshold2'],
            pain_threshold_mod2=json_data['pain_threshold_mod2'],
            player_scan_delay=json_data['player_scan_delay'],
            unknown_0x108e8ed8=json_data['unknown_0x108e8ed8'],
            max_fall_time=json_data['max_fall_time'],
            unknown_0xc34bffca=json_data['unknown_0xc34bffca'],
            initial_turn_threshold=json_data['initial_turn_threshold'],
            path_find_turn_threshold=json_data['path_find_turn_threshold'],
            initial_turn_threshold_running=json_data['initial_turn_threshold_running'],
            path_find_turn_threshold_running=json_data['path_find_turn_threshold_running'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'unknown_0x2b3109a6': self.unknown_0x2b3109a6,
            'start_invisible': self.start_invisible,
            'max_hop_range': self.max_hop_range,
            'turn_prediction': self.turn_prediction,
            'spit_prediction': self.spit_prediction,
            'approach_dist': self.approach_dist,
            'jump_approach_dist': self.jump_approach_dist,
            'jump_apex': self.jump_apex,
            'min_spit_range': self.min_spit_range,
            'max_spit_range': self.max_spit_range,
            'min_spits': self.min_spits,
            'spit_starting': self.spit_starting.to_json(),
            'spit_full_speed': self.spit_full_speed.to_json(),
            'spit_slowing': self.spit_slowing.to_json(),
            'spit_stopping': self.spit_stopping.to_json(),
            'sound_gel_stream': self.sound_gel_stream,
            'sound_teleport_end': self.sound_teleport_end,
            'max_head_rotation': self.max_head_rotation,
            'head_rotation_speed': self.head_rotation_speed,
            'max_head_rotation_running': self.max_head_rotation_running,
            'unknown_0x190d9fc8': self.unknown_0x190d9fc8,
            'unknown_0xfcae3411': self.unknown_0xfcae3411,
            'unknown_0x7ecb92ca': self.unknown_0x7ecb92ca,
            'burn_damage': self.burn_damage,
            'burn_damage_duration': self.burn_damage_duration,
            'shockwave_range': self.shockwave_range,
            'shockwave_damage': self.shockwave_damage.to_json(),
            'shockwave_intensity': self.shockwave_intensity,
            'unknown_0xb39833c0': self.unknown_0xb39833c0,
            'min_hud_disable_time': self.min_hud_disable_time,
            'max_hud_disable_time': self.max_hud_disable_time,
            'blink_out': self.blink_out,
            'blink_bubble': self.blink_bubble,
            'min_bubble_time': self.min_bubble_time,
            'max_bubble_time': self.max_bubble_time,
            'min_blink_range': self.min_blink_range,
            'warp_increase_start_time': self.warp_increase_start_time,
            'warp_increase_intensity': self.warp_increase_intensity,
            'warp_intensity_max': self.warp_intensity_max,
            'warp_decrease_start_time': self.warp_decrease_start_time,
            'warp_decrease_intensity': self.warp_decrease_intensity,
            'warp_duration_max': self.warp_duration_max,
            'frozen_gib_time': self.frozen_gib_time,
            'avoidance_range': self.avoidance_range,
            'hearing_radius': self.hearing_radius,
            'recheck_path_time': self.recheck_path_time,
            'recheck_path_distance': self.recheck_path_distance,
            'pain_threshold': self.pain_threshold,
            'pain_threshold_mod': self.pain_threshold_mod,
            'pain_threshold2': self.pain_threshold2,
            'pain_threshold_mod2': self.pain_threshold_mod2,
            'player_scan_delay': self.player_scan_delay,
            'unknown_0x108e8ed8': self.unknown_0x108e8ed8,
            'max_fall_time': self.max_fall_time,
            'unknown_0xc34bffca': self.unknown_0xc34bffca,
            'initial_turn_threshold': self.initial_turn_threshold,
            'path_find_turn_threshold': self.path_find_turn_threshold,
            'initial_turn_threshold_running': self.initial_turn_threshold_running,
            'path_find_turn_threshold_running': self.path_find_turn_threshold_running,
        }

    def _dependencies_for_sound_gel_stream(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_gel_stream)

    def _dependencies_for_sound_teleport_end(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_teleport_end)

    def _dependencies_for_blink_out(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.blink_out)

    def _dependencies_for_blink_bubble(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.blink_bubble)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.spit_starting.dependencies_for, "spit_starting", "LaunchProjectileData"),
            (self.spit_full_speed.dependencies_for, "spit_full_speed", "LaunchProjectileData"),
            (self.spit_slowing.dependencies_for, "spit_slowing", "LaunchProjectileData"),
            (self.spit_stopping.dependencies_for, "spit_stopping", "LaunchProjectileData"),
            (self._dependencies_for_sound_gel_stream, "sound_gel_stream", "AssetId"),
            (self._dependencies_for_sound_teleport_end, "sound_teleport_end", "AssetId"),
            (self._dependencies_for_blink_out, "blink_out", "AssetId"),
            (self._dependencies_for_blink_bubble, "blink_bubble", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for BlinkWolfData.{field_name} ({field_type}): {e}"
                )


def _decode_spit_starting(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_spit_full_speed(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_spit_slowing(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_spit_stopping(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_shockwave_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x2b3109a6: ('unknown_0x2b3109a6', structs.decode_BIG_bool_),
    0xbb5c37e0: ('start_invisible', structs.decode_BIG_bool_),
    0x7fdee42c: ('max_hop_range', structs.decode_BIG_f),
    0x983954ae: ('turn_prediction', structs.decode_BIG_f),
    0x86b2b7d7: ('spit_prediction', structs.decode_BIG_f),
    0xa1d7e06b: ('approach_dist', structs.decode_BIG_f),
    0x6d6c84cb: ('jump_approach_dist', structs.decode_BIG_f),
    0xf2782501: ('jump_apex', structs.decode_BIG_f),
    0x0236c750: ('min_spit_range', structs.decode_BIG_f),
    0x17bd13a2: ('max_spit_range', structs.decode_BIG_f),
    0xb6055f35: ('min_spits', structs.decode_BIG_l),
    0x6dac116a: ('spit_starting', _decode_spit_starting),
    0x9aab30f1: ('spit_full_speed', _decode_spit_full_speed),
    0x76b1b8e0: ('spit_slowing', _decode_spit_slowing),
    0xfe3b5965: ('spit_stopping', _decode_spit_stopping),
    0x95eaaacb: ('sound_gel_stream', structs.decode_BIG_Q),
    0xd4c88dd1: ('sound_teleport_end', structs.decode_BIG_Q),
    0xe68cebb0: ('max_head_rotation', structs.decode_BIG_f),
    0x8b7fcf8c: ('head_rotation_speed', structs.decode_BIG_f),
    0x0f5a3164: ('max_head_rotation_running', structs.decode_BIG_f),
    0x190d9fc8: ('unknown_0x190d9fc8', structs.decode_BIG_f),
    0xfcae3411: ('unknown_0xfcae3411', structs.decode_BIG_f),
    0x7ecb92ca: ('unknown_0x7ecb92ca', structs.decode_BIG_f),
    0xcf201bfa: ('burn_damage', structs.decode_BIG_f),
    0xcf495aab: ('burn_damage_duration', structs.decode_BIG_f),
    0x8d518fd5: ('shockwave_range', structs.decode_BIG_f),
    0x0f2fa713: ('shockwave_damage', _decode_shockwave_damage),
    0xa42dbd9e: ('shockwave_intensity', structs.decode_BIG_f),
    0xb39833c0: ('unknown_0xb39833c0', structs.decode_BIG_f),
    0x96bd6426: ('min_hud_disable_time', structs.decode_BIG_f),
    0xd7aa5ba0: ('max_hud_disable_time', structs.decode_BIG_f),
    0x2050f248: ('blink_out', structs.decode_BIG_Q),
    0x9cb2109a: ('blink_bubble', structs.decode_BIG_Q),
    0x4ce0d7e5: ('min_bubble_time', structs.decode_BIG_f),
    0x1f46cf01: ('max_bubble_time', structs.decode_BIG_f),
    0x0fc0b9e3: ('min_blink_range', structs.decode_BIG_f),
    0x8e5f1638: ('warp_increase_start_time', structs.decode_BIG_f),
    0xf7ba9e21: ('warp_increase_intensity', structs.decode_BIG_f),
    0x1e501419: ('warp_intensity_max', structs.decode_BIG_f),
    0x22794c6d: ('warp_decrease_start_time', structs.decode_BIG_f),
    0x5b9cc474: ('warp_decrease_intensity', structs.decode_BIG_f),
    0x08f1e9d3: ('warp_duration_max', structs.decode_BIG_f),
    0x51bb4b6f: ('frozen_gib_time', structs.decode_BIG_f),
    0x50a9bd0d: ('avoidance_range', structs.decode_BIG_f),
    0xed69488f: ('hearing_radius', structs.decode_BIG_f),
    0x9aa90b6b: ('recheck_path_time', structs.decode_BIG_f),
    0x7626ec89: ('recheck_path_distance', structs.decode_BIG_f),
    0x13a15b89: ('pain_threshold', structs.decode_BIG_f),
    0xa6c1631d: ('pain_threshold_mod', structs.decode_BIG_f),
    0x312e194a: ('pain_threshold2', structs.decode_BIG_f),
    0xc6f92e2f: ('pain_threshold_mod2', structs.decode_BIG_f),
    0x1f844b33: ('player_scan_delay', structs.decode_BIG_f),
    0x108e8ed8: ('unknown_0x108e8ed8', structs.decode_BIG_f),
    0x74cc0ccf: ('max_fall_time', structs.decode_BIG_f),
    0xc34bffca: ('unknown_0xc34bffca', structs.decode_BIG_f),
    0xf5aa6363: ('initial_turn_threshold', structs.decode_BIG_f),
    0xd40c2b10: ('path_find_turn_threshold', structs.decode_BIG_f),
    0x6bbf9cdc: ('initial_turn_threshold_running', structs.decode_BIG_f),
    0xb2dd7c06: ('path_find_turn_threshold_running', structs.decode_BIG_f),
}
