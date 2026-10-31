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
from retro_data_structures.properties.corruption.archetypes.SeedBoss3Data import SeedBoss3Data
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SeedBoss3Json(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        seed_boss3_data: json_util.JsonObject
        seed_boss3_data_difficulty2: json_util.JsonObject
        seed_boss3_data_difficulty3: json_util.JsonObject
        patterned: json_util.JsonObject
        patterned_difficulty2: json_util.JsonObject
        patterned_difficulty3: json_util.JsonObject
        actor_information: json_util.JsonObject
    

@dataclasses.dataclass()
class SeedBoss3(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    seed_boss3_data: SeedBoss3Data = dataclasses.field(default_factory=SeedBoss3Data, metadata={
        'reflection': FieldReflection[SeedBoss3Data](
            SeedBoss3Data, id=0xfd27ed67, original_name='SeedBoss3Data', from_json=SeedBoss3Data.from_json, to_json=SeedBoss3Data.to_json
        ),
    })
    seed_boss3_data_difficulty2: SeedBoss3Data = dataclasses.field(default_factory=SeedBoss3Data, metadata={
        'reflection': FieldReflection[SeedBoss3Data](
            SeedBoss3Data, id=0x5292969e, original_name='SeedBoss3DataDifficulty2', from_json=SeedBoss3Data.from_json, to_json=SeedBoss3Data.to_json
        ),
    })
    seed_boss3_data_difficulty3: SeedBoss3Data = dataclasses.field(default_factory=SeedBoss3Data, metadata={
        'reflection': FieldReflection[SeedBoss3Data](
            SeedBoss3Data, id=0xcf9d77e8, original_name='SeedBoss3DataDifficulty3', from_json=SeedBoss3Data.from_json, to_json=SeedBoss3Data.to_json
        ),
    })
    patterned: PatternedAITypedef = dataclasses.field(default_factory=PatternedAITypedef, metadata={
        'reflection': FieldReflection[PatternedAITypedef](
            PatternedAITypedef, id=0xb3774750, original_name='Patterned', from_json=PatternedAITypedef.from_json, to_json=PatternedAITypedef.to_json
        ),
    })
    patterned_difficulty2: PatternedAITypedef = dataclasses.field(default_factory=PatternedAITypedef, metadata={
        'reflection': FieldReflection[PatternedAITypedef](
            PatternedAITypedef, id=0x5c056cef, original_name='PatternedDifficulty2', from_json=PatternedAITypedef.from_json, to_json=PatternedAITypedef.to_json
        ),
    })
    patterned_difficulty3: PatternedAITypedef = dataclasses.field(default_factory=PatternedAITypedef, metadata={
        'reflection': FieldReflection[PatternedAITypedef](
            PatternedAITypedef, id=0x8be7ecb7, original_name='PatternedDifficulty3', from_json=PatternedAITypedef.from_json, to_json=PatternedAITypedef.to_json
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
        return 'BOS3'

    @classmethod
    def modules(cls) -> list[str]:
        return ['RSO_SeedBoss3.rso']

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
        if property_count != 8:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfd27ed67
        seed_boss3_data = SeedBoss3Data.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5292969e
        seed_boss3_data_difficulty2 = SeedBoss3Data.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcf9d77e8
        seed_boss3_data_difficulty3 = SeedBoss3Data.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size, default_override={'mass': 1000.0, 'damage_wait_time': 0.009999999776482582, 'creature_size': 2, 'turn_speed': 90.0, 'disable_leg_ik': False, 'grapple_icon_offset': Vector(x=0.0, y=2.0, z=-0.5)})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5c056cef
        patterned_difficulty2 = PatternedAITypedef.from_stream(data, game, property_size, default_override={'mass': 1000.0, 'damage_wait_time': 0.009999999776482582, 'creature_size': 2, 'turn_speed': 90.0, 'disable_leg_ik': False, 'grapple_icon_offset': Vector(x=0.0, y=2.0, z=-0.5)})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8be7ecb7
        patterned_difficulty3 = PatternedAITypedef.from_stream(data, game, property_size, default_override={'mass': 1000.0, 'damage_wait_time': 0.009999999776482582, 'creature_size': 2, 'turn_speed': 90.0, 'disable_leg_ik': False, 'grapple_icon_offset': Vector(x=0.0, y=2.0, z=-0.5)})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        return cls(editor_properties, seed_boss3_data, seed_boss3_data_difficulty2, seed_boss3_data_difficulty3, patterned, patterned_difficulty2, patterned_difficulty3, actor_information)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x08')  # 8 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\xfd'\xedg")  # 0xfd27ed67
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.seed_boss3_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'R\x92\x96\x9e')  # 0x5292969e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.seed_boss3_data_difficulty2.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xcf\x9dw\xe8')  # 0xcf9d77e8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.seed_boss3_data_difficulty3.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb3wGP')  # 0xb3774750
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.patterned.to_stream(data, game, default_override={'mass': 1000.0, 'damage_wait_time': 0.009999999776482582, 'creature_size': 2, 'turn_speed': 90.0, 'disable_leg_ik': False, 'grapple_icon_offset': Vector(x=0.0, y=2.0, z=-0.5)})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\\\x05l\xef')  # 0x5c056cef
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.patterned_difficulty2.to_stream(data, game, default_override={'mass': 1000.0, 'damage_wait_time': 0.009999999776482582, 'creature_size': 2, 'turn_speed': 90.0, 'disable_leg_ik': False, 'grapple_icon_offset': Vector(x=0.0, y=2.0, z=-0.5)})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8b\xe7\xec\xb7')  # 0x8be7ecb7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.patterned_difficulty3.to_stream(data, game, default_override={'mass': 1000.0, 'damage_wait_time': 0.009999999776482582, 'creature_size': 2, 'turn_speed': 90.0, 'disable_leg_ik': False, 'grapple_icon_offset': Vector(x=0.0, y=2.0, z=-0.5)})
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
        json_data = typing.cast("SeedBoss3Json", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            seed_boss3_data=SeedBoss3Data.from_json(json_data['seed_boss3_data']),
            seed_boss3_data_difficulty2=SeedBoss3Data.from_json(json_data['seed_boss3_data_difficulty2']),
            seed_boss3_data_difficulty3=SeedBoss3Data.from_json(json_data['seed_boss3_data_difficulty3']),
            patterned=PatternedAITypedef.from_json(json_data['patterned']),
            patterned_difficulty2=PatternedAITypedef.from_json(json_data['patterned_difficulty2']),
            patterned_difficulty3=PatternedAITypedef.from_json(json_data['patterned_difficulty3']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'seed_boss3_data': self.seed_boss3_data.to_json(),
            'seed_boss3_data_difficulty2': self.seed_boss3_data_difficulty2.to_json(),
            'seed_boss3_data_difficulty3': self.seed_boss3_data_difficulty3.to_json(),
            'patterned': self.patterned.to_json(),
            'patterned_difficulty2': self.patterned_difficulty2.to_json(),
            'patterned_difficulty3': self.patterned_difficulty3.to_json(),
            'actor_information': self.actor_information.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.seed_boss3_data.dependencies_for, "seed_boss3_data", "SeedBoss3Data"),
            (self.seed_boss3_data_difficulty2.dependencies_for, "seed_boss3_data_difficulty2", "SeedBoss3Data"),
            (self.seed_boss3_data_difficulty3.dependencies_for, "seed_boss3_data_difficulty3", "SeedBoss3Data"),
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.patterned_difficulty2.dependencies_for, "patterned_difficulty2", "PatternedAITypedef"),
            (self.patterned_difficulty3.dependencies_for, "patterned_difficulty3", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for SeedBoss3.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_seed_boss3_data(data: typing.BinaryIO, game: Game, property_size: int) -> SeedBoss3Data:
    return SeedBoss3Data.from_stream(data, game, property_size)


def _decode_seed_boss3_data_difficulty2(data: typing.BinaryIO, game: Game, property_size: int) -> SeedBoss3Data:
    return SeedBoss3Data.from_stream(data, game, property_size)


def _decode_seed_boss3_data_difficulty3(data: typing.BinaryIO, game: Game, property_size: int) -> SeedBoss3Data:
    return SeedBoss3Data.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={'mass': 1000.0, 'damage_wait_time': 0.009999999776482582, 'creature_size': 2, 'turn_speed': 90.0, 'disable_leg_ik': False, 'grapple_icon_offset': Vector(x=0.0, y=2.0, z=-0.5)})


def _decode_patterned_difficulty2(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={'mass': 1000.0, 'damage_wait_time': 0.009999999776482582, 'creature_size': 2, 'turn_speed': 90.0, 'disable_leg_ik': False, 'grapple_icon_offset': Vector(x=0.0, y=2.0, z=-0.5)})


def _decode_patterned_difficulty3(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={'mass': 1000.0, 'damage_wait_time': 0.009999999776482582, 'creature_size': 2, 'turn_speed': 90.0, 'disable_leg_ik': False, 'grapple_icon_offset': Vector(x=0.0, y=2.0, z=-0.5)})


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xfd27ed67: ('seed_boss3_data', _decode_seed_boss3_data),
    0x5292969e: ('seed_boss3_data_difficulty2', _decode_seed_boss3_data_difficulty2),
    0xcf9d77e8: ('seed_boss3_data_difficulty3', _decode_seed_boss3_data_difficulty3),
    0xb3774750: ('patterned', _decode_patterned),
    0x5c056cef: ('patterned_difficulty2', _decode_patterned_difficulty2),
    0x8be7ecb7: ('patterned_difficulty3', _decode_patterned_difficulty3),
    0x7e397fed: ('actor_information', _decode_actor_information),
}
