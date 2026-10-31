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
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    class SpindleCameraInterpolantJson(typing_extensions.TypedDict):
        interpolant_type: int
        interpolant_spline: json_util.JsonObject
    

@dataclasses.dataclass()
class SpindleCameraInterpolant(BaseProperty):
    interpolant_type: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x3e9cf140, original_name='InterpolantType'
        ),
    })  # Choice
    interpolant_spline: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x9a598fa5, original_name='InterpolantSpline', from_json=Spline.from_json, to_json=Spline.to_json
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
        if property_count != 2:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3e9cf140
        interpolant_type = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9a598fa5
        interpolant_spline = Spline.from_stream(data, game, property_size)
    
        return cls(interpolant_type, interpolant_spline)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x02')  # 2 properties

        data.write(b'>\x9c\xf1@')  # 0x3e9cf140
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.interpolant_type))

        data.write(b'\x9aY\x8f\xa5')  # 0x9a598fa5
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.interpolant_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SpindleCameraInterpolantJson", data)
        return cls(
            interpolant_type=json_data['interpolant_type'],
            interpolant_spline=Spline.from_json(json_data['interpolant_spline']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'interpolant_type': self.interpolant_type,
            'interpolant_spline': self.interpolant_spline.to_json(),
        }


def _decode_interpolant_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x3e9cf140: ('interpolant_type', structs.decode_BIG_L),
    0x9a598fa5: ('interpolant_spline', _decode_interpolant_spline),
}
