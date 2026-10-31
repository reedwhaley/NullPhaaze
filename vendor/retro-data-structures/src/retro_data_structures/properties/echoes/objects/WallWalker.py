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
from retro_data_structures.properties.echoes.archetypes.CameraShakerData import CameraShakerData
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class WallWalkerJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        leg_vulnerability: json_util.JsonObject
        waypoint_approach_distance: float
        floor_turn_speed: float
        sticky_reach: float
        visible_distance: float
        explode_damage: json_util.JsonObject
        grenade_explosion: int
        grenade_effect: int
        grenade_trail: int
        grenade_mass: float
        grenade_bounciness: float
        grenade_num_bounces: int
        grenade_sound_bounce: int
        grenade_sound_explode: int
        projectile_interval: float
        projectile_stop_homing_range: float
        projectile: int
        projectile_damage: json_util.JsonObject
        projectile_explosion_spash: int
        projectile_explosion_shaker: json_util.JsonObject
    

@dataclasses.dataclass()
class WallWalker(BaseObjectType):
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
    leg_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x9f0ff852, original_name='LegVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    waypoint_approach_distance: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x733bd27c, original_name='WaypointApproachDistance'
        ),
    })
    floor_turn_speed: float = dataclasses.field(default=1080.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8e4f7b29, original_name='FloorTurnSpeed'
        ),
    })
    sticky_reach: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd5c25506, original_name='StickyReach'
        ),
    })
    visible_distance: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa72530e8, original_name='VisibleDistance'
        ),
    })
    explode_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xf6206a12, original_name='ExplodeDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    grenade_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x1319e077, original_name='GrenadeExplosion'
        ),
    })
    grenade_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd207ff0f, original_name='GrenadeEffect'
        ),
    })
    grenade_trail: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2b31c882, original_name='GrenadeTrail'
        ),
    })
    grenade_mass: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9a6bb47f, original_name='GrenadeMass'
        ),
    })
    grenade_bounciness: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xed086ce0, original_name='GrenadeBounciness'
        ),
    })
    grenade_num_bounces: int = dataclasses.field(default=5, metadata={
        'reflection': FieldReflection[int](
            int, id=0x454f16b1, original_name='GrenadeNumBounces'
        ),
    })
    grenade_sound_bounce: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x7f1613b7, original_name='GrenadeSoundBounce'
        ),
    })
    grenade_sound_explode: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x7050d866, original_name='GrenadeSoundExplode'
        ),
    })
    projectile_interval: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd4903c98, original_name='ProjectileInterval'
        ),
    })
    projectile_stop_homing_range: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x723542bb, original_name='ProjectileStopHomingRange'
        ),
    })
    projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xef485db9, original_name='Projectile'
        ),
    })
    projectile_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x553b1339, original_name='ProjectileDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    projectile_explosion_spash: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x68dc4d11, original_name='ProjectileExplosionSpash'
        ),
    })
    projectile_explosion_shaker: CameraShakerData = dataclasses.field(default_factory=CameraShakerData, metadata={
        'reflection': FieldReflection[CameraShakerData](
            CameraShakerData, id=0x22bbdd0a, original_name='ProjectileExplosionShaker', from_json=CameraShakerData.from_json, to_json=CameraShakerData.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'WLWK'

    @classmethod
    def modules(cls) -> list[str]:
        return ['WallCrawler.rel', 'WallWalker.rel']

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
        if property_count != 23:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size, default_override={'creature_size': 1})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9f0ff852
        leg_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x733bd27c
        waypoint_approach_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8e4f7b29
        floor_turn_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd5c25506
        sticky_reach = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa72530e8
        visible_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf6206a12
        explode_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1319e077
        grenade_explosion = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd207ff0f
        grenade_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2b31c882
        grenade_trail = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9a6bb47f
        grenade_mass = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed086ce0
        grenade_bounciness = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x454f16b1
        grenade_num_bounces = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7f1613b7
        grenade_sound_bounce = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7050d866
        grenade_sound_explode = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd4903c98
        projectile_interval = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x723542bb
        projectile_stop_homing_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xef485db9
        projectile = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x553b1339
        projectile_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68dc4d11
        projectile_explosion_spash = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x22bbdd0a
        projectile_explosion_shaker = CameraShakerData.from_stream(data, game, property_size)
    
        return cls(editor_properties, patterned, actor_information, leg_vulnerability, waypoint_approach_distance, floor_turn_speed, sticky_reach, visible_distance, explode_damage, grenade_explosion, grenade_effect, grenade_trail, grenade_mass, grenade_bounciness, grenade_num_bounces, grenade_sound_bounce, grenade_sound_explode, projectile_interval, projectile_stop_homing_range, projectile, projectile_damage, projectile_explosion_spash, projectile_explosion_shaker)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x17')  # 23 properties

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
        self.patterned.to_stream(data, game, default_override={'creature_size': 1})
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

        data.write(b'\x9f\x0f\xf8R')  # 0x9f0ff852
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.leg_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b's;\xd2|')  # 0x733bd27c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.waypoint_approach_distance))

        data.write(b'\x8eO{)')  # 0x8e4f7b29
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.floor_turn_speed))

        data.write(b'\xd5\xc2U\x06')  # 0xd5c25506
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.sticky_reach))

        data.write(b'\xa7%0\xe8')  # 0xa72530e8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.visible_distance))

        data.write(b'\xf6 j\x12')  # 0xf6206a12
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.explode_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x13\x19\xe0w')  # 0x1319e077
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.grenade_explosion))

        data.write(b'\xd2\x07\xff\x0f')  # 0xd207ff0f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.grenade_effect))

        data.write(b'+1\xc8\x82')  # 0x2b31c882
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.grenade_trail))

        data.write(b'\x9ak\xb4\x7f')  # 0x9a6bb47f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grenade_mass))

        data.write(b'\xed\x08l\xe0')  # 0xed086ce0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grenade_bounciness))

        data.write(b'EO\x16\xb1')  # 0x454f16b1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.grenade_num_bounces))

        data.write(b'\x7f\x16\x13\xb7')  # 0x7f1613b7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.grenade_sound_bounce))

        data.write(b'pP\xd8f')  # 0x7050d866
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.grenade_sound_explode))

        data.write(b'\xd4\x90<\x98')  # 0xd4903c98
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.projectile_interval))

        data.write(b'r5B\xbb')  # 0x723542bb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.projectile_stop_homing_range))

        data.write(b'\xefH]\xb9')  # 0xef485db9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.projectile))

        data.write(b'U;\x139')  # 0x553b1339
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.projectile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'h\xdcM\x11')  # 0x68dc4d11
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.projectile_explosion_spash))

        data.write(b'"\xbb\xdd\n')  # 0x22bbdd0a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.projectile_explosion_shaker.to_stream(data, game)
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
        json_data = typing.cast("WallWalkerJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            patterned=PatternedAITypedef.from_json(json_data['patterned']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
            leg_vulnerability=DamageVulnerability.from_json(json_data['leg_vulnerability']),
            waypoint_approach_distance=json_data['waypoint_approach_distance'],
            floor_turn_speed=json_data['floor_turn_speed'],
            sticky_reach=json_data['sticky_reach'],
            visible_distance=json_data['visible_distance'],
            explode_damage=DamageInfo.from_json(json_data['explode_damage']),
            grenade_explosion=json_data['grenade_explosion'],
            grenade_effect=json_data['grenade_effect'],
            grenade_trail=json_data['grenade_trail'],
            grenade_mass=json_data['grenade_mass'],
            grenade_bounciness=json_data['grenade_bounciness'],
            grenade_num_bounces=json_data['grenade_num_bounces'],
            grenade_sound_bounce=json_data['grenade_sound_bounce'],
            grenade_sound_explode=json_data['grenade_sound_explode'],
            projectile_interval=json_data['projectile_interval'],
            projectile_stop_homing_range=json_data['projectile_stop_homing_range'],
            projectile=json_data['projectile'],
            projectile_damage=DamageInfo.from_json(json_data['projectile_damage']),
            projectile_explosion_spash=json_data['projectile_explosion_spash'],
            projectile_explosion_shaker=CameraShakerData.from_json(json_data['projectile_explosion_shaker']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'patterned': self.patterned.to_json(),
            'actor_information': self.actor_information.to_json(),
            'leg_vulnerability': self.leg_vulnerability.to_json(),
            'waypoint_approach_distance': self.waypoint_approach_distance,
            'floor_turn_speed': self.floor_turn_speed,
            'sticky_reach': self.sticky_reach,
            'visible_distance': self.visible_distance,
            'explode_damage': self.explode_damage.to_json(),
            'grenade_explosion': self.grenade_explosion,
            'grenade_effect': self.grenade_effect,
            'grenade_trail': self.grenade_trail,
            'grenade_mass': self.grenade_mass,
            'grenade_bounciness': self.grenade_bounciness,
            'grenade_num_bounces': self.grenade_num_bounces,
            'grenade_sound_bounce': self.grenade_sound_bounce,
            'grenade_sound_explode': self.grenade_sound_explode,
            'projectile_interval': self.projectile_interval,
            'projectile_stop_homing_range': self.projectile_stop_homing_range,
            'projectile': self.projectile,
            'projectile_damage': self.projectile_damage.to_json(),
            'projectile_explosion_spash': self.projectile_explosion_spash,
            'projectile_explosion_shaker': self.projectile_explosion_shaker.to_json(),
        }

    def _dependencies_for_grenade_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grenade_explosion)

    def _dependencies_for_grenade_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grenade_effect)

    def _dependencies_for_grenade_trail(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grenade_trail)

    def _dependencies_for_grenade_sound_bounce(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.grenade_sound_bounce)

    def _dependencies_for_grenade_sound_explode(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.grenade_sound_explode)

    def _dependencies_for_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile)

    def _dependencies_for_projectile_explosion_spash(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile_explosion_spash)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_grenade_explosion, "grenade_explosion", "AssetId"),
            (self._dependencies_for_grenade_effect, "grenade_effect", "AssetId"),
            (self._dependencies_for_grenade_trail, "grenade_trail", "AssetId"),
            (self._dependencies_for_grenade_sound_bounce, "grenade_sound_bounce", "int"),
            (self._dependencies_for_grenade_sound_explode, "grenade_sound_explode", "int"),
            (self._dependencies_for_projectile, "projectile", "AssetId"),
            (self._dependencies_for_projectile_explosion_spash, "projectile_explosion_spash", "AssetId"),
            (self.projectile_explosion_shaker.dependencies_for, "projectile_explosion_shaker", "CameraShakerData"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for WallWalker.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={'creature_size': 1})


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_leg_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_explode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_projectile_explosion_shaker(data: typing.BinaryIO, game: Game, property_size: int) -> CameraShakerData:
    return CameraShakerData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xb3774750: ('patterned', _decode_patterned),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0x9f0ff852: ('leg_vulnerability', _decode_leg_vulnerability),
    0x733bd27c: ('waypoint_approach_distance', structs.decode_BIG_f),
    0x8e4f7b29: ('floor_turn_speed', structs.decode_BIG_f),
    0xd5c25506: ('sticky_reach', structs.decode_BIG_f),
    0xa72530e8: ('visible_distance', structs.decode_BIG_f),
    0xf6206a12: ('explode_damage', _decode_explode_damage),
    0x1319e077: ('grenade_explosion', structs.decode_BIG_L),
    0xd207ff0f: ('grenade_effect', structs.decode_BIG_L),
    0x2b31c882: ('grenade_trail', structs.decode_BIG_L),
    0x9a6bb47f: ('grenade_mass', structs.decode_BIG_f),
    0xed086ce0: ('grenade_bounciness', structs.decode_BIG_f),
    0x454f16b1: ('grenade_num_bounces', structs.decode_BIG_l),
    0x7f1613b7: ('grenade_sound_bounce', structs.decode_BIG_l),
    0x7050d866: ('grenade_sound_explode', structs.decode_BIG_l),
    0xd4903c98: ('projectile_interval', structs.decode_BIG_f),
    0x723542bb: ('projectile_stop_homing_range', structs.decode_BIG_f),
    0xef485db9: ('projectile', structs.decode_BIG_L),
    0x553b1339: ('projectile_damage', _decode_projectile_damage),
    0x68dc4d11: ('projectile_explosion_spash', structs.decode_BIG_L),
    0x22bbdd0a: ('projectile_explosion_shaker', _decode_projectile_explosion_shaker),
}
