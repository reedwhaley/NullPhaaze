# Generated File
from __future__ import annotations

import dataclasses
import enum
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
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.PatternedAITypedef import PatternedAITypedef
from retro_data_structures.properties.echoes.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class IngJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        patterned: json_util.JsonObject
        actor_information: json_util.JsonObject
        ing_flags: int
        face_plate_model: int
        hearing_radius: float
        ing_spot_max_speed: float
        ing_spot_max_wall_speed: float
        ing_spot_ball_pursuit_speed: float
        ing_spot_max_hurried_speed: float
        ing_spot_turn_speed: float
        ing_spot_blob_effect: int
        ing_spot_hit_normal_damage: int
        ing_spot_hit_heavy_damage: int
        ing_spot_death: int
        sound_ing_spot_idle: int
        sound_ing_spot_move: int
        sound_hit_normal_damage: int
        sound_hit_heavy_damage: int
        sound_ing_spot_death: int
        part: int
        exit_host_swarm_effect: int
        exit_host_secondary_swarm_effect: int
        unknown: float
        exit_host_smoke_effect: int
        exit_host_effect_speed: float
        exit_host_initial_tracking_time: float
        exit_host_initial_tracking_dist: float
        sound_swarm_move: int
        sound_inside_host: int
        sound_exit_host: int
        sound_exit_host_safe_zone: int
        sound: int
        cover_point_leash_radius: float
        min_corporeal_time: float
        frustration_time: float
        taunt_chance: float
        aggressiveness: float
        arm_swipe_damage: json_util.JsonObject
        body_projectile_contact_damage: json_util.JsonObject
        body_projectile_suck_damage_per_sec: float
        body_projectile_suck_time: float
        body_projectile_splat_effect: int
        body_projectile_speed: float
        body_projectile_drop_time: float
        body_projectile_min_attack_dist: float
        body_projectile_max_attack_dist: float
        sound_body_projectile: int
        sound_body_projectile_splat_wall: int
        body_projectile_odds: float
        mini_portal_min_attack_dist: float
        mini_portal_max_attack_dist: float
        mini_portal_effect: int
        sound_mini_portal: int
        mini_portal_projectile_damage: json_util.JsonObject
        mini_portal_beam_info: json_util.JsonObject
        grab_morphball_damage_per_sec: float
        exit_grapple_damage: json_util.JsonObject
        exit_grapple_spit_force: float
        sound_grapple: int
        sound_exit_grapple: int
        max_grapple_ball_hold_time: float
        grapple_ball_pursuit_range: float
        post_grapple_ball_wait_time: float
        light_color: json_util.JsonValue
        light_attenuation: float
        ing_spot_vulnerability: json_util.JsonObject
        grapple_ball_vulnerability: json_util.JsonObject
        trigger_vulnerability: json_util.JsonObject
    

class IngFlags(enum.IntFlag):
    StartsAsIngSpot = 1
    DisableArmSwipe = 2
    DisableBodyProjectile = 4
    DisableMiniPortal = 8
    DisableGrapple = 16
    DisableFormChange = 32
    DisablePathMovement = 64
    AlwaysTargetable = 128

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


@dataclasses.dataclass()
class Ing(BaseObjectType):
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
    ing_flags: IngFlags = dataclasses.field(default=IngFlags(0), metadata={
        'reflection': FieldReflection[IngFlags](
            IngFlags, id=0x092fbad0, original_name='IngFlags', from_json=IngFlags.from_json, to_json=IngFlags.to_json
        ),
    })
    face_plate_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xbdcce71b, original_name='FacePlateModel'
        ),
    })
    hearing_radius: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xed69488f, original_name='HearingRadius'
        ),
    })
    ing_spot_max_speed: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x95b47cf9, original_name='IngSpotMaxSpeed'
        ),
    })
    ing_spot_max_wall_speed: float = dataclasses.field(default=7.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8d42a8d5, original_name='IngSpotMaxWallSpeed'
        ),
    })
    ing_spot_ball_pursuit_speed: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x84586bfd, original_name='IngSpotBallPursuitSpeed'
        ),
    })
    ing_spot_max_hurried_speed: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x50398a06, original_name='IngSpotMaxHurriedSpeed'
        ),
    })
    ing_spot_turn_speed: float = dataclasses.field(default=360.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xeaa3c3f8, original_name='IngSpotTurnSpeed'
        ),
    })
    ing_spot_blob_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xcc5a4918, original_name='IngSpotBlobEffect'
        ),
    })
    ing_spot_hit_normal_damage: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x8851dc01, original_name='IngSpotHitNormalDamage'
        ),
    })
    ing_spot_hit_heavy_damage: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5d01100f, original_name='IngSpotHitHeavyDamage'
        ),
    })
    ing_spot_death: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x9a56892e, original_name='IngSpotDeath'
        ),
    })
    sound_ing_spot_idle: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x4cab30a9, original_name='Sound_IngSpotIdle'
        ),
    })
    sound_ing_spot_move: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x8f83be73, original_name='Sound_IngSpotMove'
        ),
    })
    sound_hit_normal_damage: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xb392943a, original_name='Sound_HitNormalDamage'
        ),
    })
    sound_hit_heavy_damage: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x24ecc1e9, original_name='Sound_HitHeavyDamage'
        ),
    })
    sound_ing_spot_death: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x4489935e, original_name='Sound_IngSpotDeath'
        ),
    })
    part: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3c2d681e, original_name='PART'
        ),
    })
    exit_host_swarm_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SRSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd576f379, original_name='ExitHostSwarmEffect'
        ),
    })
    exit_host_secondary_swarm_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3da219c7, original_name='ExitHostSecondarySwarmEffect'
        ),
    })
    unknown: float = dataclasses.field(default=0.3499999940395355, metadata={
        'reflection': FieldReflection[float](
            float, id=0x23271976, original_name='Unknown'
        ),
    })
    exit_host_smoke_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x081e9e6c, original_name='ExitHostSmokeEffect'
        ),
    })
    exit_host_effect_speed: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcb39eccb, original_name='ExitHostEffectSpeed'
        ),
    })
    exit_host_initial_tracking_time: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x587ca175, original_name='ExitHostInitialTrackingTime'
        ),
    })
    exit_host_initial_tracking_dist: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0bd7d5a9, original_name='ExitHostInitialTrackingDist'
        ),
    })
    sound_swarm_move: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xe8ea5bc8, original_name='Sound_SwarmMove'
        ),
    })
    sound_inside_host: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x5650366a, original_name='Sound_InsideHost'
        ),
    })
    sound_exit_host: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xb09af706, original_name='Sound_ExitHost'
        ),
    })
    sound_exit_host_safe_zone: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x0c13c5a8, original_name='Sound_ExitHostSafeZone'
        ),
    })
    sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x148b81e4, original_name='Sound'
        ),
    })
    cover_point_leash_radius: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5d0d2c40, original_name='CoverPointLeashRadius'
        ),
    })
    min_corporeal_time: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc620183a, original_name='MinCorporealTime'
        ),
    })
    frustration_time: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7d19c3ca, original_name='FrustrationTime'
        ),
    })
    taunt_chance: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa77f6212, original_name='TauntChance'
        ),
    })
    aggressiveness: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9579b1f2, original_name='Aggressiveness'
        ),
    })
    arm_swipe_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x915da374, original_name='ArmSwipeDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    body_projectile_contact_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xab258f6b, original_name='BodyProjectileContactDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    body_projectile_suck_damage_per_sec: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa0d63374, original_name='BodyProjectileSuckDamagePerSec'
        ),
    })
    body_projectile_suck_time: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdfea60a2, original_name='BodyProjectileSuckTime'
        ),
    })
    body_projectile_splat_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x601cc5b4, original_name='BodyProjectileSplatEffect'
        ),
    })
    body_projectile_speed: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xce980820, original_name='BodyProjectileSpeed'
        ),
    })
    body_projectile_drop_time: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb752c177, original_name='BodyProjectileDropTime'
        ),
    })
    body_projectile_min_attack_dist: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe6ddb662, original_name='BodyProjectileMinAttackDist'
        ),
    })
    body_projectile_max_attack_dist: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb57bae86, original_name='BodyProjectileMaxAttackDist'
        ),
    })
    sound_body_projectile: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x2025858b, original_name='Sound_BodyProjectile'
        ),
    })
    sound_body_projectile_splat_wall: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x19f8fee6, original_name='Sound_BodyProjectileSplatWall'
        ),
    })
    body_projectile_odds: float = dataclasses.field(default=70.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdc741fbd, original_name='BodyProjectileOdds'
        ),
    })
    mini_portal_min_attack_dist: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfa6edeb5, original_name='MiniPortalMinAttackDist'
        ),
    })
    mini_portal_max_attack_dist: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa9c8c651, original_name='MiniPortalMaxAttackDist'
        ),
    })
    mini_portal_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa926f8a8, original_name='MiniPortalEffect'
        ),
    })
    sound_mini_portal: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x4051fd1a, original_name='Sound_MiniPortal'
        ),
    })
    mini_portal_projectile_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x424a6d37, original_name='MiniPortalProjectileDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    mini_portal_beam_info: PlasmaBeamInfo = dataclasses.field(default_factory=PlasmaBeamInfo, metadata={
        'reflection': FieldReflection[PlasmaBeamInfo](
            PlasmaBeamInfo, id=0x9c170968, original_name='MiniPortalBeamInfo', from_json=PlasmaBeamInfo.from_json, to_json=PlasmaBeamInfo.to_json
        ),
    })
    grab_morphball_damage_per_sec: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x67f6c10e, original_name='GrabMorphballDamagePerSec'
        ),
    })
    exit_grapple_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x11c36d8e, original_name='ExitGrappleDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    exit_grapple_spit_force: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc2320b06, original_name='ExitGrappleSpitForce'
        ),
    })
    sound_grapple: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x4832703b, original_name='Sound_Grapple'
        ),
    })
    sound_exit_grapple: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x36b0e542, original_name='Sound_ExitGrapple'
        ),
    })
    max_grapple_ball_hold_time: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x421651f6, original_name='MaxGrappleBallHoldTime'
        ),
    })
    grapple_ball_pursuit_range: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x560b4a95, original_name='GrappleBallPursuitRange'
        ),
    })
    post_grapple_ball_wait_time: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8bdcc614, original_name='PostGrappleBallWaitTime'
        ),
    })
    light_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xbd3efe7d, original_name='LightColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    light_attenuation: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd24b888f, original_name='LightAttenuation'
        ),
    })
    ing_spot_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x1b96ff8b, original_name='IngSpotVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    grapple_ball_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x33737ea6, original_name='GrappleBallVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    trigger_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x23399d21, original_name='TriggerVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'INGS'

    @classmethod
    def modules(cls) -> list[str]:
        return ['GeomBlobV2.rel', 'Ing.rel']

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
        if property_count != 69:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3774750
        patterned = PatternedAITypedef.from_stream(data, game, property_size, default_override={'turn_speed': 360.0, 'min_attack_range': 0.0, 'creature_size': 1})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e397fed
        actor_information = ActorParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x092fbad0
        ing_flags = IngFlags.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbdcce71b
        face_plate_model = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed69488f
        hearing_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95b47cf9
        ing_spot_max_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8d42a8d5
        ing_spot_max_wall_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x84586bfd
        ing_spot_ball_pursuit_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50398a06
        ing_spot_max_hurried_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xeaa3c3f8
        ing_spot_turn_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcc5a4918
        ing_spot_blob_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8851dc01
        ing_spot_hit_normal_damage = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5d01100f
        ing_spot_hit_heavy_damage = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9a56892e
        ing_spot_death = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4cab30a9
        sound_ing_spot_idle = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8f83be73
        sound_ing_spot_move = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb392943a
        sound_hit_normal_damage = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24ecc1e9
        sound_hit_heavy_damage = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4489935e
        sound_ing_spot_death = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3c2d681e
        part = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd576f379
        exit_host_swarm_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3da219c7
        exit_host_secondary_swarm_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23271976
        unknown = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x081e9e6c
        exit_host_smoke_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcb39eccb
        exit_host_effect_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x587ca175
        exit_host_initial_tracking_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0bd7d5a9
        exit_host_initial_tracking_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe8ea5bc8
        sound_swarm_move = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5650366a
        sound_inside_host = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb09af706
        sound_exit_host = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0c13c5a8
        sound_exit_host_safe_zone = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x148b81e4
        sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5d0d2c40
        cover_point_leash_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc620183a
        min_corporeal_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7d19c3ca
        frustration_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa77f6212
        taunt_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9579b1f2
        aggressiveness = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x915da374
        arm_swipe_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xab258f6b
        body_projectile_contact_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa0d63374
        body_projectile_suck_damage_per_sec = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdfea60a2
        body_projectile_suck_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x601cc5b4
        body_projectile_splat_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xce980820
        body_projectile_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb752c177
        body_projectile_drop_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe6ddb662
        body_projectile_min_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb57bae86
        body_projectile_max_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2025858b
        sound_body_projectile = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19f8fee6
        sound_body_projectile_splat_wall = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdc741fbd
        body_projectile_odds = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfa6edeb5
        mini_portal_min_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa9c8c651
        mini_portal_max_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa926f8a8
        mini_portal_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4051fd1a
        sound_mini_portal = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x424a6d37
        mini_portal_projectile_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9c170968
        mini_portal_beam_info = PlasmaBeamInfo.from_stream(data, game, property_size, default_override={'length': 500.0, 'expansion_speed': 4.0, 'life_time': 1.0, 'pulse_speed': 20.0, 'shutdown_time': 0.25, 'pulse_effect_scale': 2.0, 'inner_color': Color(r=0.5, g=0.5, b=0.5, a=0.5), 'outer_color': Color(r=0.6000000238418579, g=0.6000000238418579, b=0.0, a=0.5)})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x67f6c10e
        grab_morphball_damage_per_sec = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x11c36d8e
        exit_grapple_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 10.0, 'di_knock_back_power': 1.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc2320b06
        exit_grapple_spit_force = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4832703b
        sound_grapple = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x36b0e542
        sound_exit_grapple = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x421651f6
        max_grapple_ball_hold_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x560b4a95
        grapple_ball_pursuit_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8bdcc614
        post_grapple_ball_wait_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbd3efe7d
        light_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd24b888f
        light_attenuation = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1b96ff8b
        ing_spot_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33737ea6
        grapple_ball_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23399d21
        trigger_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        return cls(editor_properties, patterned, actor_information, ing_flags, face_plate_model, hearing_radius, ing_spot_max_speed, ing_spot_max_wall_speed, ing_spot_ball_pursuit_speed, ing_spot_max_hurried_speed, ing_spot_turn_speed, ing_spot_blob_effect, ing_spot_hit_normal_damage, ing_spot_hit_heavy_damage, ing_spot_death, sound_ing_spot_idle, sound_ing_spot_move, sound_hit_normal_damage, sound_hit_heavy_damage, sound_ing_spot_death, part, exit_host_swarm_effect, exit_host_secondary_swarm_effect, unknown, exit_host_smoke_effect, exit_host_effect_speed, exit_host_initial_tracking_time, exit_host_initial_tracking_dist, sound_swarm_move, sound_inside_host, sound_exit_host, sound_exit_host_safe_zone, sound, cover_point_leash_radius, min_corporeal_time, frustration_time, taunt_chance, aggressiveness, arm_swipe_damage, body_projectile_contact_damage, body_projectile_suck_damage_per_sec, body_projectile_suck_time, body_projectile_splat_effect, body_projectile_speed, body_projectile_drop_time, body_projectile_min_attack_dist, body_projectile_max_attack_dist, sound_body_projectile, sound_body_projectile_splat_wall, body_projectile_odds, mini_portal_min_attack_dist, mini_portal_max_attack_dist, mini_portal_effect, sound_mini_portal, mini_portal_projectile_damage, mini_portal_beam_info, grab_morphball_damage_per_sec, exit_grapple_damage, exit_grapple_spit_force, sound_grapple, sound_exit_grapple, max_grapple_ball_hold_time, grapple_ball_pursuit_range, post_grapple_ball_wait_time, light_color, light_attenuation, ing_spot_vulnerability, grapple_ball_vulnerability, trigger_vulnerability)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00E')  # 69 properties

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
        self.patterned.to_stream(data, game, default_override={'turn_speed': 360.0, 'min_attack_range': 0.0, 'creature_size': 1})
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

        data.write(b'\t/\xba\xd0')  # 0x92fbad0
        data.write(b'\x00\x04')  # size
        self.ing_flags.to_stream(data, game)

        data.write(b'\xbd\xcc\xe7\x1b')  # 0xbdcce71b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.face_plate_model))

        data.write(b'\xediH\x8f')  # 0xed69488f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hearing_radius))

        data.write(b'\x95\xb4|\xf9')  # 0x95b47cf9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ing_spot_max_speed))

        data.write(b'\x8dB\xa8\xd5')  # 0x8d42a8d5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ing_spot_max_wall_speed))

        data.write(b'\x84Xk\xfd')  # 0x84586bfd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ing_spot_ball_pursuit_speed))

        data.write(b'P9\x8a\x06')  # 0x50398a06
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ing_spot_max_hurried_speed))

        data.write(b'\xea\xa3\xc3\xf8')  # 0xeaa3c3f8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ing_spot_turn_speed))

        data.write(b'\xccZI\x18')  # 0xcc5a4918
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.ing_spot_blob_effect))

        data.write(b'\x88Q\xdc\x01')  # 0x8851dc01
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.ing_spot_hit_normal_damage))

        data.write(b']\x01\x10\x0f')  # 0x5d01100f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.ing_spot_hit_heavy_damage))

        data.write(b'\x9aV\x89.')  # 0x9a56892e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.ing_spot_death))

        data.write(b'L\xab0\xa9')  # 0x4cab30a9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_ing_spot_idle))

        data.write(b'\x8f\x83\xbes')  # 0x8f83be73
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_ing_spot_move))

        data.write(b'\xb3\x92\x94:')  # 0xb392943a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_hit_normal_damage))

        data.write(b'$\xec\xc1\xe9')  # 0x24ecc1e9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_hit_heavy_damage))

        data.write(b'D\x89\x93^')  # 0x4489935e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_ing_spot_death))

        data.write(b'<-h\x1e')  # 0x3c2d681e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.part))

        data.write(b'\xd5v\xf3y')  # 0xd576f379
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.exit_host_swarm_effect))

        data.write(b'=\xa2\x19\xc7')  # 0x3da219c7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.exit_host_secondary_swarm_effect))

        data.write(b"#'\x19v")  # 0x23271976
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b'\x08\x1e\x9el')  # 0x81e9e6c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.exit_host_smoke_effect))

        data.write(b'\xcb9\xec\xcb')  # 0xcb39eccb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.exit_host_effect_speed))

        data.write(b'X|\xa1u')  # 0x587ca175
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.exit_host_initial_tracking_time))

        data.write(b'\x0b\xd7\xd5\xa9')  # 0xbd7d5a9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.exit_host_initial_tracking_dist))

        data.write(b'\xe8\xea[\xc8')  # 0xe8ea5bc8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_swarm_move))

        data.write(b'VP6j')  # 0x5650366a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_inside_host))

        data.write(b'\xb0\x9a\xf7\x06')  # 0xb09af706
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_exit_host))

        data.write(b'\x0c\x13\xc5\xa8')  # 0xc13c5a8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_exit_host_safe_zone))

        data.write(b'\x14\x8b\x81\xe4')  # 0x148b81e4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound))

        data.write(b']\r,@')  # 0x5d0d2c40
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.cover_point_leash_radius))

        data.write(b'\xc6 \x18:')  # 0xc620183a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_corporeal_time))

        data.write(b'}\x19\xc3\xca')  # 0x7d19c3ca
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.frustration_time))

        data.write(b'\xa7\x7fb\x12')  # 0xa77f6212
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.taunt_chance))

        data.write(b'\x95y\xb1\xf2')  # 0x9579b1f2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aggressiveness))

        data.write(b'\x91]\xa3t')  # 0x915da374
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.arm_swipe_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xab%\x8fk')  # 0xab258f6b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.body_projectile_contact_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa0\xd63t')  # 0xa0d63374
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.body_projectile_suck_damage_per_sec))

        data.write(b'\xdf\xea`\xa2')  # 0xdfea60a2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.body_projectile_suck_time))

        data.write(b'`\x1c\xc5\xb4')  # 0x601cc5b4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.body_projectile_splat_effect))

        data.write(b'\xce\x98\x08 ')  # 0xce980820
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.body_projectile_speed))

        data.write(b'\xb7R\xc1w')  # 0xb752c177
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.body_projectile_drop_time))

        data.write(b'\xe6\xdd\xb6b')  # 0xe6ddb662
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.body_projectile_min_attack_dist))

        data.write(b'\xb5{\xae\x86')  # 0xb57bae86
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.body_projectile_max_attack_dist))

        data.write(b' %\x85\x8b')  # 0x2025858b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_body_projectile))

        data.write(b'\x19\xf8\xfe\xe6')  # 0x19f8fee6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_body_projectile_splat_wall))

        data.write(b'\xdct\x1f\xbd')  # 0xdc741fbd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.body_projectile_odds))

        data.write(b'\xfan\xde\xb5')  # 0xfa6edeb5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.mini_portal_min_attack_dist))

        data.write(b'\xa9\xc8\xc6Q')  # 0xa9c8c651
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.mini_portal_max_attack_dist))

        data.write(b'\xa9&\xf8\xa8')  # 0xa926f8a8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.mini_portal_effect))

        data.write(b'@Q\xfd\x1a')  # 0x4051fd1a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_mini_portal))

        data.write(b'BJm7')  # 0x424a6d37
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.mini_portal_projectile_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9c\x17\th')  # 0x9c170968
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.mini_portal_beam_info.to_stream(data, game, default_override={'length': 500.0, 'expansion_speed': 4.0, 'life_time': 1.0, 'pulse_speed': 20.0, 'shutdown_time': 0.25, 'pulse_effect_scale': 2.0, 'inner_color': Color(r=0.5, g=0.5, b=0.5, a=0.5), 'outer_color': Color(r=0.6000000238418579, g=0.6000000238418579, b=0.0, a=0.5)})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'g\xf6\xc1\x0e')  # 0x67f6c10e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grab_morphball_damage_per_sec))

        data.write(b'\x11\xc3m\x8e')  # 0x11c36d8e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.exit_grapple_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 10.0, 'di_knock_back_power': 1.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc22\x0b\x06')  # 0xc2320b06
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.exit_grapple_spit_force))

        data.write(b'H2p;')  # 0x4832703b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_grapple))

        data.write(b'6\xb0\xe5B')  # 0x36b0e542
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_exit_grapple))

        data.write(b'B\x16Q\xf6')  # 0x421651f6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_grapple_ball_hold_time))

        data.write(b'V\x0bJ\x95')  # 0x560b4a95
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grapple_ball_pursuit_range))

        data.write(b'\x8b\xdc\xc6\x14')  # 0x8bdcc614
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.post_grapple_ball_wait_time))

        data.write(b'\xbd>\xfe}')  # 0xbd3efe7d
        data.write(b'\x00\x10')  # size
        self.light_color.to_stream(data, game)

        data.write(b'\xd2K\x88\x8f')  # 0xd24b888f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.light_attenuation))

        data.write(b'\x1b\x96\xff\x8b')  # 0x1b96ff8b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ing_spot_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'3s~\xa6')  # 0x33737ea6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grapple_ball_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'#9\x9d!')  # 0x23399d21
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.trigger_vulnerability.to_stream(data, game)
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
        json_data = typing.cast("IngJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            patterned=PatternedAITypedef.from_json(json_data['patterned']),
            actor_information=ActorParameters.from_json(json_data['actor_information']),
            ing_flags=IngFlags.from_json(json_data['ing_flags']),
            face_plate_model=json_data['face_plate_model'],
            hearing_radius=json_data['hearing_radius'],
            ing_spot_max_speed=json_data['ing_spot_max_speed'],
            ing_spot_max_wall_speed=json_data['ing_spot_max_wall_speed'],
            ing_spot_ball_pursuit_speed=json_data['ing_spot_ball_pursuit_speed'],
            ing_spot_max_hurried_speed=json_data['ing_spot_max_hurried_speed'],
            ing_spot_turn_speed=json_data['ing_spot_turn_speed'],
            ing_spot_blob_effect=json_data['ing_spot_blob_effect'],
            ing_spot_hit_normal_damage=json_data['ing_spot_hit_normal_damage'],
            ing_spot_hit_heavy_damage=json_data['ing_spot_hit_heavy_damage'],
            ing_spot_death=json_data['ing_spot_death'],
            sound_ing_spot_idle=json_data['sound_ing_spot_idle'],
            sound_ing_spot_move=json_data['sound_ing_spot_move'],
            sound_hit_normal_damage=json_data['sound_hit_normal_damage'],
            sound_hit_heavy_damage=json_data['sound_hit_heavy_damage'],
            sound_ing_spot_death=json_data['sound_ing_spot_death'],
            part=json_data['part'],
            exit_host_swarm_effect=json_data['exit_host_swarm_effect'],
            exit_host_secondary_swarm_effect=json_data['exit_host_secondary_swarm_effect'],
            unknown=json_data['unknown'],
            exit_host_smoke_effect=json_data['exit_host_smoke_effect'],
            exit_host_effect_speed=json_data['exit_host_effect_speed'],
            exit_host_initial_tracking_time=json_data['exit_host_initial_tracking_time'],
            exit_host_initial_tracking_dist=json_data['exit_host_initial_tracking_dist'],
            sound_swarm_move=json_data['sound_swarm_move'],
            sound_inside_host=json_data['sound_inside_host'],
            sound_exit_host=json_data['sound_exit_host'],
            sound_exit_host_safe_zone=json_data['sound_exit_host_safe_zone'],
            sound=json_data['sound'],
            cover_point_leash_radius=json_data['cover_point_leash_radius'],
            min_corporeal_time=json_data['min_corporeal_time'],
            frustration_time=json_data['frustration_time'],
            taunt_chance=json_data['taunt_chance'],
            aggressiveness=json_data['aggressiveness'],
            arm_swipe_damage=DamageInfo.from_json(json_data['arm_swipe_damage']),
            body_projectile_contact_damage=DamageInfo.from_json(json_data['body_projectile_contact_damage']),
            body_projectile_suck_damage_per_sec=json_data['body_projectile_suck_damage_per_sec'],
            body_projectile_suck_time=json_data['body_projectile_suck_time'],
            body_projectile_splat_effect=json_data['body_projectile_splat_effect'],
            body_projectile_speed=json_data['body_projectile_speed'],
            body_projectile_drop_time=json_data['body_projectile_drop_time'],
            body_projectile_min_attack_dist=json_data['body_projectile_min_attack_dist'],
            body_projectile_max_attack_dist=json_data['body_projectile_max_attack_dist'],
            sound_body_projectile=json_data['sound_body_projectile'],
            sound_body_projectile_splat_wall=json_data['sound_body_projectile_splat_wall'],
            body_projectile_odds=json_data['body_projectile_odds'],
            mini_portal_min_attack_dist=json_data['mini_portal_min_attack_dist'],
            mini_portal_max_attack_dist=json_data['mini_portal_max_attack_dist'],
            mini_portal_effect=json_data['mini_portal_effect'],
            sound_mini_portal=json_data['sound_mini_portal'],
            mini_portal_projectile_damage=DamageInfo.from_json(json_data['mini_portal_projectile_damage']),
            mini_portal_beam_info=PlasmaBeamInfo.from_json(json_data['mini_portal_beam_info']),
            grab_morphball_damage_per_sec=json_data['grab_morphball_damage_per_sec'],
            exit_grapple_damage=DamageInfo.from_json(json_data['exit_grapple_damage']),
            exit_grapple_spit_force=json_data['exit_grapple_spit_force'],
            sound_grapple=json_data['sound_grapple'],
            sound_exit_grapple=json_data['sound_exit_grapple'],
            max_grapple_ball_hold_time=json_data['max_grapple_ball_hold_time'],
            grapple_ball_pursuit_range=json_data['grapple_ball_pursuit_range'],
            post_grapple_ball_wait_time=json_data['post_grapple_ball_wait_time'],
            light_color=Color.from_json(json_data['light_color']),
            light_attenuation=json_data['light_attenuation'],
            ing_spot_vulnerability=DamageVulnerability.from_json(json_data['ing_spot_vulnerability']),
            grapple_ball_vulnerability=DamageVulnerability.from_json(json_data['grapple_ball_vulnerability']),
            trigger_vulnerability=DamageVulnerability.from_json(json_data['trigger_vulnerability']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'patterned': self.patterned.to_json(),
            'actor_information': self.actor_information.to_json(),
            'ing_flags': self.ing_flags.to_json(),
            'face_plate_model': self.face_plate_model,
            'hearing_radius': self.hearing_radius,
            'ing_spot_max_speed': self.ing_spot_max_speed,
            'ing_spot_max_wall_speed': self.ing_spot_max_wall_speed,
            'ing_spot_ball_pursuit_speed': self.ing_spot_ball_pursuit_speed,
            'ing_spot_max_hurried_speed': self.ing_spot_max_hurried_speed,
            'ing_spot_turn_speed': self.ing_spot_turn_speed,
            'ing_spot_blob_effect': self.ing_spot_blob_effect,
            'ing_spot_hit_normal_damage': self.ing_spot_hit_normal_damage,
            'ing_spot_hit_heavy_damage': self.ing_spot_hit_heavy_damage,
            'ing_spot_death': self.ing_spot_death,
            'sound_ing_spot_idle': self.sound_ing_spot_idle,
            'sound_ing_spot_move': self.sound_ing_spot_move,
            'sound_hit_normal_damage': self.sound_hit_normal_damage,
            'sound_hit_heavy_damage': self.sound_hit_heavy_damage,
            'sound_ing_spot_death': self.sound_ing_spot_death,
            'part': self.part,
            'exit_host_swarm_effect': self.exit_host_swarm_effect,
            'exit_host_secondary_swarm_effect': self.exit_host_secondary_swarm_effect,
            'unknown': self.unknown,
            'exit_host_smoke_effect': self.exit_host_smoke_effect,
            'exit_host_effect_speed': self.exit_host_effect_speed,
            'exit_host_initial_tracking_time': self.exit_host_initial_tracking_time,
            'exit_host_initial_tracking_dist': self.exit_host_initial_tracking_dist,
            'sound_swarm_move': self.sound_swarm_move,
            'sound_inside_host': self.sound_inside_host,
            'sound_exit_host': self.sound_exit_host,
            'sound_exit_host_safe_zone': self.sound_exit_host_safe_zone,
            'sound': self.sound,
            'cover_point_leash_radius': self.cover_point_leash_radius,
            'min_corporeal_time': self.min_corporeal_time,
            'frustration_time': self.frustration_time,
            'taunt_chance': self.taunt_chance,
            'aggressiveness': self.aggressiveness,
            'arm_swipe_damage': self.arm_swipe_damage.to_json(),
            'body_projectile_contact_damage': self.body_projectile_contact_damage.to_json(),
            'body_projectile_suck_damage_per_sec': self.body_projectile_suck_damage_per_sec,
            'body_projectile_suck_time': self.body_projectile_suck_time,
            'body_projectile_splat_effect': self.body_projectile_splat_effect,
            'body_projectile_speed': self.body_projectile_speed,
            'body_projectile_drop_time': self.body_projectile_drop_time,
            'body_projectile_min_attack_dist': self.body_projectile_min_attack_dist,
            'body_projectile_max_attack_dist': self.body_projectile_max_attack_dist,
            'sound_body_projectile': self.sound_body_projectile,
            'sound_body_projectile_splat_wall': self.sound_body_projectile_splat_wall,
            'body_projectile_odds': self.body_projectile_odds,
            'mini_portal_min_attack_dist': self.mini_portal_min_attack_dist,
            'mini_portal_max_attack_dist': self.mini_portal_max_attack_dist,
            'mini_portal_effect': self.mini_portal_effect,
            'sound_mini_portal': self.sound_mini_portal,
            'mini_portal_projectile_damage': self.mini_portal_projectile_damage.to_json(),
            'mini_portal_beam_info': self.mini_portal_beam_info.to_json(),
            'grab_morphball_damage_per_sec': self.grab_morphball_damage_per_sec,
            'exit_grapple_damage': self.exit_grapple_damage.to_json(),
            'exit_grapple_spit_force': self.exit_grapple_spit_force,
            'sound_grapple': self.sound_grapple,
            'sound_exit_grapple': self.sound_exit_grapple,
            'max_grapple_ball_hold_time': self.max_grapple_ball_hold_time,
            'grapple_ball_pursuit_range': self.grapple_ball_pursuit_range,
            'post_grapple_ball_wait_time': self.post_grapple_ball_wait_time,
            'light_color': self.light_color.to_json(),
            'light_attenuation': self.light_attenuation,
            'ing_spot_vulnerability': self.ing_spot_vulnerability.to_json(),
            'grapple_ball_vulnerability': self.grapple_ball_vulnerability.to_json(),
            'trigger_vulnerability': self.trigger_vulnerability.to_json(),
        }

    def _dependencies_for_face_plate_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.face_plate_model)

    def _dependencies_for_ing_spot_blob_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ing_spot_blob_effect)

    def _dependencies_for_ing_spot_hit_normal_damage(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ing_spot_hit_normal_damage)

    def _dependencies_for_ing_spot_hit_heavy_damage(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ing_spot_hit_heavy_damage)

    def _dependencies_for_ing_spot_death(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ing_spot_death)

    def _dependencies_for_sound_ing_spot_idle(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_ing_spot_idle)

    def _dependencies_for_sound_ing_spot_move(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_ing_spot_move)

    def _dependencies_for_sound_hit_normal_damage(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_hit_normal_damage)

    def _dependencies_for_sound_hit_heavy_damage(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_hit_heavy_damage)

    def _dependencies_for_sound_ing_spot_death(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_ing_spot_death)

    def _dependencies_for_part(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part)

    def _dependencies_for_exit_host_swarm_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.exit_host_swarm_effect)

    def _dependencies_for_exit_host_secondary_swarm_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.exit_host_secondary_swarm_effect)

    def _dependencies_for_exit_host_smoke_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.exit_host_smoke_effect)

    def _dependencies_for_sound_swarm_move(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_swarm_move)

    def _dependencies_for_sound_inside_host(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_inside_host)

    def _dependencies_for_sound_exit_host(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_exit_host)

    def _dependencies_for_sound_exit_host_safe_zone(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_exit_host_safe_zone)

    def _dependencies_for_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound)

    def _dependencies_for_body_projectile_splat_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.body_projectile_splat_effect)

    def _dependencies_for_sound_body_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_body_projectile)

    def _dependencies_for_sound_body_projectile_splat_wall(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_body_projectile_splat_wall)

    def _dependencies_for_mini_portal_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.mini_portal_effect)

    def _dependencies_for_sound_mini_portal(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_mini_portal)

    def _dependencies_for_sound_grapple(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_grapple)

    def _dependencies_for_sound_exit_grapple(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_exit_grapple)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.patterned.dependencies_for, "patterned", "PatternedAITypedef"),
            (self.actor_information.dependencies_for, "actor_information", "ActorParameters"),
            (self._dependencies_for_face_plate_model, "face_plate_model", "AssetId"),
            (self._dependencies_for_ing_spot_blob_effect, "ing_spot_blob_effect", "AssetId"),
            (self._dependencies_for_ing_spot_hit_normal_damage, "ing_spot_hit_normal_damage", "AssetId"),
            (self._dependencies_for_ing_spot_hit_heavy_damage, "ing_spot_hit_heavy_damage", "AssetId"),
            (self._dependencies_for_ing_spot_death, "ing_spot_death", "AssetId"),
            (self._dependencies_for_sound_ing_spot_idle, "sound_ing_spot_idle", "int"),
            (self._dependencies_for_sound_ing_spot_move, "sound_ing_spot_move", "int"),
            (self._dependencies_for_sound_hit_normal_damage, "sound_hit_normal_damage", "int"),
            (self._dependencies_for_sound_hit_heavy_damage, "sound_hit_heavy_damage", "int"),
            (self._dependencies_for_sound_ing_spot_death, "sound_ing_spot_death", "int"),
            (self._dependencies_for_part, "part", "AssetId"),
            (self._dependencies_for_exit_host_swarm_effect, "exit_host_swarm_effect", "AssetId"),
            (self._dependencies_for_exit_host_secondary_swarm_effect, "exit_host_secondary_swarm_effect", "AssetId"),
            (self._dependencies_for_exit_host_smoke_effect, "exit_host_smoke_effect", "AssetId"),
            (self._dependencies_for_sound_swarm_move, "sound_swarm_move", "int"),
            (self._dependencies_for_sound_inside_host, "sound_inside_host", "int"),
            (self._dependencies_for_sound_exit_host, "sound_exit_host", "int"),
            (self._dependencies_for_sound_exit_host_safe_zone, "sound_exit_host_safe_zone", "int"),
            (self._dependencies_for_sound, "sound", "int"),
            (self._dependencies_for_body_projectile_splat_effect, "body_projectile_splat_effect", "AssetId"),
            (self._dependencies_for_sound_body_projectile, "sound_body_projectile", "int"),
            (self._dependencies_for_sound_body_projectile_splat_wall, "sound_body_projectile_splat_wall", "int"),
            (self._dependencies_for_mini_portal_effect, "mini_portal_effect", "AssetId"),
            (self._dependencies_for_sound_mini_portal, "sound_mini_portal", "int"),
            (self.mini_portal_beam_info.dependencies_for, "mini_portal_beam_info", "PlasmaBeamInfo"),
            (self._dependencies_for_sound_grapple, "sound_grapple", "int"),
            (self._dependencies_for_sound_exit_grapple, "sound_exit_grapple", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for Ing.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_patterned(data: typing.BinaryIO, game: Game, property_size: int) -> PatternedAITypedef:
    return PatternedAITypedef.from_stream(data, game, property_size, default_override={'turn_speed': 360.0, 'min_attack_range': 0.0, 'creature_size': 1})


def _decode_actor_information(data: typing.BinaryIO, game: Game, property_size: int) -> ActorParameters:
    return ActorParameters.from_stream(data, game, property_size)


def _decode_ing_flags(data: typing.BinaryIO, game: Game, property_size: int) -> IngFlags:
    return IngFlags.from_stream(data, game)


def _decode_arm_swipe_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})


def _decode_body_projectile_contact_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 5.0})


def _decode_mini_portal_projectile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})


def _decode_mini_portal_beam_info(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size, default_override={'length': 500.0, 'expansion_speed': 4.0, 'life_time': 1.0, 'pulse_speed': 20.0, 'shutdown_time': 0.25, 'pulse_effect_scale': 2.0, 'inner_color': Color(r=0.5, g=0.5, b=0.5, a=0.5), 'outer_color': Color(r=0.6000000238418579, g=0.6000000238418579, b=0.0, a=0.5)})


def _decode_exit_grapple_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 10.0, 'di_knock_back_power': 1.0})


def _decode_light_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_ing_spot_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_grapple_ball_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_trigger_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xb3774750: ('patterned', _decode_patterned),
    0x7e397fed: ('actor_information', _decode_actor_information),
    0x092fbad0: ('ing_flags', _decode_ing_flags),
    0xbdcce71b: ('face_plate_model', structs.decode_BIG_L),
    0xed69488f: ('hearing_radius', structs.decode_BIG_f),
    0x95b47cf9: ('ing_spot_max_speed', structs.decode_BIG_f),
    0x8d42a8d5: ('ing_spot_max_wall_speed', structs.decode_BIG_f),
    0x84586bfd: ('ing_spot_ball_pursuit_speed', structs.decode_BIG_f),
    0x50398a06: ('ing_spot_max_hurried_speed', structs.decode_BIG_f),
    0xeaa3c3f8: ('ing_spot_turn_speed', structs.decode_BIG_f),
    0xcc5a4918: ('ing_spot_blob_effect', structs.decode_BIG_L),
    0x8851dc01: ('ing_spot_hit_normal_damage', structs.decode_BIG_L),
    0x5d01100f: ('ing_spot_hit_heavy_damage', structs.decode_BIG_L),
    0x9a56892e: ('ing_spot_death', structs.decode_BIG_L),
    0x4cab30a9: ('sound_ing_spot_idle', structs.decode_BIG_l),
    0x8f83be73: ('sound_ing_spot_move', structs.decode_BIG_l),
    0xb392943a: ('sound_hit_normal_damage', structs.decode_BIG_l),
    0x24ecc1e9: ('sound_hit_heavy_damage', structs.decode_BIG_l),
    0x4489935e: ('sound_ing_spot_death', structs.decode_BIG_l),
    0x3c2d681e: ('part', structs.decode_BIG_L),
    0xd576f379: ('exit_host_swarm_effect', structs.decode_BIG_L),
    0x3da219c7: ('exit_host_secondary_swarm_effect', structs.decode_BIG_L),
    0x23271976: ('unknown', structs.decode_BIG_f),
    0x081e9e6c: ('exit_host_smoke_effect', structs.decode_BIG_L),
    0xcb39eccb: ('exit_host_effect_speed', structs.decode_BIG_f),
    0x587ca175: ('exit_host_initial_tracking_time', structs.decode_BIG_f),
    0x0bd7d5a9: ('exit_host_initial_tracking_dist', structs.decode_BIG_f),
    0xe8ea5bc8: ('sound_swarm_move', structs.decode_BIG_l),
    0x5650366a: ('sound_inside_host', structs.decode_BIG_l),
    0xb09af706: ('sound_exit_host', structs.decode_BIG_l),
    0x0c13c5a8: ('sound_exit_host_safe_zone', structs.decode_BIG_l),
    0x148b81e4: ('sound', structs.decode_BIG_l),
    0x5d0d2c40: ('cover_point_leash_radius', structs.decode_BIG_f),
    0xc620183a: ('min_corporeal_time', structs.decode_BIG_f),
    0x7d19c3ca: ('frustration_time', structs.decode_BIG_f),
    0xa77f6212: ('taunt_chance', structs.decode_BIG_f),
    0x9579b1f2: ('aggressiveness', structs.decode_BIG_f),
    0x915da374: ('arm_swipe_damage', _decode_arm_swipe_damage),
    0xab258f6b: ('body_projectile_contact_damage', _decode_body_projectile_contact_damage),
    0xa0d63374: ('body_projectile_suck_damage_per_sec', structs.decode_BIG_f),
    0xdfea60a2: ('body_projectile_suck_time', structs.decode_BIG_f),
    0x601cc5b4: ('body_projectile_splat_effect', structs.decode_BIG_L),
    0xce980820: ('body_projectile_speed', structs.decode_BIG_f),
    0xb752c177: ('body_projectile_drop_time', structs.decode_BIG_f),
    0xe6ddb662: ('body_projectile_min_attack_dist', structs.decode_BIG_f),
    0xb57bae86: ('body_projectile_max_attack_dist', structs.decode_BIG_f),
    0x2025858b: ('sound_body_projectile', structs.decode_BIG_l),
    0x19f8fee6: ('sound_body_projectile_splat_wall', structs.decode_BIG_l),
    0xdc741fbd: ('body_projectile_odds', structs.decode_BIG_f),
    0xfa6edeb5: ('mini_portal_min_attack_dist', structs.decode_BIG_f),
    0xa9c8c651: ('mini_portal_max_attack_dist', structs.decode_BIG_f),
    0xa926f8a8: ('mini_portal_effect', structs.decode_BIG_L),
    0x4051fd1a: ('sound_mini_portal', structs.decode_BIG_l),
    0x424a6d37: ('mini_portal_projectile_damage', _decode_mini_portal_projectile_damage),
    0x9c170968: ('mini_portal_beam_info', _decode_mini_portal_beam_info),
    0x67f6c10e: ('grab_morphball_damage_per_sec', structs.decode_BIG_f),
    0x11c36d8e: ('exit_grapple_damage', _decode_exit_grapple_damage),
    0xc2320b06: ('exit_grapple_spit_force', structs.decode_BIG_f),
    0x4832703b: ('sound_grapple', structs.decode_BIG_l),
    0x36b0e542: ('sound_exit_grapple', structs.decode_BIG_l),
    0x421651f6: ('max_grapple_ball_hold_time', structs.decode_BIG_f),
    0x560b4a95: ('grapple_ball_pursuit_range', structs.decode_BIG_f),
    0x8bdcc614: ('post_grapple_ball_wait_time', structs.decode_BIG_f),
    0xbd3efe7d: ('light_color', _decode_light_color),
    0xd24b888f: ('light_attenuation', structs.decode_BIG_f),
    0x1b96ff8b: ('ing_spot_vulnerability', _decode_ing_spot_vulnerability),
    0x33737ea6: ('grapple_ball_vulnerability', _decode_grapple_ball_vulnerability),
    0x23399d21: ('trigger_vulnerability', _decode_trigger_vulnerability),
}
