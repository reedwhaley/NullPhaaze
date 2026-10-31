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
from retro_data_structures.properties.echoes.archetypes.AudioPlaybackParms import AudioPlaybackParms
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class DarkSamusJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        health_message_threshold: float
        health_bar_initial_health_override: float
        glide_sound: int
        missile_ricochet_sound: int
        starts_in_the_air: bool
        txtr: int
        unknown_0x2c6a3344: float
        melee_attack_damage: json_util.JsonObject
        melee_attack_fx: int
        melee_attack_fx_quick: int
        dive_attack_damage: json_util.JsonObject
        dive_attack_impulse_vertical: float
        dive_attack_impulse_horizontal: float
        dive_attack_effect: int
        scatter_shot_projectile: int
        scatter_shot_projectile2: int
        scatter_shot_damage: json_util.JsonObject
        unknown_0x378285b9: float
        scatter_shot_projectiles_per_second: float
        normal_missile_projectile: int
        normal_missile_damage: json_util.JsonObject
        normal_missile_min_missiles_in_sequence: int
        normal_missile_max_missiles_in_sequence: int
        super_missile_projectile: int
        super_missile_damage: json_util.JsonObject
        freeze_beam_projectile: int
        freeze_beam_damage: json_util.JsonObject
        freeze_beam_visor_texture: int
        damage_interrupt_threshold: float
        damage_interrupt_decrease_per_second: float
        sweep_swoosh: int
        sweep_beam_damage: json_util.JsonObject
        sweep_beam_collision_effect: int
        sweep_beam_sound: int
        sweep_beam_impact_sound: int
        invulnerable_model: int
        invulnerable_skin_rules: int
        boost_ball_model: json_util.JsonObject
        boost_ball_damage: json_util.JsonObject
        boost_ball_glow: int
        boost_ball_trail_swoosh: int
        swhc: int
        boost_ball_roll_sound: int
        boost_ball_hit_player_sound: int
        boost_ball_collision: int
        boost_ball_collision_sound_one_shot: json_util.JsonObject
        ice_spread_fx: int
        ice_spread_sound: int
        big_phazon_part: int
        big_phazon_collision_part: int
        big_phazon_impact_sound: int
        big_phazon_damage_per_second: json_util.JsonObject
        inside_big_phazon_visor_effect: int
        phazon_projectile: int
        phazon_super_missile_projectile: int
        phazon_super_missile_damage: json_util.JsonObject
        phazon_projectile_damage: json_util.JsonObject
        phazon_enrage_sphere: int
        phazon_enrage_sphere_contact_damage: json_util.JsonObject
        alternate_scannable_info: int
    

@dataclasses.dataclass()
class DarkSamus(BaseObjectType):
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
    health_message_threshold: float = dataclasses.field(default=-1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x72edeb7d, original_name='HealthMessageThreshold'
        ),
    })
    health_bar_initial_health_override: float = dataclasses.field(default=-1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x74fa22f0, original_name='HealthBarInitialHealthOverride'
        ),
    })
    glide_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x1f468967, original_name='GlideSound'
        ),
    })
    missile_ricochet_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x1a08aadc, original_name='MissileRicochetSound'
        ),
    })
    starts_in_the_air: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x6689925b, original_name='StartsInTheAir'
        ),
    })
    txtr: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['TXTR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3863160b, original_name='TXTR'
        ),
    })
    unknown_0x2c6a3344: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2c6a3344, original_name='Unknown'
        ),
    })
    melee_attack_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x4d790ee9, original_name='MeleeAttackDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    melee_attack_fx: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x6d40aa56, original_name='MeleeAttackFX'
        ),
    })
    melee_attack_fx_quick: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x9603a544, original_name='MeleeAttackFXQuick'
        ),
    })
    dive_attack_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x8688f535, original_name='DiveAttackDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    dive_attack_impulse_vertical: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4aa5dd62, original_name='DiveAttackImpulseVertical'
        ),
    })
    dive_attack_impulse_horizontal: float = dataclasses.field(default=500.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1ad7dc21, original_name='DiveAttackImpulseHorizontal'
        ),
    })
    dive_attack_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xed30b0ef, original_name='DiveAttackEffect'
        ),
    })
    scatter_shot_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x855f0749, original_name='ScatterShotProjectile'
        ),
    })
    scatter_shot_projectile2: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x83a5517f, original_name='ScatterShotProjectile2'
        ),
    })
    scatter_shot_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x8ea87062, original_name='ScatterShotDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    unknown_0x378285b9: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x378285b9, original_name='Unknown'
        ),
    })
    scatter_shot_projectiles_per_second: float = dataclasses.field(default=300.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd242e25f, original_name='ScatterShotProjectilesPerSecond'
        ),
    })
    normal_missile_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe00db62d, original_name='NormalMissileProjectile'
        ),
    })
    normal_missile_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xc4128792, original_name='NormalMissileDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    normal_missile_min_missiles_in_sequence: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x1f1ef7a9, original_name='NormalMissileMinMissilesInSequence'
        ),
    })
    normal_missile_max_missiles_in_sequence: int = dataclasses.field(default=3, metadata={
        'reflection': FieldReflection[int](
            int, id=0xc4a1a44e, original_name='NormalMissileMaxMissilesInSequence'
        ),
    })
    super_missile_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x29db4ee4, original_name='SuperMissileProjectile'
        ),
    })
    super_missile_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x26632b7e, original_name='SuperMissileDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    freeze_beam_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xf9104a69, original_name='FreezeBeamProjectile'
        ),
    })
    freeze_beam_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xb5ba1fe7, original_name='FreezeBeamDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    freeze_beam_visor_texture: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['TXTR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x7ffeb33d, original_name='FreezeBeamVisorTexture'
        ),
    })
    damage_interrupt_threshold: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8f70d3f2, original_name='DamageInterruptThreshold'
        ),
    })
    damage_interrupt_decrease_per_second: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf317f4d5, original_name='DamageInterruptDecreasePerSecond'
        ),
    })
    sweep_swoosh: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd2122711, original_name='SweepSwoosh'
        ),
    })
    sweep_beam_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x08c2bfe0, original_name='SweepBeamDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    sweep_beam_collision_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CRSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x68b658f2, original_name='SweepBeamCollisionEffect'
        ),
    })
    sweep_beam_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xea17cb66, original_name='SweepBeamSound'
        ),
    })
    sweep_beam_impact_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x0ef8dc15, original_name='SweepBeamImpactSound'
        ),
    })
    invulnerable_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x072df331, original_name='InvulnerableModel'
        ),
    })
    invulnerable_skin_rules: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CSKR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xaa96399c, original_name='InvulnerableSkinRules'
        ),
    })
    boost_ball_model: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0xf148f728, original_name='BoostBallModel', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    boost_ball_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xe18dc6fc, original_name='BoostBallDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    boost_ball_glow: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xac43ba34, original_name='BoostBallGlow'
        ),
    })
    boost_ball_trail_swoosh: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SWHC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x449aa4aa, original_name='BoostBallTrailSwoosh'
        ),
    })
    swhc: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SWHC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x0345fa17, original_name='SWHC'
        ),
    })
    boost_ball_roll_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x2c72576b, original_name='BoostBallRollSound'
        ),
    })
    boost_ball_hit_player_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x9e02691c, original_name='BoostBallHitPlayerSound'
        ),
    })
    boost_ball_collision: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3433bc8b, original_name='BoostBallCollision'
        ),
    })
    boost_ball_collision_sound_one_shot: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x4841182b, original_name='BoostBallCollisionSound_OneShot', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    ice_spread_fx: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa6c42023, original_name='IceSpreadFX'
        ),
    })
    ice_spread_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xd3593630, original_name='IceSpreadSound'
        ),
    })
    big_phazon_part: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x908b06e9, original_name='BigPhazonPart'
        ),
    })
    big_phazon_collision_part: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x494de4a4, original_name='BigPhazonCollisionPart'
        ),
    })
    big_phazon_impact_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xa861649f, original_name='BigPhazonImpactSound'
        ),
    })
    big_phazon_damage_per_second: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x18402aa9, original_name='BigPhazonDamagePerSecond', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    inside_big_phazon_visor_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe701daea, original_name='InsideBigPhazonVisorEffect'
        ),
    })
    phazon_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xbf62b633, original_name='PhazonProjectile'
        ),
    })
    phazon_super_missile_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x8d123fe9, original_name='PhazonSuperMissileProjectile'
        ),
    })
    phazon_super_missile_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x58769eb2, original_name='PhazonSuperMissileDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    phazon_projectile_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x4d8e735f, original_name='PhazonProjectileDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    phazon_enrage_sphere: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x83106405, original_name='PhazonEnrageSphere'
        ),
    })
    phazon_enrage_sphere_contact_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x8f3af226, original_name='PhazonEnrageSphereContactDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    alternate_scannable_info: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SCAN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xf60ac5cc, original_name='AlternateScannableInfo'
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'DRKS'

    @classmethod
    def modules(cls) -> list[str]:
        return ['DarkSamus.rel']

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
        if property_count != 63:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size, default_override={'detection_range': 32.0, 'collision_radius': 0.5, 'collision_height': 1.0, 'creature_size': 1})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x72edeb7d
        health_message_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x74fa22f0
        health_bar_initial_health_override = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1f468967
        glide_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1a08aadc
        missile_ricochet_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6689925b
        starts_in_the_air = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3863160b
        txtr = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2c6a3344
        unknown_0x2c6a3344 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4d790ee9
        melee_attack_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6d40aa56
        melee_attack_fx = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9603a544
        melee_attack_fx_quick = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8688f535
        dive_attack_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4aa5dd62
        dive_attack_impulse_vertical = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1ad7dc21
        dive_attack_impulse_horizontal = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed30b0ef
        dive_attack_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x855f0749
        scatter_shot_projectile = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x83a5517f
        scatter_shot_projectile2 = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8ea87062
        scatter_shot_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x378285b9
        unknown_0x378285b9 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd242e25f
        scatter_shot_projectiles_per_second = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe00db62d
        normal_missile_projectile = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc4128792
        normal_missile_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1f1ef7a9
        normal_missile_min_missiles_in_sequence = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc4a1a44e
        normal_missile_max_missiles_in_sequence = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x29db4ee4
        super_missile_projectile = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x26632b7e
        super_missile_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf9104a69
        freeze_beam_projectile = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb5ba1fe7
        freeze_beam_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7ffeb33d
        freeze_beam_visor_texture = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8f70d3f2
        damage_interrupt_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf317f4d5
        damage_interrupt_decrease_per_second = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd2122711
        sweep_swoosh = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08c2bfe0
        sweep_beam_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68b658f2
        sweep_beam_collision_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xea17cb66
        sweep_beam_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0ef8dc15
        sweep_beam_impact_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x072df331
        invulnerable_model = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaa96399c
        invulnerable_skin_rules = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf148f728
        boost_ball_model = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe18dc6fc
        boost_ball_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xac43ba34
        boost_ball_glow = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x449aa4aa
        boost_ball_trail_swoosh = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0345fa17
        swhc = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2c72576b
        boost_ball_roll_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9e02691c
        boost_ball_hit_player_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3433bc8b
        boost_ball_collision = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4841182b
        boost_ball_collision_sound_one_shot = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa6c42023
        ice_spread_fx = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd3593630
        ice_spread_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x908b06e9
        big_phazon_part = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x494de4a4
        big_phazon_collision_part = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa861649f
        big_phazon_impact_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x18402aa9
        big_phazon_damage_per_second = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe701daea
        inside_big_phazon_visor_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbf62b633
        phazon_projectile = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8d123fe9
        phazon_super_missile_projectile = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58769eb2
        phazon_super_missile_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4d8e735f
        phazon_projectile_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 10.0, 'di_radius': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x83106405
        phazon_enrage_sphere = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8f3af226
        phazon_enrage_sphere_contact_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf60ac5cc
        alternate_scannable_info = structs.BIG_L.unpack(data.read(4))[0]
    
        return cls(editor_properties, patterned, actor_information, health_message_threshold, health_bar_initial_health_override, glide_sound, missile_ricochet_sound, starts_in_the_air, txtr, unknown_0x2c6a3344, melee_attack_damage, melee_attack_fx, melee_attack_fx_quick, dive_attack_damage, dive_attack_impulse_vertical, dive_attack_impulse_horizontal, dive_attack_effect, scatter_shot_projectile, scatter_shot_projectile2, scatter_shot_damage, unknown_0x378285b9, scatter_shot_projectiles_per_second, normal_missile_projectile, normal_missile_damage, normal_missile_min_missiles_in_sequence, normal_missile_max_missiles_in_sequence, super_missile_projectile, super_missile_damage, freeze_beam_projectile, freeze_beam_damage, freeze_beam_visor_texture, damage_interrupt_threshold, damage_interrupt_decrease_per_second, sweep_swoosh, sweep_beam_damage, sweep_beam_collision_effect, sweep_beam_sound, sweep_beam_impact_sound, invulnerable_model, invulnerable_skin_rules, boost_ball_model, boost_ball_damage, boost_ball_glow, boost_ball_trail_swoosh, swhc, boost_ball_roll_sound, boost_ball_hit_player_sound, boost_ball_collision, boost_ball_collision_sound_one_shot, ice_spread_fx, ice_spread_sound, big_phazon_part, big_phazon_collision_part, big_phazon_impact_sound, big_phazon_damage_per_second, inside_big_phazon_visor_effect, phazon_projectile, phazon_super_missile_projectile, phazon_super_missile_damage, phazon_projectile_damage, phazon_enrage_sphere, phazon_enrage_sphere_contact_damage, alternate_scannable_info)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00?')  # 63 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game, default_override={'misc_flags': 3})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb3wGP')  # 0xb3774750
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.patterned.to_stream(data, game, default_override={'detection_range': 32.0, 'collision_radius': 0.5, 'collision_height': 1.0, 'creature_size': 1})
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

        data.write(b'r\xed\xeb}')  # 0x72edeb7d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.health_message_threshold))

        data.write(b't\xfa"\xf0')  # 0x74fa22f0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.health_bar_initial_health_override))

        data.write(b'\x1fF\x89g')  # 0x1f468967
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.glide_sound))

        data.write(b'\x1a\x08\xaa\xdc')  # 0x1a08aadc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.missile_ricochet_sound))

        data.write(b'f\x89\x92[')  # 0x6689925b
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.starts_in_the_air))

        data.write(b'8c\x16\x0b')  # 0x3863160b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.txtr))

        data.write(b',j3D')  # 0x2c6a3344
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2c6a3344))

        data.write(b'My\x0e\xe9')  # 0x4d790ee9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.melee_attack_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'm@\xaaV')  # 0x6d40aa56
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.melee_attack_fx))

        data.write(b'\x96\x03\xa5D')  # 0x9603a544
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.melee_attack_fx_quick))

        data.write(b'\x86\x88\xf55')  # 0x8688f535
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.dive_attack_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'J\xa5\xddb')  # 0x4aa5dd62
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dive_attack_impulse_vertical))

        data.write(b'\x1a\xd7\xdc!')  # 0x1ad7dc21
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dive_attack_impulse_horizontal))

        data.write(b'\xed0\xb0\xef')  # 0xed30b0ef
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.dive_attack_effect))

        data.write(b'\x85_\x07I')  # 0x855f0749
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.scatter_shot_projectile))

        data.write(b'\x83\xa5Q\x7f')  # 0x83a5517f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.scatter_shot_projectile2))

        data.write(b'\x8e\xa8pb')  # 0x8ea87062
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.scatter_shot_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'7\x82\x85\xb9')  # 0x378285b9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x378285b9))

        data.write(b'\xd2B\xe2_')  # 0xd242e25f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scatter_shot_projectiles_per_second))

        data.write(b'\xe0\r\xb6-')  # 0xe00db62d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.normal_missile_projectile))

        data.write(b'\xc4\x12\x87\x92')  # 0xc4128792
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.normal_missile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x1f\x1e\xf7\xa9')  # 0x1f1ef7a9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.normal_missile_min_missiles_in_sequence))

        data.write(b'\xc4\xa1\xa4N')  # 0xc4a1a44e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.normal_missile_max_missiles_in_sequence))

        data.write(b')\xdbN\xe4')  # 0x29db4ee4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.super_missile_projectile))

        data.write(b'&c+~')  # 0x26632b7e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.super_missile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf9\x10Ji')  # 0xf9104a69
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.freeze_beam_projectile))

        data.write(b'\xb5\xba\x1f\xe7')  # 0xb5ba1fe7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.freeze_beam_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x7f\xfe\xb3=')  # 0x7ffeb33d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.freeze_beam_visor_texture))

        data.write(b'\x8fp\xd3\xf2')  # 0x8f70d3f2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.damage_interrupt_threshold))

        data.write(b'\xf3\x17\xf4\xd5')  # 0xf317f4d5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.damage_interrupt_decrease_per_second))

        data.write(b"\xd2\x12'\x11")  # 0xd2122711
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.sweep_swoosh))

        data.write(b'\x08\xc2\xbf\xe0')  # 0x8c2bfe0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sweep_beam_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'h\xb6X\xf2')  # 0x68b658f2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.sweep_beam_collision_effect))

        data.write(b'\xea\x17\xcbf')  # 0xea17cb66
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sweep_beam_sound))

        data.write(b'\x0e\xf8\xdc\x15')  # 0xef8dc15
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sweep_beam_impact_sound))

        data.write(b'\x07-\xf31')  # 0x72df331
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.invulnerable_model))

        data.write(b'\xaa\x969\x9c')  # 0xaa96399c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.invulnerable_skin_rules))

        data.write(b'\xf1H\xf7(')  # 0xf148f728
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.boost_ball_model.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe1\x8d\xc6\xfc')  # 0xe18dc6fc
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.boost_ball_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xacC\xba4')  # 0xac43ba34
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.boost_ball_glow))

        data.write(b'D\x9a\xa4\xaa')  # 0x449aa4aa
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.boost_ball_trail_swoosh))

        data.write(b'\x03E\xfa\x17')  # 0x345fa17
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.swhc))

        data.write(b',rWk')  # 0x2c72576b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.boost_ball_roll_sound))

        data.write(b'\x9e\x02i\x1c')  # 0x9e02691c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.boost_ball_hit_player_sound))

        data.write(b'43\xbc\x8b')  # 0x3433bc8b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.boost_ball_collision))

        data.write(b'HA\x18+')  # 0x4841182b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.boost_ball_collision_sound_one_shot.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa6\xc4 #')  # 0xa6c42023
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.ice_spread_fx))

        data.write(b'\xd3Y60')  # 0xd3593630
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.ice_spread_sound))

        data.write(b'\x90\x8b\x06\xe9')  # 0x908b06e9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.big_phazon_part))

        data.write(b'IM\xe4\xa4')  # 0x494de4a4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.big_phazon_collision_part))

        data.write(b'\xa8ad\x9f')  # 0xa861649f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.big_phazon_impact_sound))

        data.write(b'\x18@*\xa9')  # 0x18402aa9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.big_phazon_damage_per_second.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe7\x01\xda\xea')  # 0xe701daea
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.inside_big_phazon_visor_effect))

        data.write(b'\xbfb\xb63')  # 0xbf62b633
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.phazon_projectile))

        data.write(b'\x8d\x12?\xe9')  # 0x8d123fe9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.phazon_super_missile_projectile))

        data.write(b'Xv\x9e\xb2')  # 0x58769eb2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.phazon_super_missile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'M\x8es_')  # 0x4d8e735f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.phazon_projectile_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 10.0, 'di_radius': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x83\x10d\x05')  # 0x83106405
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.phazon_enrage_sphere))

        data.write(b'\x8f:\xf2&')  # 0x8f3af226
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.phazon_enrage_sphere_contact_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf6\n\xc5\xcc')  # 0xf60ac5cc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.alternate_scannable_info))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DarkSamusJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            patterned=PatternedAITypedef.from_json(json_data['patterned']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
            health_message_threshold=json_data['health_message_threshold'],
            health_bar_initial_health_override=json_data['health_bar_initial_health_override'],
            glide_sound=json_data['glide_sound'],
            missile_ricochet_sound=json_data['missile_ricochet_sound'],
            starts_in_the_air=json_data['starts_in_the_air'],
            txtr=json_data['txtr'],
            unknown_0x2c6a3344=json_data['unknown_0x2c6a3344'],
            melee_attack_damage=DamageInfo.from_json(json_data['melee_attack_damage']),
            melee_attack_fx=json_data['melee_attack_fx'],
            melee_attack_fx_quick=json_data['melee_attack_fx_quick'],
            dive_attack_damage=DamageInfo.from_json(json_data['dive_attack_damage']),
            dive_attack_impulse_vertical=json_data['dive_attack_impulse_vertical'],
            dive_attack_impulse_horizontal=json_data['dive_attack_impulse_horizontal'],
            dive_attack_effect=json_data['dive_attack_effect'],
            scatter_shot_projectile=json_data['scatter_shot_projectile'],
            scatter_shot_projectile2=json_data['scatter_shot_projectile2'],
            scatter_shot_damage=DamageInfo.from_json(json_data['scatter_shot_damage']),
            unknown_0x378285b9=json_data['unknown_0x378285b9'],
            scatter_shot_projectiles_per_second=json_data['scatter_shot_projectiles_per_second'],
            normal_missile_projectile=json_data['normal_missile_projectile'],
            normal_missile_damage=DamageInfo.from_json(json_data['normal_missile_damage']),
            normal_missile_min_missiles_in_sequence=json_data['normal_missile_min_missiles_in_sequence'],
            normal_missile_max_missiles_in_sequence=json_data['normal_missile_max_missiles_in_sequence'],
            super_missile_projectile=json_data['super_missile_projectile'],
            super_missile_damage=DamageInfo.from_json(json_data['super_missile_damage']),
            freeze_beam_projectile=json_data['freeze_beam_projectile'],
            freeze_beam_damage=DamageInfo.from_json(json_data['freeze_beam_damage']),
            freeze_beam_visor_texture=json_data['freeze_beam_visor_texture'],
            damage_interrupt_threshold=json_data['damage_interrupt_threshold'],
            damage_interrupt_decrease_per_second=json_data['damage_interrupt_decrease_per_second'],
            sweep_swoosh=json_data['sweep_swoosh'],
            sweep_beam_damage=DamageInfo.from_json(json_data['sweep_beam_damage']),
            sweep_beam_collision_effect=json_data['sweep_beam_collision_effect'],
            sweep_beam_sound=json_data['sweep_beam_sound'],
            sweep_beam_impact_sound=json_data['sweep_beam_impact_sound'],
            invulnerable_model=json_data['invulnerable_model'],
            invulnerable_skin_rules=json_data['invulnerable_skin_rules'],
            boost_ball_model=AnimationParameters.from_json(json_data['boost_ball_model']),
            boost_ball_damage=DamageInfo.from_json(json_data['boost_ball_damage']),
            boost_ball_glow=json_data['boost_ball_glow'],
            boost_ball_trail_swoosh=json_data['boost_ball_trail_swoosh'],
            swhc=json_data['swhc'],
            boost_ball_roll_sound=json_data['boost_ball_roll_sound'],
            boost_ball_hit_player_sound=json_data['boost_ball_hit_player_sound'],
            boost_ball_collision=json_data['boost_ball_collision'],
            boost_ball_collision_sound_one_shot=AudioPlaybackParms.from_json(json_data['boost_ball_collision_sound_one_shot']),
            ice_spread_fx=json_data['ice_spread_fx'],
            ice_spread_sound=json_data['ice_spread_sound'],
            big_phazon_part=json_data['big_phazon_part'],
            big_phazon_collision_part=json_data['big_phazon_collision_part'],
            big_phazon_impact_sound=json_data['big_phazon_impact_sound'],
            big_phazon_damage_per_second=DamageInfo.from_json(json_data['big_phazon_damage_per_second']),
            inside_big_phazon_visor_effect=json_data['inside_big_phazon_visor_effect'],
            phazon_projectile=json_data['phazon_projectile'],
            phazon_super_missile_projectile=json_data['phazon_super_missile_projectile'],
            phazon_super_missile_damage=DamageInfo.from_json(json_data['phazon_super_missile_damage']),
            phazon_projectile_damage=DamageInfo.from_json(json_data['phazon_projectile_damage']),
            phazon_enrage_sphere=json_data['phazon_enrage_sphere'],
            phazon_enrage_sphere_contact_damage=DamageInfo.from_json(json_data['phazon_enrage_sphere_contact_damage']),
            alternate_scannable_info=json_data['alternate_scannable_info'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'patterned': self.patterned.to_json(),
            'actor_information': self.actor_information.to_json(),
            'health_message_threshold': self.health_message_threshold,
            'health_bar_initial_health_override': self.health_bar_initial_health_override,
            'glide_sound': self.glide_sound,
            'missile_ricochet_sound': self.missile_ricochet_sound,
            'starts_in_the_air': self.starts_in_the_air,
            'txtr': self.txtr,
            'unknown_0x2c6a3344': self.unknown_0x2c6a3344,
            'melee_attack_damage': self.melee_attack_damage.to_json(),
            'melee_attack_fx': self.melee_attack_fx,
            'melee_attack_fx_quick': self.melee_attack_fx_quick,
            'dive_attack_damage': self.dive_attack_damage.to_json(),
            'dive_attack_impulse_vertical': self.dive_attack_impulse_vertical,
            'dive_attack_impulse_horizontal': self.dive_attack_impulse_horizontal,
            'dive_attack_effect': self.dive_attack_effect,
            'scatter_shot_projectile': self.scatter_shot_projectile,
            'scatter_shot_projectile2': self.scatter_shot_projectile2,
            'scatter_shot_damage': self.scatter_shot_damage.to_json(),
            'unknown_0x378285b9': self.unknown_0x378285b9,
            'scatter_shot_projectiles_per_second': self.scatter_shot_projectiles_per_second,
            'normal_missile_projectile': self.normal_missile_projectile,
            'normal_missile_damage': self.normal_missile_damage.to_json(),
            'normal_missile_min_missiles_in_sequence': self.normal_missile_min_missiles_in_sequence,
            'normal_missile_max_missiles_in_sequence': self.normal_missile_max_missiles_in_sequence,
            'super_missile_projectile': self.super_missile_projectile,
            'super_missile_damage': self.super_missile_damage.to_json(),
            'freeze_beam_projectile': self.freeze_beam_projectile,
            'freeze_beam_damage': self.freeze_beam_damage.to_json(),
            'freeze_beam_visor_texture': self.freeze_beam_visor_texture,
            'damage_interrupt_threshold': self.damage_interrupt_threshold,
            'damage_interrupt_decrease_per_second': self.damage_interrupt_decrease_per_second,
            'sweep_swoosh': self.sweep_swoosh,
            'sweep_beam_damage': self.sweep_beam_damage.to_json(),
            'sweep_beam_collision_effect': self.sweep_beam_collision_effect,
            'sweep_beam_sound': self.sweep_beam_sound,
            'sweep_beam_impact_sound': self.sweep_beam_impact_sound,
            'invulnerable_model': self.invulnerable_model,
            'invulnerable_skin_rules': self.invulnerable_skin_rules,
            'boost_ball_model': self.boost_ball_model.to_json(),
            'boost_ball_damage': self.boost_ball_damage.to_json(),
            'boost_ball_glow': self.boost_ball_glow,
            'boost_ball_trail_swoosh': self.boost_ball_trail_swoosh,
            'swhc': self.swhc,
            'boost_ball_roll_sound': self.boost_ball_roll_sound,
            'boost_ball_hit_player_sound': self.boost_ball_hit_player_sound,
            'boost_ball_collision': self.boost_ball_collision,
            'boost_ball_collision_sound_one_shot': self.boost_ball_collision_sound_one_shot.to_json(),
            'ice_spread_fx': self.ice_spread_fx,
            'ice_spread_sound': self.ice_spread_sound,
            'big_phazon_part': self.big_phazon_part,
            'big_phazon_collision_part': self.big_phazon_collision_part,
            'big_phazon_impact_sound': self.big_phazon_impact_sound,
            'big_phazon_damage_per_second': self.big_phazon_damage_per_second.to_json(),
            'inside_big_phazon_visor_effect': self.inside_big_phazon_visor_effect,
            'phazon_projectile': self.phazon_projectile,
            'phazon_super_missile_projectile': self.phazon_super_missile_projectile,
            'phazon_super_missile_damage': self.phazon_super_missile_damage.to_json(),
            'phazon_projectile_damage': self.phazon_projectile_damage.to_json(),
            'phazon_enrage_sphere': self.phazon_enrage_sphere,
            'phazon_enrage_sphere_contact_damage': self.phazon_enrage_sphere_contact_damage.to_json(),
            'alternate_scannable_info': self.alternate_scannable_info,
        }

    def _dependencies_for_glide_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.glide_sound)

    def _dependencies_for_missile_ricochet_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.missile_ricochet_sound)

    def _dependencies_for_txtr(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.txtr)

    def _dependencies_for_melee_attack_fx(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.melee_attack_fx)

    def _dependencies_for_melee_attack_fx_quick(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.melee_attack_fx_quick)

    def _dependencies_for_dive_attack_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.dive_attack_effect)

    def _dependencies_for_scatter_shot_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scatter_shot_projectile)

    def _dependencies_for_scatter_shot_projectile2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scatter_shot_projectile2)

    def _dependencies_for_normal_missile_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.normal_missile_projectile)

    def _dependencies_for_super_missile_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.super_missile_projectile)

    def _dependencies_for_freeze_beam_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.freeze_beam_projectile)

    def _dependencies_for_freeze_beam_visor_texture(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.freeze_beam_visor_texture)

    def _dependencies_for_sweep_swoosh(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sweep_swoosh)

    def _dependencies_for_sweep_beam_collision_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sweep_beam_collision_effect)

    def _dependencies_for_sweep_beam_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sweep_beam_sound)

    def _dependencies_for_sweep_beam_impact_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sweep_beam_impact_sound)

    def _dependencies_for_invulnerable_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.invulnerable_model)

    def _dependencies_for_invulnerable_skin_rules(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.invulnerable_skin_rules)

    def _dependencies_for_boost_ball_glow(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.boost_ball_glow)

    def _dependencies_for_boost_ball_trail_swoosh(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.boost_ball_trail_swoosh)

    def _dependencies_for_swhc(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.swhc)

    def _dependencies_for_boost_ball_roll_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.boost_ball_roll_sound)

    def _dependencies_for_boost_ball_hit_player_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.boost_ball_hit_player_sound)

    def _dependencies_for_boost_ball_collision(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.boost_ball_collision)

    def _dependencies_for_ice_spread_fx(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ice_spread_fx)

    def _dependencies_for_ice_spread_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.ice_spread_sound)

    def _dependencies_for_big_phazon_part(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.big_phazon_part)

    def _dependencies_for_big_phazon_collision_part(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.big_phazon_collision_part)

    def _dependencies_for_big_phazon_impact_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.big_phazon_impact_sound)

    def _dependencies_for_inside_big_phazon_visor_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.inside_big_phazon_visor_effect)

    def _dependencies_for_phazon_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.phazon_projectile)

    def _dependencies_for_phazon_super_missile_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.phazon_super_missile_projectile)

    def _dependencies_for_phazon_enrage_sphere(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.phazon_enrage_sphere)

    def _dependencies_for_alternate_scannable_info(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.alternate_scannable_info)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_glide_sound, "glide_sound", "int"),
            (self._dependencies_for_missile_ricochet_sound, "missile_ricochet_sound", "int"),
            (self._dependencies_for_txtr, "txtr", "AssetId"),
            (self._dependencies_for_melee_attack_fx, "melee_attack_fx", "AssetId"),
            (self._dependencies_for_melee_attack_fx_quick, "melee_attack_fx_quick", "AssetId"),
            (self._dependencies_for_dive_attack_effect, "dive_attack_effect", "AssetId"),
            (self._dependencies_for_scatter_shot_projectile, "scatter_shot_projectile", "AssetId"),
            (self._dependencies_for_scatter_shot_projectile2, "scatter_shot_projectile2", "AssetId"),
            (self._dependencies_for_normal_missile_projectile, "normal_missile_projectile", "AssetId"),
            (self._dependencies_for_super_missile_projectile, "super_missile_projectile", "AssetId"),
            (self._dependencies_for_freeze_beam_projectile, "freeze_beam_projectile", "AssetId"),
            (self._dependencies_for_freeze_beam_visor_texture, "freeze_beam_visor_texture", "AssetId"),
            (self._dependencies_for_sweep_swoosh, "sweep_swoosh", "AssetId"),
            (self._dependencies_for_sweep_beam_collision_effect, "sweep_beam_collision_effect", "AssetId"),
            (self._dependencies_for_sweep_beam_sound, "sweep_beam_sound", "int"),
            (self._dependencies_for_sweep_beam_impact_sound, "sweep_beam_impact_sound", "int"),
            (self._dependencies_for_invulnerable_model, "invulnerable_model", "AssetId"),
            (self._dependencies_for_invulnerable_skin_rules, "invulnerable_skin_rules", "AssetId"),
            (self.boost_ball_model.dependencies_for, "boost_ball_model", "AnimationParameters"),
            (self._dependencies_for_boost_ball_glow, "boost_ball_glow", "AssetId"),
            (self._dependencies_for_boost_ball_trail_swoosh, "boost_ball_trail_swoosh", "AssetId"),
            (self._dependencies_for_swhc, "swhc", "AssetId"),
            (self._dependencies_for_boost_ball_roll_sound, "boost_ball_roll_sound", "int"),
            (self._dependencies_for_boost_ball_hit_player_sound, "boost_ball_hit_player_sound", "int"),
            (self._dependencies_for_boost_ball_collision, "boost_ball_collision", "AssetId"),
            (self.boost_ball_collision_sound_one_shot.dependencies_for, "boost_ball_collision_sound_one_shot", "AudioPlaybackParms"),
            (self._dependencies_for_ice_spread_fx, "ice_spread_fx", "AssetId"),
            (self._dependencies_for_ice_spread_sound, "ice_spread_sound", "int"),
            (self._dependencies_for_big_phazon_part, "big_phazon_part", "AssetId"),
            (self._dependencies_for_big_phazon_collision_part, "big_phazon_collision_part", "AssetId"),
            (self._dependencies_for_big_phazon_impact_sound, "big_phazon_impact_sound", "int"),
            (self._dependencies_for_inside_big_phazon_visor_effect, "inside_big_phazon_visor_effect", "AssetId"),
            (self._dependencies_for_phazon_projectile, "phazon_projectile", "AssetId"),
            (self._dependencies_for_phazon_super_missile_projectile, "phazon_super_missile_projectile", "AssetId"),
            (self._dependencies_for_phazon_enrage_sphere, "phazon_enrage_sphere", "AssetId"),
            (self._dependencies_for_alternate_scannable_info, "alternate_scannable_info", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for DarkSamus.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={'detection_range': 32.0, 'collision_radius': 0.5, 'collision_height': 1.0, 'creature_size': 1})


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_melee_attack_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_dive_attack_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_scatter_shot_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_normal_missile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_super_missile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_freeze_beam_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_sweep_beam_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_boost_ball_model(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_boost_ball_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_boost_ball_collision_sound_one_shot(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_big_phazon_damage_per_second(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_phazon_super_missile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_phazon_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 10.0, 'di_radius': 5.0})


def _decode_phazon_enrage_sphere_contact_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xb3774750: ('patterned', _decode_patterned),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0x72edeb7d: ('health_message_threshold', structs.decode_BIG_f),
    0x74fa22f0: ('health_bar_initial_health_override', structs.decode_BIG_f),
    0x1f468967: ('glide_sound', structs.decode_BIG_l),
    0x1a08aadc: ('missile_ricochet_sound', structs.decode_BIG_l),
    0x6689925b: ('starts_in_the_air', structs.decode_BIG_bool_),
    0x3863160b: ('txtr', structs.decode_BIG_L),
    0x2c6a3344: ('unknown_0x2c6a3344', structs.decode_BIG_f),
    0x4d790ee9: ('melee_attack_damage', _decode_melee_attack_damage),
    0x6d40aa56: ('melee_attack_fx', structs.decode_BIG_L),
    0x9603a544: ('melee_attack_fx_quick', structs.decode_BIG_L),
    0x8688f535: ('dive_attack_damage', _decode_dive_attack_damage),
    0x4aa5dd62: ('dive_attack_impulse_vertical', structs.decode_BIG_f),
    0x1ad7dc21: ('dive_attack_impulse_horizontal', structs.decode_BIG_f),
    0xed30b0ef: ('dive_attack_effect', structs.decode_BIG_L),
    0x855f0749: ('scatter_shot_projectile', structs.decode_BIG_L),
    0x83a5517f: ('scatter_shot_projectile2', structs.decode_BIG_L),
    0x8ea87062: ('scatter_shot_damage', _decode_scatter_shot_damage),
    0x378285b9: ('unknown_0x378285b9', structs.decode_BIG_f),
    0xd242e25f: ('scatter_shot_projectiles_per_second', structs.decode_BIG_f),
    0xe00db62d: ('normal_missile_projectile', structs.decode_BIG_L),
    0xc4128792: ('normal_missile_damage', _decode_normal_missile_damage),
    0x1f1ef7a9: ('normal_missile_min_missiles_in_sequence', structs.decode_BIG_l),
    0xc4a1a44e: ('normal_missile_max_missiles_in_sequence', structs.decode_BIG_l),
    0x29db4ee4: ('super_missile_projectile', structs.decode_BIG_L),
    0x26632b7e: ('super_missile_damage', _decode_super_missile_damage),
    0xf9104a69: ('freeze_beam_projectile', structs.decode_BIG_L),
    0xb5ba1fe7: ('freeze_beam_damage', _decode_freeze_beam_damage),
    0x7ffeb33d: ('freeze_beam_visor_texture', structs.decode_BIG_L),
    0x8f70d3f2: ('damage_interrupt_threshold', structs.decode_BIG_f),
    0xf317f4d5: ('damage_interrupt_decrease_per_second', structs.decode_BIG_f),
    0xd2122711: ('sweep_swoosh', structs.decode_BIG_L),
    0x08c2bfe0: ('sweep_beam_damage', _decode_sweep_beam_damage),
    0x68b658f2: ('sweep_beam_collision_effect', structs.decode_BIG_L),
    0xea17cb66: ('sweep_beam_sound', structs.decode_BIG_l),
    0x0ef8dc15: ('sweep_beam_impact_sound', structs.decode_BIG_l),
    0x072df331: ('invulnerable_model', structs.decode_BIG_L),
    0xaa96399c: ('invulnerable_skin_rules', structs.decode_BIG_L),
    0xf148f728: ('boost_ball_model', _decode_boost_ball_model),
    0xe18dc6fc: ('boost_ball_damage', _decode_boost_ball_damage),
    0xac43ba34: ('boost_ball_glow', structs.decode_BIG_L),
    0x449aa4aa: ('boost_ball_trail_swoosh', structs.decode_BIG_L),
    0x0345fa17: ('swhc', structs.decode_BIG_L),
    0x2c72576b: ('boost_ball_roll_sound', structs.decode_BIG_l),
    0x9e02691c: ('boost_ball_hit_player_sound', structs.decode_BIG_l),
    0x3433bc8b: ('boost_ball_collision', structs.decode_BIG_L),
    0x4841182b: ('boost_ball_collision_sound_one_shot', _decode_boost_ball_collision_sound_one_shot),
    0xa6c42023: ('ice_spread_fx', structs.decode_BIG_L),
    0xd3593630: ('ice_spread_sound', structs.decode_BIG_l),
    0x908b06e9: ('big_phazon_part', structs.decode_BIG_L),
    0x494de4a4: ('big_phazon_collision_part', structs.decode_BIG_L),
    0xa861649f: ('big_phazon_impact_sound', structs.decode_BIG_l),
    0x18402aa9: ('big_phazon_damage_per_second', _decode_big_phazon_damage_per_second),
    0xe701daea: ('inside_big_phazon_visor_effect', structs.decode_BIG_L),
    0xbf62b633: ('phazon_projectile', structs.decode_BIG_L),
    0x8d123fe9: ('phazon_super_missile_projectile', structs.decode_BIG_L),
    0x58769eb2: ('phazon_super_missile_damage', _decode_phazon_super_missile_damage),
    0x4d8e735f: ('phazon_projectile_damage', _decode_phazon_projectile_damage),
    0x83106405: ('phazon_enrage_sphere', structs.decode_BIG_L),
    0x8f3af226: ('phazon_enrage_sphere_contact_damage', _decode_phazon_enrage_sphere_contact_damage),
    0xf60ac5cc: ('alternate_scannable_info', structs.decode_BIG_L),
}
