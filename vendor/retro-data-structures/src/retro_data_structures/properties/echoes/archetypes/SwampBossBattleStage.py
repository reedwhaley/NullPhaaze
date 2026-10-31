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
    class SwampBossBattleStageJson(typing_extensions.TypedDict):
        unknown: float
        min_time_between_attacks: float
        max_time_between_attacks: float
        min_splashes_in_sequence: int
        max_splashes_in_sequence: int
        first_attack: int
        second_attack: int
        third_attack: int
        fourth_attack: int
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x98106ee2, 0x95e7a2c2, 0x76ba1c18, 0xbb0ffdd6, 0x60b0ae31, 0x9cfa9acb, 0x180f81dd, 0x42617cfd, 0xc39f864e)


@dataclasses.dataclass()
class SwampBossBattleStage(BaseProperty):
    unknown: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x98106ee2, original_name='Unknown'
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
    min_splashes_in_sequence: int = dataclasses.field(default=3, metadata={
        'reflection': FieldReflection[int](
            int, id=0xbb0ffdd6, original_name='MinSplashesInSequence'
        ),
    })
    max_splashes_in_sequence: int = dataclasses.field(default=3, metadata={
        'reflection': FieldReflection[int](
            int, id=0x60b0ae31, original_name='MaxSplashesInSequence'
        ),
    })
    first_attack: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x9cfa9acb, original_name='FirstAttack'
        ),
    })  # Choice
    second_attack: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x180f81dd, original_name='SecondAttack'
        ),
    })  # Choice
    third_attack: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x42617cfd, original_name='ThirdAttack'
        ),
    })  # Choice
    fourth_attack: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xc39f864e, original_name='FourthAttack'
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
        if property_count != 9:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHfLHfLHfLHlLHlLHLLHLLHLLHL')
    
        dec = _FAST_FORMAT.unpack(data.read(90))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
            dec[26],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\t')  # 9 properties

        data.write(b'\x98\x10n\xe2')  # 0x98106ee2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b'\x95\xe7\xa2\xc2')  # 0x95e7a2c2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_attacks))

        data.write(b'v\xba\x1c\x18')  # 0x76ba1c18
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_time_between_attacks))

        data.write(b'\xbb\x0f\xfd\xd6')  # 0xbb0ffdd6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.min_splashes_in_sequence))

        data.write(b'`\xb0\xae1')  # 0x60b0ae31
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_splashes_in_sequence))

        data.write(b'\x9c\xfa\x9a\xcb')  # 0x9cfa9acb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.first_attack))

        data.write(b'\x18\x0f\x81\xdd')  # 0x180f81dd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.second_attack))

        data.write(b'Ba|\xfd')  # 0x42617cfd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.third_attack))

        data.write(b'\xc3\x9f\x86N')  # 0xc39f864e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.fourth_attack))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SwampBossBattleStageJson", data)
        return cls(
            unknown=json_data['unknown'],
            min_time_between_attacks=json_data['min_time_between_attacks'],
            max_time_between_attacks=json_data['max_time_between_attacks'],
            min_splashes_in_sequence=json_data['min_splashes_in_sequence'],
            max_splashes_in_sequence=json_data['max_splashes_in_sequence'],
            first_attack=json_data['first_attack'],
            second_attack=json_data['second_attack'],
            third_attack=json_data['third_attack'],
            fourth_attack=json_data['fourth_attack'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'unknown': self.unknown,
            'min_time_between_attacks': self.min_time_between_attacks,
            'max_time_between_attacks': self.max_time_between_attacks,
            'min_splashes_in_sequence': self.min_splashes_in_sequence,
            'max_splashes_in_sequence': self.max_splashes_in_sequence,
            'first_attack': self.first_attack,
            'second_attack': self.second_attack,
            'third_attack': self.third_attack,
            'fourth_attack': self.fourth_attack,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x98106ee2: ('unknown', structs.decode_BIG_f),
    0x95e7a2c2: ('min_time_between_attacks', structs.decode_BIG_f),
    0x76ba1c18: ('max_time_between_attacks', structs.decode_BIG_f),
    0xbb0ffdd6: ('min_splashes_in_sequence', structs.decode_BIG_l),
    0x60b0ae31: ('max_splashes_in_sequence', structs.decode_BIG_l),
    0x9cfa9acb: ('first_attack', structs.decode_BIG_L),
    0x180f81dd: ('second_attack', structs.decode_BIG_L),
    0x42617cfd: ('third_attack', structs.decode_BIG_L),
    0xc39f864e: ('fourth_attack', structs.decode_BIG_L),
}
