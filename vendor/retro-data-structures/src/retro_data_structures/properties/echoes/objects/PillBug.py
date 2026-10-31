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
from retro_data_structures.properties.echoes.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class PillBugJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        planar_constraint: int
        floor_turn_speed: float
        stick_radius: float
        waypoint_approach_distance: float
        visible_distance: float
        squirm_vulnerability: json_util.JsonObject
        wander_vulnerability: json_util.JsonObject
        crawl_radius: float
        roll_radius: float
        floor_snap_lerp_factor: float
        collision_look_ahead_time: float
        forward_priority: float
        down_additive_time_into: float
        down_additive_time_outof: float
        up_additive_time_into: float
        up_additive_time_outof: float
    

@dataclasses.dataclass()
class PillBug(BaseObjectType):
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
    planar_constraint: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xde7e9f94, original_name='PlanarConstraint'
        ),
    })  # Choice
    floor_turn_speed: float = dataclasses.field(default=120.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8e4f7b29, original_name='FloorTurnSpeed'
        ),
    })
    stick_radius: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5a3a30f4, original_name='StickRadius'
        ),
    })
    waypoint_approach_distance: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x733bd27c, original_name='WaypointApproachDistance'
        ),
    })
    visible_distance: float = dataclasses.field(default=200.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa72530e8, original_name='VisibleDistance'
        ),
    })
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
    floor_snap_lerp_factor: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x519c7197, original_name='FloorSnapLerpFactor'
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
    down_additive_time_into: float = dataclasses.field(default=0.6000000238418579, metadata={
        'reflection': FieldReflection[float](
            float, id=0x558c0692, original_name='DownAdditiveTimeInto'
        ),
    })
    down_additive_time_outof: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0f991bf1, original_name='DownAdditiveTimeOutof'
        ),
    })
    up_additive_time_into: float = dataclasses.field(default=0.6000000238418579, metadata={
        'reflection': FieldReflection[float](
            float, id=0x385a1bed, original_name='UpAdditiveTimeInto'
        ),
    })
    up_additive_time_outof: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcf4ea141, original_name='UpAdditiveTimeOutof'
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'PILB'

    @classmethod
    def modules(cls) -> list[str]:
        return ['WallCrawler.rel', 'PillBug.rel']

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
        if property_count != 19:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xde7e9f94
        planar_constraint = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8e4f7b29
        floor_turn_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5a3a30f4
        stick_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x733bd27c
        waypoint_approach_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa72530e8
        visible_distance = structs.BIG_f.unpack(data.read(4))[0]
    
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
        assert property_id == 0x519c7197
        floor_snap_lerp_factor = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa265383c
        collision_look_ahead_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xad08e189
        forward_priority = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x558c0692
        down_additive_time_into = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0f991bf1
        down_additive_time_outof = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x385a1bed
        up_additive_time_into = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcf4ea141
        up_additive_time_outof = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(editor_properties, patterned, actor_information, planar_constraint, floor_turn_speed, stick_radius, waypoint_approach_distance, visible_distance, squirm_vulnerability, wander_vulnerability, crawl_radius, roll_radius, floor_snap_lerp_factor, collision_look_ahead_time, forward_priority, down_additive_time_into, down_additive_time_outof, up_additive_time_into, up_additive_time_outof)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x13')  # 19 properties

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
        self.patterned.to_stream(data, game)
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

        data.write(b'\xde~\x9f\x94')  # 0xde7e9f94
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.planar_constraint))

        data.write(b'\x8eO{)')  # 0x8e4f7b29
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.floor_turn_speed))

        data.write(b'Z:0\xf4')  # 0x5a3a30f4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stick_radius))

        data.write(b's;\xd2|')  # 0x733bd27c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.waypoint_approach_distance))

        data.write(b'\xa7%0\xe8')  # 0xa72530e8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.visible_distance))

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

        data.write(b'Q\x9cq\x97')  # 0x519c7197
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.floor_snap_lerp_factor))

        data.write(b'\xa2e8<')  # 0xa265383c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.collision_look_ahead_time))

        data.write(b'\xad\x08\xe1\x89')  # 0xad08e189
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.forward_priority))

        data.write(b'U\x8c\x06\x92')  # 0x558c0692
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.down_additive_time_into))

        data.write(b'\x0f\x99\x1b\xf1')  # 0xf991bf1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.down_additive_time_outof))

        data.write(b'8Z\x1b\xed')  # 0x385a1bed
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.up_additive_time_into))

        data.write(b'\xcfN\xa1A')  # 0xcf4ea141
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.up_additive_time_outof))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PillBugJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            patterned=PatternedAITypedef.from_json(json_data['patterned']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
            planar_constraint=json_data['planar_constraint'],
            floor_turn_speed=json_data['floor_turn_speed'],
            stick_radius=json_data['stick_radius'],
            waypoint_approach_distance=json_data['waypoint_approach_distance'],
            visible_distance=json_data['visible_distance'],
            squirm_vulnerability=DamageVulnerability.from_json(json_data['squirm_vulnerability']),
            wander_vulnerability=DamageVulnerability.from_json(json_data['wander_vulnerability']),
            crawl_radius=json_data['crawl_radius'],
            roll_radius=json_data['roll_radius'],
            floor_snap_lerp_factor=json_data['floor_snap_lerp_factor'],
            collision_look_ahead_time=json_data['collision_look_ahead_time'],
            forward_priority=json_data['forward_priority'],
            down_additive_time_into=json_data['down_additive_time_into'],
            down_additive_time_outof=json_data['down_additive_time_outof'],
            up_additive_time_into=json_data['up_additive_time_into'],
            up_additive_time_outof=json_data['up_additive_time_outof'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'patterned': self.patterned.to_json(),
            'actor_information': self.actor_information.to_json(),
            'planar_constraint': self.planar_constraint,
            'floor_turn_speed': self.floor_turn_speed,
            'stick_radius': self.stick_radius,
            'waypoint_approach_distance': self.waypoint_approach_distance,
            'visible_distance': self.visible_distance,
            'squirm_vulnerability': self.squirm_vulnerability.to_json(),
            'wander_vulnerability': self.wander_vulnerability.to_json(),
            'crawl_radius': self.crawl_radius,
            'roll_radius': self.roll_radius,
            'floor_snap_lerp_factor': self.floor_snap_lerp_factor,
            'collision_look_ahead_time': self.collision_look_ahead_time,
            'forward_priority': self.forward_priority,
            'down_additive_time_into': self.down_additive_time_into,
            'down_additive_time_outof': self.down_additive_time_outof,
            'up_additive_time_into': self.up_additive_time_into,
            'up_additive_time_outof': self.up_additive_time_outof,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for PillBug.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size)


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_squirm_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_wander_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xb3774750: ('patterned', _decode_patterned),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0xde7e9f94: ('planar_constraint', structs.decode_BIG_L),
    0x8e4f7b29: ('floor_turn_speed', structs.decode_BIG_f),
    0x5a3a30f4: ('stick_radius', structs.decode_BIG_f),
    0x733bd27c: ('waypoint_approach_distance', structs.decode_BIG_f),
    0xa72530e8: ('visible_distance', structs.decode_BIG_f),
    0x5d84ed71: ('squirm_vulnerability', _decode_squirm_vulnerability),
    0xf382dff7: ('wander_vulnerability', _decode_wander_vulnerability),
    0xad98e16d: ('crawl_radius', structs.decode_BIG_f),
    0x81d699b0: ('roll_radius', structs.decode_BIG_f),
    0x519c7197: ('floor_snap_lerp_factor', structs.decode_BIG_f),
    0xa265383c: ('collision_look_ahead_time', structs.decode_BIG_f),
    0xad08e189: ('forward_priority', structs.decode_BIG_f),
    0x558c0692: ('down_additive_time_into', structs.decode_BIG_f),
    0x0f991bf1: ('down_additive_time_outof', structs.decode_BIG_f),
    0x385a1bed: ('up_additive_time_into', structs.decode_BIG_f),
    0xcf4ea141: ('up_additive_time_outof', structs.decode_BIG_f),
}
