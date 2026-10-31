# Generated File
from __future__ import annotations

import dataclasses
import enum
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

    class WeaponGeneratorPropertiesJson(typing_extensions.TypedDict):
        damage: json_util.JsonObject
        weapon: int
        fire_sound: int
        script_weapon_type: int
        collision_checks: int
        world_collision_test: json_util.JsonObject
        unknown: bool
        locator_name: str
    

class ScriptWeaponType(enum.IntEnum):
    kSWT_EnergyProjectile = 2667276721

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


class CollisionChecks(enum.IntEnum):
    kCC_None = 2950079402
    kCC_World = 3581750714
    kCC_Actor = 2877254144
    kCC_Both = 731683444

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


@dataclasses.dataclass()
class WeaponGeneratorProperties(BaseProperty):
    damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x337f9524, original_name='Damage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    weapon: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x9ef6b290, original_name='Weapon'
        ),
    })
    fire_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x4e83f4a7, original_name='FireSound'
        ),
    })
    script_weapon_type: ScriptWeaponType = dataclasses.field(default=ScriptWeaponType.kSWT_EnergyProjectile, metadata={
        'reflection': FieldReflection[ScriptWeaponType](
            ScriptWeaponType, id=0xbada8dea, original_name='ScriptWeaponType', from_json=ScriptWeaponType.from_json, to_json=ScriptWeaponType.to_json
        ),
    })
    collision_checks: CollisionChecks = dataclasses.field(default=CollisionChecks.kCC_Both, metadata={
        'reflection': FieldReflection[CollisionChecks](
            CollisionChecks, id=0x921b78a9, original_name='CollisionChecks', from_json=CollisionChecks.from_json, to_json=CollisionChecks.to_json
        ),
    })
    world_collision_test: StaticGeometryTest = dataclasses.field(default_factory=StaticGeometryTest, metadata={
        'reflection': FieldReflection[StaticGeometryTest](
            StaticGeometryTest, id=0xfb0f9549, original_name='WorldCollisionTest', from_json=StaticGeometryTest.from_json, to_json=StaticGeometryTest.to_json
        ),
    })
    unknown: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x482d569d, original_name='Unknown'
        ),
    })
    locator_name: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xfbc6c110, original_name='LocatorName'
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
        if property_count != 8:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337f9524
        damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9ef6b290
        weapon = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4e83f4a7
        fire_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbada8dea
        script_weapon_type = ScriptWeaponType.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x921b78a9
        collision_checks = CollisionChecks.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfb0f9549
        world_collision_test = StaticGeometryTest.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x482d569d
        unknown = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfbc6c110
        locator_name = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        return cls(damage, weapon, fire_sound, script_weapon_type, collision_checks, world_collision_test, unknown, locator_name)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x08')  # 8 properties

        data.write(b'3\x7f\x95$')  # 0x337f9524
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9e\xf6\xb2\x90')  # 0x9ef6b290
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.weapon))

        data.write(b'N\x83\xf4\xa7')  # 0x4e83f4a7
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.fire_sound))

        data.write(b'\xba\xda\x8d\xea')  # 0xbada8dea
        data.write(b'\x00\x04')  # size
        self.script_weapon_type.to_stream(data, game)

        data.write(b'\x92\x1bx\xa9')  # 0x921b78a9
        data.write(b'\x00\x04')  # size
        self.collision_checks.to_stream(data, game)

        data.write(b'\xfb\x0f\x95I')  # 0xfb0f9549
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.world_collision_test.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'H-V\x9d')  # 0x482d569d
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown))

        data.write(b'\xfb\xc6\xc1\x10')  # 0xfbc6c110
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.locator_name.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("WeaponGeneratorPropertiesJson", data)
        return cls(
            damage=DamageInfo.from_json(json_data['damage']),
            weapon=json_data['weapon'],
            fire_sound=json_data['fire_sound'],
            script_weapon_type=ScriptWeaponType.from_json(json_data['script_weapon_type']),
            collision_checks=CollisionChecks.from_json(json_data['collision_checks']),
            world_collision_test=StaticGeometryTest.from_json(json_data['world_collision_test']),
            unknown=json_data['unknown'],
            locator_name=json_data['locator_name'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'damage': self.damage.to_json(),
            'weapon': self.weapon,
            'fire_sound': self.fire_sound,
            'script_weapon_type': self.script_weapon_type.to_json(),
            'collision_checks': self.collision_checks.to_json(),
            'world_collision_test': self.world_collision_test.to_json(),
            'unknown': self.unknown,
            'locator_name': self.locator_name,
        }

    def _dependencies_for_weapon(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.weapon)

    def _dependencies_for_fire_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.fire_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_weapon, "weapon", "AssetId"),
            (self._dependencies_for_fire_sound, "fire_sound", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for WeaponGeneratorProperties.{field_name} ({field_type}): {e}"
                )


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_script_weapon_type(data: typing.BinaryIO, game: Game, property_size: int) -> ScriptWeaponType:
    return ScriptWeaponType.from_stream(data, game)


def _decode_collision_checks(data: typing.BinaryIO, game: Game, property_size: int) -> CollisionChecks:
    return CollisionChecks.from_stream(data, game)


def _decode_world_collision_test(data: typing.BinaryIO, game: Game, property_size: int) -> StaticGeometryTest:
    return StaticGeometryTest.from_stream(data, game, property_size)


def _decode_locator_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x337f9524: ('damage', _decode_damage),
    0x9ef6b290: ('weapon', structs.decode_BIG_Q),
    0x4e83f4a7: ('fire_sound', structs.decode_BIG_Q),
    0xbada8dea: ('script_weapon_type', _decode_script_weapon_type),
    0x921b78a9: ('collision_checks', _decode_collision_checks),
    0xfb0f9549: ('world_collision_test', _decode_world_collision_test),
    0x482d569d: ('unknown', structs.decode_BIG_bool_),
    0xfbc6c110: ('locator_name', _decode_locator_name),
}
