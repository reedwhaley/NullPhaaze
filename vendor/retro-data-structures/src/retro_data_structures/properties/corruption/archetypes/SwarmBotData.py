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
from retro_data_structures.properties.corruption.archetypes.SwarmSoundData import SwarmSoundData
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SwarmBotDataJson(typing_extensions.TypedDict):
        initial_swarm_bots: int
        max_swarm_bots: int
        unknown_0x37ded7f2: bool
        unknown_0xcab4e0b3: int
        unknown_0xb3fbffc8: float
        creation_effect_pulse_ring: int
        creation_effect_circ_saw: int
        creation_effect_electric_eel: int
        bot_vulnerability_effect: int
        unknown_0x056b2de2: bool
        unknown_0x14eddffc: bool
        can_spin_attack: bool
        can_pulse_ring_attack: bool
        can_electric_eel_attack: bool
        wing_flap_speed: float
        unknown_0xbf0f6889: float
        spinning_tire_damage: json_util.JsonObject
        dive_bomb_damage: json_util.JsonObject
        pulse_projectile: int
        pulse_projectile_damage: json_util.JsonObject
        eel_form_contact_damage: json_util.JsonObject
        eel_form_discharge_damage: json_util.JsonObject
        eel_form_dissolve_explosion: int
        electric_effect: int
        electric_discharge_effect: int
        discharge_effect_contact_explosion: int
        circ_saw_ground_contact_explosion: int
        death_explosion: int
        sound_locomotion_looped: json_util.JsonObject
        sound_locomotion_one_shot_a: json_util.JsonObject
        sound_locomotion_one_shot_b: json_util.JsonObject
        caud: int
        sound_form_pulse_ring: int
        sound_fire_pulse_ring: int
        sound_break_pulse_ring: int
        sound_form_circ_saw: int
        sound_circ_saw_dive: int
        sound_circ_saw_hit_ground: int
        sound_circ_saw_hit_player: int
        sound_form_electric_eel: int
        sound_electric_discharge: int
        sound_electricity_hits_wall: int
        sound_electricity_hits_player: int
        sound_break_electric_eel: int
        sound_swarm_broken: int
        sound_swarm_bot_stunned: int
        stunned_sound_frequency: float
        sound_swarm_bot_begin_dive: int
        sound_swarm_bot_killed: int
        sound_swarm_bot_explosion: int
    

@dataclasses.dataclass()
class SwarmBotData(BaseProperty):
    initial_swarm_bots: int = dataclasses.field(default=8, metadata={
        'reflection': FieldReflection[int](
            int, id=0x6315837d, original_name='InitialSwarmBots'
        ),
    })
    max_swarm_bots: int = dataclasses.field(default=8, metadata={
        'reflection': FieldReflection[int](
            int, id=0x6c605925, original_name='MaxSwarmBots'
        ),
    })
    unknown_0x37ded7f2: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x37ded7f2, original_name='Unknown'
        ),
    })
    unknown_0xcab4e0b3: int = dataclasses.field(default=3, metadata={
        'reflection': FieldReflection[int](
            int, id=0xcab4e0b3, original_name='Unknown'
        ),
    })
    unknown_0xb3fbffc8: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb3fbffc8, original_name='Unknown'
        ),
    })
    creation_effect_pulse_ring: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb07a5895, original_name='CreationEffect_PulseRing'
        ),
    })
    creation_effect_circ_saw: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa3b64d8c, original_name='CreationEffect_CircSaw'
        ),
    })
    creation_effect_electric_eel: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa5b4ed57, original_name='CreationEffect_ElectricEel'
        ),
    })
    bot_vulnerability_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x10cbc9fd, original_name='BotVulnerabilityEffect'
        ),
    })
    unknown_0x056b2de2: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x056b2de2, original_name='Unknown'
        ),
    })
    unknown_0x14eddffc: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x14eddffc, original_name='Unknown'
        ),
    })
    can_spin_attack: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x9bc4fc8d, original_name='CanSpinAttack'
        ),
    })
    can_pulse_ring_attack: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x46f96675, original_name='CanPulseRingAttack'
        ),
    })
    can_electric_eel_attack: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xe6c41f91, original_name='CanElectricEelAttack'
        ),
    })
    wing_flap_speed: float = dataclasses.field(default=28.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x204b8e19, original_name='WingFlapSpeed'
        ),
    })
    unknown_0xbf0f6889: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbf0f6889, original_name='Unknown'
        ),
    })
    spinning_tire_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x1e054e04, original_name='SpinningTireDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    dive_bomb_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xbc7b9832, original_name='DiveBombDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    pulse_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2b309650, original_name='PulseProjectile'
        ),
    })
    pulse_projectile_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x3c8b534d, original_name='PulseProjectileDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    eel_form_contact_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x4d19c32e, original_name='EelFormContactDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    eel_form_discharge_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x840ba904, original_name='EelFormDischargeDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    eel_form_dissolve_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xaf7ffe63, original_name='EelFormDissolveExplosion'
        ),
    })
    electric_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['ELSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x49fae143, original_name='ElectricEffect'
        ),
    })
    electric_discharge_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['ELSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x570aa8f2, original_name='ElectricDischargeEffect'
        ),
    })
    discharge_effect_contact_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xf2dc8618, original_name='DischargeEffectContactExplosion'
        ),
    })
    circ_saw_ground_contact_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd53f059b, original_name='CircSawGroundContactExplosion'
        ),
    })
    death_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x0687c33e, original_name='DeathExplosion'
        ),
    })
    sound_locomotion_looped: SwarmSoundData = dataclasses.field(default_factory=SwarmSoundData, metadata={
        'reflection': FieldReflection[SwarmSoundData](
            SwarmSoundData, id=0x13f55169, original_name='Sound_LocomotionLooped', from_json=SwarmSoundData.from_json, to_json=SwarmSoundData.to_json
        ),
    })
    sound_locomotion_one_shot_a: SwarmSoundData = dataclasses.field(default_factory=SwarmSoundData, metadata={
        'reflection': FieldReflection[SwarmSoundData](
            SwarmSoundData, id=0x9c04df2f, original_name='Sound_LocomotionOneShotA', from_json=SwarmSoundData.from_json, to_json=SwarmSoundData.to_json
        ),
    })
    sound_locomotion_one_shot_b: SwarmSoundData = dataclasses.field(default_factory=SwarmSoundData, metadata={
        'reflection': FieldReflection[SwarmSoundData](
            SwarmSoundData, id=0x8d79b556, original_name='Sound_LocomotionOneShotB', from_json=SwarmSoundData.from_json, to_json=SwarmSoundData.to_json
        ),
    })
    caud: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xeb9a9949, original_name='CAUD'
        ),
    })
    sound_form_pulse_ring: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc3de457e, original_name='Sound_FormPulseRing'
        ),
    })
    sound_fire_pulse_ring: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xab633ef1, original_name='Sound_FirePulseRing'
        ),
    })
    sound_break_pulse_ring: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2a430eb0, original_name='Sound_BreakPulseRing'
        ),
    })
    sound_form_circ_saw: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xaf1768c4, original_name='Sound_FormCircSaw'
        ),
    })
    sound_circ_saw_dive: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x435a0b62, original_name='Sound_CircSawDive'
        ),
    })
    sound_circ_saw_hit_ground: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x13ec5401, original_name='Sound_CircSawHitGround'
        ),
    })
    sound_circ_saw_hit_player: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe5a34fb3, original_name='Sound_CircSawHitPlayer'
        ),
    })
    sound_form_electric_eel: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x7b38d80d, original_name='Sound_FormElectricEel'
        ),
    })
    sound_electric_discharge: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x84360d80, original_name='Sound_ElectricDischarge'
        ),
    })
    sound_electricity_hits_wall: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd2be3af7, original_name='Sound_ElectricityHitsWall'
        ),
    })
    sound_electricity_hits_player: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x9ecc3d08, original_name='Sound_ElectricityHitsPlayer'
        ),
    })
    sound_break_electric_eel: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xcf4f5348, original_name='Sound_BreakElectricEel'
        ),
    })
    sound_swarm_broken: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x05117e35, original_name='Sound_SwarmBroken'
        ),
    })
    sound_swarm_bot_stunned: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa53694c2, original_name='Sound_SwarmBotStunned'
        ),
    })
    stunned_sound_frequency: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdc478968, original_name='StunnedSoundFrequency'
        ),
    })
    sound_swarm_bot_begin_dive: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x091cb316, original_name='Sound_SwarmBotBeginDive'
        ),
    })
    sound_swarm_bot_killed: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x358177cc, original_name='Sound_SwarmBotKilled'
        ),
    })
    sound_swarm_bot_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xab3e98b8, original_name='Sound_SwarmBotExplosion'
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
        if property_count != 50:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6315837d
        initial_swarm_bots = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6c605925
        max_swarm_bots = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x37ded7f2
        unknown_0x37ded7f2 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcab4e0b3
        unknown_0xcab4e0b3 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3fbffc8
        unknown_0xb3fbffc8 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb07a5895
        creation_effect_pulse_ring = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa3b64d8c
        creation_effect_circ_saw = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa5b4ed57
        creation_effect_electric_eel = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x10cbc9fd
        bot_vulnerability_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x056b2de2
        unknown_0x056b2de2 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x14eddffc
        unknown_0x14eddffc = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9bc4fc8d
        can_spin_attack = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x46f96675
        can_pulse_ring_attack = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe6c41f91
        can_electric_eel_attack = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x204b8e19
        wing_flap_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbf0f6889
        unknown_0xbf0f6889 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1e054e04
        spinning_tire_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbc7b9832
        dive_bomb_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2b309650
        pulse_projectile = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3c8b534d
        pulse_projectile_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4d19c32e
        eel_form_contact_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x840ba904
        eel_form_discharge_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaf7ffe63
        eel_form_dissolve_explosion = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49fae143
        electric_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x570aa8f2
        electric_discharge_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf2dc8618
        discharge_effect_contact_explosion = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd53f059b
        circ_saw_ground_contact_explosion = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0687c33e
        death_explosion = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13f55169
        sound_locomotion_looped = SwarmSoundData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9c04df2f
        sound_locomotion_one_shot_a = SwarmSoundData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8d79b556
        sound_locomotion_one_shot_b = SwarmSoundData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xeb9a9949
        caud = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc3de457e
        sound_form_pulse_ring = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xab633ef1
        sound_fire_pulse_ring = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2a430eb0
        sound_break_pulse_ring = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaf1768c4
        sound_form_circ_saw = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x435a0b62
        sound_circ_saw_dive = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13ec5401
        sound_circ_saw_hit_ground = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe5a34fb3
        sound_circ_saw_hit_player = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7b38d80d
        sound_form_electric_eel = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x84360d80
        sound_electric_discharge = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd2be3af7
        sound_electricity_hits_wall = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9ecc3d08
        sound_electricity_hits_player = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcf4f5348
        sound_break_electric_eel = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x05117e35
        sound_swarm_broken = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa53694c2
        sound_swarm_bot_stunned = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdc478968
        stunned_sound_frequency = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x091cb316
        sound_swarm_bot_begin_dive = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x358177cc
        sound_swarm_bot_killed = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xab3e98b8
        sound_swarm_bot_explosion = structs.BIG_Q.unpack(data.read(8))[0]
    
        return cls(initial_swarm_bots, max_swarm_bots, unknown_0x37ded7f2, unknown_0xcab4e0b3, unknown_0xb3fbffc8, creation_effect_pulse_ring, creation_effect_circ_saw, creation_effect_electric_eel, bot_vulnerability_effect, unknown_0x056b2de2, unknown_0x14eddffc, can_spin_attack, can_pulse_ring_attack, can_electric_eel_attack, wing_flap_speed, unknown_0xbf0f6889, spinning_tire_damage, dive_bomb_damage, pulse_projectile, pulse_projectile_damage, eel_form_contact_damage, eel_form_discharge_damage, eel_form_dissolve_explosion, electric_effect, electric_discharge_effect, discharge_effect_contact_explosion, circ_saw_ground_contact_explosion, death_explosion, sound_locomotion_looped, sound_locomotion_one_shot_a, sound_locomotion_one_shot_b, caud, sound_form_pulse_ring, sound_fire_pulse_ring, sound_break_pulse_ring, sound_form_circ_saw, sound_circ_saw_dive, sound_circ_saw_hit_ground, sound_circ_saw_hit_player, sound_form_electric_eel, sound_electric_discharge, sound_electricity_hits_wall, sound_electricity_hits_player, sound_break_electric_eel, sound_swarm_broken, sound_swarm_bot_stunned, stunned_sound_frequency, sound_swarm_bot_begin_dive, sound_swarm_bot_killed, sound_swarm_bot_explosion)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x002')  # 50 properties

        data.write(b'c\x15\x83}')  # 0x6315837d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.initial_swarm_bots))

        data.write(b'l`Y%')  # 0x6c605925
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_swarm_bots))

        data.write(b'7\xde\xd7\xf2')  # 0x37ded7f2
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x37ded7f2))

        data.write(b'\xca\xb4\xe0\xb3')  # 0xcab4e0b3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xcab4e0b3))

        data.write(b'\xb3\xfb\xff\xc8')  # 0xb3fbffc8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb3fbffc8))

        data.write(b'\xb0zX\x95')  # 0xb07a5895
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.creation_effect_pulse_ring))

        data.write(b'\xa3\xb6M\x8c')  # 0xa3b64d8c
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.creation_effect_circ_saw))

        data.write(b'\xa5\xb4\xedW')  # 0xa5b4ed57
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.creation_effect_electric_eel))

        data.write(b'\x10\xcb\xc9\xfd')  # 0x10cbc9fd
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.bot_vulnerability_effect))

        data.write(b'\x05k-\xe2')  # 0x56b2de2
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x056b2de2))

        data.write(b'\x14\xed\xdf\xfc')  # 0x14eddffc
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x14eddffc))

        data.write(b'\x9b\xc4\xfc\x8d')  # 0x9bc4fc8d
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.can_spin_attack))

        data.write(b'F\xf9fu')  # 0x46f96675
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.can_pulse_ring_attack))

        data.write(b'\xe6\xc4\x1f\x91')  # 0xe6c41f91
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.can_electric_eel_attack))

        data.write(b' K\x8e\x19')  # 0x204b8e19
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.wing_flap_speed))

        data.write(b'\xbf\x0fh\x89')  # 0xbf0f6889
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbf0f6889))

        data.write(b'\x1e\x05N\x04')  # 0x1e054e04
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.spinning_tire_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbc{\x982')  # 0xbc7b9832
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.dive_bomb_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'+0\x96P')  # 0x2b309650
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.pulse_projectile))

        data.write(b'<\x8bSM')  # 0x3c8b534d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.pulse_projectile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'M\x19\xc3.')  # 0x4d19c32e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.eel_form_contact_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x84\x0b\xa9\x04')  # 0x840ba904
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.eel_form_discharge_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xaf\x7f\xfec')  # 0xaf7ffe63
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.eel_form_dissolve_explosion))

        data.write(b'I\xfa\xe1C')  # 0x49fae143
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.electric_effect))

        data.write(b'W\n\xa8\xf2')  # 0x570aa8f2
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.electric_discharge_effect))

        data.write(b'\xf2\xdc\x86\x18')  # 0xf2dc8618
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.discharge_effect_contact_explosion))

        data.write(b'\xd5?\x05\x9b')  # 0xd53f059b
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.circ_saw_ground_contact_explosion))

        data.write(b'\x06\x87\xc3>')  # 0x687c33e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.death_explosion))

        data.write(b'\x13\xf5Qi')  # 0x13f55169
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_locomotion_looped.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9c\x04\xdf/')  # 0x9c04df2f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_locomotion_one_shot_a.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8dy\xb5V')  # 0x8d79b556
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_locomotion_one_shot_b.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xeb\x9a\x99I')  # 0xeb9a9949
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.caud))

        data.write(b'\xc3\xdeE~')  # 0xc3de457e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_form_pulse_ring))

        data.write(b'\xabc>\xf1')  # 0xab633ef1
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_fire_pulse_ring))

        data.write(b'*C\x0e\xb0')  # 0x2a430eb0
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_break_pulse_ring))

        data.write(b'\xaf\x17h\xc4')  # 0xaf1768c4
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_form_circ_saw))

        data.write(b'CZ\x0bb')  # 0x435a0b62
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_circ_saw_dive))

        data.write(b'\x13\xecT\x01')  # 0x13ec5401
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_circ_saw_hit_ground))

        data.write(b'\xe5\xa3O\xb3')  # 0xe5a34fb3
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_circ_saw_hit_player))

        data.write(b'{8\xd8\r')  # 0x7b38d80d
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_form_electric_eel))

        data.write(b'\x846\r\x80')  # 0x84360d80
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_electric_discharge))

        data.write(b'\xd2\xbe:\xf7')  # 0xd2be3af7
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_electricity_hits_wall))

        data.write(b'\x9e\xcc=\x08')  # 0x9ecc3d08
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_electricity_hits_player))

        data.write(b'\xcfOSH')  # 0xcf4f5348
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_break_electric_eel))

        data.write(b'\x05\x11~5')  # 0x5117e35
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_swarm_broken))

        data.write(b'\xa56\x94\xc2')  # 0xa53694c2
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_swarm_bot_stunned))

        data.write(b'\xdcG\x89h')  # 0xdc478968
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stunned_sound_frequency))

        data.write(b'\t\x1c\xb3\x16')  # 0x91cb316
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_swarm_bot_begin_dive))

        data.write(b'5\x81w\xcc')  # 0x358177cc
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_swarm_bot_killed))

        data.write(b'\xab>\x98\xb8')  # 0xab3e98b8
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_swarm_bot_explosion))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SwarmBotDataJson", data)
        return cls(
            initial_swarm_bots=json_data['initial_swarm_bots'],
            max_swarm_bots=json_data['max_swarm_bots'],
            unknown_0x37ded7f2=json_data['unknown_0x37ded7f2'],
            unknown_0xcab4e0b3=json_data['unknown_0xcab4e0b3'],
            unknown_0xb3fbffc8=json_data['unknown_0xb3fbffc8'],
            creation_effect_pulse_ring=json_data['creation_effect_pulse_ring'],
            creation_effect_circ_saw=json_data['creation_effect_circ_saw'],
            creation_effect_electric_eel=json_data['creation_effect_electric_eel'],
            bot_vulnerability_effect=json_data['bot_vulnerability_effect'],
            unknown_0x056b2de2=json_data['unknown_0x056b2de2'],
            unknown_0x14eddffc=json_data['unknown_0x14eddffc'],
            can_spin_attack=json_data['can_spin_attack'],
            can_pulse_ring_attack=json_data['can_pulse_ring_attack'],
            can_electric_eel_attack=json_data['can_electric_eel_attack'],
            wing_flap_speed=json_data['wing_flap_speed'],
            unknown_0xbf0f6889=json_data['unknown_0xbf0f6889'],
            spinning_tire_damage=DamageInfo.from_json(json_data['spinning_tire_damage']),
            dive_bomb_damage=DamageInfo.from_json(json_data['dive_bomb_damage']),
            pulse_projectile=json_data['pulse_projectile'],
            pulse_projectile_damage=DamageInfo.from_json(json_data['pulse_projectile_damage']),
            eel_form_contact_damage=DamageInfo.from_json(json_data['eel_form_contact_damage']),
            eel_form_discharge_damage=DamageInfo.from_json(json_data['eel_form_discharge_damage']),
            eel_form_dissolve_explosion=json_data['eel_form_dissolve_explosion'],
            electric_effect=json_data['electric_effect'],
            electric_discharge_effect=json_data['electric_discharge_effect'],
            discharge_effect_contact_explosion=json_data['discharge_effect_contact_explosion'],
            circ_saw_ground_contact_explosion=json_data['circ_saw_ground_contact_explosion'],
            death_explosion=json_data['death_explosion'],
            sound_locomotion_looped=SwarmSoundData.from_json(json_data['sound_locomotion_looped']),
            sound_locomotion_one_shot_a=SwarmSoundData.from_json(json_data['sound_locomotion_one_shot_a']),
            sound_locomotion_one_shot_b=SwarmSoundData.from_json(json_data['sound_locomotion_one_shot_b']),
            caud=json_data['caud'],
            sound_form_pulse_ring=json_data['sound_form_pulse_ring'],
            sound_fire_pulse_ring=json_data['sound_fire_pulse_ring'],
            sound_break_pulse_ring=json_data['sound_break_pulse_ring'],
            sound_form_circ_saw=json_data['sound_form_circ_saw'],
            sound_circ_saw_dive=json_data['sound_circ_saw_dive'],
            sound_circ_saw_hit_ground=json_data['sound_circ_saw_hit_ground'],
            sound_circ_saw_hit_player=json_data['sound_circ_saw_hit_player'],
            sound_form_electric_eel=json_data['sound_form_electric_eel'],
            sound_electric_discharge=json_data['sound_electric_discharge'],
            sound_electricity_hits_wall=json_data['sound_electricity_hits_wall'],
            sound_electricity_hits_player=json_data['sound_electricity_hits_player'],
            sound_break_electric_eel=json_data['sound_break_electric_eel'],
            sound_swarm_broken=json_data['sound_swarm_broken'],
            sound_swarm_bot_stunned=json_data['sound_swarm_bot_stunned'],
            stunned_sound_frequency=json_data['stunned_sound_frequency'],
            sound_swarm_bot_begin_dive=json_data['sound_swarm_bot_begin_dive'],
            sound_swarm_bot_killed=json_data['sound_swarm_bot_killed'],
            sound_swarm_bot_explosion=json_data['sound_swarm_bot_explosion'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'initial_swarm_bots': self.initial_swarm_bots,
            'max_swarm_bots': self.max_swarm_bots,
            'unknown_0x37ded7f2': self.unknown_0x37ded7f2,
            'unknown_0xcab4e0b3': self.unknown_0xcab4e0b3,
            'unknown_0xb3fbffc8': self.unknown_0xb3fbffc8,
            'creation_effect_pulse_ring': self.creation_effect_pulse_ring,
            'creation_effect_circ_saw': self.creation_effect_circ_saw,
            'creation_effect_electric_eel': self.creation_effect_electric_eel,
            'bot_vulnerability_effect': self.bot_vulnerability_effect,
            'unknown_0x056b2de2': self.unknown_0x056b2de2,
            'unknown_0x14eddffc': self.unknown_0x14eddffc,
            'can_spin_attack': self.can_spin_attack,
            'can_pulse_ring_attack': self.can_pulse_ring_attack,
            'can_electric_eel_attack': self.can_electric_eel_attack,
            'wing_flap_speed': self.wing_flap_speed,
            'unknown_0xbf0f6889': self.unknown_0xbf0f6889,
            'spinning_tire_damage': self.spinning_tire_damage.to_json(),
            'dive_bomb_damage': self.dive_bomb_damage.to_json(),
            'pulse_projectile': self.pulse_projectile,
            'pulse_projectile_damage': self.pulse_projectile_damage.to_json(),
            'eel_form_contact_damage': self.eel_form_contact_damage.to_json(),
            'eel_form_discharge_damage': self.eel_form_discharge_damage.to_json(),
            'eel_form_dissolve_explosion': self.eel_form_dissolve_explosion,
            'electric_effect': self.electric_effect,
            'electric_discharge_effect': self.electric_discharge_effect,
            'discharge_effect_contact_explosion': self.discharge_effect_contact_explosion,
            'circ_saw_ground_contact_explosion': self.circ_saw_ground_contact_explosion,
            'death_explosion': self.death_explosion,
            'sound_locomotion_looped': self.sound_locomotion_looped.to_json(),
            'sound_locomotion_one_shot_a': self.sound_locomotion_one_shot_a.to_json(),
            'sound_locomotion_one_shot_b': self.sound_locomotion_one_shot_b.to_json(),
            'caud': self.caud,
            'sound_form_pulse_ring': self.sound_form_pulse_ring,
            'sound_fire_pulse_ring': self.sound_fire_pulse_ring,
            'sound_break_pulse_ring': self.sound_break_pulse_ring,
            'sound_form_circ_saw': self.sound_form_circ_saw,
            'sound_circ_saw_dive': self.sound_circ_saw_dive,
            'sound_circ_saw_hit_ground': self.sound_circ_saw_hit_ground,
            'sound_circ_saw_hit_player': self.sound_circ_saw_hit_player,
            'sound_form_electric_eel': self.sound_form_electric_eel,
            'sound_electric_discharge': self.sound_electric_discharge,
            'sound_electricity_hits_wall': self.sound_electricity_hits_wall,
            'sound_electricity_hits_player': self.sound_electricity_hits_player,
            'sound_break_electric_eel': self.sound_break_electric_eel,
            'sound_swarm_broken': self.sound_swarm_broken,
            'sound_swarm_bot_stunned': self.sound_swarm_bot_stunned,
            'stunned_sound_frequency': self.stunned_sound_frequency,
            'sound_swarm_bot_begin_dive': self.sound_swarm_bot_begin_dive,
            'sound_swarm_bot_killed': self.sound_swarm_bot_killed,
            'sound_swarm_bot_explosion': self.sound_swarm_bot_explosion,
        }

    def _dependencies_for_creation_effect_pulse_ring(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.creation_effect_pulse_ring)

    def _dependencies_for_creation_effect_circ_saw(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.creation_effect_circ_saw)

    def _dependencies_for_creation_effect_electric_eel(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.creation_effect_electric_eel)

    def _dependencies_for_bot_vulnerability_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.bot_vulnerability_effect)

    def _dependencies_for_pulse_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.pulse_projectile)

    def _dependencies_for_eel_form_dissolve_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.eel_form_dissolve_explosion)

    def _dependencies_for_electric_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.electric_effect)

    def _dependencies_for_electric_discharge_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.electric_discharge_effect)

    def _dependencies_for_discharge_effect_contact_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.discharge_effect_contact_explosion)

    def _dependencies_for_circ_saw_ground_contact_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.circ_saw_ground_contact_explosion)

    def _dependencies_for_death_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.death_explosion)

    def _dependencies_for_caud(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.caud)

    def _dependencies_for_sound_form_pulse_ring(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_form_pulse_ring)

    def _dependencies_for_sound_fire_pulse_ring(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_fire_pulse_ring)

    def _dependencies_for_sound_break_pulse_ring(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_break_pulse_ring)

    def _dependencies_for_sound_form_circ_saw(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_form_circ_saw)

    def _dependencies_for_sound_circ_saw_dive(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_circ_saw_dive)

    def _dependencies_for_sound_circ_saw_hit_ground(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_circ_saw_hit_ground)

    def _dependencies_for_sound_circ_saw_hit_player(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_circ_saw_hit_player)

    def _dependencies_for_sound_form_electric_eel(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_form_electric_eel)

    def _dependencies_for_sound_electric_discharge(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_electric_discharge)

    def _dependencies_for_sound_electricity_hits_wall(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_electricity_hits_wall)

    def _dependencies_for_sound_electricity_hits_player(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_electricity_hits_player)

    def _dependencies_for_sound_break_electric_eel(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_break_electric_eel)

    def _dependencies_for_sound_swarm_broken(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_swarm_broken)

    def _dependencies_for_sound_swarm_bot_stunned(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_swarm_bot_stunned)

    def _dependencies_for_sound_swarm_bot_begin_dive(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_swarm_bot_begin_dive)

    def _dependencies_for_sound_swarm_bot_killed(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_swarm_bot_killed)

    def _dependencies_for_sound_swarm_bot_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_swarm_bot_explosion)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_creation_effect_pulse_ring, "creation_effect_pulse_ring", "AssetId"),
            (self._dependencies_for_creation_effect_circ_saw, "creation_effect_circ_saw", "AssetId"),
            (self._dependencies_for_creation_effect_electric_eel, "creation_effect_electric_eel", "AssetId"),
            (self._dependencies_for_bot_vulnerability_effect, "bot_vulnerability_effect", "AssetId"),
            (self._dependencies_for_pulse_projectile, "pulse_projectile", "AssetId"),
            (self._dependencies_for_eel_form_dissolve_explosion, "eel_form_dissolve_explosion", "AssetId"),
            (self._dependencies_for_electric_effect, "electric_effect", "AssetId"),
            (self._dependencies_for_electric_discharge_effect, "electric_discharge_effect", "AssetId"),
            (self._dependencies_for_discharge_effect_contact_explosion, "discharge_effect_contact_explosion", "AssetId"),
            (self._dependencies_for_circ_saw_ground_contact_explosion, "circ_saw_ground_contact_explosion", "AssetId"),
            (self._dependencies_for_death_explosion, "death_explosion", "AssetId"),
            (self.sound_locomotion_looped.dependencies_for, "sound_locomotion_looped", "SwarmSoundData"),
            (self.sound_locomotion_one_shot_a.dependencies_for, "sound_locomotion_one_shot_a", "SwarmSoundData"),
            (self.sound_locomotion_one_shot_b.dependencies_for, "sound_locomotion_one_shot_b", "SwarmSoundData"),
            (self._dependencies_for_caud, "caud", "AssetId"),
            (self._dependencies_for_sound_form_pulse_ring, "sound_form_pulse_ring", "AssetId"),
            (self._dependencies_for_sound_fire_pulse_ring, "sound_fire_pulse_ring", "AssetId"),
            (self._dependencies_for_sound_break_pulse_ring, "sound_break_pulse_ring", "AssetId"),
            (self._dependencies_for_sound_form_circ_saw, "sound_form_circ_saw", "AssetId"),
            (self._dependencies_for_sound_circ_saw_dive, "sound_circ_saw_dive", "AssetId"),
            (self._dependencies_for_sound_circ_saw_hit_ground, "sound_circ_saw_hit_ground", "AssetId"),
            (self._dependencies_for_sound_circ_saw_hit_player, "sound_circ_saw_hit_player", "AssetId"),
            (self._dependencies_for_sound_form_electric_eel, "sound_form_electric_eel", "AssetId"),
            (self._dependencies_for_sound_electric_discharge, "sound_electric_discharge", "AssetId"),
            (self._dependencies_for_sound_electricity_hits_wall, "sound_electricity_hits_wall", "AssetId"),
            (self._dependencies_for_sound_electricity_hits_player, "sound_electricity_hits_player", "AssetId"),
            (self._dependencies_for_sound_break_electric_eel, "sound_break_electric_eel", "AssetId"),
            (self._dependencies_for_sound_swarm_broken, "sound_swarm_broken", "AssetId"),
            (self._dependencies_for_sound_swarm_bot_stunned, "sound_swarm_bot_stunned", "AssetId"),
            (self._dependencies_for_sound_swarm_bot_begin_dive, "sound_swarm_bot_begin_dive", "AssetId"),
            (self._dependencies_for_sound_swarm_bot_killed, "sound_swarm_bot_killed", "AssetId"),
            (self._dependencies_for_sound_swarm_bot_explosion, "sound_swarm_bot_explosion", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for SwarmBotData.{field_name} ({field_type}): {e}"
                )


def _decode_spinning_tire_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_dive_bomb_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_pulse_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_eel_form_contact_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_eel_form_discharge_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_sound_locomotion_looped(data: typing.BinaryIO, game: Game, property_size: int) -> SwarmSoundData:
    return SwarmSoundData.from_stream(data, game, property_size)


def _decode_sound_locomotion_one_shot_a(data: typing.BinaryIO, game: Game, property_size: int) -> SwarmSoundData:
    return SwarmSoundData.from_stream(data, game, property_size)


def _decode_sound_locomotion_one_shot_b(data: typing.BinaryIO, game: Game, property_size: int) -> SwarmSoundData:
    return SwarmSoundData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x6315837d: ('initial_swarm_bots', structs.decode_BIG_l),
    0x6c605925: ('max_swarm_bots', structs.decode_BIG_l),
    0x37ded7f2: ('unknown_0x37ded7f2', structs.decode_BIG_bool_),
    0xcab4e0b3: ('unknown_0xcab4e0b3', structs.decode_BIG_l),
    0xb3fbffc8: ('unknown_0xb3fbffc8', structs.decode_BIG_f),
    0xb07a5895: ('creation_effect_pulse_ring', structs.decode_BIG_Q),
    0xa3b64d8c: ('creation_effect_circ_saw', structs.decode_BIG_Q),
    0xa5b4ed57: ('creation_effect_electric_eel', structs.decode_BIG_Q),
    0x10cbc9fd: ('bot_vulnerability_effect', structs.decode_BIG_Q),
    0x056b2de2: ('unknown_0x056b2de2', structs.decode_BIG_bool_),
    0x14eddffc: ('unknown_0x14eddffc', structs.decode_BIG_bool_),
    0x9bc4fc8d: ('can_spin_attack', structs.decode_BIG_bool_),
    0x46f96675: ('can_pulse_ring_attack', structs.decode_BIG_bool_),
    0xe6c41f91: ('can_electric_eel_attack', structs.decode_BIG_bool_),
    0x204b8e19: ('wing_flap_speed', structs.decode_BIG_f),
    0xbf0f6889: ('unknown_0xbf0f6889', structs.decode_BIG_f),
    0x1e054e04: ('spinning_tire_damage', _decode_spinning_tire_damage),
    0xbc7b9832: ('dive_bomb_damage', _decode_dive_bomb_damage),
    0x2b309650: ('pulse_projectile', structs.decode_BIG_Q),
    0x3c8b534d: ('pulse_projectile_damage', _decode_pulse_projectile_damage),
    0x4d19c32e: ('eel_form_contact_damage', _decode_eel_form_contact_damage),
    0x840ba904: ('eel_form_discharge_damage', _decode_eel_form_discharge_damage),
    0xaf7ffe63: ('eel_form_dissolve_explosion', structs.decode_BIG_Q),
    0x49fae143: ('electric_effect', structs.decode_BIG_Q),
    0x570aa8f2: ('electric_discharge_effect', structs.decode_BIG_Q),
    0xf2dc8618: ('discharge_effect_contact_explosion', structs.decode_BIG_Q),
    0xd53f059b: ('circ_saw_ground_contact_explosion', structs.decode_BIG_Q),
    0x0687c33e: ('death_explosion', structs.decode_BIG_Q),
    0x13f55169: ('sound_locomotion_looped', _decode_sound_locomotion_looped),
    0x9c04df2f: ('sound_locomotion_one_shot_a', _decode_sound_locomotion_one_shot_a),
    0x8d79b556: ('sound_locomotion_one_shot_b', _decode_sound_locomotion_one_shot_b),
    0xeb9a9949: ('caud', structs.decode_BIG_Q),
    0xc3de457e: ('sound_form_pulse_ring', structs.decode_BIG_Q),
    0xab633ef1: ('sound_fire_pulse_ring', structs.decode_BIG_Q),
    0x2a430eb0: ('sound_break_pulse_ring', structs.decode_BIG_Q),
    0xaf1768c4: ('sound_form_circ_saw', structs.decode_BIG_Q),
    0x435a0b62: ('sound_circ_saw_dive', structs.decode_BIG_Q),
    0x13ec5401: ('sound_circ_saw_hit_ground', structs.decode_BIG_Q),
    0xe5a34fb3: ('sound_circ_saw_hit_player', structs.decode_BIG_Q),
    0x7b38d80d: ('sound_form_electric_eel', structs.decode_BIG_Q),
    0x84360d80: ('sound_electric_discharge', structs.decode_BIG_Q),
    0xd2be3af7: ('sound_electricity_hits_wall', structs.decode_BIG_Q),
    0x9ecc3d08: ('sound_electricity_hits_player', structs.decode_BIG_Q),
    0xcf4f5348: ('sound_break_electric_eel', structs.decode_BIG_Q),
    0x05117e35: ('sound_swarm_broken', structs.decode_BIG_Q),
    0xa53694c2: ('sound_swarm_bot_stunned', structs.decode_BIG_Q),
    0xdc478968: ('stunned_sound_frequency', structs.decode_BIG_f),
    0x091cb316: ('sound_swarm_bot_begin_dive', structs.decode_BIG_Q),
    0x358177cc: ('sound_swarm_bot_killed', structs.decode_BIG_Q),
    0xab3e98b8: ('sound_swarm_bot_explosion', structs.decode_BIG_Q),
}
