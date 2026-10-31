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
import retro_data_structures.enums.echoes as enums
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.ScannableParameters import ScannableParameters
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class ScanTreeInventoryJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        node_name: int
        string_name: str
        inventory_item: int
        scannable_info: json_util.JsonObject
    

@dataclasses.dataclass()
class ScanTreeInventory(BaseObjectType):
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
    inventory_item: enums.InventorySlotEnum = dataclasses.field(default=enums.InventorySlotEnum.DarkVisor, metadata={
        'reflection': FieldReflection[enums.InventorySlotEnum](
            enums.InventorySlotEnum, id=0x3d326f90, original_name='InventoryItem', from_json=enums.InventorySlotEnum.from_json, to_json=enums.InventorySlotEnum.to_json
        ),
    })
    scannable_info: ScannableParameters = dataclasses.field(default_factory=ScannableParameters, metadata={
        'reflection': FieldReflection[ScannableParameters](
            ScannableParameters, id=0x2da1ec33, original_name='ScannableInfo', from_json=ScannableParameters.from_json, to_json=ScannableParameters.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'SCIN'

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
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x46219bac
        node_name = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32698bd6
        string_name = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3d326f90
        inventory_item = enums.InventorySlotEnum.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2da1ec33
        scannable_info = ScannableParameters.from_stream(data, game, property_size)
    
        return cls(editor_properties, node_name, string_name, inventory_item, scannable_info)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x05')  # 5 properties

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

        data.write(b'=2o\x90')  # 0x3d326f90
        data.write(b'\x00\x04')  # size
        self.inventory_item.to_stream(data, game)

        data.write(b'-\xa1\xec3')  # 0x2da1ec33
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.scannable_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ScanTreeInventoryJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            node_name=json_data['node_name'],
            string_name=json_data['string_name'],
            inventory_item=enums.InventorySlotEnum.from_json(json_data['inventory_item']),
            scannable_info=ScannableParameters.from_json(json_data['scannable_info']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'node_name': self.node_name,
            'string_name': self.string_name,
            'inventory_item': self.inventory_item.to_json(),
            'scannable_info': self.scannable_info.to_json(),
        }

    def _dependencies_for_node_name(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.node_name)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_node_name, "node_name", "AssetId"),
            (self.scannable_info.dependencies_for, "scannable_info", "ScannableParameters"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for ScanTreeInventory.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_string_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_inventory_item(data: typing.BinaryIO, game: Game, property_size: int) -> enums.InventorySlotEnum:
    return enums.InventorySlotEnum.from_stream(data, game)


def _decode_scannable_info(data: typing.BinaryIO, game: Game, property_size: int) -> ScannableParameters:
    return ScannableParameters.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0x46219bac: ('node_name', structs.decode_BIG_L),
    0x32698bd6: ('string_name', _decode_string_name),
    0x3d326f90: ('inventory_item', _decode_inventory_item),
    0x2da1ec33: ('scannable_info', _decode_scannable_info),
}
