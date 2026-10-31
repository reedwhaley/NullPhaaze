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
from retro_data_structures.properties.corruption.archetypes.GhorClawData import GhorClawData
from retro_data_structures.properties.corruption.archetypes.HoverThenHomeProjectile import HoverThenHomeProjectile
from retro_data_structures.properties.corruption.archetypes.LaunchProjectileData import LaunchProjectileData
from retro_data_structures.properties.corruption.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class GhorWeaponDataJson(typing_extensions.TypedDict):
        mini_gun_projectile: json_util.JsonObject
        beam_info: json_util.JsonObject
        beam_damage: json_util.JsonObject
        beam_constraint_angle: float
        charge_attack_damage: json_util.JsonObject
        missile_hover_then_home_projectile: json_util.JsonObject
        missile_projectile: json_util.JsonObject
        unknown: float
        missile_collision_size: json_util.JsonValue
        missile_hit_points: float
        claw: json_util.JsonObject
        melee_damage: json_util.JsonObject
    

@dataclasses.dataclass()
class GhorWeaponData(BaseProperty):
    mini_gun_projectile: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0x078a03d9, original_name='MiniGunProjectile', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    beam_info: PlasmaBeamInfo = dataclasses.field(default_factory=PlasmaBeamInfo, metadata={
        'reflection': FieldReflection[PlasmaBeamInfo](
            PlasmaBeamInfo, id=0x1598012a, original_name='BeamInfo', from_json=PlasmaBeamInfo.from_json, to_json=PlasmaBeamInfo.to_json
        ),
    })
    beam_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x13e30e4d, original_name='BeamDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    beam_constraint_angle: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4cacfae3, original_name='BeamConstraintAngle'
        ),
    })
    charge_attack_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xe79ecfd4, original_name='ChargeAttackDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    missile_hover_then_home_projectile: HoverThenHomeProjectile = dataclasses.field(default_factory=HoverThenHomeProjectile, metadata={
        'reflection': FieldReflection[HoverThenHomeProjectile](
            HoverThenHomeProjectile, id=0x603bfd21, original_name='MissileHoverThenHomeProjectile', from_json=HoverThenHomeProjectile.from_json, to_json=HoverThenHomeProjectile.to_json
        ),
    })
    missile_projectile: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0x8f4d54f9, original_name='MissileProjectile', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    unknown: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x63fee872, original_name='Unknown'
        ),
    })
    missile_collision_size: Vector = dataclasses.field(default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0xa2f2168c, original_name='MissileCollisionSize', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    missile_hit_points: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1ba35af4, original_name='MissileHitPoints'
        ),
    })
    claw: GhorClawData = dataclasses.field(default_factory=GhorClawData, metadata={
        'reflection': FieldReflection[GhorClawData](
            GhorClawData, id=0xdae21374, original_name='Claw', from_json=GhorClawData.from_json, to_json=GhorClawData.to_json
        ),
    })
    melee_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xc9416034, original_name='MeleeDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
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
        if property_count != 12:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x078a03d9
        mini_gun_projectile = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1598012a
        beam_info = PlasmaBeamInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13e30e4d
        beam_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4cacfae3
        beam_constraint_angle = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe79ecfd4
        charge_attack_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x603bfd21
        missile_hover_then_home_projectile = HoverThenHomeProjectile.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8f4d54f9
        missile_projectile = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x63fee872
        unknown = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa2f2168c
        missile_collision_size = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1ba35af4
        missile_hit_points = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdae21374
        claw = GhorClawData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc9416034
        melee_damage = DamageInfo.from_stream(data, game, property_size)
    
        return cls(mini_gun_projectile, beam_info, beam_damage, beam_constraint_angle, charge_attack_damage, missile_hover_then_home_projectile, missile_projectile, unknown, missile_collision_size, missile_hit_points, claw, melee_damage)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x0c')  # 12 properties

        data.write(b'\x07\x8a\x03\xd9')  # 0x78a03d9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.mini_gun_projectile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x15\x98\x01*')  # 0x1598012a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.beam_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x13\xe3\x0eM')  # 0x13e30e4d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.beam_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'L\xac\xfa\xe3')  # 0x4cacfae3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.beam_constraint_angle))

        data.write(b'\xe7\x9e\xcf\xd4')  # 0xe79ecfd4
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.charge_attack_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'`;\xfd!')  # 0x603bfd21
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.missile_hover_then_home_projectile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8fMT\xf9')  # 0x8f4d54f9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.missile_projectile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'c\xfe\xe8r')  # 0x63fee872
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b'\xa2\xf2\x16\x8c')  # 0xa2f2168c
        data.write(b'\x00\x0c')  # size
        self.missile_collision_size.to_stream(data, game)

        data.write(b'\x1b\xa3Z\xf4')  # 0x1ba35af4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.missile_hit_points))

        data.write(b'\xda\xe2\x13t')  # 0xdae21374
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.claw.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc9A`4')  # 0xc9416034
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.melee_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GhorWeaponDataJson", data)
        return cls(
            mini_gun_projectile=LaunchProjectileData.from_json(json_data['mini_gun_projectile']),
            beam_info=PlasmaBeamInfo.from_json(json_data['beam_info']),
            beam_damage=DamageInfo.from_json(json_data['beam_damage']),
            beam_constraint_angle=json_data['beam_constraint_angle'],
            charge_attack_damage=DamageInfo.from_json(json_data['charge_attack_damage']),
            missile_hover_then_home_projectile=HoverThenHomeProjectile.from_json(json_data['missile_hover_then_home_projectile']),
            missile_projectile=LaunchProjectileData.from_json(json_data['missile_projectile']),
            unknown=json_data['unknown'],
            missile_collision_size=Vector.from_json(json_data['missile_collision_size']),
            missile_hit_points=json_data['missile_hit_points'],
            claw=GhorClawData.from_json(json_data['claw']),
            melee_damage=DamageInfo.from_json(json_data['melee_damage']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'mini_gun_projectile': self.mini_gun_projectile.to_json(),
            'beam_info': self.beam_info.to_json(),
            'beam_damage': self.beam_damage.to_json(),
            'beam_constraint_angle': self.beam_constraint_angle,
            'charge_attack_damage': self.charge_attack_damage.to_json(),
            'missile_hover_then_home_projectile': self.missile_hover_then_home_projectile.to_json(),
            'missile_projectile': self.missile_projectile.to_json(),
            'unknown': self.unknown,
            'missile_collision_size': self.missile_collision_size.to_json(),
            'missile_hit_points': self.missile_hit_points,
            'claw': self.claw.to_json(),
            'melee_damage': self.melee_damage.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.mini_gun_projectile.dependencies_for, "mini_gun_projectile", "LaunchProjectileData"),
            (self.beam_info.dependencies_for, "beam_info", "PlasmaBeamInfo"),
            (self.missile_hover_then_home_projectile.dependencies_for, "missile_hover_then_home_projectile", "HoverThenHomeProjectile"),
            (self.missile_projectile.dependencies_for, "missile_projectile", "LaunchProjectileData"),
            (self.claw.dependencies_for, "claw", "GhorClawData"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for GhorWeaponData.{field_name} ({field_type}): {e}"
                )


def _decode_mini_gun_projectile(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_beam_info(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size)


def _decode_beam_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_charge_attack_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_missile_hover_then_home_projectile(data: typing.BinaryIO, game: Game, property_size: int) -> HoverThenHomeProjectile:
    return HoverThenHomeProjectile.from_stream(data, game, property_size)


def _decode_missile_projectile(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_missile_collision_size(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_claw(data: typing.BinaryIO, game: Game, property_size: int) -> GhorClawData:
    return GhorClawData.from_stream(data, game, property_size)


def _decode_melee_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x078a03d9: ('mini_gun_projectile', _decode_mini_gun_projectile),
    0x1598012a: ('beam_info', _decode_beam_info),
    0x13e30e4d: ('beam_damage', _decode_beam_damage),
    0x4cacfae3: ('beam_constraint_angle', structs.decode_BIG_f),
    0xe79ecfd4: ('charge_attack_damage', _decode_charge_attack_damage),
    0x603bfd21: ('missile_hover_then_home_projectile', _decode_missile_hover_then_home_projectile),
    0x8f4d54f9: ('missile_projectile', _decode_missile_projectile),
    0x63fee872: ('unknown', structs.decode_BIG_f),
    0xa2f2168c: ('missile_collision_size', _decode_missile_collision_size),
    0x1ba35af4: ('missile_hit_points', structs.decode_BIG_f),
    0xdae21374: ('claw', _decode_claw),
    0xc9416034: ('melee_damage', _decode_melee_damage),
}
