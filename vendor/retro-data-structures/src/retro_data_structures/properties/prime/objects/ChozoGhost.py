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
from retro_data_structures.properties.prime.archetypes.ActorParameters import ActorParameters
from retro_data_structures.properties.prime.archetypes.BehaveChance import BehaveChance
from retro_data_structures.properties.prime.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.prime.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.prime.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class ChozoGhostJson(typing_extensions.TypedDict):
        name: str
        position: json_util.JsonValue
        rotation: json_util.JsonValue
        scale: json_util.JsonValue
        unnamed_0x00000004: json_util.JsonObject
        unnamed_0x00000005: json_util.JsonObject
        hearing_radius: float
        fade_out_delay: float
        attack_delay: float
        freeze_time: float
        hand_blast: int
        hand_blast_damage: json_util.JsonObject
        powerball: int
        powerball_damage: json_util.JsonObject
        far: json_util.JsonObject
        mid: json_util.JsonObject
        near: json_util.JsonObject
        sound_impact: int
        disable_player_gun_time: float
        sound_phaze_in: int
        sound_phaze_out: int
        unknown: int
        projectile_stop_homing_range: float
        start_style: int
        hurl_recover_time: float
        projectile_visor_effect: int
        sound_projectile_visor: int
        near_to_mid_distance: float
        mid_to_far_distance: float
        near_chance: int
        mid_chance: int
    

@dataclasses.dataclass()
class ChozoGhost(BaseObjectType):
    name: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x00000000, original_name='Name'
        ),
    })
    position: Vector = dataclasses.field(default_factory=Vector, metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x00000001, original_name='Position', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    rotation: Vector = dataclasses.field(default_factory=Vector, metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x00000002, original_name='Rotation', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    scale: Vector = dataclasses.field(default_factory=Vector, metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x00000003, original_name='Scale', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    unnamed_0x00000004: PatternedAITypedef = dataclasses.field(default_factory=PatternedAITypedef, metadata={
        'reflection': FieldReflection[PatternedAITypedef](
            PatternedAITypedef, id=0x00000004, original_name='4', from_json=PatternedAITypedef.from_json, to_json=PatternedAITypedef.to_json
        ),
    })
    unnamed_0x00000005: ActorParameters = dataclasses.field(default_factory=ActorParameters, metadata={
        'reflection': FieldReflection[ActorParameters](
            ActorParameters, id=0x00000005, original_name='5', from_json=ActorParameters.from_json, to_json=ActorParameters.to_json
        ),
    })
    hearing_radius: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x00000006, original_name='HearingRadius'
        ),
    })
    fade_out_delay: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x00000007, original_name='FadeOutDelay'
        ),
    })
    attack_delay: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x00000008, original_name='AttackDelay'
        ),
    })
    freeze_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x00000009, original_name='FreezeTime'
        ),
    })
    hand_blast: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x0000000a, original_name='HandBlast'
        ),
    })
    hand_blast_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x0000000b, original_name='HandBlastDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    powerball: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x0000000c, original_name='Powerball'
        ),
    })
    powerball_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x0000000d, original_name='PowerballDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    far: BehaveChance = dataclasses.field(default_factory=BehaveChance, metadata={
        'reflection': FieldReflection[BehaveChance](
            BehaveChance, id=0x0000000e, original_name='Far', from_json=BehaveChance.from_json, to_json=BehaveChance.to_json
        ),
    })
    mid: BehaveChance = dataclasses.field(default_factory=BehaveChance, metadata={
        'reflection': FieldReflection[BehaveChance](
            BehaveChance, id=0x0000000f, original_name='Mid', from_json=BehaveChance.from_json, to_json=BehaveChance.to_json
        ),
    })
    near: BehaveChance = dataclasses.field(default_factory=BehaveChance, metadata={
        'reflection': FieldReflection[BehaveChance](
            BehaveChance, id=0x00000010, original_name='Near', from_json=BehaveChance.from_json, to_json=BehaveChance.to_json
        ),
    })
    sound_impact: int = dataclasses.field(default=0, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x00000011, original_name='Sound_Impact'
        ),
    })
    disable_player_gun_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x00000012, original_name='DisablePlayerGunTime'
        ),
    })
    sound_phaze_in: int = dataclasses.field(default=0, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x00000013, original_name='Sound_PhazeIn'
        ),
    })
    sound_phaze_out: int = dataclasses.field(default=0, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x00000014, original_name='Sound_PhazeOut'
        ),
    })
    unknown: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x00000015, original_name='Unknown'
        ),
    })
    projectile_stop_homing_range: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x00000016, original_name='ProjectileStopHomingRange'
        ),
    })
    start_style: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x00000017, original_name='StartStyle'
        ),
    })
    hurl_recover_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x00000018, original_name='HurlRecoverTime'
        ),
    })
    projectile_visor_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x00000019, original_name='ProjectileVisorEffect'
        ),
    })
    sound_projectile_visor: int = dataclasses.field(default=0, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x0000001a, original_name='Sound_ProjectileVisor'
        ),
    })
    near_to_mid_distance: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0000001b, original_name='NearToMidDistance'
        ),
    })
    mid_to_far_distance: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0000001c, original_name='MidToFarDistance'
        ),
    })
    near_chance: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x0000001d, original_name='NearChance'
        ),
    })
    mid_chance: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x0000001e, original_name='MidChance'
        ),
    })

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    @classmethod
    def object_type(cls) -> int:
        return 0x28

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None) -> typing_extensions.Self:
        property_size = None  # Atomic
        property_count = structs.BIG_L.unpack(data.read(4))[0]
        name = b"".join(iter(lambda: data.read(1), b'\x00')).decode("utf-8", errors="surrogateescape")
        position = Vector.from_stream(data, game, property_size)
        rotation = Vector.from_stream(data, game, property_size)
        scale = Vector.from_stream(data, game, property_size)
        unnamed_0x00000004 = PatternedAITypedef.from_stream(data, game, property_size)
        unnamed_0x00000005 = ActorParameters.from_stream(data, game, property_size)
        hearing_radius = structs.BIG_f.unpack(data.read(4))[0]
        fade_out_delay = structs.BIG_f.unpack(data.read(4))[0]
        attack_delay = structs.BIG_f.unpack(data.read(4))[0]
        freeze_time = structs.BIG_f.unpack(data.read(4))[0]
        hand_blast = structs.BIG_L.unpack(data.read(4))[0]
        hand_blast_damage = DamageInfo.from_stream(data, game, property_size)
        powerball = structs.BIG_L.unpack(data.read(4))[0]
        powerball_damage = DamageInfo.from_stream(data, game, property_size)
        far = BehaveChance.from_stream(data, game, property_size)
        mid = BehaveChance.from_stream(data, game, property_size)
        near = BehaveChance.from_stream(data, game, property_size)
        sound_impact = structs.BIG_l.unpack(data.read(4))[0]
        disable_player_gun_time = structs.BIG_f.unpack(data.read(4))[0]
        sound_phaze_in = structs.BIG_l.unpack(data.read(4))[0]
        sound_phaze_out = structs.BIG_l.unpack(data.read(4))[0]
        unknown = structs.BIG_l.unpack(data.read(4))[0]
        projectile_stop_homing_range = structs.BIG_f.unpack(data.read(4))[0]
        start_style = structs.BIG_l.unpack(data.read(4))[0]
        hurl_recover_time = structs.BIG_f.unpack(data.read(4))[0]
        projectile_visor_effect = structs.BIG_L.unpack(data.read(4))[0]
        sound_projectile_visor = structs.BIG_l.unpack(data.read(4))[0]
        near_to_mid_distance = structs.BIG_f.unpack(data.read(4))[0]
        mid_to_far_distance = structs.BIG_f.unpack(data.read(4))[0]
        near_chance = structs.BIG_l.unpack(data.read(4))[0]
        mid_chance = structs.BIG_l.unpack(data.read(4))[0]
        return cls(name, position, rotation, scale, unnamed_0x00000004, unnamed_0x00000005, hearing_radius, fade_out_delay, attack_delay, freeze_time, hand_blast, hand_blast_damage, powerball, powerball_damage, far, mid, near, sound_impact, disable_player_gun_time, sound_phaze_in, sound_phaze_out, unknown, projectile_stop_homing_range, start_style, hurl_recover_time, projectile_visor_effect, sound_projectile_visor, near_to_mid_distance, mid_to_far_distance, near_chance, mid_chance)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x00\x00\x1f')  # 31 properties
        data.write(self.name.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        self.position.to_stream(data, game)
        self.rotation.to_stream(data, game)
        self.scale.to_stream(data, game)
        self.unnamed_0x00000004.to_stream(data, game)
        self.unnamed_0x00000005.to_stream(data, game)
        data.write(structs.BIG_f.pack(self.hearing_radius))
        data.write(structs.BIG_f.pack(self.fade_out_delay))
        data.write(structs.BIG_f.pack(self.attack_delay))
        data.write(structs.BIG_f.pack(self.freeze_time))
        data.write(structs.BIG_L.pack(self.hand_blast))
        self.hand_blast_damage.to_stream(data, game)
        data.write(structs.BIG_L.pack(self.powerball))
        self.powerball_damage.to_stream(data, game)
        self.far.to_stream(data, game)
        self.mid.to_stream(data, game)
        self.near.to_stream(data, game)
        data.write(structs.BIG_l.pack(self.sound_impact))
        data.write(structs.BIG_f.pack(self.disable_player_gun_time))
        data.write(structs.BIG_l.pack(self.sound_phaze_in))
        data.write(structs.BIG_l.pack(self.sound_phaze_out))
        data.write(structs.BIG_l.pack(self.unknown))
        data.write(structs.BIG_f.pack(self.projectile_stop_homing_range))
        data.write(structs.BIG_l.pack(self.start_style))
        data.write(structs.BIG_f.pack(self.hurl_recover_time))
        data.write(structs.BIG_L.pack(self.projectile_visor_effect))
        data.write(structs.BIG_l.pack(self.sound_projectile_visor))
        data.write(structs.BIG_f.pack(self.near_to_mid_distance))
        data.write(structs.BIG_f.pack(self.mid_to_far_distance))
        data.write(structs.BIG_l.pack(self.near_chance))
        data.write(structs.BIG_l.pack(self.mid_chance))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ChozoGhostJson", data)
        return cls(
            name=json_data['name'],
            position=Vector.from_json(json_data['position']),
            rotation=Vector.from_json(json_data['rotation']),
            scale=Vector.from_json(json_data['scale']),
            unnamed_0x00000004=PatternedAITypedef.from_json(json_data['unnamed_0x00000004']),
            unnamed_0x00000005=ActorParameters.from_json(json_data['unnamed_0x00000005']),
            hearing_radius=json_data['hearing_radius'],
            fade_out_delay=json_data['fade_out_delay'],
            attack_delay=json_data['attack_delay'],
            freeze_time=json_data['freeze_time'],
            hand_blast=json_data['hand_blast'],
            hand_blast_damage=DamageInfo.from_json(json_data['hand_blast_damage']),
            powerball=json_data['powerball'],
            powerball_damage=DamageInfo.from_json(json_data['powerball_damage']),
            far=BehaveChance.from_json(json_data['far']),
            mid=BehaveChance.from_json(json_data['mid']),
            near=BehaveChance.from_json(json_data['near']),
            sound_impact=json_data['sound_impact'],
            disable_player_gun_time=json_data['disable_player_gun_time'],
            sound_phaze_in=json_data['sound_phaze_in'],
            sound_phaze_out=json_data['sound_phaze_out'],
            unknown=json_data['unknown'],
            projectile_stop_homing_range=json_data['projectile_stop_homing_range'],
            start_style=json_data['start_style'],
            hurl_recover_time=json_data['hurl_recover_time'],
            projectile_visor_effect=json_data['projectile_visor_effect'],
            sound_projectile_visor=json_data['sound_projectile_visor'],
            near_to_mid_distance=json_data['near_to_mid_distance'],
            mid_to_far_distance=json_data['mid_to_far_distance'],
            near_chance=json_data['near_chance'],
            mid_chance=json_data['mid_chance'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'name': self.name,
            'position': self.position.to_json(),
            'rotation': self.rotation.to_json(),
            'scale': self.scale.to_json(),
            'unnamed_0x00000004': self.unnamed_0x00000004.to_json(),
            'unnamed_0x00000005': self.unnamed_0x00000005.to_json(),
            'hearing_radius': self.hearing_radius,
            'fade_out_delay': self.fade_out_delay,
            'attack_delay': self.attack_delay,
            'freeze_time': self.freeze_time,
            'hand_blast': self.hand_blast,
            'hand_blast_damage': self.hand_blast_damage.to_json(),
            'powerball': self.powerball,
            'powerball_damage': self.powerball_damage.to_json(),
            'far': self.far.to_json(),
            'mid': self.mid.to_json(),
            'near': self.near.to_json(),
            'sound_impact': self.sound_impact,
            'disable_player_gun_time': self.disable_player_gun_time,
            'sound_phaze_in': self.sound_phaze_in,
            'sound_phaze_out': self.sound_phaze_out,
            'unknown': self.unknown,
            'projectile_stop_homing_range': self.projectile_stop_homing_range,
            'start_style': self.start_style,
            'hurl_recover_time': self.hurl_recover_time,
            'projectile_visor_effect': self.projectile_visor_effect,
            'sound_projectile_visor': self.sound_projectile_visor,
            'near_to_mid_distance': self.near_to_mid_distance,
            'mid_to_far_distance': self.mid_to_far_distance,
            'near_chance': self.near_chance,
            'mid_chance': self.mid_chance,
        }

    def _dependencies_for_hand_blast(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.hand_blast)

    def _dependencies_for_powerball(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.powerball)

    def _dependencies_for_sound_impact(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_impact)

    def _dependencies_for_sound_phaze_in(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_phaze_in)

    def _dependencies_for_sound_phaze_out(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_phaze_out)

    def _dependencies_for_projectile_visor_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile_visor_effect)

    def _dependencies_for_sound_projectile_visor(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_projectile_visor)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unnamed_0x00000004.dependencies_for, "unnamed_0x00000004", "PatternedAITypedef"),
            (self.unnamed_0x00000005.dependencies_for, "unnamed_0x00000005", "ActorParameters"),
            (self._dependencies_for_hand_blast, "hand_blast", "AssetId"),
            (self._dependencies_for_powerball, "powerball", "AssetId"),
            (self._dependencies_for_sound_impact, "sound_impact", "int"),
            (self._dependencies_for_sound_phaze_in, "sound_phaze_in", "int"),
            (self._dependencies_for_sound_phaze_out, "sound_phaze_out", "int"),
            (self._dependencies_for_projectile_visor_effect, "projectile_visor_effect", "AssetId"),
            (self._dependencies_for_sound_projectile_visor, "sound_projectile_visor", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for ChozoGhost.{field_name} ({field_type}): {e}"
                )
