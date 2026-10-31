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
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class PlayerHintJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        priority: int
        timer: float
        interpolate_control_time: float
        flags: int
    

class PlayerHintFlags(enum.IntFlag):
    Unknown1 = 1
    ControlDirOverride = 2
    ExtendTargetDistance = 4
    OutOfBallLookAtHint = 8
    SpiderBallControlXY = 16
    DisableUnmorph = 32
    DisableMorph = 64
    DisableControls = 128
    DisableBoost = 256
    ForceCombatVisor = 512
    ForceScanVisor = 1024
    ForceDarkVisor = 2048
    ForceEchoVisor = 4096
    FreezePlayer = 8192
    FaceOnUnmorph = 16384
    IgnoreDarkWorldDamage = 32768
    NoSafeZoneHealing = 65536
    NoMorphBallDamageTimer = 131072
    AbsorbPhazonShots = 262144
    ForceFreeLook = 524288
    AcrossAreas = 1048576
    ForceFirstPerson = 2097152
    ForceThirdPerson = 4194304
    DampBoostEntryVelocity = 8388608

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
class PlayerHint(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    priority: int = dataclasses.field(default=10, metadata={
        'reflection': FieldReflection[int](
            int, id=0x42087650, original_name='Priority'
        ),
    })
    timer: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8747552e, original_name='Timer'
        ),
    })
    interpolate_control_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc91ef813, original_name='InterpolateControlTime'
        ),
    })
    flags: PlayerHintFlags = dataclasses.field(default=PlayerHintFlags(1), metadata={
        'reflection': FieldReflection[PlayerHintFlags](
            PlayerHintFlags, id=0x1bce57e1, original_name='Flags', from_json=PlayerHintFlags.from_json, to_json=PlayerHintFlags.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'HINT'

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
        editor_properties = EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42087650
        priority = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8747552e
        timer = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc91ef813
        interpolate_control_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1bce57e1
        flags = PlayerHintFlags.from_stream(data, game)
    
        return cls(editor_properties, priority, timer, interpolate_control_time, flags)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x05')  # 5 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game, default_override={'misc_flags': 3})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'B\x08vP')  # 0x42087650
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.priority))

        data.write(b'\x87GU.')  # 0x8747552e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.timer))

        data.write(b'\xc9\x1e\xf8\x13')  # 0xc91ef813
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.interpolate_control_time))

        data.write(b'\x1b\xceW\xe1')  # 0x1bce57e1
        data.write(b'\x00\x04')  # size
        self.flags.to_stream(data, game)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlayerHintJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            priority=json_data['priority'],
            timer=json_data['timer'],
            interpolate_control_time=json_data['interpolate_control_time'],
            flags=PlayerHintFlags.from_json(json_data['flags']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'priority': self.priority,
            'timer': self.timer,
            'interpolate_control_time': self.interpolate_control_time,
            'flags': self.flags.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})


def _decode_flags(data: typing.BinaryIO, game: Game, property_size: int) -> PlayerHintFlags:
    return PlayerHintFlags.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0x42087650: ('priority', structs.decode_BIG_l),
    0x8747552e: ('timer', structs.decode_BIG_f),
    0xc91ef813: ('interpolate_control_time', structs.decode_BIG_f),
    0x1bce57e1: ('flags', _decode_flags),
}
