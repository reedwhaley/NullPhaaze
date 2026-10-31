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
from retro_data_structures.properties.corruption.archetypes.PlayerInventoryAbilities import PlayerInventoryAbilities
from retro_data_structures.properties.corruption.archetypes.PlayerInventoryBall import PlayerInventoryBall
from retro_data_structures.properties.corruption.archetypes.PlayerInventoryHyperMode import PlayerInventoryHyperMode
from retro_data_structures.properties.corruption.archetypes.PlayerInventoryMisc import PlayerInventoryMisc
from retro_data_structures.properties.corruption.archetypes.PlayerInventoryShip import PlayerInventoryShip
from retro_data_structures.properties.corruption.archetypes.PlayerInventoryVisors import PlayerInventoryVisors
from retro_data_structures.properties.corruption.archetypes.PlayerInventoryWeapons import PlayerInventoryWeapons

if typing.TYPE_CHECKING:
    class PlayerInventoryJson(typing_extensions.TypedDict):
        misc: json_util.JsonObject
        weapons: json_util.JsonObject
        visors: json_util.JsonObject
        ball: json_util.JsonObject
        abilities: json_util.JsonObject
        hyper_mode: json_util.JsonObject
        ship: json_util.JsonObject
    

@dataclasses.dataclass()
class PlayerInventory(BaseProperty):
    misc: PlayerInventoryMisc = dataclasses.field(default_factory=PlayerInventoryMisc, metadata={
        'reflection': FieldReflection[PlayerInventoryMisc](
            PlayerInventoryMisc, id=0x52c779c0, original_name='Misc', from_json=PlayerInventoryMisc.from_json, to_json=PlayerInventoryMisc.to_json
        ),
    })
    weapons: PlayerInventoryWeapons = dataclasses.field(default_factory=PlayerInventoryWeapons, metadata={
        'reflection': FieldReflection[PlayerInventoryWeapons](
            PlayerInventoryWeapons, id=0xef43b845, original_name='Weapons', from_json=PlayerInventoryWeapons.from_json, to_json=PlayerInventoryWeapons.to_json
        ),
    })
    visors: PlayerInventoryVisors = dataclasses.field(default_factory=PlayerInventoryVisors, metadata={
        'reflection': FieldReflection[PlayerInventoryVisors](
            PlayerInventoryVisors, id=0x317d45bb, original_name='Visors', from_json=PlayerInventoryVisors.from_json, to_json=PlayerInventoryVisors.to_json
        ),
    })
    ball: PlayerInventoryBall = dataclasses.field(default_factory=PlayerInventoryBall, metadata={
        'reflection': FieldReflection[PlayerInventoryBall](
            PlayerInventoryBall, id=0xed7f3b4a, original_name='Ball', from_json=PlayerInventoryBall.from_json, to_json=PlayerInventoryBall.to_json
        ),
    })
    abilities: PlayerInventoryAbilities = dataclasses.field(default_factory=PlayerInventoryAbilities, metadata={
        'reflection': FieldReflection[PlayerInventoryAbilities](
            PlayerInventoryAbilities, id=0x267f91e5, original_name='Abilities', from_json=PlayerInventoryAbilities.from_json, to_json=PlayerInventoryAbilities.to_json
        ),
    })
    hyper_mode: PlayerInventoryHyperMode = dataclasses.field(default_factory=PlayerInventoryHyperMode, metadata={
        'reflection': FieldReflection[PlayerInventoryHyperMode](
            PlayerInventoryHyperMode, id=0x378e02b2, original_name='HyperMode', from_json=PlayerInventoryHyperMode.from_json, to_json=PlayerInventoryHyperMode.to_json
        ),
    })
    ship: PlayerInventoryShip = dataclasses.field(default_factory=PlayerInventoryShip, metadata={
        'reflection': FieldReflection[PlayerInventoryShip](
            PlayerInventoryShip, id=0xe9c4a786, original_name='Ship', from_json=PlayerInventoryShip.from_json, to_json=PlayerInventoryShip.to_json
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
        assert property_id == 0x52c779c0
        misc = PlayerInventoryMisc.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xef43b845
        weapons = PlayerInventoryWeapons.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x317d45bb
        visors = PlayerInventoryVisors.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed7f3b4a
        ball = PlayerInventoryBall.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x267f91e5
        abilities = PlayerInventoryAbilities.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x378e02b2
        hyper_mode = PlayerInventoryHyperMode.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe9c4a786
        ship = PlayerInventoryShip.from_stream(data, game, property_size)
    
        return cls(misc, weapons, visors, ball, abilities, hyper_mode, ship)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x07')  # 7 properties

        data.write(b'R\xc7y\xc0')  # 0x52c779c0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.misc.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xefC\xb8E')  # 0xef43b845
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.weapons.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'1}E\xbb')  # 0x317d45bb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.visors.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xed\x7f;J')  # 0xed7f3b4a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ball.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'&\x7f\x91\xe5')  # 0x267f91e5
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.abilities.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'7\x8e\x02\xb2')  # 0x378e02b2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper_mode.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe9\xc4\xa7\x86')  # 0xe9c4a786
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ship.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlayerInventoryJson", data)
        return cls(
            misc=PlayerInventoryMisc.from_json(json_data['misc']),
            weapons=PlayerInventoryWeapons.from_json(json_data['weapons']),
            visors=PlayerInventoryVisors.from_json(json_data['visors']),
            ball=PlayerInventoryBall.from_json(json_data['ball']),
            abilities=PlayerInventoryAbilities.from_json(json_data['abilities']),
            hyper_mode=PlayerInventoryHyperMode.from_json(json_data['hyper_mode']),
            ship=PlayerInventoryShip.from_json(json_data['ship']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'misc': self.misc.to_json(),
            'weapons': self.weapons.to_json(),
            'visors': self.visors.to_json(),
            'ball': self.ball.to_json(),
            'abilities': self.abilities.to_json(),
            'hyper_mode': self.hyper_mode.to_json(),
            'ship': self.ship.to_json(),
        }


def _decode_misc(data: typing.BinaryIO, game: Game, property_size: int) -> PlayerInventoryMisc:
    return PlayerInventoryMisc.from_stream(data, game, property_size)


def _decode_weapons(data: typing.BinaryIO, game: Game, property_size: int) -> PlayerInventoryWeapons:
    return PlayerInventoryWeapons.from_stream(data, game, property_size)


def _decode_visors(data: typing.BinaryIO, game: Game, property_size: int) -> PlayerInventoryVisors:
    return PlayerInventoryVisors.from_stream(data, game, property_size)


def _decode_ball(data: typing.BinaryIO, game: Game, property_size: int) -> PlayerInventoryBall:
    return PlayerInventoryBall.from_stream(data, game, property_size)


def _decode_abilities(data: typing.BinaryIO, game: Game, property_size: int) -> PlayerInventoryAbilities:
    return PlayerInventoryAbilities.from_stream(data, game, property_size)


def _decode_hyper_mode(data: typing.BinaryIO, game: Game, property_size: int) -> PlayerInventoryHyperMode:
    return PlayerInventoryHyperMode.from_stream(data, game, property_size)


def _decode_ship(data: typing.BinaryIO, game: Game, property_size: int) -> PlayerInventoryShip:
    return PlayerInventoryShip.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x52c779c0: ('misc', _decode_misc),
    0xef43b845: ('weapons', _decode_weapons),
    0x317d45bb: ('visors', _decode_visors),
    0xed7f3b4a: ('ball', _decode_ball),
    0x267f91e5: ('abilities', _decode_abilities),
    0x378e02b2: ('hyper_mode', _decode_hyper_mode),
    0xe9c4a786: ('ship', _decode_ship),
}
