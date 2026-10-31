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
    class BlinkDataJson(typing_extensions.TypedDict):
        blinking_enabled: bool
        min_time_between_blinks: float
        max_time_between_blinks: float
        max_sub_blinks: int
        min_time_between_sub_blinks: float
        max_time_between_sub_blinks: float
        unknown: float
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x47c836c5, 0x9b131110, 0xa5a6d998, 0xd9f6253b, 0x896fde0, 0x5f98ada3, 0xc3230652)


@dataclasses.dataclass()
class BlinkData(BaseProperty):
    blinking_enabled: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x47c836c5, original_name='BlinkingEnabled'
        ),
    })
    min_time_between_blinks: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9b131110, original_name='MinTimeBetweenBlinks'
        ),
    })
    max_time_between_blinks: float = dataclasses.field(default=6.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa5a6d998, original_name='MaxTimeBetweenBlinks'
        ),
    })
    max_sub_blinks: int = dataclasses.field(default=3, metadata={
        'reflection': FieldReflection[int](
            int, id=0xd9f6253b, original_name='MaxSubBlinks'
        ),
    })
    min_time_between_sub_blinks: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0896fde0, original_name='MinTimeBetweenSubBlinks'
        ),
    })
    max_time_between_sub_blinks: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5f98ada3, original_name='MaxTimeBetweenSubBlinks'
        ),
    })
    unknown: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc3230652, original_name='Unknown'
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
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LH?LHfLHfLHlLHfLHfLHf')
    
        dec = _FAST_FORMAT.unpack(data.read(67))
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

        data.write(b'G\xc86\xc5')  # 0x47c836c5
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.blinking_enabled))

        data.write(b'\x9b\x13\x11\x10')  # 0x9b131110
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_blinks))

        data.write(b'\xa5\xa6\xd9\x98')  # 0xa5a6d998
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_time_between_blinks))

        data.write(b'\xd9\xf6%;')  # 0xd9f6253b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_sub_blinks))

        data.write(b'\x08\x96\xfd\xe0')  # 0x896fde0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_sub_blinks))

        data.write(b'_\x98\xad\xa3')  # 0x5f98ada3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_time_between_sub_blinks))

        data.write(b'\xc3#\x06R')  # 0xc3230652
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("BlinkDataJson", data)
        return cls(
            blinking_enabled=json_data['blinking_enabled'],
            min_time_between_blinks=json_data['min_time_between_blinks'],
            max_time_between_blinks=json_data['max_time_between_blinks'],
            max_sub_blinks=json_data['max_sub_blinks'],
            min_time_between_sub_blinks=json_data['min_time_between_sub_blinks'],
            max_time_between_sub_blinks=json_data['max_time_between_sub_blinks'],
            unknown=json_data['unknown'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'blinking_enabled': self.blinking_enabled,
            'min_time_between_blinks': self.min_time_between_blinks,
            'max_time_between_blinks': self.max_time_between_blinks,
            'max_sub_blinks': self.max_sub_blinks,
            'min_time_between_sub_blinks': self.min_time_between_sub_blinks,
            'max_time_between_sub_blinks': self.max_time_between_sub_blinks,
            'unknown': self.unknown,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x47c836c5: ('blinking_enabled', structs.decode_BIG_bool_),
    0x9b131110: ('min_time_between_blinks', structs.decode_BIG_f),
    0xa5a6d998: ('max_time_between_blinks', structs.decode_BIG_f),
    0xd9f6253b: ('max_sub_blinks', structs.decode_BIG_l),
    0x0896fde0: ('min_time_between_sub_blinks', structs.decode_BIG_f),
    0x5f98ada3: ('max_time_between_sub_blinks', structs.decode_BIG_f),
    0xc3230652: ('unknown', structs.decode_BIG_f),
}
