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
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.IngPossessionData import IngPossessionData
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class GrenchlerJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        tail_destroyed_health: float
        is_grapple_guardian: bool
        has_health_bar: bool
        damage_vulnerability: json_util.JsonObject
        tail: json_util.JsonObject
        tail_when_underwater: json_util.JsonObject
        tailless_model: int
        tailless_skin_rules: int
        tail_dark: json_util.JsonObject
        tail_when_underwater_dark: json_util.JsonObject
        tailless_model_dark: int
        tailless_skin_rules_dark: int
        tail_hit_sound: int
        tail_destroyed_sound: int
        min_time_between_charges: float
        unknown_0x7bd1a35f: float
        charge_attack_min_range: float
        charge_attack_max_range: float
        bite_attack_min_range: float
        bite_attack_max_range: float
        bite_attack_min_pause: float
        bite_attack_max_pause: float
        bite_attack_damage_radius: float
        bite_damage: json_util.JsonObject
        beam_attack_min_range: float
        beam_attack_max_range: float
        beam_attack_min_pause: float
        beam_attack_max_pause: float
        electric_effect: int
        beam_damage: json_util.JsonObject
        beam_attack_max_angle: float
        beam_attack_sound_one_shot: json_util.JsonObject
        burst_attack_min_range: float
        burst_attack_max_range: float
        burst_attack_min_pause: float
        burst_attack_max_pause: float
        burst_attack_damage_radius: float
        burst_projectile: int
        burst_damage: json_util.JsonObject
        surface_rings_effect: int
        shallow_water_ring: int
        shallow_water_splash: int
        shake_off_visor_effect: int
        grapple_swoosh: int
        grapple_beam_part: int
        grapple_hit_fx: int
        grapple_damage: json_util.JsonObject
        grapple_beam_sound_loop: json_util.JsonObject
        beam_effect: int
        unknown_0xd4753ff4: int
        unknown_0x05fc6001: float
        unknown_0x13e5b580: float
        unknown_0xfc6f199d: float
        grapple_visor_effect: int
        electrified_contact_damage: json_util.JsonObject
        electrified_visor_effect: int
        electrified_sound_loop: json_util.JsonObject
        grapple_guardian_eye_glow: int
        alternate_scannable_info: int
        ing_possession_data: json_util.JsonObject
    

@dataclasses.dataclass()
class Grenchler(BaseObjectType):
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
    tail_destroyed_health: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x04d51e3a, original_name='TailDestroyedHealth'
        ),
    })
    is_grapple_guardian: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x33408e7f, original_name='IsGrappleGuardian'
        ),
    })
    has_health_bar: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x67b6ea0b, original_name='HasHealthBar'
        ),
    })
    damage_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x0a7326a3, original_name='DamageVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    tail: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0xa18f626b, original_name='Tail', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    tail_when_underwater: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0x0abef809, original_name='TailWhenUnderwater', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    tailless_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x4f3a4566, original_name='TaillessModel'
        ),
    })
    tailless_skin_rules: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CSKR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x401bc111, original_name='TaillessSkinRules'
        ),
    })
    tail_dark: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0x9b193ae8, original_name='Tail_Dark', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    tail_when_underwater_dark: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0xc24cf580, original_name='TailWhenUnderwater_Dark', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    tailless_model_dark: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x72258fe7, original_name='TaillessModel_Dark'
        ),
    })
    tailless_skin_rules_dark: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CSKR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe5fba24c, original_name='TaillessSkinRules_Dark'
        ),
    })
    tail_hit_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x55c51213, original_name='TailHitSound'
        ),
    })
    tail_destroyed_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x385e4738, original_name='TailDestroyedSound'
        ),
    })
    min_time_between_charges: float = dataclasses.field(default=4.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5d8f2bee, original_name='MinTimeBetweenCharges'
        ),
    })
    unknown_0x7bd1a35f: float = dataclasses.field(default=-1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7bd1a35f, original_name='Unknown'
        ),
    })
    charge_attack_min_range: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xea4b88c8, original_name='ChargeAttackMinRange'
        ),
    })
    charge_attack_max_range: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xaa04f0be, original_name='ChargeAttackMaxRange'
        ),
    })
    bite_attack_min_range: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x98d5d373, original_name='BiteAttackMinRange'
        ),
    })
    bite_attack_max_range: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd89aab05, original_name='BiteAttackMaxRange'
        ),
    })
    bite_attack_min_pause: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2e6096ee, original_name='BiteAttackMinPause'
        ),
    })
    bite_attack_max_pause: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6e2fee98, original_name='BiteAttackMaxPause'
        ),
    })
    bite_attack_damage_radius: float = dataclasses.field(default=6.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x49632b31, original_name='BiteAttackDamageRadius'
        ),
    })
    bite_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xdf636c4b, original_name='BiteDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    beam_attack_min_range: float = dataclasses.field(default=9.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x262b2508, original_name='BeamAttackMinRange'
        ),
    })
    beam_attack_max_range: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x66645d7e, original_name='BeamAttackMaxRange'
        ),
    })
    beam_attack_min_pause: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x909e6095, original_name='BeamAttackMinPause'
        ),
    })
    beam_attack_max_pause: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd0d118e3, original_name='BeamAttackMaxPause'
        ),
    })
    electric_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['ELSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x49fae143, original_name='ElectricEffect'
        ),
    })
    beam_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x13e30e4d, original_name='BeamDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    beam_attack_max_angle: float = dataclasses.field(default=45.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x680ce795, original_name='BeamAttackMaxAngle'
        ),
    })
    beam_attack_sound_one_shot: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xad47febe, original_name='BeamAttackSound_OneShot', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    burst_attack_min_range: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x06f7ceed, original_name='BurstAttackMinRange'
        ),
    })
    burst_attack_max_range: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x46b8b69b, original_name='BurstAttackMaxRange'
        ),
    })
    burst_attack_min_pause: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb0428b70, original_name='BurstAttackMinPause'
        ),
    })
    burst_attack_max_pause: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf00df306, original_name='BurstAttackMaxPause'
        ),
    })
    burst_attack_damage_radius: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb00775e6, original_name='BurstAttackDamageRadius'
        ),
    })
    burst_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x7ef9aa67, original_name='BurstProjectile'
        ),
    })
    burst_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x5285db00, original_name='BurstDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    surface_rings_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x30b81a7e, original_name='SurfaceRingsEffect'
        ),
    })
    shallow_water_ring: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xbf4daae6, original_name='ShallowWaterRing'
        ),
    })
    shallow_water_splash: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x70247a6e, original_name='ShallowWaterSplash'
        ),
    })
    shake_off_visor_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xffcee1a9, original_name='ShakeOffVisorEffect'
        ),
    })
    grapple_swoosh: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xae1f2a26, original_name='GrappleSwoosh'
        ),
    })
    grapple_beam_part: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x0dabf0af, original_name='GrappleBeamPart'
        ),
    })
    grapple_hit_fx: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe51746d1, original_name='GrappleHitFx'
        ),
    })
    grapple_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x2ce7520f, original_name='GrappleDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    grapple_beam_sound_loop: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xb6b9074b, original_name='GrappleBeamSound_Loop', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    beam_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x05439a08, original_name='BeamEffect'
        ),
    })
    unknown_0xd4753ff4: int = dataclasses.field(default=4, metadata={
        'reflection': FieldReflection[int](
            int, id=0xd4753ff4, original_name='Unknown'
        ),
    })
    unknown_0x05fc6001: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x05fc6001, original_name='Unknown'
        ),
    })
    unknown_0x13e5b580: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x13e5b580, original_name='Unknown'
        ),
    })
    unknown_0xfc6f199d: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfc6f199d, original_name='Unknown'
        ),
    })
    grapple_visor_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xf6502596, original_name='GrappleVisorEffect'
        ),
    })
    electrified_contact_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x6ec26414, original_name='ElectrifiedContactDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    electrified_visor_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x54b6bfa1, original_name='ElectrifiedVisorEffect'
        ),
    })
    electrified_sound_loop: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x5cf705f2, original_name='ElectrifiedSound_Loop', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    grapple_guardian_eye_glow: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb9f9f4f2, original_name='GrappleGuardianEyeGlow'
        ),
    })
    alternate_scannable_info: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SCAN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xf60ac5cc, original_name='AlternateScannableInfo'
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
        return 'GRCH'

    @classmethod
    def modules(cls) -> list[str]:
        return ['Grenchler.rel']

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
        patterned = PatternedAITypedef.from_stream(data, game, property_size, default_override={'leash_radius': 100.0, 'collision_radius': 1.600000023841858, 'collision_height': 2.5, 'step_up_height': 1.0, 'creature_size': 1})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x04d51e3a
        tail_destroyed_health = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33408e7f
        is_grapple_guardian = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x67b6ea0b
        has_health_bar = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0a7326a3
        damage_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa18f626b
        tail = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0abef809
        tail_when_underwater = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4f3a4566
        tailless_model = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x401bc111
        tailless_skin_rules = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9b193ae8
        tail_dark = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc24cf580
        tail_when_underwater_dark = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x72258fe7
        tailless_model_dark = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe5fba24c
        tailless_skin_rules_dark = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x55c51213
        tail_hit_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x385e4738
        tail_destroyed_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5d8f2bee
        min_time_between_charges = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7bd1a35f
        unknown_0x7bd1a35f = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xea4b88c8
        charge_attack_min_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaa04f0be
        charge_attack_max_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x98d5d373
        bite_attack_min_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd89aab05
        bite_attack_max_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2e6096ee
        bite_attack_min_pause = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6e2fee98
        bite_attack_max_pause = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49632b31
        bite_attack_damage_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdf636c4b
        bite_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x262b2508
        beam_attack_min_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x66645d7e
        beam_attack_max_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x909e6095
        beam_attack_min_pause = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd0d118e3
        beam_attack_max_pause = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49fae143
        electric_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13e30e4d
        beam_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x680ce795
        beam_attack_max_angle = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xad47febe
        beam_attack_sound_one_shot = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x06f7ceed
        burst_attack_min_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x46b8b69b
        burst_attack_max_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb0428b70
        burst_attack_min_pause = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf00df306
        burst_attack_max_pause = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb00775e6
        burst_attack_damage_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7ef9aa67
        burst_projectile = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5285db00
        burst_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x30b81a7e
        surface_rings_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbf4daae6
        shallow_water_ring = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x70247a6e
        shallow_water_splash = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xffcee1a9
        shake_off_visor_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xae1f2a26
        grapple_swoosh = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0dabf0af
        grapple_beam_part = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe51746d1
        grapple_hit_fx = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2ce7520f
        grapple_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb6b9074b
        grapple_beam_sound_loop = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x05439a08
        beam_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd4753ff4
        unknown_0xd4753ff4 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x05fc6001
        unknown_0x05fc6001 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13e5b580
        unknown_0x13e5b580 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfc6f199d
        unknown_0xfc6f199d = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf6502596
        grapple_visor_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6ec26414
        electrified_contact_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x54b6bfa1
        electrified_visor_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5cf705f2
        electrified_sound_loop = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb9f9f4f2
        grapple_guardian_eye_glow = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf60ac5cc
        alternate_scannable_info = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe61748ed
        ing_possession_data = IngPossessionData.from_stream(data, game, property_size)
    
        return cls(editor_properties, patterned, actor_information, tail_destroyed_health, is_grapple_guardian, has_health_bar, damage_vulnerability, tail, tail_when_underwater, tailless_model, tailless_skin_rules, tail_dark, tail_when_underwater_dark, tailless_model_dark, tailless_skin_rules_dark, tail_hit_sound, tail_destroyed_sound, min_time_between_charges, unknown_0x7bd1a35f, charge_attack_min_range, charge_attack_max_range, bite_attack_min_range, bite_attack_max_range, bite_attack_min_pause, bite_attack_max_pause, bite_attack_damage_radius, bite_damage, beam_attack_min_range, beam_attack_max_range, beam_attack_min_pause, beam_attack_max_pause, electric_effect, beam_damage, beam_attack_max_angle, beam_attack_sound_one_shot, burst_attack_min_range, burst_attack_max_range, burst_attack_min_pause, burst_attack_max_pause, burst_attack_damage_radius, burst_projectile, burst_damage, surface_rings_effect, shallow_water_ring, shallow_water_splash, shake_off_visor_effect, grapple_swoosh, grapple_beam_part, grapple_hit_fx, grapple_damage, grapple_beam_sound_loop, beam_effect, unknown_0xd4753ff4, unknown_0x05fc6001, unknown_0x13e5b580, unknown_0xfc6f199d, grapple_visor_effect, electrified_contact_damage, electrified_visor_effect, electrified_sound_loop, grapple_guardian_eye_glow, alternate_scannable_info, ing_possession_data)

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
        self.patterned.to_stream(data, game, default_override={'leash_radius': 100.0, 'collision_radius': 1.600000023841858, 'collision_height': 2.5, 'step_up_height': 1.0, 'creature_size': 1})
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

        data.write(b'\x04\xd5\x1e:')  # 0x4d51e3a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.tail_destroyed_health))

        data.write(b'3@\x8e\x7f')  # 0x33408e7f
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_grapple_guardian))

        data.write(b'g\xb6\xea\x0b')  # 0x67b6ea0b
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.has_health_bar))

        data.write(b'\ns&\xa3')  # 0xa7326a3
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa1\x8fbk')  # 0xa18f626b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.tail.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\n\xbe\xf8\t')  # 0xabef809
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.tail_when_underwater.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'O:Ef')  # 0x4f3a4566
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.tailless_model))

        data.write(b'@\x1b\xc1\x11')  # 0x401bc111
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.tailless_skin_rules))

        data.write(b'\x9b\x19:\xe8')  # 0x9b193ae8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.tail_dark.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc2L\xf5\x80')  # 0xc24cf580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.tail_when_underwater_dark.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'r%\x8f\xe7')  # 0x72258fe7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.tailless_model_dark))

        data.write(b'\xe5\xfb\xa2L')  # 0xe5fba24c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.tailless_skin_rules_dark))

        data.write(b'U\xc5\x12\x13')  # 0x55c51213
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.tail_hit_sound))

        data.write(b'8^G8')  # 0x385e4738
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.tail_destroyed_sound))

        data.write(b']\x8f+\xee')  # 0x5d8f2bee
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_charges))

        data.write(b'{\xd1\xa3_')  # 0x7bd1a35f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7bd1a35f))

        data.write(b'\xeaK\x88\xc8')  # 0xea4b88c8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_attack_min_range))

        data.write(b'\xaa\x04\xf0\xbe')  # 0xaa04f0be
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_attack_max_range))

        data.write(b'\x98\xd5\xd3s')  # 0x98d5d373
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.bite_attack_min_range))

        data.write(b'\xd8\x9a\xab\x05')  # 0xd89aab05
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.bite_attack_max_range))

        data.write(b'.`\x96\xee')  # 0x2e6096ee
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.bite_attack_min_pause))

        data.write(b'n/\xee\x98')  # 0x6e2fee98
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.bite_attack_max_pause))

        data.write(b'Ic+1')  # 0x49632b31
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.bite_attack_damage_radius))

        data.write(b'\xdfclK')  # 0xdf636c4b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.bite_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'&+%\x08')  # 0x262b2508
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.beam_attack_min_range))

        data.write(b'fd]~')  # 0x66645d7e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.beam_attack_max_range))

        data.write(b'\x90\x9e`\x95')  # 0x909e6095
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.beam_attack_min_pause))

        data.write(b'\xd0\xd1\x18\xe3')  # 0xd0d118e3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.beam_attack_max_pause))

        data.write(b'I\xfa\xe1C')  # 0x49fae143
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.electric_effect))

        data.write(b'\x13\xe3\x0eM')  # 0x13e30e4d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.beam_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'h\x0c\xe7\x95')  # 0x680ce795
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.beam_attack_max_angle))

        data.write(b'\xadG\xfe\xbe')  # 0xad47febe
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.beam_attack_sound_one_shot.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x06\xf7\xce\xed')  # 0x6f7ceed
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.burst_attack_min_range))

        data.write(b'F\xb8\xb6\x9b')  # 0x46b8b69b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.burst_attack_max_range))

        data.write(b'\xb0B\x8bp')  # 0xb0428b70
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.burst_attack_min_pause))

        data.write(b'\xf0\r\xf3\x06')  # 0xf00df306
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.burst_attack_max_pause))

        data.write(b'\xb0\x07u\xe6')  # 0xb00775e6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.burst_attack_damage_radius))

        data.write(b'~\xf9\xaag')  # 0x7ef9aa67
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.burst_projectile))

        data.write(b'R\x85\xdb\x00')  # 0x5285db00
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.burst_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'0\xb8\x1a~')  # 0x30b81a7e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.surface_rings_effect))

        data.write(b'\xbfM\xaa\xe6')  # 0xbf4daae6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.shallow_water_ring))

        data.write(b'p$zn')  # 0x70247a6e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.shallow_water_splash))

        data.write(b'\xff\xce\xe1\xa9')  # 0xffcee1a9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.shake_off_visor_effect))

        data.write(b'\xae\x1f*&')  # 0xae1f2a26
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.grapple_swoosh))

        data.write(b'\r\xab\xf0\xaf')  # 0xdabf0af
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.grapple_beam_part))

        data.write(b'\xe5\x17F\xd1')  # 0xe51746d1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.grapple_hit_fx))

        data.write(b',\xe7R\x0f')  # 0x2ce7520f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grapple_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb6\xb9\x07K')  # 0xb6b9074b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grapple_beam_sound_loop.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x05C\x9a\x08')  # 0x5439a08
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.beam_effect))

        data.write(b'\xd4u?\xf4')  # 0xd4753ff4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xd4753ff4))

        data.write(b'\x05\xfc`\x01')  # 0x5fc6001
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x05fc6001))

        data.write(b'\x13\xe5\xb5\x80')  # 0x13e5b580
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x13e5b580))

        data.write(b'\xfco\x19\x9d')  # 0xfc6f199d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfc6f199d))

        data.write(b'\xf6P%\x96')  # 0xf6502596
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.grapple_visor_effect))

        data.write(b'n\xc2d\x14')  # 0x6ec26414
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.electrified_contact_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'T\xb6\xbf\xa1')  # 0x54b6bfa1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.electrified_visor_effect))

        data.write(b'\\\xf7\x05\xf2')  # 0x5cf705f2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.electrified_sound_loop.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb9\xf9\xf4\xf2')  # 0xb9f9f4f2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.grapple_guardian_eye_glow))

        data.write(b'\xf6\n\xc5\xcc')  # 0xf60ac5cc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.alternate_scannable_info))

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
        json_data = typing.cast("GrenchlerJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            patterned=PatternedAITypedef.from_json(json_data['patterned']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
            tail_destroyed_health=json_data['tail_destroyed_health'],
            is_grapple_guardian=json_data['is_grapple_guardian'],
            has_health_bar=json_data['has_health_bar'],
            damage_vulnerability=DamageVulnerability.from_json(json_data['damage_vulnerability']),
            tail=AnimationParameters.from_json(json_data['tail']),
            tail_when_underwater=AnimationParameters.from_json(json_data['tail_when_underwater']),
            tailless_model=json_data['tailless_model'],
            tailless_skin_rules=json_data['tailless_skin_rules'],
            tail_dark=AnimationParameters.from_json(json_data['tail_dark']),
            tail_when_underwater_dark=AnimationParameters.from_json(json_data['tail_when_underwater_dark']),
            tailless_model_dark=json_data['tailless_model_dark'],
            tailless_skin_rules_dark=json_data['tailless_skin_rules_dark'],
            tail_hit_sound=json_data['tail_hit_sound'],
            tail_destroyed_sound=json_data['tail_destroyed_sound'],
            min_time_between_charges=json_data['min_time_between_charges'],
            unknown_0x7bd1a35f=json_data['unknown_0x7bd1a35f'],
            charge_attack_min_range=json_data['charge_attack_min_range'],
            charge_attack_max_range=json_data['charge_attack_max_range'],
            bite_attack_min_range=json_data['bite_attack_min_range'],
            bite_attack_max_range=json_data['bite_attack_max_range'],
            bite_attack_min_pause=json_data['bite_attack_min_pause'],
            bite_attack_max_pause=json_data['bite_attack_max_pause'],
            bite_attack_damage_radius=json_data['bite_attack_damage_radius'],
            bite_damage=DamageInfo.from_json(json_data['bite_damage']),
            beam_attack_min_range=json_data['beam_attack_min_range'],
            beam_attack_max_range=json_data['beam_attack_max_range'],
            beam_attack_min_pause=json_data['beam_attack_min_pause'],
            beam_attack_max_pause=json_data['beam_attack_max_pause'],
            electric_effect=json_data['electric_effect'],
            beam_damage=DamageInfo.from_json(json_data['beam_damage']),
            beam_attack_max_angle=json_data['beam_attack_max_angle'],
            beam_attack_sound_one_shot=AudioPlaybackParms.from_json(json_data['beam_attack_sound_one_shot']),
            burst_attack_min_range=json_data['burst_attack_min_range'],
            burst_attack_max_range=json_data['burst_attack_max_range'],
            burst_attack_min_pause=json_data['burst_attack_min_pause'],
            burst_attack_max_pause=json_data['burst_attack_max_pause'],
            burst_attack_damage_radius=json_data['burst_attack_damage_radius'],
            burst_projectile=json_data['burst_projectile'],
            burst_damage=DamageInfo.from_json(json_data['burst_damage']),
            surface_rings_effect=json_data['surface_rings_effect'],
            shallow_water_ring=json_data['shallow_water_ring'],
            shallow_water_splash=json_data['shallow_water_splash'],
            shake_off_visor_effect=json_data['shake_off_visor_effect'],
            grapple_swoosh=json_data['grapple_swoosh'],
            grapple_beam_part=json_data['grapple_beam_part'],
            grapple_hit_fx=json_data['grapple_hit_fx'],
            grapple_damage=DamageInfo.from_json(json_data['grapple_damage']),
            grapple_beam_sound_loop=AudioPlaybackParms.from_json(json_data['grapple_beam_sound_loop']),
            beam_effect=json_data['beam_effect'],
            unknown_0xd4753ff4=json_data['unknown_0xd4753ff4'],
            unknown_0x05fc6001=json_data['unknown_0x05fc6001'],
            unknown_0x13e5b580=json_data['unknown_0x13e5b580'],
            unknown_0xfc6f199d=json_data['unknown_0xfc6f199d'],
            grapple_visor_effect=json_data['grapple_visor_effect'],
            electrified_contact_damage=DamageInfo.from_json(json_data['electrified_contact_damage']),
            electrified_visor_effect=json_data['electrified_visor_effect'],
            electrified_sound_loop=AudioPlaybackParms.from_json(json_data['electrified_sound_loop']),
            grapple_guardian_eye_glow=json_data['grapple_guardian_eye_glow'],
            alternate_scannable_info=json_data['alternate_scannable_info'],
            ing_possession_data=IngPossessionData.from_json(json_data['ing_possession_data']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'patterned': self.patterned.to_json(),
            'actor_information': self.actor_information.to_json(),
            'tail_destroyed_health': self.tail_destroyed_health,
            'is_grapple_guardian': self.is_grapple_guardian,
            'has_health_bar': self.has_health_bar,
            'damage_vulnerability': self.damage_vulnerability.to_json(),
            'tail': self.tail.to_json(),
            'tail_when_underwater': self.tail_when_underwater.to_json(),
            'tailless_model': self.tailless_model,
            'tailless_skin_rules': self.tailless_skin_rules,
            'tail_dark': self.tail_dark.to_json(),
            'tail_when_underwater_dark': self.tail_when_underwater_dark.to_json(),
            'tailless_model_dark': self.tailless_model_dark,
            'tailless_skin_rules_dark': self.tailless_skin_rules_dark,
            'tail_hit_sound': self.tail_hit_sound,
            'tail_destroyed_sound': self.tail_destroyed_sound,
            'min_time_between_charges': self.min_time_between_charges,
            'unknown_0x7bd1a35f': self.unknown_0x7bd1a35f,
            'charge_attack_min_range': self.charge_attack_min_range,
            'charge_attack_max_range': self.charge_attack_max_range,
            'bite_attack_min_range': self.bite_attack_min_range,
            'bite_attack_max_range': self.bite_attack_max_range,
            'bite_attack_min_pause': self.bite_attack_min_pause,
            'bite_attack_max_pause': self.bite_attack_max_pause,
            'bite_attack_damage_radius': self.bite_attack_damage_radius,
            'bite_damage': self.bite_damage.to_json(),
            'beam_attack_min_range': self.beam_attack_min_range,
            'beam_attack_max_range': self.beam_attack_max_range,
            'beam_attack_min_pause': self.beam_attack_min_pause,
            'beam_attack_max_pause': self.beam_attack_max_pause,
            'electric_effect': self.electric_effect,
            'beam_damage': self.beam_damage.to_json(),
            'beam_attack_max_angle': self.beam_attack_max_angle,
            'beam_attack_sound_one_shot': self.beam_attack_sound_one_shot.to_json(),
            'burst_attack_min_range': self.burst_attack_min_range,
            'burst_attack_max_range': self.burst_attack_max_range,
            'burst_attack_min_pause': self.burst_attack_min_pause,
            'burst_attack_max_pause': self.burst_attack_max_pause,
            'burst_attack_damage_radius': self.burst_attack_damage_radius,
            'burst_projectile': self.burst_projectile,
            'burst_damage': self.burst_damage.to_json(),
            'surface_rings_effect': self.surface_rings_effect,
            'shallow_water_ring': self.shallow_water_ring,
            'shallow_water_splash': self.shallow_water_splash,
            'shake_off_visor_effect': self.shake_off_visor_effect,
            'grapple_swoosh': self.grapple_swoosh,
            'grapple_beam_part': self.grapple_beam_part,
            'grapple_hit_fx': self.grapple_hit_fx,
            'grapple_damage': self.grapple_damage.to_json(),
            'grapple_beam_sound_loop': self.grapple_beam_sound_loop.to_json(),
            'beam_effect': self.beam_effect,
            'unknown_0xd4753ff4': self.unknown_0xd4753ff4,
            'unknown_0x05fc6001': self.unknown_0x05fc6001,
            'unknown_0x13e5b580': self.unknown_0x13e5b580,
            'unknown_0xfc6f199d': self.unknown_0xfc6f199d,
            'grapple_visor_effect': self.grapple_visor_effect,
            'electrified_contact_damage': self.electrified_contact_damage.to_json(),
            'electrified_visor_effect': self.electrified_visor_effect,
            'electrified_sound_loop': self.electrified_sound_loop.to_json(),
            'grapple_guardian_eye_glow': self.grapple_guardian_eye_glow,
            'alternate_scannable_info': self.alternate_scannable_info,
            'ing_possession_data': self.ing_possession_data.to_json(),
        }

    def _dependencies_for_tailless_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.tailless_model)

    def _dependencies_for_tailless_skin_rules(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.tailless_skin_rules)

    def _dependencies_for_tailless_model_dark(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.tailless_model_dark)

    def _dependencies_for_tailless_skin_rules_dark(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.tailless_skin_rules_dark)

    def _dependencies_for_tail_hit_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.tail_hit_sound)

    def _dependencies_for_tail_destroyed_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.tail_destroyed_sound)

    def _dependencies_for_electric_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.electric_effect)

    def _dependencies_for_burst_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.burst_projectile)

    def _dependencies_for_surface_rings_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.surface_rings_effect)

    def _dependencies_for_shallow_water_ring(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shallow_water_ring)

    def _dependencies_for_shallow_water_splash(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shallow_water_splash)

    def _dependencies_for_shake_off_visor_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shake_off_visor_effect)

    def _dependencies_for_grapple_swoosh(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grapple_swoosh)

    def _dependencies_for_grapple_beam_part(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grapple_beam_part)

    def _dependencies_for_grapple_hit_fx(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grapple_hit_fx)

    def _dependencies_for_beam_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.beam_effect)

    def _dependencies_for_grapple_visor_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grapple_visor_effect)

    def _dependencies_for_electrified_visor_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.electrified_visor_effect)

    def _dependencies_for_grapple_guardian_eye_glow(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grapple_guardian_eye_glow)

    def _dependencies_for_alternate_scannable_info(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.alternate_scannable_info)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self.tail.dependencies_for, "tail", "AnimationParameters"),
            (self.tail_when_underwater.dependencies_for, "tail_when_underwater", "AnimationParameters"),
            (self._dependencies_for_tailless_model, "tailless_model", "AssetId"),
            (self._dependencies_for_tailless_skin_rules, "tailless_skin_rules", "AssetId"),
            (self.tail_dark.dependencies_for, "tail_dark", "AnimationParameters"),
            (self.tail_when_underwater_dark.dependencies_for, "tail_when_underwater_dark", "AnimationParameters"),
            (self._dependencies_for_tailless_model_dark, "tailless_model_dark", "AssetId"),
            (self._dependencies_for_tailless_skin_rules_dark, "tailless_skin_rules_dark", "AssetId"),
            (self._dependencies_for_tail_hit_sound, "tail_hit_sound", "int"),
            (self._dependencies_for_tail_destroyed_sound, "tail_destroyed_sound", "int"),
            (self._dependencies_for_electric_effect, "electric_effect", "AssetId"),
            (self.beam_attack_sound_one_shot.dependencies_for, "beam_attack_sound_one_shot", "AudioPlaybackParms"),
            (self._dependencies_for_burst_projectile, "burst_projectile", "AssetId"),
            (self._dependencies_for_surface_rings_effect, "surface_rings_effect", "AssetId"),
            (self._dependencies_for_shallow_water_ring, "shallow_water_ring", "AssetId"),
            (self._dependencies_for_shallow_water_splash, "shallow_water_splash", "AssetId"),
            (self._dependencies_for_shake_off_visor_effect, "shake_off_visor_effect", "AssetId"),
            (self._dependencies_for_grapple_swoosh, "grapple_swoosh", "AssetId"),
            (self._dependencies_for_grapple_beam_part, "grapple_beam_part", "AssetId"),
            (self._dependencies_for_grapple_hit_fx, "grapple_hit_fx", "AssetId"),
            (self.grapple_beam_sound_loop.dependencies_for, "grapple_beam_sound_loop", "AudioPlaybackParms"),
            (self._dependencies_for_beam_effect, "beam_effect", "AssetId"),
            (self._dependencies_for_grapple_visor_effect, "grapple_visor_effect", "AssetId"),
            (self._dependencies_for_electrified_visor_effect, "electrified_visor_effect", "AssetId"),
            (self.electrified_sound_loop.dependencies_for, "electrified_sound_loop", "AudioPlaybackParms"),
            (self._dependencies_for_grapple_guardian_eye_glow, "grapple_guardian_eye_glow", "AssetId"),
            (self._dependencies_for_alternate_scannable_info, "alternate_scannable_info", "AssetId"),
            (self.ing_possession_data.dependencies_for, "ing_possession_data", "IngPossessionData"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for Grenchler.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={'leash_radius': 100.0, 'collision_radius': 1.600000023841858, 'collision_height': 2.5, 'step_up_height': 1.0, 'creature_size': 1})


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_damage_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_tail(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_tail_when_underwater(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_tail_dark(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_tail_when_underwater_dark(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_bite_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0})


def _decode_beam_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0})


def _decode_beam_attack_sound_one_shot(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_burst_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0})


def _decode_grapple_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_grapple_beam_sound_loop(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_electrified_contact_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 5.0})


def _decode_electrified_sound_loop(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_ing_possession_data(data: typing.BinaryIO, game: Game, property_size: int) -> IngPossessionData:
    return IngPossessionData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xb3774750: ('patterned', _decode_patterned),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0x04d51e3a: ('tail_destroyed_health', structs.decode_BIG_f),
    0x33408e7f: ('is_grapple_guardian', structs.decode_BIG_bool_),
    0x67b6ea0b: ('has_health_bar', structs.decode_BIG_bool_),
    0x0a7326a3: ('damage_vulnerability', _decode_damage_vulnerability),
    0xa18f626b: ('tail', _decode_tail),
    0x0abef809: ('tail_when_underwater', _decode_tail_when_underwater),
    0x4f3a4566: ('tailless_model', structs.decode_BIG_L),
    0x401bc111: ('tailless_skin_rules', structs.decode_BIG_L),
    0x9b193ae8: ('tail_dark', _decode_tail_dark),
    0xc24cf580: ('tail_when_underwater_dark', _decode_tail_when_underwater_dark),
    0x72258fe7: ('tailless_model_dark', structs.decode_BIG_L),
    0xe5fba24c: ('tailless_skin_rules_dark', structs.decode_BIG_L),
    0x55c51213: ('tail_hit_sound', structs.decode_BIG_l),
    0x385e4738: ('tail_destroyed_sound', structs.decode_BIG_l),
    0x5d8f2bee: ('min_time_between_charges', structs.decode_BIG_f),
    0x7bd1a35f: ('unknown_0x7bd1a35f', structs.decode_BIG_f),
    0xea4b88c8: ('charge_attack_min_range', structs.decode_BIG_f),
    0xaa04f0be: ('charge_attack_max_range', structs.decode_BIG_f),
    0x98d5d373: ('bite_attack_min_range', structs.decode_BIG_f),
    0xd89aab05: ('bite_attack_max_range', structs.decode_BIG_f),
    0x2e6096ee: ('bite_attack_min_pause', structs.decode_BIG_f),
    0x6e2fee98: ('bite_attack_max_pause', structs.decode_BIG_f),
    0x49632b31: ('bite_attack_damage_radius', structs.decode_BIG_f),
    0xdf636c4b: ('bite_damage', _decode_bite_damage),
    0x262b2508: ('beam_attack_min_range', structs.decode_BIG_f),
    0x66645d7e: ('beam_attack_max_range', structs.decode_BIG_f),
    0x909e6095: ('beam_attack_min_pause', structs.decode_BIG_f),
    0xd0d118e3: ('beam_attack_max_pause', structs.decode_BIG_f),
    0x49fae143: ('electric_effect', structs.decode_BIG_L),
    0x13e30e4d: ('beam_damage', _decode_beam_damage),
    0x680ce795: ('beam_attack_max_angle', structs.decode_BIG_f),
    0xad47febe: ('beam_attack_sound_one_shot', _decode_beam_attack_sound_one_shot),
    0x06f7ceed: ('burst_attack_min_range', structs.decode_BIG_f),
    0x46b8b69b: ('burst_attack_max_range', structs.decode_BIG_f),
    0xb0428b70: ('burst_attack_min_pause', structs.decode_BIG_f),
    0xf00df306: ('burst_attack_max_pause', structs.decode_BIG_f),
    0xb00775e6: ('burst_attack_damage_radius', structs.decode_BIG_f),
    0x7ef9aa67: ('burst_projectile', structs.decode_BIG_L),
    0x5285db00: ('burst_damage', _decode_burst_damage),
    0x30b81a7e: ('surface_rings_effect', structs.decode_BIG_L),
    0xbf4daae6: ('shallow_water_ring', structs.decode_BIG_L),
    0x70247a6e: ('shallow_water_splash', structs.decode_BIG_L),
    0xffcee1a9: ('shake_off_visor_effect', structs.decode_BIG_L),
    0xae1f2a26: ('grapple_swoosh', structs.decode_BIG_L),
    0x0dabf0af: ('grapple_beam_part', structs.decode_BIG_L),
    0xe51746d1: ('grapple_hit_fx', structs.decode_BIG_L),
    0x2ce7520f: ('grapple_damage', _decode_grapple_damage),
    0xb6b9074b: ('grapple_beam_sound_loop', _decode_grapple_beam_sound_loop),
    0x05439a08: ('beam_effect', structs.decode_BIG_L),
    0xd4753ff4: ('unknown_0xd4753ff4', structs.decode_BIG_l),
    0x05fc6001: ('unknown_0x05fc6001', structs.decode_BIG_f),
    0x13e5b580: ('unknown_0x13e5b580', structs.decode_BIG_f),
    0xfc6f199d: ('unknown_0xfc6f199d', structs.decode_BIG_f),
    0xf6502596: ('grapple_visor_effect', structs.decode_BIG_L),
    0x6ec26414: ('electrified_contact_damage', _decode_electrified_contact_damage),
    0x54b6bfa1: ('electrified_visor_effect', structs.decode_BIG_L),
    0x5cf705f2: ('electrified_sound_loop', _decode_electrified_sound_loop),
    0xb9f9f4f2: ('grapple_guardian_eye_glow', structs.decode_BIG_L),
    0xf60ac5cc: ('alternate_scannable_info', structs.decode_BIG_L),
    0xe61748ed: ('ing_possession_data', _decode_ing_possession_data),
}
