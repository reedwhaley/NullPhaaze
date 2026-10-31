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

if typing.TYPE_CHECKING:
    class PillBugDataJson(typing_extensions.TypedDict):
        planar_constraint: int
        squirm_vulnerability: json_util.JsonObject
        wander_vulnerability: json_util.JsonObject
        crawl_radius: float
        roll_radius: float
        collision_look_ahead_time: float
        forward_priority: float
        unknown: float
    

@dataclasses.dataclass()
class PillBugData(BaseProperty):
    planar_constraint: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xde7e9f94, original_name='PlanarConstraint'
        ),
    })  # Choice
    squirm_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x5d84ed71, original_name='SquirmVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    wander_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xf382dff7, original_name='WanderVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    crawl_radius: float = dataclasses.field(default=0.3499999940395355, metadata={
        'reflection': FieldReflection[float](
            float, id=0xad98e16d, original_name='CrawlRadius'
        ),
    })
    roll_radius: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x81d699b0, original_name='RollRadius'
        ),
    })
    collision_look_ahead_time: float = dataclasses.field(default=0.019999999552965164, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa265383c, original_name='CollisionLookAheadTime'
        ),
    })
    forward_priority: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0xad08e189, original_name='ForwardPriority'
        ),
    })
    unknown: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2f798cdd, original_name='Unknown'
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
        if property_count != 8:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xde7e9f94
        planar_constraint = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5d84ed71
        squirm_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf382dff7
        wander_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xad98e16d
        crawl_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x81d699b0
        roll_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa265383c
        collision_look_ahead_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xad08e189
        forward_priority = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2f798cdd
        unknown = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(planar_constraint, squirm_vulnerability, wander_vulnerability, crawl_radius, roll_radius, collision_look_ahead_time, forward_priority, unknown)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x08')  # 8 properties

        data.write(b'\xde~\x9f\x94')  # 0xde7e9f94
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.planar_constraint))

        data.write(b']\x84\xedq')  # 0x5d84ed71
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.squirm_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf3\x82\xdf\xf7')  # 0xf382dff7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.wander_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xad\x98\xe1m')  # 0xad98e16d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.crawl_radius))

        data.write(b'\x81\xd6\x99\xb0')  # 0x81d699b0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.roll_radius))

        data.write(b'\xa2e8<')  # 0xa265383c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.collision_look_ahead_time))

        data.write(b'\xad\x08\xe1\x89')  # 0xad08e189
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.forward_priority))

        data.write(b'/y\x8c\xdd')  # 0x2f798cdd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PillBugDataJson", data)
        return cls(
            planar_constraint=json_data['planar_constraint'],
            squirm_vulnerability=DamageVulnerability.from_json(json_data['squirm_vulnerability']),
            wander_vulnerability=DamageVulnerability.from_json(json_data['wander_vulnerability']),
            crawl_radius=json_data['crawl_radius'],
            roll_radius=json_data['roll_radius'],
            collision_look_ahead_time=json_data['collision_look_ahead_time'],
            forward_priority=json_data['forward_priority'],
            unknown=json_data['unknown'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'planar_constraint': self.planar_constraint,
            'squirm_vulnerability': self.squirm_vulnerability.to_json(),
            'wander_vulnerability': self.wander_vulnerability.to_json(),
            'crawl_radius': self.crawl_radius,
            'roll_radius': self.roll_radius,
            'collision_look_ahead_time': self.collision_look_ahead_time,
            'forward_priority': self.forward_priority,
            'unknown': self.unknown,
        }


def _decode_squirm_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_wander_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xde7e9f94: ('planar_constraint', structs.decode_BIG_L),
    0x5d84ed71: ('squirm_vulnerability', _decode_squirm_vulnerability),
    0xf382dff7: ('wander_vulnerability', _decode_wander_vulnerability),
    0xad98e16d: ('crawl_radius', structs.decode_BIG_f),
    0x81d699b0: ('roll_radius', structs.decode_BIG_f),
    0xa265383c: ('collision_look_ahead_time', structs.decode_BIG_f),
    0xad08e189: ('forward_priority', structs.decode_BIG_f),
    0x2f798cdd: ('unknown', structs.decode_BIG_f),
}
