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
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class KraleeJson(typing_extensions.TypedDict):
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
        warp_in_time: float
        warp_out_time: float
        visible_time: float
        visible_time_random_offset: float
        invisible_time: float
        invisible_time_random_offset: float
        warp_attack_radius: float
        warp_attack_knockback: float
        warp_attack_damage: float
        anim_speed_scalar: float
        max_audible_distance: float
        warp_in_particle_effect: int
        warp_out_particle_effect: int
        warp_in_sound: int
        warp_out_sound: int
        initially_paused: bool
        initially_invisible: bool
    

@dataclasses.dataclass()
class Kralee(BaseObjectType):
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
    warp_in_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xed6a9353, original_name='WarpInTime'
        ),
    })
    warp_out_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x033153a0, original_name='WarpOutTime'
        ),
    })
    visible_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5704897c, original_name='VisibleTime'
        ),
    })
    visible_time_random_offset: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7bba36ff, original_name='VisibleTimeRandomOffset'
        ),
    })
    invisible_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbbd4b10c, original_name='InvisibleTime'
        ),
    })
    invisible_time_random_offset: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4e4ae0e4, original_name='InvisibleTimeRandomOffset'
        ),
    })
    warp_attack_radius: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xad69ac32, original_name='WarpAttackRadius'
        ),
    })
    warp_attack_knockback: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc7d2ede8, original_name='WarpAttackKnockback'
        ),
    })
    warp_attack_damage: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb1a26335, original_name='WarpAttackDamage'
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
    warp_in_particle_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x351dbc73, original_name='WarpInParticleEffect'
        ),
    })
    warp_out_particle_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2d72ba7b, original_name='WarpOutParticleEffect'
        ),
    })
    warp_in_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x80b58324, original_name='WarpInSound'
        ),
    })
    warp_out_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xa4ef7b42, original_name='WarpOutSound'
        ),
    })
    initially_paused: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xc3cc437f, original_name='InitiallyPaused'
        ),
    })
    initially_invisible: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x738d1c80, original_name='InitiallyInvisible'
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'KRAL'

    @classmethod
    def modules(cls) -> list[str]:
        return ['WallCrawler.rel', 'Kralee.rel']

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
        if property_count != 29:
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
        assert property_id == 0xed6a9353
        warp_in_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x033153a0
        warp_out_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5704897c
        visible_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7bba36ff
        visible_time_random_offset = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbbd4b10c
        invisible_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4e4ae0e4
        invisible_time_random_offset = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xad69ac32
        warp_attack_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc7d2ede8
        warp_attack_knockback = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb1a26335
        warp_attack_damage = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8590483b
        anim_speed_scalar = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x214e48a0
        max_audible_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x351dbc73
        warp_in_particle_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2d72ba7b
        warp_out_particle_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x80b58324
        warp_in_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa4ef7b42
        warp_out_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc3cc437f
        initially_paused = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x738d1c80
        initially_invisible = structs.BIG_bool_.unpack(data.read(1))[0]
    
        return cls(editor_properties, flavor, patterned, actor_information, waypoint_approach_distance, visible_distance, wall_turn_speed, floor_turn_speed, down_turn_speed, sticky_reach, projectile_bounds_multiplier, collision_look_ahead, warp_in_time, warp_out_time, visible_time, visible_time_random_offset, invisible_time, invisible_time_random_offset, warp_attack_radius, warp_attack_knockback, warp_attack_damage, anim_speed_scalar, max_audible_distance, warp_in_particle_effect, warp_out_particle_effect, warp_in_sound, warp_out_sound, initially_paused, initially_invisible)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x1d')  # 29 properties

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

        data.write(b'\xedj\x93S')  # 0xed6a9353
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.warp_in_time))

        data.write(b'\x031S\xa0')  # 0x33153a0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.warp_out_time))

        data.write(b'W\x04\x89|')  # 0x5704897c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.visible_time))

        data.write(b'{\xba6\xff')  # 0x7bba36ff
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.visible_time_random_offset))

        data.write(b'\xbb\xd4\xb1\x0c')  # 0xbbd4b10c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.invisible_time))

        data.write(b'NJ\xe0\xe4')  # 0x4e4ae0e4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.invisible_time_random_offset))

        data.write(b'\xadi\xac2')  # 0xad69ac32
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.warp_attack_radius))

        data.write(b'\xc7\xd2\xed\xe8')  # 0xc7d2ede8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.warp_attack_knockback))

        data.write(b'\xb1\xa2c5')  # 0xb1a26335
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.warp_attack_damage))

        data.write(b'\x85\x90H;')  # 0x8590483b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.anim_speed_scalar))

        data.write(b'!NH\xa0')  # 0x214e48a0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_audible_distance))

        data.write(b'5\x1d\xbcs')  # 0x351dbc73
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.warp_in_particle_effect))

        data.write(b'-r\xba{')  # 0x2d72ba7b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.warp_out_particle_effect))

        data.write(b'\x80\xb5\x83$')  # 0x80b58324
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.warp_in_sound))

        data.write(b'\xa4\xef{B')  # 0xa4ef7b42
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.warp_out_sound))

        data.write(b'\xc3\xccC\x7f')  # 0xc3cc437f
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.initially_paused))

        data.write(b's\x8d\x1c\x80')  # 0x738d1c80
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.initially_invisible))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("KraleeJson", data)
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
            warp_in_time=json_data['warp_in_time'],
            warp_out_time=json_data['warp_out_time'],
            visible_time=json_data['visible_time'],
            visible_time_random_offset=json_data['visible_time_random_offset'],
            invisible_time=json_data['invisible_time'],
            invisible_time_random_offset=json_data['invisible_time_random_offset'],
            warp_attack_radius=json_data['warp_attack_radius'],
            warp_attack_knockback=json_data['warp_attack_knockback'],
            warp_attack_damage=json_data['warp_attack_damage'],
            anim_speed_scalar=json_data['anim_speed_scalar'],
            max_audible_distance=json_data['max_audible_distance'],
            warp_in_particle_effect=json_data['warp_in_particle_effect'],
            warp_out_particle_effect=json_data['warp_out_particle_effect'],
            warp_in_sound=json_data['warp_in_sound'],
            warp_out_sound=json_data['warp_out_sound'],
            initially_paused=json_data['initially_paused'],
            initially_invisible=json_data['initially_invisible'],
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
            'warp_in_time': self.warp_in_time,
            'warp_out_time': self.warp_out_time,
            'visible_time': self.visible_time,
            'visible_time_random_offset': self.visible_time_random_offset,
            'invisible_time': self.invisible_time,
            'invisible_time_random_offset': self.invisible_time_random_offset,
            'warp_attack_radius': self.warp_attack_radius,
            'warp_attack_knockback': self.warp_attack_knockback,
            'warp_attack_damage': self.warp_attack_damage,
            'anim_speed_scalar': self.anim_speed_scalar,
            'max_audible_distance': self.max_audible_distance,
            'warp_in_particle_effect': self.warp_in_particle_effect,
            'warp_out_particle_effect': self.warp_out_particle_effect,
            'warp_in_sound': self.warp_in_sound,
            'warp_out_sound': self.warp_out_sound,
            'initially_paused': self.initially_paused,
            'initially_invisible': self.initially_invisible,
        }

    def _dependencies_for_warp_in_particle_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.warp_in_particle_effect)

    def _dependencies_for_warp_out_particle_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.warp_out_particle_effect)

    def _dependencies_for_warp_in_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.warp_in_sound)

    def _dependencies_for_warp_out_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.warp_out_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_warp_in_particle_effect, "warp_in_particle_effect", "AssetId"),
            (self._dependencies_for_warp_out_particle_effect, "warp_out_particle_effect", "AssetId"),
            (self._dependencies_for_warp_in_sound, "warp_in_sound", "int"),
            (self._dependencies_for_warp_out_sound, "warp_out_sound", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for Kralee.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={'mass': 25.0, 'speed': 3.0, 'turn_speed': 720.0, 'detection_range': 5.0, 'detection_height_range': 5.0, 'detection_angle': 90.0, 'min_attack_range': 4.0, 'max_attack_range': 20.0, 'damage_wait_time': 3.0, 'collision_radius': 0.20000000298023224, 'collision_height': 5.0})


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


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
    0xed6a9353: ('warp_in_time', structs.decode_BIG_f),
    0x033153a0: ('warp_out_time', structs.decode_BIG_f),
    0x5704897c: ('visible_time', structs.decode_BIG_f),
    0x7bba36ff: ('visible_time_random_offset', structs.decode_BIG_f),
    0xbbd4b10c: ('invisible_time', structs.decode_BIG_f),
    0x4e4ae0e4: ('invisible_time_random_offset', structs.decode_BIG_f),
    0xad69ac32: ('warp_attack_radius', structs.decode_BIG_f),
    0xc7d2ede8: ('warp_attack_knockback', structs.decode_BIG_f),
    0xb1a26335: ('warp_attack_damage', structs.decode_BIG_f),
    0x8590483b: ('anim_speed_scalar', structs.decode_BIG_f),
    0x214e48a0: ('max_audible_distance', structs.decode_BIG_f),
    0x351dbc73: ('warp_in_particle_effect', structs.decode_BIG_L),
    0x2d72ba7b: ('warp_out_particle_effect', structs.decode_BIG_L),
    0x80b58324: ('warp_in_sound', structs.decode_BIG_l),
    0xa4ef7b42: ('warp_out_sound', structs.decode_BIG_l),
    0xc3cc437f: ('initially_paused', structs.decode_BIG_bool_),
    0x738d1c80: ('initially_invisible', structs.decode_BIG_bool_),
}
