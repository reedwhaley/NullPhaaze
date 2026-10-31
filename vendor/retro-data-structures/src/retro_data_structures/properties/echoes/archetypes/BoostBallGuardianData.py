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
from retro_data_structures.properties.echoes.archetypes.IngBoostBallGuardianBoostData import IngBoostBallGuardianBoostData
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.spline import Spline
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class BoostBallGuardianDataJson(typing_extensions.TypedDict):
        boost_ball_scale: json_util.JsonValue
        boost_ball_mass: float
        boost_ball_bounciness: float
        boost_ball_speed: json_util.JsonObject
        boost_ball_damage_to_morph_ball: json_util.JsonObject
        boost_ball_damage_to_first_person: json_util.JsonObject
        boost_ball_min_damage_speed: float
        unknown_0x7b21e31a: float
        boost_ball_model: int
        boost_ball_charge_up_effect: int
        boost_ball_shield_effect: int
        boost_ball_trail_effect: int
        sound_bounce: int
        sound_into_ball: int
        sound_outof_ball: int
        sound: int
        sound_boost: int
        sound_rolling: int
        boost_ball_vulnerability: json_util.JsonObject
        unknown_0xee69b993: int
        unknown_0x4b2de673: int
        search_cone_angle: float
        unknown_0xb0e85d53: float
        ing_spot_damage_to_morph_ball: json_util.JsonObject
        ing_spot_damage_to_first_person: json_util.JsonObject
        boost_ing_spot_blob_effect: int
        boost_ing_spot_hit_normal_damage: int
        boost_ing_spot_hit_heavy_damage: int
        stage1: json_util.JsonObject
        stage2: json_util.JsonObject
        stage3: json_util.JsonObject
    

@dataclasses.dataclass()
class BoostBallGuardianData(BaseProperty):
    boost_ball_scale: Vector = dataclasses.field(default_factory=lambda: Vector(x=1.7999999523162842, y=1.7999999523162842, z=1.7999999523162842), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0xa322f51d, original_name='BoostBallScale', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    boost_ball_mass: float = dataclasses.field(default=150.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x528d951e, original_name='BoostBallMass'
        ),
    })
    boost_ball_bounciness: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbea96fb7, original_name='BoostBallBounciness'
        ),
    })
    boost_ball_speed: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xa25b96e1, original_name='BoostBallSpeed', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    boost_ball_damage_to_morph_ball: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x0e1a78bd, original_name='BoostBallDamageToMorphBall', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    boost_ball_damage_to_first_person: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x19c3d263, original_name='BoostBallDamageToFirstPerson', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    boost_ball_min_damage_speed: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd8047cba, original_name='BoostBallMinDamageSpeed'
        ),
    })
    unknown_0x7b21e31a: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7b21e31a, original_name='Unknown'
        ),
    })
    boost_ball_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x18381479, original_name='BoostBallModel'
        ),
    })
    boost_ball_charge_up_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x15534429, original_name='BoostBallChargeUpEffect'
        ),
    })
    boost_ball_shield_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x4cceb7ad, original_name='BoostBallShieldEffect'
        ),
    })
    boost_ball_trail_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe41cb449, original_name='BoostBallTrailEffect'
        ),
    })
    sound_bounce: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x6758bf01, original_name='Sound_Bounce'
        ),
    })
    sound_into_ball: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x8d9e014f, original_name='Sound_IntoBall'
        ),
    })
    sound_outof_ball: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xe35ae4be, original_name='Sound_OutofBall'
        ),
    })
    sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x9f7372b3, original_name='Sound'
        ),
    })
    sound_boost: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xdd69a116, original_name='Sound_Boost'
        ),
    })
    sound_rolling: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xbf42c3ec, original_name='Sound_Rolling'
        ),
    })
    boost_ball_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x42eca523, original_name='BoostBallVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    unknown_0xee69b993: int = dataclasses.field(default=2, metadata={
        'reflection': FieldReflection[int](
            int, id=0xee69b993, original_name='Unknown'
        ),
    })
    unknown_0x4b2de673: int = dataclasses.field(default=3, metadata={
        'reflection': FieldReflection[int](
            int, id=0x4b2de673, original_name='Unknown'
        ),
    })
    search_cone_angle: float = dataclasses.field(default=80.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2a7073ce, original_name='SearchConeAngle'
        ),
    })
    unknown_0xb0e85d53: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb0e85d53, original_name='Unknown'
        ),
    })
    ing_spot_damage_to_morph_ball: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x5616d5f1, original_name='IngSpotDamageToMorphBall', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    ing_spot_damage_to_first_person: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xed685533, original_name='IngSpotDamageToFirstPerson', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    boost_ing_spot_blob_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd771ec43, original_name='BoostIngSpotBlobEffect'
        ),
    })
    boost_ing_spot_hit_normal_damage: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2009a977, original_name='BoostIngSpotHitNormalDamage'
        ),
    })
    boost_ing_spot_hit_heavy_damage: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x62ab33a2, original_name='BoostIngSpotHitHeavyDamage'
        ),
    })
    stage1: IngBoostBallGuardianBoostData = dataclasses.field(default_factory=IngBoostBallGuardianBoostData, metadata={
        'reflection': FieldReflection[IngBoostBallGuardianBoostData](
            IngBoostBallGuardianBoostData, id=0xbab98497, original_name='Stage1', from_json=IngBoostBallGuardianBoostData.from_json, to_json=IngBoostBallGuardianBoostData.to_json
        ),
    })
    stage2: IngBoostBallGuardianBoostData = dataclasses.field(default_factory=IngBoostBallGuardianBoostData, metadata={
        'reflection': FieldReflection[IngBoostBallGuardianBoostData](
            IngBoostBallGuardianBoostData, id=0xfe18a18f, original_name='Stage2', from_json=IngBoostBallGuardianBoostData.from_json, to_json=IngBoostBallGuardianBoostData.to_json
        ),
    })
    stage3: IngBoostBallGuardianBoostData = dataclasses.field(default_factory=IngBoostBallGuardianBoostData, metadata={
        'reflection': FieldReflection[IngBoostBallGuardianBoostData](
            IngBoostBallGuardianBoostData, id=0xc2784287, original_name='Stage3', from_json=IngBoostBallGuardianBoostData.from_json, to_json=IngBoostBallGuardianBoostData.to_json
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
        assert property_id == 0xa322f51d
        boost_ball_scale = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x528d951e
        boost_ball_mass = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbea96fb7
        boost_ball_bounciness = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa25b96e1
        boost_ball_speed = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0e1a78bd
        boost_ball_damage_to_morph_ball = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 7, 'di_damage': 30.0, 'di_radius': 1.5, 'di_knock_back_power': 4.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19c3d263
        boost_ball_damage_to_first_person = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 7, 'di_damage': 30.0, 'di_radius': 1.5, 'di_knock_back_power': 6.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd8047cba
        boost_ball_min_damage_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7b21e31a
        unknown_0x7b21e31a = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x18381479
        boost_ball_model = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x15534429
        boost_ball_charge_up_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4cceb7ad
        boost_ball_shield_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe41cb449
        boost_ball_trail_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6758bf01
        sound_bounce = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8d9e014f
        sound_into_ball = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe35ae4be
        sound_outof_ball = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9f7372b3
        sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdd69a116
        sound_boost = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbf42c3ec
        sound_rolling = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42eca523
        boost_ball_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xee69b993
        unknown_0xee69b993 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4b2de673
        unknown_0x4b2de673 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2a7073ce
        search_cone_angle = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb0e85d53
        unknown_0xb0e85d53 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5616d5f1
        ing_spot_damage_to_morph_ball = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed685533
        ing_spot_damage_to_first_person = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 10.0, 'di_knock_back_power': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd771ec43
        boost_ing_spot_blob_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2009a977
        boost_ing_spot_hit_normal_damage = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x62ab33a2
        boost_ing_spot_hit_heavy_damage = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbab98497
        stage1 = IngBoostBallGuardianBoostData.from_stream(data, game, property_size, default_override={'boost_puddle_mode_time': 15.0, 'percentage_puddle_damage_to_boost': 0.5, 'break_boost_puddle_mode_damage': 90.0, 'break_boost_mode_damage': 10.0, 'next_boost_time_min': 2.0, 'next_boost_time_max': 5.0, 'sequential_boost_attacks_min': 3, 'sequential_boost_attacks_max': 3, 'small_boost_num_bounces_min': 1, 'small_boost_num_bounces_max': 5, 'large_boost_num_bounces_min': 6, 'large_boost_num_bounces_max': 10, 'locomotion_speed_scale': 1.0, 'ing_spot_speed_scale': 1.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfe18a18f
        stage2 = IngBoostBallGuardianBoostData.from_stream(data, game, property_size, default_override={'boost_puddle_mode_time': 15.0, 'percentage_puddle_damage_to_boost': 0.5, 'break_boost_puddle_mode_damage': 90.0, 'break_boost_mode_damage': 10.0, 'next_boost_time_min': 2.0, 'next_boost_time_max': 5.0, 'sequential_boost_attacks_min': 3, 'sequential_boost_attacks_max': 3, 'small_boost_num_bounces_min': 1, 'small_boost_num_bounces_max': 5, 'large_boost_num_bounces_min': 6, 'large_boost_num_bounces_max': 10, 'locomotion_speed_scale': 1.0, 'ing_spot_speed_scale': 1.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc2784287
        stage3 = IngBoostBallGuardianBoostData.from_stream(data, game, property_size, default_override={'boost_puddle_mode_time': 15.0, 'percentage_puddle_damage_to_boost': 0.5, 'break_boost_puddle_mode_damage': 90.0, 'break_boost_mode_damage': 10.0, 'next_boost_time_min': 2.0, 'next_boost_time_max': 5.0, 'sequential_boost_attacks_min': 3, 'sequential_boost_attacks_max': 3, 'small_boost_num_bounces_min': 1, 'small_boost_num_bounces_max': 5, 'large_boost_num_bounces_min': 6, 'large_boost_num_bounces_max': 10, 'locomotion_speed_scale': 1.0, 'ing_spot_speed_scale': 1.0})
    
        return cls(boost_ball_scale, boost_ball_mass, boost_ball_bounciness, boost_ball_speed, boost_ball_damage_to_morph_ball, boost_ball_damage_to_first_person, boost_ball_min_damage_speed, unknown_0x7b21e31a, boost_ball_model, boost_ball_charge_up_effect, boost_ball_shield_effect, boost_ball_trail_effect, sound_bounce, sound_into_ball, sound_outof_ball, sound, sound_boost, sound_rolling, boost_ball_vulnerability, unknown_0xee69b993, unknown_0x4b2de673, search_cone_angle, unknown_0xb0e85d53, ing_spot_damage_to_morph_ball, ing_spot_damage_to_first_person, boost_ing_spot_blob_effect, boost_ing_spot_hit_normal_damage, boost_ing_spot_hit_heavy_damage, stage1, stage2, stage3)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x1f')  # 31 properties

        data.write(b'\xa3"\xf5\x1d')  # 0xa322f51d
        data.write(b'\x00\x0c')  # size
        self.boost_ball_scale.to_stream(data, game)

        data.write(b'R\x8d\x95\x1e')  # 0x528d951e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.boost_ball_mass))

        data.write(b'\xbe\xa9o\xb7')  # 0xbea96fb7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.boost_ball_bounciness))

        data.write(b'\xa2[\x96\xe1')  # 0xa25b96e1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.boost_ball_speed.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x0e\x1ax\xbd')  # 0xe1a78bd
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.boost_ball_damage_to_morph_ball.to_stream(data, game, default_override={'di_weapon_type': 7, 'di_damage': 30.0, 'di_radius': 1.5, 'di_knock_back_power': 4.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x19\xc3\xd2c')  # 0x19c3d263
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.boost_ball_damage_to_first_person.to_stream(data, game, default_override={'di_weapon_type': 7, 'di_damage': 30.0, 'di_radius': 1.5, 'di_knock_back_power': 6.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd8\x04|\xba')  # 0xd8047cba
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.boost_ball_min_damage_speed))

        data.write(b'{!\xe3\x1a')  # 0x7b21e31a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7b21e31a))

        data.write(b'\x188\x14y')  # 0x18381479
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.boost_ball_model))

        data.write(b'\x15SD)')  # 0x15534429
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.boost_ball_charge_up_effect))

        data.write(b'L\xce\xb7\xad')  # 0x4cceb7ad
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.boost_ball_shield_effect))

        data.write(b'\xe4\x1c\xb4I')  # 0xe41cb449
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.boost_ball_trail_effect))

        data.write(b'gX\xbf\x01')  # 0x6758bf01
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_bounce))

        data.write(b'\x8d\x9e\x01O')  # 0x8d9e014f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_into_ball))

        data.write(b'\xe3Z\xe4\xbe')  # 0xe35ae4be
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_outof_ball))

        data.write(b'\x9fsr\xb3')  # 0x9f7372b3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound))

        data.write(b'\xddi\xa1\x16')  # 0xdd69a116
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_boost))

        data.write(b'\xbfB\xc3\xec')  # 0xbf42c3ec
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_rolling))

        data.write(b'B\xec\xa5#')  # 0x42eca523
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.boost_ball_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xeei\xb9\x93')  # 0xee69b993
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xee69b993))

        data.write(b'K-\xe6s')  # 0x4b2de673
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x4b2de673))

        data.write(b'*ps\xce')  # 0x2a7073ce
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.search_cone_angle))

        data.write(b'\xb0\xe8]S')  # 0xb0e85d53
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb0e85d53))

        data.write(b'V\x16\xd5\xf1')  # 0x5616d5f1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ing_spot_damage_to_morph_ball.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xedhU3')  # 0xed685533
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ing_spot_damage_to_first_person.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 10.0, 'di_knock_back_power': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd7q\xecC')  # 0xd771ec43
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.boost_ing_spot_blob_effect))

        data.write(b' \t\xa9w')  # 0x2009a977
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.boost_ing_spot_hit_normal_damage))

        data.write(b'b\xab3\xa2')  # 0x62ab33a2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.boost_ing_spot_hit_heavy_damage))

        data.write(b'\xba\xb9\x84\x97')  # 0xbab98497
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stage1.to_stream(data, game, default_override={'boost_puddle_mode_time': 15.0, 'percentage_puddle_damage_to_boost': 0.5, 'break_boost_puddle_mode_damage': 90.0, 'break_boost_mode_damage': 10.0, 'next_boost_time_min': 2.0, 'next_boost_time_max': 5.0, 'sequential_boost_attacks_min': 3, 'sequential_boost_attacks_max': 3, 'small_boost_num_bounces_min': 1, 'small_boost_num_bounces_max': 5, 'large_boost_num_bounces_min': 6, 'large_boost_num_bounces_max': 10, 'locomotion_speed_scale': 1.0, 'ing_spot_speed_scale': 1.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfe\x18\xa1\x8f')  # 0xfe18a18f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stage2.to_stream(data, game, default_override={'boost_puddle_mode_time': 15.0, 'percentage_puddle_damage_to_boost': 0.5, 'break_boost_puddle_mode_damage': 90.0, 'break_boost_mode_damage': 10.0, 'next_boost_time_min': 2.0, 'next_boost_time_max': 5.0, 'sequential_boost_attacks_min': 3, 'sequential_boost_attacks_max': 3, 'small_boost_num_bounces_min': 1, 'small_boost_num_bounces_max': 5, 'large_boost_num_bounces_min': 6, 'large_boost_num_bounces_max': 10, 'locomotion_speed_scale': 1.0, 'ing_spot_speed_scale': 1.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc2xB\x87')  # 0xc2784287
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stage3.to_stream(data, game, default_override={'boost_puddle_mode_time': 15.0, 'percentage_puddle_damage_to_boost': 0.5, 'break_boost_puddle_mode_damage': 90.0, 'break_boost_mode_damage': 10.0, 'next_boost_time_min': 2.0, 'next_boost_time_max': 5.0, 'sequential_boost_attacks_min': 3, 'sequential_boost_attacks_max': 3, 'small_boost_num_bounces_min': 1, 'small_boost_num_bounces_max': 5, 'large_boost_num_bounces_min': 6, 'large_boost_num_bounces_max': 10, 'locomotion_speed_scale': 1.0, 'ing_spot_speed_scale': 1.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("BoostBallGuardianDataJson", data)
        return cls(
            boost_ball_scale=Vector.from_json(json_data['boost_ball_scale']),
            boost_ball_mass=json_data['boost_ball_mass'],
            boost_ball_bounciness=json_data['boost_ball_bounciness'],
            boost_ball_speed=Spline.from_json(json_data['boost_ball_speed']),
            boost_ball_damage_to_morph_ball=DamageInfo.from_json(json_data['boost_ball_damage_to_morph_ball']),
            boost_ball_damage_to_first_person=DamageInfo.from_json(json_data['boost_ball_damage_to_first_person']),
            boost_ball_min_damage_speed=json_data['boost_ball_min_damage_speed'],
            unknown_0x7b21e31a=json_data['unknown_0x7b21e31a'],
            boost_ball_model=json_data['boost_ball_model'],
            boost_ball_charge_up_effect=json_data['boost_ball_charge_up_effect'],
            boost_ball_shield_effect=json_data['boost_ball_shield_effect'],
            boost_ball_trail_effect=json_data['boost_ball_trail_effect'],
            sound_bounce=json_data['sound_bounce'],
            sound_into_ball=json_data['sound_into_ball'],
            sound_outof_ball=json_data['sound_outof_ball'],
            sound=json_data['sound'],
            sound_boost=json_data['sound_boost'],
            sound_rolling=json_data['sound_rolling'],
            boost_ball_vulnerability=DamageVulnerability.from_json(json_data['boost_ball_vulnerability']),
            unknown_0xee69b993=json_data['unknown_0xee69b993'],
            unknown_0x4b2de673=json_data['unknown_0x4b2de673'],
            search_cone_angle=json_data['search_cone_angle'],
            unknown_0xb0e85d53=json_data['unknown_0xb0e85d53'],
            ing_spot_damage_to_morph_ball=DamageInfo.from_json(json_data['ing_spot_damage_to_morph_ball']),
            ing_spot_damage_to_first_person=DamageInfo.from_json(json_data['ing_spot_damage_to_first_person']),
            boost_ing_spot_blob_effect=json_data['boost_ing_spot_blob_effect'],
            boost_ing_spot_hit_normal_damage=json_data['boost_ing_spot_hit_normal_damage'],
            boost_ing_spot_hit_heavy_damage=json_data['boost_ing_spot_hit_heavy_damage'],
            stage1=IngBoostBallGuardianBoostData.from_json(json_data['stage1']),
            stage2=IngBoostBallGuardianBoostData.from_json(json_data['stage2']),
            stage3=IngBoostBallGuardianBoostData.from_json(json_data['stage3']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'boost_ball_scale': self.boost_ball_scale.to_json(),
            'boost_ball_mass': self.boost_ball_mass,
            'boost_ball_bounciness': self.boost_ball_bounciness,
            'boost_ball_speed': self.boost_ball_speed.to_json(),
            'boost_ball_damage_to_morph_ball': self.boost_ball_damage_to_morph_ball.to_json(),
            'boost_ball_damage_to_first_person': self.boost_ball_damage_to_first_person.to_json(),
            'boost_ball_min_damage_speed': self.boost_ball_min_damage_speed,
            'unknown_0x7b21e31a': self.unknown_0x7b21e31a,
            'boost_ball_model': self.boost_ball_model,
            'boost_ball_charge_up_effect': self.boost_ball_charge_up_effect,
            'boost_ball_shield_effect': self.boost_ball_shield_effect,
            'boost_ball_trail_effect': self.boost_ball_trail_effect,
            'sound_bounce': self.sound_bounce,
            'sound_into_ball': self.sound_into_ball,
            'sound_outof_ball': self.sound_outof_ball,
            'sound': self.sound,
            'sound_boost': self.sound_boost,
            'sound_rolling': self.sound_rolling,
            'boost_ball_vulnerability': self.boost_ball_vulnerability.to_json(),
            'unknown_0xee69b993': self.unknown_0xee69b993,
            'unknown_0x4b2de673': self.unknown_0x4b2de673,
            'search_cone_angle': self.search_cone_angle,
            'unknown_0xb0e85d53': self.unknown_0xb0e85d53,
            'ing_spot_damage_to_morph_ball': self.ing_spot_damage_to_morph_ball.to_json(),
            'ing_spot_damage_to_first_person': self.ing_spot_damage_to_first_person.to_json(),
            'boost_ing_spot_blob_effect': self.boost_ing_spot_blob_effect,
            'boost_ing_spot_hit_normal_damage': self.boost_ing_spot_hit_normal_damage,
            'boost_ing_spot_hit_heavy_damage': self.boost_ing_spot_hit_heavy_damage,
            'stage1': self.stage1.to_json(),
            'stage2': self.stage2.to_json(),
            'stage3': self.stage3.to_json(),
        }

    def _dependencies_for_boost_ball_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.boost_ball_model)

    def _dependencies_for_boost_ball_charge_up_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.boost_ball_charge_up_effect)

    def _dependencies_for_boost_ball_shield_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.boost_ball_shield_effect)

    def _dependencies_for_boost_ball_trail_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.boost_ball_trail_effect)

    def _dependencies_for_sound_bounce(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_bounce)

    def _dependencies_for_sound_into_ball(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_into_ball)

    def _dependencies_for_sound_outof_ball(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_outof_ball)

    def _dependencies_for_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound)

    def _dependencies_for_sound_boost(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_boost)

    def _dependencies_for_sound_rolling(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_rolling)

    def _dependencies_for_boost_ing_spot_blob_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.boost_ing_spot_blob_effect)

    def _dependencies_for_boost_ing_spot_hit_normal_damage(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.boost_ing_spot_hit_normal_damage)

    def _dependencies_for_boost_ing_spot_hit_heavy_damage(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.boost_ing_spot_hit_heavy_damage)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_boost_ball_model, "boost_ball_model", "AssetId"),
            (self._dependencies_for_boost_ball_charge_up_effect, "boost_ball_charge_up_effect", "AssetId"),
            (self._dependencies_for_boost_ball_shield_effect, "boost_ball_shield_effect", "AssetId"),
            (self._dependencies_for_boost_ball_trail_effect, "boost_ball_trail_effect", "AssetId"),
            (self._dependencies_for_sound_bounce, "sound_bounce", "int"),
            (self._dependencies_for_sound_into_ball, "sound_into_ball", "int"),
            (self._dependencies_for_sound_outof_ball, "sound_outof_ball", "int"),
            (self._dependencies_for_sound, "sound", "int"),
            (self._dependencies_for_sound_boost, "sound_boost", "int"),
            (self._dependencies_for_sound_rolling, "sound_rolling", "int"),
            (self._dependencies_for_boost_ing_spot_blob_effect, "boost_ing_spot_blob_effect", "AssetId"),
            (self._dependencies_for_boost_ing_spot_hit_normal_damage, "boost_ing_spot_hit_normal_damage", "AssetId"),
            (self._dependencies_for_boost_ing_spot_hit_heavy_damage, "boost_ing_spot_hit_heavy_damage", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for BoostBallGuardianData.{field_name} ({field_type}): {e}"
                )


def _decode_boost_ball_scale(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_boost_ball_speed(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_boost_ball_damage_to_morph_ball(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 7, 'di_damage': 30.0, 'di_radius': 1.5, 'di_knock_back_power': 4.0})


def _decode_boost_ball_damage_to_first_person(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 7, 'di_damage': 30.0, 'di_radius': 1.5, 'di_knock_back_power': 6.0})


def _decode_boost_ball_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_ing_spot_damage_to_morph_ball(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})


def _decode_ing_spot_damage_to_first_person(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 10.0, 'di_knock_back_power': 5.0})


def _decode_stage1(data: typing.BinaryIO, game: Game, property_size: int) -> IngBoostBallGuardianBoostData:
    return IngBoostBallGuardianBoostData.from_stream(data, game, property_size, default_override={'boost_puddle_mode_time': 15.0, 'percentage_puddle_damage_to_boost': 0.5, 'break_boost_puddle_mode_damage': 90.0, 'break_boost_mode_damage': 10.0, 'next_boost_time_min': 2.0, 'next_boost_time_max': 5.0, 'sequential_boost_attacks_min': 3, 'sequential_boost_attacks_max': 3, 'small_boost_num_bounces_min': 1, 'small_boost_num_bounces_max': 5, 'large_boost_num_bounces_min': 6, 'large_boost_num_bounces_max': 10, 'locomotion_speed_scale': 1.0, 'ing_spot_speed_scale': 1.0})


def _decode_stage2(data: typing.BinaryIO, game: Game, property_size: int) -> IngBoostBallGuardianBoostData:
    return IngBoostBallGuardianBoostData.from_stream(data, game, property_size, default_override={'boost_puddle_mode_time': 15.0, 'percentage_puddle_damage_to_boost': 0.5, 'break_boost_puddle_mode_damage': 90.0, 'break_boost_mode_damage': 10.0, 'next_boost_time_min': 2.0, 'next_boost_time_max': 5.0, 'sequential_boost_attacks_min': 3, 'sequential_boost_attacks_max': 3, 'small_boost_num_bounces_min': 1, 'small_boost_num_bounces_max': 5, 'large_boost_num_bounces_min': 6, 'large_boost_num_bounces_max': 10, 'locomotion_speed_scale': 1.0, 'ing_spot_speed_scale': 1.0})


def _decode_stage3(data: typing.BinaryIO, game: Game, property_size: int) -> IngBoostBallGuardianBoostData:
    return IngBoostBallGuardianBoostData.from_stream(data, game, property_size, default_override={'boost_puddle_mode_time': 15.0, 'percentage_puddle_damage_to_boost': 0.5, 'break_boost_puddle_mode_damage': 90.0, 'break_boost_mode_damage': 10.0, 'next_boost_time_min': 2.0, 'next_boost_time_max': 5.0, 'sequential_boost_attacks_min': 3, 'sequential_boost_attacks_max': 3, 'small_boost_num_bounces_min': 1, 'small_boost_num_bounces_max': 5, 'large_boost_num_bounces_min': 6, 'large_boost_num_bounces_max': 10, 'locomotion_speed_scale': 1.0, 'ing_spot_speed_scale': 1.0})


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xa322f51d: ('boost_ball_scale', _decode_boost_ball_scale),
    0x528d951e: ('boost_ball_mass', structs.decode_BIG_f),
    0xbea96fb7: ('boost_ball_bounciness', structs.decode_BIG_f),
    0xa25b96e1: ('boost_ball_speed', _decode_boost_ball_speed),
    0x0e1a78bd: ('boost_ball_damage_to_morph_ball', _decode_boost_ball_damage_to_morph_ball),
    0x19c3d263: ('boost_ball_damage_to_first_person', _decode_boost_ball_damage_to_first_person),
    0xd8047cba: ('boost_ball_min_damage_speed', structs.decode_BIG_f),
    0x7b21e31a: ('unknown_0x7b21e31a', structs.decode_BIG_f),
    0x18381479: ('boost_ball_model', structs.decode_BIG_L),
    0x15534429: ('boost_ball_charge_up_effect', structs.decode_BIG_L),
    0x4cceb7ad: ('boost_ball_shield_effect', structs.decode_BIG_L),
    0xe41cb449: ('boost_ball_trail_effect', structs.decode_BIG_L),
    0x6758bf01: ('sound_bounce', structs.decode_BIG_l),
    0x8d9e014f: ('sound_into_ball', structs.decode_BIG_l),
    0xe35ae4be: ('sound_outof_ball', structs.decode_BIG_l),
    0x9f7372b3: ('sound', structs.decode_BIG_l),
    0xdd69a116: ('sound_boost', structs.decode_BIG_l),
    0xbf42c3ec: ('sound_rolling', structs.decode_BIG_l),
    0x42eca523: ('boost_ball_vulnerability', _decode_boost_ball_vulnerability),
    0xee69b993: ('unknown_0xee69b993', structs.decode_BIG_l),
    0x4b2de673: ('unknown_0x4b2de673', structs.decode_BIG_l),
    0x2a7073ce: ('search_cone_angle', structs.decode_BIG_f),
    0xb0e85d53: ('unknown_0xb0e85d53', structs.decode_BIG_f),
    0x5616d5f1: ('ing_spot_damage_to_morph_ball', _decode_ing_spot_damage_to_morph_ball),
    0xed685533: ('ing_spot_damage_to_first_person', _decode_ing_spot_damage_to_first_person),
    0xd771ec43: ('boost_ing_spot_blob_effect', structs.decode_BIG_L),
    0x2009a977: ('boost_ing_spot_hit_normal_damage', structs.decode_BIG_L),
    0x62ab33a2: ('boost_ing_spot_hit_heavy_damage', structs.decode_BIG_L),
    0xbab98497: ('stage1', _decode_stage1),
    0xfe18a18f: ('stage2', _decode_stage2),
    0xc2784287: ('stage3', _decode_stage3),
}
