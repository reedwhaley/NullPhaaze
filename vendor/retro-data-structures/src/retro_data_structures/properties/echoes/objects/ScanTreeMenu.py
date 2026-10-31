# Generated File
from __future__ import annotations

import dataclasses
import struct
import typing
import typing_extensions

from retro_data_structures import json_util
from retro_data_structures.game_check import Game
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class ScanTreeMenuJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        node_name: int
        string_name: str
        game_option: int
        menu_string_table: int
        string_table_option1: str
        menu_value1: int
        string_table_option2: str
        menu_value2: int
        string_table_option3: str
        menu_value3: int
        string_table_option4: str
        menu_value4: int
    

@dataclasses.dataclass()
class ScanTreeMenu(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    node_name: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['STRG'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x46219bac, original_name='NodeName'
        ),
    })
    string_name: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x32698bd6, original_name='StringName'
        ),
    })
    game_option: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x0261a4e0, original_name='GameOption'
        ),
    })  # Choice
    menu_string_table: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['STRG'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa6a874e9, original_name='MenuStringTable'
        ),
    })
    string_table_option1: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x30531924, original_name='StringTableOption1'
        ),
    })
    menu_value1: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x50bce632, original_name='MenuValue1'
        ),
    })
    string_table_option2: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x01bb03b9, original_name='StringTableOption2'
        ),
    })
    menu_value2: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x420949dc, original_name='MenuValue2'
        ),
    })
    string_table_option3: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xa7cc080d, original_name='StringTableOption3'
        ),
    })
    menu_value3: int = dataclasses.field(default=2, metadata={
        'reflection': FieldReflection[int](
            int, id=0xfab52eb9, original_name='MenuValue3'
        ),
    })
    string_table_option4: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x626b3683, original_name='StringTableOption4'
        ),
    })
    menu_value4: int = dataclasses.field(default=3, metadata={
        'reflection': FieldReflection[int](
            int, id=0x67621600, original_name='MenuValue4'
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'SCMN'

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
        if property_count != 13:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x46219bac
        node_name = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32698bd6
        string_name = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0261a4e0
        game_option = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa6a874e9
        menu_string_table = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x30531924
        string_table_option1 = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50bce632
        menu_value1 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x01bb03b9
        string_table_option2 = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x420949dc
        menu_value2 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa7cc080d
        string_table_option3 = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfab52eb9
        menu_value3 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x626b3683
        string_table_option4 = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x67621600
        menu_value4 = structs.BIG_l.unpack(data.read(4))[0]
    
        return cls(editor_properties, node_name, string_name, game_option, menu_string_table, string_table_option1, menu_value1, string_table_option2, menu_value2, string_table_option3, menu_value3, string_table_option4, menu_value4)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\r')  # 13 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'F!\x9b\xac')  # 0x46219bac
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.node_name))

        data.write(b'2i\x8b\xd6')  # 0x32698bd6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.string_name.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x02a\xa4\xe0')  # 0x261a4e0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.game_option))

        data.write(b'\xa6\xa8t\xe9')  # 0xa6a874e9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.menu_string_table))

        data.write(b'0S\x19$')  # 0x30531924
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.string_table_option1.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'P\xbc\xe62')  # 0x50bce632
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.menu_value1))

        data.write(b'\x01\xbb\x03\xb9')  # 0x1bb03b9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.string_table_option2.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'B\tI\xdc')  # 0x420949dc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.menu_value2))

        data.write(b'\xa7\xcc\x08\r')  # 0xa7cc080d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.string_table_option3.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfa\xb5.\xb9')  # 0xfab52eb9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.menu_value3))

        data.write(b'bk6\x83')  # 0x626b3683
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.string_table_option4.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'gb\x16\x00')  # 0x67621600
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.menu_value4))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ScanTreeMenuJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            node_name=json_data['node_name'],
            string_name=json_data['string_name'],
            game_option=json_data['game_option'],
            menu_string_table=json_data['menu_string_table'],
            string_table_option1=json_data['string_table_option1'],
            menu_value1=json_data['menu_value1'],
            string_table_option2=json_data['string_table_option2'],
            menu_value2=json_data['menu_value2'],
            string_table_option3=json_data['string_table_option3'],
            menu_value3=json_data['menu_value3'],
            string_table_option4=json_data['string_table_option4'],
            menu_value4=json_data['menu_value4'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'node_name': self.node_name,
            'string_name': self.string_name,
            'game_option': self.game_option,
            'menu_string_table': self.menu_string_table,
            'string_table_option1': self.string_table_option1,
            'menu_value1': self.menu_value1,
            'string_table_option2': self.string_table_option2,
            'menu_value2': self.menu_value2,
            'string_table_option3': self.string_table_option3,
            'menu_value3': self.menu_value3,
            'string_table_option4': self.string_table_option4,
            'menu_value4': self.menu_value4,
        }

    def _dependencies_for_node_name(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.node_name)

    def _dependencies_for_menu_string_table(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.menu_string_table)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_node_name, "node_name", "AssetId"),
            (self._dependencies_for_menu_string_table, "menu_string_table", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for ScanTreeMenu.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_string_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_string_table_option1(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_string_table_option2(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_string_table_option3(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_string_table_option4(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0x46219bac: ('node_name', structs.decode_BIG_L),
    0x32698bd6: ('string_name', _decode_string_name),
    0x0261a4e0: ('game_option', structs.decode_BIG_L),
    0xa6a874e9: ('menu_string_table', structs.decode_BIG_L),
    0x30531924: ('string_table_option1', _decode_string_table_option1),
    0x50bce632: ('menu_value1', structs.decode_BIG_l),
    0x01bb03b9: ('string_table_option2', _decode_string_table_option2),
    0x420949dc: ('menu_value2', structs.decode_BIG_l),
    0xa7cc080d: ('string_table_option3', _decode_string_table_option3),
    0xfab52eb9: ('menu_value3', structs.decode_BIG_l),
    0x626b3683: ('string_table_option4', _decode_string_table_option4),
    0x67621600: ('menu_value4', structs.decode_BIG_l),
}
