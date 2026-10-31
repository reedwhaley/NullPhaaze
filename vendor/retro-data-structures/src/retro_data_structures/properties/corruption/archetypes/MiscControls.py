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
from retro_data_structures.properties.corruption.archetypes.InventoryControls import InventoryControls
from retro_data_structures.properties.corruption.archetypes.LogBookControls import LogBookControls
from retro_data_structures.properties.corruption.archetypes.MapControls import MapControls
from retro_data_structures.properties.corruption.archetypes.QuickSelectControls import QuickSelectControls
from retro_data_structures.properties.corruption.archetypes.RevolutionControl import RevolutionControl

if typing.TYPE_CHECKING:
    class MiscControlsJson(typing_extensions.TypedDict):
        map: json_util.JsonObject
        inventory: json_util.JsonObject
        options_screen: json_util.JsonObject
        log_book: json_util.JsonObject
        quick_select: json_util.JsonObject
        screenshot_tool: json_util.JsonObject
    

@dataclasses.dataclass()
class MiscControls(BaseProperty):
    map: MapControls = dataclasses.field(default_factory=MapControls, metadata={
        'reflection': FieldReflection[MapControls](
            MapControls, id=0x9acb4ace, original_name='Map', from_json=MapControls.from_json, to_json=MapControls.to_json
        ),
    })
    inventory: InventoryControls = dataclasses.field(default_factory=InventoryControls, metadata={
        'reflection': FieldReflection[InventoryControls](
            InventoryControls, id=0xed3482b7, original_name='Inventory', from_json=InventoryControls.from_json, to_json=InventoryControls.to_json
        ),
    })
    options_screen: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x36e52f14, original_name='OptionsScreen', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    log_book: LogBookControls = dataclasses.field(default_factory=LogBookControls, metadata={
        'reflection': FieldReflection[LogBookControls](
            LogBookControls, id=0xc6232204, original_name='LogBook', from_json=LogBookControls.from_json, to_json=LogBookControls.to_json
        ),
    })
    quick_select: QuickSelectControls = dataclasses.field(default_factory=QuickSelectControls, metadata={
        'reflection': FieldReflection[QuickSelectControls](
            QuickSelectControls, id=0x5126ffe7, original_name='QuickSelect', from_json=QuickSelectControls.from_json, to_json=QuickSelectControls.to_json
        ),
    })
    screenshot_tool: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x439f3678, original_name='ScreenshotTool', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
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
        if property_count != 6:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9acb4ace
        map = MapControls.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed3482b7
        inventory = InventoryControls.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x36e52f14
        options_screen = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc6232204
        log_book = LogBookControls.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5126ffe7
        quick_select = QuickSelectControls.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x439f3678
        screenshot_tool = RevolutionControl.from_stream(data, game, property_size)
    
        return cls(map, inventory, options_screen, log_book, quick_select, screenshot_tool)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x06')  # 6 properties

        data.write(b'\x9a\xcbJ\xce')  # 0x9acb4ace
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xed4\x82\xb7')  # 0xed3482b7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.inventory.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'6\xe5/\x14')  # 0x36e52f14
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.options_screen.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc6#"\x04')  # 0xc6232204
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.log_book.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'Q&\xff\xe7')  # 0x5126ffe7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.quick_select.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'C\x9f6x')  # 0x439f3678
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.screenshot_tool.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MiscControlsJson", data)
        return cls(
            map=MapControls.from_json(json_data['map']),
            inventory=InventoryControls.from_json(json_data['inventory']),
            options_screen=RevolutionControl.from_json(json_data['options_screen']),
            log_book=LogBookControls.from_json(json_data['log_book']),
            quick_select=QuickSelectControls.from_json(json_data['quick_select']),
            screenshot_tool=RevolutionControl.from_json(json_data['screenshot_tool']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'map': self.map.to_json(),
            'inventory': self.inventory.to_json(),
            'options_screen': self.options_screen.to_json(),
            'log_book': self.log_book.to_json(),
            'quick_select': self.quick_select.to_json(),
            'screenshot_tool': self.screenshot_tool.to_json(),
        }


def _decode_map(data: typing.BinaryIO, game: Game, property_size: int) -> MapControls:
    return MapControls.from_stream(data, game, property_size)


def _decode_inventory(data: typing.BinaryIO, game: Game, property_size: int) -> InventoryControls:
    return InventoryControls.from_stream(data, game, property_size)


def _decode_options_screen(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_log_book(data: typing.BinaryIO, game: Game, property_size: int) -> LogBookControls:
    return LogBookControls.from_stream(data, game, property_size)


def _decode_quick_select(data: typing.BinaryIO, game: Game, property_size: int) -> QuickSelectControls:
    return QuickSelectControls.from_stream(data, game, property_size)


def _decode_screenshot_tool(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x9acb4ace: ('map', _decode_map),
    0xed3482b7: ('inventory', _decode_inventory),
    0x36e52f14: ('options_screen', _decode_options_screen),
    0xc6232204: ('log_book', _decode_log_book),
    0x5126ffe7: ('quick_select', _decode_quick_select),
    0x439f3678: ('screenshot_tool', _decode_screenshot_tool),
}
