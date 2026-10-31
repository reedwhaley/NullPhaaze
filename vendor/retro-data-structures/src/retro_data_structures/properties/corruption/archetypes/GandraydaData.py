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
from retro_data_structures.properties.corruption.archetypes.GandraydaChakram import GandraydaChakram
from retro_data_structures.properties.corruption.archetypes.GandraydaStage1Data import GandraydaStage1Data
from retro_data_structures.properties.corruption.archetypes.GandraydaStage2Data import GandraydaStage2Data
from retro_data_structures.properties.corruption.archetypes.GandraydaStage3Data import GandraydaStage3Data
from retro_data_structures.properties.corruption.archetypes.GandraydaStage4Data import GandraydaStage4Data
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class GandraydaDataJson(typing_extensions.TypedDict):
        unknown_0x538d71cb: float
        unknown_0xd42bba88: float
        unknown_0xf4b9c6c3: float
        unknown_0x4d4d934b: float
        min_navigation_time: float
        max_navigation_time: float
        unknown_0x32dd1ed4: float
        unknown_0x4ba741d5: float
        unknown_0x1eebf378: float
        melee_weapon: int
        melee_damage: json_util.JsonObject
        radial_melee_damage: json_util.JsonObject
        min_throw_projectile_time: float
        max_throw_projectile_time: float
        thrown_projectile: int
        thrown_projectile_damage: json_util.JsonObject
        thrown_projectile_visor_effect: int
        thrown_projectile_visor_impact_sound: int
        energy_wave_chance: float
        unknown_0x61f74274: int
        min_energy_wave_jump_dist: float
        max_energy_wave_jump_dist: float
        min_energy_wave_attack_time: float
        max_energy_wave_attack_time: float
        energy_wave_jump_apex: float
        min_energy_wave_attack_dist: float
        energy_wave_projectile: int
        energy_wave_projectile_damage: json_util.JsonObject
        grapple_attack_chance: float
        min_grapple_attack_dist: float
        max_grapple_attack_dist: float
        grapple_connect_dist: float
        grapple_offset: json_util.JsonValue
        grapple_turn_speed: float
        min_grapple_attack_time: float
        max_grapple_attack_time: float
        grapple_mount_jump_apex: float
        grapple_dismount_jump_apex: float
        grapple_connected_visor_effect: int
        grapple_damage_visor_effect_left: int
        grapple_damage_visor_effect_right: int
        grapple_condensation_visor_effect: int
        grapple_pull_damage: json_util.JsonObject
        grapple_damage: json_util.JsonObject
        grapple_shake_sound: int
        min_grapple_shake_volume: float
        max_grapple_shake_volume: float
        unknown_0xb5fdc280: float
        unknown_0x41d8c39c: float
        chakram: json_util.JsonObject
        stage1_data: json_util.JsonObject
        stage2_data: json_util.JsonObject
        stage3_data: json_util.JsonObject
        stage4_data: json_util.JsonObject
    

@dataclasses.dataclass()
class GandraydaData(BaseProperty):
    unknown_0x538d71cb: float = dataclasses.field(default=75.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x538d71cb, original_name='Unknown'
        ),
    })
    unknown_0xd42bba88: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd42bba88, original_name='Unknown'
        ),
    })
    unknown_0xf4b9c6c3: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf4b9c6c3, original_name='Unknown'
        ),
    })
    unknown_0x4d4d934b: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4d4d934b, original_name='Unknown'
        ),
    })
    min_navigation_time: float = dataclasses.field(default=6.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x20651830, original_name='MinNavigationTime'
        ),
    })
    max_navigation_time: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x617227b6, original_name='MaxNavigationTime'
        ),
    })
    unknown_0x32dd1ed4: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x32dd1ed4, original_name='Unknown'
        ),
    })
    unknown_0x4ba741d5: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4ba741d5, original_name='Unknown'
        ),
    })
    unknown_0x1eebf378: float = dataclasses.field(default=13.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1eebf378, original_name='Unknown'
        ),
    })
    melee_weapon: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x4a426bb3, original_name='MeleeWeapon'
        ),
    })
    melee_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xc9416034, original_name='MeleeDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    radial_melee_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x5f11893b, original_name='RadialMeleeDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    min_throw_projectile_time: float = dataclasses.field(default=7.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x587fa387, original_name='MinThrowProjectileTime'
        ),
    })
    max_throw_projectile_time: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3e9ac5f3, original_name='MaxThrowProjectileTime'
        ),
    })
    thrown_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2697e437, original_name='ThrownProjectile'
        ),
    })
    thrown_projectile_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xac187fa7, original_name='ThrownProjectileDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    thrown_projectile_visor_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x76af083e, original_name='ThrownProjectileVisorEffect'
        ),
    })
    thrown_projectile_visor_impact_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x723a9398, original_name='ThrownProjectileVisorImpactSound'
        ),
    })
    energy_wave_chance: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x79bc753e, original_name='EnergyWaveChance'
        ),
    })
    unknown_0x61f74274: int = dataclasses.field(default=2, metadata={
        'reflection': FieldReflection[int](
            int, id=0x61f74274, original_name='Unknown'
        ),
    })
    min_energy_wave_jump_dist: float = dataclasses.field(default=12.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x51a1ae4d, original_name='MinEnergyWaveJumpDist'
        ),
    })
    max_energy_wave_jump_dist: float = dataclasses.field(default=18.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb2fc1097, original_name='MaxEnergyWaveJumpDist'
        ),
    })
    min_energy_wave_attack_time: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd89e391a, original_name='MinEnergyWaveAttackTime'
        ),
    })
    max_energy_wave_attack_time: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8f906959, original_name='MaxEnergyWaveAttackTime'
        ),
    })
    energy_wave_jump_apex: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb281f490, original_name='EnergyWaveJumpApex'
        ),
    })
    min_energy_wave_attack_dist: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8b354dc6, original_name='MinEnergyWaveAttackDist'
        ),
    })
    energy_wave_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x76c64459, original_name='EnergyWaveProjectile'
        ),
    })
    energy_wave_projectile_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x37ed6ebb, original_name='EnergyWaveProjectileDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    grapple_attack_chance: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd20cecf7, original_name='GrappleAttackChance'
        ),
    })
    min_grapple_attack_dist: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x24c6cdcf, original_name='MinGrappleAttackDist'
        ),
    })
    max_grapple_attack_dist: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1a730547, original_name='MaxGrappleAttackDist'
        ),
    })
    grapple_connect_dist: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2684b001, original_name='GrappleConnectDist'
        ),
    })
    grapple_offset: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.4000000059604645, z=-1.600000023841858), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0xb49d657d, original_name='GrappleOffset', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    grapple_turn_speed: float = dataclasses.field(default=180.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf4d1c792, original_name='GrappleTurnSpeed'
        ),
    })
    min_grapple_attack_time: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x776db913, original_name='MinGrappleAttackTime'
        ),
    })
    max_grapple_attack_time: float = dataclasses.field(default=7.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x49d8719b, original_name='MaxGrappleAttackTime'
        ),
    })
    grapple_mount_jump_apex: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xec97cdbb, original_name='GrappleMountJumpApex'
        ),
    })
    grapple_dismount_jump_apex: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6d5796ef, original_name='GrappleDismountJumpApex'
        ),
    })
    grapple_connected_visor_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x98e19187, original_name='GrappleConnectedVisorEffect'
        ),
    })
    grapple_damage_visor_effect_left: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['ELSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x323f59c3, original_name='GrappleDamageVisorEffectLeft'
        ),
    })
    grapple_damage_visor_effect_right: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['ELSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe4f90605, original_name='GrappleDamageVisorEffectRight'
        ),
    })
    grapple_condensation_visor_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x96805afd, original_name='GrappleCondensationVisorEffect'
        ),
    })
    grapple_pull_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x89e7495b, original_name='GrapplePullDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    grapple_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x2ce7520f, original_name='GrappleDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    grapple_shake_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x58066c47, original_name='GrappleShakeSound'
        ),
    })
    min_grapple_shake_volume: float = dataclasses.field(default=0.75, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc2b3754e, original_name='MinGrappleShakeVolume'
        ),
    })
    max_grapple_shake_volume: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x21eecb94, original_name='MaxGrappleShakeVolume'
        ),
    })
    unknown_0xb5fdc280: float = dataclasses.field(default=2.6666998863220215, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb5fdc280, original_name='Unknown'
        ),
    })
    unknown_0x41d8c39c: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x41d8c39c, original_name='Unknown'
        ),
    })
    chakram: GandraydaChakram = dataclasses.field(default_factory=GandraydaChakram, metadata={
        'reflection': FieldReflection[GandraydaChakram](
            GandraydaChakram, id=0xaf8984b2, original_name='Chakram', from_json=GandraydaChakram.from_json, to_json=GandraydaChakram.to_json
        ),
    })
    stage1_data: GandraydaStage1Data = dataclasses.field(default_factory=GandraydaStage1Data, metadata={
        'reflection': FieldReflection[GandraydaStage1Data](
            GandraydaStage1Data, id=0xdcb5b112, original_name='Stage1Data', from_json=GandraydaStage1Data.from_json, to_json=GandraydaStage1Data.to_json
        ),
    })
    stage2_data: GandraydaStage2Data = dataclasses.field(default_factory=GandraydaStage2Data, metadata={
        'reflection': FieldReflection[GandraydaStage2Data](
            GandraydaStage2Data, id=0xc30b62ea, original_name='Stage2Data', from_json=GandraydaStage2Data.from_json, to_json=GandraydaStage2Data.to_json
        ),
    })
    stage3_data: GandraydaStage3Data = dataclasses.field(default_factory=GandraydaStage3Data, metadata={
        'reflection': FieldReflection[GandraydaStage3Data](
            GandraydaStage3Data, id=0x7f4e2e7d, original_name='Stage3Data', from_json=GandraydaStage3Data.from_json, to_json=GandraydaStage3Data.to_json
        ),
    })
    stage4_data: GandraydaStage4Data = dataclasses.field(default_factory=GandraydaStage4Data, metadata={
        'reflection': FieldReflection[GandraydaStage4Data](
            GandraydaStage4Data, id=0xfc76c51a, original_name='Stage4Data', from_json=GandraydaStage4Data.from_json, to_json=GandraydaStage4Data.to_json
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
        if property_count != 54:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x538d71cb
        unknown_0x538d71cb = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd42bba88
        unknown_0xd42bba88 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf4b9c6c3
        unknown_0xf4b9c6c3 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4d4d934b
        unknown_0x4d4d934b = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x20651830
        min_navigation_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x617227b6
        max_navigation_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32dd1ed4
        unknown_0x32dd1ed4 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4ba741d5
        unknown_0x4ba741d5 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1eebf378
        unknown_0x1eebf378 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4a426bb3
        melee_weapon = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc9416034
        melee_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5f11893b
        radial_melee_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x587fa387
        min_throw_projectile_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3e9ac5f3
        max_throw_projectile_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2697e437
        thrown_projectile = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xac187fa7
        thrown_projectile_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76af083e
        thrown_projectile_visor_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x723a9398
        thrown_projectile_visor_impact_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x79bc753e
        energy_wave_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x61f74274
        unknown_0x61f74274 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x51a1ae4d
        min_energy_wave_jump_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb2fc1097
        max_energy_wave_jump_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd89e391a
        min_energy_wave_attack_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8f906959
        max_energy_wave_attack_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb281f490
        energy_wave_jump_apex = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8b354dc6
        min_energy_wave_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76c64459
        energy_wave_projectile = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x37ed6ebb
        energy_wave_projectile_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd20cecf7
        grapple_attack_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24c6cdcf
        min_grapple_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1a730547
        max_grapple_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2684b001
        grapple_connect_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb49d657d
        grapple_offset = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf4d1c792
        grapple_turn_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x776db913
        min_grapple_attack_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49d8719b
        max_grapple_attack_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xec97cdbb
        grapple_mount_jump_apex = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6d5796ef
        grapple_dismount_jump_apex = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x98e19187
        grapple_connected_visor_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x323f59c3
        grapple_damage_visor_effect_left = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe4f90605
        grapple_damage_visor_effect_right = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x96805afd
        grapple_condensation_visor_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x89e7495b
        grapple_pull_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2ce7520f
        grapple_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58066c47
        grapple_shake_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc2b3754e
        min_grapple_shake_volume = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21eecb94
        max_grapple_shake_volume = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb5fdc280
        unknown_0xb5fdc280 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x41d8c39c
        unknown_0x41d8c39c = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaf8984b2
        chakram = GandraydaChakram.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdcb5b112
        stage1_data = GandraydaStage1Data.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc30b62ea
        stage2_data = GandraydaStage2Data.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7f4e2e7d
        stage3_data = GandraydaStage3Data.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfc76c51a
        stage4_data = GandraydaStage4Data.from_stream(data, game, property_size)
    
        return cls(unknown_0x538d71cb, unknown_0xd42bba88, unknown_0xf4b9c6c3, unknown_0x4d4d934b, min_navigation_time, max_navigation_time, unknown_0x32dd1ed4, unknown_0x4ba741d5, unknown_0x1eebf378, melee_weapon, melee_damage, radial_melee_damage, min_throw_projectile_time, max_throw_projectile_time, thrown_projectile, thrown_projectile_damage, thrown_projectile_visor_effect, thrown_projectile_visor_impact_sound, energy_wave_chance, unknown_0x61f74274, min_energy_wave_jump_dist, max_energy_wave_jump_dist, min_energy_wave_attack_time, max_energy_wave_attack_time, energy_wave_jump_apex, min_energy_wave_attack_dist, energy_wave_projectile, energy_wave_projectile_damage, grapple_attack_chance, min_grapple_attack_dist, max_grapple_attack_dist, grapple_connect_dist, grapple_offset, grapple_turn_speed, min_grapple_attack_time, max_grapple_attack_time, grapple_mount_jump_apex, grapple_dismount_jump_apex, grapple_connected_visor_effect, grapple_damage_visor_effect_left, grapple_damage_visor_effect_right, grapple_condensation_visor_effect, grapple_pull_damage, grapple_damage, grapple_shake_sound, min_grapple_shake_volume, max_grapple_shake_volume, unknown_0xb5fdc280, unknown_0x41d8c39c, chakram, stage1_data, stage2_data, stage3_data, stage4_data)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x006')  # 54 properties

        data.write(b'S\x8dq\xcb')  # 0x538d71cb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x538d71cb))

        data.write(b'\xd4+\xba\x88')  # 0xd42bba88
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd42bba88))

        data.write(b'\xf4\xb9\xc6\xc3')  # 0xf4b9c6c3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf4b9c6c3))

        data.write(b'MM\x93K')  # 0x4d4d934b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4d4d934b))

        data.write(b' e\x180')  # 0x20651830
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_navigation_time))

        data.write(b"ar'\xb6")  # 0x617227b6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_navigation_time))

        data.write(b'2\xdd\x1e\xd4')  # 0x32dd1ed4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x32dd1ed4))

        data.write(b'K\xa7A\xd5')  # 0x4ba741d5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4ba741d5))

        data.write(b'\x1e\xeb\xf3x')  # 0x1eebf378
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1eebf378))

        data.write(b'JBk\xb3')  # 0x4a426bb3
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.melee_weapon))

        data.write(b'\xc9A`4')  # 0xc9416034
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.melee_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'_\x11\x89;')  # 0x5f11893b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.radial_melee_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'X\x7f\xa3\x87')  # 0x587fa387
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_throw_projectile_time))

        data.write(b'>\x9a\xc5\xf3')  # 0x3e9ac5f3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_throw_projectile_time))

        data.write(b'&\x97\xe47')  # 0x2697e437
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.thrown_projectile))

        data.write(b'\xac\x18\x7f\xa7')  # 0xac187fa7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.thrown_projectile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'v\xaf\x08>')  # 0x76af083e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.thrown_projectile_visor_effect))

        data.write(b'r:\x93\x98')  # 0x723a9398
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.thrown_projectile_visor_impact_sound))

        data.write(b'y\xbcu>')  # 0x79bc753e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.energy_wave_chance))

        data.write(b'a\xf7Bt')  # 0x61f74274
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x61f74274))

        data.write(b'Q\xa1\xaeM')  # 0x51a1ae4d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_energy_wave_jump_dist))

        data.write(b'\xb2\xfc\x10\x97')  # 0xb2fc1097
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_energy_wave_jump_dist))

        data.write(b'\xd8\x9e9\x1a')  # 0xd89e391a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_energy_wave_attack_time))

        data.write(b'\x8f\x90iY')  # 0x8f906959
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_energy_wave_attack_time))

        data.write(b'\xb2\x81\xf4\x90')  # 0xb281f490
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.energy_wave_jump_apex))

        data.write(b'\x8b5M\xc6')  # 0x8b354dc6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_energy_wave_attack_dist))

        data.write(b'v\xc6DY')  # 0x76c64459
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.energy_wave_projectile))

        data.write(b'7\xedn\xbb')  # 0x37ed6ebb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.energy_wave_projectile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd2\x0c\xec\xf7')  # 0xd20cecf7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grapple_attack_chance))

        data.write(b'$\xc6\xcd\xcf')  # 0x24c6cdcf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_grapple_attack_dist))

        data.write(b'\x1as\x05G')  # 0x1a730547
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_grapple_attack_dist))

        data.write(b'&\x84\xb0\x01')  # 0x2684b001
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grapple_connect_dist))

        data.write(b'\xb4\x9de}')  # 0xb49d657d
        data.write(b'\x00\x0c')  # size
        self.grapple_offset.to_stream(data, game)

        data.write(b'\xf4\xd1\xc7\x92')  # 0xf4d1c792
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grapple_turn_speed))

        data.write(b'wm\xb9\x13')  # 0x776db913
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_grapple_attack_time))

        data.write(b'I\xd8q\x9b')  # 0x49d8719b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_grapple_attack_time))

        data.write(b'\xec\x97\xcd\xbb')  # 0xec97cdbb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grapple_mount_jump_apex))

        data.write(b'mW\x96\xef')  # 0x6d5796ef
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grapple_dismount_jump_apex))

        data.write(b'\x98\xe1\x91\x87')  # 0x98e19187
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.grapple_connected_visor_effect))

        data.write(b'2?Y\xc3')  # 0x323f59c3
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.grapple_damage_visor_effect_left))

        data.write(b'\xe4\xf9\x06\x05')  # 0xe4f90605
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.grapple_damage_visor_effect_right))

        data.write(b'\x96\x80Z\xfd')  # 0x96805afd
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.grapple_condensation_visor_effect))

        data.write(b'\x89\xe7I[')  # 0x89e7495b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grapple_pull_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b',\xe7R\x0f')  # 0x2ce7520f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grapple_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'X\x06lG')  # 0x58066c47
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.grapple_shake_sound))

        data.write(b'\xc2\xb3uN')  # 0xc2b3754e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_grapple_shake_volume))

        data.write(b'!\xee\xcb\x94')  # 0x21eecb94
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_grapple_shake_volume))

        data.write(b'\xb5\xfd\xc2\x80')  # 0xb5fdc280
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb5fdc280))

        data.write(b'A\xd8\xc3\x9c')  # 0x41d8c39c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x41d8c39c))

        data.write(b'\xaf\x89\x84\xb2')  # 0xaf8984b2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.chakram.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xdc\xb5\xb1\x12')  # 0xdcb5b112
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stage1_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc3\x0bb\xea')  # 0xc30b62ea
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stage2_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x7fN.}')  # 0x7f4e2e7d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stage3_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfcv\xc5\x1a')  # 0xfc76c51a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stage4_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GandraydaDataJson", data)
        return cls(
            unknown_0x538d71cb=json_data['unknown_0x538d71cb'],
            unknown_0xd42bba88=json_data['unknown_0xd42bba88'],
            unknown_0xf4b9c6c3=json_data['unknown_0xf4b9c6c3'],
            unknown_0x4d4d934b=json_data['unknown_0x4d4d934b'],
            min_navigation_time=json_data['min_navigation_time'],
            max_navigation_time=json_data['max_navigation_time'],
            unknown_0x32dd1ed4=json_data['unknown_0x32dd1ed4'],
            unknown_0x4ba741d5=json_data['unknown_0x4ba741d5'],
            unknown_0x1eebf378=json_data['unknown_0x1eebf378'],
            melee_weapon=json_data['melee_weapon'],
            melee_damage=DamageInfo.from_json(json_data['melee_damage']),
            radial_melee_damage=DamageInfo.from_json(json_data['radial_melee_damage']),
            min_throw_projectile_time=json_data['min_throw_projectile_time'],
            max_throw_projectile_time=json_data['max_throw_projectile_time'],
            thrown_projectile=json_data['thrown_projectile'],
            thrown_projectile_damage=DamageInfo.from_json(json_data['thrown_projectile_damage']),
            thrown_projectile_visor_effect=json_data['thrown_projectile_visor_effect'],
            thrown_projectile_visor_impact_sound=json_data['thrown_projectile_visor_impact_sound'],
            energy_wave_chance=json_data['energy_wave_chance'],
            unknown_0x61f74274=json_data['unknown_0x61f74274'],
            min_energy_wave_jump_dist=json_data['min_energy_wave_jump_dist'],
            max_energy_wave_jump_dist=json_data['max_energy_wave_jump_dist'],
            min_energy_wave_attack_time=json_data['min_energy_wave_attack_time'],
            max_energy_wave_attack_time=json_data['max_energy_wave_attack_time'],
            energy_wave_jump_apex=json_data['energy_wave_jump_apex'],
            min_energy_wave_attack_dist=json_data['min_energy_wave_attack_dist'],
            energy_wave_projectile=json_data['energy_wave_projectile'],
            energy_wave_projectile_damage=DamageInfo.from_json(json_data['energy_wave_projectile_damage']),
            grapple_attack_chance=json_data['grapple_attack_chance'],
            min_grapple_attack_dist=json_data['min_grapple_attack_dist'],
            max_grapple_attack_dist=json_data['max_grapple_attack_dist'],
            grapple_connect_dist=json_data['grapple_connect_dist'],
            grapple_offset=Vector.from_json(json_data['grapple_offset']),
            grapple_turn_speed=json_data['grapple_turn_speed'],
            min_grapple_attack_time=json_data['min_grapple_attack_time'],
            max_grapple_attack_time=json_data['max_grapple_attack_time'],
            grapple_mount_jump_apex=json_data['grapple_mount_jump_apex'],
            grapple_dismount_jump_apex=json_data['grapple_dismount_jump_apex'],
            grapple_connected_visor_effect=json_data['grapple_connected_visor_effect'],
            grapple_damage_visor_effect_left=json_data['grapple_damage_visor_effect_left'],
            grapple_damage_visor_effect_right=json_data['grapple_damage_visor_effect_right'],
            grapple_condensation_visor_effect=json_data['grapple_condensation_visor_effect'],
            grapple_pull_damage=DamageInfo.from_json(json_data['grapple_pull_damage']),
            grapple_damage=DamageInfo.from_json(json_data['grapple_damage']),
            grapple_shake_sound=json_data['grapple_shake_sound'],
            min_grapple_shake_volume=json_data['min_grapple_shake_volume'],
            max_grapple_shake_volume=json_data['max_grapple_shake_volume'],
            unknown_0xb5fdc280=json_data['unknown_0xb5fdc280'],
            unknown_0x41d8c39c=json_data['unknown_0x41d8c39c'],
            chakram=GandraydaChakram.from_json(json_data['chakram']),
            stage1_data=GandraydaStage1Data.from_json(json_data['stage1_data']),
            stage2_data=GandraydaStage2Data.from_json(json_data['stage2_data']),
            stage3_data=GandraydaStage3Data.from_json(json_data['stage3_data']),
            stage4_data=GandraydaStage4Data.from_json(json_data['stage4_data']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'unknown_0x538d71cb': self.unknown_0x538d71cb,
            'unknown_0xd42bba88': self.unknown_0xd42bba88,
            'unknown_0xf4b9c6c3': self.unknown_0xf4b9c6c3,
            'unknown_0x4d4d934b': self.unknown_0x4d4d934b,
            'min_navigation_time': self.min_navigation_time,
            'max_navigation_time': self.max_navigation_time,
            'unknown_0x32dd1ed4': self.unknown_0x32dd1ed4,
            'unknown_0x4ba741d5': self.unknown_0x4ba741d5,
            'unknown_0x1eebf378': self.unknown_0x1eebf378,
            'melee_weapon': self.melee_weapon,
            'melee_damage': self.melee_damage.to_json(),
            'radial_melee_damage': self.radial_melee_damage.to_json(),
            'min_throw_projectile_time': self.min_throw_projectile_time,
            'max_throw_projectile_time': self.max_throw_projectile_time,
            'thrown_projectile': self.thrown_projectile,
            'thrown_projectile_damage': self.thrown_projectile_damage.to_json(),
            'thrown_projectile_visor_effect': self.thrown_projectile_visor_effect,
            'thrown_projectile_visor_impact_sound': self.thrown_projectile_visor_impact_sound,
            'energy_wave_chance': self.energy_wave_chance,
            'unknown_0x61f74274': self.unknown_0x61f74274,
            'min_energy_wave_jump_dist': self.min_energy_wave_jump_dist,
            'max_energy_wave_jump_dist': self.max_energy_wave_jump_dist,
            'min_energy_wave_attack_time': self.min_energy_wave_attack_time,
            'max_energy_wave_attack_time': self.max_energy_wave_attack_time,
            'energy_wave_jump_apex': self.energy_wave_jump_apex,
            'min_energy_wave_attack_dist': self.min_energy_wave_attack_dist,
            'energy_wave_projectile': self.energy_wave_projectile,
            'energy_wave_projectile_damage': self.energy_wave_projectile_damage.to_json(),
            'grapple_attack_chance': self.grapple_attack_chance,
            'min_grapple_attack_dist': self.min_grapple_attack_dist,
            'max_grapple_attack_dist': self.max_grapple_attack_dist,
            'grapple_connect_dist': self.grapple_connect_dist,
            'grapple_offset': self.grapple_offset.to_json(),
            'grapple_turn_speed': self.grapple_turn_speed,
            'min_grapple_attack_time': self.min_grapple_attack_time,
            'max_grapple_attack_time': self.max_grapple_attack_time,
            'grapple_mount_jump_apex': self.grapple_mount_jump_apex,
            'grapple_dismount_jump_apex': self.grapple_dismount_jump_apex,
            'grapple_connected_visor_effect': self.grapple_connected_visor_effect,
            'grapple_damage_visor_effect_left': self.grapple_damage_visor_effect_left,
            'grapple_damage_visor_effect_right': self.grapple_damage_visor_effect_right,
            'grapple_condensation_visor_effect': self.grapple_condensation_visor_effect,
            'grapple_pull_damage': self.grapple_pull_damage.to_json(),
            'grapple_damage': self.grapple_damage.to_json(),
            'grapple_shake_sound': self.grapple_shake_sound,
            'min_grapple_shake_volume': self.min_grapple_shake_volume,
            'max_grapple_shake_volume': self.max_grapple_shake_volume,
            'unknown_0xb5fdc280': self.unknown_0xb5fdc280,
            'unknown_0x41d8c39c': self.unknown_0x41d8c39c,
            'chakram': self.chakram.to_json(),
            'stage1_data': self.stage1_data.to_json(),
            'stage2_data': self.stage2_data.to_json(),
            'stage3_data': self.stage3_data.to_json(),
            'stage4_data': self.stage4_data.to_json(),
        }

    def _dependencies_for_melee_weapon(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.melee_weapon)

    def _dependencies_for_thrown_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.thrown_projectile)

    def _dependencies_for_thrown_projectile_visor_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.thrown_projectile_visor_effect)

    def _dependencies_for_thrown_projectile_visor_impact_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.thrown_projectile_visor_impact_sound)

    def _dependencies_for_energy_wave_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.energy_wave_projectile)

    def _dependencies_for_grapple_connected_visor_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grapple_connected_visor_effect)

    def _dependencies_for_grapple_damage_visor_effect_left(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grapple_damage_visor_effect_left)

    def _dependencies_for_grapple_damage_visor_effect_right(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grapple_damage_visor_effect_right)

    def _dependencies_for_grapple_condensation_visor_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grapple_condensation_visor_effect)

    def _dependencies_for_grapple_shake_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grapple_shake_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_melee_weapon, "melee_weapon", "AssetId"),
            (self._dependencies_for_thrown_projectile, "thrown_projectile", "AssetId"),
            (self._dependencies_for_thrown_projectile_visor_effect, "thrown_projectile_visor_effect", "AssetId"),
            (self._dependencies_for_thrown_projectile_visor_impact_sound, "thrown_projectile_visor_impact_sound", "AssetId"),
            (self._dependencies_for_energy_wave_projectile, "energy_wave_projectile", "AssetId"),
            (self._dependencies_for_grapple_connected_visor_effect, "grapple_connected_visor_effect", "AssetId"),
            (self._dependencies_for_grapple_damage_visor_effect_left, "grapple_damage_visor_effect_left", "AssetId"),
            (self._dependencies_for_grapple_damage_visor_effect_right, "grapple_damage_visor_effect_right", "AssetId"),
            (self._dependencies_for_grapple_condensation_visor_effect, "grapple_condensation_visor_effect", "AssetId"),
            (self._dependencies_for_grapple_shake_sound, "grapple_shake_sound", "AssetId"),
            (self.chakram.dependencies_for, "chakram", "GandraydaChakram"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for GandraydaData.{field_name} ({field_type}): {e}"
                )


def _decode_melee_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_radial_melee_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_thrown_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_energy_wave_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_grapple_offset(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_grapple_pull_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_grapple_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_chakram(data: typing.BinaryIO, game: Game, property_size: int) -> GandraydaChakram:
    return GandraydaChakram.from_stream(data, game, property_size)


def _decode_stage1_data(data: typing.BinaryIO, game: Game, property_size: int) -> GandraydaStage1Data:
    return GandraydaStage1Data.from_stream(data, game, property_size)


def _decode_stage2_data(data: typing.BinaryIO, game: Game, property_size: int) -> GandraydaStage2Data:
    return GandraydaStage2Data.from_stream(data, game, property_size)


def _decode_stage3_data(data: typing.BinaryIO, game: Game, property_size: int) -> GandraydaStage3Data:
    return GandraydaStage3Data.from_stream(data, game, property_size)


def _decode_stage4_data(data: typing.BinaryIO, game: Game, property_size: int) -> GandraydaStage4Data:
    return GandraydaStage4Data.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x538d71cb: ('unknown_0x538d71cb', structs.decode_BIG_f),
    0xd42bba88: ('unknown_0xd42bba88', structs.decode_BIG_f),
    0xf4b9c6c3: ('unknown_0xf4b9c6c3', structs.decode_BIG_f),
    0x4d4d934b: ('unknown_0x4d4d934b', structs.decode_BIG_f),
    0x20651830: ('min_navigation_time', structs.decode_BIG_f),
    0x617227b6: ('max_navigation_time', structs.decode_BIG_f),
    0x32dd1ed4: ('unknown_0x32dd1ed4', structs.decode_BIG_f),
    0x4ba741d5: ('unknown_0x4ba741d5', structs.decode_BIG_f),
    0x1eebf378: ('unknown_0x1eebf378', structs.decode_BIG_f),
    0x4a426bb3: ('melee_weapon', structs.decode_BIG_Q),
    0xc9416034: ('melee_damage', _decode_melee_damage),
    0x5f11893b: ('radial_melee_damage', _decode_radial_melee_damage),
    0x587fa387: ('min_throw_projectile_time', structs.decode_BIG_f),
    0x3e9ac5f3: ('max_throw_projectile_time', structs.decode_BIG_f),
    0x2697e437: ('thrown_projectile', structs.decode_BIG_Q),
    0xac187fa7: ('thrown_projectile_damage', _decode_thrown_projectile_damage),
    0x76af083e: ('thrown_projectile_visor_effect', structs.decode_BIG_Q),
    0x723a9398: ('thrown_projectile_visor_impact_sound', structs.decode_BIG_Q),
    0x79bc753e: ('energy_wave_chance', structs.decode_BIG_f),
    0x61f74274: ('unknown_0x61f74274', structs.decode_BIG_l),
    0x51a1ae4d: ('min_energy_wave_jump_dist', structs.decode_BIG_f),
    0xb2fc1097: ('max_energy_wave_jump_dist', structs.decode_BIG_f),
    0xd89e391a: ('min_energy_wave_attack_time', structs.decode_BIG_f),
    0x8f906959: ('max_energy_wave_attack_time', structs.decode_BIG_f),
    0xb281f490: ('energy_wave_jump_apex', structs.decode_BIG_f),
    0x8b354dc6: ('min_energy_wave_attack_dist', structs.decode_BIG_f),
    0x76c64459: ('energy_wave_projectile', structs.decode_BIG_Q),
    0x37ed6ebb: ('energy_wave_projectile_damage', _decode_energy_wave_projectile_damage),
    0xd20cecf7: ('grapple_attack_chance', structs.decode_BIG_f),
    0x24c6cdcf: ('min_grapple_attack_dist', structs.decode_BIG_f),
    0x1a730547: ('max_grapple_attack_dist', structs.decode_BIG_f),
    0x2684b001: ('grapple_connect_dist', structs.decode_BIG_f),
    0xb49d657d: ('grapple_offset', _decode_grapple_offset),
    0xf4d1c792: ('grapple_turn_speed', structs.decode_BIG_f),
    0x776db913: ('min_grapple_attack_time', structs.decode_BIG_f),
    0x49d8719b: ('max_grapple_attack_time', structs.decode_BIG_f),
    0xec97cdbb: ('grapple_mount_jump_apex', structs.decode_BIG_f),
    0x6d5796ef: ('grapple_dismount_jump_apex', structs.decode_BIG_f),
    0x98e19187: ('grapple_connected_visor_effect', structs.decode_BIG_Q),
    0x323f59c3: ('grapple_damage_visor_effect_left', structs.decode_BIG_Q),
    0xe4f90605: ('grapple_damage_visor_effect_right', structs.decode_BIG_Q),
    0x96805afd: ('grapple_condensation_visor_effect', structs.decode_BIG_Q),
    0x89e7495b: ('grapple_pull_damage', _decode_grapple_pull_damage),
    0x2ce7520f: ('grapple_damage', _decode_grapple_damage),
    0x58066c47: ('grapple_shake_sound', structs.decode_BIG_Q),
    0xc2b3754e: ('min_grapple_shake_volume', structs.decode_BIG_f),
    0x21eecb94: ('max_grapple_shake_volume', structs.decode_BIG_f),
    0xb5fdc280: ('unknown_0xb5fdc280', structs.decode_BIG_f),
    0x41d8c39c: ('unknown_0x41d8c39c', structs.decode_BIG_f),
    0xaf8984b2: ('chakram', _decode_chakram),
    0xdcb5b112: ('stage1_data', _decode_stage1_data),
    0xc30b62ea: ('stage2_data', _decode_stage2_data),
    0x7f4e2e7d: ('stage3_data', _decode_stage3_data),
    0xfc76c51a: ('stage4_data', _decode_stage4_data),
}
