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
    class SandwormAttackSequenceJson(typing_extensions.TypedDict):
        unknown: float
        min_time_between_sequences: float
        max_time_between_sequences: float
        move_speed_multiplier: float
        first_attack_in_sequence: int
        second_attack_in_sequence: int
        third_attack_in_sequence: int
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x98106ee2, 0x95081226, 0xc2064265, 0xfe9133cd, 0x59f14d7c, 0x9606b4b0, 0xfc2697dd)


@dataclasses.dataclass()
class SandwormAttackSequence(BaseProperty):
    unknown: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x98106ee2, original_name='Unknown'
        ),
    })
    min_time_between_sequences: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x95081226, original_name='MinTimeBetweenSequences'
        ),
    })
    max_time_between_sequences: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc2064265, original_name='MaxTimeBetweenSequences'
        ),
    })
    move_speed_multiplier: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfe9133cd, original_name='MoveSpeedMultiplier'
        ),
    })
    first_attack_in_sequence: int = dataclasses.field(default=3, metadata={
        'reflection': FieldReflection[int](
            int, id=0x59f14d7c, original_name='FirstAttackInSequence'
        ),
    })  # Choice
    second_attack_in_sequence: int = dataclasses.field(default=5, metadata={
        'reflection': FieldReflection[int](
            int, id=0x9606b4b0, original_name='SecondAttackInSequence'
        ),
    })  # Choice
    third_attack_in_sequence: int = dataclasses.field(default=5, metadata={
        'reflection': FieldReflection[int](
            int, id=0xfc2697dd, original_name='ThirdAttackInSequence'
        ),
    })  # Choice

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
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHfLHfLHfLHfLHLLHLLHL')
    
        dec = _FAST_FORMAT.unpack(data.read(70))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x07')  # 7 properties

        data.write(b'\x98\x10n\xe2')  # 0x98106ee2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b'\x95\x08\x12&')  # 0x95081226
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_sequences))

        data.write(b'\xc2\x06Be')  # 0xc2064265
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_time_between_sequences))

        data.write(b'\xfe\x913\xcd')  # 0xfe9133cd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.move_speed_multiplier))

        data.write(b'Y\xf1M|')  # 0x59f14d7c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.first_attack_in_sequence))

        data.write(b'\x96\x06\xb4\xb0')  # 0x9606b4b0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.second_attack_in_sequence))

        data.write(b'\xfc&\x97\xdd')  # 0xfc2697dd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.third_attack_in_sequence))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SandwormAttackSequenceJson", data)
        return cls(
            unknown=json_data['unknown'],
            min_time_between_sequences=json_data['min_time_between_sequences'],
            max_time_between_sequences=json_data['max_time_between_sequences'],
            move_speed_multiplier=json_data['move_speed_multiplier'],
            first_attack_in_sequence=json_data['first_attack_in_sequence'],
            second_attack_in_sequence=json_data['second_attack_in_sequence'],
            third_attack_in_sequence=json_data['third_attack_in_sequence'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'unknown': self.unknown,
            'min_time_between_sequences': self.min_time_between_sequences,
            'max_time_between_sequences': self.max_time_between_sequences,
            'move_speed_multiplier': self.move_speed_multiplier,
            'first_attack_in_sequence': self.first_attack_in_sequence,
            'second_attack_in_sequence': self.second_attack_in_sequence,
            'third_attack_in_sequence': self.third_attack_in_sequence,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x98106ee2: ('unknown', structs.decode_BIG_f),
    0x95081226: ('min_time_between_sequences', structs.decode_BIG_f),
    0xc2064265: ('max_time_between_sequences', structs.decode_BIG_f),
    0xfe9133cd: ('move_speed_multiplier', structs.decode_BIG_f),
    0x59f14d7c: ('first_attack_in_sequence', structs.decode_BIG_L),
    0x9606b4b0: ('second_attack_in_sequence', structs.decode_BIG_L),
    0xfc2697dd: ('third_attack_in_sequence', structs.decode_BIG_L),
}
