# Generated File
from __future__ import annotations

import dataclasses
import struct
import typing
import typing_extensions

from retro_data_structures import json_util
from retro_data_structures.game_check import Game
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.archetypes.WorldTeleporterAttribute import WorldTeleporterAttribute

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class WorldTeleporterAttributesJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        _1: json_util.JsonObject
        _2: json_util.JsonObject
        _3: json_util.JsonObject
        _4: json_util.JsonObject
        _5: json_util.JsonObject
        _6: json_util.JsonObject
        _7: json_util.JsonObject
        _8: json_util.JsonObject
        _9: json_util.JsonObject
        _10: json_util.JsonObject
        _11: json_util.JsonObject
        _12: json_util.JsonObject
        _13: json_util.JsonObject
        _14: json_util.JsonObject
        _15: json_util.JsonObject
        _16: json_util.JsonObject
        _17: json_util.JsonObject
        _18: json_util.JsonObject
        _19: json_util.JsonObject
        _20: json_util.JsonObject
    

@dataclasses.dataclass()
class WorldTeleporterAttributes(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    _1: WorldTeleporterAttribute = dataclasses.field(default_factory=WorldTeleporterAttribute, metadata={
        'reflection': FieldReflection[WorldTeleporterAttribute](
            WorldTeleporterAttribute, id=0xcf05a0d1, original_name='1', from_json=WorldTeleporterAttribute.from_json, to_json=WorldTeleporterAttribute.to_json
        ),
    })
    _2: WorldTeleporterAttribute = dataclasses.field(default_factory=WorldTeleporterAttribute, metadata={
        'reflection': FieldReflection[WorldTeleporterAttribute](
            WorldTeleporterAttribute, id=0xfae81682, original_name='2', from_json=WorldTeleporterAttribute.from_json, to_json=WorldTeleporterAttribute.to_json
        ),
    })
    _3: WorldTeleporterAttribute = dataclasses.field(default_factory=WorldTeleporterAttribute, metadata={
        'reflection': FieldReflection[WorldTeleporterAttribute](
            WorldTeleporterAttribute, id=0x5f63868c, original_name='3', from_json=WorldTeleporterAttribute.from_json, to_json=WorldTeleporterAttribute.to_json
        ),
    })
    _4: WorldTeleporterAttribute = dataclasses.field(default_factory=WorldTeleporterAttribute, metadata={
        'reflection': FieldReflection[WorldTeleporterAttribute](
            WorldTeleporterAttribute, id=0x91337a24, original_name='4', from_json=WorldTeleporterAttribute.from_json, to_json=WorldTeleporterAttribute.to_json
        ),
    })
    _5: WorldTeleporterAttribute = dataclasses.field(default_factory=WorldTeleporterAttribute, metadata={
        'reflection': FieldReflection[WorldTeleporterAttribute](
            WorldTeleporterAttribute, id=0x34b8ea2a, original_name='5', from_json=WorldTeleporterAttribute.from_json, to_json=WorldTeleporterAttribute.to_json
        ),
    })
    _6: WorldTeleporterAttribute = dataclasses.field(default_factory=WorldTeleporterAttribute, metadata={
        'reflection': FieldReflection[WorldTeleporterAttribute](
            WorldTeleporterAttribute, id=0x01555c79, original_name='6', from_json=WorldTeleporterAttribute.from_json, to_json=WorldTeleporterAttribute.to_json
        ),
    })
    _7: WorldTeleporterAttribute = dataclasses.field(default_factory=WorldTeleporterAttribute, metadata={
        'reflection': FieldReflection[WorldTeleporterAttribute](
            WorldTeleporterAttribute, id=0xa4decc77, original_name='7', from_json=WorldTeleporterAttribute.from_json, to_json=WorldTeleporterAttribute.to_json
        ),
    })
    _8: WorldTeleporterAttribute = dataclasses.field(default_factory=WorldTeleporterAttribute, metadata={
        'reflection': FieldReflection[WorldTeleporterAttribute](
            WorldTeleporterAttribute, id=0x4685a368, original_name='8', from_json=WorldTeleporterAttribute.from_json, to_json=WorldTeleporterAttribute.to_json
        ),
    })
    _9: WorldTeleporterAttribute = dataclasses.field(default_factory=WorldTeleporterAttribute, metadata={
        'reflection': FieldReflection[WorldTeleporterAttribute](
            WorldTeleporterAttribute, id=0xe30e3366, original_name='9', from_json=WorldTeleporterAttribute.from_json, to_json=WorldTeleporterAttribute.to_json
        ),
    })
    _10: WorldTeleporterAttribute = dataclasses.field(default_factory=WorldTeleporterAttribute, metadata={
        'reflection': FieldReflection[WorldTeleporterAttribute](
            WorldTeleporterAttribute, id=0xee37cd3c, original_name='10', from_json=WorldTeleporterAttribute.from_json, to_json=WorldTeleporterAttribute.to_json
        ),
    })
    _11: WorldTeleporterAttribute = dataclasses.field(default_factory=WorldTeleporterAttribute, metadata={
        'reflection': FieldReflection[WorldTeleporterAttribute](
            WorldTeleporterAttribute, id=0x4bbc5d32, original_name='11', from_json=WorldTeleporterAttribute.from_json, to_json=WorldTeleporterAttribute.to_json
        ),
    })
    _12: WorldTeleporterAttribute = dataclasses.field(default_factory=WorldTeleporterAttribute, metadata={
        'reflection': FieldReflection[WorldTeleporterAttribute](
            WorldTeleporterAttribute, id=0x7e51eb61, original_name='12', from_json=WorldTeleporterAttribute.from_json, to_json=WorldTeleporterAttribute.to_json
        ),
    })
    _13: WorldTeleporterAttribute = dataclasses.field(default_factory=WorldTeleporterAttribute, metadata={
        'reflection': FieldReflection[WorldTeleporterAttribute](
            WorldTeleporterAttribute, id=0xdbda7b6f, original_name='13', from_json=WorldTeleporterAttribute.from_json, to_json=WorldTeleporterAttribute.to_json
        ),
    })
    _14: WorldTeleporterAttribute = dataclasses.field(default_factory=WorldTeleporterAttribute, metadata={
        'reflection': FieldReflection[WorldTeleporterAttribute](
            WorldTeleporterAttribute, id=0x158a87c7, original_name='14', from_json=WorldTeleporterAttribute.from_json, to_json=WorldTeleporterAttribute.to_json
        ),
    })
    _15: WorldTeleporterAttribute = dataclasses.field(default_factory=WorldTeleporterAttribute, metadata={
        'reflection': FieldReflection[WorldTeleporterAttribute](
            WorldTeleporterAttribute, id=0xb00117c9, original_name='15', from_json=WorldTeleporterAttribute.from_json, to_json=WorldTeleporterAttribute.to_json
        ),
    })
    _16: WorldTeleporterAttribute = dataclasses.field(default_factory=WorldTeleporterAttribute, metadata={
        'reflection': FieldReflection[WorldTeleporterAttribute](
            WorldTeleporterAttribute, id=0x85eca19a, original_name='16', from_json=WorldTeleporterAttribute.from_json, to_json=WorldTeleporterAttribute.to_json
        ),
    })
    _17: WorldTeleporterAttribute = dataclasses.field(default_factory=WorldTeleporterAttribute, metadata={
        'reflection': FieldReflection[WorldTeleporterAttribute](
            WorldTeleporterAttribute, id=0x20673194, original_name='17', from_json=WorldTeleporterAttribute.from_json, to_json=WorldTeleporterAttribute.to_json
        ),
    })
    _18: WorldTeleporterAttribute = dataclasses.field(default_factory=WorldTeleporterAttribute, metadata={
        'reflection': FieldReflection[WorldTeleporterAttribute](
            WorldTeleporterAttribute, id=0xc23c5e8b, original_name='18', from_json=WorldTeleporterAttribute.from_json, to_json=WorldTeleporterAttribute.to_json
        ),
    })
    _19: WorldTeleporterAttribute = dataclasses.field(default_factory=WorldTeleporterAttribute, metadata={
        'reflection': FieldReflection[WorldTeleporterAttribute](
            WorldTeleporterAttribute, id=0x67b7ce85, original_name='19', from_json=WorldTeleporterAttribute.from_json, to_json=WorldTeleporterAttribute.to_json
        ),
    })
    _20: WorldTeleporterAttribute = dataclasses.field(default_factory=WorldTeleporterAttribute, metadata={
        'reflection': FieldReflection[WorldTeleporterAttribute](
            WorldTeleporterAttribute, id=0x1c6020c4, original_name='20', from_json=WorldTeleporterAttribute.from_json, to_json=WorldTeleporterAttribute.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'WTAT'

    @classmethod
    def modules(cls) -> list[str]:
        return ['RSO_ScriptWorldTeleporterAttributes.rso']

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
        if property_count != 21:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcf05a0d1
        _1 = WorldTeleporterAttribute.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfae81682
        _2 = WorldTeleporterAttribute.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5f63868c
        _3 = WorldTeleporterAttribute.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x91337a24
        _4 = WorldTeleporterAttribute.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x34b8ea2a
        _5 = WorldTeleporterAttribute.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x01555c79
        _6 = WorldTeleporterAttribute.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa4decc77
        _7 = WorldTeleporterAttribute.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4685a368
        _8 = WorldTeleporterAttribute.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe30e3366
        _9 = WorldTeleporterAttribute.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xee37cd3c
        _10 = WorldTeleporterAttribute.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4bbc5d32
        _11 = WorldTeleporterAttribute.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e51eb61
        _12 = WorldTeleporterAttribute.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdbda7b6f
        _13 = WorldTeleporterAttribute.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x158a87c7
        _14 = WorldTeleporterAttribute.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb00117c9
        _15 = WorldTeleporterAttribute.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x85eca19a
        _16 = WorldTeleporterAttribute.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x20673194
        _17 = WorldTeleporterAttribute.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc23c5e8b
        _18 = WorldTeleporterAttribute.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x67b7ce85
        _19 = WorldTeleporterAttribute.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1c6020c4
        _20 = WorldTeleporterAttribute.from_stream(data, game, property_size)
    
        return cls(editor_properties, _1, _2, _3, _4, _5, _6, _7, _8, _9, _10, _11, _12, _13, _14, _15, _16, _17, _18, _19, _20)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x0f')  # 15 properties
        num_properties_written = 15

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xcf\x05\xa0\xd1')  # 0xcf05a0d1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self._1.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfa\xe8\x16\x82')  # 0xfae81682
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self._2.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'_c\x86\x8c')  # 0x5f63868c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self._3.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x913z$')  # 0x91337a24
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self._4.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'4\xb8\xea*')  # 0x34b8ea2a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self._5.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x01U\\y')  # 0x1555c79
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self._6.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa4\xde\xccw')  # 0xa4decc77
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self._7.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'F\x85\xa3h')  # 0x4685a368
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self._8.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe3\x0e3f')  # 0xe30e3366
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self._9.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xee7\xcd<')  # 0xee37cd3c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self._10.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'K\xbc]2')  # 0x4bbc5d32
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self._11.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'~Q\xeba')  # 0x7e51eb61
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self._12.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xdb\xda{o')  # 0xdbda7b6f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self._13.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x15\x8a\x87\xc7')  # 0x158a87c7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self._14.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        if self._15 != default_override.get('_15', WorldTeleporterAttribute()):
            num_properties_written += 1
            data.write(b'\xb0\x01\x17\xc9')  # 0xb00117c9
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            self._15.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self._16 != default_override.get('_16', WorldTeleporterAttribute()):
            num_properties_written += 1
            data.write(b'\x85\xec\xa1\x9a')  # 0x85eca19a
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            self._16.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self._17 != default_override.get('_17', WorldTeleporterAttribute()):
            num_properties_written += 1
            data.write(b' g1\x94')  # 0x20673194
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            self._17.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self._18 != default_override.get('_18', WorldTeleporterAttribute()):
            num_properties_written += 1
            data.write(b'\xc2<^\x8b')  # 0xc23c5e8b
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            self._18.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self._19 != default_override.get('_19', WorldTeleporterAttribute()):
            num_properties_written += 1
            data.write(b'g\xb7\xce\x85')  # 0x67b7ce85
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            self._19.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self._20 != default_override.get('_20', WorldTeleporterAttribute()):
            num_properties_written += 1
            data.write(b'\x1c` \xc4')  # 0x1c6020c4
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            self._20.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.write(struct.pack(">H", num_properties_written))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("WorldTeleporterAttributesJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            _1=WorldTeleporterAttribute.from_json(json_data['_1']),
            _2=WorldTeleporterAttribute.from_json(json_data['_2']),
            _3=WorldTeleporterAttribute.from_json(json_data['_3']),
            _4=WorldTeleporterAttribute.from_json(json_data['_4']),
            _5=WorldTeleporterAttribute.from_json(json_data['_5']),
            _6=WorldTeleporterAttribute.from_json(json_data['_6']),
            _7=WorldTeleporterAttribute.from_json(json_data['_7']),
            _8=WorldTeleporterAttribute.from_json(json_data['_8']),
            _9=WorldTeleporterAttribute.from_json(json_data['_9']),
            _10=WorldTeleporterAttribute.from_json(json_data['_10']),
            _11=WorldTeleporterAttribute.from_json(json_data['_11']),
            _12=WorldTeleporterAttribute.from_json(json_data['_12']),
            _13=WorldTeleporterAttribute.from_json(json_data['_13']),
            _14=WorldTeleporterAttribute.from_json(json_data['_14']),
            _15=WorldTeleporterAttribute.from_json(json_data['_15']),
            _16=WorldTeleporterAttribute.from_json(json_data['_16']),
            _17=WorldTeleporterAttribute.from_json(json_data['_17']),
            _18=WorldTeleporterAttribute.from_json(json_data['_18']),
            _19=WorldTeleporterAttribute.from_json(json_data['_19']),
            _20=WorldTeleporterAttribute.from_json(json_data['_20']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            '_1': self._1.to_json(),
            '_2': self._2.to_json(),
            '_3': self._3.to_json(),
            '_4': self._4.to_json(),
            '_5': self._5.to_json(),
            '_6': self._6.to_json(),
            '_7': self._7.to_json(),
            '_8': self._8.to_json(),
            '_9': self._9.to_json(),
            '_10': self._10.to_json(),
            '_11': self._11.to_json(),
            '_12': self._12.to_json(),
            '_13': self._13.to_json(),
            '_14': self._14.to_json(),
            '_15': self._15.to_json(),
            '_16': self._16.to_json(),
            '_17': self._17.to_json(),
            '_18': self._18.to_json(),
            '_19': self._19.to_json(),
            '_20': self._20.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode__1(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTeleporterAttribute:
    return WorldTeleporterAttribute.from_stream(data, game, property_size)


def _decode__2(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTeleporterAttribute:
    return WorldTeleporterAttribute.from_stream(data, game, property_size)


def _decode__3(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTeleporterAttribute:
    return WorldTeleporterAttribute.from_stream(data, game, property_size)


def _decode__4(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTeleporterAttribute:
    return WorldTeleporterAttribute.from_stream(data, game, property_size)


def _decode__5(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTeleporterAttribute:
    return WorldTeleporterAttribute.from_stream(data, game, property_size)


def _decode__6(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTeleporterAttribute:
    return WorldTeleporterAttribute.from_stream(data, game, property_size)


def _decode__7(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTeleporterAttribute:
    return WorldTeleporterAttribute.from_stream(data, game, property_size)


def _decode__8(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTeleporterAttribute:
    return WorldTeleporterAttribute.from_stream(data, game, property_size)


def _decode__9(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTeleporterAttribute:
    return WorldTeleporterAttribute.from_stream(data, game, property_size)


def _decode__10(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTeleporterAttribute:
    return WorldTeleporterAttribute.from_stream(data, game, property_size)


def _decode__11(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTeleporterAttribute:
    return WorldTeleporterAttribute.from_stream(data, game, property_size)


def _decode__12(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTeleporterAttribute:
    return WorldTeleporterAttribute.from_stream(data, game, property_size)


def _decode__13(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTeleporterAttribute:
    return WorldTeleporterAttribute.from_stream(data, game, property_size)


def _decode__14(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTeleporterAttribute:
    return WorldTeleporterAttribute.from_stream(data, game, property_size)


def _decode__15(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTeleporterAttribute:
    return WorldTeleporterAttribute.from_stream(data, game, property_size)


def _decode__16(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTeleporterAttribute:
    return WorldTeleporterAttribute.from_stream(data, game, property_size)


def _decode__17(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTeleporterAttribute:
    return WorldTeleporterAttribute.from_stream(data, game, property_size)


def _decode__18(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTeleporterAttribute:
    return WorldTeleporterAttribute.from_stream(data, game, property_size)


def _decode__19(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTeleporterAttribute:
    return WorldTeleporterAttribute.from_stream(data, game, property_size)


def _decode__20(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTeleporterAttribute:
    return WorldTeleporterAttribute.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xcf05a0d1: ('_1', _decode__1),
    0xfae81682: ('_2', _decode__2),
    0x5f63868c: ('_3', _decode__3),
    0x91337a24: ('_4', _decode__4),
    0x34b8ea2a: ('_5', _decode__5),
    0x01555c79: ('_6', _decode__6),
    0xa4decc77: ('_7', _decode__7),
    0x4685a368: ('_8', _decode__8),
    0xe30e3366: ('_9', _decode__9),
    0xee37cd3c: ('_10', _decode__10),
    0x4bbc5d32: ('_11', _decode__11),
    0x7e51eb61: ('_12', _decode__12),
    0xdbda7b6f: ('_13', _decode__13),
    0x158a87c7: ('_14', _decode__14),
    0xb00117c9: ('_15', _decode__15),
    0x85eca19a: ('_16', _decode__16),
    0x20673194: ('_17', _decode__17),
    0xc23c5e8b: ('_18', _decode__18),
    0x67b7ce85: ('_19', _decode__19),
    0x1c6020c4: ('_20', _decode__20),
}
