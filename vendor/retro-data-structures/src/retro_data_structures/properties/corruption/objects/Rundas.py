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
from retro_data_structures.properties.corruption.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.corruption.archetypes.RundasAssets import RundasAssets
from retro_data_structures.properties.corruption.archetypes.RundasData import RundasData

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class RundasJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        rundas_assets: json_util.JsonObject
        rundas_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        rundas_properties_easy_difficulty: json_util.JsonObject
        patterned_easy_difficulty: json_util.JsonObject
        rundas_properties_elite_difficulty: json_util.JsonObject
        patterned_elite_difficulty: json_util.JsonObject
        actor_information: json_util.JsonObject
    

@dataclasses.dataclass()
class Rundas(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    rundas_assets: RundasAssets = dataclasses.field(default_factory=RundasAssets, metadata={
        'reflection': FieldReflection[RundasAssets](
            RundasAssets, id=0xa6790709, original_name='RundasAssets', from_json=RundasAssets.from_json, to_json=RundasAssets.to_json
        ),
    })
    rundas_properties: RundasData = dataclasses.field(default_factory=RundasData, metadata={
        'reflection': FieldReflection[RundasData](
            RundasData, id=0x9d90d49f, original_name='RundasProperties', from_json=RundasData.from_json, to_json=RundasData.to_json
        ),
    })
    patterned: PatternedAITypedef = dataclasses.field(default_factory=PatternedAITypedef, metadata={
        'reflection': FieldReflection[PatternedAITypedef](
            PatternedAITypedef, id=0xb3774750, original_name='Patterned', from_json=PatternedAITypedef.from_json, to_json=PatternedAITypedef.to_json
        ),
    })
    rundas_properties_easy_difficulty: RundasData = dataclasses.field(default_factory=RundasData, metadata={
        'reflection': FieldReflection[RundasData](
            RundasData, id=0x877b2ce9, original_name='RundasPropertiesEasyDifficulty', from_json=RundasData.from_json, to_json=RundasData.to_json
        ),
    })
    patterned_easy_difficulty: PatternedAITypedef = dataclasses.field(default_factory=PatternedAITypedef, metadata={
        'reflection': FieldReflection[PatternedAITypedef](
            PatternedAITypedef, id=0x1464ae05, original_name='PatternedEasyDifficulty', from_json=PatternedAITypedef.from_json, to_json=PatternedAITypedef.to_json
        ),
    })
    rundas_properties_elite_difficulty: RundasData = dataclasses.field(default_factory=RundasData, metadata={
        'reflection': FieldReflection[RundasData](
            RundasData, id=0xce6183d8, original_name='RundasPropertiesEliteDifficulty', from_json=RundasData.from_json, to_json=RundasData.to_json
        ),
    })
    patterned_elite_difficulty: PatternedAITypedef = dataclasses.field(default_factory=PatternedAITypedef, metadata={
        'reflection': FieldReflection[PatternedAITypedef](
            PatternedAITypedef, id=0x24d00673, original_name='PatternedEliteDifficulty', from_json=PatternedAITypedef.from_json, to_json=PatternedAITypedef.to_json
        ),
    })
    actor_information: ActorParameters = dataclasses.field(default_factory=ActorParameters, metadata={
        'reflection': FieldReflection[ActorParameters](
            ActorParameters, id=0x7e397fed, original_name='ActorInformation', from_json=ActorParameters.from_json, to_json=ActorParameters.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'RUND'

    @classmethod
    def modules(cls) -> list[str]:
        return ['RSO_Rundas.rso']

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
        if property_count != 9:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa6790709
        rundas_assets = RundasAssets.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9d90d49f
        rundas_properties = RundasData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size, default_override={'leash_radius': 100.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x877b2ce9
        rundas_properties_easy_difficulty = RundasData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1464ae05
        patterned_easy_difficulty = PatternedAITypedef.from_stream(data, game, property_size, default_override={'leash_radius': 100.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xce6183d8
        rundas_properties_elite_difficulty = RundasData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24d00673
        patterned_elite_difficulty = PatternedAITypedef.from_stream(data, game, property_size, default_override={'leash_radius': 100.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        return cls(editor_properties, rundas_assets, rundas_properties, patterned, rundas_properties_easy_difficulty, patterned_easy_difficulty, rundas_properties_elite_difficulty, patterned_elite_difficulty, actor_information)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\t')  # 9 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa6y\x07\t')  # 0xa6790709
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.rundas_assets.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9d\x90\xd4\x9f')  # 0x9d90d49f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.rundas_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb3wGP')  # 0xb3774750
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.patterned.to_stream(data, game, default_override={'leash_radius': 100.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x87{,\xe9')  # 0x877b2ce9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.rundas_properties_easy_difficulty.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x14d\xae\x05')  # 0x1464ae05
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.patterned_easy_difficulty.to_stream(data, game, default_override={'leash_radius': 100.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xcea\x83\xd8')  # 0xce6183d8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.rundas_properties_elite_difficulty.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'$\xd0\x06s')  # 0x24d00673
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.patterned_elite_difficulty.to_stream(data, game, default_override={'leash_radius': 100.0})
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

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("RundasJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            rundas_assets=RundasAssets.from_json(json_data['rundas_assets']),
            rundas_properties=RundasData.from_json(json_data['rundas_properties']),
            patterned=PatternedAITypedef.from_json(json_data['patterned']),
            rundas_properties_easy_difficulty=RundasData.from_json(json_data['rundas_properties_easy_difficulty']),
            patterned_easy_difficulty=PatternedAITypedef.from_json(json_data['patterned_easy_difficulty']),
            rundas_properties_elite_difficulty=RundasData.from_json(json_data['rundas_properties_elite_difficulty']),
            patterned_elite_difficulty=PatternedAITypedef.from_json(json_data['patterned_elite_difficulty']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'rundas_assets': self.rundas_assets.to_json(),
            'rundas_properties': self.rundas_properties.to_json(),
            'patterned': self.patterned.to_json(),
            'rundas_properties_easy_difficulty': self.rundas_properties_easy_difficulty.to_json(),
            'patterned_easy_difficulty': self.patterned_easy_difficulty.to_json(),
            'rundas_properties_elite_difficulty': self.rundas_properties_elite_difficulty.to_json(),
            'patterned_elite_difficulty': self.patterned_elite_difficulty.to_json(),
            'actor_information': self.actor_information.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.rundas_assets.dependencies_for, "rundas_assets", "RundasAssets"),
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.patterned_easy_difficulty.dependencies_for, "patterned_easy_difficulty", "PatternedAITypedef"),
            (self.patterned_elite_difficulty.dependencies_for, "patterned_elite_difficulty", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for Rundas.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_rundas_assets(data: typing.BinaryIO, game: Game, property_size: int) -> RundasAssets:
    return RundasAssets.from_stream(data, game, property_size)


def _decode_rundas_properties(data: typing.BinaryIO, game: Game, property_size: int) -> RundasData:
    return RundasData.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={'leash_radius': 100.0})


def _decode_rundas_properties_easy_difficulty(data: typing.BinaryIO, game: Game, property_size: int) -> RundasData:
    return RundasData.from_stream(data, game, property_size)


def _decode_patterned_easy_difficulty(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={'leash_radius': 100.0})


def _decode_rundas_properties_elite_difficulty(data: typing.BinaryIO, game: Game, property_size: int) -> RundasData:
    return RundasData.from_stream(data, game, property_size)


def _decode_patterned_elite_difficulty(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={'leash_radius': 100.0})


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xa6790709: ('rundas_assets', _decode_rundas_assets),
    0x9d90d49f: ('rundas_properties', _decode_rundas_properties),
    0xb3774750: ('patterned', _decode_patterned),
    0x877b2ce9: ('rundas_properties_easy_difficulty', _decode_rundas_properties_easy_difficulty),
    0x1464ae05: ('patterned_easy_difficulty', _decode_patterned_easy_difficulty),
    0xce6183d8: ('rundas_properties_elite_difficulty', _decode_rundas_properties_elite_difficulty),
    0x24d00673: ('patterned_elite_difficulty', _decode_patterned_elite_difficulty),
    0x7e397fed: ('actor_information', _decode_actor_information),
}
