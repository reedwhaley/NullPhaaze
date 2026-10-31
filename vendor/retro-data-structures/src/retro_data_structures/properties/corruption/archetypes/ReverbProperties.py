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
    class ReverbPropertiesJson(typing_extensions.TypedDict):
        time: float
        predelay: float
        damping: float
        coloration: float
        cross_talk: float
        mix: float
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x44335aff, 0x5724ccd8, 0xfcf4aab0, 0x5d6b1084, 0xfb11a412, 0xde9dd8b8)


@dataclasses.dataclass()
class ReverbProperties(BaseProperty):
    time: float = dataclasses.field(default=0.009999999776482582, metadata={
        'reflection': FieldReflection[float](
            float, id=0x44335aff, original_name='Time'
        ),
    })
    predelay: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5724ccd8, original_name='Predelay'
        ),
    })
    damping: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfcf4aab0, original_name='Damping'
        ),
    })
    coloration: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5d6b1084, original_name='Coloration'
        ),
    })
    cross_talk: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfb11a412, original_name='CrossTalk'
        ),
    })
    mix: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0xde9dd8b8, original_name='Mix'
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
        if property_count != 6:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHfLHfLHfLHfLHfLHf')
    
        dec = _FAST_FORMAT.unpack(data.read(60))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x06')  # 6 properties

        data.write(b'D3Z\xff')  # 0x44335aff
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.time))

        data.write(b'W$\xcc\xd8')  # 0x5724ccd8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.predelay))

        data.write(b'\xfc\xf4\xaa\xb0')  # 0xfcf4aab0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.damping))

        data.write(b']k\x10\x84')  # 0x5d6b1084
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.coloration))

        data.write(b'\xfb\x11\xa4\x12')  # 0xfb11a412
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.cross_talk))

        data.write(b'\xde\x9d\xd8\xb8')  # 0xde9dd8b8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.mix))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ReverbPropertiesJson", data)
        return cls(
            time=json_data['time'],
            predelay=json_data['predelay'],
            damping=json_data['damping'],
            coloration=json_data['coloration'],
            cross_talk=json_data['cross_talk'],
            mix=json_data['mix'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'time': self.time,
            'predelay': self.predelay,
            'damping': self.damping,
            'coloration': self.coloration,
            'cross_talk': self.cross_talk,
            'mix': self.mix,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x44335aff: ('time', structs.decode_BIG_f),
    0x5724ccd8: ('predelay', structs.decode_BIG_f),
    0xfcf4aab0: ('damping', structs.decode_BIG_f),
    0x5d6b1084: ('coloration', structs.decode_BIG_f),
    0xfb11a412: ('cross_talk', structs.decode_BIG_f),
    0xde9dd8b8: ('mix', structs.decode_BIG_f),
}
