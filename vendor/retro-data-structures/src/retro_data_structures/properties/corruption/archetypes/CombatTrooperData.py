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
    class CombatTrooperDataJson(typing_extensions.TypedDict):
        start_on_task: bool
        cover_search_radius: float
        min_time_between_attacks: float
        max_time_between_attacks: float
        min_attack_time: float
        max_attack_time: float
        min_cover_attack_time: float
        max_cover_attack_time: float
        unknown: int
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x1c81f07, 0x820cf2de, 0x95e7a2c2, 0x76ba1c18, 0x2edf3368, 0x7d792b8c, 0x1109ad02, 0x15939c28, 0x761ed7af)


@dataclasses.dataclass()
class CombatTrooperData(BaseProperty):
    start_on_task: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x01c81f07, original_name='StartOnTask'
        ),
    })
    cover_search_radius: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x820cf2de, original_name='CoverSearchRadius'
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
    min_attack_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2edf3368, original_name='MinAttackTime'
        ),
    })
    max_attack_time: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7d792b8c, original_name='MaxAttackTime'
        ),
    })
    min_cover_attack_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1109ad02, original_name='MinCoverAttackTime'
        ),
    })
    max_cover_attack_time: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x15939c28, original_name='MaxCoverAttackTime'
        ),
    })
    unknown: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x761ed7af, original_name='Unknown'
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
        if property_count != 9:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LH?LHfLHfLHfLHfLHfLHfLHfLHl')
    
        dec = _FAST_FORMAT.unpack(data.read(87))
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

        data.write(b'\x01\xc8\x1f\x07')  # 0x1c81f07
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.start_on_task))

        data.write(b'\x82\x0c\xf2\xde')  # 0x820cf2de
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.cover_search_radius))

        data.write(b'\x95\xe7\xa2\xc2')  # 0x95e7a2c2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_attacks))

        data.write(b'v\xba\x1c\x18')  # 0x76ba1c18
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_time_between_attacks))

        data.write(b'.\xdf3h')  # 0x2edf3368
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_attack_time))

        data.write(b'}y+\x8c')  # 0x7d792b8c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_attack_time))

        data.write(b'\x11\t\xad\x02')  # 0x1109ad02
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_cover_attack_time))

        data.write(b'\x15\x93\x9c(')  # 0x15939c28
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_cover_attack_time))

        data.write(b'v\x1e\xd7\xaf')  # 0x761ed7af
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CombatTrooperDataJson", data)
        return cls(
            start_on_task=json_data['start_on_task'],
            cover_search_radius=json_data['cover_search_radius'],
            min_time_between_attacks=json_data['min_time_between_attacks'],
            max_time_between_attacks=json_data['max_time_between_attacks'],
            min_attack_time=json_data['min_attack_time'],
            max_attack_time=json_data['max_attack_time'],
            min_cover_attack_time=json_data['min_cover_attack_time'],
            max_cover_attack_time=json_data['max_cover_attack_time'],
            unknown=json_data['unknown'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'start_on_task': self.start_on_task,
            'cover_search_radius': self.cover_search_radius,
            'min_time_between_attacks': self.min_time_between_attacks,
            'max_time_between_attacks': self.max_time_between_attacks,
            'min_attack_time': self.min_attack_time,
            'max_attack_time': self.max_attack_time,
            'min_cover_attack_time': self.min_cover_attack_time,
            'max_cover_attack_time': self.max_cover_attack_time,
            'unknown': self.unknown,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x01c81f07: ('start_on_task', structs.decode_BIG_bool_),
    0x820cf2de: ('cover_search_radius', structs.decode_BIG_f),
    0x95e7a2c2: ('min_time_between_attacks', structs.decode_BIG_f),
    0x76ba1c18: ('max_time_between_attacks', structs.decode_BIG_f),
    0x2edf3368: ('min_attack_time', structs.decode_BIG_f),
    0x7d792b8c: ('max_attack_time', structs.decode_BIG_f),
    0x1109ad02: ('min_cover_attack_time', structs.decode_BIG_f),
    0x15939c28: ('max_cover_attack_time', structs.decode_BIG_f),
    0x761ed7af: ('unknown', structs.decode_BIG_l),
}
