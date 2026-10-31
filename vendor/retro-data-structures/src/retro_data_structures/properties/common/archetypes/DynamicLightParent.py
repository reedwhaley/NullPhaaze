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
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    class DynamicLightParentJson(typing_extensions.TypedDict):
        translation_from_parent: json_util.JsonValue
        rotation_from_parent: json_util.JsonValue
        locator_name: str
        use_parent_rotation: bool
    

@dataclasses.dataclass()
class DynamicLightParent(BaseProperty):
    translation_from_parent: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0xddd74295, original_name='TranslationFromParent', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    rotation_from_parent: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x88f018b3, original_name='RotationFromParent', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    locator_name: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xfbc6c110, original_name='LocatorName'
        ),
    })
    use_parent_rotation: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xf72eefbd, original_name='UseParentRotation'
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
        assert property_id == 0xddd74295
        translation_from_parent = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x88f018b3
        rotation_from_parent = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfbc6c110
        locator_name = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf72eefbd
        use_parent_rotation = structs.BIG_bool_.unpack(data.read(1))[0]
    
        return cls(translation_from_parent, rotation_from_parent, locator_name, use_parent_rotation)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x04')  # 4 properties

        data.write(b'\xdd\xd7B\x95')  # 0xddd74295
        data.write(b'\x00\x0c')  # size
        self.translation_from_parent.to_stream(data, game)

        data.write(b'\x88\xf0\x18\xb3')  # 0x88f018b3
        data.write(b'\x00\x0c')  # size
        self.rotation_from_parent.to_stream(data, game)

        data.write(b'\xfb\xc6\xc1\x10')  # 0xfbc6c110
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.locator_name.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf7.\xef\xbd')  # 0xf72eefbd
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.use_parent_rotation))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DynamicLightParentJson", data)
        return cls(
            translation_from_parent=Vector.from_json(json_data['translation_from_parent']),
            rotation_from_parent=Vector.from_json(json_data['rotation_from_parent']),
            locator_name=json_data['locator_name'],
            use_parent_rotation=json_data['use_parent_rotation'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'translation_from_parent': self.translation_from_parent.to_json(),
            'rotation_from_parent': self.rotation_from_parent.to_json(),
            'locator_name': self.locator_name,
            'use_parent_rotation': self.use_parent_rotation,
        }


def _decode_translation_from_parent(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_rotation_from_parent(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_locator_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xddd74295: ('translation_from_parent', _decode_translation_from_parent),
    0x88f018b3: ('rotation_from_parent', _decode_rotation_from_parent),
    0xfbc6c110: ('locator_name', _decode_locator_name),
    0xf72eefbd: ('use_parent_rotation', structs.decode_BIG_bool_),
}
