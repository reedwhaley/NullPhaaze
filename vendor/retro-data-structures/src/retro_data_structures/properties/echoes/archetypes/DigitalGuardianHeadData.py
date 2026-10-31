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
from retro_data_structures.properties.echoes.archetypes.DigitalGuardianHeadStruct import DigitalGuardianHeadStruct
from retro_data_structures.properties.echoes.archetypes.EchoParameters import EchoParameters
from retro_data_structures.properties.echoes.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class DigitalGuardianHeadDataJson(typing_extensions.TypedDict):
        scannable_info_shield_head: int
        scannable_info_stunned_head: int
        scannable_info_final_head: int
        head_armor: int
        max_turn_speed: float
        max_linear_velocity: float
        gravity_repulsor_hp: float
        max_stunned_linear_velocity: float
        max_stage2_stunned_time: float
        max_stage3a_stunned_time: float
        max_stage3b_stunned_time: float
        sound_head_module_hit: json_util.JsonObject
        detach_from_body_wait_time: float
        drop_shields_fx: int
        sound_raise_shields: json_util.JsonObject
        sound_drop_shields: json_util.JsonObject
        sound_eject_splitter: json_util.JsonObject
        eject_splitter_fx: int
        echo_target_hp: float
        echo_targets: int
        echo_target_emitter_fx: int
        echo_target_destroyed_fx: int
        sound_echo_target_extract: json_util.JsonObject
        sound_echo_target_retract: json_util.JsonObject
        sound_echo_target_transmit: json_util.JsonObject
        sound_echo_target_hit: json_util.JsonObject
        sound_echo_target_explosion: json_util.JsonObject
        echo_targets_parameters: json_util.JsonObject
        unknown: float
        bomb_slot_destroyed_fx: int
        sound_bomb_slot_explosion: json_util.JsonObject
        sound_bomb_slot_destroyed: json_util.JsonObject
        sound_stage3_recover: json_util.JsonObject
        annihilator_pulse: int
        annihilator_pulse_damage: json_util.JsonObject
        annihilator_charge: int
        annihilator_charge_damage: json_util.JsonObject
        annihilator_charge_blur_visor_time: float
        annihilator_charge_filter_cutoff_frequency: int
        frme: int
        lock_on_beams: json_util.JsonObject
        lock_on_missiles: int
        lock_on_missiles_damage: json_util.JsonObject
        machine_gun: int
        machine_gun_damage: json_util.JsonObject
        sound_machine_gun: json_util.JsonObject
        machine_gun_half_sweep_dist: float
        machine_gun_sweep_duration: float
        machine_gun_charge_duration: float
        machine_gun_fire_time: float
        digital_guardian_head_struct_0x8f6732ea: json_util.JsonObject
        digital_guardian_head_struct_0x8e128141: json_util.JsonObject
        digital_guardian_head_struct_0xea54b390: json_util.JsonObject
        digital_guardian_head_struct_0xbbd3e7a7: json_util.JsonObject
        digital_guardian_head_struct_0x2dd88764: json_util.JsonObject
        digital_guardian_head_struct_0x48b46e55: json_util.JsonObject
        bomb_pit_vulnerability: json_util.JsonObject
        echo_target_vulnerability: json_util.JsonObject
    

@dataclasses.dataclass()
class DigitalGuardianHeadData(BaseProperty):
    scannable_info_shield_head: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SCAN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x4eaf47d7, original_name='ScannableInfoShieldHead'
        ),
    })
    scannable_info_stunned_head: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SCAN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x390f3677, original_name='ScannableInfoStunnedHead'
        ),
    })
    scannable_info_final_head: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SCAN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb6eea4ce, original_name='ScannableInfoFinalHead'
        ),
    })
    head_armor: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x07d8cc4f, original_name='HeadArmor'
        ),
    })
    max_turn_speed: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0b5c3c1a, original_name='MaxTurnSpeed'
        ),
    })
    max_linear_velocity: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x00d74fc3, original_name='MaxLinearVelocity'
        ),
    })
    gravity_repulsor_hp: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe7de8b82, original_name='GravityRepulsorHP'
        ),
    })
    max_stunned_linear_velocity: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x96e18283, original_name='MaxStunnedLinearVelocity'
        ),
    })
    max_stage2_stunned_time: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf77138d5, original_name='MaxStage2StunnedTime'
        ),
    })
    max_stage3a_stunned_time: float = dataclasses.field(default=22.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8a83a097, original_name='MaxStage3aStunnedTime'
        ),
    })
    max_stage3b_stunned_time: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd919fb13, original_name='MaxStage3bStunnedTime'
        ),
    })
    sound_head_module_hit: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x0a693a04, original_name='Sound_HeadModuleHit', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    detach_from_body_wait_time: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1cc6d870, original_name='DetachFromBodyWaitTime'
        ),
    })
    drop_shields_fx: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5ff0b26c, original_name='DropShieldsFx'
        ),
    })
    sound_raise_shields: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x50baee63, original_name='Sound_RaiseShields', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_drop_shields: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xa5e1ec03, original_name='Sound_DropShields', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_eject_splitter: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x8d6053cb, original_name='Sound_EjectSplitter', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    eject_splitter_fx: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc91ef399, original_name='EjectSplitterFx'
        ),
    })
    echo_target_hp: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7d3d44af, original_name='EchoTargetHP'
        ),
    })
    echo_targets: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2fa93722, original_name='EchoTargets'
        ),
    })
    echo_target_emitter_fx: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x342ae844, original_name='EchoTargetEmitterFx'
        ),
    })
    echo_target_destroyed_fx: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xcf98f423, original_name='EchoTargetDestroyedFx'
        ),
    })
    sound_echo_target_extract: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x76eedd2a, original_name='Sound_EchoTargetExtract', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_echo_target_retract: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xa5ecbe17, original_name='Sound_EchoTargetRetract', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_echo_target_transmit: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xb1fc705f, original_name='Sound_EchoTargetTransmit', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_echo_target_hit: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x2bc2677a, original_name='Sound_EchoTargetHit', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_echo_target_explosion: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x7f5b82b2, original_name='Sound_EchoTargetExplosion', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    echo_targets_parameters: EchoParameters = dataclasses.field(default_factory=EchoParameters, metadata={
        'reflection': FieldReflection[EchoParameters](
            EchoParameters, id=0x331fd5f7, original_name='EchoTargetsParameters', from_json=EchoParameters.from_json, to_json=EchoParameters.to_json
        ),
    })
    unknown: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8317610f, original_name='Unknown'
        ),
    })
    bomb_slot_destroyed_fx: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x321c97a9, original_name='BombSlotDestroyedFx'
        ),
    })
    sound_bomb_slot_explosion: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xd5cc7e71, original_name='Sound_BombSlotExplosion', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_bomb_slot_destroyed: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xa62c0ea7, original_name='Sound_BombSlotDestroyed', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_stage3_recover: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xfd9f5486, original_name='Sound_Stage3Recover', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    annihilator_pulse: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x27464886, original_name='AnnihilatorPulse'
        ),
    })
    annihilator_pulse_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x4eaf615f, original_name='AnnihilatorPulseDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    annihilator_charge: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd669f12c, original_name='AnnihilatorCharge'
        ),
    })
    annihilator_charge_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x41177ac6, original_name='AnnihilatorChargeDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    annihilator_charge_blur_visor_time: float = dataclasses.field(default=6.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xff7688bf, original_name='AnnihilatorChargeBlurVisorTime'
        ),
    })
    annihilator_charge_filter_cutoff_frequency: int = dataclasses.field(default=1500, metadata={
        'reflection': FieldReflection[int](
            int, id=0x12ebb390, original_name='AnnihilatorChargeFilterCutoffFrequency'
        ),
    })
    frme: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['FRME'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xad151546, original_name='FRME'
        ),
    })
    lock_on_beams: PlasmaBeamInfo = dataclasses.field(default_factory=PlasmaBeamInfo, metadata={
        'reflection': FieldReflection[PlasmaBeamInfo](
            PlasmaBeamInfo, id=0xc7cf5db1, original_name='LockOnBeams', from_json=PlasmaBeamInfo.from_json, to_json=PlasmaBeamInfo.to_json
        ),
    })
    lock_on_missiles: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd187f05c, original_name='LockOnMissiles'
        ),
    })
    lock_on_missiles_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xa8c6106b, original_name='LockOnMissilesDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    machine_gun: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x0b5498d6, original_name='MachineGun'
        ),
    })
    machine_gun_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x45ef2edc, original_name='MachineGunDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    sound_machine_gun: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x47c8115e, original_name='Sound_MachineGun', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    machine_gun_half_sweep_dist: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4ab23ffe, original_name='MachineGunHalfSweepDist'
        ),
    })
    machine_gun_sweep_duration: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x81a8474f, original_name='MachineGunSweepDuration'
        ),
    })
    machine_gun_charge_duration: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x71c406ac, original_name='MachineGunChargeDuration'
        ),
    })
    machine_gun_fire_time: float = dataclasses.field(default=0.15000000596046448, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe5bc88b7, original_name='MachineGunFireTime'
        ),
    })
    digital_guardian_head_struct_0x8f6732ea: DigitalGuardianHeadStruct = dataclasses.field(default_factory=DigitalGuardianHeadStruct, metadata={
        'reflection': FieldReflection[DigitalGuardianHeadStruct](
            DigitalGuardianHeadStruct, id=0x8f6732ea, original_name='DigitalGuardianHeadStruct', from_json=DigitalGuardianHeadStruct.from_json, to_json=DigitalGuardianHeadStruct.to_json
        ),
    })
    digital_guardian_head_struct_0x8e128141: DigitalGuardianHeadStruct = dataclasses.field(default_factory=DigitalGuardianHeadStruct, metadata={
        'reflection': FieldReflection[DigitalGuardianHeadStruct](
            DigitalGuardianHeadStruct, id=0x8e128141, original_name='DigitalGuardianHeadStruct', from_json=DigitalGuardianHeadStruct.from_json, to_json=DigitalGuardianHeadStruct.to_json
        ),
    })
    digital_guardian_head_struct_0xea54b390: DigitalGuardianHeadStruct = dataclasses.field(default_factory=DigitalGuardianHeadStruct, metadata={
        'reflection': FieldReflection[DigitalGuardianHeadStruct](
            DigitalGuardianHeadStruct, id=0xea54b390, original_name='DigitalGuardianHeadStruct', from_json=DigitalGuardianHeadStruct.from_json, to_json=DigitalGuardianHeadStruct.to_json
        ),
    })
    digital_guardian_head_struct_0xbbd3e7a7: DigitalGuardianHeadStruct = dataclasses.field(default_factory=DigitalGuardianHeadStruct, metadata={
        'reflection': FieldReflection[DigitalGuardianHeadStruct](
            DigitalGuardianHeadStruct, id=0xbbd3e7a7, original_name='DigitalGuardianHeadStruct', from_json=DigitalGuardianHeadStruct.from_json, to_json=DigitalGuardianHeadStruct.to_json
        ),
    })
    digital_guardian_head_struct_0x2dd88764: DigitalGuardianHeadStruct = dataclasses.field(default_factory=DigitalGuardianHeadStruct, metadata={
        'reflection': FieldReflection[DigitalGuardianHeadStruct](
            DigitalGuardianHeadStruct, id=0x2dd88764, original_name='DigitalGuardianHeadStruct', from_json=DigitalGuardianHeadStruct.from_json, to_json=DigitalGuardianHeadStruct.to_json
        ),
    })
    digital_guardian_head_struct_0x48b46e55: DigitalGuardianHeadStruct = dataclasses.field(default_factory=DigitalGuardianHeadStruct, metadata={
        'reflection': FieldReflection[DigitalGuardianHeadStruct](
            DigitalGuardianHeadStruct, id=0x48b46e55, original_name='DigitalGuardianHeadStruct', from_json=DigitalGuardianHeadStruct.from_json, to_json=DigitalGuardianHeadStruct.to_json
        ),
    })
    bomb_pit_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x7352d60a, original_name='BombPitVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    echo_target_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x1b2aa049, original_name='EchoTargetVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
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
        if property_count != 58:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4eaf47d7
        scannable_info_shield_head = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x390f3677
        scannable_info_stunned_head = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb6eea4ce
        scannable_info_final_head = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x07d8cc4f
        head_armor = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0b5c3c1a
        max_turn_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x00d74fc3
        max_linear_velocity = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe7de8b82
        gravity_repulsor_hp = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x96e18283
        max_stunned_linear_velocity = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf77138d5
        max_stage2_stunned_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8a83a097
        max_stage3a_stunned_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd919fb13
        max_stage3b_stunned_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0a693a04
        sound_head_module_hit = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1cc6d870
        detach_from_body_wait_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5ff0b26c
        drop_shields_fx = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50baee63
        sound_raise_shields = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa5e1ec03
        sound_drop_shields = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8d6053cb
        sound_eject_splitter = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc91ef399
        eject_splitter_fx = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7d3d44af
        echo_target_hp = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2fa93722
        echo_targets = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x342ae844
        echo_target_emitter_fx = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcf98f423
        echo_target_destroyed_fx = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76eedd2a
        sound_echo_target_extract = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa5ecbe17
        sound_echo_target_retract = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb1fc705f
        sound_echo_target_transmit = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2bc2677a
        sound_echo_target_hit = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7f5b82b2
        sound_echo_target_explosion = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x331fd5f7
        echo_targets_parameters = EchoParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8317610f
        unknown = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x321c97a9
        bomb_slot_destroyed_fx = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd5cc7e71
        sound_bomb_slot_explosion = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa62c0ea7
        sound_bomb_slot_destroyed = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfd9f5486
        sound_stage3_recover = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x27464886
        annihilator_pulse = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4eaf615f
        annihilator_pulse_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd669f12c
        annihilator_charge = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x41177ac6
        annihilator_charge_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xff7688bf
        annihilator_charge_blur_visor_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x12ebb390
        annihilator_charge_filter_cutoff_frequency = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xad151546
        frme = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc7cf5db1
        lock_on_beams = PlasmaBeamInfo.from_stream(data, game, property_size, default_override={'length': 500.0, 'expansion_speed': 4.0, 'life_time': 1.0, 'pulse_speed': 20.0, 'shutdown_time': 0.25, 'pulse_effect_scale': 2.0, 'inner_color': Color(r=0.5, g=0.0, b=0.0, a=0.5), 'outer_color': Color(r=0.699999988079071, g=0.0, b=0.0, a=0.5)})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd187f05c
        lock_on_missiles = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa8c6106b
        lock_on_missiles_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0b5498d6
        machine_gun = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x45ef2edc
        machine_gun_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47c8115e
        sound_machine_gun = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4ab23ffe
        machine_gun_half_sweep_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x81a8474f
        machine_gun_sweep_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71c406ac
        machine_gun_charge_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe5bc88b7
        machine_gun_fire_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8f6732ea
        digital_guardian_head_struct_0x8f6732ea = DigitalGuardianHeadStruct.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8e128141
        digital_guardian_head_struct_0x8e128141 = DigitalGuardianHeadStruct.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xea54b390
        digital_guardian_head_struct_0xea54b390 = DigitalGuardianHeadStruct.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbbd3e7a7
        digital_guardian_head_struct_0xbbd3e7a7 = DigitalGuardianHeadStruct.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2dd88764
        digital_guardian_head_struct_0x2dd88764 = DigitalGuardianHeadStruct.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x48b46e55
        digital_guardian_head_struct_0x48b46e55 = DigitalGuardianHeadStruct.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7352d60a
        bomb_pit_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1b2aa049
        echo_target_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        return cls(scannable_info_shield_head, scannable_info_stunned_head, scannable_info_final_head, head_armor, max_turn_speed, max_linear_velocity, gravity_repulsor_hp, max_stunned_linear_velocity, max_stage2_stunned_time, max_stage3a_stunned_time, max_stage3b_stunned_time, sound_head_module_hit, detach_from_body_wait_time, drop_shields_fx, sound_raise_shields, sound_drop_shields, sound_eject_splitter, eject_splitter_fx, echo_target_hp, echo_targets, echo_target_emitter_fx, echo_target_destroyed_fx, sound_echo_target_extract, sound_echo_target_retract, sound_echo_target_transmit, sound_echo_target_hit, sound_echo_target_explosion, echo_targets_parameters, unknown, bomb_slot_destroyed_fx, sound_bomb_slot_explosion, sound_bomb_slot_destroyed, sound_stage3_recover, annihilator_pulse, annihilator_pulse_damage, annihilator_charge, annihilator_charge_damage, annihilator_charge_blur_visor_time, annihilator_charge_filter_cutoff_frequency, frme, lock_on_beams, lock_on_missiles, lock_on_missiles_damage, machine_gun, machine_gun_damage, sound_machine_gun, machine_gun_half_sweep_dist, machine_gun_sweep_duration, machine_gun_charge_duration, machine_gun_fire_time, digital_guardian_head_struct_0x8f6732ea, digital_guardian_head_struct_0x8e128141, digital_guardian_head_struct_0xea54b390, digital_guardian_head_struct_0xbbd3e7a7, digital_guardian_head_struct_0x2dd88764, digital_guardian_head_struct_0x48b46e55, bomb_pit_vulnerability, echo_target_vulnerability)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00:')  # 58 properties

        data.write(b'N\xafG\xd7')  # 0x4eaf47d7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.scannable_info_shield_head))

        data.write(b'9\x0f6w')  # 0x390f3677
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.scannable_info_stunned_head))

        data.write(b'\xb6\xee\xa4\xce')  # 0xb6eea4ce
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.scannable_info_final_head))

        data.write(b'\x07\xd8\xccO')  # 0x7d8cc4f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.head_armor))

        data.write(b'\x0b\\<\x1a')  # 0xb5c3c1a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_turn_speed))

        data.write(b'\x00\xd7O\xc3')  # 0xd74fc3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_linear_velocity))

        data.write(b'\xe7\xde\x8b\x82')  # 0xe7de8b82
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.gravity_repulsor_hp))

        data.write(b'\x96\xe1\x82\x83')  # 0x96e18283
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_stunned_linear_velocity))

        data.write(b'\xf7q8\xd5')  # 0xf77138d5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_stage2_stunned_time))

        data.write(b'\x8a\x83\xa0\x97')  # 0x8a83a097
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_stage3a_stunned_time))

        data.write(b'\xd9\x19\xfb\x13')  # 0xd919fb13
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_stage3b_stunned_time))

        data.write(b'\ni:\x04')  # 0xa693a04
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_head_module_hit.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x1c\xc6\xd8p')  # 0x1cc6d870
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.detach_from_body_wait_time))

        data.write(b'_\xf0\xb2l')  # 0x5ff0b26c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.drop_shields_fx))

        data.write(b'P\xba\xeec')  # 0x50baee63
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_raise_shields.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa5\xe1\xec\x03')  # 0xa5e1ec03
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_drop_shields.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8d`S\xcb')  # 0x8d6053cb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_eject_splitter.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc9\x1e\xf3\x99')  # 0xc91ef399
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.eject_splitter_fx))

        data.write(b'}=D\xaf')  # 0x7d3d44af
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.echo_target_hp))

        data.write(b'/\xa97"')  # 0x2fa93722
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.echo_targets))

        data.write(b'4*\xe8D')  # 0x342ae844
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.echo_target_emitter_fx))

        data.write(b'\xcf\x98\xf4#')  # 0xcf98f423
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.echo_target_destroyed_fx))

        data.write(b'v\xee\xdd*')  # 0x76eedd2a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_echo_target_extract.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa5\xec\xbe\x17')  # 0xa5ecbe17
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_echo_target_retract.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb1\xfcp_')  # 0xb1fc705f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_echo_target_transmit.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'+\xc2gz')  # 0x2bc2677a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_echo_target_hit.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x7f[\x82\xb2')  # 0x7f5b82b2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_echo_target_explosion.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'3\x1f\xd5\xf7')  # 0x331fd5f7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.echo_targets_parameters.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x83\x17a\x0f')  # 0x8317610f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b'2\x1c\x97\xa9')  # 0x321c97a9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.bomb_slot_destroyed_fx))

        data.write(b'\xd5\xcc~q')  # 0xd5cc7e71
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_bomb_slot_explosion.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa6,\x0e\xa7')  # 0xa62c0ea7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_bomb_slot_destroyed.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfd\x9fT\x86')  # 0xfd9f5486
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_stage3_recover.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"'FH\x86")  # 0x27464886
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.annihilator_pulse))

        data.write(b'N\xafa_')  # 0x4eaf615f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.annihilator_pulse_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd6i\xf1,')  # 0xd669f12c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.annihilator_charge))

        data.write(b'A\x17z\xc6')  # 0x41177ac6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.annihilator_charge_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xffv\x88\xbf')  # 0xff7688bf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.annihilator_charge_blur_visor_time))

        data.write(b'\x12\xeb\xb3\x90')  # 0x12ebb390
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.annihilator_charge_filter_cutoff_frequency))

        data.write(b'\xad\x15\x15F')  # 0xad151546
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.frme))

        data.write(b'\xc7\xcf]\xb1')  # 0xc7cf5db1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.lock_on_beams.to_stream(data, game, default_override={'length': 500.0, 'expansion_speed': 4.0, 'life_time': 1.0, 'pulse_speed': 20.0, 'shutdown_time': 0.25, 'pulse_effect_scale': 2.0, 'inner_color': Color(r=0.5, g=0.0, b=0.0, a=0.5), 'outer_color': Color(r=0.699999988079071, g=0.0, b=0.0, a=0.5)})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd1\x87\xf0\\')  # 0xd187f05c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.lock_on_missiles))

        data.write(b'\xa8\xc6\x10k')  # 0xa8c6106b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.lock_on_missiles_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x0bT\x98\xd6')  # 0xb5498d6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.machine_gun))

        data.write(b'E\xef.\xdc')  # 0x45ef2edc
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.machine_gun_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'G\xc8\x11^')  # 0x47c8115e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_machine_gun.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'J\xb2?\xfe')  # 0x4ab23ffe
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.machine_gun_half_sweep_dist))

        data.write(b'\x81\xa8GO')  # 0x81a8474f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.machine_gun_sweep_duration))

        data.write(b'q\xc4\x06\xac')  # 0x71c406ac
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.machine_gun_charge_duration))

        data.write(b'\xe5\xbc\x88\xb7')  # 0xe5bc88b7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.machine_gun_fire_time))

        data.write(b'\x8fg2\xea')  # 0x8f6732ea
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.digital_guardian_head_struct_0x8f6732ea.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8e\x12\x81A')  # 0x8e128141
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.digital_guardian_head_struct_0x8e128141.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xeaT\xb3\x90')  # 0xea54b390
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.digital_guardian_head_struct_0xea54b390.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbb\xd3\xe7\xa7')  # 0xbbd3e7a7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.digital_guardian_head_struct_0xbbd3e7a7.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'-\xd8\x87d')  # 0x2dd88764
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.digital_guardian_head_struct_0x2dd88764.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'H\xb4nU')  # 0x48b46e55
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.digital_guardian_head_struct_0x48b46e55.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'sR\xd6\n')  # 0x7352d60a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.bomb_pit_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x1b*\xa0I')  # 0x1b2aa049
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.echo_target_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DigitalGuardianHeadDataJson", data)
        return cls(
            scannable_info_shield_head=json_data['scannable_info_shield_head'],
            scannable_info_stunned_head=json_data['scannable_info_stunned_head'],
            scannable_info_final_head=json_data['scannable_info_final_head'],
            head_armor=json_data['head_armor'],
            max_turn_speed=json_data['max_turn_speed'],
            max_linear_velocity=json_data['max_linear_velocity'],
            gravity_repulsor_hp=json_data['gravity_repulsor_hp'],
            max_stunned_linear_velocity=json_data['max_stunned_linear_velocity'],
            max_stage2_stunned_time=json_data['max_stage2_stunned_time'],
            max_stage3a_stunned_time=json_data['max_stage3a_stunned_time'],
            max_stage3b_stunned_time=json_data['max_stage3b_stunned_time'],
            sound_head_module_hit=AudioPlaybackParms.from_json(json_data['sound_head_module_hit']),
            detach_from_body_wait_time=json_data['detach_from_body_wait_time'],
            drop_shields_fx=json_data['drop_shields_fx'],
            sound_raise_shields=AudioPlaybackParms.from_json(json_data['sound_raise_shields']),
            sound_drop_shields=AudioPlaybackParms.from_json(json_data['sound_drop_shields']),
            sound_eject_splitter=AudioPlaybackParms.from_json(json_data['sound_eject_splitter']),
            eject_splitter_fx=json_data['eject_splitter_fx'],
            echo_target_hp=json_data['echo_target_hp'],
            echo_targets=json_data['echo_targets'],
            echo_target_emitter_fx=json_data['echo_target_emitter_fx'],
            echo_target_destroyed_fx=json_data['echo_target_destroyed_fx'],
            sound_echo_target_extract=AudioPlaybackParms.from_json(json_data['sound_echo_target_extract']),
            sound_echo_target_retract=AudioPlaybackParms.from_json(json_data['sound_echo_target_retract']),
            sound_echo_target_transmit=AudioPlaybackParms.from_json(json_data['sound_echo_target_transmit']),
            sound_echo_target_hit=AudioPlaybackParms.from_json(json_data['sound_echo_target_hit']),
            sound_echo_target_explosion=AudioPlaybackParms.from_json(json_data['sound_echo_target_explosion']),
            echo_targets_parameters=EchoParameters.from_json(json_data['echo_targets_parameters']),
            unknown=json_data['unknown'],
            bomb_slot_destroyed_fx=json_data['bomb_slot_destroyed_fx'],
            sound_bomb_slot_explosion=AudioPlaybackParms.from_json(json_data['sound_bomb_slot_explosion']),
            sound_bomb_slot_destroyed=AudioPlaybackParms.from_json(json_data['sound_bomb_slot_destroyed']),
            sound_stage3_recover=AudioPlaybackParms.from_json(json_data['sound_stage3_recover']),
            annihilator_pulse=json_data['annihilator_pulse'],
            annihilator_pulse_damage=DamageInfo.from_json(json_data['annihilator_pulse_damage']),
            annihilator_charge=json_data['annihilator_charge'],
            annihilator_charge_damage=DamageInfo.from_json(json_data['annihilator_charge_damage']),
            annihilator_charge_blur_visor_time=json_data['annihilator_charge_blur_visor_time'],
            annihilator_charge_filter_cutoff_frequency=json_data['annihilator_charge_filter_cutoff_frequency'],
            frme=json_data['frme'],
            lock_on_beams=PlasmaBeamInfo.from_json(json_data['lock_on_beams']),
            lock_on_missiles=json_data['lock_on_missiles'],
            lock_on_missiles_damage=DamageInfo.from_json(json_data['lock_on_missiles_damage']),
            machine_gun=json_data['machine_gun'],
            machine_gun_damage=DamageInfo.from_json(json_data['machine_gun_damage']),
            sound_machine_gun=AudioPlaybackParms.from_json(json_data['sound_machine_gun']),
            machine_gun_half_sweep_dist=json_data['machine_gun_half_sweep_dist'],
            machine_gun_sweep_duration=json_data['machine_gun_sweep_duration'],
            machine_gun_charge_duration=json_data['machine_gun_charge_duration'],
            machine_gun_fire_time=json_data['machine_gun_fire_time'],
            digital_guardian_head_struct_0x8f6732ea=DigitalGuardianHeadStruct.from_json(json_data['digital_guardian_head_struct_0x8f6732ea']),
            digital_guardian_head_struct_0x8e128141=DigitalGuardianHeadStruct.from_json(json_data['digital_guardian_head_struct_0x8e128141']),
            digital_guardian_head_struct_0xea54b390=DigitalGuardianHeadStruct.from_json(json_data['digital_guardian_head_struct_0xea54b390']),
            digital_guardian_head_struct_0xbbd3e7a7=DigitalGuardianHeadStruct.from_json(json_data['digital_guardian_head_struct_0xbbd3e7a7']),
            digital_guardian_head_struct_0x2dd88764=DigitalGuardianHeadStruct.from_json(json_data['digital_guardian_head_struct_0x2dd88764']),
            digital_guardian_head_struct_0x48b46e55=DigitalGuardianHeadStruct.from_json(json_data['digital_guardian_head_struct_0x48b46e55']),
            bomb_pit_vulnerability=DamageVulnerability.from_json(json_data['bomb_pit_vulnerability']),
            echo_target_vulnerability=DamageVulnerability.from_json(json_data['echo_target_vulnerability']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'scannable_info_shield_head': self.scannable_info_shield_head,
            'scannable_info_stunned_head': self.scannable_info_stunned_head,
            'scannable_info_final_head': self.scannable_info_final_head,
            'head_armor': self.head_armor,
            'max_turn_speed': self.max_turn_speed,
            'max_linear_velocity': self.max_linear_velocity,
            'gravity_repulsor_hp': self.gravity_repulsor_hp,
            'max_stunned_linear_velocity': self.max_stunned_linear_velocity,
            'max_stage2_stunned_time': self.max_stage2_stunned_time,
            'max_stage3a_stunned_time': self.max_stage3a_stunned_time,
            'max_stage3b_stunned_time': self.max_stage3b_stunned_time,
            'sound_head_module_hit': self.sound_head_module_hit.to_json(),
            'detach_from_body_wait_time': self.detach_from_body_wait_time,
            'drop_shields_fx': self.drop_shields_fx,
            'sound_raise_shields': self.sound_raise_shields.to_json(),
            'sound_drop_shields': self.sound_drop_shields.to_json(),
            'sound_eject_splitter': self.sound_eject_splitter.to_json(),
            'eject_splitter_fx': self.eject_splitter_fx,
            'echo_target_hp': self.echo_target_hp,
            'echo_targets': self.echo_targets,
            'echo_target_emitter_fx': self.echo_target_emitter_fx,
            'echo_target_destroyed_fx': self.echo_target_destroyed_fx,
            'sound_echo_target_extract': self.sound_echo_target_extract.to_json(),
            'sound_echo_target_retract': self.sound_echo_target_retract.to_json(),
            'sound_echo_target_transmit': self.sound_echo_target_transmit.to_json(),
            'sound_echo_target_hit': self.sound_echo_target_hit.to_json(),
            'sound_echo_target_explosion': self.sound_echo_target_explosion.to_json(),
            'echo_targets_parameters': self.echo_targets_parameters.to_json(),
            'unknown': self.unknown,
            'bomb_slot_destroyed_fx': self.bomb_slot_destroyed_fx,
            'sound_bomb_slot_explosion': self.sound_bomb_slot_explosion.to_json(),
            'sound_bomb_slot_destroyed': self.sound_bomb_slot_destroyed.to_json(),
            'sound_stage3_recover': self.sound_stage3_recover.to_json(),
            'annihilator_pulse': self.annihilator_pulse,
            'annihilator_pulse_damage': self.annihilator_pulse_damage.to_json(),
            'annihilator_charge': self.annihilator_charge,
            'annihilator_charge_damage': self.annihilator_charge_damage.to_json(),
            'annihilator_charge_blur_visor_time': self.annihilator_charge_blur_visor_time,
            'annihilator_charge_filter_cutoff_frequency': self.annihilator_charge_filter_cutoff_frequency,
            'frme': self.frme,
            'lock_on_beams': self.lock_on_beams.to_json(),
            'lock_on_missiles': self.lock_on_missiles,
            'lock_on_missiles_damage': self.lock_on_missiles_damage.to_json(),
            'machine_gun': self.machine_gun,
            'machine_gun_damage': self.machine_gun_damage.to_json(),
            'sound_machine_gun': self.sound_machine_gun.to_json(),
            'machine_gun_half_sweep_dist': self.machine_gun_half_sweep_dist,
            'machine_gun_sweep_duration': self.machine_gun_sweep_duration,
            'machine_gun_charge_duration': self.machine_gun_charge_duration,
            'machine_gun_fire_time': self.machine_gun_fire_time,
            'digital_guardian_head_struct_0x8f6732ea': self.digital_guardian_head_struct_0x8f6732ea.to_json(),
            'digital_guardian_head_struct_0x8e128141': self.digital_guardian_head_struct_0x8e128141.to_json(),
            'digital_guardian_head_struct_0xea54b390': self.digital_guardian_head_struct_0xea54b390.to_json(),
            'digital_guardian_head_struct_0xbbd3e7a7': self.digital_guardian_head_struct_0xbbd3e7a7.to_json(),
            'digital_guardian_head_struct_0x2dd88764': self.digital_guardian_head_struct_0x2dd88764.to_json(),
            'digital_guardian_head_struct_0x48b46e55': self.digital_guardian_head_struct_0x48b46e55.to_json(),
            'bomb_pit_vulnerability': self.bomb_pit_vulnerability.to_json(),
            'echo_target_vulnerability': self.echo_target_vulnerability.to_json(),
        }

    def _dependencies_for_scannable_info_shield_head(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scannable_info_shield_head)

    def _dependencies_for_scannable_info_stunned_head(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scannable_info_stunned_head)

    def _dependencies_for_scannable_info_final_head(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scannable_info_final_head)

    def _dependencies_for_head_armor(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.head_armor)

    def _dependencies_for_drop_shields_fx(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.drop_shields_fx)

    def _dependencies_for_eject_splitter_fx(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.eject_splitter_fx)

    def _dependencies_for_echo_targets(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.echo_targets)

    def _dependencies_for_echo_target_emitter_fx(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.echo_target_emitter_fx)

    def _dependencies_for_echo_target_destroyed_fx(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.echo_target_destroyed_fx)

    def _dependencies_for_bomb_slot_destroyed_fx(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.bomb_slot_destroyed_fx)

    def _dependencies_for_annihilator_pulse(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.annihilator_pulse)

    def _dependencies_for_annihilator_charge(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.annihilator_charge)

    def _dependencies_for_frme(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.frme)

    def _dependencies_for_lock_on_missiles(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.lock_on_missiles)

    def _dependencies_for_machine_gun(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.machine_gun)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_scannable_info_shield_head, "scannable_info_shield_head", "AssetId"),
            (self._dependencies_for_scannable_info_stunned_head, "scannable_info_stunned_head", "AssetId"),
            (self._dependencies_for_scannable_info_final_head, "scannable_info_final_head", "AssetId"),
            (self._dependencies_for_head_armor, "head_armor", "AssetId"),
            (self.sound_head_module_hit.dependencies_for, "sound_head_module_hit", "AudioPlaybackParms"),
            (self._dependencies_for_drop_shields_fx, "drop_shields_fx", "AssetId"),
            (self.sound_raise_shields.dependencies_for, "sound_raise_shields", "AudioPlaybackParms"),
            (self.sound_drop_shields.dependencies_for, "sound_drop_shields", "AudioPlaybackParms"),
            (self.sound_eject_splitter.dependencies_for, "sound_eject_splitter", "AudioPlaybackParms"),
            (self._dependencies_for_eject_splitter_fx, "eject_splitter_fx", "AssetId"),
            (self._dependencies_for_echo_targets, "echo_targets", "AssetId"),
            (self._dependencies_for_echo_target_emitter_fx, "echo_target_emitter_fx", "AssetId"),
            (self._dependencies_for_echo_target_destroyed_fx, "echo_target_destroyed_fx", "AssetId"),
            (self.sound_echo_target_extract.dependencies_for, "sound_echo_target_extract", "AudioPlaybackParms"),
            (self.sound_echo_target_retract.dependencies_for, "sound_echo_target_retract", "AudioPlaybackParms"),
            (self.sound_echo_target_transmit.dependencies_for, "sound_echo_target_transmit", "AudioPlaybackParms"),
            (self.sound_echo_target_hit.dependencies_for, "sound_echo_target_hit", "AudioPlaybackParms"),
            (self.sound_echo_target_explosion.dependencies_for, "sound_echo_target_explosion", "AudioPlaybackParms"),
            (self._dependencies_for_bomb_slot_destroyed_fx, "bomb_slot_destroyed_fx", "AssetId"),
            (self.sound_bomb_slot_explosion.dependencies_for, "sound_bomb_slot_explosion", "AudioPlaybackParms"),
            (self.sound_bomb_slot_destroyed.dependencies_for, "sound_bomb_slot_destroyed", "AudioPlaybackParms"),
            (self.sound_stage3_recover.dependencies_for, "sound_stage3_recover", "AudioPlaybackParms"),
            (self._dependencies_for_annihilator_pulse, "annihilator_pulse", "AssetId"),
            (self._dependencies_for_annihilator_charge, "annihilator_charge", "AssetId"),
            (self._dependencies_for_frme, "frme", "AssetId"),
            (self.lock_on_beams.dependencies_for, "lock_on_beams", "PlasmaBeamInfo"),
            (self._dependencies_for_lock_on_missiles, "lock_on_missiles", "AssetId"),
            (self._dependencies_for_machine_gun, "machine_gun", "AssetId"),
            (self.sound_machine_gun.dependencies_for, "sound_machine_gun", "AudioPlaybackParms"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for DigitalGuardianHeadData.{field_name} ({field_type}): {e}"
                )


def _decode_sound_head_module_hit(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_raise_shields(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_drop_shields(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_eject_splitter(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_echo_target_extract(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_echo_target_retract(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_echo_target_transmit(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_echo_target_hit(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_echo_target_explosion(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_echo_targets_parameters(data: typing.BinaryIO, game: Game, property_size: int) -> EchoParameters:
    return EchoParameters.from_stream(data, game, property_size)


def _decode_sound_bomb_slot_explosion(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_bomb_slot_destroyed(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_stage3_recover(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_annihilator_pulse_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})


def _decode_annihilator_charge_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})


def _decode_lock_on_beams(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size, default_override={'length': 500.0, 'expansion_speed': 4.0, 'life_time': 1.0, 'pulse_speed': 20.0, 'shutdown_time': 0.25, 'pulse_effect_scale': 2.0, 'inner_color': Color(r=0.5, g=0.0, b=0.0, a=0.5), 'outer_color': Color(r=0.699999988079071, g=0.0, b=0.0, a=0.5)})


def _decode_lock_on_missiles_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})


def _decode_machine_gun_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})


def _decode_sound_machine_gun(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_digital_guardian_head_struct_0x8f6732ea(data: typing.BinaryIO, game: Game, property_size: int) -> DigitalGuardianHeadStruct:
    return DigitalGuardianHeadStruct.from_stream(data, game, property_size)


def _decode_digital_guardian_head_struct_0x8e128141(data: typing.BinaryIO, game: Game, property_size: int) -> DigitalGuardianHeadStruct:
    return DigitalGuardianHeadStruct.from_stream(data, game, property_size)


def _decode_digital_guardian_head_struct_0xea54b390(data: typing.BinaryIO, game: Game, property_size: int) -> DigitalGuardianHeadStruct:
    return DigitalGuardianHeadStruct.from_stream(data, game, property_size)


def _decode_digital_guardian_head_struct_0xbbd3e7a7(data: typing.BinaryIO, game: Game, property_size: int) -> DigitalGuardianHeadStruct:
    return DigitalGuardianHeadStruct.from_stream(data, game, property_size)


def _decode_digital_guardian_head_struct_0x2dd88764(data: typing.BinaryIO, game: Game, property_size: int) -> DigitalGuardianHeadStruct:
    return DigitalGuardianHeadStruct.from_stream(data, game, property_size)


def _decode_digital_guardian_head_struct_0x48b46e55(data: typing.BinaryIO, game: Game, property_size: int) -> DigitalGuardianHeadStruct:
    return DigitalGuardianHeadStruct.from_stream(data, game, property_size)


def _decode_bomb_pit_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_echo_target_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x4eaf47d7: ('scannable_info_shield_head', structs.decode_BIG_L),
    0x390f3677: ('scannable_info_stunned_head', structs.decode_BIG_L),
    0xb6eea4ce: ('scannable_info_final_head', structs.decode_BIG_L),
    0x07d8cc4f: ('head_armor', structs.decode_BIG_L),
    0x0b5c3c1a: ('max_turn_speed', structs.decode_BIG_f),
    0x00d74fc3: ('max_linear_velocity', structs.decode_BIG_f),
    0xe7de8b82: ('gravity_repulsor_hp', structs.decode_BIG_f),
    0x96e18283: ('max_stunned_linear_velocity', structs.decode_BIG_f),
    0xf77138d5: ('max_stage2_stunned_time', structs.decode_BIG_f),
    0x8a83a097: ('max_stage3a_stunned_time', structs.decode_BIG_f),
    0xd919fb13: ('max_stage3b_stunned_time', structs.decode_BIG_f),
    0x0a693a04: ('sound_head_module_hit', _decode_sound_head_module_hit),
    0x1cc6d870: ('detach_from_body_wait_time', structs.decode_BIG_f),
    0x5ff0b26c: ('drop_shields_fx', structs.decode_BIG_L),
    0x50baee63: ('sound_raise_shields', _decode_sound_raise_shields),
    0xa5e1ec03: ('sound_drop_shields', _decode_sound_drop_shields),
    0x8d6053cb: ('sound_eject_splitter', _decode_sound_eject_splitter),
    0xc91ef399: ('eject_splitter_fx', structs.decode_BIG_L),
    0x7d3d44af: ('echo_target_hp', structs.decode_BIG_f),
    0x2fa93722: ('echo_targets', structs.decode_BIG_L),
    0x342ae844: ('echo_target_emitter_fx', structs.decode_BIG_L),
    0xcf98f423: ('echo_target_destroyed_fx', structs.decode_BIG_L),
    0x76eedd2a: ('sound_echo_target_extract', _decode_sound_echo_target_extract),
    0xa5ecbe17: ('sound_echo_target_retract', _decode_sound_echo_target_retract),
    0xb1fc705f: ('sound_echo_target_transmit', _decode_sound_echo_target_transmit),
    0x2bc2677a: ('sound_echo_target_hit', _decode_sound_echo_target_hit),
    0x7f5b82b2: ('sound_echo_target_explosion', _decode_sound_echo_target_explosion),
    0x331fd5f7: ('echo_targets_parameters', _decode_echo_targets_parameters),
    0x8317610f: ('unknown', structs.decode_BIG_f),
    0x321c97a9: ('bomb_slot_destroyed_fx', structs.decode_BIG_L),
    0xd5cc7e71: ('sound_bomb_slot_explosion', _decode_sound_bomb_slot_explosion),
    0xa62c0ea7: ('sound_bomb_slot_destroyed', _decode_sound_bomb_slot_destroyed),
    0xfd9f5486: ('sound_stage3_recover', _decode_sound_stage3_recover),
    0x27464886: ('annihilator_pulse', structs.decode_BIG_L),
    0x4eaf615f: ('annihilator_pulse_damage', _decode_annihilator_pulse_damage),
    0xd669f12c: ('annihilator_charge', structs.decode_BIG_L),
    0x41177ac6: ('annihilator_charge_damage', _decode_annihilator_charge_damage),
    0xff7688bf: ('annihilator_charge_blur_visor_time', structs.decode_BIG_f),
    0x12ebb390: ('annihilator_charge_filter_cutoff_frequency', structs.decode_BIG_l),
    0xad151546: ('frme', structs.decode_BIG_L),
    0xc7cf5db1: ('lock_on_beams', _decode_lock_on_beams),
    0xd187f05c: ('lock_on_missiles', structs.decode_BIG_L),
    0xa8c6106b: ('lock_on_missiles_damage', _decode_lock_on_missiles_damage),
    0x0b5498d6: ('machine_gun', structs.decode_BIG_L),
    0x45ef2edc: ('machine_gun_damage', _decode_machine_gun_damage),
    0x47c8115e: ('sound_machine_gun', _decode_sound_machine_gun),
    0x4ab23ffe: ('machine_gun_half_sweep_dist', structs.decode_BIG_f),
    0x81a8474f: ('machine_gun_sweep_duration', structs.decode_BIG_f),
    0x71c406ac: ('machine_gun_charge_duration', structs.decode_BIG_f),
    0xe5bc88b7: ('machine_gun_fire_time', structs.decode_BIG_f),
    0x8f6732ea: ('digital_guardian_head_struct_0x8f6732ea', _decode_digital_guardian_head_struct_0x8f6732ea),
    0x8e128141: ('digital_guardian_head_struct_0x8e128141', _decode_digital_guardian_head_struct_0x8e128141),
    0xea54b390: ('digital_guardian_head_struct_0xea54b390', _decode_digital_guardian_head_struct_0xea54b390),
    0xbbd3e7a7: ('digital_guardian_head_struct_0xbbd3e7a7', _decode_digital_guardian_head_struct_0xbbd3e7a7),
    0x2dd88764: ('digital_guardian_head_struct_0x2dd88764', _decode_digital_guardian_head_struct_0x2dd88764),
    0x48b46e55: ('digital_guardian_head_struct_0x48b46e55', _decode_digital_guardian_head_struct_0x48b46e55),
    0x7352d60a: ('bomb_pit_vulnerability', _decode_bomb_pit_vulnerability),
    0x1b2aa049: ('echo_target_vulnerability', _decode_echo_target_vulnerability),
}
