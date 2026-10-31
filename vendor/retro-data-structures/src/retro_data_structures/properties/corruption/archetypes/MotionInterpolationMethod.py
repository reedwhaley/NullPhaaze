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
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.corruption.archetypes.InterpolationMethod import InterpolationMethod
from retro_data_structures.properties.corruption.archetypes.PathInterpolation import PathInterpolation

if typing.TYPE_CHECKING:
    class MotionInterpolationMethodJson(typing_extensions.TypedDict):
        motion_type: int
        path: json_util.JsonObject
        motion_control: json_util.JsonObject
    

class MotionType(enum.IntEnum):
    kMIT_None = 2003923368
    kMIT_Linear = 1102650983
    kMIT_Path = 62257768

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
class MotionInterpolationMethod(BaseProperty):
    motion_type: MotionType = dataclasses.field(default=MotionType.kMIT_Linear, metadata={
        'reflection': FieldReflection[MotionType](
            MotionType, id=0x948af571, original_name='MotionType', from_json=MotionType.from_json, to_json=MotionType.to_json
        ),
    })
    path: PathInterpolation = dataclasses.field(default_factory=PathInterpolation, metadata={
        'reflection': FieldReflection[PathInterpolation](
            PathInterpolation, id=0x79de4ba5, original_name='Path', from_json=PathInterpolation.from_json, to_json=PathInterpolation.to_json
        ),
    })
    motion_control: InterpolationMethod = dataclasses.field(default_factory=InterpolationMethod, metadata={
        'reflection': FieldReflection[InterpolationMethod](
            InterpolationMethod, id=0x287f9f45, original_name='MotionControl', from_json=InterpolationMethod.from_json, to_json=InterpolationMethod.to_json
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
        if property_count != 3:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x948af571
        motion_type = MotionType.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x79de4ba5
        path = PathInterpolation.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x287f9f45
        motion_control = InterpolationMethod.from_stream(data, game, property_size)
    
        return cls(motion_type, path, motion_control)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x03')  # 3 properties

        data.write(b'\x94\x8a\xf5q')  # 0x948af571
        data.write(b'\x00\x04')  # size
        self.motion_type.to_stream(data, game)

        data.write(b'y\xdeK\xa5')  # 0x79de4ba5
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.path.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'(\x7f\x9fE')  # 0x287f9f45
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.motion_control.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MotionInterpolationMethodJson", data)
        return cls(
            motion_type=MotionType.from_json(json_data['motion_type']),
            path=PathInterpolation.from_json(json_data['path']),
            motion_control=InterpolationMethod.from_json(json_data['motion_control']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'motion_type': self.motion_type.to_json(),
            'path': self.path.to_json(),
            'motion_control': self.motion_control.to_json(),
        }


def _decode_motion_type(data: typing.BinaryIO, game: Game, property_size: int) -> MotionType:
    return MotionType.from_stream(data, game)


def _decode_path(data: typing.BinaryIO, game: Game, property_size: int) -> PathInterpolation:
    return PathInterpolation.from_stream(data, game, property_size)


def _decode_motion_control(data: typing.BinaryIO, game: Game, property_size: int) -> InterpolationMethod:
    return InterpolationMethod.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x948af571: ('motion_type', _decode_motion_type),
    0x79de4ba5: ('path', _decode_path),
    0x287f9f45: ('motion_control', _decode_motion_control),
}
