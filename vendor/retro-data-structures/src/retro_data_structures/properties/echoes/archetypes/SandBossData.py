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
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.SandBossArmorData import SandBossArmorData
from retro_data_structures.properties.echoes.archetypes.SandBossMultiWormAttackData import SandBossMultiWormAttackData
from retro_data_structures.properties.echoes.archetypes.SandBossStampedeData import SandBossStampedeData
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SandBossDataJson(typing_extensions.TypedDict):
        scannable_info1: int
        command_index: int
        cracked_sphere1: int
        cracked_sphere2: int
        cracked_sphere3: int
        snap_jaw_damage: json_util.JsonObject
        spit_out_damage: json_util.JsonObject
        min_dark_beam_attack_time: float
        dark_beam_attack_time_variance: float
        dark_beam_projectile: int
        dark_beam_damage: json_util.JsonObject
        unknown_0x2b42dddf: float
        unknown_0x1562e0d6: float
        head_armor_hp: float
        suck_air_time: float
        suck_morphball_range: float
        spit_morphball_time: float
        head_armor_explosion: int
        stampede_properties: json_util.JsonObject
        multi_worm_properties: json_util.JsonObject
        attached_armor: json_util.JsonObject
        stampede_armor: json_util.JsonObject
        with_tail_armor_model: int
        with_tail_armor_skin_rules: int
        damage_vulnerability: json_util.JsonObject
        stampede_vulnerability: json_util.JsonObject
        suck_air_vulnerability: json_util.JsonObject
    

@dataclasses.dataclass()
class SandBossData(BaseProperty):
    scannable_info1: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SCAN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x72124842, original_name='ScannableInfo1'
        ),
    })
    command_index: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xe34d7c49, original_name='CommandIndex'
        ),
    })
    cracked_sphere1: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe47262f5, original_name='CrackedSphere1'
        ),
    })
    cracked_sphere2: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x62e6105b, original_name='CrackedSphere2'
        ),
    })
    cracked_sphere3: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa9bac3fe, original_name='CrackedSphere3'
        ),
    })
    snap_jaw_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x19c91aaa, original_name='SnapJawDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    spit_out_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x58889364, original_name='SpitOutDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    min_dark_beam_attack_time: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbf88fe4f, original_name='MinDarkBeamAttackTime'
        ),
    })
    dark_beam_attack_time_variance: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x74c702b3, original_name='DarkBeamAttackTimeVariance'
        ),
    })
    dark_beam_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x35ee175d, original_name='DarkBeamProjectile'
        ),
    })
    dark_beam_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x94c2150f, original_name='DarkBeamDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    unknown_0x2b42dddf: float = dataclasses.field(default=90.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2b42dddf, original_name='Unknown'
        ),
    })
    unknown_0x1562e0d6: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1562e0d6, original_name='Unknown'
        ),
    })
    head_armor_hp: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd0db2574, original_name='HeadArmorHP'
        ),
    })
    suck_air_time: float = dataclasses.field(default=7.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf1aed43d, original_name='SuckAirTime'
        ),
    })
    suck_morphball_range: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3055dd0e, original_name='SuckMorphballRange'
        ),
    })
    spit_morphball_time: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6f135965, original_name='SpitMorphballTime'
        ),
    })
    head_armor_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc49086d9, original_name='HeadArmorExplosion'
        ),
    })
    stampede_properties: SandBossStampedeData = dataclasses.field(default_factory=SandBossStampedeData, metadata={
        'reflection': FieldReflection[SandBossStampedeData](
            SandBossStampedeData, id=0x95371a32, original_name='StampedeProperties', from_json=SandBossStampedeData.from_json, to_json=SandBossStampedeData.to_json
        ),
    })
    multi_worm_properties: SandBossMultiWormAttackData = dataclasses.field(default_factory=SandBossMultiWormAttackData, metadata={
        'reflection': FieldReflection[SandBossMultiWormAttackData](
            SandBossMultiWormAttackData, id=0x7619e561, original_name='MultiWormProperties', from_json=SandBossMultiWormAttackData.from_json, to_json=SandBossMultiWormAttackData.to_json
        ),
    })
    attached_armor: SandBossArmorData = dataclasses.field(default_factory=SandBossArmorData, metadata={
        'reflection': FieldReflection[SandBossArmorData](
            SandBossArmorData, id=0x8b452a19, original_name='AttachedArmor', from_json=SandBossArmorData.from_json, to_json=SandBossArmorData.to_json
        ),
    })
    stampede_armor: SandBossArmorData = dataclasses.field(default_factory=SandBossArmorData, metadata={
        'reflection': FieldReflection[SandBossArmorData](
            SandBossArmorData, id=0x0cf8c54c, original_name='StampedeArmor', from_json=SandBossArmorData.from_json, to_json=SandBossArmorData.to_json
        ),
    })
    with_tail_armor_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xbbd84681, original_name='WithTailArmorModel'
        ),
    })
    with_tail_armor_skin_rules: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CSKR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xdf6da1a2, original_name='WithTailArmorSkinRules'
        ),
    })
    damage_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xb7ecdcf9, original_name='DamageVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    stampede_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x844ed79c, original_name='StampedeVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    suck_air_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x77210167, original_name='SuckAirVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
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
        if property_count != 27:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x72124842
        scannable_info1 = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe34d7c49
        command_index = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe47262f5
        cracked_sphere1 = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x62e6105b
        cracked_sphere2 = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa9bac3fe
        cracked_sphere3 = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19c91aaa
        snap_jaw_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58889364
        spit_out_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbf88fe4f
        min_dark_beam_attack_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x74c702b3
        dark_beam_attack_time_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x35ee175d
        dark_beam_projectile = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x94c2150f
        dark_beam_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 1, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2b42dddf
        unknown_0x2b42dddf = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1562e0d6
        unknown_0x1562e0d6 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd0db2574
        head_armor_hp = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf1aed43d
        suck_air_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3055dd0e
        suck_morphball_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6f135965
        spit_morphball_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc49086d9
        head_armor_explosion = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95371a32
        stampede_properties = SandBossStampedeData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7619e561
        multi_worm_properties = SandBossMultiWormAttackData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8b452a19
        attached_armor = SandBossArmorData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0cf8c54c
        stampede_armor = SandBossArmorData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbbd84681
        with_tail_armor_model = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdf6da1a2
        with_tail_armor_skin_rules = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb7ecdcf9
        damage_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x844ed79c
        stampede_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77210167
        suck_air_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        return cls(scannable_info1, command_index, cracked_sphere1, cracked_sphere2, cracked_sphere3, snap_jaw_damage, spit_out_damage, min_dark_beam_attack_time, dark_beam_attack_time_variance, dark_beam_projectile, dark_beam_damage, unknown_0x2b42dddf, unknown_0x1562e0d6, head_armor_hp, suck_air_time, suck_morphball_range, spit_morphball_time, head_armor_explosion, stampede_properties, multi_worm_properties, attached_armor, stampede_armor, with_tail_armor_model, with_tail_armor_skin_rules, damage_vulnerability, stampede_vulnerability, suck_air_vulnerability)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x1b')  # 27 properties

        data.write(b'r\x12HB')  # 0x72124842
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.scannable_info1))

        data.write(b'\xe3M|I')  # 0xe34d7c49
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.command_index))

        data.write(b'\xe4rb\xf5')  # 0xe47262f5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.cracked_sphere1))

        data.write(b'b\xe6\x10[')  # 0x62e6105b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.cracked_sphere2))

        data.write(b'\xa9\xba\xc3\xfe')  # 0xa9bac3fe
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.cracked_sphere3))

        data.write(b'\x19\xc9\x1a\xaa')  # 0x19c91aaa
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.snap_jaw_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'X\x88\x93d')  # 0x58889364
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.spit_out_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbf\x88\xfeO')  # 0xbf88fe4f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_dark_beam_attack_time))

        data.write(b't\xc7\x02\xb3')  # 0x74c702b3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dark_beam_attack_time_variance))

        data.write(b'5\xee\x17]')  # 0x35ee175d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.dark_beam_projectile))

        data.write(b'\x94\xc2\x15\x0f')  # 0x94c2150f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.dark_beam_damage.to_stream(data, game, default_override={'di_weapon_type': 1, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'+B\xdd\xdf')  # 0x2b42dddf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2b42dddf))

        data.write(b'\x15b\xe0\xd6')  # 0x1562e0d6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x1562e0d6))

        data.write(b'\xd0\xdb%t')  # 0xd0db2574
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.head_armor_hp))

        data.write(b'\xf1\xae\xd4=')  # 0xf1aed43d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.suck_air_time))

        data.write(b'0U\xdd\x0e')  # 0x3055dd0e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.suck_morphball_range))

        data.write(b'o\x13Ye')  # 0x6f135965
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.spit_morphball_time))

        data.write(b'\xc4\x90\x86\xd9')  # 0xc49086d9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.head_armor_explosion))

        data.write(b'\x957\x1a2')  # 0x95371a32
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stampede_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'v\x19\xe5a')  # 0x7619e561
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.multi_worm_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8bE*\x19')  # 0x8b452a19
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.attached_armor.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x0c\xf8\xc5L')  # 0xcf8c54c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stampede_armor.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbb\xd8F\x81')  # 0xbbd84681
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.with_tail_armor_model))

        data.write(b'\xdfm\xa1\xa2')  # 0xdf6da1a2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.with_tail_armor_skin_rules))

        data.write(b'\xb7\xec\xdc\xf9')  # 0xb7ecdcf9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x84N\xd7\x9c')  # 0x844ed79c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stampede_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'w!\x01g')  # 0x77210167
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.suck_air_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SandBossDataJson", data)
        return cls(
            scannable_info1=json_data['scannable_info1'],
            command_index=json_data['command_index'],
            cracked_sphere1=json_data['cracked_sphere1'],
            cracked_sphere2=json_data['cracked_sphere2'],
            cracked_sphere3=json_data['cracked_sphere3'],
            snap_jaw_damage=DamageInfo.from_json(json_data['snap_jaw_damage']),
            spit_out_damage=DamageInfo.from_json(json_data['spit_out_damage']),
            min_dark_beam_attack_time=json_data['min_dark_beam_attack_time'],
            dark_beam_attack_time_variance=json_data['dark_beam_attack_time_variance'],
            dark_beam_projectile=json_data['dark_beam_projectile'],
            dark_beam_damage=DamageInfo.from_json(json_data['dark_beam_damage']),
            unknown_0x2b42dddf=json_data['unknown_0x2b42dddf'],
            unknown_0x1562e0d6=json_data['unknown_0x1562e0d6'],
            head_armor_hp=json_data['head_armor_hp'],
            suck_air_time=json_data['suck_air_time'],
            suck_morphball_range=json_data['suck_morphball_range'],
            spit_morphball_time=json_data['spit_morphball_time'],
            head_armor_explosion=json_data['head_armor_explosion'],
            stampede_properties=SandBossStampedeData.from_json(json_data['stampede_properties']),
            multi_worm_properties=SandBossMultiWormAttackData.from_json(json_data['multi_worm_properties']),
            attached_armor=SandBossArmorData.from_json(json_data['attached_armor']),
            stampede_armor=SandBossArmorData.from_json(json_data['stampede_armor']),
            with_tail_armor_model=json_data['with_tail_armor_model'],
            with_tail_armor_skin_rules=json_data['with_tail_armor_skin_rules'],
            damage_vulnerability=DamageVulnerability.from_json(json_data['damage_vulnerability']),
            stampede_vulnerability=DamageVulnerability.from_json(json_data['stampede_vulnerability']),
            suck_air_vulnerability=DamageVulnerability.from_json(json_data['suck_air_vulnerability']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'scannable_info1': self.scannable_info1,
            'command_index': self.command_index,
            'cracked_sphere1': self.cracked_sphere1,
            'cracked_sphere2': self.cracked_sphere2,
            'cracked_sphere3': self.cracked_sphere3,
            'snap_jaw_damage': self.snap_jaw_damage.to_json(),
            'spit_out_damage': self.spit_out_damage.to_json(),
            'min_dark_beam_attack_time': self.min_dark_beam_attack_time,
            'dark_beam_attack_time_variance': self.dark_beam_attack_time_variance,
            'dark_beam_projectile': self.dark_beam_projectile,
            'dark_beam_damage': self.dark_beam_damage.to_json(),
            'unknown_0x2b42dddf': self.unknown_0x2b42dddf,
            'unknown_0x1562e0d6': self.unknown_0x1562e0d6,
            'head_armor_hp': self.head_armor_hp,
            'suck_air_time': self.suck_air_time,
            'suck_morphball_range': self.suck_morphball_range,
            'spit_morphball_time': self.spit_morphball_time,
            'head_armor_explosion': self.head_armor_explosion,
            'stampede_properties': self.stampede_properties.to_json(),
            'multi_worm_properties': self.multi_worm_properties.to_json(),
            'attached_armor': self.attached_armor.to_json(),
            'stampede_armor': self.stampede_armor.to_json(),
            'with_tail_armor_model': self.with_tail_armor_model,
            'with_tail_armor_skin_rules': self.with_tail_armor_skin_rules,
            'damage_vulnerability': self.damage_vulnerability.to_json(),
            'stampede_vulnerability': self.stampede_vulnerability.to_json(),
            'suck_air_vulnerability': self.suck_air_vulnerability.to_json(),
        }

    def _dependencies_for_scannable_info1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scannable_info1)

    def _dependencies_for_cracked_sphere1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.cracked_sphere1)

    def _dependencies_for_cracked_sphere2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.cracked_sphere2)

    def _dependencies_for_cracked_sphere3(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.cracked_sphere3)

    def _dependencies_for_dark_beam_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.dark_beam_projectile)

    def _dependencies_for_head_armor_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.head_armor_explosion)

    def _dependencies_for_with_tail_armor_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.with_tail_armor_model)

    def _dependencies_for_with_tail_armor_skin_rules(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.with_tail_armor_skin_rules)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_scannable_info1, "scannable_info1", "AssetId"),
            (self._dependencies_for_cracked_sphere1, "cracked_sphere1", "AssetId"),
            (self._dependencies_for_cracked_sphere2, "cracked_sphere2", "AssetId"),
            (self._dependencies_for_cracked_sphere3, "cracked_sphere3", "AssetId"),
            (self._dependencies_for_dark_beam_projectile, "dark_beam_projectile", "AssetId"),
            (self._dependencies_for_head_armor_explosion, "head_armor_explosion", "AssetId"),
            (self.stampede_properties.dependencies_for, "stampede_properties", "SandBossStampedeData"),
            (self.multi_worm_properties.dependencies_for, "multi_worm_properties", "SandBossMultiWormAttackData"),
            (self.attached_armor.dependencies_for, "attached_armor", "SandBossArmorData"),
            (self.stampede_armor.dependencies_for, "stampede_armor", "SandBossArmorData"),
            (self._dependencies_for_with_tail_armor_model, "with_tail_armor_model", "AssetId"),
            (self._dependencies_for_with_tail_armor_skin_rules, "with_tail_armor_skin_rules", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for SandBossData.{field_name} ({field_type}): {e}"
                )


def _decode_snap_jaw_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})


def _decode_spit_out_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})


def _decode_dark_beam_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 1, 'di_damage': 20.0, 'di_knock_back_power': 10.0})


def _decode_stampede_properties(data: typing.BinaryIO, game: Game, property_size: int) -> SandBossStampedeData:
    return SandBossStampedeData.from_stream(data, game, property_size)


def _decode_multi_worm_properties(data: typing.BinaryIO, game: Game, property_size: int) -> SandBossMultiWormAttackData:
    return SandBossMultiWormAttackData.from_stream(data, game, property_size)


def _decode_attached_armor(data: typing.BinaryIO, game: Game, property_size: int) -> SandBossArmorData:
    return SandBossArmorData.from_stream(data, game, property_size)


def _decode_stampede_armor(data: typing.BinaryIO, game: Game, property_size: int) -> SandBossArmorData:
    return SandBossArmorData.from_stream(data, game, property_size)


def _decode_damage_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_stampede_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_suck_air_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x72124842: ('scannable_info1', structs.decode_BIG_L),
    0xe34d7c49: ('command_index', structs.decode_BIG_l),
    0xe47262f5: ('cracked_sphere1', structs.decode_BIG_L),
    0x62e6105b: ('cracked_sphere2', structs.decode_BIG_L),
    0xa9bac3fe: ('cracked_sphere3', structs.decode_BIG_L),
    0x19c91aaa: ('snap_jaw_damage', _decode_snap_jaw_damage),
    0x58889364: ('spit_out_damage', _decode_spit_out_damage),
    0xbf88fe4f: ('min_dark_beam_attack_time', structs.decode_BIG_f),
    0x74c702b3: ('dark_beam_attack_time_variance', structs.decode_BIG_f),
    0x35ee175d: ('dark_beam_projectile', structs.decode_BIG_L),
    0x94c2150f: ('dark_beam_damage', _decode_dark_beam_damage),
    0x2b42dddf: ('unknown_0x2b42dddf', structs.decode_BIG_f),
    0x1562e0d6: ('unknown_0x1562e0d6', structs.decode_BIG_f),
    0xd0db2574: ('head_armor_hp', structs.decode_BIG_f),
    0xf1aed43d: ('suck_air_time', structs.decode_BIG_f),
    0x3055dd0e: ('suck_morphball_range', structs.decode_BIG_f),
    0x6f135965: ('spit_morphball_time', structs.decode_BIG_f),
    0xc49086d9: ('head_armor_explosion', structs.decode_BIG_L),
    0x95371a32: ('stampede_properties', _decode_stampede_properties),
    0x7619e561: ('multi_worm_properties', _decode_multi_worm_properties),
    0x8b452a19: ('attached_armor', _decode_attached_armor),
    0x0cf8c54c: ('stampede_armor', _decode_stampede_armor),
    0xbbd84681: ('with_tail_armor_model', structs.decode_BIG_L),
    0xdf6da1a2: ('with_tail_armor_skin_rules', structs.decode_BIG_L),
    0xb7ecdcf9: ('damage_vulnerability', _decode_damage_vulnerability),
    0x844ed79c: ('stampede_vulnerability', _decode_stampede_vulnerability),
    0x77210167: ('suck_air_vulnerability', _decode_suck_air_vulnerability),
}
