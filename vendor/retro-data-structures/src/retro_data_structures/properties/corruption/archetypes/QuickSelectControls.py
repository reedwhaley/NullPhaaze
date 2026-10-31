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
from retro_data_structures.properties.corruption.archetypes.RevolutionControl import RevolutionControl

if typing.TYPE_CHECKING:
    class QuickSelectControlsJson(typing_extensions.TypedDict):
        quick_select_method: int
        menu: json_util.JsonObject
        choice: json_util.JsonObject
        exit: json_util.JsonObject
    

@dataclasses.dataclass()
class QuickSelectControls(BaseProperty):
    quick_select_method: enums.QuickSelectMethodEnum = dataclasses.field(default=enums.QuickSelectMethodEnum.kQSM_None, metadata={
        'reflection': FieldReflection[enums.QuickSelectMethodEnum](
            enums.QuickSelectMethodEnum, id=0x67739b75, original_name='QuickSelectMethod', from_json=enums.QuickSelectMethodEnum.from_json, to_json=enums.QuickSelectMethodEnum.to_json
        ),
    })
    menu: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xa5e20450, original_name='Menu', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    choice: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xa74987ff, original_name='Choice', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    exit: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x73eb9d04, original_name='Exit', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
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
        assert property_id == 0x67739b75
        quick_select_method = enums.QuickSelectMethodEnum.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa5e20450
        menu = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa74987ff
        choice = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x73eb9d04
        exit = RevolutionControl.from_stream(data, game, property_size)
    
        return cls(quick_select_method, menu, choice, exit)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x04')  # 4 properties

        data.write(b'gs\x9bu')  # 0x67739b75
        data.write(b'\x00\x04')  # size
        self.quick_select_method.to_stream(data, game)

        data.write(b'\xa5\xe2\x04P')  # 0xa5e20450
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.menu.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa7I\x87\xff')  # 0xa74987ff
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.choice.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b's\xeb\x9d\x04')  # 0x73eb9d04
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.exit.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("QuickSelectControlsJson", data)
        return cls(
            quick_select_method=enums.QuickSelectMethodEnum.from_json(json_data['quick_select_method']),
            menu=RevolutionControl.from_json(json_data['menu']),
            choice=RevolutionControl.from_json(json_data['choice']),
            exit=RevolutionControl.from_json(json_data['exit']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'quick_select_method': self.quick_select_method.to_json(),
            'menu': self.menu.to_json(),
            'choice': self.choice.to_json(),
            'exit': self.exit.to_json(),
        }


def _decode_quick_select_method(data: typing.BinaryIO, game: Game, property_size: int) -> enums.QuickSelectMethodEnum:
    return enums.QuickSelectMethodEnum.from_stream(data, game)


def _decode_menu(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_choice(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_exit(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x67739b75: ('quick_select_method', _decode_quick_select_method),
    0xa5e20450: ('menu', _decode_menu),
    0xa74987ff: ('choice', _decode_choice),
    0x73eb9d04: ('exit', _decode_exit),
}
