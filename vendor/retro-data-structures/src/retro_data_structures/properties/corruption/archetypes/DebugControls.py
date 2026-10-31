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
    class DebugControlsJson(typing_extensions.TypedDict):
        move_camera: json_util.JsonObject
        move_camera_fast: json_util.JsonObject
        move_camera_forward: json_util.JsonObject
        move_camera_backward: json_util.JsonObject
        move_camera_right: json_util.JsonObject
        move_camera_left: json_util.JsonObject
        turn_camera_right: json_util.JsonObject
        turn_camera_left: json_util.JsonObject
        pitch_camera_up: json_util.JsonObject
        pitch_camera_down: json_util.JsonObject
        toggle_camera: json_util.JsonObject
        drop_player: json_util.JsonObject
        menu_start: json_util.JsonObject
        menu_up: json_util.JsonObject
        menu_down: json_util.JsonObject
        menu_left: json_util.JsonObject
        menu_right: json_util.JsonObject
        menu_select: json_util.JsonObject
        menu_back: json_util.JsonObject
        menu_increment_value: json_util.JsonObject
        menu_decrement_value: json_util.JsonObject
        menu_value_multiplier: json_util.JsonObject
        restart_level: json_util.JsonObject
        map_teleport: json_util.JsonObject
        advance_frame: json_util.JsonObject
    

@dataclasses.dataclass()
class DebugControls(BaseProperty):
    move_camera: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x38ed0ec3, original_name='MoveCamera', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    move_camera_fast: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xce9d8f9b, original_name='MoveCameraFast', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    move_camera_forward: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xcf8d32f4, original_name='MoveCameraForward', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    move_camera_backward: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x6e2701e2, original_name='MoveCameraBackward', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    move_camera_right: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x233dfcb8, original_name='MoveCameraRight', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    move_camera_left: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x6c8eda79, original_name='MoveCameraLeft', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    turn_camera_right: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x52739b7b, original_name='TurnCameraRight', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    turn_camera_left: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x936c903d, original_name='TurnCameraLeft', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    pitch_camera_up: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xf3e413f0, original_name='PitchCameraUp', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    pitch_camera_down: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x769412eb, original_name='PitchCameraDown', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    toggle_camera: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xce92be94, original_name='ToggleCamera', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    drop_player: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xfc31e19e, original_name='DropPlayer', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    menu_start: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x0bfcb7a2, original_name='MenuStart', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
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
    menu_back: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xbcbe70f0, original_name='MenuBack', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    menu_increment_value: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xd38203d7, original_name='MenuIncrementValue', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    menu_decrement_value: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xed1235d3, original_name='MenuDecrementValue', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    menu_value_multiplier: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xc73501a3, original_name='MenuValueMultiplier', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    restart_level: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xc578ca0d, original_name='RestartLevel', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    map_teleport: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x8bb24630, original_name='MapTeleport', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    advance_frame: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x4c3fa03b, original_name='AdvanceFrame', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
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
        if property_count != 25:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x38ed0ec3
        move_camera = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xce9d8f9b
        move_camera_fast = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcf8d32f4
        move_camera_forward = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6e2701e2
        move_camera_backward = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x233dfcb8
        move_camera_right = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6c8eda79
        move_camera_left = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x52739b7b
        turn_camera_right = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x936c903d
        turn_camera_left = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf3e413f0
        pitch_camera_up = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x769412eb
        pitch_camera_down = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xce92be94
        toggle_camera = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfc31e19e
        drop_player = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0bfcb7a2
        menu_start = RevolutionControl.from_stream(data, game, property_size)
    
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
        assert property_id == 0xbcbe70f0
        menu_back = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd38203d7
        menu_increment_value = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed1235d3
        menu_decrement_value = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc73501a3
        menu_value_multiplier = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc578ca0d
        restart_level = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8bb24630
        map_teleport = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4c3fa03b
        advance_frame = RevolutionControl.from_stream(data, game, property_size)
    
        return cls(move_camera, move_camera_fast, move_camera_forward, move_camera_backward, move_camera_right, move_camera_left, turn_camera_right, turn_camera_left, pitch_camera_up, pitch_camera_down, toggle_camera, drop_player, menu_start, menu_up, menu_down, menu_left, menu_right, menu_select, menu_back, menu_increment_value, menu_decrement_value, menu_value_multiplier, restart_level, map_teleport, advance_frame)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x19')  # 25 properties

        data.write(b'8\xed\x0e\xc3')  # 0x38ed0ec3
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.move_camera.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xce\x9d\x8f\x9b')  # 0xce9d8f9b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.move_camera_fast.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xcf\x8d2\xf4')  # 0xcf8d32f4
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.move_camera_forward.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"n'\x01\xe2")  # 0x6e2701e2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.move_camera_backward.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'#=\xfc\xb8')  # 0x233dfcb8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.move_camera_right.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'l\x8e\xday')  # 0x6c8eda79
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.move_camera_left.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'Rs\x9b{')  # 0x52739b7b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.turn_camera_right.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x93l\x90=')  # 0x936c903d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.turn_camera_left.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf3\xe4\x13\xf0')  # 0xf3e413f0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.pitch_camera_up.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'v\x94\x12\xeb')  # 0x769412eb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.pitch_camera_down.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xce\x92\xbe\x94')  # 0xce92be94
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.toggle_camera.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfc1\xe1\x9e')  # 0xfc31e19e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.drop_player.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x0b\xfc\xb7\xa2')  # 0xbfcb7a2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.menu_start.to_stream(data, game)
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

        data.write(b'\xbc\xbep\xf0')  # 0xbcbe70f0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.menu_back.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd3\x82\x03\xd7')  # 0xd38203d7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.menu_increment_value.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xed\x125\xd3')  # 0xed1235d3
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.menu_decrement_value.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc75\x01\xa3')  # 0xc73501a3
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.menu_value_multiplier.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc5x\xca\r')  # 0xc578ca0d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.restart_level.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8b\xb2F0')  # 0x8bb24630
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.map_teleport.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'L?\xa0;')  # 0x4c3fa03b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.advance_frame.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DebugControlsJson", data)
        return cls(
            move_camera=RevolutionControl.from_json(json_data['move_camera']),
            move_camera_fast=RevolutionControl.from_json(json_data['move_camera_fast']),
            move_camera_forward=RevolutionControl.from_json(json_data['move_camera_forward']),
            move_camera_backward=RevolutionControl.from_json(json_data['move_camera_backward']),
            move_camera_right=RevolutionControl.from_json(json_data['move_camera_right']),
            move_camera_left=RevolutionControl.from_json(json_data['move_camera_left']),
            turn_camera_right=RevolutionControl.from_json(json_data['turn_camera_right']),
            turn_camera_left=RevolutionControl.from_json(json_data['turn_camera_left']),
            pitch_camera_up=RevolutionControl.from_json(json_data['pitch_camera_up']),
            pitch_camera_down=RevolutionControl.from_json(json_data['pitch_camera_down']),
            toggle_camera=RevolutionControl.from_json(json_data['toggle_camera']),
            drop_player=RevolutionControl.from_json(json_data['drop_player']),
            menu_start=RevolutionControl.from_json(json_data['menu_start']),
            menu_up=RevolutionControl.from_json(json_data['menu_up']),
            menu_down=RevolutionControl.from_json(json_data['menu_down']),
            menu_left=RevolutionControl.from_json(json_data['menu_left']),
            menu_right=RevolutionControl.from_json(json_data['menu_right']),
            menu_select=RevolutionControl.from_json(json_data['menu_select']),
            menu_back=RevolutionControl.from_json(json_data['menu_back']),
            menu_increment_value=RevolutionControl.from_json(json_data['menu_increment_value']),
            menu_decrement_value=RevolutionControl.from_json(json_data['menu_decrement_value']),
            menu_value_multiplier=RevolutionControl.from_json(json_data['menu_value_multiplier']),
            restart_level=RevolutionControl.from_json(json_data['restart_level']),
            map_teleport=RevolutionControl.from_json(json_data['map_teleport']),
            advance_frame=RevolutionControl.from_json(json_data['advance_frame']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'move_camera': self.move_camera.to_json(),
            'move_camera_fast': self.move_camera_fast.to_json(),
            'move_camera_forward': self.move_camera_forward.to_json(),
            'move_camera_backward': self.move_camera_backward.to_json(),
            'move_camera_right': self.move_camera_right.to_json(),
            'move_camera_left': self.move_camera_left.to_json(),
            'turn_camera_right': self.turn_camera_right.to_json(),
            'turn_camera_left': self.turn_camera_left.to_json(),
            'pitch_camera_up': self.pitch_camera_up.to_json(),
            'pitch_camera_down': self.pitch_camera_down.to_json(),
            'toggle_camera': self.toggle_camera.to_json(),
            'drop_player': self.drop_player.to_json(),
            'menu_start': self.menu_start.to_json(),
            'menu_up': self.menu_up.to_json(),
            'menu_down': self.menu_down.to_json(),
            'menu_left': self.menu_left.to_json(),
            'menu_right': self.menu_right.to_json(),
            'menu_select': self.menu_select.to_json(),
            'menu_back': self.menu_back.to_json(),
            'menu_increment_value': self.menu_increment_value.to_json(),
            'menu_decrement_value': self.menu_decrement_value.to_json(),
            'menu_value_multiplier': self.menu_value_multiplier.to_json(),
            'restart_level': self.restart_level.to_json(),
            'map_teleport': self.map_teleport.to_json(),
            'advance_frame': self.advance_frame.to_json(),
        }


def _decode_move_camera(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_move_camera_fast(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_move_camera_forward(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_move_camera_backward(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_move_camera_right(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_move_camera_left(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_turn_camera_right(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_turn_camera_left(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_pitch_camera_up(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_pitch_camera_down(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_toggle_camera(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_drop_player(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_menu_start(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
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


def _decode_menu_back(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_menu_increment_value(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_menu_decrement_value(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_menu_value_multiplier(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_restart_level(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_map_teleport(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_advance_frame(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x38ed0ec3: ('move_camera', _decode_move_camera),
    0xce9d8f9b: ('move_camera_fast', _decode_move_camera_fast),
    0xcf8d32f4: ('move_camera_forward', _decode_move_camera_forward),
    0x6e2701e2: ('move_camera_backward', _decode_move_camera_backward),
    0x233dfcb8: ('move_camera_right', _decode_move_camera_right),
    0x6c8eda79: ('move_camera_left', _decode_move_camera_left),
    0x52739b7b: ('turn_camera_right', _decode_turn_camera_right),
    0x936c903d: ('turn_camera_left', _decode_turn_camera_left),
    0xf3e413f0: ('pitch_camera_up', _decode_pitch_camera_up),
    0x769412eb: ('pitch_camera_down', _decode_pitch_camera_down),
    0xce92be94: ('toggle_camera', _decode_toggle_camera),
    0xfc31e19e: ('drop_player', _decode_drop_player),
    0x0bfcb7a2: ('menu_start', _decode_menu_start),
    0x769909c1: ('menu_up', _decode_menu_up),
    0x4dab695e: ('menu_down', _decode_menu_down),
    0xc7cae2d3: ('menu_left', _decode_menu_left),
    0x1595f276: ('menu_right', _decode_menu_right),
    0xbf09b38b: ('menu_select', _decode_menu_select),
    0xbcbe70f0: ('menu_back', _decode_menu_back),
    0xd38203d7: ('menu_increment_value', _decode_menu_increment_value),
    0xed1235d3: ('menu_decrement_value', _decode_menu_decrement_value),
    0xc73501a3: ('menu_value_multiplier', _decode_menu_value_multiplier),
    0xc578ca0d: ('restart_level', _decode_restart_level),
    0x8bb24630: ('map_teleport', _decode_map_teleport),
    0x4c3fa03b: ('advance_frame', _decode_advance_frame),
}
