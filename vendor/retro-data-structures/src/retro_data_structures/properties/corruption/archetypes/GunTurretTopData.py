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
from retro_data_structures.properties.corruption.archetypes.StaticGeometryTest import StaticGeometryTest
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class GunTurretTopDataJson(typing_extensions.TypedDict):
        is_pirate_turret: bool
        unknown_0xf54e1111: bool
        shoots_at_player: bool
        think_when_inactive: bool
        instant_hit_range: float
        projectile_world_collision_test: json_util.JsonObject
        tracking_speed: float
        panning_speed: float
        unknown_0x4b106481: float
        unknown_0xa1dd15f6: float
        min_time_between_attacks: float
        max_time_between_attacks: float
        min_time_between_shots: float
        max_time_between_shots: float
        min_shots_in_a_burst: int
        max_shots_in_a_burst: int
        federation_projectile_collision_response: int
        pirate_projectile_weapon_system: int
        projectile_damage_info: json_util.JsonObject
        unknown_0x4173ec53: float
        shot_angle_variance: float
    

@dataclasses.dataclass()
class GunTurretTopData(BaseProperty):
    is_pirate_turret: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x701d65cd, original_name='IsPirateTurret'
        ),
    })
    unknown_0xf54e1111: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xf54e1111, original_name='Unknown'
        ),
    })
    shoots_at_player: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x0a7846ec, original_name='ShootsAtPlayer'
        ),
    })
    think_when_inactive: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x5219dccd, original_name='ThinkWhenInactive'
        ),
    })
    instant_hit_range: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0bd3794d, original_name='InstantHitRange'
        ),
    })
    projectile_world_collision_test: StaticGeometryTest = dataclasses.field(default_factory=StaticGeometryTest, metadata={
        'reflection': FieldReflection[StaticGeometryTest](
            StaticGeometryTest, id=0xcfa1ace2, original_name='ProjectileWorldCollisionTest', from_json=StaticGeometryTest.from_json, to_json=StaticGeometryTest.to_json
        ),
    })
    tracking_speed: float = dataclasses.field(default=180.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfe6829ec, original_name='TrackingSpeed'
        ),
    })
    panning_speed: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4d28523e, original_name='PanningSpeed'
        ),
    })
    unknown_0x4b106481: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4b106481, original_name='Unknown'
        ),
    })
    unknown_0xa1dd15f6: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa1dd15f6, original_name='Unknown'
        ),
    })
    min_time_between_attacks: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x95e7a2c2, original_name='MinTimeBetweenAttacks'
        ),
    })
    max_time_between_attacks: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x76ba1c18, original_name='MaxTimeBetweenAttacks'
        ),
    })
    min_time_between_shots: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3eb2de35, original_name='MinTimeBetweenShots'
        ),
    })
    max_time_between_shots: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe50d8dd2, original_name='MaxTimeBetweenShots'
        ),
    })
    min_shots_in_a_burst: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x64d482d5, original_name='MinShotsInABurst'
        ),
    })
    max_shots_in_a_burst: int = dataclasses.field(default=5, metadata={
        'reflection': FieldReflection[int](
            int, id=0xc3e002ac, original_name='MaxShotsInABurst'
        ),
    })
    federation_projectile_collision_response: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CRSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x16e7d74a, original_name='FederationProjectileCollisionResponse'
        ),
    })
    pirate_projectile_weapon_system: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x00e9c72c, original_name='PirateProjectileWeaponSystem'
        ),
    })
    projectile_damage_info: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xbe7fb5cc, original_name='ProjectileDamageInfo', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    unknown_0x4173ec53: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4173ec53, original_name='Unknown'
        ),
    })
    shot_angle_variance: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd75f9cf2, original_name='ShotAngleVariance'
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
        if property_count != 21:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x701d65cd
        is_pirate_turret = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf54e1111
        unknown_0xf54e1111 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0a7846ec
        shoots_at_player = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5219dccd
        think_when_inactive = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0bd3794d
        instant_hit_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcfa1ace2
        projectile_world_collision_test = StaticGeometryTest.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfe6829ec
        tracking_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4d28523e
        panning_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4b106481
        unknown_0x4b106481 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa1dd15f6
        unknown_0xa1dd15f6 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95e7a2c2
        min_time_between_attacks = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76ba1c18
        max_time_between_attacks = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3eb2de35
        min_time_between_shots = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe50d8dd2
        max_time_between_shots = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64d482d5
        min_shots_in_a_burst = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc3e002ac
        max_shots_in_a_burst = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x16e7d74a
        federation_projectile_collision_response = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x00e9c72c
        pirate_projectile_weapon_system = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbe7fb5cc
        projectile_damage_info = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4173ec53
        unknown_0x4173ec53 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd75f9cf2
        shot_angle_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(is_pirate_turret, unknown_0xf54e1111, shoots_at_player, think_when_inactive, instant_hit_range, projectile_world_collision_test, tracking_speed, panning_speed, unknown_0x4b106481, unknown_0xa1dd15f6, min_time_between_attacks, max_time_between_attacks, min_time_between_shots, max_time_between_shots, min_shots_in_a_burst, max_shots_in_a_burst, federation_projectile_collision_response, pirate_projectile_weapon_system, projectile_damage_info, unknown_0x4173ec53, shot_angle_variance)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x15')  # 21 properties

        data.write(b'p\x1de\xcd')  # 0x701d65cd
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_pirate_turret))

        data.write(b'\xf5N\x11\x11')  # 0xf54e1111
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xf54e1111))

        data.write(b'\nxF\xec')  # 0xa7846ec
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.shoots_at_player))

        data.write(b'R\x19\xdc\xcd')  # 0x5219dccd
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.think_when_inactive))

        data.write(b'\x0b\xd3yM')  # 0xbd3794d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.instant_hit_range))

        data.write(b'\xcf\xa1\xac\xe2')  # 0xcfa1ace2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.projectile_world_collision_test.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfeh)\xec')  # 0xfe6829ec
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.tracking_speed))

        data.write(b'M(R>')  # 0x4d28523e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.panning_speed))

        data.write(b'K\x10d\x81')  # 0x4b106481
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4b106481))

        data.write(b'\xa1\xdd\x15\xf6')  # 0xa1dd15f6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa1dd15f6))

        data.write(b'\x95\xe7\xa2\xc2')  # 0x95e7a2c2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_attacks))

        data.write(b'v\xba\x1c\x18')  # 0x76ba1c18
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_time_between_attacks))

        data.write(b'>\xb2\xde5')  # 0x3eb2de35
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_shots))

        data.write(b'\xe5\r\x8d\xd2')  # 0xe50d8dd2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_time_between_shots))

        data.write(b'd\xd4\x82\xd5')  # 0x64d482d5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.min_shots_in_a_burst))

        data.write(b'\xc3\xe0\x02\xac')  # 0xc3e002ac
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_shots_in_a_burst))

        data.write(b'\x16\xe7\xd7J')  # 0x16e7d74a
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.federation_projectile_collision_response))

        data.write(b'\x00\xe9\xc7,')  # 0xe9c72c
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.pirate_projectile_weapon_system))

        data.write(b'\xbe\x7f\xb5\xcc')  # 0xbe7fb5cc
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.projectile_damage_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'As\xecS')  # 0x4173ec53
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4173ec53))

        data.write(b'\xd7_\x9c\xf2')  # 0xd75f9cf2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.shot_angle_variance))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GunTurretTopDataJson", data)
        return cls(
            is_pirate_turret=json_data['is_pirate_turret'],
            unknown_0xf54e1111=json_data['unknown_0xf54e1111'],
            shoots_at_player=json_data['shoots_at_player'],
            think_when_inactive=json_data['think_when_inactive'],
            instant_hit_range=json_data['instant_hit_range'],
            projectile_world_collision_test=StaticGeometryTest.from_json(json_data['projectile_world_collision_test']),
            tracking_speed=json_data['tracking_speed'],
            panning_speed=json_data['panning_speed'],
            unknown_0x4b106481=json_data['unknown_0x4b106481'],
            unknown_0xa1dd15f6=json_data['unknown_0xa1dd15f6'],
            min_time_between_attacks=json_data['min_time_between_attacks'],
            max_time_between_attacks=json_data['max_time_between_attacks'],
            min_time_between_shots=json_data['min_time_between_shots'],
            max_time_between_shots=json_data['max_time_between_shots'],
            min_shots_in_a_burst=json_data['min_shots_in_a_burst'],
            max_shots_in_a_burst=json_data['max_shots_in_a_burst'],
            federation_projectile_collision_response=json_data['federation_projectile_collision_response'],
            pirate_projectile_weapon_system=json_data['pirate_projectile_weapon_system'],
            projectile_damage_info=DamageInfo.from_json(json_data['projectile_damage_info']),
            unknown_0x4173ec53=json_data['unknown_0x4173ec53'],
            shot_angle_variance=json_data['shot_angle_variance'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'is_pirate_turret': self.is_pirate_turret,
            'unknown_0xf54e1111': self.unknown_0xf54e1111,
            'shoots_at_player': self.shoots_at_player,
            'think_when_inactive': self.think_when_inactive,
            'instant_hit_range': self.instant_hit_range,
            'projectile_world_collision_test': self.projectile_world_collision_test.to_json(),
            'tracking_speed': self.tracking_speed,
            'panning_speed': self.panning_speed,
            'unknown_0x4b106481': self.unknown_0x4b106481,
            'unknown_0xa1dd15f6': self.unknown_0xa1dd15f6,
            'min_time_between_attacks': self.min_time_between_attacks,
            'max_time_between_attacks': self.max_time_between_attacks,
            'min_time_between_shots': self.min_time_between_shots,
            'max_time_between_shots': self.max_time_between_shots,
            'min_shots_in_a_burst': self.min_shots_in_a_burst,
            'max_shots_in_a_burst': self.max_shots_in_a_burst,
            'federation_projectile_collision_response': self.federation_projectile_collision_response,
            'pirate_projectile_weapon_system': self.pirate_projectile_weapon_system,
            'projectile_damage_info': self.projectile_damage_info.to_json(),
            'unknown_0x4173ec53': self.unknown_0x4173ec53,
            'shot_angle_variance': self.shot_angle_variance,
        }

    def _dependencies_for_federation_projectile_collision_response(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.federation_projectile_collision_response)

    def _dependencies_for_pirate_projectile_weapon_system(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.pirate_projectile_weapon_system)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_federation_projectile_collision_response, "federation_projectile_collision_response", "AssetId"),
            (self._dependencies_for_pirate_projectile_weapon_system, "pirate_projectile_weapon_system", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for GunTurretTopData.{field_name} ({field_type}): {e}"
                )


def _decode_projectile_world_collision_test(data: typing.BinaryIO, game: Game, property_size: int) -> StaticGeometryTest:
    return StaticGeometryTest.from_stream(data, game, property_size)


def _decode_projectile_damage_info(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x701d65cd: ('is_pirate_turret', structs.decode_BIG_bool_),
    0xf54e1111: ('unknown_0xf54e1111', structs.decode_BIG_bool_),
    0x0a7846ec: ('shoots_at_player', structs.decode_BIG_bool_),
    0x5219dccd: ('think_when_inactive', structs.decode_BIG_bool_),
    0x0bd3794d: ('instant_hit_range', structs.decode_BIG_f),
    0xcfa1ace2: ('projectile_world_collision_test', _decode_projectile_world_collision_test),
    0xfe6829ec: ('tracking_speed', structs.decode_BIG_f),
    0x4d28523e: ('panning_speed', structs.decode_BIG_f),
    0x4b106481: ('unknown_0x4b106481', structs.decode_BIG_f),
    0xa1dd15f6: ('unknown_0xa1dd15f6', structs.decode_BIG_f),
    0x95e7a2c2: ('min_time_between_attacks', structs.decode_BIG_f),
    0x76ba1c18: ('max_time_between_attacks', structs.decode_BIG_f),
    0x3eb2de35: ('min_time_between_shots', structs.decode_BIG_f),
    0xe50d8dd2: ('max_time_between_shots', structs.decode_BIG_f),
    0x64d482d5: ('min_shots_in_a_burst', structs.decode_BIG_l),
    0xc3e002ac: ('max_shots_in_a_burst', structs.decode_BIG_l),
    0x16e7d74a: ('federation_projectile_collision_response', structs.decode_BIG_Q),
    0x00e9c72c: ('pirate_projectile_weapon_system', structs.decode_BIG_Q),
    0xbe7fb5cc: ('projectile_damage_info', _decode_projectile_damage_info),
    0x4173ec53: ('unknown_0x4173ec53', structs.decode_BIG_f),
    0xd75f9cf2: ('shot_angle_variance', structs.decode_BIG_f),
}
