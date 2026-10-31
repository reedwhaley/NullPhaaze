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
    class TweakPlayerGun_PositionJson(typing_extensions.TypedDict):
        gun_extend_distance: float
        x: float
        y: float
        z: float
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x1547d77b, 0xa1677d4e, 0x6a3baeeb, 0xecafdc45)


@dataclasses.dataclass()
class TweakPlayerGun_Position(BaseProperty):
    gun_extend_distance: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1547d77b, original_name='Gun_Extend_Distance'
        ),
    })
    x: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa1677d4e, original_name='X'
        ),
    })
    y: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6a3baeeb, original_name='Y'
        ),
    })
    z: float = dataclasses.field(default=-0.3499999940395355, metadata={
        'reflection': FieldReflection[float](
            float, id=0xecafdc45, original_name='Z'
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
        if property_count != 4:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHfLHfLHfLHf')
    
        dec = _FAST_FORMAT.unpack(data.read(40))
        assert (dec[0], dec[3], dec[6], dec[9]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x04')  # 4 properties

        data.write(b'\x15G\xd7{')  # 0x1547d77b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.gun_extend_distance))

        data.write(b'\xa1g}N')  # 0xa1677d4e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.x))

        data.write(b'j;\xae\xeb')  # 0x6a3baeeb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.y))

        data.write(b'\xec\xaf\xdcE')  # 0xecafdc45
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.z))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayerGun_PositionJson", data)
        return cls(
            gun_extend_distance=json_data['gun_extend_distance'],
            x=json_data['x'],
            y=json_data['y'],
            z=json_data['z'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'gun_extend_distance': self.gun_extend_distance,
            'x': self.x,
            'y': self.y,
            'z': self.z,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x1547d77b: ('gun_extend_distance', structs.decode_BIG_f),
    0xa1677d4e: ('x', structs.decode_BIG_f),
    0x6a3baeeb: ('y', structs.decode_BIG_f),
    0xecafdc45: ('z', structs.decode_BIG_f),
}
