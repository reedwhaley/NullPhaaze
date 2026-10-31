# Generated File
from __future__ import annotations

import dataclasses
import struct
import typing
import typing_extensions

from retro_data_structures import json_util
from retro_data_structures.game_check import Game
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.echoes.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class FlyingPirateJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        search_radius: float
        hearing_radius: float
        unknown_0x20daf45e: int
        projectile: int
        projectile_damage: json_util.JsonObject
        sound_projectile: int
        missile: int
        missile_damage: json_util.JsonObject
        wpsc: int
        hurl_recover_time: float
        hover_height: float
        rocket_pack_explosion: int
        rocket_pack_explosion_damage: json_util.JsonObject
        spiral_chance: float
        minimum_missile_time: float
        missile_time_variation: float
        flight_thrust: float
        sound_impact: int
        sound_spiral: int
        land_chance: float
        intra_burst_shot_time: float
        intra_burst_shot_variation: float
        landing_cloud_dirt: int
        landing_cloud_dust: int
        landing_cloud_snow: int
        sound_hurled: int
        sound_death: int
        double_attack_chance: float
        unknown_0x3427d27f: float
        stop_homing_range: float
        jet_pack_flame_size_min: float
        jet_pack_flame_size_max: float
        jet_pack_flame_speed_min: float
        jet_pack_flame_speed_max: float
    

@dataclasses.dataclass()
class FlyingPirate(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    patterned: PatternedAITypedef = dataclasses.field(default_factory=PatternedAITypedef, metadata={
        'reflection': FieldReflection[PatternedAITypedef](
            PatternedAITypedef, id=0xb3774750, original_name='Patterned', from_json=PatternedAITypedef.from_json, to_json=PatternedAITypedef.to_json
        ),
    })
    actor_information: ActorParameters = dataclasses.field(default_factory=ActorParameters, metadata={
        'reflection': FieldReflection[ActorParameters](
            ActorParameters, id=0x7e397fed, original_name='ActorInformation', from_json=ActorParameters.from_json, to_json=ActorParameters.to_json
        ),
    })
    search_radius: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xed9bf5a3, original_name='SearchRadius'
        ),
    })
    hearing_radius: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xed69488f, original_name='HearingRadius'
        ),
    })
    unknown_0x20daf45e: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x20daf45e, original_name='Unknown'
        ),
    })
    projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xef485db9, original_name='Projectile'
        ),
    })
    projectile_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x553b1339, original_name='ProjectileDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    sound_projectile: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xeac27605, original_name='Sound_Projectile'
        ),
    })
    missile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xca294811, original_name='Missile'
        ),
    })
    missile_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x258cfb4d, original_name='MissileDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    wpsc: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x1d510c6c, original_name='WPSC'
        ),
    })
    hurl_recover_time: float = dataclasses.field(default=0.800000011920929, metadata={
        'reflection': FieldReflection[float](
            float, id=0x96feb75d, original_name='HurlRecoverTime'
        ),
    })
    hover_height: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc75998aa, original_name='HoverHeight'
        ),
    })
    rocket_pack_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x6475fc6f, original_name='RocketPackExplosion'
        ),
    })
    rocket_pack_explosion_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x2564ee27, original_name='RocketPackExplosionDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    spiral_chance: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdf88607d, original_name='SpiralChance'
        ),
    })
    minimum_missile_time: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8fff07e9, original_name='MinimumMissileTime'
        ),
    })
    missile_time_variation: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb9bb2f64, original_name='MissileTimeVariation'
        ),
    })
    flight_thrust: float = dataclasses.field(default=1000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8ee7f440, original_name='FlightThrust'
        ),
    })
    sound_impact: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x1bb16ea5, original_name='Sound_Impact'
        ),
    })
    sound_spiral: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x0ff5ab8f, original_name='Sound_Spiral'
        ),
    })
    land_chance: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x87b2bc5a, original_name='LandChance'
        ),
    })
    intra_burst_shot_time: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x71587b45, original_name='IntraBurstShotTime'
        ),
    })
    intra_burst_shot_variation: float = dataclasses.field(default=0.05000000074505806, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7903312e, original_name='IntraBurstShotVariation'
        ),
    })
    landing_cloud_dirt: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x317212ab, original_name='LandingCloudDirt'
        ),
    })
    landing_cloud_dust: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xbc113d7b, original_name='LandingCloudDust'
        ),
    })
    landing_cloud_snow: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x738bbbaa, original_name='LandingCloudSnow'
        ),
    })
    sound_hurled: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x3bb37a8f, original_name='Sound_Hurled'
        ),
    })
    sound_death: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xe160b593, original_name='Sound_Death'
        ),
    })
    double_attack_chance: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x966d11f3, original_name='DoubleAttackChance'
        ),
    })
    unknown_0x3427d27f: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3427d27f, original_name='Unknown'
        ),
    })
    stop_homing_range: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x053ae4a7, original_name='StopHomingRange'
        ),
    })
    jet_pack_flame_size_min: float = dataclasses.field(default=2.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0xccf05648, original_name='JetPackFlameSizeMin'
        ),
    })
    jet_pack_flame_size_max: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2a90f9a9, original_name='JetPackFlameSizeMax'
        ),
    })
    jet_pack_flame_speed_min: float = dataclasses.field(default=-0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9ca8f357, original_name='JetPackFlameSpeedMin'
        ),
    })
    jet_pack_flame_speed_max: float = dataclasses.field(default=-0.23000000417232513, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7ac85cb6, original_name='JetPackFlameSpeedMax'
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'FPRT'

    @classmethod
    def modules(cls) -> list[str]:
        return ['FlyingPirate.rel']

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None) -> typing_extensions.Self:
        struct_id, size, property_count = structs.BIG_LHH.unpack(data.read(8))
        assert struct_id == 0xFFFFFFFF
        root_size_start = data.tell() - 2

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

        assert data.tell() - root_size_start == size
        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 37:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size, default_override={'turn_speed': 360.0, 'detection_angle': 90.0, 'min_attack_range': 15.0, 'max_attack_range': 40.0, 'average_attack_time': 1.0, 'attack_time_variation': 0.5, 'damage_wait_time': 3.0, 'collision_height': 6.0, 'step_up_height': 0.30000001192092896})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed9bf5a3
        search_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed69488f
        hearing_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x20daf45e
        unknown_0x20daf45e = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xef485db9
        projectile = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x553b1339
        projectile_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 9, 'di_damage': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xeac27605
        sound_projectile = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xca294811
        missile = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x258cfb4d
        missile_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 9, 'di_damage': 10.0, 'di_radius': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1d510c6c
        wpsc = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x96feb75d
        hurl_recover_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc75998aa
        hover_height = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6475fc6f
        rocket_pack_explosion = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2564ee27
        rocket_pack_explosion_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 9, 'di_damage': 20.0, 'di_radius': 10.0, 'di_knock_back_power': 10.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdf88607d
        spiral_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8fff07e9
        minimum_missile_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb9bb2f64
        missile_time_variation = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8ee7f440
        flight_thrust = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1bb16ea5
        sound_impact = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0ff5ab8f
        sound_spiral = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x87b2bc5a
        land_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71587b45
        intra_burst_shot_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7903312e
        intra_burst_shot_variation = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x317212ab
        landing_cloud_dirt = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbc113d7b
        landing_cloud_dust = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x738bbbaa
        landing_cloud_snow = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3bb37a8f
        sound_hurled = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe160b593
        sound_death = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x966d11f3
        double_attack_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3427d27f
        unknown_0x3427d27f = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x053ae4a7
        stop_homing_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xccf05648
        jet_pack_flame_size_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2a90f9a9
        jet_pack_flame_size_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9ca8f357
        jet_pack_flame_speed_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7ac85cb6
        jet_pack_flame_speed_max = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(editor_properties, patterned, actor_information, search_radius, hearing_radius, unknown_0x20daf45e, projectile, projectile_damage, sound_projectile, missile, missile_damage, wpsc, hurl_recover_time, hover_height, rocket_pack_explosion, rocket_pack_explosion_damage, spiral_chance, minimum_missile_time, missile_time_variation, flight_thrust, sound_impact, sound_spiral, land_chance, intra_burst_shot_time, intra_burst_shot_variation, landing_cloud_dirt, landing_cloud_dust, landing_cloud_snow, sound_hurled, sound_death, double_attack_chance, unknown_0x3427d27f, stop_homing_range, jet_pack_flame_size_min, jet_pack_flame_size_max, jet_pack_flame_speed_min, jet_pack_flame_speed_max)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00%')  # 37 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb3wGP')  # 0xb3774750
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.patterned.to_stream(data, game, default_override={'turn_speed': 360.0, 'detection_angle': 90.0, 'min_attack_range': 15.0, 'max_attack_range': 40.0, 'average_attack_time': 1.0, 'attack_time_variation': 0.5, 'damage_wait_time': 3.0, 'collision_height': 6.0, 'step_up_height': 0.30000001192092896})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'~9\x7f\xed')  # 0x7e397fed
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.actor_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xed\x9b\xf5\xa3')  # 0xed9bf5a3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.search_radius))

        data.write(b'\xediH\x8f')  # 0xed69488f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hearing_radius))

        data.write(b' \xda\xf4^')  # 0x20daf45e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x20daf45e))

        data.write(b'\xefH]\xb9')  # 0xef485db9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.projectile))

        data.write(b'U;\x139')  # 0x553b1339
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.projectile_damage.to_stream(data, game, default_override={'di_weapon_type': 9, 'di_damage': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xea\xc2v\x05')  # 0xeac27605
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_projectile))

        data.write(b'\xca)H\x11')  # 0xca294811
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.missile))

        data.write(b'%\x8c\xfbM')  # 0x258cfb4d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.missile_damage.to_stream(data, game, default_override={'di_weapon_type': 9, 'di_damage': 10.0, 'di_radius': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x1dQ\x0cl')  # 0x1d510c6c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.wpsc))

        data.write(b'\x96\xfe\xb7]')  # 0x96feb75d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hurl_recover_time))

        data.write(b'\xc7Y\x98\xaa')  # 0xc75998aa
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hover_height))

        data.write(b'du\xfco')  # 0x6475fc6f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.rocket_pack_explosion))

        data.write(b"%d\xee'")  # 0x2564ee27
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.rocket_pack_explosion_damage.to_stream(data, game, default_override={'di_weapon_type': 9, 'di_damage': 20.0, 'di_radius': 10.0, 'di_knock_back_power': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xdf\x88`}')  # 0xdf88607d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.spiral_chance))

        data.write(b'\x8f\xff\x07\xe9')  # 0x8fff07e9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.minimum_missile_time))

        data.write(b'\xb9\xbb/d')  # 0xb9bb2f64
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.missile_time_variation))

        data.write(b'\x8e\xe7\xf4@')  # 0x8ee7f440
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flight_thrust))

        data.write(b'\x1b\xb1n\xa5')  # 0x1bb16ea5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_impact))

        data.write(b'\x0f\xf5\xab\x8f')  # 0xff5ab8f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_spiral))

        data.write(b'\x87\xb2\xbcZ')  # 0x87b2bc5a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.land_chance))

        data.write(b'qX{E')  # 0x71587b45
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.intra_burst_shot_time))

        data.write(b'y\x031.')  # 0x7903312e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.intra_burst_shot_variation))

        data.write(b'1r\x12\xab')  # 0x317212ab
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.landing_cloud_dirt))

        data.write(b'\xbc\x11={')  # 0xbc113d7b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.landing_cloud_dust))

        data.write(b's\x8b\xbb\xaa')  # 0x738bbbaa
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.landing_cloud_snow))

        data.write(b';\xb3z\x8f')  # 0x3bb37a8f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_hurled))

        data.write(b'\xe1`\xb5\x93')  # 0xe160b593
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_death))

        data.write(b'\x96m\x11\xf3')  # 0x966d11f3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.double_attack_chance))

        data.write(b"4'\xd2\x7f")  # 0x3427d27f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3427d27f))

        data.write(b'\x05:\xe4\xa7')  # 0x53ae4a7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stop_homing_range))

        data.write(b'\xcc\xf0VH')  # 0xccf05648
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jet_pack_flame_size_min))

        data.write(b'*\x90\xf9\xa9')  # 0x2a90f9a9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jet_pack_flame_size_max))

        data.write(b'\x9c\xa8\xf3W')  # 0x9ca8f357
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jet_pack_flame_speed_min))

        data.write(b'z\xc8\\\xb6')  # 0x7ac85cb6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jet_pack_flame_speed_max))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FlyingPirateJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            patterned=PatternedAITypedef.from_json(json_data['patterned']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
            search_radius=json_data['search_radius'],
            hearing_radius=json_data['hearing_radius'],
            unknown_0x20daf45e=json_data['unknown_0x20daf45e'],
            projectile=json_data['projectile'],
            projectile_damage=DamageInfo.from_json(json_data['projectile_damage']),
            sound_projectile=json_data['sound_projectile'],
            missile=json_data['missile'],
            missile_damage=DamageInfo.from_json(json_data['missile_damage']),
            wpsc=json_data['wpsc'],
            hurl_recover_time=json_data['hurl_recover_time'],
            hover_height=json_data['hover_height'],
            rocket_pack_explosion=json_data['rocket_pack_explosion'],
            rocket_pack_explosion_damage=DamageInfo.from_json(json_data['rocket_pack_explosion_damage']),
            spiral_chance=json_data['spiral_chance'],
            minimum_missile_time=json_data['minimum_missile_time'],
            missile_time_variation=json_data['missile_time_variation'],
            flight_thrust=json_data['flight_thrust'],
            sound_impact=json_data['sound_impact'],
            sound_spiral=json_data['sound_spiral'],
            land_chance=json_data['land_chance'],
            intra_burst_shot_time=json_data['intra_burst_shot_time'],
            intra_burst_shot_variation=json_data['intra_burst_shot_variation'],
            landing_cloud_dirt=json_data['landing_cloud_dirt'],
            landing_cloud_dust=json_data['landing_cloud_dust'],
            landing_cloud_snow=json_data['landing_cloud_snow'],
            sound_hurled=json_data['sound_hurled'],
            sound_death=json_data['sound_death'],
            double_attack_chance=json_data['double_attack_chance'],
            unknown_0x3427d27f=json_data['unknown_0x3427d27f'],
            stop_homing_range=json_data['stop_homing_range'],
            jet_pack_flame_size_min=json_data['jet_pack_flame_size_min'],
            jet_pack_flame_size_max=json_data['jet_pack_flame_size_max'],
            jet_pack_flame_speed_min=json_data['jet_pack_flame_speed_min'],
            jet_pack_flame_speed_max=json_data['jet_pack_flame_speed_max'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'patterned': self.patterned.to_json(),
            'actor_information': self.actor_information.to_json(),
            'search_radius': self.search_radius,
            'hearing_radius': self.hearing_radius,
            'unknown_0x20daf45e': self.unknown_0x20daf45e,
            'projectile': self.projectile,
            'projectile_damage': self.projectile_damage.to_json(),
            'sound_projectile': self.sound_projectile,
            'missile': self.missile,
            'missile_damage': self.missile_damage.to_json(),
            'wpsc': self.wpsc,
            'hurl_recover_time': self.hurl_recover_time,
            'hover_height': self.hover_height,
            'rocket_pack_explosion': self.rocket_pack_explosion,
            'rocket_pack_explosion_damage': self.rocket_pack_explosion_damage.to_json(),
            'spiral_chance': self.spiral_chance,
            'minimum_missile_time': self.minimum_missile_time,
            'missile_time_variation': self.missile_time_variation,
            'flight_thrust': self.flight_thrust,
            'sound_impact': self.sound_impact,
            'sound_spiral': self.sound_spiral,
            'land_chance': self.land_chance,
            'intra_burst_shot_time': self.intra_burst_shot_time,
            'intra_burst_shot_variation': self.intra_burst_shot_variation,
            'landing_cloud_dirt': self.landing_cloud_dirt,
            'landing_cloud_dust': self.landing_cloud_dust,
            'landing_cloud_snow': self.landing_cloud_snow,
            'sound_hurled': self.sound_hurled,
            'sound_death': self.sound_death,
            'double_attack_chance': self.double_attack_chance,
            'unknown_0x3427d27f': self.unknown_0x3427d27f,
            'stop_homing_range': self.stop_homing_range,
            'jet_pack_flame_size_min': self.jet_pack_flame_size_min,
            'jet_pack_flame_size_max': self.jet_pack_flame_size_max,
            'jet_pack_flame_speed_min': self.jet_pack_flame_speed_min,
            'jet_pack_flame_speed_max': self.jet_pack_flame_speed_max,
        }

    def _dependencies_for_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile)

    def _dependencies_for_sound_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_projectile)

    def _dependencies_for_missile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.missile)

    def _dependencies_for_wpsc(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wpsc)

    def _dependencies_for_rocket_pack_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.rocket_pack_explosion)

    def _dependencies_for_sound_impact(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_impact)

    def _dependencies_for_sound_spiral(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_spiral)

    def _dependencies_for_landing_cloud_dirt(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.landing_cloud_dirt)

    def _dependencies_for_landing_cloud_dust(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.landing_cloud_dust)

    def _dependencies_for_landing_cloud_snow(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.landing_cloud_snow)

    def _dependencies_for_sound_hurled(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_hurled)

    def _dependencies_for_sound_death(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_death)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_projectile, "projectile", "AssetId"),
            (self._dependencies_for_sound_projectile, "sound_projectile", "int"),
            (self._dependencies_for_missile, "missile", "AssetId"),
            (self._dependencies_for_wpsc, "wpsc", "AssetId"),
            (self._dependencies_for_rocket_pack_explosion, "rocket_pack_explosion", "AssetId"),
            (self._dependencies_for_sound_impact, "sound_impact", "int"),
            (self._dependencies_for_sound_spiral, "sound_spiral", "int"),
            (self._dependencies_for_landing_cloud_dirt, "landing_cloud_dirt", "AssetId"),
            (self._dependencies_for_landing_cloud_dust, "landing_cloud_dust", "AssetId"),
            (self._dependencies_for_landing_cloud_snow, "landing_cloud_snow", "AssetId"),
            (self._dependencies_for_sound_hurled, "sound_hurled", "int"),
            (self._dependencies_for_sound_death, "sound_death", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for FlyingPirate.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={'turn_speed': 360.0, 'detection_angle': 90.0, 'min_attack_range': 15.0, 'max_attack_range': 40.0, 'average_attack_time': 1.0, 'attack_time_variation': 0.5, 'damage_wait_time': 3.0, 'collision_height': 6.0, 'step_up_height': 0.30000001192092896})


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 9, 'di_damage': 5.0})


def _decode_missile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 9, 'di_damage': 10.0, 'di_radius': 5.0})


def _decode_rocket_pack_explosion_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 9, 'di_damage': 20.0, 'di_radius': 10.0, 'di_knock_back_power': 10.0})


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xb3774750: ('patterned', _decode_patterned),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0xed9bf5a3: ('search_radius', structs.decode_BIG_f),
    0xed69488f: ('hearing_radius', structs.decode_BIG_f),
    0x20daf45e: ('unknown_0x20daf45e', structs.decode_BIG_l),
    0xef485db9: ('projectile', structs.decode_BIG_L),
    0x553b1339: ('projectile_damage', _decode_projectile_damage),
    0xeac27605: ('sound_projectile', structs.decode_BIG_l),
    0xca294811: ('missile', structs.decode_BIG_L),
    0x258cfb4d: ('missile_damage', _decode_missile_damage),
    0x1d510c6c: ('wpsc', structs.decode_BIG_L),
    0x96feb75d: ('hurl_recover_time', structs.decode_BIG_f),
    0xc75998aa: ('hover_height', structs.decode_BIG_f),
    0x6475fc6f: ('rocket_pack_explosion', structs.decode_BIG_L),
    0x2564ee27: ('rocket_pack_explosion_damage', _decode_rocket_pack_explosion_damage),
    0xdf88607d: ('spiral_chance', structs.decode_BIG_f),
    0x8fff07e9: ('minimum_missile_time', structs.decode_BIG_f),
    0xb9bb2f64: ('missile_time_variation', structs.decode_BIG_f),
    0x8ee7f440: ('flight_thrust', structs.decode_BIG_f),
    0x1bb16ea5: ('sound_impact', structs.decode_BIG_l),
    0x0ff5ab8f: ('sound_spiral', structs.decode_BIG_l),
    0x87b2bc5a: ('land_chance', structs.decode_BIG_f),
    0x71587b45: ('intra_burst_shot_time', structs.decode_BIG_f),
    0x7903312e: ('intra_burst_shot_variation', structs.decode_BIG_f),
    0x317212ab: ('landing_cloud_dirt', structs.decode_BIG_L),
    0xbc113d7b: ('landing_cloud_dust', structs.decode_BIG_L),
    0x738bbbaa: ('landing_cloud_snow', structs.decode_BIG_L),
    0x3bb37a8f: ('sound_hurled', structs.decode_BIG_l),
    0xe160b593: ('sound_death', structs.decode_BIG_l),
    0x966d11f3: ('double_attack_chance', structs.decode_BIG_f),
    0x3427d27f: ('unknown_0x3427d27f', structs.decode_BIG_f),
    0x053ae4a7: ('stop_homing_range', structs.decode_BIG_f),
    0xccf05648: ('jet_pack_flame_size_min', structs.decode_BIG_f),
    0x2a90f9a9: ('jet_pack_flame_size_max', structs.decode_BIG_f),
    0x9ca8f357: ('jet_pack_flame_speed_min', structs.decode_BIG_f),
    0x7ac85cb6: ('jet_pack_flame_speed_max', structs.decode_BIG_f),
}
