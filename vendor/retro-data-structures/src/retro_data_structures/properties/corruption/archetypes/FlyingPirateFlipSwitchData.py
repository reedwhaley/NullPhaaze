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
    class FlyingPirateFlipSwitchDataJson(typing_extensions.TypedDict):
        common_vertical_scale: float
        min_flip_switch_time: float
        max_flip_switch_time: float
        min_re_flip_switch_time: float
        max_re_flip_switch_time: float
        unknown_0x9c27ea0d: float
        unknown_0xe8c00bb1: float
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x50af31e, 0x8ed32be8, 0xcfc4146e, 0x479c95b, 0xdfc69abc, 0x9c27ea0d, 0xe8c00bb1)


@dataclasses.dataclass()
class FlyingPirateFlipSwitchData(BaseProperty):
    common_vertical_scale: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x050af31e, original_name='CommonVerticalScale'
        ),
    })
    min_flip_switch_time: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8ed32be8, original_name='MinFlipSwitchTime'
        ),
    })
    max_flip_switch_time: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcfc4146e, original_name='MaxFlipSwitchTime'
        ),
    })
    min_re_flip_switch_time: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0479c95b, original_name='MinReFlipSwitchTime'
        ),
    })
    max_re_flip_switch_time: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdfc69abc, original_name='MaxReFlipSwitchTime'
        ),
    })
    unknown_0x9c27ea0d: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9c27ea0d, original_name='Unknown'
        ),
    })
    unknown_0xe8c00bb1: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe8c00bb1, original_name='Unknown'
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
            _FAST_FORMAT = struct.Struct('>LHfLHfLHfLHfLHfLHfLHf')
    
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

        data.write(b'\x05\n\xf3\x1e')  # 0x50af31e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.common_vertical_scale))

        data.write(b'\x8e\xd3+\xe8')  # 0x8ed32be8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_flip_switch_time))

        data.write(b'\xcf\xc4\x14n')  # 0xcfc4146e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_flip_switch_time))

        data.write(b'\x04y\xc9[')  # 0x479c95b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_re_flip_switch_time))

        data.write(b'\xdf\xc6\x9a\xbc')  # 0xdfc69abc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_re_flip_switch_time))

        data.write(b"\x9c'\xea\r")  # 0x9c27ea0d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9c27ea0d))

        data.write(b'\xe8\xc0\x0b\xb1')  # 0xe8c00bb1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe8c00bb1))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FlyingPirateFlipSwitchDataJson", data)
        return cls(
            common_vertical_scale=json_data['common_vertical_scale'],
            min_flip_switch_time=json_data['min_flip_switch_time'],
            max_flip_switch_time=json_data['max_flip_switch_time'],
            min_re_flip_switch_time=json_data['min_re_flip_switch_time'],
            max_re_flip_switch_time=json_data['max_re_flip_switch_time'],
            unknown_0x9c27ea0d=json_data['unknown_0x9c27ea0d'],
            unknown_0xe8c00bb1=json_data['unknown_0xe8c00bb1'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'common_vertical_scale': self.common_vertical_scale,
            'min_flip_switch_time': self.min_flip_switch_time,
            'max_flip_switch_time': self.max_flip_switch_time,
            'min_re_flip_switch_time': self.min_re_flip_switch_time,
            'max_re_flip_switch_time': self.max_re_flip_switch_time,
            'unknown_0x9c27ea0d': self.unknown_0x9c27ea0d,
            'unknown_0xe8c00bb1': self.unknown_0xe8c00bb1,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x050af31e: ('common_vertical_scale', structs.decode_BIG_f),
    0x8ed32be8: ('min_flip_switch_time', structs.decode_BIG_f),
    0xcfc4146e: ('max_flip_switch_time', structs.decode_BIG_f),
    0x0479c95b: ('min_re_flip_switch_time', structs.decode_BIG_f),
    0xdfc69abc: ('max_re_flip_switch_time', structs.decode_BIG_f),
    0x9c27ea0d: ('unknown_0x9c27ea0d', structs.decode_BIG_f),
    0xe8c00bb1: ('unknown_0xe8c00bb1', structs.decode_BIG_f),
}
