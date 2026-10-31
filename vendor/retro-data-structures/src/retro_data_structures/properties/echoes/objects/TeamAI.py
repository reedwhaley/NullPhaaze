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

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class TeamAIJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        max_team_size: int
        max_melee_attackers: int
        max_ranged_attackers: int
        max_hecklers: int
        max_simultaneous_melee_attacks: int
        max_simultaneous_ranged_attacks: int
        team_formation: int
        min_time_between_melee_attacks: float
        min_time_between_ranged_attacks: float
    

@dataclasses.dataclass()
class TeamAI(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    max_team_size: int = dataclasses.field(default=20, metadata={
        'reflection': FieldReflection[int](
            int, id=0xbf37e518, original_name='MaxTeamSize'
        ),
    })
    max_melee_attackers: int = dataclasses.field(default=2, metadata={
        'reflection': FieldReflection[int](
            int, id=0xcebee4ab, original_name='MaxMeleeAttackers'
        ),
    })
    max_ranged_attackers: int = dataclasses.field(default=2, metadata={
        'reflection': FieldReflection[int](
            int, id=0x7555c1ea, original_name='MaxRangedAttackers'
        ),
    })
    max_hecklers: int = dataclasses.field(default=30, metadata={
        'reflection': FieldReflection[int](
            int, id=0x9fa9c457, original_name='MaxHecklers'
        ),
    })
    max_simultaneous_melee_attacks: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x54cd2755, original_name='MaxSimultaneousMeleeAttacks'
        ),
    })
    max_simultaneous_ranged_attacks: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0xc36ed15c, original_name='MaxSimultaneousRangedAttacks'
        ),
    })
    team_formation: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x37a20376, original_name='TeamFormation'
        ),
    })  # Choice
    min_time_between_melee_attacks: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd3ad55b6, original_name='MinTimeBetweenMeleeAttacks'
        ),
    })
    min_time_between_ranged_attacks: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8d00b839, original_name='MinTimeBetweenRangedAttacks'
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'TMAI'

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
        if property_count != 10:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbf37e518
        max_team_size = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcebee4ab
        max_melee_attackers = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7555c1ea
        max_ranged_attackers = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9fa9c457
        max_hecklers = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x54cd2755
        max_simultaneous_melee_attacks = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc36ed15c
        max_simultaneous_ranged_attacks = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x37a20376
        team_formation = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd3ad55b6
        min_time_between_melee_attacks = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8d00b839
        min_time_between_ranged_attacks = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(editor_properties, max_team_size, max_melee_attackers, max_ranged_attackers, max_hecklers, max_simultaneous_melee_attacks, max_simultaneous_ranged_attacks, team_formation, min_time_between_melee_attacks, min_time_between_ranged_attacks)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\n')  # 10 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbf7\xe5\x18')  # 0xbf37e518
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_team_size))

        data.write(b'\xce\xbe\xe4\xab')  # 0xcebee4ab
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_melee_attackers))

        data.write(b'uU\xc1\xea')  # 0x7555c1ea
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_ranged_attackers))

        data.write(b'\x9f\xa9\xc4W')  # 0x9fa9c457
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_hecklers))

        data.write(b"T\xcd'U")  # 0x54cd2755
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_simultaneous_melee_attacks))

        data.write(b'\xc3n\xd1\\')  # 0xc36ed15c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_simultaneous_ranged_attacks))

        data.write(b'7\xa2\x03v')  # 0x37a20376
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.team_formation))

        data.write(b'\xd3\xadU\xb6')  # 0xd3ad55b6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_melee_attacks))

        data.write(b'\x8d\x00\xb89')  # 0x8d00b839
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_ranged_attacks))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TeamAIJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            max_team_size=json_data['max_team_size'],
            max_melee_attackers=json_data['max_melee_attackers'],
            max_ranged_attackers=json_data['max_ranged_attackers'],
            max_hecklers=json_data['max_hecklers'],
            max_simultaneous_melee_attacks=json_data['max_simultaneous_melee_attacks'],
            max_simultaneous_ranged_attacks=json_data['max_simultaneous_ranged_attacks'],
            team_formation=json_data['team_formation'],
            min_time_between_melee_attacks=json_data['min_time_between_melee_attacks'],
            min_time_between_ranged_attacks=json_data['min_time_between_ranged_attacks'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'max_team_size': self.max_team_size,
            'max_melee_attackers': self.max_melee_attackers,
            'max_ranged_attackers': self.max_ranged_attackers,
            'max_hecklers': self.max_hecklers,
            'max_simultaneous_melee_attacks': self.max_simultaneous_melee_attacks,
            'max_simultaneous_ranged_attacks': self.max_simultaneous_ranged_attacks,
            'team_formation': self.team_formation,
            'min_time_between_melee_attacks': self.min_time_between_melee_attacks,
            'min_time_between_ranged_attacks': self.min_time_between_ranged_attacks,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xbf37e518: ('max_team_size', structs.decode_BIG_l),
    0xcebee4ab: ('max_melee_attackers', structs.decode_BIG_l),
    0x7555c1ea: ('max_ranged_attackers', structs.decode_BIG_l),
    0x9fa9c457: ('max_hecklers', structs.decode_BIG_l),
    0x54cd2755: ('max_simultaneous_melee_attacks', structs.decode_BIG_l),
    0xc36ed15c: ('max_simultaneous_ranged_attacks', structs.decode_BIG_l),
    0x37a20376: ('team_formation', structs.decode_BIG_L),
    0xd3ad55b6: ('min_time_between_melee_attacks', structs.decode_BIG_f),
    0x8d00b839: ('min_time_between_ranged_attacks', structs.decode_BIG_f),
}
