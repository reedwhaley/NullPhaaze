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
import retro_data_structures.enums.corruption as enums
from retro_data_structures.properties.corruption.archetypes.DPDArc import DPDArc
from retro_data_structures.properties.corruption.archetypes.DPDCircle import DPDCircle
from retro_data_structures.properties.corruption.archetypes.DPDRectangle import DPDRectangle

if typing.TYPE_CHECKING:
    class RevolutionDPDControlJson(typing_extensions.TypedDict):
        revolution_pointer_shape: int
        circle: json_util.JsonObject
        rectangle: json_util.JsonObject
        pie_slice: json_util.JsonObject
    

@dataclasses.dataclass()
class RevolutionDPDControl(BaseProperty):
    revolution_pointer_shape: enums.RevolutionPointerShapeEnum = dataclasses.field(default=enums.RevolutionPointerShapeEnum.kRPS_Circle, metadata={
        'reflection': FieldReflection[enums.RevolutionPointerShapeEnum](
            enums.RevolutionPointerShapeEnum, id=0xe1c76bfb, original_name='RevolutionPointerShape', from_json=enums.RevolutionPointerShapeEnum.from_json, to_json=enums.RevolutionPointerShapeEnum.to_json
        ),
    })
    circle: DPDCircle = dataclasses.field(default_factory=DPDCircle, metadata={
        'reflection': FieldReflection[DPDCircle](
            DPDCircle, id=0x3d8010c2, original_name='Circle', from_json=DPDCircle.from_json, to_json=DPDCircle.to_json
        ),
    })
    rectangle: DPDRectangle = dataclasses.field(default_factory=DPDRectangle, metadata={
        'reflection': FieldReflection[DPDRectangle](
            DPDRectangle, id=0x9e8e5bf9, original_name='Rectangle', from_json=DPDRectangle.from_json, to_json=DPDRectangle.to_json
        ),
    })
    pie_slice: DPDArc = dataclasses.field(default_factory=DPDArc, metadata={
        'reflection': FieldReflection[DPDArc](
            DPDArc, id=0x6d33ae8f, original_name='PieSlice', from_json=DPDArc.from_json, to_json=DPDArc.to_json
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
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe1c76bfb
        revolution_pointer_shape = enums.RevolutionPointerShapeEnum.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3d8010c2
        circle = DPDCircle.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9e8e5bf9
        rectangle = DPDRectangle.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6d33ae8f
        pie_slice = DPDArc.from_stream(data, game, property_size)
    
        return cls(revolution_pointer_shape, circle, rectangle, pie_slice)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x04')  # 4 properties

        data.write(b'\xe1\xc7k\xfb')  # 0xe1c76bfb
        data.write(b'\x00\x04')  # size
        self.revolution_pointer_shape.to_stream(data, game)

        data.write(b'=\x80\x10\xc2')  # 0x3d8010c2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.circle.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9e\x8e[\xf9')  # 0x9e8e5bf9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.rectangle.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'm3\xae\x8f')  # 0x6d33ae8f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.pie_slice.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("RevolutionDPDControlJson", data)
        return cls(
            revolution_pointer_shape=enums.RevolutionPointerShapeEnum.from_json(json_data['revolution_pointer_shape']),
            circle=DPDCircle.from_json(json_data['circle']),
            rectangle=DPDRectangle.from_json(json_data['rectangle']),
            pie_slice=DPDArc.from_json(json_data['pie_slice']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'revolution_pointer_shape': self.revolution_pointer_shape.to_json(),
            'circle': self.circle.to_json(),
            'rectangle': self.rectangle.to_json(),
            'pie_slice': self.pie_slice.to_json(),
        }


def _decode_revolution_pointer_shape(data: typing.BinaryIO, game: Game, property_size: int) -> enums.RevolutionPointerShapeEnum:
    return enums.RevolutionPointerShapeEnum.from_stream(data, game)


def _decode_circle(data: typing.BinaryIO, game: Game, property_size: int) -> DPDCircle:
    return DPDCircle.from_stream(data, game, property_size)


def _decode_rectangle(data: typing.BinaryIO, game: Game, property_size: int) -> DPDRectangle:
    return DPDRectangle.from_stream(data, game, property_size)


def _decode_pie_slice(data: typing.BinaryIO, game: Game, property_size: int) -> DPDArc:
    return DPDArc.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xe1c76bfb: ('revolution_pointer_shape', _decode_revolution_pointer_shape),
    0x3d8010c2: ('circle', _decode_circle),
    0x9e8e5bf9: ('rectangle', _decode_rectangle),
    0x6d33ae8f: ('pie_slice', _decode_pie_slice),
}
