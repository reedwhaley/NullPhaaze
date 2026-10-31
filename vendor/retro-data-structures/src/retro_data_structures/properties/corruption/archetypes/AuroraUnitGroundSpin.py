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

if typing.TYPE_CHECKING:
    class AuroraUnitGroundSpinJson(typing_extensions.TypedDict):
        turn_speed: float
        movement_speed: float
        stun_damage_threshold: float
        min_ground_spin_time: float
        max_ground_spin_time: float
        damage: json_util.JsonObject
        next_attack_chance: json_util.JsonObject
    

@dataclasses.dataclass()
class AuroraUnitGroundSpin(BaseProperty):
    turn_speed: float = dataclasses.field(default=540.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x020c78bb, original_name='TurnSpeed'
        ),
    })
    movement_speed: float = dataclasses.field(default=75.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x416f15e8, original_name='MovementSpeed'
        ),
    })
    stun_damage_threshold: float = dataclasses.field(default=250.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x79d90292, original_name='StunDamageThreshold'
        ),
    })
    min_ground_spin_time: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4839dde0, original_name='MinGroundSpinTime'
        ),
    })
    max_ground_spin_time: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x092ee266, original_name='MaxGroundSpinTime'
        ),
    })
    damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x337f9524, original_name='Damage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
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
        if property_count != 7:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x020c78bb
        turn_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x416f15e8
        movement_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x79d90292
        stun_damage_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4839dde0
        min_ground_spin_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x092ee266
        max_ground_spin_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337f9524
        damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x659df76d
        next_attack_chance = AuroraUnit2AttackChance.from_stream(data, game, property_size)
    
        return cls(turn_speed, movement_speed, stun_damage_threshold, min_ground_spin_time, max_ground_spin_time, damage, next_attack_chance)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x07')  # 7 properties

        data.write(b'\x02\x0cx\xbb')  # 0x20c78bb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.turn_speed))

        data.write(b'Ao\x15\xe8')  # 0x416f15e8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.movement_speed))

        data.write(b'y\xd9\x02\x92')  # 0x79d90292
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stun_damage_threshold))

        data.write(b'H9\xdd\xe0')  # 0x4839dde0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_ground_spin_time))

        data.write(b'\t.\xe2f')  # 0x92ee266
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_ground_spin_time))

        data.write(b'3\x7f\x95$')  # 0x337f9524
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

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
        json_data = typing.cast("AuroraUnitGroundSpinJson", data)
        return cls(
            turn_speed=json_data['turn_speed'],
            movement_speed=json_data['movement_speed'],
            stun_damage_threshold=json_data['stun_damage_threshold'],
            min_ground_spin_time=json_data['min_ground_spin_time'],
            max_ground_spin_time=json_data['max_ground_spin_time'],
            damage=DamageInfo.from_json(json_data['damage']),
            next_attack_chance=AuroraUnit2AttackChance.from_json(json_data['next_attack_chance']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'turn_speed': self.turn_speed,
            'movement_speed': self.movement_speed,
            'stun_damage_threshold': self.stun_damage_threshold,
            'min_ground_spin_time': self.min_ground_spin_time,
            'max_ground_spin_time': self.max_ground_spin_time,
            'damage': self.damage.to_json(),
            'next_attack_chance': self.next_attack_chance.to_json(),
        }


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_next_attack_chance(data: typing.BinaryIO, game: Game, property_size: int) -> AuroraUnit2AttackChance:
    return AuroraUnit2AttackChance.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x020c78bb: ('turn_speed', structs.decode_BIG_f),
    0x416f15e8: ('movement_speed', structs.decode_BIG_f),
    0x79d90292: ('stun_damage_threshold', structs.decode_BIG_f),
    0x4839dde0: ('min_ground_spin_time', structs.decode_BIG_f),
    0x092ee266: ('max_ground_spin_time', structs.decode_BIG_f),
    0x337f9524: ('damage', _decode_damage),
    0x659df76d: ('next_attack_chance', _decode_next_attack_chance),
}
