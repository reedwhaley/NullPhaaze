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
from retro_data_structures.properties.corruption.archetypes.GhorArmorPiece import GhorArmorPiece

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class GhorLowerArmorDataJson(typing_extensions.TypedDict):
        cup: json_util.JsonObject
        left_hip: json_util.JsonObject
        right_hip: json_util.JsonObject
        right_flap: json_util.JsonObject
        right_knee_flap: json_util.JsonObject
    

@dataclasses.dataclass()
class GhorLowerArmorData(BaseProperty):
    cup: GhorArmorPiece = dataclasses.field(default_factory=GhorArmorPiece, metadata={
        'reflection': FieldReflection[GhorArmorPiece](
            GhorArmorPiece, id=0x8b5db983, original_name='Cup', from_json=GhorArmorPiece.from_json, to_json=GhorArmorPiece.to_json
        ),
    })
    left_hip: GhorArmorPiece = dataclasses.field(default_factory=GhorArmorPiece, metadata={
        'reflection': FieldReflection[GhorArmorPiece](
            GhorArmorPiece, id=0x04cdc6a6, original_name='LeftHip', from_json=GhorArmorPiece.from_json, to_json=GhorArmorPiece.to_json
        ),
    })
    right_hip: GhorArmorPiece = dataclasses.field(default_factory=GhorArmorPiece, metadata={
        'reflection': FieldReflection[GhorArmorPiece](
            GhorArmorPiece, id=0xe451d02c, original_name='RightHip', from_json=GhorArmorPiece.from_json, to_json=GhorArmorPiece.to_json
        ),
    })
    right_flap: GhorArmorPiece = dataclasses.field(default_factory=GhorArmorPiece, metadata={
        'reflection': FieldReflection[GhorArmorPiece](
            GhorArmorPiece, id=0x72f708f2, original_name='RightFlap', from_json=GhorArmorPiece.from_json, to_json=GhorArmorPiece.to_json
        ),
    })
    right_knee_flap: GhorArmorPiece = dataclasses.field(default_factory=GhorArmorPiece, metadata={
        'reflection': FieldReflection[GhorArmorPiece](
            GhorArmorPiece, id=0x8cb41734, original_name='RightKneeFlap', from_json=GhorArmorPiece.from_json, to_json=GhorArmorPiece.to_json
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
        if property_count != 5:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8b5db983
        cup = GhorArmorPiece.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x04cdc6a6
        left_hip = GhorArmorPiece.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe451d02c
        right_hip = GhorArmorPiece.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x72f708f2
        right_flap = GhorArmorPiece.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8cb41734
        right_knee_flap = GhorArmorPiece.from_stream(data, game, property_size)
    
        return cls(cup, left_hip, right_hip, right_flap, right_knee_flap)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x05')  # 5 properties

        data.write(b'\x8b]\xb9\x83')  # 0x8b5db983
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.cup.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x04\xcd\xc6\xa6')  # 0x4cdc6a6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.left_hip.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe4Q\xd0,')  # 0xe451d02c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.right_hip.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'r\xf7\x08\xf2')  # 0x72f708f2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.right_flap.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8c\xb4\x174')  # 0x8cb41734
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.right_knee_flap.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GhorLowerArmorDataJson", data)
        return cls(
            cup=GhorArmorPiece.from_json(json_data['cup']),
            left_hip=GhorArmorPiece.from_json(json_data['left_hip']),
            right_hip=GhorArmorPiece.from_json(json_data['right_hip']),
            right_flap=GhorArmorPiece.from_json(json_data['right_flap']),
            right_knee_flap=GhorArmorPiece.from_json(json_data['right_knee_flap']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'cup': self.cup.to_json(),
            'left_hip': self.left_hip.to_json(),
            'right_hip': self.right_hip.to_json(),
            'right_flap': self.right_flap.to_json(),
            'right_knee_flap': self.right_knee_flap.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.cup.dependencies_for, "cup", "GhorArmorPiece"),
            (self.left_hip.dependencies_for, "left_hip", "GhorArmorPiece"),
            (self.right_hip.dependencies_for, "right_hip", "GhorArmorPiece"),
            (self.right_flap.dependencies_for, "right_flap", "GhorArmorPiece"),
            (self.right_knee_flap.dependencies_for, "right_knee_flap", "GhorArmorPiece"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for GhorLowerArmorData.{field_name} ({field_type}): {e}"
                )


def _decode_cup(data: typing.BinaryIO, game: Game, property_size: int) -> GhorArmorPiece:
    return GhorArmorPiece.from_stream(data, game, property_size)


def _decode_left_hip(data: typing.BinaryIO, game: Game, property_size: int) -> GhorArmorPiece:
    return GhorArmorPiece.from_stream(data, game, property_size)


def _decode_right_hip(data: typing.BinaryIO, game: Game, property_size: int) -> GhorArmorPiece:
    return GhorArmorPiece.from_stream(data, game, property_size)


def _decode_right_flap(data: typing.BinaryIO, game: Game, property_size: int) -> GhorArmorPiece:
    return GhorArmorPiece.from_stream(data, game, property_size)


def _decode_right_knee_flap(data: typing.BinaryIO, game: Game, property_size: int) -> GhorArmorPiece:
    return GhorArmorPiece.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x8b5db983: ('cup', _decode_cup),
    0x04cdc6a6: ('left_hip', _decode_left_hip),
    0xe451d02c: ('right_hip', _decode_right_hip),
    0x72f708f2: ('right_flap', _decode_right_flap),
    0x8cb41734: ('right_knee_flap', _decode_right_knee_flap),
}
