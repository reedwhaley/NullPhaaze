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
from retro_data_structures.properties.common.archetypes.Transform import Transform

if typing.TYPE_CHECKING:
    class EditorPropertiesJson(typing_extensions.TypedDict):
        name: str
        transform: json_util.JsonObject
        active: bool
        misc_flags: int
    

class MiscEditorFlags(enum.IntFlag):
    Activewhileoffscreen = 1
    Activeduringcutsceneskip = 2

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
class EditorProperties(BaseProperty):
    name: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x494e414d, original_name='Name'
        ),
    })
    transform: Transform = dataclasses.field(default_factory=Transform, metadata={
        'reflection': FieldReflection[Transform](
            Transform, id=0x5846524d, original_name='Transform', from_json=Transform.from_json, to_json=Transform.to_json
        ),
    })
    active: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x41435456, original_name='Active'
        ),
    })
    misc_flags: MiscEditorFlags = dataclasses.field(default=MiscEditorFlags(3), metadata={
        'reflection': FieldReflection[MiscEditorFlags](
            MiscEditorFlags, id=0x5d298a43, original_name='MiscFlags', from_json=MiscEditorFlags.from_json, to_json=MiscEditorFlags.to_json
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
        assert property_id == 0x494e414d
        name = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5846524d
        transform = Transform.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x41435456
        active = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5d298a43
        misc_flags = MiscEditorFlags.from_stream(data, game)
    
        return cls(name, transform, active, misc_flags)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x04')  # 4 properties

        data.write(b'INAM')  # 0x494e414d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.name.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'XFRM')  # 0x5846524d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.transform.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'ACTV')  # 0x41435456
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.active))

        data.write(b'])\x8aC')  # 0x5d298a43
        data.write(b'\x00\x04')  # size
        self.misc_flags.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("EditorPropertiesJson", data)
        return cls(
            name=json_data['name'],
            transform=Transform.from_json(json_data['transform']),
            active=json_data['active'],
            misc_flags=MiscEditorFlags.from_json(json_data['misc_flags']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'name': self.name,
            'transform': self.transform.to_json(),
            'active': self.active,
            'misc_flags': self.misc_flags.to_json(),
        }


def _decode_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_transform(data: typing.BinaryIO, game: Game, property_size: int) -> Transform:
    return Transform.from_stream(data, game, property_size)


def _decode_misc_flags(data: typing.BinaryIO, game: Game, property_size: int) -> MiscEditorFlags:
    return MiscEditorFlags.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x494e414d: ('name', _decode_name),
    0x5846524d: ('transform', _decode_transform),
    0x41435456: ('active', structs.decode_BIG_bool_),
    0x5d298a43: ('misc_flags', _decode_misc_flags),
}
