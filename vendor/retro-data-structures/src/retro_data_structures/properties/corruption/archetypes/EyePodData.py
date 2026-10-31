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
from retro_data_structures.properties.corruption.archetypes.EyePodHypermodeData import EyePodHypermodeData
from retro_data_structures.properties.corruption.archetypes.StaticGeometryTest import StaticGeometryTest
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class EyePodDataJson(typing_extensions.TypedDict):
        hearing_range: float
        lose_interest_distance: float
        lose_interest_time: float
        min_time_between_attacks: float
        max_time_between_attacks: float
        min_shots_in_a_burst: int
        max_shots_in_a_burst: int
        min_time_between_rapid_shots: float
        max_time_between_rapid_shots: float
        min_charge_time: float
        max_charge_time: float
        min_charge_attack_frequency: float
        max_charge_attack_frequency: float
        rapid_fire_projectile: int
        charge_shot_projectile: int
        rapid_fire_damage_info: json_util.JsonObject
        charge_shot_damage_info: json_util.JsonObject
        shot_angle_variance: float
        charge_shot_enabled: bool
        unknown: float
        turn_anim_speed: float
        hypermode_data: json_util.JsonObject
        hard_hypermode_data: json_util.JsonObject
        elite_hypermode_data: json_util.JsonObject
        starts_invulnerable: bool
        stand_in_place: bool
        shot_collision_test: json_util.JsonObject
    

@dataclasses.dataclass()
class EyePodData(BaseProperty):
    hearing_range: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x25474550, original_name='HearingRange'
        ),
    })
    lose_interest_distance: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf6b051b3, original_name='LoseInterestDistance'
        ),
    })
    lose_interest_time: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf8b0c2bb, original_name='LoseInterestTime'
        ),
    })
    min_time_between_attacks: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x95e7a2c2, original_name='MinTimeBetweenAttacks'
        ),
    })
    max_time_between_attacks: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x76ba1c18, original_name='MaxTimeBetweenAttacks'
        ),
    })
    min_shots_in_a_burst: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x64d482d5, original_name='MinShotsInABurst'
        ),
    })
    max_shots_in_a_burst: int = dataclasses.field(default=4, metadata={
        'reflection': FieldReflection[int](
            int, id=0xc3e002ac, original_name='MaxShotsInABurst'
        ),
    })
    min_time_between_rapid_shots: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4da7906b, original_name='MinTimeBetweenRapidShots'
        ),
    })
    max_time_between_rapid_shots: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa2258e11, original_name='MaxTimeBetweenRapidShots'
        ),
    })
    min_charge_time: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb6a0464c, original_name='MinChargeTime'
        ),
    })
    max_charge_time: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe5065ea8, original_name='MaxChargeTime'
        ),
    })
    min_charge_attack_frequency: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x88f13a51, original_name='MinChargeAttackFrequency'
        ),
    })
    max_charge_attack_frequency: float = dataclasses.field(default=7.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6773242b, original_name='MaxChargeAttackFrequency'
        ),
    })
    rapid_fire_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe8c819e6, original_name='RapidFireProjectile'
        ),
    })
    charge_shot_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb14fea52, original_name='ChargeShotProjectile'
        ),
    })
    rapid_fire_damage_info: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xc93109e7, original_name='RapidFireDamageInfo', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    charge_shot_damage_info: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x37a6f562, original_name='ChargeShotDamageInfo', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    shot_angle_variance: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd75f9cf2, original_name='ShotAngleVariance'
        ),
    })
    charge_shot_enabled: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x7076d432, original_name='ChargeShotEnabled'
        ),
    })
    unknown: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3db05763, original_name='Unknown'
        ),
    })
    turn_anim_speed: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x190cb8d7, original_name='TurnAnimSpeed'
        ),
    })
    hypermode_data: EyePodHypermodeData = dataclasses.field(default_factory=EyePodHypermodeData, metadata={
        'reflection': FieldReflection[EyePodHypermodeData](
            EyePodHypermodeData, id=0x5b0a8c8a, original_name='HypermodeData', from_json=EyePodHypermodeData.from_json, to_json=EyePodHypermodeData.to_json
        ),
    })
    hard_hypermode_data: EyePodHypermodeData = dataclasses.field(default_factory=EyePodHypermodeData, metadata={
        'reflection': FieldReflection[EyePodHypermodeData](
            EyePodHypermodeData, id=0x0ce679bb, original_name='HardHypermodeData', from_json=EyePodHypermodeData.from_json, to_json=EyePodHypermodeData.to_json
        ),
    })
    elite_hypermode_data: EyePodHypermodeData = dataclasses.field(default_factory=EyePodHypermodeData, metadata={
        'reflection': FieldReflection[EyePodHypermodeData](
            EyePodHypermodeData, id=0xf9bbcc33, original_name='EliteHypermodeData', from_json=EyePodHypermodeData.from_json, to_json=EyePodHypermodeData.to_json
        ),
    })
    starts_invulnerable: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xf1c247ff, original_name='StartsInvulnerable'
        ),
    })
    stand_in_place: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xa1ed5408, original_name='StandInPlace'
        ),
    })
    shot_collision_test: StaticGeometryTest = dataclasses.field(default_factory=StaticGeometryTest, metadata={
        'reflection': FieldReflection[StaticGeometryTest](
            StaticGeometryTest, id=0x511961d4, original_name='ShotCollisionTest', from_json=StaticGeometryTest.from_json, to_json=StaticGeometryTest.to_json
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
        assert property_id == 0x25474550
        hearing_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf6b051b3
        lose_interest_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf8b0c2bb
        lose_interest_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95e7a2c2
        min_time_between_attacks = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76ba1c18
        max_time_between_attacks = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64d482d5
        min_shots_in_a_burst = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc3e002ac
        max_shots_in_a_burst = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4da7906b
        min_time_between_rapid_shots = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa2258e11
        max_time_between_rapid_shots = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb6a0464c
        min_charge_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe5065ea8
        max_charge_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x88f13a51
        min_charge_attack_frequency = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6773242b
        max_charge_attack_frequency = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe8c819e6
        rapid_fire_projectile = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb14fea52
        charge_shot_projectile = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc93109e7
        rapid_fire_damage_info = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x37a6f562
        charge_shot_damage_info = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd75f9cf2
        shot_angle_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7076d432
        charge_shot_enabled = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3db05763
        unknown = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x190cb8d7
        turn_anim_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5b0a8c8a
        hypermode_data = EyePodHypermodeData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0ce679bb
        hard_hypermode_data = EyePodHypermodeData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf9bbcc33
        elite_hypermode_data = EyePodHypermodeData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf1c247ff
        starts_invulnerable = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa1ed5408
        stand_in_place = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x511961d4
        shot_collision_test = StaticGeometryTest.from_stream(data, game, property_size)
    
        return cls(hearing_range, lose_interest_distance, lose_interest_time, min_time_between_attacks, max_time_between_attacks, min_shots_in_a_burst, max_shots_in_a_burst, min_time_between_rapid_shots, max_time_between_rapid_shots, min_charge_time, max_charge_time, min_charge_attack_frequency, max_charge_attack_frequency, rapid_fire_projectile, charge_shot_projectile, rapid_fire_damage_info, charge_shot_damage_info, shot_angle_variance, charge_shot_enabled, unknown, turn_anim_speed, hypermode_data, hard_hypermode_data, elite_hypermode_data, starts_invulnerable, stand_in_place, shot_collision_test)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x1b')  # 27 properties

        data.write(b'%GEP')  # 0x25474550
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hearing_range))

        data.write(b'\xf6\xb0Q\xb3')  # 0xf6b051b3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.lose_interest_distance))

        data.write(b'\xf8\xb0\xc2\xbb')  # 0xf8b0c2bb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.lose_interest_time))

        data.write(b'\x95\xe7\xa2\xc2')  # 0x95e7a2c2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_attacks))

        data.write(b'v\xba\x1c\x18')  # 0x76ba1c18
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_time_between_attacks))

        data.write(b'd\xd4\x82\xd5')  # 0x64d482d5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.min_shots_in_a_burst))

        data.write(b'\xc3\xe0\x02\xac')  # 0xc3e002ac
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_shots_in_a_burst))

        data.write(b'M\xa7\x90k')  # 0x4da7906b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_rapid_shots))

        data.write(b'\xa2%\x8e\x11')  # 0xa2258e11
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_time_between_rapid_shots))

        data.write(b'\xb6\xa0FL')  # 0xb6a0464c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_charge_time))

        data.write(b'\xe5\x06^\xa8')  # 0xe5065ea8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_charge_time))

        data.write(b'\x88\xf1:Q')  # 0x88f13a51
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_charge_attack_frequency))

        data.write(b'gs$+')  # 0x6773242b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_charge_attack_frequency))

        data.write(b'\xe8\xc8\x19\xe6')  # 0xe8c819e6
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.rapid_fire_projectile))

        data.write(b'\xb1O\xeaR')  # 0xb14fea52
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.charge_shot_projectile))

        data.write(b'\xc91\t\xe7')  # 0xc93109e7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.rapid_fire_damage_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'7\xa6\xf5b')  # 0x37a6f562
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.charge_shot_damage_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd7_\x9c\xf2')  # 0xd75f9cf2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.shot_angle_variance))

        data.write(b'pv\xd42')  # 0x7076d432
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.charge_shot_enabled))

        data.write(b'=\xb0Wc')  # 0x3db05763
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b'\x19\x0c\xb8\xd7')  # 0x190cb8d7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.turn_anim_speed))

        data.write(b'[\n\x8c\x8a')  # 0x5b0a8c8a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hypermode_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x0c\xe6y\xbb')  # 0xce679bb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hard_hypermode_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf9\xbb\xcc3')  # 0xf9bbcc33
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.elite_hypermode_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf1\xc2G\xff')  # 0xf1c247ff
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.starts_invulnerable))

        data.write(b'\xa1\xedT\x08')  # 0xa1ed5408
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.stand_in_place))

        data.write(b'Q\x19a\xd4')  # 0x511961d4
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shot_collision_test.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("EyePodDataJson", data)
        return cls(
            hearing_range=json_data['hearing_range'],
            lose_interest_distance=json_data['lose_interest_distance'],
            lose_interest_time=json_data['lose_interest_time'],
            min_time_between_attacks=json_data['min_time_between_attacks'],
            max_time_between_attacks=json_data['max_time_between_attacks'],
            min_shots_in_a_burst=json_data['min_shots_in_a_burst'],
            max_shots_in_a_burst=json_data['max_shots_in_a_burst'],
            min_time_between_rapid_shots=json_data['min_time_between_rapid_shots'],
            max_time_between_rapid_shots=json_data['max_time_between_rapid_shots'],
            min_charge_time=json_data['min_charge_time'],
            max_charge_time=json_data['max_charge_time'],
            min_charge_attack_frequency=json_data['min_charge_attack_frequency'],
            max_charge_attack_frequency=json_data['max_charge_attack_frequency'],
            rapid_fire_projectile=json_data['rapid_fire_projectile'],
            charge_shot_projectile=json_data['charge_shot_projectile'],
            rapid_fire_damage_info=DamageInfo.from_json(json_data['rapid_fire_damage_info']),
            charge_shot_damage_info=DamageInfo.from_json(json_data['charge_shot_damage_info']),
            shot_angle_variance=json_data['shot_angle_variance'],
            charge_shot_enabled=json_data['charge_shot_enabled'],
            unknown=json_data['unknown'],
            turn_anim_speed=json_data['turn_anim_speed'],
            hypermode_data=EyePodHypermodeData.from_json(json_data['hypermode_data']),
            hard_hypermode_data=EyePodHypermodeData.from_json(json_data['hard_hypermode_data']),
            elite_hypermode_data=EyePodHypermodeData.from_json(json_data['elite_hypermode_data']),
            starts_invulnerable=json_data['starts_invulnerable'],
            stand_in_place=json_data['stand_in_place'],
            shot_collision_test=StaticGeometryTest.from_json(json_data['shot_collision_test']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'hearing_range': self.hearing_range,
            'lose_interest_distance': self.lose_interest_distance,
            'lose_interest_time': self.lose_interest_time,
            'min_time_between_attacks': self.min_time_between_attacks,
            'max_time_between_attacks': self.max_time_between_attacks,
            'min_shots_in_a_burst': self.min_shots_in_a_burst,
            'max_shots_in_a_burst': self.max_shots_in_a_burst,
            'min_time_between_rapid_shots': self.min_time_between_rapid_shots,
            'max_time_between_rapid_shots': self.max_time_between_rapid_shots,
            'min_charge_time': self.min_charge_time,
            'max_charge_time': self.max_charge_time,
            'min_charge_attack_frequency': self.min_charge_attack_frequency,
            'max_charge_attack_frequency': self.max_charge_attack_frequency,
            'rapid_fire_projectile': self.rapid_fire_projectile,
            'charge_shot_projectile': self.charge_shot_projectile,
            'rapid_fire_damage_info': self.rapid_fire_damage_info.to_json(),
            'charge_shot_damage_info': self.charge_shot_damage_info.to_json(),
            'shot_angle_variance': self.shot_angle_variance,
            'charge_shot_enabled': self.charge_shot_enabled,
            'unknown': self.unknown,
            'turn_anim_speed': self.turn_anim_speed,
            'hypermode_data': self.hypermode_data.to_json(),
            'hard_hypermode_data': self.hard_hypermode_data.to_json(),
            'elite_hypermode_data': self.elite_hypermode_data.to_json(),
            'starts_invulnerable': self.starts_invulnerable,
            'stand_in_place': self.stand_in_place,
            'shot_collision_test': self.shot_collision_test.to_json(),
        }

    def _dependencies_for_rapid_fire_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.rapid_fire_projectile)

    def _dependencies_for_charge_shot_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.charge_shot_projectile)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_rapid_fire_projectile, "rapid_fire_projectile", "AssetId"),
            (self._dependencies_for_charge_shot_projectile, "charge_shot_projectile", "AssetId"),
            (self.hypermode_data.dependencies_for, "hypermode_data", "EyePodHypermodeData"),
            (self.hard_hypermode_data.dependencies_for, "hard_hypermode_data", "EyePodHypermodeData"),
            (self.elite_hypermode_data.dependencies_for, "elite_hypermode_data", "EyePodHypermodeData"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for EyePodData.{field_name} ({field_type}): {e}"
                )


def _decode_rapid_fire_damage_info(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_charge_shot_damage_info(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_hypermode_data(data: typing.BinaryIO, game: Game, property_size: int) -> EyePodHypermodeData:
    return EyePodHypermodeData.from_stream(data, game, property_size)


def _decode_hard_hypermode_data(data: typing.BinaryIO, game: Game, property_size: int) -> EyePodHypermodeData:
    return EyePodHypermodeData.from_stream(data, game, property_size)


def _decode_elite_hypermode_data(data: typing.BinaryIO, game: Game, property_size: int) -> EyePodHypermodeData:
    return EyePodHypermodeData.from_stream(data, game, property_size)


def _decode_shot_collision_test(data: typing.BinaryIO, game: Game, property_size: int) -> StaticGeometryTest:
    return StaticGeometryTest.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x25474550: ('hearing_range', structs.decode_BIG_f),
    0xf6b051b3: ('lose_interest_distance', structs.decode_BIG_f),
    0xf8b0c2bb: ('lose_interest_time', structs.decode_BIG_f),
    0x95e7a2c2: ('min_time_between_attacks', structs.decode_BIG_f),
    0x76ba1c18: ('max_time_between_attacks', structs.decode_BIG_f),
    0x64d482d5: ('min_shots_in_a_burst', structs.decode_BIG_l),
    0xc3e002ac: ('max_shots_in_a_burst', structs.decode_BIG_l),
    0x4da7906b: ('min_time_between_rapid_shots', structs.decode_BIG_f),
    0xa2258e11: ('max_time_between_rapid_shots', structs.decode_BIG_f),
    0xb6a0464c: ('min_charge_time', structs.decode_BIG_f),
    0xe5065ea8: ('max_charge_time', structs.decode_BIG_f),
    0x88f13a51: ('min_charge_attack_frequency', structs.decode_BIG_f),
    0x6773242b: ('max_charge_attack_frequency', structs.decode_BIG_f),
    0xe8c819e6: ('rapid_fire_projectile', structs.decode_BIG_Q),
    0xb14fea52: ('charge_shot_projectile', structs.decode_BIG_Q),
    0xc93109e7: ('rapid_fire_damage_info', _decode_rapid_fire_damage_info),
    0x37a6f562: ('charge_shot_damage_info', _decode_charge_shot_damage_info),
    0xd75f9cf2: ('shot_angle_variance', structs.decode_BIG_f),
    0x7076d432: ('charge_shot_enabled', structs.decode_BIG_bool_),
    0x3db05763: ('unknown', structs.decode_BIG_f),
    0x190cb8d7: ('turn_anim_speed', structs.decode_BIG_f),
    0x5b0a8c8a: ('hypermode_data', _decode_hypermode_data),
    0x0ce679bb: ('hard_hypermode_data', _decode_hard_hypermode_data),
    0xf9bbcc33: ('elite_hypermode_data', _decode_elite_hypermode_data),
    0xf1c247ff: ('starts_invulnerable', structs.decode_BIG_bool_),
    0xa1ed5408: ('stand_in_place', structs.decode_BIG_bool_),
    0x511961d4: ('shot_collision_test', _decode_shot_collision_test),
}
