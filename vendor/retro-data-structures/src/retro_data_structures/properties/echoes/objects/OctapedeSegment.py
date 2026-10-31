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
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class OctapedeSegmentJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        flavor: int
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        waypoint_approach_distance: float
        visible_distance: float
        wall_turn_speed: float
        floor_turn_speed: float
        down_turn_speed: float
        sticky_reach: float
        projectile_bounds_multiplier: float
        collision_look_ahead: float
        anim_speed_scalar: float
        max_audible_distance: float
        initially_paused: bool
        unknown_0x4fb8747e: float
        between_segments_effect: int
        min_break_apart_speed: float
        max_break_apart_speed: float
        min_break_apart_angle: float
        max_break_apart_angle: float
        min_break_apart_spin_speed: float
        max_break_apart_spin_speed: float
        min_run_around_time: float
        max_run_around_time: float
        min_______________________________: float
        max_______________________________: float
        min_bounces: int
        max_bounces: int
        bounciness: float
        explosion_damage: json_util.JsonObject
        walk_sound: int
        idle_sound: int
        seperate_sound: int
        bounce_sound: int
        explode_sound: int
        unknown_0x0c4763d7: float
    

@dataclasses.dataclass()
class OctapedeSegment(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    flavor: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xbe73724a, original_name='Flavor'
        ),
    })  # Choice
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
    waypoint_approach_distance: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x733bd27c, original_name='WaypointApproachDistance'
        ),
    })
    visible_distance: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa72530e8, original_name='VisibleDistance'
        ),
    })
    wall_turn_speed: float = dataclasses.field(default=360.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xac47c628, original_name='WallTurnSpeed'
        ),
    })
    floor_turn_speed: float = dataclasses.field(default=180.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8e4f7b29, original_name='FloorTurnSpeed'
        ),
    })
    down_turn_speed: float = dataclasses.field(default=120.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3d3c1b76, original_name='DownTurnSpeed'
        ),
    })
    sticky_reach: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd5c25506, original_name='StickyReach'
        ),
    })
    projectile_bounds_multiplier: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x742eab20, original_name='ProjectileBoundsMultiplier'
        ),
    })
    collision_look_ahead: float = dataclasses.field(default=0.019999999552965164, metadata={
        'reflection': FieldReflection[float](
            float, id=0x80a81909, original_name='CollisionLookAhead'
        ),
    })
    anim_speed_scalar: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8590483b, original_name='AnimSpeedScalar'
        ),
    })
    max_audible_distance: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x214e48a0, original_name='MaxAudibleDistance'
        ),
    })
    initially_paused: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xc3cc437f, original_name='InitiallyPaused'
        ),
    })
    unknown_0x4fb8747e: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4fb8747e, original_name='Unknown'
        ),
    })
    between_segments_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['ELSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x1b58c5f1, original_name='BetweenSegmentsEffect'
        ),
    })
    min_break_apart_speed: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9b9c46fc, original_name='MinBreakApartSpeed'
        ),
    })
    max_break_apart_speed: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9f0677d6, original_name='MaxBreakApartSpeed'
        ),
    })
    min_break_apart_angle: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc0241fc1, original_name='MinBreakApartAngle'
        ),
    })
    max_break_apart_angle: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc4be2eeb, original_name='MaxBreakApartAngle'
        ),
    })
    min_break_apart_spin_speed: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x99778599, original_name='MinBreakApartSpinSpeed'
        ),
    })
    max_break_apart_spin_speed: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xff92e3ed, original_name='MaxBreakApartSpinSpeed'
        ),
    })
    min_run_around_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb8a1f0d5, original_name='MinRunAroundTime'
        ),
    })
    max_run_around_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xabe4167e, original_name='MaxRunAroundTime'
        ),
    })
    min_______________________________: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2caddcbe, original_name='Min_______________________________'
        ),
    })
    max_______________________________: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4d320455, original_name='Max_______________________________'
        ),
    })
    min_bounces: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0xd6f71bb3, original_name='MinBounces'
        ),
    })
    max_bounces: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x96b863c5, original_name='MaxBounces'
        ),
    })
    bounciness: float = dataclasses.field(default=0.75, metadata={
        'reflection': FieldReflection[float](
            float, id=0x417f4a91, original_name='Bounciness'
        ),
    })
    explosion_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xdeff74ea, original_name='ExplosionDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    walk_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xa24376ec, original_name='WalkSound'
        ),
    })
    idle_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x40338715, original_name='IdleSound'
        ),
    })
    seperate_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x527a643e, original_name='SeperateSound'
        ),
    })
    bounce_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x0bb3ccae, original_name='BounceSound'
        ),
    })
    explode_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xf3a4af05, original_name='ExplodeSound'
        ),
    })
    unknown_0x0c4763d7: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0c4763d7, original_name='Unknown'
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'OCTS'

    @classmethod
    def modules(cls) -> list[str]:
        return ['WallCrawler.rel', 'OctapedeSegment.rel']

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
        if property_count != 37:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbe73724a
        flavor = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size, default_override={'mass': 25.0, 'speed': 3.0, 'turn_speed': 720.0, 'detection_range': 5.0, 'detection_height_range': 5.0, 'detection_angle': 90.0, 'min_attack_range': 4.0, 'max_attack_range': 20.0, 'damage_wait_time': 3.0, 'collision_radius': 0.20000000298023224, 'collision_height': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x733bd27c
        waypoint_approach_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa72530e8
        visible_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xac47c628
        wall_turn_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8e4f7b29
        floor_turn_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3d3c1b76
        down_turn_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd5c25506
        sticky_reach = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x742eab20
        projectile_bounds_multiplier = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x80a81909
        collision_look_ahead = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8590483b
        anim_speed_scalar = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x214e48a0
        max_audible_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc3cc437f
        initially_paused = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4fb8747e
        unknown_0x4fb8747e = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1b58c5f1
        between_segments_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9b9c46fc
        min_break_apart_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9f0677d6
        max_break_apart_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc0241fc1
        min_break_apart_angle = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc4be2eeb
        max_break_apart_angle = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x99778599
        min_break_apart_spin_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xff92e3ed
        max_break_apart_spin_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb8a1f0d5
        min_run_around_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xabe4167e
        max_run_around_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2caddcbe
        min_______________________________ = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4d320455
        max_______________________________ = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd6f71bb3
        min_bounces = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x96b863c5
        max_bounces = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x417f4a91
        bounciness = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdeff74ea
        explosion_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 9, 'di_damage': 5.0, 'di_knock_back_power': 2.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa24376ec
        walk_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x40338715
        idle_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x527a643e
        seperate_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0bb3ccae
        bounce_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf3a4af05
        explode_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0c4763d7
        unknown_0x0c4763d7 = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(editor_properties, flavor, patterned, actor_information, waypoint_approach_distance, visible_distance, wall_turn_speed, floor_turn_speed, down_turn_speed, sticky_reach, projectile_bounds_multiplier, collision_look_ahead, anim_speed_scalar, max_audible_distance, initially_paused, unknown_0x4fb8747e, between_segments_effect, min_break_apart_speed, max_break_apart_speed, min_break_apart_angle, max_break_apart_angle, min_break_apart_spin_speed, max_break_apart_spin_speed, min_run_around_time, max_run_around_time, min_______________________________, max_______________________________, min_bounces, max_bounces, bounciness, explosion_damage, walk_sound, idle_sound, seperate_sound, bounce_sound, explode_sound, unknown_0x0c4763d7)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00%')  # 37 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbesrJ')  # 0xbe73724a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.flavor))

        data.write(b'\xb3wGP')  # 0xb3774750
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.patterned.to_stream(data, game, default_override={'mass': 25.0, 'speed': 3.0, 'turn_speed': 720.0, 'detection_range': 5.0, 'detection_height_range': 5.0, 'detection_angle': 90.0, 'min_attack_range': 4.0, 'max_attack_range': 20.0, 'damage_wait_time': 3.0, 'collision_radius': 0.20000000298023224, 'collision_height': 5.0})
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

        data.write(b's;\xd2|')  # 0x733bd27c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.waypoint_approach_distance))

        data.write(b'\xa7%0\xe8')  # 0xa72530e8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.visible_distance))

        data.write(b'\xacG\xc6(')  # 0xac47c628
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.wall_turn_speed))

        data.write(b'\x8eO{)')  # 0x8e4f7b29
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.floor_turn_speed))

        data.write(b'=<\x1bv')  # 0x3d3c1b76
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.down_turn_speed))

        data.write(b'\xd5\xc2U\x06')  # 0xd5c25506
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.sticky_reach))

        data.write(b't.\xab ')  # 0x742eab20
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.projectile_bounds_multiplier))

        data.write(b'\x80\xa8\x19\t')  # 0x80a81909
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.collision_look_ahead))

        data.write(b'\x85\x90H;')  # 0x8590483b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.anim_speed_scalar))

        data.write(b'!NH\xa0')  # 0x214e48a0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_audible_distance))

        data.write(b'\xc3\xccC\x7f')  # 0xc3cc437f
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.initially_paused))

        data.write(b'O\xb8t~')  # 0x4fb8747e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4fb8747e))

        data.write(b'\x1bX\xc5\xf1')  # 0x1b58c5f1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.between_segments_effect))

        data.write(b'\x9b\x9cF\xfc')  # 0x9b9c46fc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_break_apart_speed))

        data.write(b'\x9f\x06w\xd6')  # 0x9f0677d6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_break_apart_speed))

        data.write(b'\xc0$\x1f\xc1')  # 0xc0241fc1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_break_apart_angle))

        data.write(b'\xc4\xbe.\xeb')  # 0xc4be2eeb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_break_apart_angle))

        data.write(b'\x99w\x85\x99')  # 0x99778599
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_break_apart_spin_speed))

        data.write(b'\xff\x92\xe3\xed')  # 0xff92e3ed
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_break_apart_spin_speed))

        data.write(b'\xb8\xa1\xf0\xd5')  # 0xb8a1f0d5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_run_around_time))

        data.write(b'\xab\xe4\x16~')  # 0xabe4167e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_run_around_time))

        data.write(b',\xad\xdc\xbe')  # 0x2caddcbe
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_______________________________))

        data.write(b'M2\x04U')  # 0x4d320455
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_______________________________))

        data.write(b'\xd6\xf7\x1b\xb3')  # 0xd6f71bb3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.min_bounces))

        data.write(b'\x96\xb8c\xc5')  # 0x96b863c5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_bounces))

        data.write(b'A\x7fJ\x91')  # 0x417f4a91
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.bounciness))

        data.write(b'\xde\xfft\xea')  # 0xdeff74ea
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.explosion_damage.to_stream(data, game, default_override={'di_weapon_type': 9, 'di_damage': 5.0, 'di_knock_back_power': 2.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa2Cv\xec')  # 0xa24376ec
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.walk_sound))

        data.write(b'@3\x87\x15')  # 0x40338715
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.idle_sound))

        data.write(b'Rzd>')  # 0x527a643e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.seperate_sound))

        data.write(b'\x0b\xb3\xcc\xae')  # 0xbb3ccae
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.bounce_sound))

        data.write(b'\xf3\xa4\xaf\x05')  # 0xf3a4af05
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.explode_sound))

        data.write(b'\x0cGc\xd7')  # 0xc4763d7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0c4763d7))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("OctapedeSegmentJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            flavor=json_data['flavor'],
            patterned=PatternedAITypedef.from_json(json_data['patterned']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
            waypoint_approach_distance=json_data['waypoint_approach_distance'],
            visible_distance=json_data['visible_distance'],
            wall_turn_speed=json_data['wall_turn_speed'],
            floor_turn_speed=json_data['floor_turn_speed'],
            down_turn_speed=json_data['down_turn_speed'],
            sticky_reach=json_data['sticky_reach'],
            projectile_bounds_multiplier=json_data['projectile_bounds_multiplier'],
            collision_look_ahead=json_data['collision_look_ahead'],
            anim_speed_scalar=json_data['anim_speed_scalar'],
            max_audible_distance=json_data['max_audible_distance'],
            initially_paused=json_data['initially_paused'],
            unknown_0x4fb8747e=json_data['unknown_0x4fb8747e'],
            between_segments_effect=json_data['between_segments_effect'],
            min_break_apart_speed=json_data['min_break_apart_speed'],
            max_break_apart_speed=json_data['max_break_apart_speed'],
            min_break_apart_angle=json_data['min_break_apart_angle'],
            max_break_apart_angle=json_data['max_break_apart_angle'],
            min_break_apart_spin_speed=json_data['min_break_apart_spin_speed'],
            max_break_apart_spin_speed=json_data['max_break_apart_spin_speed'],
            min_run_around_time=json_data['min_run_around_time'],
            max_run_around_time=json_data['max_run_around_time'],
            min_______________________________=json_data['min_______________________________'],
            max_______________________________=json_data['max_______________________________'],
            min_bounces=json_data['min_bounces'],
            max_bounces=json_data['max_bounces'],
            bounciness=json_data['bounciness'],
            explosion_damage=DamageInfo.from_json(json_data['explosion_damage']),
            walk_sound=json_data['walk_sound'],
            idle_sound=json_data['idle_sound'],
            seperate_sound=json_data['seperate_sound'],
            bounce_sound=json_data['bounce_sound'],
            explode_sound=json_data['explode_sound'],
            unknown_0x0c4763d7=json_data['unknown_0x0c4763d7'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'flavor': self.flavor,
            'patterned': self.patterned.to_json(),
            'actor_information': self.actor_information.to_json(),
            'waypoint_approach_distance': self.waypoint_approach_distance,
            'visible_distance': self.visible_distance,
            'wall_turn_speed': self.wall_turn_speed,
            'floor_turn_speed': self.floor_turn_speed,
            'down_turn_speed': self.down_turn_speed,
            'sticky_reach': self.sticky_reach,
            'projectile_bounds_multiplier': self.projectile_bounds_multiplier,
            'collision_look_ahead': self.collision_look_ahead,
            'anim_speed_scalar': self.anim_speed_scalar,
            'max_audible_distance': self.max_audible_distance,
            'initially_paused': self.initially_paused,
            'unknown_0x4fb8747e': self.unknown_0x4fb8747e,
            'between_segments_effect': self.between_segments_effect,
            'min_break_apart_speed': self.min_break_apart_speed,
            'max_break_apart_speed': self.max_break_apart_speed,
            'min_break_apart_angle': self.min_break_apart_angle,
            'max_break_apart_angle': self.max_break_apart_angle,
            'min_break_apart_spin_speed': self.min_break_apart_spin_speed,
            'max_break_apart_spin_speed': self.max_break_apart_spin_speed,
            'min_run_around_time': self.min_run_around_time,
            'max_run_around_time': self.max_run_around_time,
            'min_______________________________': self.min_______________________________,
            'max_______________________________': self.max_______________________________,
            'min_bounces': self.min_bounces,
            'max_bounces': self.max_bounces,
            'bounciness': self.bounciness,
            'explosion_damage': self.explosion_damage.to_json(),
            'walk_sound': self.walk_sound,
            'idle_sound': self.idle_sound,
            'seperate_sound': self.seperate_sound,
            'bounce_sound': self.bounce_sound,
            'explode_sound': self.explode_sound,
            'unknown_0x0c4763d7': self.unknown_0x0c4763d7,
        }

    def _dependencies_for_between_segments_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.between_segments_effect)

    def _dependencies_for_walk_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.walk_sound)

    def _dependencies_for_idle_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.idle_sound)

    def _dependencies_for_seperate_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.seperate_sound)

    def _dependencies_for_bounce_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.bounce_sound)

    def _dependencies_for_explode_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.explode_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_between_segments_effect, "between_segments_effect", "AssetId"),
            (self._dependencies_for_walk_sound, "walk_sound", "int"),
            (self._dependencies_for_idle_sound, "idle_sound", "int"),
            (self._dependencies_for_seperate_sound, "seperate_sound", "int"),
            (self._dependencies_for_bounce_sound, "bounce_sound", "int"),
            (self._dependencies_for_explode_sound, "explode_sound", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for OctapedeSegment.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={'mass': 25.0, 'speed': 3.0, 'turn_speed': 720.0, 'detection_range': 5.0, 'detection_height_range': 5.0, 'detection_angle': 90.0, 'min_attack_range': 4.0, 'max_attack_range': 20.0, 'damage_wait_time': 3.0, 'collision_radius': 0.20000000298023224, 'collision_height': 5.0})


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_explosion_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 9, 'di_damage': 5.0, 'di_knock_back_power': 2.0})


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xbe73724a: ('flavor', structs.decode_BIG_L),
    0xb3774750: ('patterned', _decode_patterned),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0x733bd27c: ('waypoint_approach_distance', structs.decode_BIG_f),
    0xa72530e8: ('visible_distance', structs.decode_BIG_f),
    0xac47c628: ('wall_turn_speed', structs.decode_BIG_f),
    0x8e4f7b29: ('floor_turn_speed', structs.decode_BIG_f),
    0x3d3c1b76: ('down_turn_speed', structs.decode_BIG_f),
    0xd5c25506: ('sticky_reach', structs.decode_BIG_f),
    0x742eab20: ('projectile_bounds_multiplier', structs.decode_BIG_f),
    0x80a81909: ('collision_look_ahead', structs.decode_BIG_f),
    0x8590483b: ('anim_speed_scalar', structs.decode_BIG_f),
    0x214e48a0: ('max_audible_distance', structs.decode_BIG_f),
    0xc3cc437f: ('initially_paused', structs.decode_BIG_bool_),
    0x4fb8747e: ('unknown_0x4fb8747e', structs.decode_BIG_f),
    0x1b58c5f1: ('between_segments_effect', structs.decode_BIG_L),
    0x9b9c46fc: ('min_break_apart_speed', structs.decode_BIG_f),
    0x9f0677d6: ('max_break_apart_speed', structs.decode_BIG_f),
    0xc0241fc1: ('min_break_apart_angle', structs.decode_BIG_f),
    0xc4be2eeb: ('max_break_apart_angle', structs.decode_BIG_f),
    0x99778599: ('min_break_apart_spin_speed', structs.decode_BIG_f),
    0xff92e3ed: ('max_break_apart_spin_speed', structs.decode_BIG_f),
    0xb8a1f0d5: ('min_run_around_time', structs.decode_BIG_f),
    0xabe4167e: ('max_run_around_time', structs.decode_BIG_f),
    0x2caddcbe: ('min_______________________________', structs.decode_BIG_f),
    0x4d320455: ('max_______________________________', structs.decode_BIG_f),
    0xd6f71bb3: ('min_bounces', structs.decode_BIG_l),
    0x96b863c5: ('max_bounces', structs.decode_BIG_l),
    0x417f4a91: ('bounciness', structs.decode_BIG_f),
    0xdeff74ea: ('explosion_damage', _decode_explosion_damage),
    0xa24376ec: ('walk_sound', structs.decode_BIG_l),
    0x40338715: ('idle_sound', structs.decode_BIG_l),
    0x527a643e: ('seperate_sound', structs.decode_BIG_l),
    0x0bb3ccae: ('bounce_sound', structs.decode_BIG_l),
    0xf3a4af05: ('explode_sound', structs.decode_BIG_l),
    0x0c4763d7: ('unknown_0x0c4763d7', structs.decode_BIG_f),
}
