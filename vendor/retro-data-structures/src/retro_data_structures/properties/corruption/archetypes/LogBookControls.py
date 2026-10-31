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
    class LogBookControlsJson(typing_extensions.TypedDict):
        log_screen: json_util.JsonObject
        log_screen_exit: json_util.JsonObject
        log_book_scroll_up: json_util.JsonObject
        log_book_scroll_down: json_util.JsonObject
    

@dataclasses.dataclass()
class LogBookControls(BaseProperty):
    log_screen: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x10699c6f, original_name='LogScreen', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    log_screen_exit: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x50de5441, original_name='LogScreenExit', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    log_book_scroll_up: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xa9a26569, original_name='LogBookScrollUp', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    log_book_scroll_down: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x6f71adf7, original_name='LogBookScrollDown', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
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
        assert property_id == 0x10699c6f
        log_screen = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50de5441
        log_screen_exit = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa9a26569
        log_book_scroll_up = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6f71adf7
        log_book_scroll_down = RevolutionControl.from_stream(data, game, property_size)
    
        return cls(log_screen, log_screen_exit, log_book_scroll_up, log_book_scroll_down)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x04')  # 4 properties

        data.write(b'\x10i\x9co')  # 0x10699c6f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.log_screen.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'P\xdeTA')  # 0x50de5441
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.log_screen_exit.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa9\xa2ei')  # 0xa9a26569
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.log_book_scroll_up.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'oq\xad\xf7')  # 0x6f71adf7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.log_book_scroll_down.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("LogBookControlsJson", data)
        return cls(
            log_screen=RevolutionControl.from_json(json_data['log_screen']),
            log_screen_exit=RevolutionControl.from_json(json_data['log_screen_exit']),
            log_book_scroll_up=RevolutionControl.from_json(json_data['log_book_scroll_up']),
            log_book_scroll_down=RevolutionControl.from_json(json_data['log_book_scroll_down']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'log_screen': self.log_screen.to_json(),
            'log_screen_exit': self.log_screen_exit.to_json(),
            'log_book_scroll_up': self.log_book_scroll_up.to_json(),
            'log_book_scroll_down': self.log_book_scroll_down.to_json(),
        }


def _decode_log_screen(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_log_screen_exit(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_log_book_scroll_up(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_log_book_scroll_down(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x10699c6f: ('log_screen', _decode_log_screen),
    0x50de5441: ('log_screen_exit', _decode_log_screen_exit),
    0xa9a26569: ('log_book_scroll_up', _decode_log_book_scroll_up),
    0x6f71adf7: ('log_book_scroll_down', _decode_log_book_scroll_down),
}
