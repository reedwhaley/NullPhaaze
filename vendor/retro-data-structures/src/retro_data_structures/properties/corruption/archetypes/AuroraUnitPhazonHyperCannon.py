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
from retro_data_structures.properties.corruption.archetypes.AuroraUnit2AttackChance import AuroraUnit2AttackChance
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class AuroraUnitPhazonHyperCannonJson(typing_extensions.TypedDict):
        projectile: int
        damage: json_util.JsonObject
        max_turn_speed: float
        next_attack_chance: json_util.JsonObject
    

@dataclasses.dataclass()
class AuroraUnitPhazonHyperCannon(BaseProperty):
    projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xef485db9, original_name='Projectile'
        ),
    })
    damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x337f9524, original_name='Damage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    max_turn_speed: float = dataclasses.field(default=45.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0b5c3c1a, original_name='MaxTurnSpeed'
        ),
    })
    next_attack_chance: AuroraUnit2AttackChance = dataclasses.field(default_factory=AuroraUnit2AttackChance, metadata={
        'reflection': FieldReflection[AuroraUnit2AttackChance](
            AuroraUnit2AttackChance, id=0x659df76d, original_name='NextAttackChance', from_json=AuroraUnit2AttackChance.from_json, to_json=AuroraUnit2AttackChance.to_json
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
        if property_count != 4:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xef485db9
        projectile = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337f9524
        damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0b5c3c1a
        max_turn_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x659df76d
        next_attack_chance = AuroraUnit2AttackChance.from_stream(data, game, property_size)
    
        return cls(projectile, damage, max_turn_speed, next_attack_chance)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x04')  # 4 properties

        data.write(b'\xefH]\xb9')  # 0xef485db9
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.projectile))

        data.write(b'3\x7f\x95$')  # 0x337f9524
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x0b\\<\x1a')  # 0xb5c3c1a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_turn_speed))

        data.write(b'e\x9d\xf7m')  # 0x659df76d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.next_attack_chance.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("AuroraUnitPhazonHyperCannonJson", data)
        return cls(
            projectile=json_data['projectile'],
            damage=DamageInfo.from_json(json_data['damage']),
            max_turn_speed=json_data['max_turn_speed'],
            next_attack_chance=AuroraUnit2AttackChance.from_json(json_data['next_attack_chance']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'projectile': self.projectile,
            'damage': self.damage.to_json(),
            'max_turn_speed': self.max_turn_speed,
            'next_attack_chance': self.next_attack_chance.to_json(),
        }

    def _dependencies_for_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_projectile(asset_manager)


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_next_attack_chance(data: typing.BinaryIO, game: Game, property_size: int) -> AuroraUnit2AttackChance:
    return AuroraUnit2AttackChance.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xef485db9: ('projectile', structs.decode_BIG_Q),
    0x337f9524: ('damage', _decode_damage),
    0x0b5c3c1a: ('max_turn_speed', structs.decode_BIG_f),
    0x659df76d: ('next_attack_chance', _decode_next_attack_chance),
}
