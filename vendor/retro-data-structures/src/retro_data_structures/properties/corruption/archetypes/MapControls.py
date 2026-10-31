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
    class MapControlsJson(typing_extensions.TypedDict):
        map_screen: json_util.JsonObject
        map_circle_up: json_util.JsonObject
        map_circle_down: json_util.JsonObject
        map_circle_left: json_util.JsonObject
        map_circle_right: json_util.JsonObject
        map_rotate_enable: json_util.JsonObject
        map_move_forward: json_util.JsonObject
        map_move_backward: json_util.JsonObject
        map_move_left: json_util.JsonObject
        map_move_right: json_util.JsonObject
        map_pointer_pan_enable: json_util.JsonObject
        map_zoom_in: json_util.JsonObject
        map_zoom_out: json_util.JsonObject
        map_legend: json_util.JsonObject
        map_select: json_util.JsonObject
        map_help: json_util.JsonObject
        map_exit: json_util.JsonObject
        map_history_back: json_util.JsonObject
        map_navigate_up: json_util.JsonObject
        map_navigate_down: json_util.JsonObject
        map_navigate_left: json_util.JsonObject
        map_navigate_right: json_util.JsonObject
    

@dataclasses.dataclass()
class MapControls(BaseProperty):
    map_screen: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xfed78da3, original_name='MapScreen', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_circle_up: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x74e647c1, original_name='MapCircleUp', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_circle_down: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xdccf07b6, original_name='MapCircleDown', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_circle_left: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x56ae8c3b, original_name='MapCircleLeft', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_circle_right: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xbbd5fc52, original_name='MapCircleRight', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_rotate_enable: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x19a0c4cb, original_name='MapRotateEnable', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_move_forward: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x827c4e63, original_name='MapMoveForward', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_move_backward: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x0001f679, original_name='MapMoveBackward', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_move_left: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xfb5628fa, original_name='MapMoveLeft', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_move_right: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x571bf6d0, original_name='MapMoveRight', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_pointer_pan_enable: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xcfaa0627, original_name='MapPointerPanEnable', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_zoom_in: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x385cbd2f, original_name='MapZoomIn', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_zoom_out: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x5f55ccca, original_name='MapZoomOut', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_legend: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x85e1418d, original_name='MapLegend', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_select: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xb5f75bfb, original_name='MapSelect', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_help: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x31c2d282, original_name='MapHelp', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_exit: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xfaa6abe5, original_name='MapExit', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_history_back: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xdda39041, original_name='MapHistoryBack', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_navigate_up: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x705876ab, original_name='MapNavigateUp', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_navigate_down: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x1203801f, original_name='MapNavigateDown', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_navigate_left: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x98620b92, original_name='MapNavigateLeft', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_navigate_right: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x14112b99, original_name='MapNavigateRight', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
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
        if property_count != 22:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfed78da3
        map_screen = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x74e647c1
        map_circle_up = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdccf07b6
        map_circle_down = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x56ae8c3b
        map_circle_left = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbbd5fc52
        map_circle_right = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19a0c4cb
        map_rotate_enable = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x827c4e63
        map_move_forward = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0001f679
        map_move_backward = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfb5628fa
        map_move_left = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x571bf6d0
        map_move_right = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcfaa0627
        map_pointer_pan_enable = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x385cbd2f
        map_zoom_in = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5f55ccca
        map_zoom_out = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x85e1418d
        map_legend = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb5f75bfb
        map_select = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x31c2d282
        map_help = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfaa6abe5
        map_exit = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdda39041
        map_history_back = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x705876ab
        map_navigate_up = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1203801f
        map_navigate_down = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x98620b92
        map_navigate_left = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x14112b99
        map_navigate_right = RevolutionControl.from_stream(data, game, property_size)
    
        return cls(map_screen, map_circle_up, map_circle_down, map_circle_left, map_circle_right, map_rotate_enable, map_move_forward, map_move_backward, map_move_left, map_move_right, map_pointer_pan_enable, map_zoom_in, map_zoom_out, map_legend, map_select, map_help, map_exit, map_history_back, map_navigate_up, map_navigate_down, map_navigate_left, map_navigate_right)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x16')  # 22 properties

        data.write(b'\xfe\xd7\x8d\xa3')  # 0xfed78da3
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_screen.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b't\xe6G\xc1')  # 0x74e647c1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_circle_up.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xdc\xcf\x07\xb6')  # 0xdccf07b6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_circle_down.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'V\xae\x8c;')  # 0x56ae8c3b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_circle_left.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbb\xd5\xfcR')  # 0xbbd5fc52
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_circle_right.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x19\xa0\xc4\xcb')  # 0x19a0c4cb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_rotate_enable.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x82|Nc')  # 0x827c4e63
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_move_forward.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x00\x01\xf6y')  # 0x1f679
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_move_backward.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfbV(\xfa')  # 0xfb5628fa
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_move_left.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'W\x1b\xf6\xd0')  # 0x571bf6d0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_move_right.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xcf\xaa\x06'")  # 0xcfaa0627
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_pointer_pan_enable.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'8\\\xbd/')  # 0x385cbd2f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_zoom_in.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'_U\xcc\xca')  # 0x5f55ccca
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_zoom_out.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x85\xe1A\x8d')  # 0x85e1418d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_legend.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb5\xf7[\xfb')  # 0xb5f75bfb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_select.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'1\xc2\xd2\x82')  # 0x31c2d282
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_help.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfa\xa6\xab\xe5')  # 0xfaa6abe5
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_exit.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xdd\xa3\x90A')  # 0xdda39041
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_history_back.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'pXv\xab')  # 0x705876ab
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_navigate_up.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x12\x03\x80\x1f')  # 0x1203801f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_navigate_down.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x98b\x0b\x92')  # 0x98620b92
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_navigate_left.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x14\x11+\x99')  # 0x14112b99
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_navigate_right.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MapControlsJson", data)
        return cls(
            map_screen=RevolutionControl.from_json(json_data['map_screen']),
            map_circle_up=RevolutionControl.from_json(json_data['map_circle_up']),
            map_circle_down=RevolutionControl.from_json(json_data['map_circle_down']),
            map_circle_left=RevolutionControl.from_json(json_data['map_circle_left']),
            map_circle_right=RevolutionControl.from_json(json_data['map_circle_right']),
            map_rotate_enable=RevolutionControl.from_json(json_data['map_rotate_enable']),
            map_move_forward=RevolutionControl.from_json(json_data['map_move_forward']),
            map_move_backward=RevolutionControl.from_json(json_data['map_move_backward']),
            map_move_left=RevolutionControl.from_json(json_data['map_move_left']),
            map_move_right=RevolutionControl.from_json(json_data['map_move_right']),
            map_pointer_pan_enable=RevolutionControl.from_json(json_data['map_pointer_pan_enable']),
            map_zoom_in=RevolutionControl.from_json(json_data['map_zoom_in']),
            map_zoom_out=RevolutionControl.from_json(json_data['map_zoom_out']),
            map_legend=RevolutionControl.from_json(json_data['map_legend']),
            map_select=RevolutionControl.from_json(json_data['map_select']),
            map_help=RevolutionControl.from_json(json_data['map_help']),
            map_exit=RevolutionControl.from_json(json_data['map_exit']),
            map_history_back=RevolutionControl.from_json(json_data['map_history_back']),
            map_navigate_up=RevolutionControl.from_json(json_data['map_navigate_up']),
            map_navigate_down=RevolutionControl.from_json(json_data['map_navigate_down']),
            map_navigate_left=RevolutionControl.from_json(json_data['map_navigate_left']),
            map_navigate_right=RevolutionControl.from_json(json_data['map_navigate_right']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'map_screen': self.map_screen.to_json(),
            'map_circle_up': self.map_circle_up.to_json(),
            'map_circle_down': self.map_circle_down.to_json(),
            'map_circle_left': self.map_circle_left.to_json(),
            'map_circle_right': self.map_circle_right.to_json(),
            'map_rotate_enable': self.map_rotate_enable.to_json(),
            'map_move_forward': self.map_move_forward.to_json(),
            'map_move_backward': self.map_move_backward.to_json(),
            'map_move_left': self.map_move_left.to_json(),
            'map_move_right': self.map_move_right.to_json(),
            'map_pointer_pan_enable': self.map_pointer_pan_enable.to_json(),
            'map_zoom_in': self.map_zoom_in.to_json(),
            'map_zoom_out': self.map_zoom_out.to_json(),
            'map_legend': self.map_legend.to_json(),
            'map_select': self.map_select.to_json(),
            'map_help': self.map_help.to_json(),
            'map_exit': self.map_exit.to_json(),
            'map_history_back': self.map_history_back.to_json(),
            'map_navigate_up': self.map_navigate_up.to_json(),
            'map_navigate_down': self.map_navigate_down.to_json(),
            'map_navigate_left': self.map_navigate_left.to_json(),
            'map_navigate_right': self.map_navigate_right.to_json(),
        }


def _decode_map_screen(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_circle_up(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_circle_down(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_circle_left(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_circle_right(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_rotate_enable(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_move_forward(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_move_backward(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_move_left(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_move_right(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_pointer_pan_enable(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_zoom_in(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_zoom_out(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_legend(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_select(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_help(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_exit(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_history_back(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_navigate_up(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_navigate_down(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_navigate_left(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_navigate_right(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xfed78da3: ('map_screen', _decode_map_screen),
    0x74e647c1: ('map_circle_up', _decode_map_circle_up),
    0xdccf07b6: ('map_circle_down', _decode_map_circle_down),
    0x56ae8c3b: ('map_circle_left', _decode_map_circle_left),
    0xbbd5fc52: ('map_circle_right', _decode_map_circle_right),
    0x19a0c4cb: ('map_rotate_enable', _decode_map_rotate_enable),
    0x827c4e63: ('map_move_forward', _decode_map_move_forward),
    0x0001f679: ('map_move_backward', _decode_map_move_backward),
    0xfb5628fa: ('map_move_left', _decode_map_move_left),
    0x571bf6d0: ('map_move_right', _decode_map_move_right),
    0xcfaa0627: ('map_pointer_pan_enable', _decode_map_pointer_pan_enable),
    0x385cbd2f: ('map_zoom_in', _decode_map_zoom_in),
    0x5f55ccca: ('map_zoom_out', _decode_map_zoom_out),
    0x85e1418d: ('map_legend', _decode_map_legend),
    0xb5f75bfb: ('map_select', _decode_map_select),
    0x31c2d282: ('map_help', _decode_map_help),
    0xfaa6abe5: ('map_exit', _decode_map_exit),
    0xdda39041: ('map_history_back', _decode_map_history_back),
    0x705876ab: ('map_navigate_up', _decode_map_navigate_up),
    0x1203801f: ('map_navigate_down', _decode_map_navigate_down),
    0x98620b92: ('map_navigate_left', _decode_map_navigate_left),
    0x14112b99: ('map_navigate_right', _decode_map_navigate_right),
}
