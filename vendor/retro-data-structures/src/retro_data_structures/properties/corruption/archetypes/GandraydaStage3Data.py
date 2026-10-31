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
    class GandraydaStage3DataJson(typing_extensions.TypedDict):
        initial_morph_time: float
        unknown_0x41ed6a42: float
        unknown_0x420da002: float
        min_gandrayda_morph_time: float
        max_gandrayda_morph_time: float
        min_gandrayda_cloaked_time: float
        max_gandrayda_cloaked_time: float
        cloak_time: float
        decloak_time: float
        min_throw_projectile_time: float
        max_throw_projectile_time: float
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x45161109, 0x41ed6a42, 0x420da002, 0xa2675081, 0x413aee5b, 0x9fe347b5, 0xc8ed17f6, 0x388bc31f, 0x4319c840, 0x587fa387, 0x3e9ac5f3)


@dataclasses.dataclass()
class GandraydaStage3Data(BaseProperty):
    initial_morph_time: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x45161109, original_name='InitialMorphTime'
        ),
    })
    unknown_0x41ed6a42: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x41ed6a42, original_name='Unknown'
        ),
    })
    unknown_0x420da002: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x420da002, original_name='Unknown'
        ),
    })
    min_gandrayda_morph_time: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa2675081, original_name='MinGandraydaMorphTime'
        ),
    })
    max_gandrayda_morph_time: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x413aee5b, original_name='MaxGandraydaMorphTime'
        ),
    })
    min_gandrayda_cloaked_time: float = dataclasses.field(default=9.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9fe347b5, original_name='MinGandraydaCloakedTime'
        ),
    })
    max_gandrayda_cloaked_time: float = dataclasses.field(default=11.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc8ed17f6, original_name='MaxGandraydaCloakedTime'
        ),
    })
    cloak_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x388bc31f, original_name='CloakTime'
        ),
    })
    decloak_time: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4319c840, original_name='DecloakTime'
        ),
    })
    min_throw_projectile_time: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x587fa387, original_name='MinThrowProjectileTime'
        ),
    })
    max_throw_projectile_time: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3e9ac5f3, original_name='MaxThrowProjectileTime'
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
        if property_count != 11:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHf')
    
        dec = _FAST_FORMAT.unpack(data.read(110))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24], dec[27], dec[30]) == _FAST_IDS
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
            dec[29],
            dec[32],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x0b')  # 11 properties

        data.write(b'E\x16\x11\t')  # 0x45161109
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.initial_morph_time))

        data.write(b'A\xedjB')  # 0x41ed6a42
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x41ed6a42))

        data.write(b'B\r\xa0\x02')  # 0x420da002
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x420da002))

        data.write(b'\xa2gP\x81')  # 0xa2675081
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_gandrayda_morph_time))

        data.write(b'A:\xee[')  # 0x413aee5b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_gandrayda_morph_time))

        data.write(b'\x9f\xe3G\xb5')  # 0x9fe347b5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_gandrayda_cloaked_time))

        data.write(b'\xc8\xed\x17\xf6')  # 0xc8ed17f6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_gandrayda_cloaked_time))

        data.write(b'8\x8b\xc3\x1f')  # 0x388bc31f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.cloak_time))

        data.write(b'C\x19\xc8@')  # 0x4319c840
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.decloak_time))

        data.write(b'X\x7f\xa3\x87')  # 0x587fa387
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_throw_projectile_time))

        data.write(b'>\x9a\xc5\xf3')  # 0x3e9ac5f3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_throw_projectile_time))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GandraydaStage3DataJson", data)
        return cls(
            initial_morph_time=json_data['initial_morph_time'],
            unknown_0x41ed6a42=json_data['unknown_0x41ed6a42'],
            unknown_0x420da002=json_data['unknown_0x420da002'],
            min_gandrayda_morph_time=json_data['min_gandrayda_morph_time'],
            max_gandrayda_morph_time=json_data['max_gandrayda_morph_time'],
            min_gandrayda_cloaked_time=json_data['min_gandrayda_cloaked_time'],
            max_gandrayda_cloaked_time=json_data['max_gandrayda_cloaked_time'],
            cloak_time=json_data['cloak_time'],
            decloak_time=json_data['decloak_time'],
            min_throw_projectile_time=json_data['min_throw_projectile_time'],
            max_throw_projectile_time=json_data['max_throw_projectile_time'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'initial_morph_time': self.initial_morph_time,
            'unknown_0x41ed6a42': self.unknown_0x41ed6a42,
            'unknown_0x420da002': self.unknown_0x420da002,
            'min_gandrayda_morph_time': self.min_gandrayda_morph_time,
            'max_gandrayda_morph_time': self.max_gandrayda_morph_time,
            'min_gandrayda_cloaked_time': self.min_gandrayda_cloaked_time,
            'max_gandrayda_cloaked_time': self.max_gandrayda_cloaked_time,
            'cloak_time': self.cloak_time,
            'decloak_time': self.decloak_time,
            'min_throw_projectile_time': self.min_throw_projectile_time,
            'max_throw_projectile_time': self.max_throw_projectile_time,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x45161109: ('initial_morph_time', structs.decode_BIG_f),
    0x41ed6a42: ('unknown_0x41ed6a42', structs.decode_BIG_f),
    0x420da002: ('unknown_0x420da002', structs.decode_BIG_f),
    0xa2675081: ('min_gandrayda_morph_time', structs.decode_BIG_f),
    0x413aee5b: ('max_gandrayda_morph_time', structs.decode_BIG_f),
    0x9fe347b5: ('min_gandrayda_cloaked_time', structs.decode_BIG_f),
    0xc8ed17f6: ('max_gandrayda_cloaked_time', structs.decode_BIG_f),
    0x388bc31f: ('cloak_time', structs.decode_BIG_f),
    0x4319c840: ('decloak_time', structs.decode_BIG_f),
    0x587fa387: ('min_throw_projectile_time', structs.decode_BIG_f),
    0x3e9ac5f3: ('max_throw_projectile_time', structs.decode_BIG_f),
}
