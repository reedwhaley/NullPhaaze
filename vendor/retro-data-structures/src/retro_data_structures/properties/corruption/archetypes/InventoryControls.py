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
from retro_data_structures.properties.corruption.archetypes.RevolutionControl import RevolutionControl

if typing.TYPE_CHECKING:
    class InventoryControlsJson(typing_extensions.TypedDict):
        inventory_screen: json_util.JsonObject
        menu_up: json_util.JsonObject
        menu_down: json_util.JsonObject
        menu_left: json_util.JsonObject
        menu_right: json_util.JsonObject
        menu_select: json_util.JsonObject
        menu_exit: json_util.JsonObject
    

@dataclasses.dataclass()
class InventoryControls(BaseProperty):
    inventory_screen: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x340f912e, original_name='InventoryScreen', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    menu_up: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x769909c1, original_name='MenuUp', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    menu_down: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x4dab695e, original_name='MenuDown', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    menu_left: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xc7cae2d3, original_name='MenuLeft', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    menu_right: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x1595f276, original_name='MenuRight', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    menu_select: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xbf09b38b, original_name='MenuSelect', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    menu_exit: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x68ea537d, original_name='MenuExit', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
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
        if property_count != 7:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x340f912e
        inventory_screen = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x769909c1
        menu_up = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4dab695e
        menu_down = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc7cae2d3
        menu_left = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1595f276
        menu_right = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbf09b38b
        menu_select = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68ea537d
        menu_exit = RevolutionControl.from_stream(data, game, property_size)
    
        return cls(inventory_screen, menu_up, menu_down, menu_left, menu_right, menu_select, menu_exit)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x07')  # 7 properties

        data.write(b'4\x0f\x91.')  # 0x340f912e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.inventory_screen.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'v\x99\t\xc1')  # 0x769909c1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.menu_up.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'M\xabi^')  # 0x4dab695e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.menu_down.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc7\xca\xe2\xd3')  # 0xc7cae2d3
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.menu_left.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x15\x95\xf2v')  # 0x1595f276
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.menu_right.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbf\t\xb3\x8b')  # 0xbf09b38b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.menu_select.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'h\xeaS}')  # 0x68ea537d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.menu_exit.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("InventoryControlsJson", data)
        return cls(
            inventory_screen=RevolutionControl.from_json(json_data['inventory_screen']),
            menu_up=RevolutionControl.from_json(json_data['menu_up']),
            menu_down=RevolutionControl.from_json(json_data['menu_down']),
            menu_left=RevolutionControl.from_json(json_data['menu_left']),
            menu_right=RevolutionControl.from_json(json_data['menu_right']),
            menu_select=RevolutionControl.from_json(json_data['menu_select']),
            menu_exit=RevolutionControl.from_json(json_data['menu_exit']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'inventory_screen': self.inventory_screen.to_json(),
            'menu_up': self.menu_up.to_json(),
            'menu_down': self.menu_down.to_json(),
            'menu_left': self.menu_left.to_json(),
            'menu_right': self.menu_right.to_json(),
            'menu_select': self.menu_select.to_json(),
            'menu_exit': self.menu_exit.to_json(),
        }


def _decode_inventory_screen(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_menu_up(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_menu_down(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_menu_left(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_menu_right(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_menu_select(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_menu_exit(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x340f912e: ('inventory_screen', _decode_inventory_screen),
    0x769909c1: ('menu_up', _decode_menu_up),
    0x4dab695e: ('menu_down', _decode_menu_down),
    0xc7cae2d3: ('menu_left', _decode_menu_left),
    0x1595f276: ('menu_right', _decode_menu_right),
    0xbf09b38b: ('menu_select', _decode_menu_select),
    0x68ea537d: ('menu_exit', _decode_menu_exit),
}
