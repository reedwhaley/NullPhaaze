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
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class RepulsorJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        shape: int
        radius: float
        value: float
        flags: int
    

class RepulsorFlags(enum.IntFlag):
    RepelPlayer = 1
    UseForwardVector = 2

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


@dataclasses.dataclass()
class Repulsor(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    shape: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xf9bb2db6, original_name='Shape'
        ),
    })  # Choice
    radius: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x78c507eb, original_name='Radius'
        ),
    })
    value: float = dataclasses.field(default=-1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8dcd8978, original_name='Value'
        ),
    })
    flags: RepulsorFlags = dataclasses.field(default=RepulsorFlags(0), metadata={
        'reflection': FieldReflection[RepulsorFlags](
            RepulsorFlags, id=0x8aef6bd2, original_name='Flags', from_json=RepulsorFlags.from_json, to_json=RepulsorFlags.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'REPL'

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None) -> typing_extensions.Self:
        struct_id, size, property_count = structs.BIG_LHH.unpack(data.read(8))
        assert struct_id == 0xFFFFFFFF
        root_size_start = data.tell() - 2

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

        assert data.tell() - root_size_start == size
        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 5:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf9bb2db6
        shape = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78c507eb
        radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8dcd8978
        value = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8aef6bd2
        flags = RepulsorFlags.from_stream(data, game)
    
        return cls(editor_properties, shape, radius, value, flags)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x05')  # 5 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game, default_override={'misc_flags': 3})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf9\xbb-\xb6')  # 0xf9bb2db6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.shape))

        data.write(b'x\xc5\x07\xeb')  # 0x78c507eb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.radius))

        data.write(b'\x8d\xcd\x89x')  # 0x8dcd8978
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.value))

        data.write(b'\x8a\xefk\xd2')  # 0x8aef6bd2
        data.write(b'\x00\x04')  # size
        self.flags.to_stream(data, game)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("RepulsorJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            shape=json_data['shape'],
            radius=json_data['radius'],
            value=json_data['value'],
            flags=RepulsorFlags.from_json(json_data['flags']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'shape': self.shape,
            'radius': self.radius,
            'value': self.value,
            'flags': self.flags.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})


def _decode_flags(data: typing.BinaryIO, game: Game, property_size: int) -> RepulsorFlags:
    return RepulsorFlags.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xf9bb2db6: ('shape', structs.decode_BIG_L),
    0x78c507eb: ('radius', structs.decode_BIG_f),
    0x8dcd8978: ('value', structs.decode_BIG_f),
    0x8aef6bd2: ('flags', _decode_flags),
}
