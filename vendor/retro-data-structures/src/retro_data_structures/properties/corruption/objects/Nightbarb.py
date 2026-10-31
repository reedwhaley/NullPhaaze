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
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.archetypes.FlyerSwarmData import FlyerSwarmData
from retro_data_structures.properties.corruption.archetypes.SwarmBasicsData import SwarmBasicsData
from retro_data_structures.properties.corruption.archetypes.UnknownStruct48 import UnknownStruct48
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class NightbarbJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        actor_information: json_util.JsonObject
        character_animation_information: json_util.JsonObject
        active: bool
        basic_swarm_properties: json_util.JsonObject
        flyer_swarm_properties: json_util.JsonObject
        unknown_struct48: json_util.JsonObject
    

@dataclasses.dataclass()
class Nightbarb(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    actor_information: ActorParameters = dataclasses.field(default_factory=ActorParameters, metadata={
        'reflection': FieldReflection[ActorParameters](
            ActorParameters, id=0x7e397fed, original_name='ActorInformation', from_json=ActorParameters.from_json, to_json=ActorParameters.to_json
        ),
    })
    character_animation_information: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0xa244c9d8, original_name='CharacterAnimationInformation', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    active: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xc6bb2f45, original_name='Active'
        ),
    })
    basic_swarm_properties: SwarmBasicsData = dataclasses.field(default_factory=SwarmBasicsData, metadata={
        'reflection': FieldReflection[SwarmBasicsData](
            SwarmBasicsData, id=0x4cfc46fe, original_name='BasicSwarmProperties', from_json=SwarmBasicsData.from_json, to_json=SwarmBasicsData.to_json
        ),
    })
    flyer_swarm_properties: FlyerSwarmData = dataclasses.field(default_factory=FlyerSwarmData, metadata={
        'reflection': FieldReflection[FlyerSwarmData](
            FlyerSwarmData, id=0x99c18702, original_name='FlyerSwarmProperties', from_json=FlyerSwarmData.from_json, to_json=FlyerSwarmData.to_json
        ),
    })
    unknown_struct48: UnknownStruct48 = dataclasses.field(default_factory=UnknownStruct48, metadata={
        'reflection': FieldReflection[UnknownStruct48](
            UnknownStruct48, id=0x7971e068, original_name='UnknownStruct48', from_json=UnknownStruct48.from_json, to_json=UnknownStruct48.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'NBAR'

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
        if property_count != 7:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa244c9d8
        character_animation_information = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc6bb2f45
        active = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4cfc46fe
        basic_swarm_properties = SwarmBasicsData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x99c18702
        flyer_swarm_properties = FlyerSwarmData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7971e068
        unknown_struct48 = UnknownStruct48.from_stream(data, game, property_size)
    
        return cls(editor_properties, actor_information, character_animation_information, active, basic_swarm_properties, flyer_swarm_properties, unknown_struct48)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x07')  # 7 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
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

        data.write(b'\xa2D\xc9\xd8')  # 0xa244c9d8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.character_animation_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc6\xbb/E')  # 0xc6bb2f45
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.active))

        data.write(b'L\xfcF\xfe')  # 0x4cfc46fe
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.basic_swarm_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x99\xc1\x87\x02')  # 0x99c18702
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.flyer_swarm_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'yq\xe0h')  # 0x7971e068
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.unknown_struct48.to_stream(data, game)
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
        json_data = typing.cast("NightbarbJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
            character_animation_information=AnimationParameters.from_json(json_data['character_animation_information']),
            active=json_data['active'],
            basic_swarm_properties=SwarmBasicsData.from_json(json_data['basic_swarm_properties']),
            flyer_swarm_properties=FlyerSwarmData.from_json(json_data['flyer_swarm_properties']),
            unknown_struct48=UnknownStruct48.from_json(json_data['unknown_struct48']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'actor_information': self.actor_information.to_json(),
            'character_animation_information': self.character_animation_information.to_json(),
            'active': self.active,
            'basic_swarm_properties': self.basic_swarm_properties.to_json(),
            'flyer_swarm_properties': self.flyer_swarm_properties.to_json(),
            'unknown_struct48': self.unknown_struct48.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self.character_animation_information.dependencies_for, "character_animation_information", "AnimationParameters"),
            (self.basic_swarm_properties.dependencies_for, "basic_swarm_properties", "SwarmBasicsData"),
            (self.unknown_struct48.dependencies_for, "unknown_struct48", "UnknownStruct48"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for Nightbarb.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_character_animation_information(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_basic_swarm_properties(data: typing.BinaryIO, game: Game, property_size: int) -> SwarmBasicsData:
    return SwarmBasicsData.from_stream(data, game, property_size)


def _decode_flyer_swarm_properties(data: typing.BinaryIO, game: Game, property_size: int) -> FlyerSwarmData:
    return FlyerSwarmData.from_stream(data, game, property_size)


def _decode_unknown_struct48(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct48:
    return UnknownStruct48.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0xa244c9d8: ('character_animation_information', _decode_character_animation_information),
    0xc6bb2f45: ('active', structs.decode_BIG_bool_),
    0x4cfc46fe: ('basic_swarm_properties', _decode_basic_swarm_properties),
    0x99c18702: ('flyer_swarm_properties', _decode_flyer_swarm_properties),
    0x7971e068: ('unknown_struct48', _decode_unknown_struct48),
}
