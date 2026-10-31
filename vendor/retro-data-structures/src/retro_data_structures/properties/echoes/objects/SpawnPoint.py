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
from retro_data_structures.properties.echoes.archetypes.PlayerInventory import PlayerInventory

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SpawnPointJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        first_spawn: bool
        spawn_in_morph_ball_mode: bool
        spawn_inventory: json_util.JsonObject
        spawn_inventory_capacity: json_util.JsonObject
    

@dataclasses.dataclass()
class SpawnPoint(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    first_spawn: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xc0e4521b, original_name='FirstSpawn'
        ),
    })
    spawn_in_morph_ball_mode: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xb9c40f92, original_name='SpawnInMorphBallMode'
        ),
    })
    spawn_inventory: PlayerInventory = dataclasses.field(default_factory=PlayerInventory, metadata={
        'reflection': FieldReflection[PlayerInventory](
            PlayerInventory, id=0x4c1d4cc9, original_name='SpawnInventory', from_json=PlayerInventory.from_json, to_json=PlayerInventory.to_json
        ),
    })
    spawn_inventory_capacity: PlayerInventory = dataclasses.field(default_factory=PlayerInventory, metadata={
        'reflection': FieldReflection[PlayerInventory](
            PlayerInventory, id=0x4081bf95, original_name='SpawnInventoryCapacity', from_json=PlayerInventory.from_json, to_json=PlayerInventory.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'SPWN'

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
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc0e4521b
        first_spawn = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb9c40f92
        spawn_in_morph_ball_mode = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4c1d4cc9
        spawn_inventory = PlayerInventory.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4081bf95
        spawn_inventory_capacity = PlayerInventory.from_stream(data, game, property_size)
    
        return cls(editor_properties, first_spawn, spawn_in_morph_ball_mode, spawn_inventory, spawn_inventory_capacity)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x05')  # 5 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc0\xe4R\x1b')  # 0xc0e4521b
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.first_spawn))

        data.write(b'\xb9\xc4\x0f\x92')  # 0xb9c40f92
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.spawn_in_morph_ball_mode))

        data.write(b'L\x1dL\xc9')  # 0x4c1d4cc9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.spawn_inventory.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'@\x81\xbf\x95')  # 0x4081bf95
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.spawn_inventory_capacity.to_stream(data, game)
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
        json_data = typing.cast("SpawnPointJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            first_spawn=json_data['first_spawn'],
            spawn_in_morph_ball_mode=json_data['spawn_in_morph_ball_mode'],
            spawn_inventory=PlayerInventory.from_json(json_data['spawn_inventory']),
            spawn_inventory_capacity=PlayerInventory.from_json(json_data['spawn_inventory_capacity']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'first_spawn': self.first_spawn,
            'spawn_in_morph_ball_mode': self.spawn_in_morph_ball_mode,
            'spawn_inventory': self.spawn_inventory.to_json(),
            'spawn_inventory_capacity': self.spawn_inventory_capacity.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_spawn_inventory(data: typing.BinaryIO, game: Game, property_size: int) -> PlayerInventory:
    return PlayerInventory.from_stream(data, game, property_size)


def _decode_spawn_inventory_capacity(data: typing.BinaryIO, game: Game, property_size: int) -> PlayerInventory:
    return PlayerInventory.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xc0e4521b: ('first_spawn', structs.decode_BIG_bool_),
    0xb9c40f92: ('spawn_in_morph_ball_mode', structs.decode_BIG_bool_),
    0x4c1d4cc9: ('spawn_inventory', _decode_spawn_inventory),
    0x4081bf95: ('spawn_inventory_capacity', _decode_spawn_inventory_capacity),
}
