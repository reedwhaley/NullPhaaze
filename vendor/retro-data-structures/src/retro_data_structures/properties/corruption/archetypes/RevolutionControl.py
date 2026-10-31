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
from retro_data_structures.properties.corruption.archetypes.ControlCommands import ControlCommands
from retro_data_structures.properties.corruption.archetypes.RevolutionDPDControl import RevolutionDPDControl
from retro_data_structures.properties.corruption.archetypes.RevolutionPhysicalControl import RevolutionPhysicalControl

if typing.TYPE_CHECKING:
    class RevolutionControlJson(typing_extensions.TypedDict):
        command_enum: json_util.JsonObject
        revolution_control_type: int
        physical_control: json_util.JsonObject
        physical_control_boolean: int
        physical_control2: json_util.JsonObject
        revolution_virtual_control: int
        virtual_control_boolean: int
        revolution_virtual_control2: int
        revolution_gesture: int
        revolution_pointer_control: json_util.JsonObject
    

@dataclasses.dataclass()
class RevolutionControl(BaseProperty):
    command_enum: ControlCommands = dataclasses.field(default_factory=ControlCommands, metadata={
        'reflection': FieldReflection[ControlCommands](
            ControlCommands, id=0xb0d17d4d, original_name='CommandEnum', from_json=ControlCommands.from_json, to_json=ControlCommands.to_json
        ),
    })
    revolution_control_type: enums.RevolutionControlTypeEnum = dataclasses.field(default=enums.RevolutionControlTypeEnum.kRCT_Physical, metadata={
        'reflection': FieldReflection[enums.RevolutionControlTypeEnum](
            enums.RevolutionControlTypeEnum, id=0x81cc3d3e, original_name='RevolutionControlType', from_json=enums.RevolutionControlTypeEnum.from_json, to_json=enums.RevolutionControlTypeEnum.to_json
        ),
    })
    physical_control: RevolutionPhysicalControl = dataclasses.field(default_factory=RevolutionPhysicalControl, metadata={
        'reflection': FieldReflection[RevolutionPhysicalControl](
            RevolutionPhysicalControl, id=0xe646d3b7, original_name='PhysicalControl', from_json=RevolutionPhysicalControl.from_json, to_json=RevolutionPhysicalControl.to_json
        ),
    })
    physical_control_boolean: enums.PhysicalControlBooleanEnum = dataclasses.field(default=enums.PhysicalControlBooleanEnum.kPCB_And, metadata={
        'reflection': FieldReflection[enums.PhysicalControlBooleanEnum](
            enums.PhysicalControlBooleanEnum, id=0x6e14bc06, original_name='PhysicalControlBoolean', from_json=enums.PhysicalControlBooleanEnum.from_json, to_json=enums.PhysicalControlBooleanEnum.to_json
        ),
    })
    physical_control2: RevolutionPhysicalControl = dataclasses.field(default_factory=RevolutionPhysicalControl, metadata={
        'reflection': FieldReflection[RevolutionPhysicalControl](
            RevolutionPhysicalControl, id=0xf0bf68a4, original_name='PhysicalControl2', from_json=RevolutionPhysicalControl.from_json, to_json=RevolutionPhysicalControl.to_json
        ),
    })
    revolution_virtual_control: enums.RevolutionVirtualControlEnum = dataclasses.field(default=enums.RevolutionVirtualControlEnum.kRVC_Tap, metadata={
        'reflection': FieldReflection[enums.RevolutionVirtualControlEnum](
            enums.RevolutionVirtualControlEnum, id=0xfe819ddb, original_name='RevolutionVirtualControl', from_json=enums.RevolutionVirtualControlEnum.from_json, to_json=enums.RevolutionVirtualControlEnum.to_json
        ),
    })
    virtual_control_boolean: enums.PhysicalControlBooleanEnum = dataclasses.field(default=enums.PhysicalControlBooleanEnum.kPCB_And, metadata={
        'reflection': FieldReflection[enums.PhysicalControlBooleanEnum](
            enums.PhysicalControlBooleanEnum, id=0xebaabf01, original_name='VirtualControlBoolean', from_json=enums.PhysicalControlBooleanEnum.from_json, to_json=enums.PhysicalControlBooleanEnum.to_json
        ),
    })
    revolution_virtual_control2: enums.RevolutionVirtualControlEnum = dataclasses.field(default=enums.RevolutionVirtualControlEnum.kRVC_Tap, metadata={
        'reflection': FieldReflection[enums.RevolutionVirtualControlEnum](
            enums.RevolutionVirtualControlEnum, id=0xeda6d736, original_name='RevolutionVirtualControl2', from_json=enums.RevolutionVirtualControlEnum.from_json, to_json=enums.RevolutionVirtualControlEnum.to_json
        ),
    })
    revolution_gesture: enums.RevolutionGestureEnum = dataclasses.field(default=enums.RevolutionGestureEnum.kRG_ThrustForward, metadata={
        'reflection': FieldReflection[enums.RevolutionGestureEnum](
            enums.RevolutionGestureEnum, id=0xbf80d594, original_name='RevolutionGesture', from_json=enums.RevolutionGestureEnum.from_json, to_json=enums.RevolutionGestureEnum.to_json
        ),
    })
    revolution_pointer_control: RevolutionDPDControl = dataclasses.field(default_factory=RevolutionDPDControl, metadata={
        'reflection': FieldReflection[RevolutionDPDControl](
            RevolutionDPDControl, id=0x91b8c18a, original_name='RevolutionPointerControl', from_json=RevolutionDPDControl.from_json, to_json=RevolutionDPDControl.to_json
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
        if property_count != 10:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb0d17d4d
        command_enum = ControlCommands.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x81cc3d3e
        revolution_control_type = enums.RevolutionControlTypeEnum.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe646d3b7
        physical_control = RevolutionPhysicalControl.from_stream(data, game, property_size, default_override={'physical_control': enums.PhysicalControlEnum.kControl_REV_B})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6e14bc06
        physical_control_boolean = enums.PhysicalControlBooleanEnum.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf0bf68a4
        physical_control2 = RevolutionPhysicalControl.from_stream(data, game, property_size, default_override={'physical_control': enums.PhysicalControlEnum.kControl_REV_B})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfe819ddb
        revolution_virtual_control = enums.RevolutionVirtualControlEnum.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xebaabf01
        virtual_control_boolean = enums.PhysicalControlBooleanEnum.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xeda6d736
        revolution_virtual_control2 = enums.RevolutionVirtualControlEnum.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbf80d594
        revolution_gesture = enums.RevolutionGestureEnum.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x91b8c18a
        revolution_pointer_control = RevolutionDPDControl.from_stream(data, game, property_size)
    
        return cls(command_enum, revolution_control_type, physical_control, physical_control_boolean, physical_control2, revolution_virtual_control, virtual_control_boolean, revolution_virtual_control2, revolution_gesture, revolution_pointer_control)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        num_properties_offset = data.tell()
        data.write(b'\x00\x03')  # 3 properties
        num_properties_written = 3

        data.write(b'\xb0\xd1}M')  # 0xb0d17d4d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.command_enum.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x81\xcc=>')  # 0x81cc3d3e
        data.write(b'\x00\x04')  # size
        self.revolution_control_type.to_stream(data, game)

        data.write(b'\xe6F\xd3\xb7')  # 0xe646d3b7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.physical_control.to_stream(data, game, default_override={'physical_control': enums.PhysicalControlEnum.kControl_REV_B})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        if self.physical_control_boolean != default_override.get('physical_control_boolean', enums.PhysicalControlBooleanEnum.kPCB_And):
            num_properties_written += 1
            data.write(b'n\x14\xbc\x06')  # 0x6e14bc06
            data.write(b'\x00\x04')  # size
            self.physical_control_boolean.to_stream(data, game)

        if self.physical_control2 != default_override.get('physical_control2', RevolutionPhysicalControl()):
            num_properties_written += 1
            data.write(b'\xf0\xbfh\xa4')  # 0xf0bf68a4
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            self.physical_control2.to_stream(data, game, default_override={'physical_control': enums.PhysicalControlEnum.kControl_REV_B})
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self.revolution_virtual_control != default_override.get('revolution_virtual_control', enums.RevolutionVirtualControlEnum.kRVC_Tap):
            num_properties_written += 1
            data.write(b'\xfe\x81\x9d\xdb')  # 0xfe819ddb
            data.write(b'\x00\x04')  # size
            self.revolution_virtual_control.to_stream(data, game)

        if self.virtual_control_boolean != default_override.get('virtual_control_boolean', enums.PhysicalControlBooleanEnum.kPCB_And):
            num_properties_written += 1
            data.write(b'\xeb\xaa\xbf\x01')  # 0xebaabf01
            data.write(b'\x00\x04')  # size
            self.virtual_control_boolean.to_stream(data, game)

        if self.revolution_virtual_control2 != default_override.get('revolution_virtual_control2', enums.RevolutionVirtualControlEnum.kRVC_Tap):
            num_properties_written += 1
            data.write(b'\xed\xa6\xd76')  # 0xeda6d736
            data.write(b'\x00\x04')  # size
            self.revolution_virtual_control2.to_stream(data, game)

        if self.revolution_gesture != default_override.get('revolution_gesture', enums.RevolutionGestureEnum.kRG_ThrustForward):
            num_properties_written += 1
            data.write(b'\xbf\x80\xd5\x94')  # 0xbf80d594
            data.write(b'\x00\x04')  # size
            self.revolution_gesture.to_stream(data, game)

        if self.revolution_pointer_control != default_override.get('revolution_pointer_control', RevolutionDPDControl()):
            num_properties_written += 1
            data.write(b'\x91\xb8\xc1\x8a')  # 0x91b8c18a
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            self.revolution_pointer_control.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if num_properties_written != 3:
            struct_end_offset = data.tell()
            data.seek(num_properties_offset)
            data.write(struct.pack(">H", num_properties_written))
            data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("RevolutionControlJson", data)
        return cls(
            command_enum=ControlCommands.from_json(json_data['command_enum']),
            revolution_control_type=enums.RevolutionControlTypeEnum.from_json(json_data['revolution_control_type']),
            physical_control=RevolutionPhysicalControl.from_json(json_data['physical_control']),
            physical_control_boolean=enums.PhysicalControlBooleanEnum.from_json(json_data['physical_control_boolean']),
            physical_control2=RevolutionPhysicalControl.from_json(json_data['physical_control2']),
            revolution_virtual_control=enums.RevolutionVirtualControlEnum.from_json(json_data['revolution_virtual_control']),
            virtual_control_boolean=enums.PhysicalControlBooleanEnum.from_json(json_data['virtual_control_boolean']),
            revolution_virtual_control2=enums.RevolutionVirtualControlEnum.from_json(json_data['revolution_virtual_control2']),
            revolution_gesture=enums.RevolutionGestureEnum.from_json(json_data['revolution_gesture']),
            revolution_pointer_control=RevolutionDPDControl.from_json(json_data['revolution_pointer_control']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'command_enum': self.command_enum.to_json(),
            'revolution_control_type': self.revolution_control_type.to_json(),
            'physical_control': self.physical_control.to_json(),
            'physical_control_boolean': self.physical_control_boolean.to_json(),
            'physical_control2': self.physical_control2.to_json(),
            'revolution_virtual_control': self.revolution_virtual_control.to_json(),
            'virtual_control_boolean': self.virtual_control_boolean.to_json(),
            'revolution_virtual_control2': self.revolution_virtual_control2.to_json(),
            'revolution_gesture': self.revolution_gesture.to_json(),
            'revolution_pointer_control': self.revolution_pointer_control.to_json(),
        }


def _decode_command_enum(data: typing.BinaryIO, game: Game, property_size: int) -> ControlCommands:
    return ControlCommands.from_stream(data, game, property_size)


def _decode_revolution_control_type(data: typing.BinaryIO, game: Game, property_size: int) -> enums.RevolutionControlTypeEnum:
    return enums.RevolutionControlTypeEnum.from_stream(data, game)


def _decode_physical_control(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionPhysicalControl:
    return RevolutionPhysicalControl.from_stream(data, game, property_size, default_override={'physical_control': enums.PhysicalControlEnum.kControl_REV_B})


def _decode_physical_control_boolean(data: typing.BinaryIO, game: Game, property_size: int) -> enums.PhysicalControlBooleanEnum:
    return enums.PhysicalControlBooleanEnum.from_stream(data, game)


def _decode_physical_control2(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionPhysicalControl:
    return RevolutionPhysicalControl.from_stream(data, game, property_size, default_override={'physical_control': enums.PhysicalControlEnum.kControl_REV_B})


def _decode_revolution_virtual_control(data: typing.BinaryIO, game: Game, property_size: int) -> enums.RevolutionVirtualControlEnum:
    return enums.RevolutionVirtualControlEnum.from_stream(data, game)


def _decode_virtual_control_boolean(data: typing.BinaryIO, game: Game, property_size: int) -> enums.PhysicalControlBooleanEnum:
    return enums.PhysicalControlBooleanEnum.from_stream(data, game)


def _decode_revolution_virtual_control2(data: typing.BinaryIO, game: Game, property_size: int) -> enums.RevolutionVirtualControlEnum:
    return enums.RevolutionVirtualControlEnum.from_stream(data, game)


def _decode_revolution_gesture(data: typing.BinaryIO, game: Game, property_size: int) -> enums.RevolutionGestureEnum:
    return enums.RevolutionGestureEnum.from_stream(data, game)


def _decode_revolution_pointer_control(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionDPDControl:
    return RevolutionDPDControl.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xb0d17d4d: ('command_enum', _decode_command_enum),
    0x81cc3d3e: ('revolution_control_type', _decode_revolution_control_type),
    0xe646d3b7: ('physical_control', _decode_physical_control),
    0x6e14bc06: ('physical_control_boolean', _decode_physical_control_boolean),
    0xf0bf68a4: ('physical_control2', _decode_physical_control2),
    0xfe819ddb: ('revolution_virtual_control', _decode_revolution_virtual_control),
    0xebaabf01: ('virtual_control_boolean', _decode_virtual_control_boolean),
    0xeda6d736: ('revolution_virtual_control2', _decode_revolution_virtual_control2),
    0xbf80d594: ('revolution_gesture', _decode_revolution_gesture),
    0x91b8c18a: ('revolution_pointer_control', _decode_revolution_pointer_control),
}
