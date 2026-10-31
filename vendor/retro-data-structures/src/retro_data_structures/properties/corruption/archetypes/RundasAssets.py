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
from retro_data_structures.properties.corruption.archetypes.GrappleData import GrappleData
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class RundasAssetsJson(typing_extensions.TypedDict):
        ice_armor_back: int
        ice_armor_head: int
        ice_armor_l_ankle: int
        ice_armor_r_ankle: int
        ice_armor_l_collar: int
        ice_armor_r_collar: int
        ice_armor_l_knee: int
        ice_armor_r_knee: int
        ice_armor_l_thigh: int
        ice_armor_r_thigh: int
        part_0x199a4ca5: int
        part_0x9f0e3e0b: int
        part_0x5452edae: int
        part_0x4957dd16: int
        part_0xa13303f4: int
        ice_grenade_projectile1: int
        ice_grenade_projectile2: int
        ice_grenade_projectile3: int
        ice_grenade_projectile4: int
        wpsc: int
        shard_storm_visor_texture: int
        shard_storm_visor_frost_explosion: int
        morning_star_ice_chunk_model: int
        morning_star_shatter: int
        missile_frozen_model: int
        frozen_missile_shatter: int
        missile_freeze_effect: int
        ice_spike_explosion: int
        ice_platform_explosion: int
        surfing_particles: int
        part_0x96b50d90: int
        surfing_projectile: int
        surfing_projectile_visor_effect: int
        surfing_projectile_visor_impact_sound: int
        max_grapple_distance: float
        grapple_data: json_util.JsonObject
        sound_shard_storm_visor: int
        sound_morning_star_shatter: int
        scan_when_stunned: int
        scan_when_no_armor: int
    

@dataclasses.dataclass()
class RundasAssets(BaseProperty):
    ice_armor_back: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x1a662787, original_name='IceArmorBack'
        ),
    })
    ice_armor_head: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x6dcb001f, original_name='IceArmorHead'
        ),
    })
    ice_armor_l_ankle: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xac0b1ea5, original_name='IceArmorLAnkle'
        ),
    })
    ice_armor_r_ankle: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x508bf168, original_name='IceArmorRAnkle'
        ),
    })
    ice_armor_l_collar: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x02e83a7c, original_name='IceArmorLCollar'
        ),
    })
    ice_armor_r_collar: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe7c1049e, original_name='IceArmorRCollar'
        ),
    })
    ice_armor_l_knee: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2c41e9a5, original_name='IceArmorLKnee'
        ),
    })
    ice_armor_r_knee: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x152658fe, original_name='IceArmorRKnee'
        ),
    })
    ice_armor_l_thigh: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe22a6dda, original_name='IceArmorLThigh'
        ),
    })
    ice_armor_r_thigh: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x1eaa8217, original_name='IceArmorRThigh'
        ),
    })
    part_0x199a4ca5: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x199a4ca5, original_name='PART'
        ),
    })
    part_0x9f0e3e0b: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x9f0e3e0b, original_name='PART'
        ),
    })
    part_0x5452edae: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5452edae, original_name='PART'
        ),
    })
    part_0x4957dd16: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x4957dd16, original_name='PART'
        ),
    })
    part_0xa13303f4: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa13303f4, original_name='PART'
        ),
    })
    ice_grenade_projectile1: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3a2d1aa4, original_name='IceGrenadeProjectile1'
        ),
    })
    ice_grenade_projectile2: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xbcb9680a, original_name='IceGrenadeProjectile2'
        ),
    })
    ice_grenade_projectile3: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x77e5bbaf, original_name='IceGrenadeProjectile3'
        ),
    })
    ice_grenade_projectile4: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x6ae08b17, original_name='IceGrenadeProjectile4'
        ),
    })
    wpsc: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x4584843b, original_name='WPSC'
        ),
    })
    shard_storm_visor_texture: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['TXTR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x03304d0b, original_name='ShardStormVisorTexture'
        ),
    })
    shard_storm_visor_frost_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc017cf42, original_name='ShardStormVisorFrostExplosion'
        ),
    })
    morning_star_ice_chunk_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x17789d1c, original_name='MorningStarIceChunkModel'
        ),
    })
    morning_star_shatter: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x8843ce6d, original_name='MorningStarShatter'
        ),
    })
    missile_frozen_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe039c4bd, original_name='MissileFrozenModel'
        ),
    })
    frozen_missile_shatter: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x09c8db87, original_name='FrozenMissileShatter'
        ),
    })
    missile_freeze_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xcbb55845, original_name='MissileFreezeEffect'
        ),
    })
    ice_spike_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xedccf9f6, original_name='IceSpikeExplosion'
        ),
    })
    ice_platform_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x9873172a, original_name='IcePlatformExplosion'
        ),
    })
    surfing_particles: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x84c33da6, original_name='SurfingParticles'
        ),
    })
    part_0x96b50d90: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x96b50d90, original_name='PART'
        ),
    })
    surfing_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x757060d4, original_name='SurfingProjectile'
        ),
    })
    surfing_projectile_visor_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa2687ce4, original_name='SurfingProjectileVisorEffect'
        ),
    })
    surfing_projectile_visor_impact_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x24964375, original_name='SurfingProjectileVisorImpactSound'
        ),
    })
    max_grapple_distance: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1cc93984, original_name='MaxGrappleDistance'
        ),
    })
    grapple_data: GrappleData = dataclasses.field(default_factory=GrappleData, metadata={
        'reflection': FieldReflection[GrappleData](
            GrappleData, id=0xf609c637, original_name='GrappleData', from_json=GrappleData.from_json, to_json=GrappleData.to_json
        ),
    })
    sound_shard_storm_visor: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xaf284f76, original_name='Sound_ShardStormVisor'
        ),
    })
    sound_morning_star_shatter: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd2b71804, original_name='Sound_MorningStarShatter'
        ),
    })
    scan_when_stunned: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SCAN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xf69bed49, original_name='ScanWhenStunned'
        ),
    })
    scan_when_no_armor: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SCAN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3d6768d8, original_name='ScanWhenNoArmor'
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
        if property_count != 40:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1a662787
        ice_armor_back = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6dcb001f
        ice_armor_head = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xac0b1ea5
        ice_armor_l_ankle = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x508bf168
        ice_armor_r_ankle = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x02e83a7c
        ice_armor_l_collar = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe7c1049e
        ice_armor_r_collar = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2c41e9a5
        ice_armor_l_knee = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x152658fe
        ice_armor_r_knee = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe22a6dda
        ice_armor_l_thigh = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1eaa8217
        ice_armor_r_thigh = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x199a4ca5
        part_0x199a4ca5 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9f0e3e0b
        part_0x9f0e3e0b = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5452edae
        part_0x5452edae = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4957dd16
        part_0x4957dd16 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa13303f4
        part_0xa13303f4 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3a2d1aa4
        ice_grenade_projectile1 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbcb9680a
        ice_grenade_projectile2 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77e5bbaf
        ice_grenade_projectile3 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6ae08b17
        ice_grenade_projectile4 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4584843b
        wpsc = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03304d0b
        shard_storm_visor_texture = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc017cf42
        shard_storm_visor_frost_explosion = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x17789d1c
        morning_star_ice_chunk_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8843ce6d
        morning_star_shatter = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe039c4bd
        missile_frozen_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x09c8db87
        frozen_missile_shatter = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcbb55845
        missile_freeze_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xedccf9f6
        ice_spike_explosion = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9873172a
        ice_platform_explosion = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x84c33da6
        surfing_particles = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x96b50d90
        part_0x96b50d90 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x757060d4
        surfing_projectile = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa2687ce4
        surfing_projectile_visor_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24964375
        surfing_projectile_visor_impact_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1cc93984
        max_grapple_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf609c637
        grapple_data = GrappleData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaf284f76
        sound_shard_storm_visor = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd2b71804
        sound_morning_star_shatter = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf69bed49
        scan_when_stunned = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3d6768d8
        scan_when_no_armor = structs.BIG_Q.unpack(data.read(8))[0]
    
        return cls(ice_armor_back, ice_armor_head, ice_armor_l_ankle, ice_armor_r_ankle, ice_armor_l_collar, ice_armor_r_collar, ice_armor_l_knee, ice_armor_r_knee, ice_armor_l_thigh, ice_armor_r_thigh, part_0x199a4ca5, part_0x9f0e3e0b, part_0x5452edae, part_0x4957dd16, part_0xa13303f4, ice_grenade_projectile1, ice_grenade_projectile2, ice_grenade_projectile3, ice_grenade_projectile4, wpsc, shard_storm_visor_texture, shard_storm_visor_frost_explosion, morning_star_ice_chunk_model, morning_star_shatter, missile_frozen_model, frozen_missile_shatter, missile_freeze_effect, ice_spike_explosion, ice_platform_explosion, surfing_particles, part_0x96b50d90, surfing_projectile, surfing_projectile_visor_effect, surfing_projectile_visor_impact_sound, max_grapple_distance, grapple_data, sound_shard_storm_visor, sound_morning_star_shatter, scan_when_stunned, scan_when_no_armor)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00(')  # 40 properties

        data.write(b"\x1af'\x87")  # 0x1a662787
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ice_armor_back))

        data.write(b'm\xcb\x00\x1f')  # 0x6dcb001f
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ice_armor_head))

        data.write(b'\xac\x0b\x1e\xa5')  # 0xac0b1ea5
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ice_armor_l_ankle))

        data.write(b'P\x8b\xf1h')  # 0x508bf168
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ice_armor_r_ankle))

        data.write(b'\x02\xe8:|')  # 0x2e83a7c
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ice_armor_l_collar))

        data.write(b'\xe7\xc1\x04\x9e')  # 0xe7c1049e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ice_armor_r_collar))

        data.write(b',A\xe9\xa5')  # 0x2c41e9a5
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ice_armor_l_knee))

        data.write(b'\x15&X\xfe')  # 0x152658fe
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ice_armor_r_knee))

        data.write(b'\xe2*m\xda')  # 0xe22a6dda
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ice_armor_l_thigh))

        data.write(b'\x1e\xaa\x82\x17')  # 0x1eaa8217
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ice_armor_r_thigh))

        data.write(b'\x19\x9aL\xa5')  # 0x199a4ca5
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.part_0x199a4ca5))

        data.write(b'\x9f\x0e>\x0b')  # 0x9f0e3e0b
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.part_0x9f0e3e0b))

        data.write(b'TR\xed\xae')  # 0x5452edae
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.part_0x5452edae))

        data.write(b'IW\xdd\x16')  # 0x4957dd16
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.part_0x4957dd16))

        data.write(b'\xa13\x03\xf4')  # 0xa13303f4
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.part_0xa13303f4))

        data.write(b':-\x1a\xa4')  # 0x3a2d1aa4
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ice_grenade_projectile1))

        data.write(b'\xbc\xb9h\n')  # 0xbcb9680a
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ice_grenade_projectile2))

        data.write(b'w\xe5\xbb\xaf')  # 0x77e5bbaf
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ice_grenade_projectile3))

        data.write(b'j\xe0\x8b\x17')  # 0x6ae08b17
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ice_grenade_projectile4))

        data.write(b'E\x84\x84;')  # 0x4584843b
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.wpsc))

        data.write(b'\x030M\x0b')  # 0x3304d0b
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shard_storm_visor_texture))

        data.write(b'\xc0\x17\xcfB')  # 0xc017cf42
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shard_storm_visor_frost_explosion))

        data.write(b'\x17x\x9d\x1c')  # 0x17789d1c
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.morning_star_ice_chunk_model))

        data.write(b'\x88C\xcem')  # 0x8843ce6d
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.morning_star_shatter))

        data.write(b'\xe09\xc4\xbd')  # 0xe039c4bd
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.missile_frozen_model))

        data.write(b'\t\xc8\xdb\x87')  # 0x9c8db87
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.frozen_missile_shatter))

        data.write(b'\xcb\xb5XE')  # 0xcbb55845
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.missile_freeze_effect))

        data.write(b'\xed\xcc\xf9\xf6')  # 0xedccf9f6
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ice_spike_explosion))

        data.write(b'\x98s\x17*')  # 0x9873172a
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ice_platform_explosion))

        data.write(b'\x84\xc3=\xa6')  # 0x84c33da6
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.surfing_particles))

        data.write(b'\x96\xb5\r\x90')  # 0x96b50d90
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.part_0x96b50d90))

        data.write(b'up`\xd4')  # 0x757060d4
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.surfing_projectile))

        data.write(b'\xa2h|\xe4')  # 0xa2687ce4
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.surfing_projectile_visor_effect))

        data.write(b'$\x96Cu')  # 0x24964375
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.surfing_projectile_visor_impact_sound))

        data.write(b'\x1c\xc99\x84')  # 0x1cc93984
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_grapple_distance))

        data.write(b'\xf6\t\xc67')  # 0xf609c637
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grapple_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xaf(Ov')  # 0xaf284f76
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_shard_storm_visor))

        data.write(b'\xd2\xb7\x18\x04')  # 0xd2b71804
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_morning_star_shatter))

        data.write(b'\xf6\x9b\xedI')  # 0xf69bed49
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.scan_when_stunned))

        data.write(b'=gh\xd8')  # 0x3d6768d8
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.scan_when_no_armor))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("RundasAssetsJson", data)
        return cls(
            ice_armor_back=json_data['ice_armor_back'],
            ice_armor_head=json_data['ice_armor_head'],
            ice_armor_l_ankle=json_data['ice_armor_l_ankle'],
            ice_armor_r_ankle=json_data['ice_armor_r_ankle'],
            ice_armor_l_collar=json_data['ice_armor_l_collar'],
            ice_armor_r_collar=json_data['ice_armor_r_collar'],
            ice_armor_l_knee=json_data['ice_armor_l_knee'],
            ice_armor_r_knee=json_data['ice_armor_r_knee'],
            ice_armor_l_thigh=json_data['ice_armor_l_thigh'],
            ice_armor_r_thigh=json_data['ice_armor_r_thigh'],
            part_0x199a4ca5=json_data['part_0x199a4ca5'],
            part_0x9f0e3e0b=json_data['part_0x9f0e3e0b'],
            part_0x5452edae=json_data['part_0x5452edae'],
            part_0x4957dd16=json_data['part_0x4957dd16'],
            part_0xa13303f4=json_data['part_0xa13303f4'],
            ice_grenade_projectile1=json_data['ice_grenade_projectile1'],
            ice_grenade_projectile2=json_data['ice_grenade_projectile2'],
            ice_grenade_projectile3=json_data['ice_grenade_projectile3'],
            ice_grenade_projectile4=json_data['ice_grenade_projectile4'],
            wpsc=json_data['wpsc'],
            shard_storm_visor_texture=json_data['shard_storm_visor_texture'],
            shard_storm_visor_frost_explosion=json_data['shard_storm_visor_frost_explosion'],
            morning_star_ice_chunk_model=json_data['morning_star_ice_chunk_model'],
            morning_star_shatter=json_data['morning_star_shatter'],
            missile_frozen_model=json_data['missile_frozen_model'],
            frozen_missile_shatter=json_data['frozen_missile_shatter'],
            missile_freeze_effect=json_data['missile_freeze_effect'],
            ice_spike_explosion=json_data['ice_spike_explosion'],
            ice_platform_explosion=json_data['ice_platform_explosion'],
            surfing_particles=json_data['surfing_particles'],
            part_0x96b50d90=json_data['part_0x96b50d90'],
            surfing_projectile=json_data['surfing_projectile'],
            surfing_projectile_visor_effect=json_data['surfing_projectile_visor_effect'],
            surfing_projectile_visor_impact_sound=json_data['surfing_projectile_visor_impact_sound'],
            max_grapple_distance=json_data['max_grapple_distance'],
            grapple_data=GrappleData.from_json(json_data['grapple_data']),
            sound_shard_storm_visor=json_data['sound_shard_storm_visor'],
            sound_morning_star_shatter=json_data['sound_morning_star_shatter'],
            scan_when_stunned=json_data['scan_when_stunned'],
            scan_when_no_armor=json_data['scan_when_no_armor'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'ice_armor_back': self.ice_armor_back,
            'ice_armor_head': self.ice_armor_head,
            'ice_armor_l_ankle': self.ice_armor_l_ankle,
            'ice_armor_r_ankle': self.ice_armor_r_ankle,
            'ice_armor_l_collar': self.ice_armor_l_collar,
            'ice_armor_r_collar': self.ice_armor_r_collar,
            'ice_armor_l_knee': self.ice_armor_l_knee,
            'ice_armor_r_knee': self.ice_armor_r_knee,
            'ice_armor_l_thigh': self.ice_armor_l_thigh,
            'ice_armor_r_thigh': self.ice_armor_r_thigh,
            'part_0x199a4ca5': self.part_0x199a4ca5,
            'part_0x9f0e3e0b': self.part_0x9f0e3e0b,
            'part_0x5452edae': self.part_0x5452edae,
            'part_0x4957dd16': self.part_0x4957dd16,
            'part_0xa13303f4': self.part_0xa13303f4,
            'ice_grenade_projectile1': self.ice_grenade_projectile1,
            'ice_grenade_projectile2': self.ice_grenade_projectile2,
            'ice_grenade_projectile3': self.ice_grenade_projectile3,
            'ice_grenade_projectile4': self.ice_grenade_projectile4,
            'wpsc': self.wpsc,
            'shard_storm_visor_texture': self.shard_storm_visor_texture,
            'shard_storm_visor_frost_explosion': self.shard_storm_visor_frost_explosion,
            'morning_star_ice_chunk_model': self.morning_star_ice_chunk_model,
            'morning_star_shatter': self.morning_star_shatter,
            'missile_frozen_model': self.missile_frozen_model,
            'frozen_missile_shatter': self.frozen_missile_shatter,
            'missile_freeze_effect': self.missile_freeze_effect,
            'ice_spike_explosion': self.ice_spike_explosion,
            'ice_platform_explosion': self.ice_platform_explosion,
            'surfing_particles': self.surfing_particles,
            'part_0x96b50d90': self.part_0x96b50d90,
            'surfing_projectile': self.surfing_projectile,
            'surfing_projectile_visor_effect': self.surfing_projectile_visor_effect,
            'surfing_projectile_visor_impact_sound': self.surfing_projectile_visor_impact_sound,
            'max_grapple_distance': self.max_grapple_distance,
            'grapple_data': self.grapple_data.to_json(),
            'sound_shard_storm_visor': self.sound_shard_storm_visor,
            'sound_morning_star_shatter': self.sound_morning_star_shatter,
            'scan_when_stunned': self.scan_when_stunned,
            'scan_when_no_armor': self.scan_when_no_armor,
        }

    def _dependencies_for_ice_armor_back(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ice_armor_back)

    def _dependencies_for_ice_armor_head(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ice_armor_head)

    def _dependencies_for_ice_armor_l_ankle(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ice_armor_l_ankle)

    def _dependencies_for_ice_armor_r_ankle(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ice_armor_r_ankle)

    def _dependencies_for_ice_armor_l_collar(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ice_armor_l_collar)

    def _dependencies_for_ice_armor_r_collar(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ice_armor_r_collar)

    def _dependencies_for_ice_armor_l_knee(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ice_armor_l_knee)

    def _dependencies_for_ice_armor_r_knee(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ice_armor_r_knee)

    def _dependencies_for_ice_armor_l_thigh(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ice_armor_l_thigh)

    def _dependencies_for_ice_armor_r_thigh(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ice_armor_r_thigh)

    def _dependencies_for_part_0x199a4ca5(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0x199a4ca5)

    def _dependencies_for_part_0x9f0e3e0b(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0x9f0e3e0b)

    def _dependencies_for_part_0x5452edae(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0x5452edae)

    def _dependencies_for_part_0x4957dd16(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0x4957dd16)

    def _dependencies_for_part_0xa13303f4(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0xa13303f4)

    def _dependencies_for_ice_grenade_projectile1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ice_grenade_projectile1)

    def _dependencies_for_ice_grenade_projectile2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ice_grenade_projectile2)

    def _dependencies_for_ice_grenade_projectile3(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ice_grenade_projectile3)

    def _dependencies_for_ice_grenade_projectile4(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ice_grenade_projectile4)

    def _dependencies_for_wpsc(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wpsc)

    def _dependencies_for_shard_storm_visor_texture(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shard_storm_visor_texture)

    def _dependencies_for_shard_storm_visor_frost_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shard_storm_visor_frost_explosion)

    def _dependencies_for_morning_star_ice_chunk_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.morning_star_ice_chunk_model)

    def _dependencies_for_morning_star_shatter(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.morning_star_shatter)

    def _dependencies_for_missile_frozen_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.missile_frozen_model)

    def _dependencies_for_frozen_missile_shatter(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.frozen_missile_shatter)

    def _dependencies_for_missile_freeze_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.missile_freeze_effect)

    def _dependencies_for_ice_spike_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ice_spike_explosion)

    def _dependencies_for_ice_platform_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ice_platform_explosion)

    def _dependencies_for_surfing_particles(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.surfing_particles)

    def _dependencies_for_part_0x96b50d90(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0x96b50d90)

    def _dependencies_for_surfing_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.surfing_projectile)

    def _dependencies_for_surfing_projectile_visor_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.surfing_projectile_visor_effect)

    def _dependencies_for_surfing_projectile_visor_impact_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.surfing_projectile_visor_impact_sound)

    def _dependencies_for_sound_shard_storm_visor(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_shard_storm_visor)

    def _dependencies_for_sound_morning_star_shatter(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_morning_star_shatter)

    def _dependencies_for_scan_when_stunned(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scan_when_stunned)

    def _dependencies_for_scan_when_no_armor(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scan_when_no_armor)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_ice_armor_back, "ice_armor_back", "AssetId"),
            (self._dependencies_for_ice_armor_head, "ice_armor_head", "AssetId"),
            (self._dependencies_for_ice_armor_l_ankle, "ice_armor_l_ankle", "AssetId"),
            (self._dependencies_for_ice_armor_r_ankle, "ice_armor_r_ankle", "AssetId"),
            (self._dependencies_for_ice_armor_l_collar, "ice_armor_l_collar", "AssetId"),
            (self._dependencies_for_ice_armor_r_collar, "ice_armor_r_collar", "AssetId"),
            (self._dependencies_for_ice_armor_l_knee, "ice_armor_l_knee", "AssetId"),
            (self._dependencies_for_ice_armor_r_knee, "ice_armor_r_knee", "AssetId"),
            (self._dependencies_for_ice_armor_l_thigh, "ice_armor_l_thigh", "AssetId"),
            (self._dependencies_for_ice_armor_r_thigh, "ice_armor_r_thigh", "AssetId"),
            (self._dependencies_for_part_0x199a4ca5, "part_0x199a4ca5", "AssetId"),
            (self._dependencies_for_part_0x9f0e3e0b, "part_0x9f0e3e0b", "AssetId"),
            (self._dependencies_for_part_0x5452edae, "part_0x5452edae", "AssetId"),
            (self._dependencies_for_part_0x4957dd16, "part_0x4957dd16", "AssetId"),
            (self._dependencies_for_part_0xa13303f4, "part_0xa13303f4", "AssetId"),
            (self._dependencies_for_ice_grenade_projectile1, "ice_grenade_projectile1", "AssetId"),
            (self._dependencies_for_ice_grenade_projectile2, "ice_grenade_projectile2", "AssetId"),
            (self._dependencies_for_ice_grenade_projectile3, "ice_grenade_projectile3", "AssetId"),
            (self._dependencies_for_ice_grenade_projectile4, "ice_grenade_projectile4", "AssetId"),
            (self._dependencies_for_wpsc, "wpsc", "AssetId"),
            (self._dependencies_for_shard_storm_visor_texture, "shard_storm_visor_texture", "AssetId"),
            (self._dependencies_for_shard_storm_visor_frost_explosion, "shard_storm_visor_frost_explosion", "AssetId"),
            (self._dependencies_for_morning_star_ice_chunk_model, "morning_star_ice_chunk_model", "AssetId"),
            (self._dependencies_for_morning_star_shatter, "morning_star_shatter", "AssetId"),
            (self._dependencies_for_missile_frozen_model, "missile_frozen_model", "AssetId"),
            (self._dependencies_for_frozen_missile_shatter, "frozen_missile_shatter", "AssetId"),
            (self._dependencies_for_missile_freeze_effect, "missile_freeze_effect", "AssetId"),
            (self._dependencies_for_ice_spike_explosion, "ice_spike_explosion", "AssetId"),
            (self._dependencies_for_ice_platform_explosion, "ice_platform_explosion", "AssetId"),
            (self._dependencies_for_surfing_particles, "surfing_particles", "AssetId"),
            (self._dependencies_for_part_0x96b50d90, "part_0x96b50d90", "AssetId"),
            (self._dependencies_for_surfing_projectile, "surfing_projectile", "AssetId"),
            (self._dependencies_for_surfing_projectile_visor_effect, "surfing_projectile_visor_effect", "AssetId"),
            (self._dependencies_for_surfing_projectile_visor_impact_sound, "surfing_projectile_visor_impact_sound", "AssetId"),
            (self.grapple_data.dependencies_for, "grapple_data", "GrappleData"),
            (self._dependencies_for_sound_shard_storm_visor, "sound_shard_storm_visor", "AssetId"),
            (self._dependencies_for_sound_morning_star_shatter, "sound_morning_star_shatter", "AssetId"),
            (self._dependencies_for_scan_when_stunned, "scan_when_stunned", "AssetId"),
            (self._dependencies_for_scan_when_no_armor, "scan_when_no_armor", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for RundasAssets.{field_name} ({field_type}): {e}"
                )


def _decode_grapple_data(data: typing.BinaryIO, game: Game, property_size: int) -> GrappleData:
    return GrappleData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x1a662787: ('ice_armor_back', structs.decode_BIG_Q),
    0x6dcb001f: ('ice_armor_head', structs.decode_BIG_Q),
    0xac0b1ea5: ('ice_armor_l_ankle', structs.decode_BIG_Q),
    0x508bf168: ('ice_armor_r_ankle', structs.decode_BIG_Q),
    0x02e83a7c: ('ice_armor_l_collar', structs.decode_BIG_Q),
    0xe7c1049e: ('ice_armor_r_collar', structs.decode_BIG_Q),
    0x2c41e9a5: ('ice_armor_l_knee', structs.decode_BIG_Q),
    0x152658fe: ('ice_armor_r_knee', structs.decode_BIG_Q),
    0xe22a6dda: ('ice_armor_l_thigh', structs.decode_BIG_Q),
    0x1eaa8217: ('ice_armor_r_thigh', structs.decode_BIG_Q),
    0x199a4ca5: ('part_0x199a4ca5', structs.decode_BIG_Q),
    0x9f0e3e0b: ('part_0x9f0e3e0b', structs.decode_BIG_Q),
    0x5452edae: ('part_0x5452edae', structs.decode_BIG_Q),
    0x4957dd16: ('part_0x4957dd16', structs.decode_BIG_Q),
    0xa13303f4: ('part_0xa13303f4', structs.decode_BIG_Q),
    0x3a2d1aa4: ('ice_grenade_projectile1', structs.decode_BIG_Q),
    0xbcb9680a: ('ice_grenade_projectile2', structs.decode_BIG_Q),
    0x77e5bbaf: ('ice_grenade_projectile3', structs.decode_BIG_Q),
    0x6ae08b17: ('ice_grenade_projectile4', structs.decode_BIG_Q),
    0x4584843b: ('wpsc', structs.decode_BIG_Q),
    0x03304d0b: ('shard_storm_visor_texture', structs.decode_BIG_Q),
    0xc017cf42: ('shard_storm_visor_frost_explosion', structs.decode_BIG_Q),
    0x17789d1c: ('morning_star_ice_chunk_model', structs.decode_BIG_Q),
    0x8843ce6d: ('morning_star_shatter', structs.decode_BIG_Q),
    0xe039c4bd: ('missile_frozen_model', structs.decode_BIG_Q),
    0x09c8db87: ('frozen_missile_shatter', structs.decode_BIG_Q),
    0xcbb55845: ('missile_freeze_effect', structs.decode_BIG_Q),
    0xedccf9f6: ('ice_spike_explosion', structs.decode_BIG_Q),
    0x9873172a: ('ice_platform_explosion', structs.decode_BIG_Q),
    0x84c33da6: ('surfing_particles', structs.decode_BIG_Q),
    0x96b50d90: ('part_0x96b50d90', structs.decode_BIG_Q),
    0x757060d4: ('surfing_projectile', structs.decode_BIG_Q),
    0xa2687ce4: ('surfing_projectile_visor_effect', structs.decode_BIG_Q),
    0x24964375: ('surfing_projectile_visor_impact_sound', structs.decode_BIG_Q),
    0x1cc93984: ('max_grapple_distance', structs.decode_BIG_f),
    0xf609c637: ('grapple_data', _decode_grapple_data),
    0xaf284f76: ('sound_shard_storm_visor', structs.decode_BIG_Q),
    0xd2b71804: ('sound_morning_star_shatter', structs.decode_BIG_Q),
    0xf69bed49: ('scan_when_stunned', structs.decode_BIG_Q),
    0x3d6768d8: ('scan_when_no_armor', structs.decode_BIG_Q),
}
