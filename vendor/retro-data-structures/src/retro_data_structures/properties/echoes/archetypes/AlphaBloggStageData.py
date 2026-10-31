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

if typing.TYPE_CHECKING:
    class AlphaBloggStageDataJson(typing_extensions.TypedDict):
        min_attacks_before_triple_charge: int
        max_attacks_before_triple_charge: int
        chance_to_charge_without_projectile_attack: float
        chance_to_charge_after_projectile_attack: float
        chance_to_open_mouth_during_charge: float
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x3e505ddb, 0x118f1e46, 0x6e603df2, 0x1e74f1ec, 0xecba9fb2)


@dataclasses.dataclass()
class AlphaBloggStageData(BaseProperty):
    min_attacks_before_triple_charge: int = dataclasses.field(default=-2143184152, metadata={
        'reflection': FieldReflection[int](
            int, id=0x3e505ddb, original_name='MinAttacksBeforeTripleCharge'
        ),
    })
    max_attacks_before_triple_charge: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x118f1e46, original_name='MaxAttacksBeforeTripleCharge'
        ),
    })
    chance_to_charge_without_projectile_attack: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6e603df2, original_name='ChanceToChargeWithoutProjectileAttack'
        ),
    })
    chance_to_charge_after_projectile_attack: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1e74f1ec, original_name='ChanceToChargeAfterProjectileAttack'
        ),
    })
    chance_to_open_mouth_during_charge: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xecba9fb2, original_name='ChanceToOpenMouthDuringCharge'
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
        if property_count != 5:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHlLHlLHfLHfLHf')
    
        dec = _FAST_FORMAT.unpack(data.read(50))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x05')  # 5 properties

        data.write(b'>P]\xdb')  # 0x3e505ddb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.min_attacks_before_triple_charge))

        data.write(b'\x11\x8f\x1eF')  # 0x118f1e46
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_attacks_before_triple_charge))

        data.write(b'n`=\xf2')  # 0x6e603df2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.chance_to_charge_without_projectile_attack))

        data.write(b'\x1et\xf1\xec')  # 0x1e74f1ec
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.chance_to_charge_after_projectile_attack))

        data.write(b'\xec\xba\x9f\xb2')  # 0xecba9fb2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.chance_to_open_mouth_during_charge))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("AlphaBloggStageDataJson", data)
        return cls(
            min_attacks_before_triple_charge=json_data['min_attacks_before_triple_charge'],
            max_attacks_before_triple_charge=json_data['max_attacks_before_triple_charge'],
            chance_to_charge_without_projectile_attack=json_data['chance_to_charge_without_projectile_attack'],
            chance_to_charge_after_projectile_attack=json_data['chance_to_charge_after_projectile_attack'],
            chance_to_open_mouth_during_charge=json_data['chance_to_open_mouth_during_charge'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'min_attacks_before_triple_charge': self.min_attacks_before_triple_charge,
            'max_attacks_before_triple_charge': self.max_attacks_before_triple_charge,
            'chance_to_charge_without_projectile_attack': self.chance_to_charge_without_projectile_attack,
            'chance_to_charge_after_projectile_attack': self.chance_to_charge_after_projectile_attack,
            'chance_to_open_mouth_during_charge': self.chance_to_open_mouth_during_charge,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x3e505ddb: ('min_attacks_before_triple_charge', structs.decode_BIG_l),
    0x118f1e46: ('max_attacks_before_triple_charge', structs.decode_BIG_l),
    0x6e603df2: ('chance_to_charge_without_projectile_attack', structs.decode_BIG_f),
    0x1e74f1ec: ('chance_to_charge_after_projectile_attack', structs.decode_BIG_f),
    0xecba9fb2: ('chance_to_open_mouth_during_charge', structs.decode_BIG_f),
}
