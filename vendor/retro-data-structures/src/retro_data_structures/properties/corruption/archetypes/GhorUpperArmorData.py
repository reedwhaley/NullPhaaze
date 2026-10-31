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
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.GhorArmorPiece import GhorArmorPiece

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class GhorUpperArmorDataJson(typing_extensions.TypedDict):
        face_plate: json_util.JsonObject
        left_collar: json_util.JsonObject
        left_jammer: json_util.JsonObject
        right_jammer: json_util.JsonObject
        spine: json_util.JsonObject
        collision_set: str
        vulnerability: json_util.JsonObject
    

@dataclasses.dataclass()
class GhorUpperArmorData(BaseProperty):
    face_plate: GhorArmorPiece = dataclasses.field(default_factory=GhorArmorPiece, metadata={
        'reflection': FieldReflection[GhorArmorPiece](
            GhorArmorPiece, id=0x17386c2c, original_name='FacePlate', from_json=GhorArmorPiece.from_json, to_json=GhorArmorPiece.to_json
        ),
    })
    left_collar: GhorArmorPiece = dataclasses.field(default_factory=GhorArmorPiece, metadata={
        'reflection': FieldReflection[GhorArmorPiece](
            GhorArmorPiece, id=0xd171838c, original_name='LeftCollar', from_json=GhorArmorPiece.from_json, to_json=GhorArmorPiece.to_json
        ),
    })
    left_jammer: GhorArmorPiece = dataclasses.field(default_factory=GhorArmorPiece, metadata={
        'reflection': FieldReflection[GhorArmorPiece](
            GhorArmorPiece, id=0x017549cb, original_name='LeftJammer', from_json=GhorArmorPiece.from_json, to_json=GhorArmorPiece.to_json
        ),
    })
    right_jammer: GhorArmorPiece = dataclasses.field(default_factory=GhorArmorPiece, metadata={
        'reflection': FieldReflection[GhorArmorPiece](
            GhorArmorPiece, id=0x08f6bdc5, original_name='RightJammer', from_json=GhorArmorPiece.from_json, to_json=GhorArmorPiece.to_json
        ),
    })
    spine: GhorArmorPiece = dataclasses.field(default_factory=GhorArmorPiece, metadata={
        'reflection': FieldReflection[GhorArmorPiece](
            GhorArmorPiece, id=0x7b589dd6, original_name='Spine', from_json=GhorArmorPiece.from_json, to_json=GhorArmorPiece.to_json
        ),
    })
    collision_set: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x9ce31ffa, original_name='CollisionSet'
        ),
    })
    vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x7b71ae90, original_name='Vulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
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
        assert property_id == 0x17386c2c
        face_plate = GhorArmorPiece.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd171838c
        left_collar = GhorArmorPiece.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x017549cb
        left_jammer = GhorArmorPiece.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08f6bdc5
        right_jammer = GhorArmorPiece.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7b589dd6
        spine = GhorArmorPiece.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9ce31ffa
        collision_set = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7b71ae90
        vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        return cls(face_plate, left_collar, left_jammer, right_jammer, spine, collision_set, vulnerability)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x07')  # 7 properties

        data.write(b'\x178l,')  # 0x17386c2c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.face_plate.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd1q\x83\x8c')  # 0xd171838c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.left_collar.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x01uI\xcb')  # 0x17549cb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.left_jammer.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x08\xf6\xbd\xc5')  # 0x8f6bdc5
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.right_jammer.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'{X\x9d\xd6')  # 0x7b589dd6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.spine.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9c\xe3\x1f\xfa')  # 0x9ce31ffa
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.collision_set.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'{q\xae\x90')  # 0x7b71ae90
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GhorUpperArmorDataJson", data)
        return cls(
            face_plate=GhorArmorPiece.from_json(json_data['face_plate']),
            left_collar=GhorArmorPiece.from_json(json_data['left_collar']),
            left_jammer=GhorArmorPiece.from_json(json_data['left_jammer']),
            right_jammer=GhorArmorPiece.from_json(json_data['right_jammer']),
            spine=GhorArmorPiece.from_json(json_data['spine']),
            collision_set=json_data['collision_set'],
            vulnerability=DamageVulnerability.from_json(json_data['vulnerability']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'face_plate': self.face_plate.to_json(),
            'left_collar': self.left_collar.to_json(),
            'left_jammer': self.left_jammer.to_json(),
            'right_jammer': self.right_jammer.to_json(),
            'spine': self.spine.to_json(),
            'collision_set': self.collision_set,
            'vulnerability': self.vulnerability.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.face_plate.dependencies_for, "face_plate", "GhorArmorPiece"),
            (self.left_collar.dependencies_for, "left_collar", "GhorArmorPiece"),
            (self.left_jammer.dependencies_for, "left_jammer", "GhorArmorPiece"),
            (self.right_jammer.dependencies_for, "right_jammer", "GhorArmorPiece"),
            (self.spine.dependencies_for, "spine", "GhorArmorPiece"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for GhorUpperArmorData.{field_name} ({field_type}): {e}"
                )


def _decode_face_plate(data: typing.BinaryIO, game: Game, property_size: int) -> GhorArmorPiece:
    return GhorArmorPiece.from_stream(data, game, property_size)


def _decode_left_collar(data: typing.BinaryIO, game: Game, property_size: int) -> GhorArmorPiece:
    return GhorArmorPiece.from_stream(data, game, property_size)


def _decode_left_jammer(data: typing.BinaryIO, game: Game, property_size: int) -> GhorArmorPiece:
    return GhorArmorPiece.from_stream(data, game, property_size)


def _decode_right_jammer(data: typing.BinaryIO, game: Game, property_size: int) -> GhorArmorPiece:
    return GhorArmorPiece.from_stream(data, game, property_size)


def _decode_spine(data: typing.BinaryIO, game: Game, property_size: int) -> GhorArmorPiece:
    return GhorArmorPiece.from_stream(data, game, property_size)


def _decode_collision_set(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x17386c2c: ('face_plate', _decode_face_plate),
    0xd171838c: ('left_collar', _decode_left_collar),
    0x017549cb: ('left_jammer', _decode_left_jammer),
    0x08f6bdc5: ('right_jammer', _decode_right_jammer),
    0x7b589dd6: ('spine', _decode_spine),
    0x9ce31ffa: ('collision_set', _decode_collision_set),
    0x7b71ae90: ('vulnerability', _decode_vulnerability),
}
