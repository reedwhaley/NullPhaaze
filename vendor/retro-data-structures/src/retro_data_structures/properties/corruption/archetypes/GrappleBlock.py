# Generated File
from __future__ import annotations

import dataclasses
import enum
import struct
import typing
import typing_extensions

from retro_data_structures import json_util
from retro_data_structures.game_check import Game
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection

if typing.TYPE_CHECKING:
    class GrappleBlockJson(typing_extensions.TypedDict):
        block_type: int
        unknown_0x54178cb8: float
        unknown_0xde38f04e: float
        unknown_0x9d0c992f: float
        time_to_complete_block: float
        use_time_to_complete_block: bool
        unknown_0xa62bf627: bool
        yank_adjustment_type: int
        can_fail_when_pulling: bool
        unknown_0x0887fefe: bool
    

class YankAdjustmentType(enum.IntEnum):
    kYankAdjustment_2D = 3516796033
    kYankAdjustment_3D = 3364175296

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x8bd240, 0x54178cb8, 0xde38f04e, 0x9d0c992f, 0x8382cd42, 0x8a40fd1b, 0xa62bf627, 0xf8a14c37, 0x64fb595c, 0x887fefe)


@dataclasses.dataclass()
class GrappleBlock(BaseProperty):
    block_type: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x008bd240, original_name='BlockType'
        ),
    })  # Choice
    unknown_0x54178cb8: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x54178cb8, original_name='Unknown'
        ),
    })
    unknown_0xde38f04e: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xde38f04e, original_name='Unknown'
        ),
    })
    unknown_0x9d0c992f: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9d0c992f, original_name='Unknown'
        ),
    })
    time_to_complete_block: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8382cd42, original_name='TimeToCompleteBlock'
        ),
    })
    use_time_to_complete_block: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x8a40fd1b, original_name='UseTimeToCompleteBlock'
        ),
    })
    unknown_0xa62bf627: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xa62bf627, original_name='Unknown'
        ),
    })
    yank_adjustment_type: YankAdjustmentType = dataclasses.field(default=YankAdjustmentType.kYankAdjustment_3D, metadata={
        'reflection': FieldReflection[YankAdjustmentType](
            YankAdjustmentType, id=0xf8a14c37, original_name='YankAdjustmentType', from_json=YankAdjustmentType.from_json, to_json=YankAdjustmentType.to_json
        ),
    })
    can_fail_when_pulling: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x64fb595c, original_name='CanFailWhenPulling'
        ),
    })
    unknown_0x0887fefe: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x0887fefe, original_name='Unknown'
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
        if property_count != 10:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHLLHfLHfLHfLHfLH?LH?LHLLH?LH?')
    
        dec = _FAST_FORMAT.unpack(data.read(88))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24], dec[27]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            YankAdjustmentType(dec[23]),
            dec[26],
            dec[29],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\n')  # 10 properties

        data.write(b'\x00\x8b\xd2@')  # 0x8bd240
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.block_type))

        data.write(b'T\x17\x8c\xb8')  # 0x54178cb8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x54178cb8))

        data.write(b'\xde8\xf0N')  # 0xde38f04e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xde38f04e))

        data.write(b'\x9d\x0c\x99/')  # 0x9d0c992f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9d0c992f))

        data.write(b'\x83\x82\xcdB')  # 0x8382cd42
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.time_to_complete_block))

        data.write(b'\x8a@\xfd\x1b')  # 0x8a40fd1b
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.use_time_to_complete_block))

        data.write(b"\xa6+\xf6'")  # 0xa62bf627
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xa62bf627))

        data.write(b'\xf8\xa1L7')  # 0xf8a14c37
        data.write(b'\x00\x04')  # size
        self.yank_adjustment_type.to_stream(data, game)

        data.write(b'd\xfbY\\')  # 0x64fb595c
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.can_fail_when_pulling))

        data.write(b'\x08\x87\xfe\xfe')  # 0x887fefe
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x0887fefe))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GrappleBlockJson", data)
        return cls(
            block_type=json_data['block_type'],
            unknown_0x54178cb8=json_data['unknown_0x54178cb8'],
            unknown_0xde38f04e=json_data['unknown_0xde38f04e'],
            unknown_0x9d0c992f=json_data['unknown_0x9d0c992f'],
            time_to_complete_block=json_data['time_to_complete_block'],
            use_time_to_complete_block=json_data['use_time_to_complete_block'],
            unknown_0xa62bf627=json_data['unknown_0xa62bf627'],
            yank_adjustment_type=YankAdjustmentType.from_json(json_data['yank_adjustment_type']),
            can_fail_when_pulling=json_data['can_fail_when_pulling'],
            unknown_0x0887fefe=json_data['unknown_0x0887fefe'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'block_type': self.block_type,
            'unknown_0x54178cb8': self.unknown_0x54178cb8,
            'unknown_0xde38f04e': self.unknown_0xde38f04e,
            'unknown_0x9d0c992f': self.unknown_0x9d0c992f,
            'time_to_complete_block': self.time_to_complete_block,
            'use_time_to_complete_block': self.use_time_to_complete_block,
            'unknown_0xa62bf627': self.unknown_0xa62bf627,
            'yank_adjustment_type': self.yank_adjustment_type.to_json(),
            'can_fail_when_pulling': self.can_fail_when_pulling,
            'unknown_0x0887fefe': self.unknown_0x0887fefe,
        }


def _decode_yank_adjustment_type(data: typing.BinaryIO, game: Game, property_size: int) -> YankAdjustmentType:
    return YankAdjustmentType.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x008bd240: ('block_type', structs.decode_BIG_L),
    0x54178cb8: ('unknown_0x54178cb8', structs.decode_BIG_f),
    0xde38f04e: ('unknown_0xde38f04e', structs.decode_BIG_f),
    0x9d0c992f: ('unknown_0x9d0c992f', structs.decode_BIG_f),
    0x8382cd42: ('time_to_complete_block', structs.decode_BIG_f),
    0x8a40fd1b: ('use_time_to_complete_block', structs.decode_BIG_bool_),
    0xa62bf627: ('unknown_0xa62bf627', structs.decode_BIG_bool_),
    0xf8a14c37: ('yank_adjustment_type', _decode_yank_adjustment_type),
    0x64fb595c: ('can_fail_when_pulling', structs.decode_BIG_bool_),
    0x0887fefe: ('unknown_0x0887fefe', structs.decode_BIG_bool_),
}
