# Generated File
from __future__ import annotations

import dataclasses
import struct
import typing
import typing_extensions

from retro_data_structures import json_util
from retro_data_structures.game_check import Game
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SpacePirateWeaponDataJson(typing_extensions.TypedDict):
        scale_radial_damage: bool
        blur_player_visor: bool
        unknown_0xa93e9e12: bool
        unknown_0x01c62b32: bool
        bounce_off_other_grenades: bool
        unknown_0xc7f4966c: bool
        unknown_0x96db63f9: bool
        can_be_shot_down: bool
        unknown_0x9e20f24e: bool
        force_player_into_hyper_mode: bool
        unknown_0xe33b92c9: bool
        grenade_model: int
        grenade_min_attack_dist: float
        grenade_max_attack_dist: float
        grenade_damage: json_util.JsonObject
        grenade_damage_hard: json_util.JsonObject
        grenade_damage_elite: json_util.JsonObject
        grenade_explosion: int
        grenade_effect: int
        grenade_trail: int
        grenade_mass: float
        grenade_bounciness: float
        grenade_min_launch_speed: float
        grenade_max_launch_speed: float
        min_up_launch_angle: float
        max_up_launch_angle: float
        max_lateral_launch_angle: float
        grenade_num_bounces: int
        sound_grenade_bounce: int
        sound_grenade_explode: int
        unknown_0xa46a487e: int
        min_time_between_grenades: float
        unknown_0xd2ee80b9: float
        homing_max_turn_angle: float
        curing_time: float
        sound_grenade_flight: int
        sound_grenade_curing: int
        sound_stick: int
        start_curing_color: json_util.JsonValue
        end_curing_color: json_util.JsonValue
        sticky_grenade_impact: int
        sticky_grenade_visor_effect: int
        blur_player_visor_time: float
        unknown_0x32dcc4f9: float
        unknown_0xe1558837: float
    

@dataclasses.dataclass()
class SpacePirateWeaponData(BaseProperty):
    scale_radial_damage: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xf1c823a6, original_name='ScaleRadialDamage'
        ),
    })
    blur_player_visor: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xa3b45ab5, original_name='BlurPlayerVisor'
        ),
    })
    unknown_0xa93e9e12: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xa93e9e12, original_name='Unknown'
        ),
    })
    unknown_0x01c62b32: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x01c62b32, original_name='Unknown'
        ),
    })
    bounce_off_other_grenades: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x71f8b8f4, original_name='BounceOffOtherGrenades'
        ),
    })
    unknown_0xc7f4966c: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xc7f4966c, original_name='Unknown'
        ),
    })
    unknown_0x96db63f9: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x96db63f9, original_name='Unknown'
        ),
    })
    can_be_shot_down: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x0b3bf4c6, original_name='CanBeShotDown'
        ),
    })
    unknown_0x9e20f24e: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x9e20f24e, original_name='Unknown'
        ),
    })
    force_player_into_hyper_mode: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x51a7ff4c, original_name='ForcePlayerIntoHyperMode'
        ),
    })
    unknown_0xe33b92c9: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xe33b92c9, original_name='Unknown'
        ),
    })
    grenade_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2245a396, original_name='GrenadeModel'
        ),
    })
    grenade_min_attack_dist: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x25f822c4, original_name='GrenadeMinAttackDist'
        ),
    })
    grenade_max_attack_dist: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x765e3a20, original_name='GrenadeMaxAttackDist'
        ),
    })
    grenade_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x14d1a3a8, original_name='GrenadeDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    grenade_damage_hard: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x4dd7c2f9, original_name='GrenadeDamageHard', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    grenade_damage_elite: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x9ae342fb, original_name='GrenadeDamageElite', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
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
    grenade_mass: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9a6bb47f, original_name='GrenadeMass'
        ),
    })
    grenade_bounciness: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0xed086ce0, original_name='GrenadeBounciness'
        ),
    })
    grenade_min_launch_speed: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x00fc6646, original_name='GrenadeMinLaunchSpeed'
        ),
    })
    grenade_max_launch_speed: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa7c8e63f, original_name='GrenadeMaxLaunchSpeed'
        ),
    })
    min_up_launch_angle: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa7261cf9, original_name='MinUpLaunchAngle'
        ),
    })
    max_up_launch_angle: float = dataclasses.field(default=45.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb463fa52, original_name='MaxUpLaunchAngle'
        ),
    })
    max_lateral_launch_angle: float = dataclasses.field(default=45.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x223b58e8, original_name='MaxLateralLaunchAngle'
        ),
    })
    grenade_num_bounces: int = dataclasses.field(default=2, metadata={
        'reflection': FieldReflection[int](
            int, id=0x454f16b1, original_name='GrenadeNumBounces'
        ),
    })
    sound_grenade_bounce: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xdfada7c3, original_name='Sound_GrenadeBounce'
        ),
    })
    sound_grenade_explode: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x554b3450, original_name='Sound_GrenadeExplode'
        ),
    })
    unknown_0xa46a487e: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa46a487e, original_name='Unknown'
        ),
    })
    min_time_between_grenades: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x36d1b707, original_name='MinTimeBetweenGrenades'
        ),
    })
    unknown_0xd2ee80b9: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd2ee80b9, original_name='Unknown'
        ),
    })
    homing_max_turn_angle: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x95c7f681, original_name='HomingMaxTurnAngle'
        ),
    })
    curing_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9e69bcfb, original_name='CuringTime'
        ),
    })
    sound_grenade_flight: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x1b7540c8, original_name='Sound_GrenadeFlight'
        ),
    })
    sound_grenade_curing: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x6c14cd39, original_name='Sound_GrenadeCuring'
        ),
    })
    sound_stick: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x92802bb3, original_name='Sound_Stick'
        ),
    })
    start_curing_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=1.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xbf95a130, original_name='StartCuringColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    end_curing_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x8b4a07d2, original_name='EndCuringColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    sticky_grenade_impact: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xf769f604, original_name='StickyGrenadeImpact'
        ),
    })
    sticky_grenade_visor_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x491bf41d, original_name='StickyGrenadeVisorEffect'
        ),
    })
    blur_player_visor_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1fb988f2, original_name='BlurPlayerVisorTime'
        ),
    })
    unknown_0x32dcc4f9: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x32dcc4f9, original_name='Unknown'
        ),
    })
    unknown_0xe1558837: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe1558837, original_name='Unknown'
        ),
    })

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None) -> typing_extensions.Self:
        property_count = structs.BIG_H.unpack(data.read(2))[0]
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

        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 45:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf1c823a6
        scale_radial_damage = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa3b45ab5
        blur_player_visor = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa93e9e12
        unknown_0xa93e9e12 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x01c62b32
        unknown_0x01c62b32 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71f8b8f4
        bounce_off_other_grenades = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc7f4966c
        unknown_0xc7f4966c = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x96db63f9
        unknown_0x96db63f9 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0b3bf4c6
        can_be_shot_down = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9e20f24e
        unknown_0x9e20f24e = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x51a7ff4c
        force_player_into_hyper_mode = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe33b92c9
        unknown_0xe33b92c9 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2245a396
        grenade_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x25f822c4
        grenade_min_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x765e3a20
        grenade_max_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x14d1a3a8
        grenade_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4dd7c2f9
        grenade_damage_hard = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9ae342fb
        grenade_damage_elite = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1319e077
        grenade_explosion = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd207ff0f
        grenade_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2b31c882
        grenade_trail = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9a6bb47f
        grenade_mass = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed086ce0
        grenade_bounciness = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x00fc6646
        grenade_min_launch_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa7c8e63f
        grenade_max_launch_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa7261cf9
        min_up_launch_angle = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb463fa52
        max_up_launch_angle = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x223b58e8
        max_lateral_launch_angle = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x454f16b1
        grenade_num_bounces = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdfada7c3
        sound_grenade_bounce = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x554b3450
        sound_grenade_explode = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa46a487e
        unknown_0xa46a487e = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x36d1b707
        min_time_between_grenades = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd2ee80b9
        unknown_0xd2ee80b9 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95c7f681
        homing_max_turn_angle = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9e69bcfb
        curing_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1b7540c8
        sound_grenade_flight = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6c14cd39
        sound_grenade_curing = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x92802bb3
        sound_stick = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbf95a130
        start_curing_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8b4a07d2
        end_curing_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf769f604
        sticky_grenade_impact = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x491bf41d
        sticky_grenade_visor_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1fb988f2
        blur_player_visor_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32dcc4f9
        unknown_0x32dcc4f9 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe1558837
        unknown_0xe1558837 = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(scale_radial_damage, blur_player_visor, unknown_0xa93e9e12, unknown_0x01c62b32, bounce_off_other_grenades, unknown_0xc7f4966c, unknown_0x96db63f9, can_be_shot_down, unknown_0x9e20f24e, force_player_into_hyper_mode, unknown_0xe33b92c9, grenade_model, grenade_min_attack_dist, grenade_max_attack_dist, grenade_damage, grenade_damage_hard, grenade_damage_elite, grenade_explosion, grenade_effect, grenade_trail, grenade_mass, grenade_bounciness, grenade_min_launch_speed, grenade_max_launch_speed, min_up_launch_angle, max_up_launch_angle, max_lateral_launch_angle, grenade_num_bounces, sound_grenade_bounce, sound_grenade_explode, unknown_0xa46a487e, min_time_between_grenades, unknown_0xd2ee80b9, homing_max_turn_angle, curing_time, sound_grenade_flight, sound_grenade_curing, sound_stick, start_curing_color, end_curing_color, sticky_grenade_impact, sticky_grenade_visor_effect, blur_player_visor_time, unknown_0x32dcc4f9, unknown_0xe1558837)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00-')  # 45 properties

        data.write(b'\xf1\xc8#\xa6')  # 0xf1c823a6
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.scale_radial_damage))

        data.write(b'\xa3\xb4Z\xb5')  # 0xa3b45ab5
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.blur_player_visor))

        data.write(b'\xa9>\x9e\x12')  # 0xa93e9e12
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xa93e9e12))

        data.write(b'\x01\xc6+2')  # 0x1c62b32
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x01c62b32))

        data.write(b'q\xf8\xb8\xf4')  # 0x71f8b8f4
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.bounce_off_other_grenades))

        data.write(b'\xc7\xf4\x96l')  # 0xc7f4966c
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xc7f4966c))

        data.write(b'\x96\xdbc\xf9')  # 0x96db63f9
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x96db63f9))

        data.write(b'\x0b;\xf4\xc6')  # 0xb3bf4c6
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.can_be_shot_down))

        data.write(b'\x9e \xf2N')  # 0x9e20f24e
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x9e20f24e))

        data.write(b'Q\xa7\xffL')  # 0x51a7ff4c
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.force_player_into_hyper_mode))

        data.write(b'\xe3;\x92\xc9')  # 0xe33b92c9
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xe33b92c9))

        data.write(b'"E\xa3\x96')  # 0x2245a396
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.grenade_model))

        data.write(b'%\xf8"\xc4')  # 0x25f822c4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grenade_min_attack_dist))

        data.write(b'v^: ')  # 0x765e3a20
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grenade_max_attack_dist))

        data.write(b'\x14\xd1\xa3\xa8')  # 0x14d1a3a8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grenade_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'M\xd7\xc2\xf9')  # 0x4dd7c2f9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grenade_damage_hard.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9a\xe3B\xfb')  # 0x9ae342fb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grenade_damage_elite.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x13\x19\xe0w')  # 0x1319e077
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.grenade_explosion))

        data.write(b'\xd2\x07\xff\x0f')  # 0xd207ff0f
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.grenade_effect))

        data.write(b'+1\xc8\x82')  # 0x2b31c882
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.grenade_trail))

        data.write(b'\x9ak\xb4\x7f')  # 0x9a6bb47f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grenade_mass))

        data.write(b'\xed\x08l\xe0')  # 0xed086ce0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grenade_bounciness))

        data.write(b'\x00\xfcfF')  # 0xfc6646
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grenade_min_launch_speed))

        data.write(b'\xa7\xc8\xe6?')  # 0xa7c8e63f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grenade_max_launch_speed))

        data.write(b'\xa7&\x1c\xf9')  # 0xa7261cf9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_up_launch_angle))

        data.write(b'\xb4c\xfaR')  # 0xb463fa52
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_up_launch_angle))

        data.write(b'";X\xe8')  # 0x223b58e8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_lateral_launch_angle))

        data.write(b'EO\x16\xb1')  # 0x454f16b1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.grenade_num_bounces))

        data.write(b'\xdf\xad\xa7\xc3')  # 0xdfada7c3
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_grenade_bounce))

        data.write(b'UK4P')  # 0x554b3450
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_grenade_explode))

        data.write(b'\xa4jH~')  # 0xa46a487e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.unknown_0xa46a487e))

        data.write(b'6\xd1\xb7\x07')  # 0x36d1b707
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_time_between_grenades))

        data.write(b'\xd2\xee\x80\xb9')  # 0xd2ee80b9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xd2ee80b9))

        data.write(b'\x95\xc7\xf6\x81')  # 0x95c7f681
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.homing_max_turn_angle))

        data.write(b'\x9ei\xbc\xfb')  # 0x9e69bcfb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.curing_time))

        data.write(b'\x1bu@\xc8')  # 0x1b7540c8
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_grenade_flight))

        data.write(b'l\x14\xcd9')  # 0x6c14cd39
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_grenade_curing))

        data.write(b'\x92\x80+\xb3')  # 0x92802bb3
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_stick))

        data.write(b'\xbf\x95\xa10')  # 0xbf95a130
        data.write(b'\x00\x10')  # size
        self.start_curing_color.to_stream(data, game)

        data.write(b'\x8bJ\x07\xd2')  # 0x8b4a07d2
        data.write(b'\x00\x10')  # size
        self.end_curing_color.to_stream(data, game)

        data.write(b'\xf7i\xf6\x04')  # 0xf769f604
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sticky_grenade_impact))

        data.write(b'I\x1b\xf4\x1d')  # 0x491bf41d
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sticky_grenade_visor_effect))

        data.write(b'\x1f\xb9\x88\xf2')  # 0x1fb988f2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.blur_player_visor_time))

        data.write(b'2\xdc\xc4\xf9')  # 0x32dcc4f9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x32dcc4f9))

        data.write(b'\xe1U\x887')  # 0xe1558837
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe1558837))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SpacePirateWeaponDataJson", data)
        return cls(
            scale_radial_damage=json_data['scale_radial_damage'],
            blur_player_visor=json_data['blur_player_visor'],
            unknown_0xa93e9e12=json_data['unknown_0xa93e9e12'],
            unknown_0x01c62b32=json_data['unknown_0x01c62b32'],
            bounce_off_other_grenades=json_data['bounce_off_other_grenades'],
            unknown_0xc7f4966c=json_data['unknown_0xc7f4966c'],
            unknown_0x96db63f9=json_data['unknown_0x96db63f9'],
            can_be_shot_down=json_data['can_be_shot_down'],
            unknown_0x9e20f24e=json_data['unknown_0x9e20f24e'],
            force_player_into_hyper_mode=json_data['force_player_into_hyper_mode'],
            unknown_0xe33b92c9=json_data['unknown_0xe33b92c9'],
            grenade_model=json_data['grenade_model'],
            grenade_min_attack_dist=json_data['grenade_min_attack_dist'],
            grenade_max_attack_dist=json_data['grenade_max_attack_dist'],
            grenade_damage=DamageInfo.from_json(json_data['grenade_damage']),
            grenade_damage_hard=DamageInfo.from_json(json_data['grenade_damage_hard']),
            grenade_damage_elite=DamageInfo.from_json(json_data['grenade_damage_elite']),
            grenade_explosion=json_data['grenade_explosion'],
            grenade_effect=json_data['grenade_effect'],
            grenade_trail=json_data['grenade_trail'],
            grenade_mass=json_data['grenade_mass'],
            grenade_bounciness=json_data['grenade_bounciness'],
            grenade_min_launch_speed=json_data['grenade_min_launch_speed'],
            grenade_max_launch_speed=json_data['grenade_max_launch_speed'],
            min_up_launch_angle=json_data['min_up_launch_angle'],
            max_up_launch_angle=json_data['max_up_launch_angle'],
            max_lateral_launch_angle=json_data['max_lateral_launch_angle'],
            grenade_num_bounces=json_data['grenade_num_bounces'],
            sound_grenade_bounce=json_data['sound_grenade_bounce'],
            sound_grenade_explode=json_data['sound_grenade_explode'],
            unknown_0xa46a487e=json_data['unknown_0xa46a487e'],
            min_time_between_grenades=json_data['min_time_between_grenades'],
            unknown_0xd2ee80b9=json_data['unknown_0xd2ee80b9'],
            homing_max_turn_angle=json_data['homing_max_turn_angle'],
            curing_time=json_data['curing_time'],
            sound_grenade_flight=json_data['sound_grenade_flight'],
            sound_grenade_curing=json_data['sound_grenade_curing'],
            sound_stick=json_data['sound_stick'],
            start_curing_color=Color.from_json(json_data['start_curing_color']),
            end_curing_color=Color.from_json(json_data['end_curing_color']),
            sticky_grenade_impact=json_data['sticky_grenade_impact'],
            sticky_grenade_visor_effect=json_data['sticky_grenade_visor_effect'],
            blur_player_visor_time=json_data['blur_player_visor_time'],
            unknown_0x32dcc4f9=json_data['unknown_0x32dcc4f9'],
            unknown_0xe1558837=json_data['unknown_0xe1558837'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'scale_radial_damage': self.scale_radial_damage,
            'blur_player_visor': self.blur_player_visor,
            'unknown_0xa93e9e12': self.unknown_0xa93e9e12,
            'unknown_0x01c62b32': self.unknown_0x01c62b32,
            'bounce_off_other_grenades': self.bounce_off_other_grenades,
            'unknown_0xc7f4966c': self.unknown_0xc7f4966c,
            'unknown_0x96db63f9': self.unknown_0x96db63f9,
            'can_be_shot_down': self.can_be_shot_down,
            'unknown_0x9e20f24e': self.unknown_0x9e20f24e,
            'force_player_into_hyper_mode': self.force_player_into_hyper_mode,
            'unknown_0xe33b92c9': self.unknown_0xe33b92c9,
            'grenade_model': self.grenade_model,
            'grenade_min_attack_dist': self.grenade_min_attack_dist,
            'grenade_max_attack_dist': self.grenade_max_attack_dist,
            'grenade_damage': self.grenade_damage.to_json(),
            'grenade_damage_hard': self.grenade_damage_hard.to_json(),
            'grenade_damage_elite': self.grenade_damage_elite.to_json(),
            'grenade_explosion': self.grenade_explosion,
            'grenade_effect': self.grenade_effect,
            'grenade_trail': self.grenade_trail,
            'grenade_mass': self.grenade_mass,
            'grenade_bounciness': self.grenade_bounciness,
            'grenade_min_launch_speed': self.grenade_min_launch_speed,
            'grenade_max_launch_speed': self.grenade_max_launch_speed,
            'min_up_launch_angle': self.min_up_launch_angle,
            'max_up_launch_angle': self.max_up_launch_angle,
            'max_lateral_launch_angle': self.max_lateral_launch_angle,
            'grenade_num_bounces': self.grenade_num_bounces,
            'sound_grenade_bounce': self.sound_grenade_bounce,
            'sound_grenade_explode': self.sound_grenade_explode,
            'unknown_0xa46a487e': self.unknown_0xa46a487e,
            'min_time_between_grenades': self.min_time_between_grenades,
            'unknown_0xd2ee80b9': self.unknown_0xd2ee80b9,
            'homing_max_turn_angle': self.homing_max_turn_angle,
            'curing_time': self.curing_time,
            'sound_grenade_flight': self.sound_grenade_flight,
            'sound_grenade_curing': self.sound_grenade_curing,
            'sound_stick': self.sound_stick,
            'start_curing_color': self.start_curing_color.to_json(),
            'end_curing_color': self.end_curing_color.to_json(),
            'sticky_grenade_impact': self.sticky_grenade_impact,
            'sticky_grenade_visor_effect': self.sticky_grenade_visor_effect,
            'blur_player_visor_time': self.blur_player_visor_time,
            'unknown_0x32dcc4f9': self.unknown_0x32dcc4f9,
            'unknown_0xe1558837': self.unknown_0xe1558837,
        }

    def _dependencies_for_grenade_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grenade_model)

    def _dependencies_for_grenade_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grenade_explosion)

    def _dependencies_for_grenade_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grenade_effect)

    def _dependencies_for_grenade_trail(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grenade_trail)

    def _dependencies_for_sound_grenade_bounce(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_grenade_bounce)

    def _dependencies_for_sound_grenade_explode(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_grenade_explode)

    def _dependencies_for_unknown_0xa46a487e(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_0xa46a487e)

    def _dependencies_for_sound_grenade_flight(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_grenade_flight)

    def _dependencies_for_sound_grenade_curing(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_grenade_curing)

    def _dependencies_for_sound_stick(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_stick)

    def _dependencies_for_sticky_grenade_impact(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sticky_grenade_impact)

    def _dependencies_for_sticky_grenade_visor_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sticky_grenade_visor_effect)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_grenade_model, "grenade_model", "AssetId"),
            (self._dependencies_for_grenade_explosion, "grenade_explosion", "AssetId"),
            (self._dependencies_for_grenade_effect, "grenade_effect", "AssetId"),
            (self._dependencies_for_grenade_trail, "grenade_trail", "AssetId"),
            (self._dependencies_for_sound_grenade_bounce, "sound_grenade_bounce", "AssetId"),
            (self._dependencies_for_sound_grenade_explode, "sound_grenade_explode", "AssetId"),
            (self._dependencies_for_unknown_0xa46a487e, "unknown_0xa46a487e", "AssetId"),
            (self._dependencies_for_sound_grenade_flight, "sound_grenade_flight", "AssetId"),
            (self._dependencies_for_sound_grenade_curing, "sound_grenade_curing", "AssetId"),
            (self._dependencies_for_sound_stick, "sound_stick", "AssetId"),
            (self._dependencies_for_sticky_grenade_impact, "sticky_grenade_impact", "AssetId"),
            (self._dependencies_for_sticky_grenade_visor_effect, "sticky_grenade_visor_effect", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for SpacePirateWeaponData.{field_name} ({field_type}): {e}"
                )


def _decode_grenade_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_grenade_damage_hard(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_grenade_damage_elite(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_start_curing_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_end_curing_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xf1c823a6: ('scale_radial_damage', structs.decode_BIG_bool_),
    0xa3b45ab5: ('blur_player_visor', structs.decode_BIG_bool_),
    0xa93e9e12: ('unknown_0xa93e9e12', structs.decode_BIG_bool_),
    0x01c62b32: ('unknown_0x01c62b32', structs.decode_BIG_bool_),
    0x71f8b8f4: ('bounce_off_other_grenades', structs.decode_BIG_bool_),
    0xc7f4966c: ('unknown_0xc7f4966c', structs.decode_BIG_bool_),
    0x96db63f9: ('unknown_0x96db63f9', structs.decode_BIG_bool_),
    0x0b3bf4c6: ('can_be_shot_down', structs.decode_BIG_bool_),
    0x9e20f24e: ('unknown_0x9e20f24e', structs.decode_BIG_bool_),
    0x51a7ff4c: ('force_player_into_hyper_mode', structs.decode_BIG_bool_),
    0xe33b92c9: ('unknown_0xe33b92c9', structs.decode_BIG_bool_),
    0x2245a396: ('grenade_model', structs.decode_BIG_Q),
    0x25f822c4: ('grenade_min_attack_dist', structs.decode_BIG_f),
    0x765e3a20: ('grenade_max_attack_dist', structs.decode_BIG_f),
    0x14d1a3a8: ('grenade_damage', _decode_grenade_damage),
    0x4dd7c2f9: ('grenade_damage_hard', _decode_grenade_damage_hard),
    0x9ae342fb: ('grenade_damage_elite', _decode_grenade_damage_elite),
    0x1319e077: ('grenade_explosion', structs.decode_BIG_Q),
    0xd207ff0f: ('grenade_effect', structs.decode_BIG_Q),
    0x2b31c882: ('grenade_trail', structs.decode_BIG_Q),
    0x9a6bb47f: ('grenade_mass', structs.decode_BIG_f),
    0xed086ce0: ('grenade_bounciness', structs.decode_BIG_f),
    0x00fc6646: ('grenade_min_launch_speed', structs.decode_BIG_f),
    0xa7c8e63f: ('grenade_max_launch_speed', structs.decode_BIG_f),
    0xa7261cf9: ('min_up_launch_angle', structs.decode_BIG_f),
    0xb463fa52: ('max_up_launch_angle', structs.decode_BIG_f),
    0x223b58e8: ('max_lateral_launch_angle', structs.decode_BIG_f),
    0x454f16b1: ('grenade_num_bounces', structs.decode_BIG_l),
    0xdfada7c3: ('sound_grenade_bounce', structs.decode_BIG_Q),
    0x554b3450: ('sound_grenade_explode', structs.decode_BIG_Q),
    0xa46a487e: ('unknown_0xa46a487e', structs.decode_BIG_Q),
    0x36d1b707: ('min_time_between_grenades', structs.decode_BIG_f),
    0xd2ee80b9: ('unknown_0xd2ee80b9', structs.decode_BIG_f),
    0x95c7f681: ('homing_max_turn_angle', structs.decode_BIG_f),
    0x9e69bcfb: ('curing_time', structs.decode_BIG_f),
    0x1b7540c8: ('sound_grenade_flight', structs.decode_BIG_Q),
    0x6c14cd39: ('sound_grenade_curing', structs.decode_BIG_Q),
    0x92802bb3: ('sound_stick', structs.decode_BIG_Q),
    0xbf95a130: ('start_curing_color', _decode_start_curing_color),
    0x8b4a07d2: ('end_curing_color', _decode_end_curing_color),
    0xf769f604: ('sticky_grenade_impact', structs.decode_BIG_Q),
    0x491bf41d: ('sticky_grenade_visor_effect', structs.decode_BIG_Q),
    0x1fb988f2: ('blur_player_visor_time', structs.decode_BIG_f),
    0x32dcc4f9: ('unknown_0x32dcc4f9', structs.decode_BIG_f),
    0xe1558837: ('unknown_0xe1558837', structs.decode_BIG_f),
}
