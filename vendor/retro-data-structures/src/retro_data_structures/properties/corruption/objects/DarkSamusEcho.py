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
from retro_data_structures.properties.corruption.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.corruption.archetypes.DarkSamusEchoData import DarkSamusEchoData
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.archetypes.PatternedAITypedef import PatternedAITypedef

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class DarkSamusEchoJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        dark_samus_echo_properties: json_util.JsonObject
        dark_samus_echo_hard_properties: json_util.JsonObject
        dark_samus_echo_elite_properties: json_util.JsonObject
    

@dataclasses.dataclass()
class DarkSamusEcho(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    patterned: PatternedAITypedef = dataclasses.field(default_factory=PatternedAITypedef, metadata={
        'reflection': FieldReflection[PatternedAITypedef](
            PatternedAITypedef, id=0xb3774750, original_name='Patterned', from_json=PatternedAITypedef.from_json, to_json=PatternedAITypedef.to_json
        ),
    })
    actor_information: ActorParameters = dataclasses.field(default_factory=ActorParameters, metadata={
        'reflection': FieldReflection[ActorParameters](
            ActorParameters, id=0x7e397fed, original_name='ActorInformation', from_json=ActorParameters.from_json, to_json=ActorParameters.to_json
        ),
    })
    dark_samus_echo_properties: DarkSamusEchoData = dataclasses.field(default_factory=DarkSamusEchoData, metadata={
        'reflection': FieldReflection[DarkSamusEchoData](
            DarkSamusEchoData, id=0x6d8a6608, original_name='DarkSamusEchoProperties', from_json=DarkSamusEchoData.from_json, to_json=DarkSamusEchoData.to_json
        ),
    })
    dark_samus_echo_hard_properties: DarkSamusEchoData = dataclasses.field(default_factory=DarkSamusEchoData, metadata={
        'reflection': FieldReflection[DarkSamusEchoData](
            DarkSamusEchoData, id=0x35c49ddd, original_name='DarkSamusEchoHardProperties', from_json=DarkSamusEchoData.from_json, to_json=DarkSamusEchoData.to_json
        ),
    })
    dark_samus_echo_elite_properties: DarkSamusEchoData = dataclasses.field(default_factory=DarkSamusEchoData, metadata={
        'reflection': FieldReflection[DarkSamusEchoData](
            DarkSamusEchoData, id=0xa1178bcf, original_name='DarkSamusEchoEliteProperties', from_json=DarkSamusEchoData.from_json, to_json=DarkSamusEchoData.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'DKSE'

    @classmethod
    def modules(cls) -> list[str]:
        return ['RSO_DarkSamusEcho.rso']

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
        if property_count != 6:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size, default_override={'turn_speed': 360.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6d8a6608
        dark_samus_echo_properties = DarkSamusEchoData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x35c49ddd
        dark_samus_echo_hard_properties = DarkSamusEchoData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa1178bcf
        dark_samus_echo_elite_properties = DarkSamusEchoData.from_stream(data, game, property_size)
    
        return cls(editor_properties, patterned, actor_information, dark_samus_echo_properties, dark_samus_echo_hard_properties, dark_samus_echo_elite_properties)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x06')  # 6 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb3wGP')  # 0xb3774750
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.patterned.to_stream(data, game, default_override={'turn_speed': 360.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'~9\x7f\xed')  # 0x7e397fed
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.actor_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'm\x8af\x08')  # 0x6d8a6608
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.dark_samus_echo_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'5\xc4\x9d\xdd')  # 0x35c49ddd
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.dark_samus_echo_hard_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa1\x17\x8b\xcf')  # 0xa1178bcf
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.dark_samus_echo_elite_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DarkSamusEchoJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            patterned=PatternedAITypedef.from_json(json_data['patterned']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
            dark_samus_echo_properties=DarkSamusEchoData.from_json(json_data['dark_samus_echo_properties']),
            dark_samus_echo_hard_properties=DarkSamusEchoData.from_json(json_data['dark_samus_echo_hard_properties']),
            dark_samus_echo_elite_properties=DarkSamusEchoData.from_json(json_data['dark_samus_echo_elite_properties']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'patterned': self.patterned.to_json(),
            'actor_information': self.actor_information.to_json(),
            'dark_samus_echo_properties': self.dark_samus_echo_properties.to_json(),
            'dark_samus_echo_hard_properties': self.dark_samus_echo_hard_properties.to_json(),
            'dark_samus_echo_elite_properties': self.dark_samus_echo_elite_properties.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self.dark_samus_echo_properties.dependencies_for, "dark_samus_echo_properties", "DarkSamusEchoData"),
            (self.dark_samus_echo_hard_properties.dependencies_for, "dark_samus_echo_hard_properties", "DarkSamusEchoData"),
            (self.dark_samus_echo_elite_properties.dependencies_for, "dark_samus_echo_elite_properties", "DarkSamusEchoData"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for DarkSamusEcho.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={'turn_speed': 360.0})


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_dark_samus_echo_properties(data: typing.BinaryIO, game: Game, property_size: int) -> DarkSamusEchoData:
    return DarkSamusEchoData.from_stream(data, game, property_size)


def _decode_dark_samus_echo_hard_properties(data: typing.BinaryIO, game: Game, property_size: int) -> DarkSamusEchoData:
    return DarkSamusEchoData.from_stream(data, game, property_size)


def _decode_dark_samus_echo_elite_properties(data: typing.BinaryIO, game: Game, property_size: int) -> DarkSamusEchoData:
    return DarkSamusEchoData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xb3774750: ('patterned', _decode_patterned),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0x6d8a6608: ('dark_samus_echo_properties', _decode_dark_samus_echo_properties),
    0x35c49ddd: ('dark_samus_echo_hard_properties', _decode_dark_samus_echo_hard_properties),
    0xa1178bcf: ('dark_samus_echo_elite_properties', _decode_dark_samus_echo_elite_properties),
}
