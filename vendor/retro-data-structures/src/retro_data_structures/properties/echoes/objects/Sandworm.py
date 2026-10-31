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
from retro_data_structures.properties.echoes.archetypes.IngPossessionData import IngPossessionData
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.archetypes.SandwormAttackSequence import SandwormAttackSequence
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SandwormJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        unknown_0x06dee4c5: int
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        pincer_scale: float
        walk_sound: int
        walk_vocal_sound: int
        melee_attack_sound: int
        eye_killed_sound: int
        pincer_l: int
        pincer_r: int
        spit_attack_min_range: float
        spit_attack_max_range: float
        spit_attack_visor_effect: int
        max_spit_angle_degrees: float
        charge_range_min: float
        charge_range_max: float
        projectile: int
        projectile_damage: json_util.JsonObject
        charge_impulse_horizontal: float
        charge_impulse_vertical: float
        morphball_toss_impulse_horizontal: float
        morphball_toss_impulse_vertical: float
        melee_impulse_horizontal: float
        melee_impulse_vertical: float
        morphball_toss_damage: json_util.JsonObject
        pincer_swipe_damage: json_util.JsonObject
        percent_damage_before_sulking: float
        lurk_underground_time_min: float
        lurk_underground_time_max: float
        pursuit_frustration_timer: float
        pursuit_frustration_radius: float
        can_link_transfer: bool
        eye_glow: int
        part_0x3221407e: int
        part_0x8b2a15ee: int
        ing_boss_bomb_fx: int
        ing_boss_bomb_explosion_fx: int
        ing_boss_bomb_damage: json_util.JsonObject
        ing_boss_bomb_drop_rate: float
        bomb_bounce_sound: int
        bomb_explode_sound: int
        unknown_0x547f9400: float
        unknown_0xefef7b45: float
        bomb_boss_attack_sequence1: json_util.JsonObject
        bomb_boss_attack_sequence2: json_util.JsonObject
        bomb_boss_attack_sequence3: json_util.JsonObject
        bomb_boss_attack_sequence4: json_util.JsonObject
        bomb_boss_attack_sequence5: json_util.JsonObject
        ing_possession_data: json_util.JsonObject
    

@dataclasses.dataclass()
class Sandworm(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    unknown_0x06dee4c5: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x06dee4c5, original_name='Unknown'
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
    pincer_scale: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3db583ae, original_name='PincerScale'
        ),
    })
    walk_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xa24376ec, original_name='WalkSound'
        ),
    })
    walk_vocal_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xd35eb69d, original_name='WalkVocalSound'
        ),
    })
    melee_attack_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xaadaabb8, original_name='MeleeAttackSound'
        ),
    })
    eye_killed_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x8128ce4a, original_name='EyeKilledSound'
        ),
    })
    pincer_l: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x66e34a08, original_name='PincerL'
        ),
    })
    pincer_r: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5f3f29e3, original_name='PincerR'
        ),
    })
    spit_attack_min_range: float = dataclasses.field(default=9.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x63dcbbb6, original_name='SpitAttackMinRange'
        ),
    })
    spit_attack_max_range: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2393c3c0, original_name='SpitAttackMaxRange'
        ),
    })
    spit_attack_visor_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xf9469e49, original_name='SpitAttackVisorEffect'
        ),
    })
    max_spit_angle_degrees: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x61f75902, original_name='MaxSpitAngleDegrees'
        ),
    })
    charge_range_min: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2a7446ee, original_name='ChargeRangeMin'
        ),
    })
    charge_range_max: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcc14e90f, original_name='ChargeRangeMax'
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
    charge_impulse_horizontal: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x12090da8, original_name='ChargeImpulseHorizontal'
        ),
    })
    charge_impulse_vertical: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc07bbe9a, original_name='ChargeImpulseVertical'
        ),
    })
    morphball_toss_impulse_horizontal: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2b053901, original_name='MorphballTossImpulseHorizontal'
        ),
    })
    morphball_toss_impulse_vertical: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x47e969d3, original_name='MorphballTossImpulseVertical'
        ),
    })
    melee_impulse_horizontal: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb8eecc95, original_name='MeleeImpulseHorizontal'
        ),
    })
    melee_impulse_vertical: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf59af01a, original_name='MeleeImpulseVertical'
        ),
    })
    morphball_toss_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xf8fd6885, original_name='MorphballTossDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    pincer_swipe_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x449233bc, original_name='PincerSwipeDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    percent_damage_before_sulking: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe593f1c6, original_name='PercentDamageBeforeSulking'
        ),
    })
    lurk_underground_time_min: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3c5d53a4, original_name='LurkUndergroundTimeMin'
        ),
    })
    lurk_underground_time_max: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xda3dfc45, original_name='LurkUndergroundTimeMax'
        ),
    })
    pursuit_frustration_timer: float = dataclasses.field(default=6.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdfa46e80, original_name='PursuitFrustrationTimer'
        ),
    })
    pursuit_frustration_radius: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x49f36a3f, original_name='PursuitFrustrationRadius'
        ),
    })
    can_link_transfer: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xb47dd18f, original_name='CanLinkTransfer'
        ),
    })
    eye_glow: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x0ca82d3c, original_name='EyeGlow'
        ),
    })
    part_0x3221407e: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3221407e, original_name='PART'
        ),
    })
    part_0x8b2a15ee: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x8b2a15ee, original_name='PART'
        ),
    })
    ing_boss_bomb_fx: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x526c6956, original_name='IngBossBombFX'
        ),
    })
    ing_boss_bomb_explosion_fx: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd24a1751, original_name='IngBossBombExplosionFX'
        ),
    })
    ing_boss_bomb_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x4461a8ad, original_name='IngBossBombDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    ing_boss_bomb_drop_rate: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3d58f51f, original_name='IngBossBombDropRate'
        ),
    })
    bomb_bounce_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x8c41066c, original_name='BombBounceSound'
        ),
    })
    bomb_explode_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x8649fe53, original_name='BombExplodeSound'
        ),
    })
    unknown_0x547f9400: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x547f9400, original_name='Unknown'
        ),
    })
    unknown_0xefef7b45: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xefef7b45, original_name='Unknown'
        ),
    })
    bomb_boss_attack_sequence1: SandwormAttackSequence = dataclasses.field(default_factory=SandwormAttackSequence, metadata={
        'reflection': FieldReflection[SandwormAttackSequence](
            SandwormAttackSequence, id=0xb8c15f15, original_name='BombBossAttackSequence1', from_json=SandwormAttackSequence.from_json, to_json=SandwormAttackSequence.to_json
        ),
    })
    bomb_boss_attack_sequence2: SandwormAttackSequence = dataclasses.field(default_factory=SandwormAttackSequence, metadata={
        'reflection': FieldReflection[SandwormAttackSequence](
            SandwormAttackSequence, id=0xce246628, original_name='BombBossAttackSequence2', from_json=SandwormAttackSequence.from_json, to_json=SandwormAttackSequence.to_json
        ),
    })
    bomb_boss_attack_sequence3: SandwormAttackSequence = dataclasses.field(default_factory=SandwormAttackSequence, metadata={
        'reflection': FieldReflection[SandwormAttackSequence](
            SandwormAttackSequence, id=0x55578cfc, original_name='BombBossAttackSequence3', from_json=SandwormAttackSequence.from_json, to_json=SandwormAttackSequence.to_json
        ),
    })
    bomb_boss_attack_sequence4: SandwormAttackSequence = dataclasses.field(default_factory=SandwormAttackSequence, metadata={
        'reflection': FieldReflection[SandwormAttackSequence](
            SandwormAttackSequence, id=0x23ee1452, original_name='BombBossAttackSequence4', from_json=SandwormAttackSequence.from_json, to_json=SandwormAttackSequence.to_json
        ),
    })
    bomb_boss_attack_sequence5: SandwormAttackSequence = dataclasses.field(default_factory=SandwormAttackSequence, metadata={
        'reflection': FieldReflection[SandwormAttackSequence](
            SandwormAttackSequence, id=0xb89dfe86, original_name='BombBossAttackSequence5', from_json=SandwormAttackSequence.from_json, to_json=SandwormAttackSequence.to_json
        ),
    })
    ing_possession_data: IngPossessionData = dataclasses.field(default_factory=IngPossessionData, metadata={
        'reflection': FieldReflection[IngPossessionData](
            IngPossessionData, id=0xe61748ed, original_name='IngPossessionData', from_json=IngPossessionData.from_json, to_json=IngPossessionData.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'WORM'

    @classmethod
    def modules(cls) -> list[str]:
        return ['Sandworm.rel']

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
        if property_count != 50:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x06dee4c5
        unknown_0x06dee4c5 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size, default_override={'detection_range': 32.0, 'collision_radius': 0.5, 'collision_height': 1.0, 'creature_size': 2})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3db583ae
        pincer_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa24376ec
        walk_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd35eb69d
        walk_vocal_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaadaabb8
        melee_attack_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8128ce4a
        eye_killed_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x66e34a08
        pincer_l = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5f3f29e3
        pincer_r = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x63dcbbb6
        spit_attack_min_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2393c3c0
        spit_attack_max_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf9469e49
        spit_attack_visor_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x61f75902
        max_spit_angle_degrees = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2a7446ee
        charge_range_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcc14e90f
        charge_range_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xef485db9
        projectile = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x553b1339
        projectile_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x12090da8
        charge_impulse_horizontal = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc07bbe9a
        charge_impulse_vertical = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2b053901
        morphball_toss_impulse_horizontal = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47e969d3
        morphball_toss_impulse_vertical = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb8eecc95
        melee_impulse_horizontal = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf59af01a
        melee_impulse_vertical = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf8fd6885
        morphball_toss_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x449233bc
        pincer_swipe_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe593f1c6
        percent_damage_before_sulking = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3c5d53a4
        lurk_underground_time_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xda3dfc45
        lurk_underground_time_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdfa46e80
        pursuit_frustration_timer = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49f36a3f
        pursuit_frustration_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb47dd18f
        can_link_transfer = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0ca82d3c
        eye_glow = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3221407e
        part_0x3221407e = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8b2a15ee
        part_0x8b2a15ee = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x526c6956
        ing_boss_bomb_fx = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd24a1751
        ing_boss_bomb_explosion_fx = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4461a8ad
        ing_boss_bomb_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3d58f51f
        ing_boss_bomb_drop_rate = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8c41066c
        bomb_bounce_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8649fe53
        bomb_explode_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x547f9400
        unknown_0x547f9400 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xefef7b45
        unknown_0xefef7b45 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb8c15f15
        bomb_boss_attack_sequence1 = SandwormAttackSequence.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xce246628
        bomb_boss_attack_sequence2 = SandwormAttackSequence.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x55578cfc
        bomb_boss_attack_sequence3 = SandwormAttackSequence.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23ee1452
        bomb_boss_attack_sequence4 = SandwormAttackSequence.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb89dfe86
        bomb_boss_attack_sequence5 = SandwormAttackSequence.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe61748ed
        ing_possession_data = IngPossessionData.from_stream(data, game, property_size)
    
        return cls(editor_properties, unknown_0x06dee4c5, patterned, actor_information, pincer_scale, walk_sound, walk_vocal_sound, melee_attack_sound, eye_killed_sound, pincer_l, pincer_r, spit_attack_min_range, spit_attack_max_range, spit_attack_visor_effect, max_spit_angle_degrees, charge_range_min, charge_range_max, projectile, projectile_damage, charge_impulse_horizontal, charge_impulse_vertical, morphball_toss_impulse_horizontal, morphball_toss_impulse_vertical, melee_impulse_horizontal, melee_impulse_vertical, morphball_toss_damage, pincer_swipe_damage, percent_damage_before_sulking, lurk_underground_time_min, lurk_underground_time_max, pursuit_frustration_timer, pursuit_frustration_radius, can_link_transfer, eye_glow, part_0x3221407e, part_0x8b2a15ee, ing_boss_bomb_fx, ing_boss_bomb_explosion_fx, ing_boss_bomb_damage, ing_boss_bomb_drop_rate, bomb_bounce_sound, bomb_explode_sound, unknown_0x547f9400, unknown_0xefef7b45, bomb_boss_attack_sequence1, bomb_boss_attack_sequence2, bomb_boss_attack_sequence3, bomb_boss_attack_sequence4, bomb_boss_attack_sequence5, ing_possession_data)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x002')  # 50 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game, default_override={'misc_flags': 3})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x06\xde\xe4\xc5')  # 0x6dee4c5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x06dee4c5))

        data.write(b'\xb3wGP')  # 0xb3774750
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.patterned.to_stream(data, game, default_override={'detection_range': 32.0, 'collision_radius': 0.5, 'collision_height': 1.0, 'creature_size': 2})
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

        data.write(b'=\xb5\x83\xae')  # 0x3db583ae
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.pincer_scale))

        data.write(b'\xa2Cv\xec')  # 0xa24376ec
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.walk_sound))

        data.write(b'\xd3^\xb6\x9d')  # 0xd35eb69d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.walk_vocal_sound))

        data.write(b'\xaa\xda\xab\xb8')  # 0xaadaabb8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.melee_attack_sound))

        data.write(b'\x81(\xceJ')  # 0x8128ce4a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.eye_killed_sound))

        data.write(b'f\xe3J\x08')  # 0x66e34a08
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.pincer_l))

        data.write(b'_?)\xe3')  # 0x5f3f29e3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.pincer_r))

        data.write(b'c\xdc\xbb\xb6')  # 0x63dcbbb6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.spit_attack_min_range))

        data.write(b'#\x93\xc3\xc0')  # 0x2393c3c0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.spit_attack_max_range))

        data.write(b'\xf9F\x9eI')  # 0xf9469e49
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.spit_attack_visor_effect))

        data.write(b'a\xf7Y\x02')  # 0x61f75902
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_spit_angle_degrees))

        data.write(b'*tF\xee')  # 0x2a7446ee
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_range_min))

        data.write(b'\xcc\x14\xe9\x0f')  # 0xcc14e90f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_range_max))

        data.write(b'\xefH]\xb9')  # 0xef485db9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.projectile))

        data.write(b'U;\x139')  # 0x553b1339
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.projectile_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x12\t\r\xa8')  # 0x12090da8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_impulse_horizontal))

        data.write(b'\xc0{\xbe\x9a')  # 0xc07bbe9a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_impulse_vertical))

        data.write(b'+\x059\x01')  # 0x2b053901
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.morphball_toss_impulse_horizontal))

        data.write(b'G\xe9i\xd3')  # 0x47e969d3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.morphball_toss_impulse_vertical))

        data.write(b'\xb8\xee\xcc\x95')  # 0xb8eecc95
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.melee_impulse_horizontal))

        data.write(b'\xf5\x9a\xf0\x1a')  # 0xf59af01a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.melee_impulse_vertical))

        data.write(b'\xf8\xfdh\x85')  # 0xf8fd6885
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.morphball_toss_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'D\x923\xbc')  # 0x449233bc
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.pincer_swipe_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe5\x93\xf1\xc6')  # 0xe593f1c6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.percent_damage_before_sulking))

        data.write(b'<]S\xa4')  # 0x3c5d53a4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.lurk_underground_time_min))

        data.write(b'\xda=\xfcE')  # 0xda3dfc45
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.lurk_underground_time_max))

        data.write(b'\xdf\xa4n\x80')  # 0xdfa46e80
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.pursuit_frustration_timer))

        data.write(b'I\xf3j?')  # 0x49f36a3f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.pursuit_frustration_radius))

        data.write(b'\xb4}\xd1\x8f')  # 0xb47dd18f
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.can_link_transfer))

        data.write(b'\x0c\xa8-<')  # 0xca82d3c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.eye_glow))

        data.write(b'2!@~')  # 0x3221407e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.part_0x3221407e))

        data.write(b'\x8b*\x15\xee')  # 0x8b2a15ee
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.part_0x8b2a15ee))

        data.write(b'RliV')  # 0x526c6956
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.ing_boss_bomb_fx))

        data.write(b'\xd2J\x17Q')  # 0xd24a1751
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.ing_boss_bomb_explosion_fx))

        data.write(b'Da\xa8\xad')  # 0x4461a8ad
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ing_boss_bomb_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'=X\xf5\x1f')  # 0x3d58f51f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ing_boss_bomb_drop_rate))

        data.write(b'\x8cA\x06l')  # 0x8c41066c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.bomb_bounce_sound))

        data.write(b'\x86I\xfeS')  # 0x8649fe53
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.bomb_explode_sound))

        data.write(b'T\x7f\x94\x00')  # 0x547f9400
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x547f9400))

        data.write(b'\xef\xef{E')  # 0xefef7b45
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xefef7b45))

        data.write(b'\xb8\xc1_\x15')  # 0xb8c15f15
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.bomb_boss_attack_sequence1.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xce$f(')  # 0xce246628
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.bomb_boss_attack_sequence2.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'UW\x8c\xfc')  # 0x55578cfc
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.bomb_boss_attack_sequence3.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'#\xee\x14R')  # 0x23ee1452
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.bomb_boss_attack_sequence4.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb8\x9d\xfe\x86')  # 0xb89dfe86
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.bomb_boss_attack_sequence5.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe6\x17H\xed')  # 0xe61748ed
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ing_possession_data.to_stream(data, game)
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
        json_data = typing.cast("SandwormJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            unknown_0x06dee4c5=json_data['unknown_0x06dee4c5'],
            patterned=PatternedAITypedef.from_json(json_data['patterned']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
            pincer_scale=json_data['pincer_scale'],
            walk_sound=json_data['walk_sound'],
            walk_vocal_sound=json_data['walk_vocal_sound'],
            melee_attack_sound=json_data['melee_attack_sound'],
            eye_killed_sound=json_data['eye_killed_sound'],
            pincer_l=json_data['pincer_l'],
            pincer_r=json_data['pincer_r'],
            spit_attack_min_range=json_data['spit_attack_min_range'],
            spit_attack_max_range=json_data['spit_attack_max_range'],
            spit_attack_visor_effect=json_data['spit_attack_visor_effect'],
            max_spit_angle_degrees=json_data['max_spit_angle_degrees'],
            charge_range_min=json_data['charge_range_min'],
            charge_range_max=json_data['charge_range_max'],
            projectile=json_data['projectile'],
            projectile_damage=DamageInfo.from_json(json_data['projectile_damage']),
            charge_impulse_horizontal=json_data['charge_impulse_horizontal'],
            charge_impulse_vertical=json_data['charge_impulse_vertical'],
            morphball_toss_impulse_horizontal=json_data['morphball_toss_impulse_horizontal'],
            morphball_toss_impulse_vertical=json_data['morphball_toss_impulse_vertical'],
            melee_impulse_horizontal=json_data['melee_impulse_horizontal'],
            melee_impulse_vertical=json_data['melee_impulse_vertical'],
            morphball_toss_damage=DamageInfo.from_json(json_data['morphball_toss_damage']),
            pincer_swipe_damage=DamageInfo.from_json(json_data['pincer_swipe_damage']),
            percent_damage_before_sulking=json_data['percent_damage_before_sulking'],
            lurk_underground_time_min=json_data['lurk_underground_time_min'],
            lurk_underground_time_max=json_data['lurk_underground_time_max'],
            pursuit_frustration_timer=json_data['pursuit_frustration_timer'],
            pursuit_frustration_radius=json_data['pursuit_frustration_radius'],
            can_link_transfer=json_data['can_link_transfer'],
            eye_glow=json_data['eye_glow'],
            part_0x3221407e=json_data['part_0x3221407e'],
            part_0x8b2a15ee=json_data['part_0x8b2a15ee'],
            ing_boss_bomb_fx=json_data['ing_boss_bomb_fx'],
            ing_boss_bomb_explosion_fx=json_data['ing_boss_bomb_explosion_fx'],
            ing_boss_bomb_damage=DamageInfo.from_json(json_data['ing_boss_bomb_damage']),
            ing_boss_bomb_drop_rate=json_data['ing_boss_bomb_drop_rate'],
            bomb_bounce_sound=json_data['bomb_bounce_sound'],
            bomb_explode_sound=json_data['bomb_explode_sound'],
            unknown_0x547f9400=json_data['unknown_0x547f9400'],
            unknown_0xefef7b45=json_data['unknown_0xefef7b45'],
            bomb_boss_attack_sequence1=SandwormAttackSequence.from_json(json_data['bomb_boss_attack_sequence1']),
            bomb_boss_attack_sequence2=SandwormAttackSequence.from_json(json_data['bomb_boss_attack_sequence2']),
            bomb_boss_attack_sequence3=SandwormAttackSequence.from_json(json_data['bomb_boss_attack_sequence3']),
            bomb_boss_attack_sequence4=SandwormAttackSequence.from_json(json_data['bomb_boss_attack_sequence4']),
            bomb_boss_attack_sequence5=SandwormAttackSequence.from_json(json_data['bomb_boss_attack_sequence5']),
            ing_possession_data=IngPossessionData.from_json(json_data['ing_possession_data']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'unknown_0x06dee4c5': self.unknown_0x06dee4c5,
            'patterned': self.patterned.to_json(),
            'actor_information': self.actor_information.to_json(),
            'pincer_scale': self.pincer_scale,
            'walk_sound': self.walk_sound,
            'walk_vocal_sound': self.walk_vocal_sound,
            'melee_attack_sound': self.melee_attack_sound,
            'eye_killed_sound': self.eye_killed_sound,
            'pincer_l': self.pincer_l,
            'pincer_r': self.pincer_r,
            'spit_attack_min_range': self.spit_attack_min_range,
            'spit_attack_max_range': self.spit_attack_max_range,
            'spit_attack_visor_effect': self.spit_attack_visor_effect,
            'max_spit_angle_degrees': self.max_spit_angle_degrees,
            'charge_range_min': self.charge_range_min,
            'charge_range_max': self.charge_range_max,
            'projectile': self.projectile,
            'projectile_damage': self.projectile_damage.to_json(),
            'charge_impulse_horizontal': self.charge_impulse_horizontal,
            'charge_impulse_vertical': self.charge_impulse_vertical,
            'morphball_toss_impulse_horizontal': self.morphball_toss_impulse_horizontal,
            'morphball_toss_impulse_vertical': self.morphball_toss_impulse_vertical,
            'melee_impulse_horizontal': self.melee_impulse_horizontal,
            'melee_impulse_vertical': self.melee_impulse_vertical,
            'morphball_toss_damage': self.morphball_toss_damage.to_json(),
            'pincer_swipe_damage': self.pincer_swipe_damage.to_json(),
            'percent_damage_before_sulking': self.percent_damage_before_sulking,
            'lurk_underground_time_min': self.lurk_underground_time_min,
            'lurk_underground_time_max': self.lurk_underground_time_max,
            'pursuit_frustration_timer': self.pursuit_frustration_timer,
            'pursuit_frustration_radius': self.pursuit_frustration_radius,
            'can_link_transfer': self.can_link_transfer,
            'eye_glow': self.eye_glow,
            'part_0x3221407e': self.part_0x3221407e,
            'part_0x8b2a15ee': self.part_0x8b2a15ee,
            'ing_boss_bomb_fx': self.ing_boss_bomb_fx,
            'ing_boss_bomb_explosion_fx': self.ing_boss_bomb_explosion_fx,
            'ing_boss_bomb_damage': self.ing_boss_bomb_damage.to_json(),
            'ing_boss_bomb_drop_rate': self.ing_boss_bomb_drop_rate,
            'bomb_bounce_sound': self.bomb_bounce_sound,
            'bomb_explode_sound': self.bomb_explode_sound,
            'unknown_0x547f9400': self.unknown_0x547f9400,
            'unknown_0xefef7b45': self.unknown_0xefef7b45,
            'bomb_boss_attack_sequence1': self.bomb_boss_attack_sequence1.to_json(),
            'bomb_boss_attack_sequence2': self.bomb_boss_attack_sequence2.to_json(),
            'bomb_boss_attack_sequence3': self.bomb_boss_attack_sequence3.to_json(),
            'bomb_boss_attack_sequence4': self.bomb_boss_attack_sequence4.to_json(),
            'bomb_boss_attack_sequence5': self.bomb_boss_attack_sequence5.to_json(),
            'ing_possession_data': self.ing_possession_data.to_json(),
        }

    def _dependencies_for_walk_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.walk_sound)

    def _dependencies_for_walk_vocal_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.walk_vocal_sound)

    def _dependencies_for_melee_attack_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.melee_attack_sound)

    def _dependencies_for_eye_killed_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.eye_killed_sound)

    def _dependencies_for_pincer_l(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.pincer_l)

    def _dependencies_for_pincer_r(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.pincer_r)

    def _dependencies_for_spit_attack_visor_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.spit_attack_visor_effect)

    def _dependencies_for_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile)

    def _dependencies_for_eye_glow(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.eye_glow)

    def _dependencies_for_part_0x3221407e(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0x3221407e)

    def _dependencies_for_part_0x8b2a15ee(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0x8b2a15ee)

    def _dependencies_for_ing_boss_bomb_fx(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ing_boss_bomb_fx)

    def _dependencies_for_ing_boss_bomb_explosion_fx(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ing_boss_bomb_explosion_fx)

    def _dependencies_for_bomb_bounce_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.bomb_bounce_sound)

    def _dependencies_for_bomb_explode_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.bomb_explode_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_walk_sound, "walk_sound", "int"),
            (self._dependencies_for_walk_vocal_sound, "walk_vocal_sound", "int"),
            (self._dependencies_for_melee_attack_sound, "melee_attack_sound", "int"),
            (self._dependencies_for_eye_killed_sound, "eye_killed_sound", "int"),
            (self._dependencies_for_pincer_l, "pincer_l", "AssetId"),
            (self._dependencies_for_pincer_r, "pincer_r", "AssetId"),
            (self._dependencies_for_spit_attack_visor_effect, "spit_attack_visor_effect", "AssetId"),
            (self._dependencies_for_projectile, "projectile", "AssetId"),
            (self._dependencies_for_eye_glow, "eye_glow", "AssetId"),
            (self._dependencies_for_part_0x3221407e, "part_0x3221407e", "AssetId"),
            (self._dependencies_for_part_0x8b2a15ee, "part_0x8b2a15ee", "AssetId"),
            (self._dependencies_for_ing_boss_bomb_fx, "ing_boss_bomb_fx", "AssetId"),
            (self._dependencies_for_ing_boss_bomb_explosion_fx, "ing_boss_bomb_explosion_fx", "AssetId"),
            (self._dependencies_for_bomb_bounce_sound, "bomb_bounce_sound", "int"),
            (self._dependencies_for_bomb_explode_sound, "bomb_explode_sound", "int"),
            (self.ing_possession_data.dependencies_for, "ing_possession_data", "IngPossessionData"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for Sandworm.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={'detection_range': 32.0, 'collision_radius': 0.5, 'collision_height': 1.0, 'creature_size': 2})


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0})


def _decode_morphball_toss_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0})


def _decode_pincer_swipe_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0})


def _decode_ing_boss_bomb_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0})


def _decode_bomb_boss_attack_sequence1(data: typing.BinaryIO, game: Game, property_size: int) -> SandwormAttackSequence:
    return SandwormAttackSequence.from_stream(data, game, property_size)


def _decode_bomb_boss_attack_sequence2(data: typing.BinaryIO, game: Game, property_size: int) -> SandwormAttackSequence:
    return SandwormAttackSequence.from_stream(data, game, property_size)


def _decode_bomb_boss_attack_sequence3(data: typing.BinaryIO, game: Game, property_size: int) -> SandwormAttackSequence:
    return SandwormAttackSequence.from_stream(data, game, property_size)


def _decode_bomb_boss_attack_sequence4(data: typing.BinaryIO, game: Game, property_size: int) -> SandwormAttackSequence:
    return SandwormAttackSequence.from_stream(data, game, property_size)


def _decode_bomb_boss_attack_sequence5(data: typing.BinaryIO, game: Game, property_size: int) -> SandwormAttackSequence:
    return SandwormAttackSequence.from_stream(data, game, property_size)


def _decode_ing_possession_data(data: typing.BinaryIO, game: Game, property_size: int) -> IngPossessionData:
    return IngPossessionData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0x06dee4c5: ('unknown_0x06dee4c5', structs.decode_BIG_l),
    0xb3774750: ('patterned', _decode_patterned),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0x3db583ae: ('pincer_scale', structs.decode_BIG_f),
    0xa24376ec: ('walk_sound', structs.decode_BIG_l),
    0xd35eb69d: ('walk_vocal_sound', structs.decode_BIG_l),
    0xaadaabb8: ('melee_attack_sound', structs.decode_BIG_l),
    0x8128ce4a: ('eye_killed_sound', structs.decode_BIG_l),
    0x66e34a08: ('pincer_l', structs.decode_BIG_L),
    0x5f3f29e3: ('pincer_r', structs.decode_BIG_L),
    0x63dcbbb6: ('spit_attack_min_range', structs.decode_BIG_f),
    0x2393c3c0: ('spit_attack_max_range', structs.decode_BIG_f),
    0xf9469e49: ('spit_attack_visor_effect', structs.decode_BIG_L),
    0x61f75902: ('max_spit_angle_degrees', structs.decode_BIG_f),
    0x2a7446ee: ('charge_range_min', structs.decode_BIG_f),
    0xcc14e90f: ('charge_range_max', structs.decode_BIG_f),
    0xef485db9: ('projectile', structs.decode_BIG_L),
    0x553b1339: ('projectile_damage', _decode_projectile_damage),
    0x12090da8: ('charge_impulse_horizontal', structs.decode_BIG_f),
    0xc07bbe9a: ('charge_impulse_vertical', structs.decode_BIG_f),
    0x2b053901: ('morphball_toss_impulse_horizontal', structs.decode_BIG_f),
    0x47e969d3: ('morphball_toss_impulse_vertical', structs.decode_BIG_f),
    0xb8eecc95: ('melee_impulse_horizontal', structs.decode_BIG_f),
    0xf59af01a: ('melee_impulse_vertical', structs.decode_BIG_f),
    0xf8fd6885: ('morphball_toss_damage', _decode_morphball_toss_damage),
    0x449233bc: ('pincer_swipe_damage', _decode_pincer_swipe_damage),
    0xe593f1c6: ('percent_damage_before_sulking', structs.decode_BIG_f),
    0x3c5d53a4: ('lurk_underground_time_min', structs.decode_BIG_f),
    0xda3dfc45: ('lurk_underground_time_max', structs.decode_BIG_f),
    0xdfa46e80: ('pursuit_frustration_timer', structs.decode_BIG_f),
    0x49f36a3f: ('pursuit_frustration_radius', structs.decode_BIG_f),
    0xb47dd18f: ('can_link_transfer', structs.decode_BIG_bool_),
    0x0ca82d3c: ('eye_glow', structs.decode_BIG_L),
    0x3221407e: ('part_0x3221407e', structs.decode_BIG_L),
    0x8b2a15ee: ('part_0x8b2a15ee', structs.decode_BIG_L),
    0x526c6956: ('ing_boss_bomb_fx', structs.decode_BIG_L),
    0xd24a1751: ('ing_boss_bomb_explosion_fx', structs.decode_BIG_L),
    0x4461a8ad: ('ing_boss_bomb_damage', _decode_ing_boss_bomb_damage),
    0x3d58f51f: ('ing_boss_bomb_drop_rate', structs.decode_BIG_f),
    0x8c41066c: ('bomb_bounce_sound', structs.decode_BIG_l),
    0x8649fe53: ('bomb_explode_sound', structs.decode_BIG_l),
    0x547f9400: ('unknown_0x547f9400', structs.decode_BIG_f),
    0xefef7b45: ('unknown_0xefef7b45', structs.decode_BIG_f),
    0xb8c15f15: ('bomb_boss_attack_sequence1', _decode_bomb_boss_attack_sequence1),
    0xce246628: ('bomb_boss_attack_sequence2', _decode_bomb_boss_attack_sequence2),
    0x55578cfc: ('bomb_boss_attack_sequence3', _decode_bomb_boss_attack_sequence3),
    0x23ee1452: ('bomb_boss_attack_sequence4', _decode_bomb_boss_attack_sequence4),
    0xb89dfe86: ('bomb_boss_attack_sequence5', _decode_bomb_boss_attack_sequence5),
    0xe61748ed: ('ing_possession_data', _decode_ing_possession_data),
}
