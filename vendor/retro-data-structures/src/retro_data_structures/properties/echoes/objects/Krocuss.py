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
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.echoes.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class KrocussJson(typing_extensions.TypedDict):
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
        initially_paused: bool
        time_shell_closed: float
        time_to_open_shell: float
        time_shell_open: float
        time_to_close_shell: float
        time_to_close_when_damaged: float
        shell_closed_vulnerability: json_util.JsonObject
        wing_light_color: json_util.JsonValue
        dpsc: int
        shell_open_sound: int
        shell_close_sound: int
        max_audible_distance: float
    

@dataclasses.dataclass()
class Krocuss(BaseObjectType):
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
    initially_paused: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xc3cc437f, original_name='InitiallyPaused'
        ),
    })
    time_shell_closed: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf04cadca, original_name='TimeShellClosed'
        ),
    })
    time_to_open_shell: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x497d54e8, original_name='TimeToOpenShell'
        ),
    })
    time_shell_open: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3371c963, original_name='TimeShellOpen'
        ),
    })
    time_to_close_shell: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x22d37771, original_name='TimeToCloseShell'
        ),
    })
    time_to_close_when_damaged: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbbebed9e, original_name='TimeToCloseWhenDamaged'
        ),
    })
    shell_closed_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x6bd144c8, original_name='ShellClosedVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    wing_light_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x4d20624b, original_name='WingLightColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dpsc: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['DPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc3566114, original_name='DPSC'
        ),
    })
    shell_open_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x6a11338f, original_name='ShellOpenSound'
        ),
    })
    shell_close_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xf64ca627, original_name='ShellCloseSound'
        ),
    })
    max_audible_distance: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x214e48a0, original_name='MaxAudibleDistance'
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'KROC'

    @classmethod
    def modules(cls) -> list[str]:
        return ['WallCrawler.rel', 'Krocuss.rel']

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
        if property_count != 25:
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
        assert property_id == 0xc3cc437f
        initially_paused = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf04cadca
        time_shell_closed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x497d54e8
        time_to_open_shell = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3371c963
        time_shell_open = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x22d37771
        time_to_close_shell = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbbebed9e
        time_to_close_when_damaged = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6bd144c8
        shell_closed_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4d20624b
        wing_light_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc3566114
        dpsc = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6a11338f
        shell_open_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf64ca627
        shell_close_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x214e48a0
        max_audible_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(editor_properties, flavor, patterned, actor_information, waypoint_approach_distance, visible_distance, wall_turn_speed, floor_turn_speed, down_turn_speed, sticky_reach, projectile_bounds_multiplier, collision_look_ahead, anim_speed_scalar, initially_paused, time_shell_closed, time_to_open_shell, time_shell_open, time_to_close_shell, time_to_close_when_damaged, shell_closed_vulnerability, wing_light_color, dpsc, shell_open_sound, shell_close_sound, max_audible_distance)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x19')  # 25 properties

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

        data.write(b'\xc3\xccC\x7f')  # 0xc3cc437f
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.initially_paused))

        data.write(b'\xf0L\xad\xca')  # 0xf04cadca
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.time_shell_closed))

        data.write(b'I}T\xe8')  # 0x497d54e8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.time_to_open_shell))

        data.write(b'3q\xc9c')  # 0x3371c963
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.time_shell_open))

        data.write(b'"\xd3wq')  # 0x22d37771
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.time_to_close_shell))

        data.write(b'\xbb\xeb\xed\x9e')  # 0xbbebed9e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.time_to_close_when_damaged))

        data.write(b'k\xd1D\xc8')  # 0x6bd144c8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shell_closed_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'M bK')  # 0x4d20624b
        data.write(b'\x00\x10')  # size
        self.wing_light_color.to_stream(data, game)

        data.write(b'\xc3Va\x14')  # 0xc3566114
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.dpsc))

        data.write(b'j\x113\x8f')  # 0x6a11338f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.shell_open_sound))

        data.write(b"\xf6L\xa6'")  # 0xf64ca627
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.shell_close_sound))

        data.write(b'!NH\xa0')  # 0x214e48a0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_audible_distance))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("KrocussJson", data)
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
            initially_paused=json_data['initially_paused'],
            time_shell_closed=json_data['time_shell_closed'],
            time_to_open_shell=json_data['time_to_open_shell'],
            time_shell_open=json_data['time_shell_open'],
            time_to_close_shell=json_data['time_to_close_shell'],
            time_to_close_when_damaged=json_data['time_to_close_when_damaged'],
            shell_closed_vulnerability=DamageVulnerability.from_json(json_data['shell_closed_vulnerability']),
            wing_light_color=Color.from_json(json_data['wing_light_color']),
            dpsc=json_data['dpsc'],
            shell_open_sound=json_data['shell_open_sound'],
            shell_close_sound=json_data['shell_close_sound'],
            max_audible_distance=json_data['max_audible_distance'],
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
            'initially_paused': self.initially_paused,
            'time_shell_closed': self.time_shell_closed,
            'time_to_open_shell': self.time_to_open_shell,
            'time_shell_open': self.time_shell_open,
            'time_to_close_shell': self.time_to_close_shell,
            'time_to_close_when_damaged': self.time_to_close_when_damaged,
            'shell_closed_vulnerability': self.shell_closed_vulnerability.to_json(),
            'wing_light_color': self.wing_light_color.to_json(),
            'dpsc': self.dpsc,
            'shell_open_sound': self.shell_open_sound,
            'shell_close_sound': self.shell_close_sound,
            'max_audible_distance': self.max_audible_distance,
        }

    def _dependencies_for_dpsc(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.dpsc)

    def _dependencies_for_shell_open_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.shell_open_sound)

    def _dependencies_for_shell_close_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.shell_close_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_dpsc, "dpsc", "AssetId"),
            (self._dependencies_for_shell_open_sound, "shell_open_sound", "int"),
            (self._dependencies_for_shell_close_sound, "shell_close_sound", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for Krocuss.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={'mass': 25.0, 'speed': 3.0, 'turn_speed': 720.0, 'detection_range': 5.0, 'detection_height_range': 5.0, 'detection_angle': 90.0, 'min_attack_range': 4.0, 'max_attack_range': 20.0, 'damage_wait_time': 3.0, 'collision_radius': 0.20000000298023224, 'collision_height': 5.0})


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_shell_closed_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_wing_light_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


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
    0xc3cc437f: ('initially_paused', structs.decode_BIG_bool_),
    0xf04cadca: ('time_shell_closed', structs.decode_BIG_f),
    0x497d54e8: ('time_to_open_shell', structs.decode_BIG_f),
    0x3371c963: ('time_shell_open', structs.decode_BIG_f),
    0x22d37771: ('time_to_close_shell', structs.decode_BIG_f),
    0xbbebed9e: ('time_to_close_when_damaged', structs.decode_BIG_f),
    0x6bd144c8: ('shell_closed_vulnerability', _decode_shell_closed_vulnerability),
    0x4d20624b: ('wing_light_color', _decode_wing_light_color),
    0xc3566114: ('dpsc', structs.decode_BIG_L),
    0x6a11338f: ('shell_open_sound', structs.decode_BIG_l),
    0xf64ca627: ('shell_close_sound', structs.decode_BIG_l),
    0x214e48a0: ('max_audible_distance', structs.decode_BIG_f),
}
