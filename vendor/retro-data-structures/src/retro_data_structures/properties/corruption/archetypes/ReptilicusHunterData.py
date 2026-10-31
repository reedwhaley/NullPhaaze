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
from retro_data_structures.properties.corruption.archetypes.ReptilicusHunterCattleProd import ReptilicusHunterCattleProd
from retro_data_structures.properties.corruption.archetypes.ReptilicusHunterChakram import ReptilicusHunterChakram
from retro_data_structures.properties.corruption.archetypes.ReptilicusHunterEnergyWhip import ReptilicusHunterEnergyWhip
from retro_data_structures.properties.corruption.archetypes.ReptilicusHunterHyperMode import ReptilicusHunterHyperMode
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class ReptilicusHunterDataJson(typing_extensions.TypedDict):
        use_defense_points: bool
        disable_terrain_alignment: bool
        disable_cloaking: bool
        is_initially_cloaked: bool
        min_visible_time: float
        max_visible_time: float
        force_visible_damage: float
        unknown_0xb7e53921: float
        unknown_0x5867275b: float
        cloak_time: float
        decloak_time: float
        cloak_sound: int
        decloak_sound: int
        unknown_0x221c7ec1: float
        unknown_0x41af5eeb: float
        hear_shot_radius: float
        cover_abort_time: float
        min_visible_cover_time: float
        max_visible_cover_time: float
        min_invisible_cover_time: float
        max_invisible_cover_time: float
        unknown_0xe6c24412: float
        heavy_hit_chance: float
        taunt_chance: float
        aggressiveness: float
        normal_hyper_mode: json_util.JsonObject
        hard_hyper_mode: json_util.JsonObject
        elite_hyper_mode: json_util.JsonObject
        cattle_prod: json_util.JsonObject
        energy_whip: json_util.JsonObject
        chakram: json_util.JsonObject
    

@dataclasses.dataclass()
class ReptilicusHunterData(BaseProperty):
    use_defense_points: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x217e944a, original_name='UseDefensePoints'
        ),
    })
    disable_terrain_alignment: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x0c81681a, original_name='DisableTerrainAlignment'
        ),
    })
    disable_cloaking: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xe9553ffa, original_name='DisableCloaking'
        ),
    })
    is_initially_cloaked: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x1c893f54, original_name='IsInitiallyCloaked'
        ),
    })
    min_visible_time: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x369d0874, original_name='MinVisibleTime'
        ),
    })
    max_visible_time: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x91a9880d, original_name='MaxVisibleTime'
        ),
    })
    force_visible_damage: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x11286bd3, original_name='ForceVisibleDamage'
        ),
    })
    unknown_0xb7e53921: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb7e53921, original_name='Unknown'
        ),
    })
    unknown_0x5867275b: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5867275b, original_name='Unknown'
        ),
    })
    cloak_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x388bc31f, original_name='CloakTime'
        ),
    })
    decloak_time: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4319c840, original_name='DecloakTime'
        ),
    })
    cloak_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x052bf617, original_name='CloakSound'
        ),
    })
    decloak_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xfe842879, original_name='DecloakSound'
        ),
    })
    unknown_0x221c7ec1: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x221c7ec1, original_name='Unknown'
        ),
    })
    unknown_0x41af5eeb: float = dataclasses.field(default=300.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x41af5eeb, original_name='Unknown'
        ),
    })
    hear_shot_radius: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0cf887f1, original_name='HearShotRadius'
        ),
    })
    cover_abort_time: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x18a9876b, original_name='CoverAbortTime'
        ),
    })
    min_visible_cover_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x164f8ca8, original_name='MinVisibleCoverTime'
        ),
    })
    max_visible_cover_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcdf0df4f, original_name='MaxVisibleCoverTime'
        ),
    })
    min_invisible_cover_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf77e2ae2, original_name='MinInvisibleCoverTime'
        ),
    })
    max_invisible_cover_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x14239438, original_name='MaxInvisibleCoverTime'
        ),
    })
    unknown_0xe6c24412: float = dataclasses.field(default=7.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe6c24412, original_name='Unknown'
        ),
    })
    heavy_hit_chance: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x583c1b1e, original_name='HeavyHitChance'
        ),
    })
    taunt_chance: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa77f6212, original_name='TauntChance'
        ),
    })
    aggressiveness: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9579b1f2, original_name='Aggressiveness'
        ),
    })
    normal_hyper_mode: ReptilicusHunterHyperMode = dataclasses.field(default_factory=ReptilicusHunterHyperMode, metadata={
        'reflection': FieldReflection[ReptilicusHunterHyperMode](
            ReptilicusHunterHyperMode, id=0x9c5e7d6f, original_name='NormalHyperMode', from_json=ReptilicusHunterHyperMode.from_json, to_json=ReptilicusHunterHyperMode.to_json
        ),
    })
    hard_hyper_mode: ReptilicusHunterHyperMode = dataclasses.field(default_factory=ReptilicusHunterHyperMode, metadata={
        'reflection': FieldReflection[ReptilicusHunterHyperMode](
            ReptilicusHunterHyperMode, id=0xaa2bee9a, original_name='HardHyperMode', from_json=ReptilicusHunterHyperMode.from_json, to_json=ReptilicusHunterHyperMode.to_json
        ),
    })
    elite_hyper_mode: ReptilicusHunterHyperMode = dataclasses.field(default_factory=ReptilicusHunterHyperMode, metadata={
        'reflection': FieldReflection[ReptilicusHunterHyperMode](
            ReptilicusHunterHyperMode, id=0xe27a4e87, original_name='EliteHyperMode', from_json=ReptilicusHunterHyperMode.from_json, to_json=ReptilicusHunterHyperMode.to_json
        ),
    })
    cattle_prod: ReptilicusHunterCattleProd = dataclasses.field(default_factory=ReptilicusHunterCattleProd, metadata={
        'reflection': FieldReflection[ReptilicusHunterCattleProd](
            ReptilicusHunterCattleProd, id=0x87b10a69, original_name='CattleProd', from_json=ReptilicusHunterCattleProd.from_json, to_json=ReptilicusHunterCattleProd.to_json
        ),
    })
    energy_whip: ReptilicusHunterEnergyWhip = dataclasses.field(default_factory=ReptilicusHunterEnergyWhip, metadata={
        'reflection': FieldReflection[ReptilicusHunterEnergyWhip](
            ReptilicusHunterEnergyWhip, id=0xd7548e97, original_name='EnergyWhip', from_json=ReptilicusHunterEnergyWhip.from_json, to_json=ReptilicusHunterEnergyWhip.to_json
        ),
    })
    chakram: ReptilicusHunterChakram = dataclasses.field(default_factory=ReptilicusHunterChakram, metadata={
        'reflection': FieldReflection[ReptilicusHunterChakram](
            ReptilicusHunterChakram, id=0x19a58c31, original_name='Chakram', from_json=ReptilicusHunterChakram.from_json, to_json=ReptilicusHunterChakram.to_json
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
        if property_count != 31:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x217e944a
        use_defense_points = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0c81681a
        disable_terrain_alignment = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe9553ffa
        disable_cloaking = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1c893f54
        is_initially_cloaked = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x369d0874
        min_visible_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x91a9880d
        max_visible_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x11286bd3
        force_visible_damage = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb7e53921
        unknown_0xb7e53921 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5867275b
        unknown_0x5867275b = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x388bc31f
        cloak_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4319c840
        decloak_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x052bf617
        cloak_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfe842879
        decloak_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x221c7ec1
        unknown_0x221c7ec1 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x41af5eeb
        unknown_0x41af5eeb = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0cf887f1
        hear_shot_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x18a9876b
        cover_abort_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x164f8ca8
        min_visible_cover_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcdf0df4f
        max_visible_cover_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf77e2ae2
        min_invisible_cover_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x14239438
        max_invisible_cover_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe6c24412
        unknown_0xe6c24412 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x583c1b1e
        heavy_hit_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa77f6212
        taunt_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9579b1f2
        aggressiveness = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9c5e7d6f
        normal_hyper_mode = ReptilicusHunterHyperMode.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaa2bee9a
        hard_hyper_mode = ReptilicusHunterHyperMode.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe27a4e87
        elite_hyper_mode = ReptilicusHunterHyperMode.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x87b10a69
        cattle_prod = ReptilicusHunterCattleProd.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd7548e97
        energy_whip = ReptilicusHunterEnergyWhip.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19a58c31
        chakram = ReptilicusHunterChakram.from_stream(data, game, property_size)
    
        return cls(use_defense_points, disable_terrain_alignment, disable_cloaking, is_initially_cloaked, min_visible_time, max_visible_time, force_visible_damage, unknown_0xb7e53921, unknown_0x5867275b, cloak_time, decloak_time, cloak_sound, decloak_sound, unknown_0x221c7ec1, unknown_0x41af5eeb, hear_shot_radius, cover_abort_time, min_visible_cover_time, max_visible_cover_time, min_invisible_cover_time, max_invisible_cover_time, unknown_0xe6c24412, heavy_hit_chance, taunt_chance, aggressiveness, normal_hyper_mode, hard_hyper_mode, elite_hyper_mode, cattle_prod, energy_whip, chakram)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x1f')  # 31 properties

        data.write(b'!~\x94J')  # 0x217e944a
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.use_defense_points))

        data.write(b'\x0c\x81h\x1a')  # 0xc81681a
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.disable_terrain_alignment))

        data.write(b'\xe9U?\xfa')  # 0xe9553ffa
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.disable_cloaking))

        data.write(b'\x1c\x89?T')  # 0x1c893f54
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_initially_cloaked))

        data.write(b'6\x9d\x08t')  # 0x369d0874
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_visible_time))

        data.write(b'\x91\xa9\x88\r')  # 0x91a9880d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_visible_time))

        data.write(b'\x11(k\xd3')  # 0x11286bd3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.force_visible_damage))

        data.write(b'\xb7\xe59!')  # 0xb7e53921
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb7e53921))

        data.write(b"Xg'[")  # 0x5867275b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5867275b))

        data.write(b'8\x8b\xc3\x1f')  # 0x388bc31f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.cloak_time))

        data.write(b'C\x19\xc8@')  # 0x4319c840
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.decloak_time))

        data.write(b'\x05+\xf6\x17')  # 0x52bf617
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.cloak_sound))

        data.write(b'\xfe\x84(y')  # 0xfe842879
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.decloak_sound))

        data.write(b'"\x1c~\xc1')  # 0x221c7ec1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x221c7ec1))

        data.write(b'A\xaf^\xeb')  # 0x41af5eeb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x41af5eeb))

        data.write(b'\x0c\xf8\x87\xf1')  # 0xcf887f1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hear_shot_radius))

        data.write(b'\x18\xa9\x87k')  # 0x18a9876b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.cover_abort_time))

        data.write(b'\x16O\x8c\xa8')  # 0x164f8ca8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_visible_cover_time))

        data.write(b'\xcd\xf0\xdfO')  # 0xcdf0df4f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_visible_cover_time))

        data.write(b'\xf7~*\xe2')  # 0xf77e2ae2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_invisible_cover_time))

        data.write(b'\x14#\x948')  # 0x14239438
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_invisible_cover_time))

        data.write(b'\xe6\xc2D\x12')  # 0xe6c24412
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe6c24412))

        data.write(b'X<\x1b\x1e')  # 0x583c1b1e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.heavy_hit_chance))

        data.write(b'\xa7\x7fb\x12')  # 0xa77f6212
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.taunt_chance))

        data.write(b'\x95y\xb1\xf2')  # 0x9579b1f2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aggressiveness))

        data.write(b'\x9c^}o')  # 0x9c5e7d6f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.normal_hyper_mode.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xaa+\xee\x9a')  # 0xaa2bee9a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hard_hyper_mode.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe2zN\x87')  # 0xe27a4e87
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.elite_hyper_mode.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x87\xb1\ni')  # 0x87b10a69
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.cattle_prod.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd7T\x8e\x97')  # 0xd7548e97
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.energy_whip.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x19\xa5\x8c1')  # 0x19a58c31
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.chakram.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ReptilicusHunterDataJson", data)
        return cls(
            use_defense_points=json_data['use_defense_points'],
            disable_terrain_alignment=json_data['disable_terrain_alignment'],
            disable_cloaking=json_data['disable_cloaking'],
            is_initially_cloaked=json_data['is_initially_cloaked'],
            min_visible_time=json_data['min_visible_time'],
            max_visible_time=json_data['max_visible_time'],
            force_visible_damage=json_data['force_visible_damage'],
            unknown_0xb7e53921=json_data['unknown_0xb7e53921'],
            unknown_0x5867275b=json_data['unknown_0x5867275b'],
            cloak_time=json_data['cloak_time'],
            decloak_time=json_data['decloak_time'],
            cloak_sound=json_data['cloak_sound'],
            decloak_sound=json_data['decloak_sound'],
            unknown_0x221c7ec1=json_data['unknown_0x221c7ec1'],
            unknown_0x41af5eeb=json_data['unknown_0x41af5eeb'],
            hear_shot_radius=json_data['hear_shot_radius'],
            cover_abort_time=json_data['cover_abort_time'],
            min_visible_cover_time=json_data['min_visible_cover_time'],
            max_visible_cover_time=json_data['max_visible_cover_time'],
            min_invisible_cover_time=json_data['min_invisible_cover_time'],
            max_invisible_cover_time=json_data['max_invisible_cover_time'],
            unknown_0xe6c24412=json_data['unknown_0xe6c24412'],
            heavy_hit_chance=json_data['heavy_hit_chance'],
            taunt_chance=json_data['taunt_chance'],
            aggressiveness=json_data['aggressiveness'],
            normal_hyper_mode=ReptilicusHunterHyperMode.from_json(json_data['normal_hyper_mode']),
            hard_hyper_mode=ReptilicusHunterHyperMode.from_json(json_data['hard_hyper_mode']),
            elite_hyper_mode=ReptilicusHunterHyperMode.from_json(json_data['elite_hyper_mode']),
            cattle_prod=ReptilicusHunterCattleProd.from_json(json_data['cattle_prod']),
            energy_whip=ReptilicusHunterEnergyWhip.from_json(json_data['energy_whip']),
            chakram=ReptilicusHunterChakram.from_json(json_data['chakram']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'use_defense_points': self.use_defense_points,
            'disable_terrain_alignment': self.disable_terrain_alignment,
            'disable_cloaking': self.disable_cloaking,
            'is_initially_cloaked': self.is_initially_cloaked,
            'min_visible_time': self.min_visible_time,
            'max_visible_time': self.max_visible_time,
            'force_visible_damage': self.force_visible_damage,
            'unknown_0xb7e53921': self.unknown_0xb7e53921,
            'unknown_0x5867275b': self.unknown_0x5867275b,
            'cloak_time': self.cloak_time,
            'decloak_time': self.decloak_time,
            'cloak_sound': self.cloak_sound,
            'decloak_sound': self.decloak_sound,
            'unknown_0x221c7ec1': self.unknown_0x221c7ec1,
            'unknown_0x41af5eeb': self.unknown_0x41af5eeb,
            'hear_shot_radius': self.hear_shot_radius,
            'cover_abort_time': self.cover_abort_time,
            'min_visible_cover_time': self.min_visible_cover_time,
            'max_visible_cover_time': self.max_visible_cover_time,
            'min_invisible_cover_time': self.min_invisible_cover_time,
            'max_invisible_cover_time': self.max_invisible_cover_time,
            'unknown_0xe6c24412': self.unknown_0xe6c24412,
            'heavy_hit_chance': self.heavy_hit_chance,
            'taunt_chance': self.taunt_chance,
            'aggressiveness': self.aggressiveness,
            'normal_hyper_mode': self.normal_hyper_mode.to_json(),
            'hard_hyper_mode': self.hard_hyper_mode.to_json(),
            'elite_hyper_mode': self.elite_hyper_mode.to_json(),
            'cattle_prod': self.cattle_prod.to_json(),
            'energy_whip': self.energy_whip.to_json(),
            'chakram': self.chakram.to_json(),
        }

    def _dependencies_for_cloak_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.cloak_sound)

    def _dependencies_for_decloak_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.decloak_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_cloak_sound, "cloak_sound", "AssetId"),
            (self._dependencies_for_decloak_sound, "decloak_sound", "AssetId"),
            (self.cattle_prod.dependencies_for, "cattle_prod", "ReptilicusHunterCattleProd"),
            (self.energy_whip.dependencies_for, "energy_whip", "ReptilicusHunterEnergyWhip"),
            (self.chakram.dependencies_for, "chakram", "ReptilicusHunterChakram"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for ReptilicusHunterData.{field_name} ({field_type}): {e}"
                )


def _decode_normal_hyper_mode(data: typing.BinaryIO, game: Game, property_size: int) -> ReptilicusHunterHyperMode:
    return ReptilicusHunterHyperMode.from_stream(data, game, property_size)


def _decode_hard_hyper_mode(data: typing.BinaryIO, game: Game, property_size: int) -> ReptilicusHunterHyperMode:
    return ReptilicusHunterHyperMode.from_stream(data, game, property_size)


def _decode_elite_hyper_mode(data: typing.BinaryIO, game: Game, property_size: int) -> ReptilicusHunterHyperMode:
    return ReptilicusHunterHyperMode.from_stream(data, game, property_size)


def _decode_cattle_prod(data: typing.BinaryIO, game: Game, property_size: int) -> ReptilicusHunterCattleProd:
    return ReptilicusHunterCattleProd.from_stream(data, game, property_size)


def _decode_energy_whip(data: typing.BinaryIO, game: Game, property_size: int) -> ReptilicusHunterEnergyWhip:
    return ReptilicusHunterEnergyWhip.from_stream(data, game, property_size)


def _decode_chakram(data: typing.BinaryIO, game: Game, property_size: int) -> ReptilicusHunterChakram:
    return ReptilicusHunterChakram.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x217e944a: ('use_defense_points', structs.decode_BIG_bool_),
    0x0c81681a: ('disable_terrain_alignment', structs.decode_BIG_bool_),
    0xe9553ffa: ('disable_cloaking', structs.decode_BIG_bool_),
    0x1c893f54: ('is_initially_cloaked', structs.decode_BIG_bool_),
    0x369d0874: ('min_visible_time', structs.decode_BIG_f),
    0x91a9880d: ('max_visible_time', structs.decode_BIG_f),
    0x11286bd3: ('force_visible_damage', structs.decode_BIG_f),
    0xb7e53921: ('unknown_0xb7e53921', structs.decode_BIG_f),
    0x5867275b: ('unknown_0x5867275b', structs.decode_BIG_f),
    0x388bc31f: ('cloak_time', structs.decode_BIG_f),
    0x4319c840: ('decloak_time', structs.decode_BIG_f),
    0x052bf617: ('cloak_sound', structs.decode_BIG_Q),
    0xfe842879: ('decloak_sound', structs.decode_BIG_Q),
    0x221c7ec1: ('unknown_0x221c7ec1', structs.decode_BIG_f),
    0x41af5eeb: ('unknown_0x41af5eeb', structs.decode_BIG_f),
    0x0cf887f1: ('hear_shot_radius', structs.decode_BIG_f),
    0x18a9876b: ('cover_abort_time', structs.decode_BIG_f),
    0x164f8ca8: ('min_visible_cover_time', structs.decode_BIG_f),
    0xcdf0df4f: ('max_visible_cover_time', structs.decode_BIG_f),
    0xf77e2ae2: ('min_invisible_cover_time', structs.decode_BIG_f),
    0x14239438: ('max_invisible_cover_time', structs.decode_BIG_f),
    0xe6c24412: ('unknown_0xe6c24412', structs.decode_BIG_f),
    0x583c1b1e: ('heavy_hit_chance', structs.decode_BIG_f),
    0xa77f6212: ('taunt_chance', structs.decode_BIG_f),
    0x9579b1f2: ('aggressiveness', structs.decode_BIG_f),
    0x9c5e7d6f: ('normal_hyper_mode', _decode_normal_hyper_mode),
    0xaa2bee9a: ('hard_hyper_mode', _decode_hard_hyper_mode),
    0xe27a4e87: ('elite_hyper_mode', _decode_elite_hyper_mode),
    0x87b10a69: ('cattle_prod', _decode_cattle_prod),
    0xd7548e97: ('energy_whip', _decode_energy_whip),
    0x19a58c31: ('chakram', _decode_chakram),
}
