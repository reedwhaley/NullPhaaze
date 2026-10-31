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
    class TIcon_ConfigurationsJson(typing_extensions.TypedDict):
        something0_angle: float
        something1_angle: float
        something2_angle: float
        something3_angle: float
        something4_angle: float
        something5_angle: float
        something6_angle: float
        something7_angle: float
        something8_angle: float
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x3058aff2, 0xf1d67032, 0x68341633, 0xa9bac9f3, 0x8081dc70, 0x410f03b0, 0xd8ed65b1, 0x1963ba71, 0x8a9b4eb7)


@dataclasses.dataclass()
class TIcon_Configurations(BaseProperty):
    something0_angle: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3058aff2, original_name='Something0Angle'
        ),
    })
    something1_angle: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf1d67032, original_name='Something1Angle'
        ),
    })
    something2_angle: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x68341633, original_name='Something2Angle'
        ),
    })
    something3_angle: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa9bac9f3, original_name='Something3Angle'
        ),
    })
    something4_angle: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8081dc70, original_name='Something4Angle'
        ),
    })
    something5_angle: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x410f03b0, original_name='Something5Angle'
        ),
    })
    something6_angle: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd8ed65b1, original_name='Something6Angle'
        ),
    })
    something7_angle: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1963ba71, original_name='Something7Angle'
        ),
    })
    something8_angle: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8a9b4eb7, original_name='Something8Angle'
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
            _FAST_FORMAT = struct.Struct('>LHfLHfLHfLHfLHfLHfLHfLHfLHf')
    
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

        data.write(b'0X\xaf\xf2')  # 0x3058aff2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.something0_angle))

        data.write(b'\xf1\xd6p2')  # 0xf1d67032
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.something1_angle))

        data.write(b'h4\x163')  # 0x68341633
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.something2_angle))

        data.write(b'\xa9\xba\xc9\xf3')  # 0xa9bac9f3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.something3_angle))

        data.write(b'\x80\x81\xdcp')  # 0x8081dc70
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.something4_angle))

        data.write(b'A\x0f\x03\xb0')  # 0x410f03b0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.something5_angle))

        data.write(b'\xd8\xede\xb1')  # 0xd8ed65b1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.something6_angle))

        data.write(b'\x19c\xbaq')  # 0x1963ba71
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.something7_angle))

        data.write(b'\x8a\x9bN\xb7')  # 0x8a9b4eb7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.something8_angle))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TIcon_ConfigurationsJson", data)
        return cls(
            something0_angle=json_data['something0_angle'],
            something1_angle=json_data['something1_angle'],
            something2_angle=json_data['something2_angle'],
            something3_angle=json_data['something3_angle'],
            something4_angle=json_data['something4_angle'],
            something5_angle=json_data['something5_angle'],
            something6_angle=json_data['something6_angle'],
            something7_angle=json_data['something7_angle'],
            something8_angle=json_data['something8_angle'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'something0_angle': self.something0_angle,
            'something1_angle': self.something1_angle,
            'something2_angle': self.something2_angle,
            'something3_angle': self.something3_angle,
            'something4_angle': self.something4_angle,
            'something5_angle': self.something5_angle,
            'something6_angle': self.something6_angle,
            'something7_angle': self.something7_angle,
            'something8_angle': self.something8_angle,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x3058aff2: ('something0_angle', structs.decode_BIG_f),
    0xf1d67032: ('something1_angle', structs.decode_BIG_f),
    0x68341633: ('something2_angle', structs.decode_BIG_f),
    0xa9bac9f3: ('something3_angle', structs.decode_BIG_f),
    0x8081dc70: ('something4_angle', structs.decode_BIG_f),
    0x410f03b0: ('something5_angle', structs.decode_BIG_f),
    0xd8ed65b1: ('something6_angle', structs.decode_BIG_f),
    0x1963ba71: ('something7_angle', structs.decode_BIG_f),
    0x8a9b4eb7: ('something8_angle', structs.decode_BIG_f),
}
