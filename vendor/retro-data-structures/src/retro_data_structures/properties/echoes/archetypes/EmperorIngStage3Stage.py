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
from retro_data_structures.properties.echoes.archetypes.EmperorIngStage3Action import EmperorIngStage3Action

if typing.TYPE_CHECKING:
    class EmperorIngStage3StageJson(typing_extensions.TypedDict):
        min_health_percentage: float
        min_time_between_attacks: float
        max_time_between_attacks: float
        stampede: json_util.JsonObject
        jump_slide: json_util.JsonObject
        light_swarm: json_util.JsonObject
        dark_beam: json_util.JsonObject
        light_beam: json_util.JsonObject
        portal_attack: json_util.JsonObject
        dark_flier: json_util.JsonObject
        jump_attack: json_util.JsonObject
    

@dataclasses.dataclass()
class EmperorIngStage3Stage(BaseProperty):
    min_health_percentage: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdfea46b3, original_name='MinHealthPercentage'
        ),
    })
    min_time_between_attacks: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x95e7a2c2, original_name='MinTimeBetweenAttacks'
        ),
    })
    max_time_between_attacks: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x76ba1c18, original_name='MaxTimeBetweenAttacks'
        ),
    })
    stampede: EmperorIngStage3Action = dataclasses.field(default_factory=EmperorIngStage3Action, metadata={
        'reflection': FieldReflection[EmperorIngStage3Action](
            EmperorIngStage3Action, id=0x3826ec75, original_name='Stampede', from_json=EmperorIngStage3Action.from_json, to_json=EmperorIngStage3Action.to_json
        ),
    })
    jump_slide: EmperorIngStage3Action = dataclasses.field(default_factory=EmperorIngStage3Action, metadata={
        'reflection': FieldReflection[EmperorIngStage3Action](
            EmperorIngStage3Action, id=0x93bf1106, original_name='JumpSlide', from_json=EmperorIngStage3Action.from_json, to_json=EmperorIngStage3Action.to_json
        ),
    })
    light_swarm: EmperorIngStage3Action = dataclasses.field(default_factory=EmperorIngStage3Action, metadata={
        'reflection': FieldReflection[EmperorIngStage3Action](
            EmperorIngStage3Action, id=0xc4b88b80, original_name='LightSwarm', from_json=EmperorIngStage3Action.from_json, to_json=EmperorIngStage3Action.to_json
        ),
    })
    dark_beam: EmperorIngStage3Action = dataclasses.field(default_factory=EmperorIngStage3Action, metadata={
        'reflection': FieldReflection[EmperorIngStage3Action](
            EmperorIngStage3Action, id=0x32c6dc77, original_name='DarkBeam', from_json=EmperorIngStage3Action.from_json, to_json=EmperorIngStage3Action.to_json
        ),
    })
    light_beam: EmperorIngStage3Action = dataclasses.field(default_factory=EmperorIngStage3Action, metadata={
        'reflection': FieldReflection[EmperorIngStage3Action](
            EmperorIngStage3Action, id=0xc6e7b293, original_name='LightBeam', from_json=EmperorIngStage3Action.from_json, to_json=EmperorIngStage3Action.to_json
        ),
    })
    portal_attack: EmperorIngStage3Action = dataclasses.field(default_factory=EmperorIngStage3Action, metadata={
        'reflection': FieldReflection[EmperorIngStage3Action](
            EmperorIngStage3Action, id=0x20746b56, original_name='PortalAttack', from_json=EmperorIngStage3Action.from_json, to_json=EmperorIngStage3Action.to_json
        ),
    })
    dark_flier: EmperorIngStage3Action = dataclasses.field(default_factory=EmperorIngStage3Action, metadata={
        'reflection': FieldReflection[EmperorIngStage3Action](
            EmperorIngStage3Action, id=0x2ab44adb, original_name='DarkFlier', from_json=EmperorIngStage3Action.from_json, to_json=EmperorIngStage3Action.to_json
        ),
    })
    jump_attack: EmperorIngStage3Action = dataclasses.field(default_factory=EmperorIngStage3Action, metadata={
        'reflection': FieldReflection[EmperorIngStage3Action](
            EmperorIngStage3Action, id=0xe2e78a78, original_name='JumpAttack', from_json=EmperorIngStage3Action.from_json, to_json=EmperorIngStage3Action.to_json
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
        if property_count != 11:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdfea46b3
        min_health_percentage = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95e7a2c2
        min_time_between_attacks = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76ba1c18
        max_time_between_attacks = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3826ec75
        stampede = EmperorIngStage3Action.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x93bf1106
        jump_slide = EmperorIngStage3Action.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc4b88b80
        light_swarm = EmperorIngStage3Action.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32c6dc77
        dark_beam = EmperorIngStage3Action.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc6e7b293
        light_beam = EmperorIngStage3Action.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x20746b56
        portal_attack = EmperorIngStage3Action.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2ab44adb
        dark_flier = EmperorIngStage3Action.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe2e78a78
        jump_attack = EmperorIngStage3Action.from_stream(data, game, property_size)
    
        return cls(min_health_percentage, min_time_between_attacks, max_time_between_attacks, stampede, jump_slide, light_swarm, dark_beam, light_beam, portal_attack, dark_flier, jump_attack)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x0b')  # 11 properties

        data.write(b'\xdf\xeaF\xb3')  # 0xdfea46b3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_health_percentage))

        data.write(b'\x95\xe7\xa2\xc2')  # 0x95e7a2c2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_attacks))

        data.write(b'v\xba\x1c\x18')  # 0x76ba1c18
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_time_between_attacks))

        data.write(b'8&\xecu')  # 0x3826ec75
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stampede.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x93\xbf\x11\x06')  # 0x93bf1106
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.jump_slide.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc4\xb8\x8b\x80')  # 0xc4b88b80
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.light_swarm.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'2\xc6\xdcw')  # 0x32c6dc77
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.dark_beam.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc6\xe7\xb2\x93')  # 0xc6e7b293
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.light_beam.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b' tkV')  # 0x20746b56
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.portal_attack.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'*\xb4J\xdb')  # 0x2ab44adb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.dark_flier.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe2\xe7\x8ax')  # 0xe2e78a78
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.jump_attack.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("EmperorIngStage3StageJson", data)
        return cls(
            min_health_percentage=json_data['min_health_percentage'],
            min_time_between_attacks=json_data['min_time_between_attacks'],
            max_time_between_attacks=json_data['max_time_between_attacks'],
            stampede=EmperorIngStage3Action.from_json(json_data['stampede']),
            jump_slide=EmperorIngStage3Action.from_json(json_data['jump_slide']),
            light_swarm=EmperorIngStage3Action.from_json(json_data['light_swarm']),
            dark_beam=EmperorIngStage3Action.from_json(json_data['dark_beam']),
            light_beam=EmperorIngStage3Action.from_json(json_data['light_beam']),
            portal_attack=EmperorIngStage3Action.from_json(json_data['portal_attack']),
            dark_flier=EmperorIngStage3Action.from_json(json_data['dark_flier']),
            jump_attack=EmperorIngStage3Action.from_json(json_data['jump_attack']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'min_health_percentage': self.min_health_percentage,
            'min_time_between_attacks': self.min_time_between_attacks,
            'max_time_between_attacks': self.max_time_between_attacks,
            'stampede': self.stampede.to_json(),
            'jump_slide': self.jump_slide.to_json(),
            'light_swarm': self.light_swarm.to_json(),
            'dark_beam': self.dark_beam.to_json(),
            'light_beam': self.light_beam.to_json(),
            'portal_attack': self.portal_attack.to_json(),
            'dark_flier': self.dark_flier.to_json(),
            'jump_attack': self.jump_attack.to_json(),
        }


def _decode_stampede(data: typing.BinaryIO, game: Game, property_size: int) -> EmperorIngStage3Action:
    return EmperorIngStage3Action.from_stream(data, game, property_size)


def _decode_jump_slide(data: typing.BinaryIO, game: Game, property_size: int) -> EmperorIngStage3Action:
    return EmperorIngStage3Action.from_stream(data, game, property_size)


def _decode_light_swarm(data: typing.BinaryIO, game: Game, property_size: int) -> EmperorIngStage3Action:
    return EmperorIngStage3Action.from_stream(data, game, property_size)


def _decode_dark_beam(data: typing.BinaryIO, game: Game, property_size: int) -> EmperorIngStage3Action:
    return EmperorIngStage3Action.from_stream(data, game, property_size)


def _decode_light_beam(data: typing.BinaryIO, game: Game, property_size: int) -> EmperorIngStage3Action:
    return EmperorIngStage3Action.from_stream(data, game, property_size)


def _decode_portal_attack(data: typing.BinaryIO, game: Game, property_size: int) -> EmperorIngStage3Action:
    return EmperorIngStage3Action.from_stream(data, game, property_size)


def _decode_dark_flier(data: typing.BinaryIO, game: Game, property_size: int) -> EmperorIngStage3Action:
    return EmperorIngStage3Action.from_stream(data, game, property_size)


def _decode_jump_attack(data: typing.BinaryIO, game: Game, property_size: int) -> EmperorIngStage3Action:
    return EmperorIngStage3Action.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xdfea46b3: ('min_health_percentage', structs.decode_BIG_f),
    0x95e7a2c2: ('min_time_between_attacks', structs.decode_BIG_f),
    0x76ba1c18: ('max_time_between_attacks', structs.decode_BIG_f),
    0x3826ec75: ('stampede', _decode_stampede),
    0x93bf1106: ('jump_slide', _decode_jump_slide),
    0xc4b88b80: ('light_swarm', _decode_light_swarm),
    0x32c6dc77: ('dark_beam', _decode_dark_beam),
    0xc6e7b293: ('light_beam', _decode_light_beam),
    0x20746b56: ('portal_attack', _decode_portal_attack),
    0x2ab44adb: ('dark_flier', _decode_dark_flier),
    0xe2e78a78: ('jump_attack', _decode_jump_attack),
}
