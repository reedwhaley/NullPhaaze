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
from retro_data_structures.properties.corruption.archetypes.WorldTransitionChoiceRelaySelection import WorldTransitionChoiceRelaySelection

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class WorldTransitionChoiceRelayJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        num_choices: int
        choice1: json_util.JsonObject
        choice2: json_util.JsonObject
        choice3: json_util.JsonObject
        choice4: json_util.JsonObject
        choice5: json_util.JsonObject
        choice6: json_util.JsonObject
        choice7: json_util.JsonObject
        choice8: json_util.JsonObject
        choice9: json_util.JsonObject
        choice10: json_util.JsonObject
    

@dataclasses.dataclass()
class WorldTransitionChoiceRelay(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    num_choices: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x58b2a49b, original_name='NumChoices'
        ),
    })
    choice1: WorldTransitionChoiceRelaySelection = dataclasses.field(default_factory=WorldTransitionChoiceRelaySelection, metadata={
        'reflection': FieldReflection[WorldTransitionChoiceRelaySelection](
            WorldTransitionChoiceRelaySelection, id=0x0f5765c9, original_name='Choice1', from_json=WorldTransitionChoiceRelaySelection.from_json, to_json=WorldTransitionChoiceRelaySelection.to_json
        ),
    })
    choice2: WorldTransitionChoiceRelaySelection = dataclasses.field(default_factory=WorldTransitionChoiceRelaySelection, metadata={
        'reflection': FieldReflection[WorldTransitionChoiceRelaySelection](
            WorldTransitionChoiceRelaySelection, id=0x6bb71e37, original_name='Choice2', from_json=WorldTransitionChoiceRelaySelection.from_json, to_json=WorldTransitionChoiceRelaySelection.to_json
        ),
    })
    choice3: WorldTransitionChoiceRelaySelection = dataclasses.field(default_factory=WorldTransitionChoiceRelaySelection, metadata={
        'reflection': FieldReflection[WorldTransitionChoiceRelaySelection](
            WorldTransitionChoiceRelaySelection, id=0xfec7caa2, original_name='Choice3', from_json=WorldTransitionChoiceRelaySelection.from_json, to_json=WorldTransitionChoiceRelaySelection.to_json
        ),
    })
    choice4: WorldTransitionChoiceRelaySelection = dataclasses.field(default_factory=WorldTransitionChoiceRelaySelection, metadata={
        'reflection': FieldReflection[WorldTransitionChoiceRelaySelection](
            WorldTransitionChoiceRelaySelection, id=0xa277e9cb, original_name='Choice4', from_json=WorldTransitionChoiceRelaySelection.from_json, to_json=WorldTransitionChoiceRelaySelection.to_json
        ),
    })
    choice5: WorldTransitionChoiceRelaySelection = dataclasses.field(default_factory=WorldTransitionChoiceRelaySelection, metadata={
        'reflection': FieldReflection[WorldTransitionChoiceRelaySelection](
            WorldTransitionChoiceRelaySelection, id=0x37073d5e, original_name='Choice5', from_json=WorldTransitionChoiceRelaySelection.from_json, to_json=WorldTransitionChoiceRelaySelection.to_json
        ),
    })
    choice6: WorldTransitionChoiceRelaySelection = dataclasses.field(default_factory=WorldTransitionChoiceRelaySelection, metadata={
        'reflection': FieldReflection[WorldTransitionChoiceRelaySelection](
            WorldTransitionChoiceRelaySelection, id=0x53e746a0, original_name='Choice6', from_json=WorldTransitionChoiceRelaySelection.from_json, to_json=WorldTransitionChoiceRelaySelection.to_json
        ),
    })
    choice7: WorldTransitionChoiceRelaySelection = dataclasses.field(default_factory=WorldTransitionChoiceRelaySelection, metadata={
        'reflection': FieldReflection[WorldTransitionChoiceRelaySelection](
            WorldTransitionChoiceRelaySelection, id=0xc6979235, original_name='Choice7', from_json=WorldTransitionChoiceRelaySelection.from_json, to_json=WorldTransitionChoiceRelaySelection.to_json
        ),
    })
    choice8: WorldTransitionChoiceRelaySelection = dataclasses.field(default_factory=WorldTransitionChoiceRelaySelection, metadata={
        'reflection': FieldReflection[WorldTransitionChoiceRelaySelection](
            WorldTransitionChoiceRelaySelection, id=0xea870072, original_name='Choice8', from_json=WorldTransitionChoiceRelaySelection.from_json, to_json=WorldTransitionChoiceRelaySelection.to_json
        ),
    })
    choice9: WorldTransitionChoiceRelaySelection = dataclasses.field(default_factory=WorldTransitionChoiceRelaySelection, metadata={
        'reflection': FieldReflection[WorldTransitionChoiceRelaySelection](
            WorldTransitionChoiceRelaySelection, id=0x7ff7d4e7, original_name='Choice9', from_json=WorldTransitionChoiceRelaySelection.from_json, to_json=WorldTransitionChoiceRelaySelection.to_json
        ),
    })
    choice10: WorldTransitionChoiceRelaySelection = dataclasses.field(default_factory=WorldTransitionChoiceRelaySelection, metadata={
        'reflection': FieldReflection[WorldTransitionChoiceRelaySelection](
            WorldTransitionChoiceRelaySelection, id=0x7db5008c, original_name='Choice10', from_json=WorldTransitionChoiceRelaySelection.from_json, to_json=WorldTransitionChoiceRelaySelection.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'WTCR'

    @classmethod
    def modules(cls) -> list[str]:
        return ['RSO_ScriptWorldTeleporter.rso']

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
        if property_count != 12:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58b2a49b
        num_choices = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0f5765c9
        choice1 = WorldTransitionChoiceRelaySelection.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6bb71e37
        choice2 = WorldTransitionChoiceRelaySelection.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfec7caa2
        choice3 = WorldTransitionChoiceRelaySelection.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa277e9cb
        choice4 = WorldTransitionChoiceRelaySelection.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x37073d5e
        choice5 = WorldTransitionChoiceRelaySelection.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x53e746a0
        choice6 = WorldTransitionChoiceRelaySelection.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc6979235
        choice7 = WorldTransitionChoiceRelaySelection.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xea870072
        choice8 = WorldTransitionChoiceRelaySelection.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7ff7d4e7
        choice9 = WorldTransitionChoiceRelaySelection.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7db5008c
        choice10 = WorldTransitionChoiceRelaySelection.from_stream(data, game, property_size)
    
        return cls(editor_properties, num_choices, choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8, choice9, choice10)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x03')  # 3 properties
        num_properties_written = 3

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'X\xb2\xa4\x9b')  # 0x58b2a49b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.num_choices))

        data.write(b'\x0fWe\xc9')  # 0xf5765c9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.choice1.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        if self.choice2 != default_override.get('choice2', WorldTransitionChoiceRelaySelection()):
            num_properties_written += 1
            data.write(b'k\xb7\x1e7')  # 0x6bb71e37
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            self.choice2.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self.choice3 != default_override.get('choice3', WorldTransitionChoiceRelaySelection()):
            num_properties_written += 1
            data.write(b'\xfe\xc7\xca\xa2')  # 0xfec7caa2
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            self.choice3.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self.choice4 != default_override.get('choice4', WorldTransitionChoiceRelaySelection()):
            num_properties_written += 1
            data.write(b'\xa2w\xe9\xcb')  # 0xa277e9cb
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            self.choice4.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self.choice5 != default_override.get('choice5', WorldTransitionChoiceRelaySelection()):
            num_properties_written += 1
            data.write(b'7\x07=^')  # 0x37073d5e
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            self.choice5.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self.choice6 != default_override.get('choice6', WorldTransitionChoiceRelaySelection()):
            num_properties_written += 1
            data.write(b'S\xe7F\xa0')  # 0x53e746a0
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            self.choice6.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self.choice7 != default_override.get('choice7', WorldTransitionChoiceRelaySelection()):
            num_properties_written += 1
            data.write(b'\xc6\x97\x925')  # 0xc6979235
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            self.choice7.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self.choice8 != default_override.get('choice8', WorldTransitionChoiceRelaySelection()):
            num_properties_written += 1
            data.write(b'\xea\x87\x00r')  # 0xea870072
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            self.choice8.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self.choice9 != default_override.get('choice9', WorldTransitionChoiceRelaySelection()):
            num_properties_written += 1
            data.write(b'\x7f\xf7\xd4\xe7')  # 0x7ff7d4e7
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            self.choice9.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self.choice10 != default_override.get('choice10', WorldTransitionChoiceRelaySelection()):
            num_properties_written += 1
            data.write(b'}\xb5\x00\x8c')  # 0x7db5008c
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            self.choice10.to_stream(data, game)
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
        json_data = typing.cast("WorldTransitionChoiceRelayJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            num_choices=json_data['num_choices'],
            choice1=WorldTransitionChoiceRelaySelection.from_json(json_data['choice1']),
            choice2=WorldTransitionChoiceRelaySelection.from_json(json_data['choice2']),
            choice3=WorldTransitionChoiceRelaySelection.from_json(json_data['choice3']),
            choice4=WorldTransitionChoiceRelaySelection.from_json(json_data['choice4']),
            choice5=WorldTransitionChoiceRelaySelection.from_json(json_data['choice5']),
            choice6=WorldTransitionChoiceRelaySelection.from_json(json_data['choice6']),
            choice7=WorldTransitionChoiceRelaySelection.from_json(json_data['choice7']),
            choice8=WorldTransitionChoiceRelaySelection.from_json(json_data['choice8']),
            choice9=WorldTransitionChoiceRelaySelection.from_json(json_data['choice9']),
            choice10=WorldTransitionChoiceRelaySelection.from_json(json_data['choice10']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'num_choices': self.num_choices,
            'choice1': self.choice1.to_json(),
            'choice2': self.choice2.to_json(),
            'choice3': self.choice3.to_json(),
            'choice4': self.choice4.to_json(),
            'choice5': self.choice5.to_json(),
            'choice6': self.choice6.to_json(),
            'choice7': self.choice7.to_json(),
            'choice8': self.choice8.to_json(),
            'choice9': self.choice9.to_json(),
            'choice10': self.choice10.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_choice1(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTransitionChoiceRelaySelection:
    return WorldTransitionChoiceRelaySelection.from_stream(data, game, property_size)


def _decode_choice2(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTransitionChoiceRelaySelection:
    return WorldTransitionChoiceRelaySelection.from_stream(data, game, property_size)


def _decode_choice3(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTransitionChoiceRelaySelection:
    return WorldTransitionChoiceRelaySelection.from_stream(data, game, property_size)


def _decode_choice4(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTransitionChoiceRelaySelection:
    return WorldTransitionChoiceRelaySelection.from_stream(data, game, property_size)


def _decode_choice5(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTransitionChoiceRelaySelection:
    return WorldTransitionChoiceRelaySelection.from_stream(data, game, property_size)


def _decode_choice6(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTransitionChoiceRelaySelection:
    return WorldTransitionChoiceRelaySelection.from_stream(data, game, property_size)


def _decode_choice7(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTransitionChoiceRelaySelection:
    return WorldTransitionChoiceRelaySelection.from_stream(data, game, property_size)


def _decode_choice8(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTransitionChoiceRelaySelection:
    return WorldTransitionChoiceRelaySelection.from_stream(data, game, property_size)


def _decode_choice9(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTransitionChoiceRelaySelection:
    return WorldTransitionChoiceRelaySelection.from_stream(data, game, property_size)


def _decode_choice10(data: typing.BinaryIO, game: Game, property_size: int) -> WorldTransitionChoiceRelaySelection:
    return WorldTransitionChoiceRelaySelection.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0x58b2a49b: ('num_choices', structs.decode_BIG_l),
    0x0f5765c9: ('choice1', _decode_choice1),
    0x6bb71e37: ('choice2', _decode_choice2),
    0xfec7caa2: ('choice3', _decode_choice3),
    0xa277e9cb: ('choice4', _decode_choice4),
    0x37073d5e: ('choice5', _decode_choice5),
    0x53e746a0: ('choice6', _decode_choice6),
    0xc6979235: ('choice7', _decode_choice7),
    0xea870072: ('choice8', _decode_choice8),
    0x7ff7d4e7: ('choice9', _decode_choice9),
    0x7db5008c: ('choice10', _decode_choice10),
}
