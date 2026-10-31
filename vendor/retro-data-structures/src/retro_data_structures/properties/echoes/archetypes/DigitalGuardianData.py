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
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.EchoParameters import EchoParameters
from retro_data_structures.properties.echoes.archetypes.ShockWaveInfo import ShockWaveInfo
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class DigitalGuardianDataJson(typing_extensions.TypedDict):
        scannable_info_crippled: int
        near_leg_stab_range: float
        far_leg_stab_range: float
        min_leg_stab_attack_time: float
        leg_stab_damage: json_util.JsonObject
        toe_target_hp: float
        toe_target_model: int
        toe_target_explosion: int
        sound_toe_target: json_util.JsonObject
        sound_toe_target_attack: json_util.JsonObject
        sound_toe_target_explosion: json_util.JsonObject
        sound_toe_target_hit: json_util.JsonObject
        sound_shock_wave: json_util.JsonObject
        shock_wave_info: json_util.JsonObject
        vortex_attack_duration: float
        vortex_attraction_force: float
        max_vortex_attraction_distance: float
        vortex_linear_velocity: float
        vortex_linear_acceleration: float
        vortex_damage: json_util.JsonObject
        unknown_0xfb5263e8: int
        unknown_0x6aaf33e3: int
        unknown_0x4f5d725c: float
        sound_vortex_flash: json_util.JsonObject
        leg_model: int
        shin_armor: int
        knee_armor_hp: float
        sound_knee_armor_hit: json_util.JsonObject
        sound_knee_vulnerable: json_util.JsonObject
        knee_armor: int
        knee_echo_parameters: json_util.JsonObject
        min_protect_knee_time: float
        unknown_0x6a754ebd: float
        jump_timer: float
        four_knees_time_scale: float
        three_knees_time_scale: float
        two_knees_time_scale: float
        one_knee_time_scale: float
        transmission_beacon: int
        transmission_beacon_fx: int
        transmission_beacon_echo_parameters: json_util.JsonObject
        sound_transmission_beacon: json_util.JsonObject
        sound_beacon_extract: json_util.JsonObject
        sound_beacon_retract: json_util.JsonObject
        transmission_beacon_hp: float
        transmission_beacon_explosion: int
        transmission_beacon_echo_hit: int
        sound_beacon_explode: json_util.JsonObject
        sound_beacon_hit: json_util.JsonObject
        knee_vulnerability: json_util.JsonObject
        vortex_vulnerability: json_util.JsonObject
        toe_target_vulnerability: json_util.JsonObject
    

@dataclasses.dataclass()
class DigitalGuardianData(BaseProperty):
    scannable_info_crippled: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SCAN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2aa63fc4, original_name='ScannableInfoCrippled'
        ),
    })
    near_leg_stab_range: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0faf6a8e, original_name='NearLegStabRange'
        ),
    })
    far_leg_stab_range: float = dataclasses.field(default=17.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd3056808, original_name='FarLegStabRange'
        ),
    })
    min_leg_stab_attack_time: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x304b47ee, original_name='MinLegStabAttackTime'
        ),
    })
    leg_stab_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xefacfa50, original_name='LegStabDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    toe_target_hp: float = dataclasses.field(default=75.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb4561f28, original_name='ToeTargetHP'
        ),
    })
    toe_target_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xbb06dd83, original_name='ToeTargetModel'
        ),
    })
    toe_target_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x783635a6, original_name='ToeTargetExplosion'
        ),
    })
    sound_toe_target: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x13845a66, original_name='Sound_ToeTarget', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_toe_target_attack: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xa305dcba, original_name='Sound_ToeTargetAttack', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_toe_target_explosion: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xc6ec1630, original_name='Sound_ToeTargetExplosion', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_toe_target_hit: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x98419eac, original_name='Sound_ToeTargetHit', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_shock_wave: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x4691c9ab, original_name='Sound_ShockWave', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    shock_wave_info: ShockWaveInfo = dataclasses.field(default_factory=ShockWaveInfo, metadata={
        'reflection': FieldReflection[ShockWaveInfo](
            ShockWaveInfo, id=0x8f4787cb, original_name='ShockWaveInfo', from_json=ShockWaveInfo.from_json, to_json=ShockWaveInfo.to_json
        ),
    })
    vortex_attack_duration: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x76527e01, original_name='VortexAttackDuration'
        ),
    })
    vortex_attraction_force: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd210dfdb, original_name='VortexAttractionForce'
        ),
    })
    max_vortex_attraction_distance: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x348bff02, original_name='MaxVortexAttractionDistance'
        ),
    })
    vortex_linear_velocity: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x84fef16f, original_name='VortexLinearVelocity'
        ),
    })
    vortex_linear_acceleration: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x93a74a46, original_name='VortexLinearAcceleration'
        ),
    })
    vortex_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x5ca612aa, original_name='VortexDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    unknown_0xfb5263e8: int = dataclasses.field(default=-5734, metadata={
        'reflection': FieldReflection[int](
            int, id=0xfb5263e8, original_name='Unknown'
        ),
    })
    unknown_0x6aaf33e3: int = dataclasses.field(default=8191, metadata={
        'reflection': FieldReflection[int](
            int, id=0x6aaf33e3, original_name='Unknown'
        ),
    })
    unknown_0x4f5d725c: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4f5d725c, original_name='Unknown'
        ),
    })
    sound_vortex_flash: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x7bfab420, original_name='Sound_VortexFlash', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    leg_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc0a86488, original_name='LegModel'
        ),
    })
    shin_armor: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x8ddd85ca, original_name='ShinArmor'
        ),
    })
    knee_armor_hp: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe3dd61e6, original_name='KneeArmorHP'
        ),
    })
    sound_knee_armor_hit: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x91d2a042, original_name='Sound_KneeArmorHit', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_knee_vulnerable: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x9386d22b, original_name='Sound_KneeVulnerable', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    knee_armor: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5ef8b288, original_name='KneeArmor'
        ),
    })
    knee_echo_parameters: EchoParameters = dataclasses.field(default_factory=EchoParameters, metadata={
        'reflection': FieldReflection[EchoParameters](
            EchoParameters, id=0x7b5b7312, original_name='KneeEchoParameters', from_json=EchoParameters.from_json, to_json=EchoParameters.to_json
        ),
    })
    min_protect_knee_time: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa324e26c, original_name='MinProtectKneeTime'
        ),
    })
    unknown_0x6a754ebd: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6a754ebd, original_name='Unknown'
        ),
    })
    jump_timer: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc9fc9977, original_name='JumpTimer'
        ),
    })
    four_knees_time_scale: float = dataclasses.field(default=0.699999988079071, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8106cda9, original_name='FourKneesTimeScale'
        ),
    })
    three_knees_time_scale: float = dataclasses.field(default=0.699999988079071, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9e1b8105, original_name='ThreeKneesTimeScale'
        ),
    })
    two_knees_time_scale: float = dataclasses.field(default=0.699999988079071, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa08fcc70, original_name='TwoKneesTimeScale'
        ),
    })
    one_knee_time_scale: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3254a16b, original_name='OneKneeTimeScale'
        ),
    })
    transmission_beacon: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5796a143, original_name='TransmissionBeacon'
        ),
    })
    transmission_beacon_fx: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3fa7df1c, original_name='TransmissionBeaconFx'
        ),
    })
    transmission_beacon_echo_parameters: EchoParameters = dataclasses.field(default_factory=EchoParameters, metadata={
        'reflection': FieldReflection[EchoParameters](
            EchoParameters, id=0x021b6f9d, original_name='TransmissionBeaconEchoParameters', from_json=EchoParameters.from_json, to_json=EchoParameters.to_json
        ),
    })
    sound_transmission_beacon: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x55a8011c, original_name='Sound_TransmissionBeacon', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_beacon_extract: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x7ae73fb3, original_name='Sound_BeaconExtract', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_beacon_retract: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xa9e55c8e, original_name='Sound_BeaconRetract', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    transmission_beacon_hp: float = dataclasses.field(default=500.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4f6d27d3, original_name='TransmissionBeaconHP'
        ),
    })
    transmission_beacon_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x71f0c674, original_name='TransmissionBeaconExplosion'
        ),
    })
    transmission_beacon_echo_hit: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc8ec315b, original_name='TransmissionBeaconEchoHit'
        ),
    })
    sound_beacon_explode: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xeed5b990, original_name='Sound_BeaconExplode', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_beacon_hit: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x535f6fec, original_name='Sound_BeaconHit', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    knee_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x6dbad233, original_name='KneeVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    vortex_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xf1259e3a, original_name='VortexVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    toe_target_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xf14f3237, original_name='ToeTargetVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
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
        if property_count != 52:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2aa63fc4
        scannable_info_crippled = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0faf6a8e
        near_leg_stab_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd3056808
        far_leg_stab_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x304b47ee
        min_leg_stab_attack_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xefacfa50
        leg_stab_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 50.0, 'di_knock_back_power': 10.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb4561f28
        toe_target_hp = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbb06dd83
        toe_target_model = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x783635a6
        toe_target_explosion = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13845a66
        sound_toe_target = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa305dcba
        sound_toe_target_attack = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc6ec1630
        sound_toe_target_explosion = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x98419eac
        sound_toe_target_hit = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4691c9ab
        sound_shock_wave = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8f4787cb
        shock_wave_info = ShockWaveInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76527e01
        vortex_attack_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd210dfdb
        vortex_attraction_force = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x348bff02
        max_vortex_attraction_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x84fef16f
        vortex_linear_velocity = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x93a74a46
        vortex_linear_acceleration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5ca612aa
        vortex_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 50.0, 'di_knock_back_power': 10.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfb5263e8
        unknown_0xfb5263e8 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6aaf33e3
        unknown_0x6aaf33e3 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4f5d725c
        unknown_0x4f5d725c = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7bfab420
        sound_vortex_flash = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc0a86488
        leg_model = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8ddd85ca
        shin_armor = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe3dd61e6
        knee_armor_hp = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x91d2a042
        sound_knee_armor_hit = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9386d22b
        sound_knee_vulnerable = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5ef8b288
        knee_armor = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7b5b7312
        knee_echo_parameters = EchoParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa324e26c
        min_protect_knee_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6a754ebd
        unknown_0x6a754ebd = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc9fc9977
        jump_timer = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8106cda9
        four_knees_time_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9e1b8105
        three_knees_time_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa08fcc70
        two_knees_time_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3254a16b
        one_knee_time_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5796a143
        transmission_beacon = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3fa7df1c
        transmission_beacon_fx = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x021b6f9d
        transmission_beacon_echo_parameters = EchoParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x55a8011c
        sound_transmission_beacon = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7ae73fb3
        sound_beacon_extract = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa9e55c8e
        sound_beacon_retract = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4f6d27d3
        transmission_beacon_hp = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71f0c674
        transmission_beacon_explosion = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc8ec315b
        transmission_beacon_echo_hit = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xeed5b990
        sound_beacon_explode = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x535f6fec
        sound_beacon_hit = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6dbad233
        knee_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf1259e3a
        vortex_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf14f3237
        toe_target_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        return cls(scannable_info_crippled, near_leg_stab_range, far_leg_stab_range, min_leg_stab_attack_time, leg_stab_damage, toe_target_hp, toe_target_model, toe_target_explosion, sound_toe_target, sound_toe_target_attack, sound_toe_target_explosion, sound_toe_target_hit, sound_shock_wave, shock_wave_info, vortex_attack_duration, vortex_attraction_force, max_vortex_attraction_distance, vortex_linear_velocity, vortex_linear_acceleration, vortex_damage, unknown_0xfb5263e8, unknown_0x6aaf33e3, unknown_0x4f5d725c, sound_vortex_flash, leg_model, shin_armor, knee_armor_hp, sound_knee_armor_hit, sound_knee_vulnerable, knee_armor, knee_echo_parameters, min_protect_knee_time, unknown_0x6a754ebd, jump_timer, four_knees_time_scale, three_knees_time_scale, two_knees_time_scale, one_knee_time_scale, transmission_beacon, transmission_beacon_fx, transmission_beacon_echo_parameters, sound_transmission_beacon, sound_beacon_extract, sound_beacon_retract, transmission_beacon_hp, transmission_beacon_explosion, transmission_beacon_echo_hit, sound_beacon_explode, sound_beacon_hit, knee_vulnerability, vortex_vulnerability, toe_target_vulnerability)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x004')  # 52 properties

        data.write(b'*\xa6?\xc4')  # 0x2aa63fc4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.scannable_info_crippled))

        data.write(b'\x0f\xafj\x8e')  # 0xfaf6a8e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.near_leg_stab_range))

        data.write(b'\xd3\x05h\x08')  # 0xd3056808
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.far_leg_stab_range))

        data.write(b'0KG\xee')  # 0x304b47ee
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_leg_stab_attack_time))

        data.write(b'\xef\xac\xfaP')  # 0xefacfa50
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.leg_stab_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 50.0, 'di_knock_back_power': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb4V\x1f(')  # 0xb4561f28
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.toe_target_hp))

        data.write(b'\xbb\x06\xdd\x83')  # 0xbb06dd83
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.toe_target_model))

        data.write(b'x65\xa6')  # 0x783635a6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.toe_target_explosion))

        data.write(b'\x13\x84Zf')  # 0x13845a66
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_toe_target.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa3\x05\xdc\xba')  # 0xa305dcba
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_toe_target_attack.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc6\xec\x160')  # 0xc6ec1630
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_toe_target_explosion.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x98A\x9e\xac')  # 0x98419eac
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_toe_target_hit.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'F\x91\xc9\xab')  # 0x4691c9ab
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_shock_wave.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8fG\x87\xcb')  # 0x8f4787cb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shock_wave_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'vR~\x01')  # 0x76527e01
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.vortex_attack_duration))

        data.write(b'\xd2\x10\xdf\xdb')  # 0xd210dfdb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.vortex_attraction_force))

        data.write(b'4\x8b\xff\x02')  # 0x348bff02
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_vortex_attraction_distance))

        data.write(b'\x84\xfe\xf1o')  # 0x84fef16f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.vortex_linear_velocity))

        data.write(b'\x93\xa7JF')  # 0x93a74a46
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.vortex_linear_acceleration))

        data.write(b'\\\xa6\x12\xaa')  # 0x5ca612aa
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.vortex_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 50.0, 'di_knock_back_power': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfbRc\xe8')  # 0xfb5263e8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xfb5263e8))

        data.write(b'j\xaf3\xe3')  # 0x6aaf33e3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x6aaf33e3))

        data.write(b'O]r\\')  # 0x4f5d725c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4f5d725c))

        data.write(b'{\xfa\xb4 ')  # 0x7bfab420
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_vortex_flash.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc0\xa8d\x88')  # 0xc0a86488
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.leg_model))

        data.write(b'\x8d\xdd\x85\xca')  # 0x8ddd85ca
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.shin_armor))

        data.write(b'\xe3\xdda\xe6')  # 0xe3dd61e6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.knee_armor_hp))

        data.write(b'\x91\xd2\xa0B')  # 0x91d2a042
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_knee_armor_hit.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x93\x86\xd2+')  # 0x9386d22b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_knee_vulnerable.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'^\xf8\xb2\x88')  # 0x5ef8b288
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.knee_armor))

        data.write(b'{[s\x12')  # 0x7b5b7312
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.knee_echo_parameters.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa3$\xe2l')  # 0xa324e26c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_protect_knee_time))

        data.write(b'juN\xbd')  # 0x6a754ebd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6a754ebd))

        data.write(b'\xc9\xfc\x99w')  # 0xc9fc9977
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_timer))

        data.write(b'\x81\x06\xcd\xa9')  # 0x8106cda9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.four_knees_time_scale))

        data.write(b'\x9e\x1b\x81\x05')  # 0x9e1b8105
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.three_knees_time_scale))

        data.write(b'\xa0\x8f\xccp')  # 0xa08fcc70
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.two_knees_time_scale))

        data.write(b'2T\xa1k')  # 0x3254a16b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.one_knee_time_scale))

        data.write(b'W\x96\xa1C')  # 0x5796a143
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.transmission_beacon))

        data.write(b'?\xa7\xdf\x1c')  # 0x3fa7df1c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.transmission_beacon_fx))

        data.write(b'\x02\x1bo\x9d')  # 0x21b6f9d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.transmission_beacon_echo_parameters.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'U\xa8\x01\x1c')  # 0x55a8011c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_transmission_beacon.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'z\xe7?\xb3')  # 0x7ae73fb3
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_beacon_extract.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa9\xe5\\\x8e')  # 0xa9e55c8e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_beacon_retract.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"Om'\xd3")  # 0x4f6d27d3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.transmission_beacon_hp))

        data.write(b'q\xf0\xc6t')  # 0x71f0c674
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.transmission_beacon_explosion))

        data.write(b'\xc8\xec1[')  # 0xc8ec315b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.transmission_beacon_echo_hit))

        data.write(b'\xee\xd5\xb9\x90')  # 0xeed5b990
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_beacon_explode.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'S_o\xec')  # 0x535f6fec
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_beacon_hit.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'm\xba\xd23')  # 0x6dbad233
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.knee_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf1%\x9e:')  # 0xf1259e3a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.vortex_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf1O27')  # 0xf14f3237
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.toe_target_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DigitalGuardianDataJson", data)
        return cls(
            scannable_info_crippled=json_data['scannable_info_crippled'],
            near_leg_stab_range=json_data['near_leg_stab_range'],
            far_leg_stab_range=json_data['far_leg_stab_range'],
            min_leg_stab_attack_time=json_data['min_leg_stab_attack_time'],
            leg_stab_damage=DamageInfo.from_json(json_data['leg_stab_damage']),
            toe_target_hp=json_data['toe_target_hp'],
            toe_target_model=json_data['toe_target_model'],
            toe_target_explosion=json_data['toe_target_explosion'],
            sound_toe_target=AudioPlaybackParms.from_json(json_data['sound_toe_target']),
            sound_toe_target_attack=AudioPlaybackParms.from_json(json_data['sound_toe_target_attack']),
            sound_toe_target_explosion=AudioPlaybackParms.from_json(json_data['sound_toe_target_explosion']),
            sound_toe_target_hit=AudioPlaybackParms.from_json(json_data['sound_toe_target_hit']),
            sound_shock_wave=AudioPlaybackParms.from_json(json_data['sound_shock_wave']),
            shock_wave_info=ShockWaveInfo.from_json(json_data['shock_wave_info']),
            vortex_attack_duration=json_data['vortex_attack_duration'],
            vortex_attraction_force=json_data['vortex_attraction_force'],
            max_vortex_attraction_distance=json_data['max_vortex_attraction_distance'],
            vortex_linear_velocity=json_data['vortex_linear_velocity'],
            vortex_linear_acceleration=json_data['vortex_linear_acceleration'],
            vortex_damage=DamageInfo.from_json(json_data['vortex_damage']),
            unknown_0xfb5263e8=json_data['unknown_0xfb5263e8'],
            unknown_0x6aaf33e3=json_data['unknown_0x6aaf33e3'],
            unknown_0x4f5d725c=json_data['unknown_0x4f5d725c'],
            sound_vortex_flash=AudioPlaybackParms.from_json(json_data['sound_vortex_flash']),
            leg_model=json_data['leg_model'],
            shin_armor=json_data['shin_armor'],
            knee_armor_hp=json_data['knee_armor_hp'],
            sound_knee_armor_hit=AudioPlaybackParms.from_json(json_data['sound_knee_armor_hit']),
            sound_knee_vulnerable=AudioPlaybackParms.from_json(json_data['sound_knee_vulnerable']),
            knee_armor=json_data['knee_armor'],
            knee_echo_parameters=EchoParameters.from_json(json_data['knee_echo_parameters']),
            min_protect_knee_time=json_data['min_protect_knee_time'],
            unknown_0x6a754ebd=json_data['unknown_0x6a754ebd'],
            jump_timer=json_data['jump_timer'],
            four_knees_time_scale=json_data['four_knees_time_scale'],
            three_knees_time_scale=json_data['three_knees_time_scale'],
            two_knees_time_scale=json_data['two_knees_time_scale'],
            one_knee_time_scale=json_data['one_knee_time_scale'],
            transmission_beacon=json_data['transmission_beacon'],
            transmission_beacon_fx=json_data['transmission_beacon_fx'],
            transmission_beacon_echo_parameters=EchoParameters.from_json(json_data['transmission_beacon_echo_parameters']),
            sound_transmission_beacon=AudioPlaybackParms.from_json(json_data['sound_transmission_beacon']),
            sound_beacon_extract=AudioPlaybackParms.from_json(json_data['sound_beacon_extract']),
            sound_beacon_retract=AudioPlaybackParms.from_json(json_data['sound_beacon_retract']),
            transmission_beacon_hp=json_data['transmission_beacon_hp'],
            transmission_beacon_explosion=json_data['transmission_beacon_explosion'],
            transmission_beacon_echo_hit=json_data['transmission_beacon_echo_hit'],
            sound_beacon_explode=AudioPlaybackParms.from_json(json_data['sound_beacon_explode']),
            sound_beacon_hit=AudioPlaybackParms.from_json(json_data['sound_beacon_hit']),
            knee_vulnerability=DamageVulnerability.from_json(json_data['knee_vulnerability']),
            vortex_vulnerability=DamageVulnerability.from_json(json_data['vortex_vulnerability']),
            toe_target_vulnerability=DamageVulnerability.from_json(json_data['toe_target_vulnerability']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'scannable_info_crippled': self.scannable_info_crippled,
            'near_leg_stab_range': self.near_leg_stab_range,
            'far_leg_stab_range': self.far_leg_stab_range,
            'min_leg_stab_attack_time': self.min_leg_stab_attack_time,
            'leg_stab_damage': self.leg_stab_damage.to_json(),
            'toe_target_hp': self.toe_target_hp,
            'toe_target_model': self.toe_target_model,
            'toe_target_explosion': self.toe_target_explosion,
            'sound_toe_target': self.sound_toe_target.to_json(),
            'sound_toe_target_attack': self.sound_toe_target_attack.to_json(),
            'sound_toe_target_explosion': self.sound_toe_target_explosion.to_json(),
            'sound_toe_target_hit': self.sound_toe_target_hit.to_json(),
            'sound_shock_wave': self.sound_shock_wave.to_json(),
            'shock_wave_info': self.shock_wave_info.to_json(),
            'vortex_attack_duration': self.vortex_attack_duration,
            'vortex_attraction_force': self.vortex_attraction_force,
            'max_vortex_attraction_distance': self.max_vortex_attraction_distance,
            'vortex_linear_velocity': self.vortex_linear_velocity,
            'vortex_linear_acceleration': self.vortex_linear_acceleration,
            'vortex_damage': self.vortex_damage.to_json(),
            'unknown_0xfb5263e8': self.unknown_0xfb5263e8,
            'unknown_0x6aaf33e3': self.unknown_0x6aaf33e3,
            'unknown_0x4f5d725c': self.unknown_0x4f5d725c,
            'sound_vortex_flash': self.sound_vortex_flash.to_json(),
            'leg_model': self.leg_model,
            'shin_armor': self.shin_armor,
            'knee_armor_hp': self.knee_armor_hp,
            'sound_knee_armor_hit': self.sound_knee_armor_hit.to_json(),
            'sound_knee_vulnerable': self.sound_knee_vulnerable.to_json(),
            'knee_armor': self.knee_armor,
            'knee_echo_parameters': self.knee_echo_parameters.to_json(),
            'min_protect_knee_time': self.min_protect_knee_time,
            'unknown_0x6a754ebd': self.unknown_0x6a754ebd,
            'jump_timer': self.jump_timer,
            'four_knees_time_scale': self.four_knees_time_scale,
            'three_knees_time_scale': self.three_knees_time_scale,
            'two_knees_time_scale': self.two_knees_time_scale,
            'one_knee_time_scale': self.one_knee_time_scale,
            'transmission_beacon': self.transmission_beacon,
            'transmission_beacon_fx': self.transmission_beacon_fx,
            'transmission_beacon_echo_parameters': self.transmission_beacon_echo_parameters.to_json(),
            'sound_transmission_beacon': self.sound_transmission_beacon.to_json(),
            'sound_beacon_extract': self.sound_beacon_extract.to_json(),
            'sound_beacon_retract': self.sound_beacon_retract.to_json(),
            'transmission_beacon_hp': self.transmission_beacon_hp,
            'transmission_beacon_explosion': self.transmission_beacon_explosion,
            'transmission_beacon_echo_hit': self.transmission_beacon_echo_hit,
            'sound_beacon_explode': self.sound_beacon_explode.to_json(),
            'sound_beacon_hit': self.sound_beacon_hit.to_json(),
            'knee_vulnerability': self.knee_vulnerability.to_json(),
            'vortex_vulnerability': self.vortex_vulnerability.to_json(),
            'toe_target_vulnerability': self.toe_target_vulnerability.to_json(),
        }

    def _dependencies_for_scannable_info_crippled(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scannable_info_crippled)

    def _dependencies_for_toe_target_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.toe_target_model)

    def _dependencies_for_toe_target_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.toe_target_explosion)

    def _dependencies_for_leg_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.leg_model)

    def _dependencies_for_shin_armor(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shin_armor)

    def _dependencies_for_knee_armor(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.knee_armor)

    def _dependencies_for_transmission_beacon(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.transmission_beacon)

    def _dependencies_for_transmission_beacon_fx(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.transmission_beacon_fx)

    def _dependencies_for_transmission_beacon_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.transmission_beacon_explosion)

    def _dependencies_for_transmission_beacon_echo_hit(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.transmission_beacon_echo_hit)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_scannable_info_crippled, "scannable_info_crippled", "AssetId"),
            (self._dependencies_for_toe_target_model, "toe_target_model", "AssetId"),
            (self._dependencies_for_toe_target_explosion, "toe_target_explosion", "AssetId"),
            (self.sound_toe_target.dependencies_for, "sound_toe_target", "AudioPlaybackParms"),
            (self.sound_toe_target_attack.dependencies_for, "sound_toe_target_attack", "AudioPlaybackParms"),
            (self.sound_toe_target_explosion.dependencies_for, "sound_toe_target_explosion", "AudioPlaybackParms"),
            (self.sound_toe_target_hit.dependencies_for, "sound_toe_target_hit", "AudioPlaybackParms"),
            (self.sound_shock_wave.dependencies_for, "sound_shock_wave", "AudioPlaybackParms"),
            (self.shock_wave_info.dependencies_for, "shock_wave_info", "ShockWaveInfo"),
            (self.sound_vortex_flash.dependencies_for, "sound_vortex_flash", "AudioPlaybackParms"),
            (self._dependencies_for_leg_model, "leg_model", "AssetId"),
            (self._dependencies_for_shin_armor, "shin_armor", "AssetId"),
            (self.sound_knee_armor_hit.dependencies_for, "sound_knee_armor_hit", "AudioPlaybackParms"),
            (self.sound_knee_vulnerable.dependencies_for, "sound_knee_vulnerable", "AudioPlaybackParms"),
            (self._dependencies_for_knee_armor, "knee_armor", "AssetId"),
            (self._dependencies_for_transmission_beacon, "transmission_beacon", "AssetId"),
            (self._dependencies_for_transmission_beacon_fx, "transmission_beacon_fx", "AssetId"),
            (self.sound_transmission_beacon.dependencies_for, "sound_transmission_beacon", "AudioPlaybackParms"),
            (self.sound_beacon_extract.dependencies_for, "sound_beacon_extract", "AudioPlaybackParms"),
            (self.sound_beacon_retract.dependencies_for, "sound_beacon_retract", "AudioPlaybackParms"),
            (self._dependencies_for_transmission_beacon_explosion, "transmission_beacon_explosion", "AssetId"),
            (self._dependencies_for_transmission_beacon_echo_hit, "transmission_beacon_echo_hit", "AssetId"),
            (self.sound_beacon_explode.dependencies_for, "sound_beacon_explode", "AudioPlaybackParms"),
            (self.sound_beacon_hit.dependencies_for, "sound_beacon_hit", "AudioPlaybackParms"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for DigitalGuardianData.{field_name} ({field_type}): {e}"
                )


def _decode_leg_stab_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 50.0, 'di_knock_back_power': 10.0})


def _decode_sound_toe_target(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_toe_target_attack(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_toe_target_explosion(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_toe_target_hit(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_shock_wave(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_shock_wave_info(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


def _decode_vortex_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 50.0, 'di_knock_back_power': 10.0})


def _decode_sound_vortex_flash(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_knee_armor_hit(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_knee_vulnerable(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_knee_echo_parameters(data: typing.BinaryIO, game: Game, property_size: int) -> EchoParameters:
    return EchoParameters.from_stream(data, game, property_size)


def _decode_transmission_beacon_echo_parameters(data: typing.BinaryIO, game: Game, property_size: int) -> EchoParameters:
    return EchoParameters.from_stream(data, game, property_size)


def _decode_sound_transmission_beacon(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_beacon_extract(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_beacon_retract(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_beacon_explode(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_beacon_hit(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_knee_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_vortex_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_toe_target_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x2aa63fc4: ('scannable_info_crippled', structs.decode_BIG_L),
    0x0faf6a8e: ('near_leg_stab_range', structs.decode_BIG_f),
    0xd3056808: ('far_leg_stab_range', structs.decode_BIG_f),
    0x304b47ee: ('min_leg_stab_attack_time', structs.decode_BIG_f),
    0xefacfa50: ('leg_stab_damage', _decode_leg_stab_damage),
    0xb4561f28: ('toe_target_hp', structs.decode_BIG_f),
    0xbb06dd83: ('toe_target_model', structs.decode_BIG_L),
    0x783635a6: ('toe_target_explosion', structs.decode_BIG_L),
    0x13845a66: ('sound_toe_target', _decode_sound_toe_target),
    0xa305dcba: ('sound_toe_target_attack', _decode_sound_toe_target_attack),
    0xc6ec1630: ('sound_toe_target_explosion', _decode_sound_toe_target_explosion),
    0x98419eac: ('sound_toe_target_hit', _decode_sound_toe_target_hit),
    0x4691c9ab: ('sound_shock_wave', _decode_sound_shock_wave),
    0x8f4787cb: ('shock_wave_info', _decode_shock_wave_info),
    0x76527e01: ('vortex_attack_duration', structs.decode_BIG_f),
    0xd210dfdb: ('vortex_attraction_force', structs.decode_BIG_f),
    0x348bff02: ('max_vortex_attraction_distance', structs.decode_BIG_f),
    0x84fef16f: ('vortex_linear_velocity', structs.decode_BIG_f),
    0x93a74a46: ('vortex_linear_acceleration', structs.decode_BIG_f),
    0x5ca612aa: ('vortex_damage', _decode_vortex_damage),
    0xfb5263e8: ('unknown_0xfb5263e8', structs.decode_BIG_l),
    0x6aaf33e3: ('unknown_0x6aaf33e3', structs.decode_BIG_l),
    0x4f5d725c: ('unknown_0x4f5d725c', structs.decode_BIG_f),
    0x7bfab420: ('sound_vortex_flash', _decode_sound_vortex_flash),
    0xc0a86488: ('leg_model', structs.decode_BIG_L),
    0x8ddd85ca: ('shin_armor', structs.decode_BIG_L),
    0xe3dd61e6: ('knee_armor_hp', structs.decode_BIG_f),
    0x91d2a042: ('sound_knee_armor_hit', _decode_sound_knee_armor_hit),
    0x9386d22b: ('sound_knee_vulnerable', _decode_sound_knee_vulnerable),
    0x5ef8b288: ('knee_armor', structs.decode_BIG_L),
    0x7b5b7312: ('knee_echo_parameters', _decode_knee_echo_parameters),
    0xa324e26c: ('min_protect_knee_time', structs.decode_BIG_f),
    0x6a754ebd: ('unknown_0x6a754ebd', structs.decode_BIG_f),
    0xc9fc9977: ('jump_timer', structs.decode_BIG_f),
    0x8106cda9: ('four_knees_time_scale', structs.decode_BIG_f),
    0x9e1b8105: ('three_knees_time_scale', structs.decode_BIG_f),
    0xa08fcc70: ('two_knees_time_scale', structs.decode_BIG_f),
    0x3254a16b: ('one_knee_time_scale', structs.decode_BIG_f),
    0x5796a143: ('transmission_beacon', structs.decode_BIG_L),
    0x3fa7df1c: ('transmission_beacon_fx', structs.decode_BIG_L),
    0x021b6f9d: ('transmission_beacon_echo_parameters', _decode_transmission_beacon_echo_parameters),
    0x55a8011c: ('sound_transmission_beacon', _decode_sound_transmission_beacon),
    0x7ae73fb3: ('sound_beacon_extract', _decode_sound_beacon_extract),
    0xa9e55c8e: ('sound_beacon_retract', _decode_sound_beacon_retract),
    0x4f6d27d3: ('transmission_beacon_hp', structs.decode_BIG_f),
    0x71f0c674: ('transmission_beacon_explosion', structs.decode_BIG_L),
    0xc8ec315b: ('transmission_beacon_echo_hit', structs.decode_BIG_L),
    0xeed5b990: ('sound_beacon_explode', _decode_sound_beacon_explode),
    0x535f6fec: ('sound_beacon_hit', _decode_sound_beacon_hit),
    0x6dbad233: ('knee_vulnerability', _decode_knee_vulnerability),
    0xf1259e3a: ('vortex_vulnerability', _decode_vortex_vulnerability),
    0xf14f3237: ('toe_target_vulnerability', _decode_toe_target_vulnerability),
}
