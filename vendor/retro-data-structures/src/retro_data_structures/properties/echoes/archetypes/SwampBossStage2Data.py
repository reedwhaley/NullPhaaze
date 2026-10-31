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
from retro_data_structures.properties.echoes.archetypes.AudioPlaybackParms import AudioPlaybackParms
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.MissileRepellerData import MissileRepellerData
from retro_data_structures.properties.echoes.archetypes.ShockWaveInfo import ShockWaveInfo
from retro_data_structures.properties.echoes.archetypes.SwampBossStage2Phase import SwampBossStage2Phase
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SwampBossStage2DataJson(typing_extensions.TypedDict):
        hover_speed: float
        wing_growth_lf: int
        wing_growth_lb: int
        wing_growth_rf: int
        wing_growth_rb: int
        wing_growth_health: float
        light_flyer1: json_util.JsonObject
        dark_flyer1: json_util.JsonObject
        light_flyer2: json_util.JsonObject
        dark_flyer2: json_util.JsonObject
        stun_time: float
        unknown_0x96ce7897: int
        spit_projectile: int
        spit_damage: json_util.JsonObject
        spit_visor_effect: int
        sound_spit_visor: int
        spit_projectile_radius: float
        swoop_damage: json_util.JsonObject
        swoop_push: float
        swoop_damage_time: float
        splash: int
        unknown_0x7fc50ac2: float
        unknown_0x13448a4a: float
        unknown_0xf55924da: float
        unknown_0x83bc1de7: float
        unknown_0x5a844633: float
        unknown_0x78e22d1b: float
        unknown_0x9e116385: float
        radar_range: float
        radar_range_half_height: float
        splash_shock_wave: json_util.JsonObject
        splash_shock_wave_max_time: float
        splash_shock_wave_knock_back_decay_rate: float
        scan_info_light: int
        scan_info_dark: int
        bubble_telegraph_effect: int
        wing_damage_effect: int
        missile_repeller: json_util.JsonObject
        blow_effect: int
        blow_damage: json_util.JsonObject
        blow_telegraph_push: float
        blow_push: float
        break_stun_damage: float
        stunned_sound: json_util.JsonObject
        audio_playback_parms_0x427a116a: json_util.JsonObject
        audio_playback_parms_0xc05d5c7a: json_util.JsonObject
        audio_playback_parms_0x2b3c923a: json_util.JsonObject
        children_alive_time: float
        flinch_sound: json_util.JsonObject
        flinch_sound_chance: float
        stunned_flinch_sound: json_util.JsonObject
        stunned_reel_sound: json_util.JsonObject
        stunned_flinch_sound_damage_threshold: float
        damaged_wing_growth_sound: json_util.JsonObject
        destroyed_wing_growth_sound: json_util.JsonObject
    

@dataclasses.dataclass()
class SwampBossStage2Data(BaseProperty):
    hover_speed: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x845ef489, original_name='HoverSpeed'
        ),
    })
    wing_growth_lf: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x11a273cb, original_name='WingGrowthLF'
        ),
    })
    wing_growth_lb: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x8a3331dd, original_name='WingGrowthLB'
        ),
    })
    wing_growth_rf: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x26439458, original_name='WingGrowthRF'
        ),
    })
    wing_growth_rb: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xbdd2d64e, original_name='WingGrowthRB'
        ),
    })
    wing_growth_health: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcabe6b96, original_name='WingGrowthHealth'
        ),
    })
    light_flyer1: SwampBossStage2Phase = dataclasses.field(default_factory=SwampBossStage2Phase, metadata={
        'reflection': FieldReflection[SwampBossStage2Phase](
            SwampBossStage2Phase, id=0x7fa9256a, original_name='LightFlyer1', from_json=SwampBossStage2Phase.from_json, to_json=SwampBossStage2Phase.to_json
        ),
    })
    dark_flyer1: SwampBossStage2Phase = dataclasses.field(default_factory=SwampBossStage2Phase, metadata={
        'reflection': FieldReflection[SwampBossStage2Phase](
            SwampBossStage2Phase, id=0x8b884b8e, original_name='DarkFlyer1', from_json=SwampBossStage2Phase.from_json, to_json=SwampBossStage2Phase.to_json
        ),
    })
    light_flyer2: SwampBossStage2Phase = dataclasses.field(default_factory=SwampBossStage2Phase, metadata={
        'reflection': FieldReflection[SwampBossStage2Phase](
            SwampBossStage2Phase, id=0x04b7a789, original_name='LightFlyer2', from_json=SwampBossStage2Phase.from_json, to_json=SwampBossStage2Phase.to_json
        ),
    })
    dark_flyer2: SwampBossStage2Phase = dataclasses.field(default_factory=SwampBossStage2Phase, metadata={
        'reflection': FieldReflection[SwampBossStage2Phase](
            SwampBossStage2Phase, id=0xf096c96d, original_name='DarkFlyer2', from_json=SwampBossStage2Phase.from_json, to_json=SwampBossStage2Phase.to_json
        ),
    })
    stun_time: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7e192395, original_name='StunTime'
        ),
    })
    unknown_0x96ce7897: int = dataclasses.field(default=2, metadata={
        'reflection': FieldReflection[int](
            int, id=0x96ce7897, original_name='Unknown'
        ),
    })
    spit_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xcfe37ebf, original_name='SpitProjectile'
        ),
    })
    spit_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xda3c9b32, original_name='SpitDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    spit_visor_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x008becab, original_name='SpitVisorEffect'
        ),
    })
    sound_spit_visor: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xf3af8417, original_name='Sound_SpitVisor'
        ),
    })
    spit_projectile_radius: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdadc5bc9, original_name='SpitProjectileRadius'
        ),
    })
    swoop_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x294e9516, original_name='SwoopDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    swoop_push: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7d483636, original_name='SwoopPush'
        ),
    })
    swoop_damage_time: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7b61a42b, original_name='SwoopDamageTime'
        ),
    })
    splash: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd8d148fb, original_name='Splash'
        ),
    })
    unknown_0x7fc50ac2: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7fc50ac2, original_name='Unknown'
        ),
    })
    unknown_0x13448a4a: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x13448a4a, original_name='Unknown'
        ),
    })
    unknown_0xf55924da: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf55924da, original_name='Unknown'
        ),
    })
    unknown_0x83bc1de7: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x83bc1de7, original_name='Unknown'
        ),
    })
    unknown_0x5a844633: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5a844633, original_name='Unknown'
        ),
    })
    unknown_0x78e22d1b: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x78e22d1b, original_name='Unknown'
        ),
    })
    unknown_0x9e116385: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9e116385, original_name='Unknown'
        ),
    })
    radar_range: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xee258868, original_name='RadarRange'
        ),
    })
    radar_range_half_height: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfe97e835, original_name='RadarRangeHalfHeight'
        ),
    })
    splash_shock_wave: ShockWaveInfo = dataclasses.field(default_factory=ShockWaveInfo, metadata={
        'reflection': FieldReflection[ShockWaveInfo](
            ShockWaveInfo, id=0x6c0f7aa3, original_name='SplashShockWave', from_json=ShockWaveInfo.from_json, to_json=ShockWaveInfo.to_json
        ),
    })
    splash_shock_wave_max_time: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9807497c, original_name='SplashShockWaveMaxTime'
        ),
    })
    splash_shock_wave_knock_back_decay_rate: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe57ca27c, original_name='SplashShockWaveKnockBackDecayRate'
        ),
    })
    scan_info_light: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SCAN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa3e1608c, original_name='ScanInfoLight'
        ),
    })
    scan_info_dark: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SCAN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa21792bf, original_name='ScanInfoDark'
        ),
    })
    bubble_telegraph_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x515268e5, original_name='BubbleTelegraphEffect'
        ),
    })
    wing_damage_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb1b55340, original_name='WingDamageEffect'
        ),
    })
    missile_repeller: MissileRepellerData = dataclasses.field(default_factory=MissileRepellerData, metadata={
        'reflection': FieldReflection[MissileRepellerData](
            MissileRepellerData, id=0x9347820e, original_name='MissileRepeller', from_json=MissileRepellerData.from_json, to_json=MissileRepellerData.to_json
        ),
    })
    blow_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb7dc6c65, original_name='BlowEffect'
        ),
    })
    blow_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xf1f0c73d, original_name='BlowDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    blow_telegraph_push: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6d89649b, original_name='BlowTelegraphPush'
        ),
    })
    blow_push: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x77f97080, original_name='BlowPush'
        ),
    })
    break_stun_damage: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6d67c284, original_name='BreakStunDamage'
        ),
    })
    stunned_sound: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x87b30e02, original_name='StunnedSound', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    audio_playback_parms_0x427a116a: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x427a116a, original_name='AudioPlaybackParms', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    audio_playback_parms_0xc05d5c7a: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xc05d5c7a, original_name='AudioPlaybackParms', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    audio_playback_parms_0x2b3c923a: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x2b3c923a, original_name='AudioPlaybackParms', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    children_alive_time: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8fe0bf01, original_name='ChildrenAliveTime'
        ),
    })
    flinch_sound: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x23087520, original_name='FlinchSound', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    flinch_sound_chance: float = dataclasses.field(default=0.800000011920929, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa3131519, original_name='FlinchSoundChance'
        ),
    })
    stunned_flinch_sound: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xb53087cc, original_name='StunnedFlinchSound', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    stunned_reel_sound: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x878a6522, original_name='StunnedReelSound', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    stunned_flinch_sound_damage_threshold: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x19849710, original_name='StunnedFlinchSoundDamageThreshold'
        ),
    })
    damaged_wing_growth_sound: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x692fa63c, original_name='DamagedWingGrowthSound', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    destroyed_wing_growth_sound: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xbe3d39aa, original_name='DestroyedWingGrowthSound', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
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
        if property_count != 55:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x845ef489
        hover_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x11a273cb
        wing_growth_lf = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8a3331dd
        wing_growth_lb = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x26439458
        wing_growth_rf = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbdd2d64e
        wing_growth_rb = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcabe6b96
        wing_growth_health = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7fa9256a
        light_flyer1 = SwampBossStage2Phase.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8b884b8e
        dark_flyer1 = SwampBossStage2Phase.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x04b7a789
        light_flyer2 = SwampBossStage2Phase.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf096c96d
        dark_flyer2 = SwampBossStage2Phase.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e192395
        stun_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x96ce7897
        unknown_0x96ce7897 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcfe37ebf
        spit_projectile = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xda3c9b32
        spit_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x008becab
        spit_visor_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf3af8417
        sound_spit_visor = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdadc5bc9
        spit_projectile_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x294e9516
        swoop_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 0.5})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7d483636
        swoop_push = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7b61a42b
        swoop_damage_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd8d148fb
        splash = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7fc50ac2
        unknown_0x7fc50ac2 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13448a4a
        unknown_0x13448a4a = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf55924da
        unknown_0xf55924da = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x83bc1de7
        unknown_0x83bc1de7 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5a844633
        unknown_0x5a844633 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78e22d1b
        unknown_0x78e22d1b = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9e116385
        unknown_0x9e116385 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xee258868
        radar_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfe97e835
        radar_range_half_height = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6c0f7aa3
        splash_shock_wave = ShockWaveInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9807497c
        splash_shock_wave_max_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe57ca27c
        splash_shock_wave_knock_back_decay_rate = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa3e1608c
        scan_info_light = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa21792bf
        scan_info_dark = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x515268e5
        bubble_telegraph_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb1b55340
        wing_damage_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9347820e
        missile_repeller = MissileRepellerData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb7dc6c65
        blow_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf1f0c73d
        blow_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 0.5})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6d89649b
        blow_telegraph_push = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77f97080
        blow_push = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6d67c284
        break_stun_damage = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x87b30e02
        stunned_sound = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x427a116a
        audio_playback_parms_0x427a116a = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc05d5c7a
        audio_playback_parms_0xc05d5c7a = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2b3c923a
        audio_playback_parms_0x2b3c923a = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8fe0bf01
        children_alive_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23087520
        flinch_sound = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa3131519
        flinch_sound_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb53087cc
        stunned_flinch_sound = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x878a6522
        stunned_reel_sound = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19849710
        stunned_flinch_sound_damage_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x692fa63c
        damaged_wing_growth_sound = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbe3d39aa
        destroyed_wing_growth_sound = AudioPlaybackParms.from_stream(data, game, property_size)
    
        return cls(hover_speed, wing_growth_lf, wing_growth_lb, wing_growth_rf, wing_growth_rb, wing_growth_health, light_flyer1, dark_flyer1, light_flyer2, dark_flyer2, stun_time, unknown_0x96ce7897, spit_projectile, spit_damage, spit_visor_effect, sound_spit_visor, spit_projectile_radius, swoop_damage, swoop_push, swoop_damage_time, splash, unknown_0x7fc50ac2, unknown_0x13448a4a, unknown_0xf55924da, unknown_0x83bc1de7, unknown_0x5a844633, unknown_0x78e22d1b, unknown_0x9e116385, radar_range, radar_range_half_height, splash_shock_wave, splash_shock_wave_max_time, splash_shock_wave_knock_back_decay_rate, scan_info_light, scan_info_dark, bubble_telegraph_effect, wing_damage_effect, missile_repeller, blow_effect, blow_damage, blow_telegraph_push, blow_push, break_stun_damage, stunned_sound, audio_playback_parms_0x427a116a, audio_playback_parms_0xc05d5c7a, audio_playback_parms_0x2b3c923a, children_alive_time, flinch_sound, flinch_sound_chance, stunned_flinch_sound, stunned_reel_sound, stunned_flinch_sound_damage_threshold, damaged_wing_growth_sound, destroyed_wing_growth_sound)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x007')  # 55 properties

        data.write(b'\x84^\xf4\x89')  # 0x845ef489
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hover_speed))

        data.write(b'\x11\xa2s\xcb')  # 0x11a273cb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.wing_growth_lf))

        data.write(b'\x8a31\xdd')  # 0x8a3331dd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.wing_growth_lb))

        data.write(b'&C\x94X')  # 0x26439458
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.wing_growth_rf))

        data.write(b'\xbd\xd2\xd6N')  # 0xbdd2d64e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.wing_growth_rb))

        data.write(b'\xca\xbek\x96')  # 0xcabe6b96
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.wing_growth_health))

        data.write(b'\x7f\xa9%j')  # 0x7fa9256a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.light_flyer1.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8b\x88K\x8e')  # 0x8b884b8e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.dark_flyer1.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x04\xb7\xa7\x89')  # 0x4b7a789
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.light_flyer2.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf0\x96\xc9m')  # 0xf096c96d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.dark_flyer2.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'~\x19#\x95')  # 0x7e192395
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stun_time))

        data.write(b'\x96\xcex\x97')  # 0x96ce7897
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x96ce7897))

        data.write(b'\xcf\xe3~\xbf')  # 0xcfe37ebf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.spit_projectile))

        data.write(b'\xda<\x9b2')  # 0xda3c9b32
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.spit_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x00\x8b\xec\xab')  # 0x8becab
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.spit_visor_effect))

        data.write(b'\xf3\xaf\x84\x17')  # 0xf3af8417
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_spit_visor))

        data.write(b'\xda\xdc[\xc9')  # 0xdadc5bc9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.spit_projectile_radius))

        data.write(b')N\x95\x16')  # 0x294e9516
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.swoop_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 0.5})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'}H66')  # 0x7d483636
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.swoop_push))

        data.write(b'{a\xa4+')  # 0x7b61a42b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.swoop_damage_time))

        data.write(b'\xd8\xd1H\xfb')  # 0xd8d148fb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.splash))

        data.write(b'\x7f\xc5\n\xc2')  # 0x7fc50ac2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7fc50ac2))

        data.write(b'\x13D\x8aJ')  # 0x13448a4a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x13448a4a))

        data.write(b'\xf5Y$\xda')  # 0xf55924da
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf55924da))

        data.write(b'\x83\xbc\x1d\xe7')  # 0x83bc1de7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x83bc1de7))

        data.write(b'Z\x84F3')  # 0x5a844633
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5a844633))

        data.write(b'x\xe2-\x1b')  # 0x78e22d1b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x78e22d1b))

        data.write(b'\x9e\x11c\x85')  # 0x9e116385
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9e116385))

        data.write(b'\xee%\x88h')  # 0xee258868
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.radar_range))

        data.write(b'\xfe\x97\xe85')  # 0xfe97e835
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.radar_range_half_height))

        data.write(b'l\x0fz\xa3')  # 0x6c0f7aa3
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.splash_shock_wave.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x98\x07I|')  # 0x9807497c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.splash_shock_wave_max_time))

        data.write(b'\xe5|\xa2|')  # 0xe57ca27c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.splash_shock_wave_knock_back_decay_rate))

        data.write(b'\xa3\xe1`\x8c')  # 0xa3e1608c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.scan_info_light))

        data.write(b'\xa2\x17\x92\xbf')  # 0xa21792bf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.scan_info_dark))

        data.write(b'QRh\xe5')  # 0x515268e5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.bubble_telegraph_effect))

        data.write(b'\xb1\xb5S@')  # 0xb1b55340
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.wing_damage_effect))

        data.write(b'\x93G\x82\x0e')  # 0x9347820e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.missile_repeller.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb7\xdcle')  # 0xb7dc6c65
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.blow_effect))

        data.write(b'\xf1\xf0\xc7=')  # 0xf1f0c73d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.blow_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 0.5})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'm\x89d\x9b')  # 0x6d89649b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.blow_telegraph_push))

        data.write(b'w\xf9p\x80')  # 0x77f97080
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.blow_push))

        data.write(b'mg\xc2\x84')  # 0x6d67c284
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.break_stun_damage))

        data.write(b'\x87\xb3\x0e\x02')  # 0x87b30e02
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stunned_sound.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'Bz\x11j')  # 0x427a116a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.audio_playback_parms_0x427a116a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc0]\\z')  # 0xc05d5c7a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.audio_playback_parms_0xc05d5c7a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'+<\x92:')  # 0x2b3c923a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.audio_playback_parms_0x2b3c923a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8f\xe0\xbf\x01')  # 0x8fe0bf01
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.children_alive_time))

        data.write(b'#\x08u ')  # 0x23087520
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.flinch_sound.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa3\x13\x15\x19')  # 0xa3131519
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flinch_sound_chance))

        data.write(b'\xb50\x87\xcc')  # 0xb53087cc
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stunned_flinch_sound.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x87\x8ae"')  # 0x878a6522
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stunned_reel_sound.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x19\x84\x97\x10')  # 0x19849710
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stunned_flinch_sound_damage_threshold))

        data.write(b'i/\xa6<')  # 0x692fa63c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damaged_wing_growth_sound.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbe=9\xaa')  # 0xbe3d39aa
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.destroyed_wing_growth_sound.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SwampBossStage2DataJson", data)
        return cls(
            hover_speed=json_data['hover_speed'],
            wing_growth_lf=json_data['wing_growth_lf'],
            wing_growth_lb=json_data['wing_growth_lb'],
            wing_growth_rf=json_data['wing_growth_rf'],
            wing_growth_rb=json_data['wing_growth_rb'],
            wing_growth_health=json_data['wing_growth_health'],
            light_flyer1=SwampBossStage2Phase.from_json(json_data['light_flyer1']),
            dark_flyer1=SwampBossStage2Phase.from_json(json_data['dark_flyer1']),
            light_flyer2=SwampBossStage2Phase.from_json(json_data['light_flyer2']),
            dark_flyer2=SwampBossStage2Phase.from_json(json_data['dark_flyer2']),
            stun_time=json_data['stun_time'],
            unknown_0x96ce7897=json_data['unknown_0x96ce7897'],
            spit_projectile=json_data['spit_projectile'],
            spit_damage=DamageInfo.from_json(json_data['spit_damage']),
            spit_visor_effect=json_data['spit_visor_effect'],
            sound_spit_visor=json_data['sound_spit_visor'],
            spit_projectile_radius=json_data['spit_projectile_radius'],
            swoop_damage=DamageInfo.from_json(json_data['swoop_damage']),
            swoop_push=json_data['swoop_push'],
            swoop_damage_time=json_data['swoop_damage_time'],
            splash=json_data['splash'],
            unknown_0x7fc50ac2=json_data['unknown_0x7fc50ac2'],
            unknown_0x13448a4a=json_data['unknown_0x13448a4a'],
            unknown_0xf55924da=json_data['unknown_0xf55924da'],
            unknown_0x83bc1de7=json_data['unknown_0x83bc1de7'],
            unknown_0x5a844633=json_data['unknown_0x5a844633'],
            unknown_0x78e22d1b=json_data['unknown_0x78e22d1b'],
            unknown_0x9e116385=json_data['unknown_0x9e116385'],
            radar_range=json_data['radar_range'],
            radar_range_half_height=json_data['radar_range_half_height'],
            splash_shock_wave=ShockWaveInfo.from_json(json_data['splash_shock_wave']),
            splash_shock_wave_max_time=json_data['splash_shock_wave_max_time'],
            splash_shock_wave_knock_back_decay_rate=json_data['splash_shock_wave_knock_back_decay_rate'],
            scan_info_light=json_data['scan_info_light'],
            scan_info_dark=json_data['scan_info_dark'],
            bubble_telegraph_effect=json_data['bubble_telegraph_effect'],
            wing_damage_effect=json_data['wing_damage_effect'],
            missile_repeller=MissileRepellerData.from_json(json_data['missile_repeller']),
            blow_effect=json_data['blow_effect'],
            blow_damage=DamageInfo.from_json(json_data['blow_damage']),
            blow_telegraph_push=json_data['blow_telegraph_push'],
            blow_push=json_data['blow_push'],
            break_stun_damage=json_data['break_stun_damage'],
            stunned_sound=AudioPlaybackParms.from_json(json_data['stunned_sound']),
            audio_playback_parms_0x427a116a=AudioPlaybackParms.from_json(json_data['audio_playback_parms_0x427a116a']),
            audio_playback_parms_0xc05d5c7a=AudioPlaybackParms.from_json(json_data['audio_playback_parms_0xc05d5c7a']),
            audio_playback_parms_0x2b3c923a=AudioPlaybackParms.from_json(json_data['audio_playback_parms_0x2b3c923a']),
            children_alive_time=json_data['children_alive_time'],
            flinch_sound=AudioPlaybackParms.from_json(json_data['flinch_sound']),
            flinch_sound_chance=json_data['flinch_sound_chance'],
            stunned_flinch_sound=AudioPlaybackParms.from_json(json_data['stunned_flinch_sound']),
            stunned_reel_sound=AudioPlaybackParms.from_json(json_data['stunned_reel_sound']),
            stunned_flinch_sound_damage_threshold=json_data['stunned_flinch_sound_damage_threshold'],
            damaged_wing_growth_sound=AudioPlaybackParms.from_json(json_data['damaged_wing_growth_sound']),
            destroyed_wing_growth_sound=AudioPlaybackParms.from_json(json_data['destroyed_wing_growth_sound']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'hover_speed': self.hover_speed,
            'wing_growth_lf': self.wing_growth_lf,
            'wing_growth_lb': self.wing_growth_lb,
            'wing_growth_rf': self.wing_growth_rf,
            'wing_growth_rb': self.wing_growth_rb,
            'wing_growth_health': self.wing_growth_health,
            'light_flyer1': self.light_flyer1.to_json(),
            'dark_flyer1': self.dark_flyer1.to_json(),
            'light_flyer2': self.light_flyer2.to_json(),
            'dark_flyer2': self.dark_flyer2.to_json(),
            'stun_time': self.stun_time,
            'unknown_0x96ce7897': self.unknown_0x96ce7897,
            'spit_projectile': self.spit_projectile,
            'spit_damage': self.spit_damage.to_json(),
            'spit_visor_effect': self.spit_visor_effect,
            'sound_spit_visor': self.sound_spit_visor,
            'spit_projectile_radius': self.spit_projectile_radius,
            'swoop_damage': self.swoop_damage.to_json(),
            'swoop_push': self.swoop_push,
            'swoop_damage_time': self.swoop_damage_time,
            'splash': self.splash,
            'unknown_0x7fc50ac2': self.unknown_0x7fc50ac2,
            'unknown_0x13448a4a': self.unknown_0x13448a4a,
            'unknown_0xf55924da': self.unknown_0xf55924da,
            'unknown_0x83bc1de7': self.unknown_0x83bc1de7,
            'unknown_0x5a844633': self.unknown_0x5a844633,
            'unknown_0x78e22d1b': self.unknown_0x78e22d1b,
            'unknown_0x9e116385': self.unknown_0x9e116385,
            'radar_range': self.radar_range,
            'radar_range_half_height': self.radar_range_half_height,
            'splash_shock_wave': self.splash_shock_wave.to_json(),
            'splash_shock_wave_max_time': self.splash_shock_wave_max_time,
            'splash_shock_wave_knock_back_decay_rate': self.splash_shock_wave_knock_back_decay_rate,
            'scan_info_light': self.scan_info_light,
            'scan_info_dark': self.scan_info_dark,
            'bubble_telegraph_effect': self.bubble_telegraph_effect,
            'wing_damage_effect': self.wing_damage_effect,
            'missile_repeller': self.missile_repeller.to_json(),
            'blow_effect': self.blow_effect,
            'blow_damage': self.blow_damage.to_json(),
            'blow_telegraph_push': self.blow_telegraph_push,
            'blow_push': self.blow_push,
            'break_stun_damage': self.break_stun_damage,
            'stunned_sound': self.stunned_sound.to_json(),
            'audio_playback_parms_0x427a116a': self.audio_playback_parms_0x427a116a.to_json(),
            'audio_playback_parms_0xc05d5c7a': self.audio_playback_parms_0xc05d5c7a.to_json(),
            'audio_playback_parms_0x2b3c923a': self.audio_playback_parms_0x2b3c923a.to_json(),
            'children_alive_time': self.children_alive_time,
            'flinch_sound': self.flinch_sound.to_json(),
            'flinch_sound_chance': self.flinch_sound_chance,
            'stunned_flinch_sound': self.stunned_flinch_sound.to_json(),
            'stunned_reel_sound': self.stunned_reel_sound.to_json(),
            'stunned_flinch_sound_damage_threshold': self.stunned_flinch_sound_damage_threshold,
            'damaged_wing_growth_sound': self.damaged_wing_growth_sound.to_json(),
            'destroyed_wing_growth_sound': self.destroyed_wing_growth_sound.to_json(),
        }

    def _dependencies_for_wing_growth_lf(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wing_growth_lf)

    def _dependencies_for_wing_growth_lb(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wing_growth_lb)

    def _dependencies_for_wing_growth_rf(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wing_growth_rf)

    def _dependencies_for_wing_growth_rb(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wing_growth_rb)

    def _dependencies_for_spit_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.spit_projectile)

    def _dependencies_for_spit_visor_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.spit_visor_effect)

    def _dependencies_for_sound_spit_visor(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_spit_visor)

    def _dependencies_for_splash(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.splash)

    def _dependencies_for_scan_info_light(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scan_info_light)

    def _dependencies_for_scan_info_dark(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scan_info_dark)

    def _dependencies_for_bubble_telegraph_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.bubble_telegraph_effect)

    def _dependencies_for_wing_damage_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wing_damage_effect)

    def _dependencies_for_blow_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.blow_effect)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_wing_growth_lf, "wing_growth_lf", "AssetId"),
            (self._dependencies_for_wing_growth_lb, "wing_growth_lb", "AssetId"),
            (self._dependencies_for_wing_growth_rf, "wing_growth_rf", "AssetId"),
            (self._dependencies_for_wing_growth_rb, "wing_growth_rb", "AssetId"),
            (self._dependencies_for_spit_projectile, "spit_projectile", "AssetId"),
            (self._dependencies_for_spit_visor_effect, "spit_visor_effect", "AssetId"),
            (self._dependencies_for_sound_spit_visor, "sound_spit_visor", "int"),
            (self._dependencies_for_splash, "splash", "AssetId"),
            (self.splash_shock_wave.dependencies_for, "splash_shock_wave", "ShockWaveInfo"),
            (self._dependencies_for_scan_info_light, "scan_info_light", "AssetId"),
            (self._dependencies_for_scan_info_dark, "scan_info_dark", "AssetId"),
            (self._dependencies_for_bubble_telegraph_effect, "bubble_telegraph_effect", "AssetId"),
            (self._dependencies_for_wing_damage_effect, "wing_damage_effect", "AssetId"),
            (self.missile_repeller.dependencies_for, "missile_repeller", "MissileRepellerData"),
            (self._dependencies_for_blow_effect, "blow_effect", "AssetId"),
            (self.stunned_sound.dependencies_for, "stunned_sound", "AudioPlaybackParms"),
            (self.audio_playback_parms_0x427a116a.dependencies_for, "audio_playback_parms_0x427a116a", "AudioPlaybackParms"),
            (self.audio_playback_parms_0xc05d5c7a.dependencies_for, "audio_playback_parms_0xc05d5c7a", "AudioPlaybackParms"),
            (self.audio_playback_parms_0x2b3c923a.dependencies_for, "audio_playback_parms_0x2b3c923a", "AudioPlaybackParms"),
            (self.flinch_sound.dependencies_for, "flinch_sound", "AudioPlaybackParms"),
            (self.stunned_flinch_sound.dependencies_for, "stunned_flinch_sound", "AudioPlaybackParms"),
            (self.stunned_reel_sound.dependencies_for, "stunned_reel_sound", "AudioPlaybackParms"),
            (self.damaged_wing_growth_sound.dependencies_for, "damaged_wing_growth_sound", "AudioPlaybackParms"),
            (self.destroyed_wing_growth_sound.dependencies_for, "destroyed_wing_growth_sound", "AudioPlaybackParms"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for SwampBossStage2Data.{field_name} ({field_type}): {e}"
                )


def _decode_light_flyer1(data: typing.BinaryIO, game: Game, property_size: int) -> SwampBossStage2Phase:
    return SwampBossStage2Phase.from_stream(data, game, property_size)


def _decode_dark_flyer1(data: typing.BinaryIO, game: Game, property_size: int) -> SwampBossStage2Phase:
    return SwampBossStage2Phase.from_stream(data, game, property_size)


def _decode_light_flyer2(data: typing.BinaryIO, game: Game, property_size: int) -> SwampBossStage2Phase:
    return SwampBossStage2Phase.from_stream(data, game, property_size)


def _decode_dark_flyer2(data: typing.BinaryIO, game: Game, property_size: int) -> SwampBossStage2Phase:
    return SwampBossStage2Phase.from_stream(data, game, property_size)


def _decode_spit_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0})


def _decode_swoop_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 0.5})


def _decode_splash_shock_wave(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


def _decode_missile_repeller(data: typing.BinaryIO, game: Game, property_size: int) -> MissileRepellerData:
    return MissileRepellerData.from_stream(data, game, property_size)


def _decode_blow_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 0.5})


def _decode_stunned_sound(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms_0x427a116a(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms_0xc05d5c7a(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_audio_playback_parms_0x2b3c923a(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_flinch_sound(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_stunned_flinch_sound(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_stunned_reel_sound(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_damaged_wing_growth_sound(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_destroyed_wing_growth_sound(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x845ef489: ('hover_speed', structs.decode_BIG_f),
    0x11a273cb: ('wing_growth_lf', structs.decode_BIG_L),
    0x8a3331dd: ('wing_growth_lb', structs.decode_BIG_L),
    0x26439458: ('wing_growth_rf', structs.decode_BIG_L),
    0xbdd2d64e: ('wing_growth_rb', structs.decode_BIG_L),
    0xcabe6b96: ('wing_growth_health', structs.decode_BIG_f),
    0x7fa9256a: ('light_flyer1', _decode_light_flyer1),
    0x8b884b8e: ('dark_flyer1', _decode_dark_flyer1),
    0x04b7a789: ('light_flyer2', _decode_light_flyer2),
    0xf096c96d: ('dark_flyer2', _decode_dark_flyer2),
    0x7e192395: ('stun_time', structs.decode_BIG_f),
    0x96ce7897: ('unknown_0x96ce7897', structs.decode_BIG_l),
    0xcfe37ebf: ('spit_projectile', structs.decode_BIG_L),
    0xda3c9b32: ('spit_damage', _decode_spit_damage),
    0x008becab: ('spit_visor_effect', structs.decode_BIG_L),
    0xf3af8417: ('sound_spit_visor', structs.decode_BIG_l),
    0xdadc5bc9: ('spit_projectile_radius', structs.decode_BIG_f),
    0x294e9516: ('swoop_damage', _decode_swoop_damage),
    0x7d483636: ('swoop_push', structs.decode_BIG_f),
    0x7b61a42b: ('swoop_damage_time', structs.decode_BIG_f),
    0xd8d148fb: ('splash', structs.decode_BIG_L),
    0x7fc50ac2: ('unknown_0x7fc50ac2', structs.decode_BIG_f),
    0x13448a4a: ('unknown_0x13448a4a', structs.decode_BIG_f),
    0xf55924da: ('unknown_0xf55924da', structs.decode_BIG_f),
    0x83bc1de7: ('unknown_0x83bc1de7', structs.decode_BIG_f),
    0x5a844633: ('unknown_0x5a844633', structs.decode_BIG_f),
    0x78e22d1b: ('unknown_0x78e22d1b', structs.decode_BIG_f),
    0x9e116385: ('unknown_0x9e116385', structs.decode_BIG_f),
    0xee258868: ('radar_range', structs.decode_BIG_f),
    0xfe97e835: ('radar_range_half_height', structs.decode_BIG_f),
    0x6c0f7aa3: ('splash_shock_wave', _decode_splash_shock_wave),
    0x9807497c: ('splash_shock_wave_max_time', structs.decode_BIG_f),
    0xe57ca27c: ('splash_shock_wave_knock_back_decay_rate', structs.decode_BIG_f),
    0xa3e1608c: ('scan_info_light', structs.decode_BIG_L),
    0xa21792bf: ('scan_info_dark', structs.decode_BIG_L),
    0x515268e5: ('bubble_telegraph_effect', structs.decode_BIG_L),
    0xb1b55340: ('wing_damage_effect', structs.decode_BIG_L),
    0x9347820e: ('missile_repeller', _decode_missile_repeller),
    0xb7dc6c65: ('blow_effect', structs.decode_BIG_L),
    0xf1f0c73d: ('blow_damage', _decode_blow_damage),
    0x6d89649b: ('blow_telegraph_push', structs.decode_BIG_f),
    0x77f97080: ('blow_push', structs.decode_BIG_f),
    0x6d67c284: ('break_stun_damage', structs.decode_BIG_f),
    0x87b30e02: ('stunned_sound', _decode_stunned_sound),
    0x427a116a: ('audio_playback_parms_0x427a116a', _decode_audio_playback_parms_0x427a116a),
    0xc05d5c7a: ('audio_playback_parms_0xc05d5c7a', _decode_audio_playback_parms_0xc05d5c7a),
    0x2b3c923a: ('audio_playback_parms_0x2b3c923a', _decode_audio_playback_parms_0x2b3c923a),
    0x8fe0bf01: ('children_alive_time', structs.decode_BIG_f),
    0x23087520: ('flinch_sound', _decode_flinch_sound),
    0xa3131519: ('flinch_sound_chance', structs.decode_BIG_f),
    0xb53087cc: ('stunned_flinch_sound', _decode_stunned_flinch_sound),
    0x878a6522: ('stunned_reel_sound', _decode_stunned_reel_sound),
    0x19849710: ('stunned_flinch_sound_damage_threshold', structs.decode_BIG_f),
    0x692fa63c: ('damaged_wing_growth_sound', _decode_damaged_wing_growth_sound),
    0xbe3d39aa: ('destroyed_wing_growth_sound', _decode_destroyed_wing_growth_sound),
}
