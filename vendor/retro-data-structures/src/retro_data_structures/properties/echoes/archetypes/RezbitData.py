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
from retro_data_structures.properties.echoes.archetypes.AudioPlaybackParms import AudioPlaybackParms
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class RezbitDataJson(typing_extensions.TypedDict):
        hearing_radius: float
        unknown: float
        derez_time: float
        derez_model: int
        derez_skin_rules: int
        shield_down_time: float
        shield_down_time_variance: float
        shield_up_time: float
        shield_hit_points: float
        shield_explode_effect: int
        sound_shield_explode: json_util.JsonObject
        sound_shield_on: json_util.JsonObject
        sound_shield_off: json_util.JsonObject
        sound_flinch: json_util.JsonObject
        missile_deflect_radius: float
        missile_deflect_rate: float
        sound_deflect_missile: json_util.JsonObject
        strafe_normal_rez_interval: float
        strafe_normal_rez_chance: float
        strafe_derez_interval: float
        strafe_derez_chance: float
        normal_rez_attack_time: float
        energy_bolt_chance: float
        cutting_laser_chance: float
        energy_bolt_min_attack_dist: float
        energy_bolt_max_attack_dist: float
        energy_bolt_damage: json_util.JsonObject
        energy_bolt_projectile: int
        energy_bolt_attack_duration: float
        energy_bolt_attack_variance: float
        energy_bolt_burst_time: float
        sound_energy_bolt: json_util.JsonObject
        virus_min_attack_dist: float
        virus_max_attack_dist: float
        virus_attack_time: float
        virus_damage: json_util.JsonObject
        virus_morphball_fx: int
        sound_virus_hud: int
        sound_hud_reboot: int
        cutting_laser_min_attack_dist: float
        cutting_laser_max_attack_dist: float
        cutting_laser_damage: json_util.JsonObject
        sound_cutting_laser: json_util.JsonObject
        cutting_laser_beam_info: json_util.JsonObject
        shield_vulnerability: json_util.JsonObject
    

@dataclasses.dataclass()
class RezbitData(BaseProperty):
    hearing_radius: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xed69488f, original_name='HearingRadius'
        ),
    })
    unknown: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4a6c4b40, original_name='Unknown'
        ),
    })
    derez_time: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x30d11671, original_name='DerezTime'
        ),
    })
    derez_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc80bb6e4, original_name='DerezModel'
        ),
    })
    derez_skin_rules: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CSKR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x05486319, original_name='DerezSkinRules'
        ),
    })
    shield_down_time: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8980a469, original_name='ShieldDownTime'
        ),
    })
    shield_down_time_variance: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xffb37b81, original_name='ShieldDownTimeVariance'
        ),
    })
    shield_up_time: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x448579cd, original_name='ShieldUpTime'
        ),
    })
    shield_hit_points: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0d1d1648, original_name='ShieldHitPoints'
        ),
    })
    shield_explode_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa41f75ef, original_name='ShieldExplodeEffect'
        ),
    })
    sound_shield_explode: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xa34e2d84, original_name='Sound_ShieldExplode', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_shield_on: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x8c598e41, original_name='Sound_ShieldOn', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_shield_off: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xf4491ed5, original_name='Sound_ShieldOff', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_flinch: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x7d832158, original_name='Sound_Flinch', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    missile_deflect_radius: float = dataclasses.field(default=12.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xad120ad7, original_name='MissileDeflectRadius'
        ),
    })
    missile_deflect_rate: float = dataclasses.field(default=1.2000000476837158, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe70ef8a3, original_name='MissileDeflectRate'
        ),
    })
    sound_deflect_missile: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x6bf2ff60, original_name='Sound_DeflectMissile', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    strafe_normal_rez_interval: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x70e597d4, original_name='StrafeNormalRezInterval'
        ),
    })
    strafe_normal_rez_chance: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x94980a67, original_name='StrafeNormalRezChance'
        ),
    })
    strafe_derez_interval: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd02f08b0, original_name='StrafeDerezInterval'
        ),
    })
    strafe_derez_chance: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x53e84718, original_name='StrafeDerezChance'
        ),
    })
    normal_rez_attack_time: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6fbc1bf9, original_name='NormalRezAttackTime'
        ),
    })
    energy_bolt_chance: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdc276015, original_name='EnergyBoltChance'
        ),
    })
    cutting_laser_chance: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2ca3e9cd, original_name='CuttingLaserChance'
        ),
    })
    energy_bolt_min_attack_dist: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x075491ca, original_name='EnergyBoltMinAttackDist'
        ),
    })
    energy_bolt_max_attack_dist: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x54f2892e, original_name='EnergyBoltMaxAttackDist'
        ),
    })
    energy_bolt_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x600c5f40, original_name='EnergyBoltDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    energy_bolt_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2f11094b, original_name='EnergyBoltProjectile'
        ),
    })
    energy_bolt_attack_duration: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa1f350f5, original_name='EnergyBoltAttackDuration'
        ),
    })
    energy_bolt_attack_variance: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x28944183, original_name='EnergyBoltAttackVariance'
        ),
    })
    energy_bolt_burst_time: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc7a69a59, original_name='EnergyBoltBurstTime'
        ),
    })
    sound_energy_bolt: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xbd3eb001, original_name='Sound_EnergyBolt', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    virus_min_attack_dist: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9ede657f, original_name='VirusMinAttackDist'
        ),
    })
    virus_max_attack_dist: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcd787d9b, original_name='VirusMaxAttackDist'
        ),
    })
    virus_attack_time: float = dataclasses.field(default=6.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4a7d3b04, original_name='VirusAttackTime'
        ),
    })
    virus_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x16869b57, original_name='VirusDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    virus_morphball_fx: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x973d7cc3, original_name='VirusMorphballFx'
        ),
    })
    sound_virus_hud: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xbb3f8a7b, original_name='Sound_VirusHUD'
        ),
    })
    sound_hud_reboot: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x601f846d, original_name='Sound_HUDReboot'
        ),
    })
    cutting_laser_min_attack_dist: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x64c7990d, original_name='CuttingLaserMinAttackDist'
        ),
    })
    cutting_laser_max_attack_dist: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x376181e9, original_name='CuttingLaserMaxAttackDist'
        ),
    })
    cutting_laser_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xbb58c088, original_name='CuttingLaserDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    sound_cutting_laser: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x7864ca32, original_name='Sound_CuttingLaser', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    cutting_laser_beam_info: PlasmaBeamInfo = dataclasses.field(default_factory=PlasmaBeamInfo, metadata={
        'reflection': FieldReflection[PlasmaBeamInfo](
            PlasmaBeamInfo, id=0x59764dbb, original_name='CuttingLaserBeamInfo', from_json=PlasmaBeamInfo.from_json, to_json=PlasmaBeamInfo.to_json
        ),
    })
    shield_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xd34f1323, original_name='ShieldVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
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
        if property_count != 45:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed69488f
        hearing_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4a6c4b40
        unknown = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x30d11671
        derez_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc80bb6e4
        derez_model = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x05486319
        derez_skin_rules = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8980a469
        shield_down_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xffb37b81
        shield_down_time_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x448579cd
        shield_up_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0d1d1648
        shield_hit_points = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa41f75ef
        shield_explode_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa34e2d84
        sound_shield_explode = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8c598e41
        sound_shield_on = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf4491ed5
        sound_shield_off = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7d832158
        sound_flinch = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xad120ad7
        missile_deflect_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe70ef8a3
        missile_deflect_rate = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6bf2ff60
        sound_deflect_missile = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x70e597d4
        strafe_normal_rez_interval = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x94980a67
        strafe_normal_rez_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd02f08b0
        strafe_derez_interval = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x53e84718
        strafe_derez_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6fbc1bf9
        normal_rez_attack_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdc276015
        energy_bolt_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2ca3e9cd
        cutting_laser_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x075491ca
        energy_bolt_min_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x54f2892e
        energy_bolt_max_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x600c5f40
        energy_bolt_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2f11094b
        energy_bolt_projectile = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa1f350f5
        energy_bolt_attack_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x28944183
        energy_bolt_attack_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc7a69a59
        energy_bolt_burst_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbd3eb001
        sound_energy_bolt = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9ede657f
        virus_min_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcd787d9b
        virus_max_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4a7d3b04
        virus_attack_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x16869b57
        virus_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x973d7cc3
        virus_morphball_fx = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbb3f8a7b
        sound_virus_hud = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x601f846d
        sound_hud_reboot = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64c7990d
        cutting_laser_min_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x376181e9
        cutting_laser_max_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbb58c088
        cutting_laser_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7864ca32
        sound_cutting_laser = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x59764dbb
        cutting_laser_beam_info = PlasmaBeamInfo.from_stream(data, game, property_size, default_override={'length': 500.0, 'expansion_speed': 4.0, 'life_time': 1.0, 'pulse_speed': 20.0, 'shutdown_time': 0.25, 'pulse_effect_scale': 2.0, 'inner_color': Color(r=0.5, g=0.5, b=0.5, a=0.5), 'outer_color': Color(r=0.6000000238418579, g=0.6000000238418579, b=0.0, a=0.5)})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd34f1323
        shield_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        return cls(hearing_radius, unknown, derez_time, derez_model, derez_skin_rules, shield_down_time, shield_down_time_variance, shield_up_time, shield_hit_points, shield_explode_effect, sound_shield_explode, sound_shield_on, sound_shield_off, sound_flinch, missile_deflect_radius, missile_deflect_rate, sound_deflect_missile, strafe_normal_rez_interval, strafe_normal_rez_chance, strafe_derez_interval, strafe_derez_chance, normal_rez_attack_time, energy_bolt_chance, cutting_laser_chance, energy_bolt_min_attack_dist, energy_bolt_max_attack_dist, energy_bolt_damage, energy_bolt_projectile, energy_bolt_attack_duration, energy_bolt_attack_variance, energy_bolt_burst_time, sound_energy_bolt, virus_min_attack_dist, virus_max_attack_dist, virus_attack_time, virus_damage, virus_morphball_fx, sound_virus_hud, sound_hud_reboot, cutting_laser_min_attack_dist, cutting_laser_max_attack_dist, cutting_laser_damage, sound_cutting_laser, cutting_laser_beam_info, shield_vulnerability)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00-')  # 45 properties

        data.write(b'\xediH\x8f')  # 0xed69488f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hearing_radius))

        data.write(b'JlK@')  # 0x4a6c4b40
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b'0\xd1\x16q')  # 0x30d11671
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.derez_time))

        data.write(b'\xc8\x0b\xb6\xe4')  # 0xc80bb6e4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.derez_model))

        data.write(b'\x05Hc\x19')  # 0x5486319
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.derez_skin_rules))

        data.write(b'\x89\x80\xa4i')  # 0x8980a469
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.shield_down_time))

        data.write(b'\xff\xb3{\x81')  # 0xffb37b81
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.shield_down_time_variance))

        data.write(b'D\x85y\xcd')  # 0x448579cd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.shield_up_time))

        data.write(b'\r\x1d\x16H')  # 0xd1d1648
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.shield_hit_points))

        data.write(b'\xa4\x1fu\xef')  # 0xa41f75ef
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.shield_explode_effect))

        data.write(b'\xa3N-\x84')  # 0xa34e2d84
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_shield_explode.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8cY\x8eA')  # 0x8c598e41
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_shield_on.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf4I\x1e\xd5')  # 0xf4491ed5
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_shield_off.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'}\x83!X')  # 0x7d832158
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_flinch.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xad\x12\n\xd7')  # 0xad120ad7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.missile_deflect_radius))

        data.write(b'\xe7\x0e\xf8\xa3')  # 0xe70ef8a3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.missile_deflect_rate))

        data.write(b'k\xf2\xff`')  # 0x6bf2ff60
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_deflect_missile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'p\xe5\x97\xd4')  # 0x70e597d4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.strafe_normal_rez_interval))

        data.write(b'\x94\x98\ng')  # 0x94980a67
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.strafe_normal_rez_chance))

        data.write(b'\xd0/\x08\xb0')  # 0xd02f08b0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.strafe_derez_interval))

        data.write(b'S\xe8G\x18')  # 0x53e84718
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.strafe_derez_chance))

        data.write(b'o\xbc\x1b\xf9')  # 0x6fbc1bf9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.normal_rez_attack_time))

        data.write(b"\xdc'`\x15")  # 0xdc276015
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.energy_bolt_chance))

        data.write(b',\xa3\xe9\xcd')  # 0x2ca3e9cd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.cutting_laser_chance))

        data.write(b'\x07T\x91\xca')  # 0x75491ca
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.energy_bolt_min_attack_dist))

        data.write(b'T\xf2\x89.')  # 0x54f2892e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.energy_bolt_max_attack_dist))

        data.write(b'`\x0c_@')  # 0x600c5f40
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.energy_bolt_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'/\x11\tK')  # 0x2f11094b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.energy_bolt_projectile))

        data.write(b'\xa1\xf3P\xf5')  # 0xa1f350f5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.energy_bolt_attack_duration))

        data.write(b'(\x94A\x83')  # 0x28944183
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.energy_bolt_attack_variance))

        data.write(b'\xc7\xa6\x9aY')  # 0xc7a69a59
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.energy_bolt_burst_time))

        data.write(b'\xbd>\xb0\x01')  # 0xbd3eb001
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_energy_bolt.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9e\xdee\x7f')  # 0x9ede657f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.virus_min_attack_dist))

        data.write(b'\xcdx}\x9b')  # 0xcd787d9b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.virus_max_attack_dist))

        data.write(b'J};\x04')  # 0x4a7d3b04
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.virus_attack_time))

        data.write(b'\x16\x86\x9bW')  # 0x16869b57
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.virus_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x97=|\xc3')  # 0x973d7cc3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.virus_morphball_fx))

        data.write(b'\xbb?\x8a{')  # 0xbb3f8a7b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_virus_hud))

        data.write(b'`\x1f\x84m')  # 0x601f846d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_hud_reboot))

        data.write(b'd\xc7\x99\r')  # 0x64c7990d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.cutting_laser_min_attack_dist))

        data.write(b'7a\x81\xe9')  # 0x376181e9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.cutting_laser_max_attack_dist))

        data.write(b'\xbbX\xc0\x88')  # 0xbb58c088
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.cutting_laser_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'xd\xca2')  # 0x7864ca32
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_cutting_laser.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'YvM\xbb')  # 0x59764dbb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.cutting_laser_beam_info.to_stream(data, game, default_override={'length': 500.0, 'expansion_speed': 4.0, 'life_time': 1.0, 'pulse_speed': 20.0, 'shutdown_time': 0.25, 'pulse_effect_scale': 2.0, 'inner_color': Color(r=0.5, g=0.5, b=0.5, a=0.5), 'outer_color': Color(r=0.6000000238418579, g=0.6000000238418579, b=0.0, a=0.5)})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd3O\x13#')  # 0xd34f1323
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shield_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("RezbitDataJson", data)
        return cls(
            hearing_radius=json_data['hearing_radius'],
            unknown=json_data['unknown'],
            derez_time=json_data['derez_time'],
            derez_model=json_data['derez_model'],
            derez_skin_rules=json_data['derez_skin_rules'],
            shield_down_time=json_data['shield_down_time'],
            shield_down_time_variance=json_data['shield_down_time_variance'],
            shield_up_time=json_data['shield_up_time'],
            shield_hit_points=json_data['shield_hit_points'],
            shield_explode_effect=json_data['shield_explode_effect'],
            sound_shield_explode=AudioPlaybackParms.from_json(json_data['sound_shield_explode']),
            sound_shield_on=AudioPlaybackParms.from_json(json_data['sound_shield_on']),
            sound_shield_off=AudioPlaybackParms.from_json(json_data['sound_shield_off']),
            sound_flinch=AudioPlaybackParms.from_json(json_data['sound_flinch']),
            missile_deflect_radius=json_data['missile_deflect_radius'],
            missile_deflect_rate=json_data['missile_deflect_rate'],
            sound_deflect_missile=AudioPlaybackParms.from_json(json_data['sound_deflect_missile']),
            strafe_normal_rez_interval=json_data['strafe_normal_rez_interval'],
            strafe_normal_rez_chance=json_data['strafe_normal_rez_chance'],
            strafe_derez_interval=json_data['strafe_derez_interval'],
            strafe_derez_chance=json_data['strafe_derez_chance'],
            normal_rez_attack_time=json_data['normal_rez_attack_time'],
            energy_bolt_chance=json_data['energy_bolt_chance'],
            cutting_laser_chance=json_data['cutting_laser_chance'],
            energy_bolt_min_attack_dist=json_data['energy_bolt_min_attack_dist'],
            energy_bolt_max_attack_dist=json_data['energy_bolt_max_attack_dist'],
            energy_bolt_damage=DamageInfo.from_json(json_data['energy_bolt_damage']),
            energy_bolt_projectile=json_data['energy_bolt_projectile'],
            energy_bolt_attack_duration=json_data['energy_bolt_attack_duration'],
            energy_bolt_attack_variance=json_data['energy_bolt_attack_variance'],
            energy_bolt_burst_time=json_data['energy_bolt_burst_time'],
            sound_energy_bolt=AudioPlaybackParms.from_json(json_data['sound_energy_bolt']),
            virus_min_attack_dist=json_data['virus_min_attack_dist'],
            virus_max_attack_dist=json_data['virus_max_attack_dist'],
            virus_attack_time=json_data['virus_attack_time'],
            virus_damage=DamageInfo.from_json(json_data['virus_damage']),
            virus_morphball_fx=json_data['virus_morphball_fx'],
            sound_virus_hud=json_data['sound_virus_hud'],
            sound_hud_reboot=json_data['sound_hud_reboot'],
            cutting_laser_min_attack_dist=json_data['cutting_laser_min_attack_dist'],
            cutting_laser_max_attack_dist=json_data['cutting_laser_max_attack_dist'],
            cutting_laser_damage=DamageInfo.from_json(json_data['cutting_laser_damage']),
            sound_cutting_laser=AudioPlaybackParms.from_json(json_data['sound_cutting_laser']),
            cutting_laser_beam_info=PlasmaBeamInfo.from_json(json_data['cutting_laser_beam_info']),
            shield_vulnerability=DamageVulnerability.from_json(json_data['shield_vulnerability']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'hearing_radius': self.hearing_radius,
            'unknown': self.unknown,
            'derez_time': self.derez_time,
            'derez_model': self.derez_model,
            'derez_skin_rules': self.derez_skin_rules,
            'shield_down_time': self.shield_down_time,
            'shield_down_time_variance': self.shield_down_time_variance,
            'shield_up_time': self.shield_up_time,
            'shield_hit_points': self.shield_hit_points,
            'shield_explode_effect': self.shield_explode_effect,
            'sound_shield_explode': self.sound_shield_explode.to_json(),
            'sound_shield_on': self.sound_shield_on.to_json(),
            'sound_shield_off': self.sound_shield_off.to_json(),
            'sound_flinch': self.sound_flinch.to_json(),
            'missile_deflect_radius': self.missile_deflect_radius,
            'missile_deflect_rate': self.missile_deflect_rate,
            'sound_deflect_missile': self.sound_deflect_missile.to_json(),
            'strafe_normal_rez_interval': self.strafe_normal_rez_interval,
            'strafe_normal_rez_chance': self.strafe_normal_rez_chance,
            'strafe_derez_interval': self.strafe_derez_interval,
            'strafe_derez_chance': self.strafe_derez_chance,
            'normal_rez_attack_time': self.normal_rez_attack_time,
            'energy_bolt_chance': self.energy_bolt_chance,
            'cutting_laser_chance': self.cutting_laser_chance,
            'energy_bolt_min_attack_dist': self.energy_bolt_min_attack_dist,
            'energy_bolt_max_attack_dist': self.energy_bolt_max_attack_dist,
            'energy_bolt_damage': self.energy_bolt_damage.to_json(),
            'energy_bolt_projectile': self.energy_bolt_projectile,
            'energy_bolt_attack_duration': self.energy_bolt_attack_duration,
            'energy_bolt_attack_variance': self.energy_bolt_attack_variance,
            'energy_bolt_burst_time': self.energy_bolt_burst_time,
            'sound_energy_bolt': self.sound_energy_bolt.to_json(),
            'virus_min_attack_dist': self.virus_min_attack_dist,
            'virus_max_attack_dist': self.virus_max_attack_dist,
            'virus_attack_time': self.virus_attack_time,
            'virus_damage': self.virus_damage.to_json(),
            'virus_morphball_fx': self.virus_morphball_fx,
            'sound_virus_hud': self.sound_virus_hud,
            'sound_hud_reboot': self.sound_hud_reboot,
            'cutting_laser_min_attack_dist': self.cutting_laser_min_attack_dist,
            'cutting_laser_max_attack_dist': self.cutting_laser_max_attack_dist,
            'cutting_laser_damage': self.cutting_laser_damage.to_json(),
            'sound_cutting_laser': self.sound_cutting_laser.to_json(),
            'cutting_laser_beam_info': self.cutting_laser_beam_info.to_json(),
            'shield_vulnerability': self.shield_vulnerability.to_json(),
        }

    def _dependencies_for_derez_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.derez_model)

    def _dependencies_for_derez_skin_rules(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.derez_skin_rules)

    def _dependencies_for_shield_explode_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_explode_effect)

    def _dependencies_for_energy_bolt_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.energy_bolt_projectile)

    def _dependencies_for_virus_morphball_fx(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.virus_morphball_fx)

    def _dependencies_for_sound_virus_hud(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_virus_hud)

    def _dependencies_for_sound_hud_reboot(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_hud_reboot)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_derez_model, "derez_model", "AssetId"),
            (self._dependencies_for_derez_skin_rules, "derez_skin_rules", "AssetId"),
            (self._dependencies_for_shield_explode_effect, "shield_explode_effect", "AssetId"),
            (self.sound_shield_explode.dependencies_for, "sound_shield_explode", "AudioPlaybackParms"),
            (self.sound_shield_on.dependencies_for, "sound_shield_on", "AudioPlaybackParms"),
            (self.sound_shield_off.dependencies_for, "sound_shield_off", "AudioPlaybackParms"),
            (self.sound_flinch.dependencies_for, "sound_flinch", "AudioPlaybackParms"),
            (self.sound_deflect_missile.dependencies_for, "sound_deflect_missile", "AudioPlaybackParms"),
            (self._dependencies_for_energy_bolt_projectile, "energy_bolt_projectile", "AssetId"),
            (self.sound_energy_bolt.dependencies_for, "sound_energy_bolt", "AudioPlaybackParms"),
            (self._dependencies_for_virus_morphball_fx, "virus_morphball_fx", "AssetId"),
            (self._dependencies_for_sound_virus_hud, "sound_virus_hud", "int"),
            (self._dependencies_for_sound_hud_reboot, "sound_hud_reboot", "int"),
            (self.sound_cutting_laser.dependencies_for, "sound_cutting_laser", "AudioPlaybackParms"),
            (self.cutting_laser_beam_info.dependencies_for, "cutting_laser_beam_info", "PlasmaBeamInfo"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for RezbitData.{field_name} ({field_type}): {e}"
                )


def _decode_sound_shield_explode(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_shield_on(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_shield_off(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_flinch(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_deflect_missile(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_energy_bolt_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 5.0})


def _decode_sound_energy_bolt(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_virus_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 5.0})


def _decode_cutting_laser_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 5.0})


def _decode_sound_cutting_laser(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_cutting_laser_beam_info(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size, default_override={'length': 500.0, 'expansion_speed': 4.0, 'life_time': 1.0, 'pulse_speed': 20.0, 'shutdown_time': 0.25, 'pulse_effect_scale': 2.0, 'inner_color': Color(r=0.5, g=0.5, b=0.5, a=0.5), 'outer_color': Color(r=0.6000000238418579, g=0.6000000238418579, b=0.0, a=0.5)})


def _decode_shield_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xed69488f: ('hearing_radius', structs.decode_BIG_f),
    0x4a6c4b40: ('unknown', structs.decode_BIG_f),
    0x30d11671: ('derez_time', structs.decode_BIG_f),
    0xc80bb6e4: ('derez_model', structs.decode_BIG_L),
    0x05486319: ('derez_skin_rules', structs.decode_BIG_L),
    0x8980a469: ('shield_down_time', structs.decode_BIG_f),
    0xffb37b81: ('shield_down_time_variance', structs.decode_BIG_f),
    0x448579cd: ('shield_up_time', structs.decode_BIG_f),
    0x0d1d1648: ('shield_hit_points', structs.decode_BIG_f),
    0xa41f75ef: ('shield_explode_effect', structs.decode_BIG_L),
    0xa34e2d84: ('sound_shield_explode', _decode_sound_shield_explode),
    0x8c598e41: ('sound_shield_on', _decode_sound_shield_on),
    0xf4491ed5: ('sound_shield_off', _decode_sound_shield_off),
    0x7d832158: ('sound_flinch', _decode_sound_flinch),
    0xad120ad7: ('missile_deflect_radius', structs.decode_BIG_f),
    0xe70ef8a3: ('missile_deflect_rate', structs.decode_BIG_f),
    0x6bf2ff60: ('sound_deflect_missile', _decode_sound_deflect_missile),
    0x70e597d4: ('strafe_normal_rez_interval', structs.decode_BIG_f),
    0x94980a67: ('strafe_normal_rez_chance', structs.decode_BIG_f),
    0xd02f08b0: ('strafe_derez_interval', structs.decode_BIG_f),
    0x53e84718: ('strafe_derez_chance', structs.decode_BIG_f),
    0x6fbc1bf9: ('normal_rez_attack_time', structs.decode_BIG_f),
    0xdc276015: ('energy_bolt_chance', structs.decode_BIG_f),
    0x2ca3e9cd: ('cutting_laser_chance', structs.decode_BIG_f),
    0x075491ca: ('energy_bolt_min_attack_dist', structs.decode_BIG_f),
    0x54f2892e: ('energy_bolt_max_attack_dist', structs.decode_BIG_f),
    0x600c5f40: ('energy_bolt_damage', _decode_energy_bolt_damage),
    0x2f11094b: ('energy_bolt_projectile', structs.decode_BIG_L),
    0xa1f350f5: ('energy_bolt_attack_duration', structs.decode_BIG_f),
    0x28944183: ('energy_bolt_attack_variance', structs.decode_BIG_f),
    0xc7a69a59: ('energy_bolt_burst_time', structs.decode_BIG_f),
    0xbd3eb001: ('sound_energy_bolt', _decode_sound_energy_bolt),
    0x9ede657f: ('virus_min_attack_dist', structs.decode_BIG_f),
    0xcd787d9b: ('virus_max_attack_dist', structs.decode_BIG_f),
    0x4a7d3b04: ('virus_attack_time', structs.decode_BIG_f),
    0x16869b57: ('virus_damage', _decode_virus_damage),
    0x973d7cc3: ('virus_morphball_fx', structs.decode_BIG_L),
    0xbb3f8a7b: ('sound_virus_hud', structs.decode_BIG_l),
    0x601f846d: ('sound_hud_reboot', structs.decode_BIG_l),
    0x64c7990d: ('cutting_laser_min_attack_dist', structs.decode_BIG_f),
    0x376181e9: ('cutting_laser_max_attack_dist', structs.decode_BIG_f),
    0xbb58c088: ('cutting_laser_damage', _decode_cutting_laser_damage),
    0x7864ca32: ('sound_cutting_laser', _decode_sound_cutting_laser),
    0x59764dbb: ('cutting_laser_beam_info', _decode_cutting_laser_beam_info),
    0xd34f1323: ('shield_vulnerability', _decode_shield_vulnerability),
}
