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
from retro_data_structures.properties.common.archetypes.TIcon_Configurations import TIcon_Configurations
from retro_data_structures.properties.corruption.archetypes.TweakTargeting_ChargeBeam import TweakTargeting_ChargeBeam
from retro_data_structures.properties.common.archetypes.TweakTargeting_Charge_Gauge import TweakTargeting_Charge_Gauge
from retro_data_structures.properties.corruption.archetypes.TweakTargeting_CombatReticules import TweakTargeting_CombatReticules
from retro_data_structures.properties.common.archetypes.TweakTargeting_LockDagger import TweakTargeting_LockDagger
from retro_data_structures.properties.common.archetypes.TweakTargeting_LockFire import TweakTargeting_LockFire
from retro_data_structures.properties.corruption.archetypes.TweakTargeting_OrbitLock import TweakTargeting_OrbitLock
from retro_data_structures.properties.common.archetypes.TweakTargeting_OuterBeamIcon import TweakTargeting_OuterBeamIcon
from retro_data_structures.properties.common.archetypes.TweakTargeting_Scan import TweakTargeting_Scan

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class TweakTargetingJson(typing_extensions.TypedDict):
        instance_name: str
        combat_reticules: json_util.JsonObject
        charge_beam: json_util.JsonObject
        orbit_lock: json_util.JsonObject
        tweak_targeting_outer_beam_icon: json_util.JsonObject
        power_beam_icon_configurations: json_util.JsonObject
        ice_beam_icon_configurations: json_util.JsonObject
        wave_beam_icon_configurations: json_util.JsonObject
        plasma_beam_icon_configurations: json_util.JsonObject
        charge_gauge: json_util.JsonObject
        lock_fire: json_util.JsonObject
        lock_dagger: json_util.JsonObject
        scan: json_util.JsonObject
        unknown_0xc3410560: int
        orbit_lock_on_acquire_target_interpolation_time: float
        orbit_lock_on_lose_target_interpolation_time: float
        orbit_lock_on_switch_target_interpolation_time: float
        lock_on_confirm_reticle_scale: float
        seeker_acquire_target_interpolation_time: float
        seeker_lose_target_interpolation_time: float
        seeker_switch_target_interpolation_time: float
        seeker_target_reticle_scale: float
        seeker_z_rotation_rate: float
        unknown_0xdcbd7bf8: float
        orbit_point_primary_color_red: float
        orbit_point_primary_color_green: float
        orbit_point_primary_color_blue: float
        orbit_point_secondary_color_red: float
        orbit_point_secondary_color_green: float
        orbit_point_secondary_color_blue: float
        orbit_point_occluded_opacity: float
        orbit_point_non_occluded_opacity: float
        orbit_point_z_offset: float
        orbit_point_interpolate_in_time: float
        orbit_point_interpolate_out_time: float
        orbit_point_color_animate_period: float
        jump_target_possible_primary_color_red: float
        jump_target_possible_primary_color_green: float
        jump_target_possible_primary_color_blue: float
        jump_target_possible_secondary_color_red: float
        jump_target_possible_secondary_color_green: float
        jump_target_possible_secondary_color_blue: float
        jump_target_impossible_primary_color_red: float
        jump_target_impossible_primary_color_green: float
        jump_target_impossible_primary_color_blue: float
        jump_target_impossible_secondary_color_red: float
        jump_target_impossible_secondary_color_green: float
        jump_target_impossible_secondary_color_blue: float
        jump_target_occluded_opacity: float
        jump_target_non_occluded_opacity: float
        jump_target_height: float
        jump_target_interpolate_in_time: float
        jump_target_interpolate_out_time: float
        jump_target_color_animate_period: float
        jump_target_z_rotate_speed: float
        orbit_point_z_rotate_speed: float
        unknown_0x42420f6e: json_util.JsonValue
        flower_reticle_scale: float
        flower_reticle_color: json_util.JsonValue
        missile_bracket_open_holster_time: float
        unknown_0x4c73a43d: float
        unknown_0x6543d31b: float
        missile_bracket_missile_fire_anim_time: float
        missile_bracket_color: json_util.JsonValue
        inner_beam_icon_open_time: float
        inner_beam_icon_scale: float
        inner_beam_icon_color_power_beam: json_util.JsonValue
        inner_beam_icon_color_ice_beam: json_util.JsonValue
        inner_beam_icon_color_wave_beam: json_util.JsonValue
        inner_beam_icon_color_plasma_beam: json_util.JsonValue
        lock_on_confirm_reticle_color: json_util.JsonValue
        seeker_reticle_color: json_util.JsonValue
        lock_on_confirm_min_radius_viewport: float
        lock_on_confirm_max_radius_viewport: float
        flower_min_radius_viewport: float
        flower_max_radius_viewport: float
        seeker_min_radius_viewport: float
        seeker_max_radius_viewport: float
        missile_bracket_min_radius_viewport: float
        missile_bracket_max_radius_viewport: float
        inner_icon_min_radius_viewport: float
        inner_icon_max_radius_viewport: float
        outer_icon_min_radius_viewport: float
        outer_icon_max_radius_viewport: float
        lock_fire_min_radius_viewport: float
        lock_fire_max_radius_viewport: float
        lock_dagger_min_radius_viewport: float
        lock_dagger_max_radius_viewport: float
        grapple_icon_scale: float
        grapple_icon_scale_inactive: float
        grapple_icon_min_radius_viewport: float
        grapple_icon_max_radius_viewport: float
        grapple_icon_color: json_util.JsonValue
        grapple_icon_color_inactive: json_util.JsonValue
        grapple_icon_color_inactive_out_of_range: json_util.JsonValue
        unknown_0x083b1cc8: json_util.JsonValue
        unknown_0x966982b1: float
        grapple_max_visible_distance: float
        charge_gauge_glow_color: json_util.JsonValue
        charge_gauge_glow_time: float
        orbit_point_model_color: json_util.JsonValue
        crosshairs_color: json_util.JsonValue
        crosshairs_fade_in_out_time: float
        is_draw_orbit_point_default: bool
        charge_gauge_glow_color_b: json_util.JsonValue
        charge_gauge_flash_cycle_time: float
        x_ray_seeker_min_radius_viewport: float
        x_ray_seeker_max_radius_viewport: float
        x_ray_seeker_reticle_color: json_util.JsonValue
        x_ray_seeker_target_reticle_scale: float
        unknown_0xcbac6d52: float
        unknown_0x980a75b6: float
        unknown_0xcd1e0e91: float
        unknown_0xa3e32481: float
        aiming_cursor_clamp_color: json_util.JsonValue
        aiming_cursor_clamp_secondary_color: json_util.JsonValue
        aiming_cursor_clamp_offset: float
        aiming_cursor_clamp_time: float
        aiming_cursor_center_ring_color: json_util.JsonValue
        aiming_cursor_center_ring_outline_color: json_util.JsonValue
        aiming_cursor_center_ring_secondary_color: json_util.JsonValue
        aiming_cursor_center_ring_outline_secondary_color: json_util.JsonValue
        aiming_cursor_center_ring_color_transition_time: float
        aiming_cursor_radius: float
        aiming_cursor_depth_ring_color: json_util.JsonValue
        aiming_cursor_depth_ring_outline_color: json_util.JsonValue
        aiming_cursor_depth_ring_secondary_color: json_util.JsonValue
        aiming_cursor_depth_ring_outline_secondary_color: json_util.JsonValue
        aiming_cursor_depth_ring_min_size: float
        aiming_cursor_depth_ring_max_size: float
        x_ray_aiming_cursor_color: json_util.JsonValue
        x_ray_depth_cursor_color: json_util.JsonValue
        x_ray_depth_cursor_min_size: float
        x_ray_depth_cursor_max_size: float
        unknown_0xc29882b7: json_util.JsonValue
        unknown_0xd33fcc91: json_util.JsonValue
    

@dataclasses.dataclass()
class TweakTargeting(BaseObjectType):
    instance_name: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x7fda1466, original_name='InstanceName'
        ),
    })
    combat_reticules: TweakTargeting_CombatReticules = dataclasses.field(default_factory=TweakTargeting_CombatReticules, metadata={
        'reflection': FieldReflection[TweakTargeting_CombatReticules](
            TweakTargeting_CombatReticules, id=0xd15b6a54, original_name='CombatReticules', from_json=TweakTargeting_CombatReticules.from_json, to_json=TweakTargeting_CombatReticules.to_json
        ),
    })
    charge_beam: TweakTargeting_ChargeBeam = dataclasses.field(default_factory=TweakTargeting_ChargeBeam, metadata={
        'reflection': FieldReflection[TweakTargeting_ChargeBeam](
            TweakTargeting_ChargeBeam, id=0xe87e2134, original_name='ChargeBeam', from_json=TweakTargeting_ChargeBeam.from_json, to_json=TweakTargeting_ChargeBeam.to_json
        ),
    })
    orbit_lock: TweakTargeting_OrbitLock = dataclasses.field(default_factory=TweakTargeting_OrbitLock, metadata={
        'reflection': FieldReflection[TweakTargeting_OrbitLock](
            TweakTargeting_OrbitLock, id=0xc6915d69, original_name='OrbitLock', from_json=TweakTargeting_OrbitLock.from_json, to_json=TweakTargeting_OrbitLock.to_json
        ),
    })
    tweak_targeting_outer_beam_icon: TweakTargeting_OuterBeamIcon = dataclasses.field(default_factory=TweakTargeting_OuterBeamIcon, metadata={
        'reflection': FieldReflection[TweakTargeting_OuterBeamIcon](
            TweakTargeting_OuterBeamIcon, id=0x5173932f, original_name='TweakTargeting_OuterBeamIcon', from_json=TweakTargeting_OuterBeamIcon.from_json, to_json=TweakTargeting_OuterBeamIcon.to_json
        ),
    })
    power_beam_icon_configurations: TIcon_Configurations = dataclasses.field(default_factory=TIcon_Configurations, metadata={
        'reflection': FieldReflection[TIcon_Configurations](
            TIcon_Configurations, id=0x23ff4be4, original_name='Power_Beam_Icon_Configurations', from_json=TIcon_Configurations.from_json, to_json=TIcon_Configurations.to_json
        ),
    })
    ice_beam_icon_configurations: TIcon_Configurations = dataclasses.field(default_factory=TIcon_Configurations, metadata={
        'reflection': FieldReflection[TIcon_Configurations](
            TIcon_Configurations, id=0x92e98613, original_name='Ice_Beam_Icon_Configurations', from_json=TIcon_Configurations.from_json, to_json=TIcon_Configurations.to_json
        ),
    })
    wave_beam_icon_configurations: TIcon_Configurations = dataclasses.field(default_factory=TIcon_Configurations, metadata={
        'reflection': FieldReflection[TIcon_Configurations](
            TIcon_Configurations, id=0x64833842, original_name='Wave_Beam_Icon_Configurations', from_json=TIcon_Configurations.from_json, to_json=TIcon_Configurations.to_json
        ),
    })
    plasma_beam_icon_configurations: TIcon_Configurations = dataclasses.field(default_factory=TIcon_Configurations, metadata={
        'reflection': FieldReflection[TIcon_Configurations](
            TIcon_Configurations, id=0x8dfd6e3c, original_name='Plasma_Beam_Icon_Configurations', from_json=TIcon_Configurations.from_json, to_json=TIcon_Configurations.to_json
        ),
    })
    charge_gauge: TweakTargeting_Charge_Gauge = dataclasses.field(default_factory=TweakTargeting_Charge_Gauge, metadata={
        'reflection': FieldReflection[TweakTargeting_Charge_Gauge](
            TweakTargeting_Charge_Gauge, id=0xbc5a41b2, original_name='Charge_Gauge', from_json=TweakTargeting_Charge_Gauge.from_json, to_json=TweakTargeting_Charge_Gauge.to_json
        ),
    })
    lock_fire: TweakTargeting_LockFire = dataclasses.field(default_factory=TweakTargeting_LockFire, metadata={
        'reflection': FieldReflection[TweakTargeting_LockFire](
            TweakTargeting_LockFire, id=0x00183589, original_name='LockFire', from_json=TweakTargeting_LockFire.from_json, to_json=TweakTargeting_LockFire.to_json
        ),
    })
    lock_dagger: TweakTargeting_LockDagger = dataclasses.field(default_factory=TweakTargeting_LockDagger, metadata={
        'reflection': FieldReflection[TweakTargeting_LockDagger](
            TweakTargeting_LockDagger, id=0xd20ecc07, original_name='LockDagger', from_json=TweakTargeting_LockDagger.from_json, to_json=TweakTargeting_LockDagger.to_json
        ),
    })
    scan: TweakTargeting_Scan = dataclasses.field(default_factory=TweakTargeting_Scan, metadata={
        'reflection': FieldReflection[TweakTargeting_Scan](
            TweakTargeting_Scan, id=0x65ef9f2a, original_name='Scan', from_json=TweakTargeting_Scan.from_json, to_json=TweakTargeting_Scan.to_json
        ),
    })
    unknown_0xc3410560: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0xc3410560, original_name='Unknown'
        ),
    })
    orbit_lock_on_acquire_target_interpolation_time: float = dataclasses.field(default=0.15000000596046448, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3eb13041, original_name='OrbitLockOnAcquireTargetInterpolationTime'
        ),
    })
    orbit_lock_on_lose_target_interpolation_time: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5e67cab0, original_name='OrbitLockOnLoseTargetInterpolationTime'
        ),
    })
    orbit_lock_on_switch_target_interpolation_time: float = dataclasses.field(default=0.15000000596046448, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe0ca98ac, original_name='OrbitLockOnSwitchTargetInterpolationTime'
        ),
    })
    lock_on_confirm_reticle_scale: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc1e35abb, original_name='LockOnConfirmReticleScale'
        ),
    })
    seeker_acquire_target_interpolation_time: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9f8d62c1, original_name='SeekerAcquireTargetInterpolationTime'
        ),
    })
    seeker_lose_target_interpolation_time: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0xff5eeeb9, original_name='SeekerLoseTargetInterpolationTime'
        ),
    })
    seeker_switch_target_interpolation_time: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0d0b660d, original_name='SeekerSwitchTargetInterpolationTime'
        ),
    })
    seeker_target_reticle_scale: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x132dd09e, original_name='SeekerTargetReticleScale'
        ),
    })
    seeker_z_rotation_rate: float = dataclasses.field(default=-120.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x03efc783, original_name='SeekerZRotationRate'
        ),
    })
    unknown_0xdcbd7bf8: float = dataclasses.field(default=120.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdcbd7bf8, original_name='Unknown'
        ),
    })
    orbit_point_primary_color_red: float = dataclasses.field(default=0.9599999785423279, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2acd6b4b, original_name='OrbitPointPrimaryColorRed'
        ),
    })
    orbit_point_primary_color_green: float = dataclasses.field(default=0.46000000834465027, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb4c6c331, original_name='OrbitPointPrimaryColorGreen'
        ),
    })
    orbit_point_primary_color_blue: float = dataclasses.field(default=0.17000000178813934, metadata={
        'reflection': FieldReflection[float](
            float, id=0x27d02089, original_name='OrbitPointPrimaryColorBlue'
        ),
    })
    orbit_point_secondary_color_red: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xae89310e, original_name='OrbitPointSecondaryColorRed'
        ),
    })
    orbit_point_secondary_color_green: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb27644df, original_name='OrbitPointSecondaryColorGreen'
        ),
    })
    orbit_point_secondary_color_blue: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x21e2d1cc, original_name='OrbitPointSecondaryColorBlue'
        ),
    })
    orbit_point_occluded_opacity: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8e3afef8, original_name='OrbitPointOccludedOpacity'
        ),
    })
    orbit_point_non_occluded_opacity: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5c489cb5, original_name='OrbitPointNonOccludedOpacity'
        ),
    })
    orbit_point_z_offset: float = dataclasses.field(default=-0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0xef2c842e, original_name='OrbitPointZOffset'
        ),
    })
    orbit_point_interpolate_in_time: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x61a6a38e, original_name='OrbitPointInterpolateInTime'
        ),
    })
    orbit_point_interpolate_out_time: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfbdf31f9, original_name='OrbitPointInterpolateOutTime'
        ),
    })
    orbit_point_color_animate_period: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf76f7d0b, original_name='OrbitPointColorAnimatePeriod'
        ),
    })
    jump_target_possible_primary_color_red: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x810b3a08, original_name='JumpTargetPossiblePrimaryColorRed'
        ),
    })
    jump_target_possible_primary_color_green: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x73fe1553, original_name='JumpTargetPossiblePrimaryColorGreen'
        ),
    })
    jump_target_possible_primary_color_blue: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc8aef6f2, original_name='JumpTargetPossiblePrimaryColorBlue'
        ),
    })
    jump_target_possible_secondary_color_red: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x69b1e76c, original_name='JumpTargetPossibleSecondaryColorRed'
        ),
    })
    jump_target_possible_secondary_color_green: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8a0dfd23, original_name='JumpTargetPossibleSecondaryColorGreen'
        ),
    })
    jump_target_possible_secondary_color_blue: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8299e96e, original_name='JumpTargetPossibleSecondaryColorBlue'
        ),
    })
    jump_target_impossible_primary_color_red: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa18a3f25, original_name='JumpTargetImpossiblePrimaryColorRed'
        ),
    })
    jump_target_impossible_primary_color_green: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x23be9bb2, original_name='JumpTargetImpossiblePrimaryColorGreen'
        ),
    })
    jump_target_impossible_primary_color_blue: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8d512b82, original_name='JumpTargetImpossiblePrimaryColorBlue'
        ),
    })
    jump_target_impossible_secondary_color_red: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x39f1698d, original_name='JumpTargetImpossibleSecondaryColorRed'
        ),
    })
    jump_target_impossible_secondary_color_green: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc768c1e9, original_name='JumpTargetImpossibleSecondaryColorGreen'
        ),
    })
    jump_target_impossible_secondary_color_blue: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x55c47b0e, original_name='JumpTargetImpossibleSecondaryColorBlue'
        ),
    })
    jump_target_occluded_opacity: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa009aea2, original_name='JumpTargetOccludedOpacity'
        ),
    })
    jump_target_non_occluded_opacity: float = dataclasses.field(default=0.699999988079071, metadata={
        'reflection': FieldReflection[float](
            float, id=0x38080bbf, original_name='JumpTargetNonOccludedOpacity'
        ),
    })
    jump_target_height: float = dataclasses.field(default=0.800000011920929, metadata={
        'reflection': FieldReflection[float](
            float, id=0x71017dbe, original_name='JumpTargetHeight'
        ),
    })
    jump_target_interpolate_in_time: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4a996997, original_name='JumpTargetInterpolateInTime'
        ),
    })
    jump_target_interpolate_out_time: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9f9fa6f3, original_name='JumpTargetInterpolateOutTime'
        ),
    })
    jump_target_color_animate_period: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x932fea01, original_name='JumpTargetColorAnimatePeriod'
        ),
    })
    jump_target_z_rotate_speed: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x165f0fa8, original_name='JumpTargetZRotateSpeed'
        ),
    })
    orbit_point_z_rotate_speed: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6bd6b11f, original_name='OrbitPointZRotateSpeed'
        ),
    })
    unknown_0x42420f6e: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x42420f6e, original_name='Unknown', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    flower_reticle_scale: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa63229f1, original_name='FlowerReticleScale'
        ),
    })
    flower_reticle_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=0.47058799862861633), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xbda45f1a, original_name='FlowerReticleColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    missile_bracket_open_holster_time: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb090e147, original_name='MissileBracketOpenHolsterTime'
        ),
    })
    unknown_0x4c73a43d: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4c73a43d, original_name='Unknown'
        ),
    })
    unknown_0x6543d31b: float = dataclasses.field(default=0.8999999761581421, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6543d31b, original_name='Unknown'
        ),
    })
    missile_bracket_missile_fire_anim_time: float = dataclasses.field(default=0.15000000596046448, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8cd2d1ce, original_name='MissileBracketMissileFireAnimTime'
        ),
    })
    missile_bracket_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4078429937362671, b=0.01960800029337406, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xe42f6be0, original_name='MissileBracketColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    inner_beam_icon_open_time: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x45910e5d, original_name='InnerBeamIconOpenTime'
        ),
    })
    inner_beam_icon_scale: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x07b30fa0, original_name='InnerBeamIconScale'
        ),
    })
    inner_beam_icon_color_power_beam: Color = dataclasses.field(default_factory=lambda: Color(r=0.274509996175766, g=0.4196079969406128, b=1.0, a=0.23529399931430817), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x13ce8500, original_name='InnerBeamIconColorPowerBeam', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    inner_beam_icon_color_ice_beam: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.23529399931430817), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x9829f256, original_name='InnerBeamIconColorIceBeam', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    inner_beam_icon_color_wave_beam: Color = dataclasses.field(default_factory=lambda: Color(r=0.4196079969406128, g=0.08627499639987946, b=0.5686269998550415, a=0.23137299716472626), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x77a613b9, original_name='InnerBeamIconColorWaveBeam', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    inner_beam_icon_color_plasma_beam: Color = dataclasses.field(default_factory=lambda: Color(r=0.4274510145187378, g=0.07451000064611435, b=0.08235300332307816, a=0.23137299716472626), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xdfa81287, original_name='InnerBeamIconColorPlasmaBeam', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    lock_on_confirm_reticle_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=0.47058799862861633), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xda752c50, original_name='LockOnConfirmReticleColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    seeker_reticle_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=0.7058820128440857), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x7b544e14, original_name='SeekerReticleColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    lock_on_confirm_min_radius_viewport: float = dataclasses.field(default=160.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x618d150a, original_name='LockOnConfirmMinRadiusViewport'
        ),
    })
    lock_on_confirm_max_radius_viewport: float = dataclasses.field(default=240.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x209a2a8c, original_name='LockOnConfirmMaxRadiusViewport'
        ),
    })
    flower_min_radius_viewport: float = dataclasses.field(default=160.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xacb3f8f7, original_name='FlowerMinRadiusViewport'
        ),
    })
    flower_max_radius_viewport: float = dataclasses.field(default=240.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xeda4c771, original_name='FlowerMaxRadiusViewport'
        ),
    })
    seeker_min_radius_viewport: float = dataclasses.field(default=160.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd3427574, original_name='SeekerMinRadiusViewport'
        ),
    })
    seeker_max_radius_viewport: float = dataclasses.field(default=240.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x92554af2, original_name='SeekerMaxRadiusViewport'
        ),
    })
    missile_bracket_min_radius_viewport: float = dataclasses.field(default=160.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1e134e75, original_name='MissileBracketMinRadiusViewport'
        ),
    })
    missile_bracket_max_radius_viewport: float = dataclasses.field(default=240.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5f0471f3, original_name='MissileBracketMaxRadiusViewport'
        ),
    })
    inner_icon_min_radius_viewport: float = dataclasses.field(default=160.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe90548ac, original_name='InnerIconMinRadiusViewport'
        ),
    })
    inner_icon_max_radius_viewport: float = dataclasses.field(default=240.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa812772a, original_name='InnerIconMaxRadiusViewport'
        ),
    })
    outer_icon_min_radius_viewport: float = dataclasses.field(default=160.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2d75c7be, original_name='OuterIconMinRadiusViewport'
        ),
    })
    outer_icon_max_radius_viewport: float = dataclasses.field(default=240.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6c62f838, original_name='OuterIconMaxRadiusViewport'
        ),
    })
    lock_fire_min_radius_viewport: float = dataclasses.field(default=160.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf98e6242, original_name='LockFireMinRadiusViewport'
        ),
    })
    lock_fire_max_radius_viewport: float = dataclasses.field(default=240.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb8995dc4, original_name='LockFireMaxRadiusViewport'
        ),
    })
    lock_dagger_min_radius_viewport: float = dataclasses.field(default=160.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5009c614, original_name='LockDaggerMinRadiusViewport'
        ),
    })
    lock_dagger_max_radius_viewport: float = dataclasses.field(default=240.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x111ef992, original_name='LockDaggerMaxRadiusViewport'
        ),
    })
    grapple_icon_scale: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xec0ff888, original_name='GrappleIconScale'
        ),
    })
    grapple_icon_scale_inactive: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf229e05e, original_name='GrappleIconScaleInactive'
        ),
    })
    grapple_icon_min_radius_viewport: float = dataclasses.field(default=80.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x498d794a, original_name='GrappleIconMinRadiusViewport'
        ),
    })
    grapple_icon_max_radius_viewport: float = dataclasses.field(default=240.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x089a46cc, original_name='GrappleIconMaxRadiusViewport'
        ),
    })
    grapple_icon_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf7998e63, original_name='GrappleIconColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    grapple_icon_color_inactive: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.6196079850196838, b=0.1568630039691925, a=0.2509799897670746), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x3ce853e3, original_name='GrappleIconColorInactive', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    grapple_icon_color_inactive_out_of_range: Color = dataclasses.field(default_factory=lambda: Color(r=0.5, g=0.3100000023841858, b=0.07999999821186066, a=0.25), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf593614f, original_name='GrappleIconColorInactiveOutOfRange', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    unknown_0x083b1cc8: Color = dataclasses.field(default_factory=lambda: Color(r=0.10980399698019028, g=0.18431399762630463, b=0.23921599984169006, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x083b1cc8, original_name='Unknown', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    unknown_0x966982b1: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x966982b1, original_name='Unknown'
        ),
    })
    grapple_max_visible_distance: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x34915075, original_name='GrappleMaxVisibleDistance'
        ),
    })
    charge_gauge_glow_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.5372549891471863, g=0.8392159938812256, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf9799f5f, original_name='ChargeGaugeGlowColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    charge_gauge_glow_time: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9b980788, original_name='ChargeGaugeGlowTime'
        ),
    })
    orbit_point_model_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=0.49019598960876465), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x3523a47f, original_name='OrbitPointModelColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    crosshairs_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=0.19607800245285034), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x27358b4d, original_name='CrosshairsColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    crosshairs_fade_in_out_time: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2ff52290, original_name='CrosshairsFadeInOutTime'
        ),
    })
    is_draw_orbit_point_default: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x8a548cc9, original_name='IsDrawOrbitPointDefault'
        ),
    })
    charge_gauge_glow_color_b: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=0.49019598960876465), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x65d449e1, original_name='ChargeGaugeGlowColorB', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    charge_gauge_flash_cycle_time: float = dataclasses.field(default=0.800000011920929, metadata={
        'reflection': FieldReflection[float](
            float, id=0x42c7fbe4, original_name='ChargeGaugeFlashCycleTime'
        ),
    })
    x_ray_seeker_min_radius_viewport: float = dataclasses.field(default=80.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x13820c03, original_name='XRaySeekerMinRadiusViewport'
        ),
    })
    x_ray_seeker_max_radius_viewport: float = dataclasses.field(default=80.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x52953385, original_name='XRaySeekerMaxRadiusViewport'
        ),
    })
    x_ray_seeker_reticle_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.2549020051956177), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x0cd8fe5d, original_name='XRaySeekerReticleColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    x_ray_seeker_target_reticle_scale: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdd8cf478, original_name='XRaySeekerTargetReticleScale'
        ),
    })
    unknown_0xcbac6d52: float = dataclasses.field(default=32.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcbac6d52, original_name='Unknown'
        ),
    })
    unknown_0x980a75b6: float = dataclasses.field(default=120.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x980a75b6, original_name='Unknown'
        ),
    })
    unknown_0xcd1e0e91: float = dataclasses.field(default=18.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcd1e0e91, original_name='Unknown'
        ),
    })
    unknown_0xa3e32481: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa3e32481, original_name='Unknown'
        ),
    })
    aiming_cursor_clamp_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x8bfd0783, original_name='AimingCursorClampColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    aiming_cursor_clamp_secondary_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xca3a8d19, original_name='AimingCursorClampSecondaryColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    aiming_cursor_clamp_offset: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbc9e3bf9, original_name='AimingCursorClampOffset'
        ),
    })
    aiming_cursor_clamp_time: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0x18675e4e, original_name='AimingCursorClampTime'
        ),
    })
    aiming_cursor_center_ring_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x9db1ddb6, original_name='AimingCursorCenterRingColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    aiming_cursor_center_ring_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x45b717df, original_name='AimingCursorCenterRingOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    aiming_cursor_center_ring_secondary_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x6f659cdb, original_name='AimingCursorCenterRingSecondaryColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    aiming_cursor_center_ring_outline_secondary_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xe97e5ba3, original_name='AimingCursorCenterRingOutlineSecondaryColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    aiming_cursor_center_ring_color_transition_time: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfec02688, original_name='AimingCursorCenterRingColorTransitionTime'
        ),
    })
    aiming_cursor_radius: float = dataclasses.field(default=36.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x84709ab2, original_name='AimingCursorRadius'
        ),
    })
    aiming_cursor_depth_ring_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xbf7aa2d0, original_name='AimingCursorDepthRingColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    aiming_cursor_depth_ring_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xc35b6f6b, original_name='AimingCursorDepthRingOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    aiming_cursor_depth_ring_secondary_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xb1128885, original_name='AimingCursorDepthRingSecondaryColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    aiming_cursor_depth_ring_outline_secondary_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x8faa7bb1, original_name='AimingCursorDepthRingOutlineSecondaryColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    aiming_cursor_depth_ring_min_size: float = dataclasses.field(default=12.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xae50c432, original_name='AimingCursorDepthRingMinSize'
        ),
    })
    aiming_cursor_depth_ring_max_size: float = dataclasses.field(default=36.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3e23d4d8, original_name='AimingCursorDepthRingMaxSize'
        ),
    })
    x_ray_aiming_cursor_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xb0522ac7, original_name='XRayAimingCursorColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    x_ray_depth_cursor_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xa4995c5c, original_name='XRayDepthCursorColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    x_ray_depth_cursor_min_size: float = dataclasses.field(default=12.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6363d78d, original_name='XRayDepthCursorMinSize'
        ),
    })
    x_ray_depth_cursor_max_size: float = dataclasses.field(default=36.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf310c767, original_name='XRayDepthCursorMaxSize'
        ),
    })
    unknown_0xc29882b7: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xc29882b7, original_name='Unknown', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    unknown_0xd33fcc91: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xd33fcc91, original_name='Unknown', from_json=Color.from_json, to_json=Color.to_json
        ),
    })

    def get_name(self) -> str:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    def set_name(self, name: str) -> None:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    @classmethod
    def object_type(cls) -> str:
        return 'TWTG'

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
        if property_count != 136:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7fda1466
        instance_name = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd15b6a54
        combat_reticules = TweakTargeting_CombatReticules.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe87e2134
        charge_beam = TweakTargeting_ChargeBeam.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc6915d69
        orbit_lock = TweakTargeting_OrbitLock.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5173932f
        tweak_targeting_outer_beam_icon = TweakTargeting_OuterBeamIcon.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23ff4be4
        power_beam_icon_configurations = TIcon_Configurations.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x92e98613
        ice_beam_icon_configurations = TIcon_Configurations.from_stream(data, game, property_size, default_override={'something0_angle': 90.0, 'something1_angle': 90.0, 'something2_angle': 90.0, 'something3_angle': 90.0, 'something4_angle': 90.0, 'something5_angle': 90.0, 'something6_angle': 90.0, 'something7_angle': 90.0, 'something8_angle': 90.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64833842
        wave_beam_icon_configurations = TIcon_Configurations.from_stream(data, game, property_size, default_override={'something0_angle': 150.0, 'something1_angle': 150.0, 'something2_angle': 150.0, 'something3_angle': 150.0, 'something4_angle': 150.0, 'something5_angle': 150.0, 'something6_angle': 150.0, 'something7_angle': 150.0, 'something8_angle': 150.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8dfd6e3c
        plasma_beam_icon_configurations = TIcon_Configurations.from_stream(data, game, property_size, default_override={'something0_angle': 210.0, 'something1_angle': 210.0, 'something2_angle': 210.0, 'something3_angle': 210.0, 'something4_angle': 210.0, 'something5_angle': 210.0, 'something6_angle': 210.0, 'something7_angle': 210.0, 'something8_angle': 210.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbc5a41b2
        charge_gauge = TweakTargeting_Charge_Gauge.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x00183589
        lock_fire = TweakTargeting_LockFire.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd20ecc07
        lock_dagger = TweakTargeting_LockDagger.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x65ef9f2a
        scan = TweakTargeting_Scan.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc3410560
        unknown_0xc3410560 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3eb13041
        orbit_lock_on_acquire_target_interpolation_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5e67cab0
        orbit_lock_on_lose_target_interpolation_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe0ca98ac
        orbit_lock_on_switch_target_interpolation_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc1e35abb
        lock_on_confirm_reticle_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9f8d62c1
        seeker_acquire_target_interpolation_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xff5eeeb9
        seeker_lose_target_interpolation_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0d0b660d
        seeker_switch_target_interpolation_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x132dd09e
        seeker_target_reticle_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03efc783
        seeker_z_rotation_rate = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdcbd7bf8
        unknown_0xdcbd7bf8 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2acd6b4b
        orbit_point_primary_color_red = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb4c6c331
        orbit_point_primary_color_green = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x27d02089
        orbit_point_primary_color_blue = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xae89310e
        orbit_point_secondary_color_red = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb27644df
        orbit_point_secondary_color_green = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21e2d1cc
        orbit_point_secondary_color_blue = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8e3afef8
        orbit_point_occluded_opacity = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5c489cb5
        orbit_point_non_occluded_opacity = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xef2c842e
        orbit_point_z_offset = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x61a6a38e
        orbit_point_interpolate_in_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfbdf31f9
        orbit_point_interpolate_out_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf76f7d0b
        orbit_point_color_animate_period = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x810b3a08
        jump_target_possible_primary_color_red = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x73fe1553
        jump_target_possible_primary_color_green = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc8aef6f2
        jump_target_possible_primary_color_blue = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x69b1e76c
        jump_target_possible_secondary_color_red = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8a0dfd23
        jump_target_possible_secondary_color_green = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8299e96e
        jump_target_possible_secondary_color_blue = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa18a3f25
        jump_target_impossible_primary_color_red = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23be9bb2
        jump_target_impossible_primary_color_green = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8d512b82
        jump_target_impossible_primary_color_blue = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x39f1698d
        jump_target_impossible_secondary_color_red = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc768c1e9
        jump_target_impossible_secondary_color_green = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x55c47b0e
        jump_target_impossible_secondary_color_blue = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa009aea2
        jump_target_occluded_opacity = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x38080bbf
        jump_target_non_occluded_opacity = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71017dbe
        jump_target_height = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4a996997
        jump_target_interpolate_in_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9f9fa6f3
        jump_target_interpolate_out_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x932fea01
        jump_target_color_animate_period = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x165f0fa8
        jump_target_z_rotate_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6bd6b11f
        orbit_point_z_rotate_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42420f6e
        unknown_0x42420f6e = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa63229f1
        flower_reticle_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbda45f1a
        flower_reticle_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb090e147
        missile_bracket_open_holster_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4c73a43d
        unknown_0x4c73a43d = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6543d31b
        unknown_0x6543d31b = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8cd2d1ce
        missile_bracket_missile_fire_anim_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe42f6be0
        missile_bracket_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x45910e5d
        inner_beam_icon_open_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x07b30fa0
        inner_beam_icon_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13ce8500
        inner_beam_icon_color_power_beam = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9829f256
        inner_beam_icon_color_ice_beam = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77a613b9
        inner_beam_icon_color_wave_beam = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdfa81287
        inner_beam_icon_color_plasma_beam = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xda752c50
        lock_on_confirm_reticle_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7b544e14
        seeker_reticle_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x618d150a
        lock_on_confirm_min_radius_viewport = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x209a2a8c
        lock_on_confirm_max_radius_viewport = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xacb3f8f7
        flower_min_radius_viewport = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xeda4c771
        flower_max_radius_viewport = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd3427574
        seeker_min_radius_viewport = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x92554af2
        seeker_max_radius_viewport = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1e134e75
        missile_bracket_min_radius_viewport = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5f0471f3
        missile_bracket_max_radius_viewport = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe90548ac
        inner_icon_min_radius_viewport = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa812772a
        inner_icon_max_radius_viewport = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2d75c7be
        outer_icon_min_radius_viewport = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6c62f838
        outer_icon_max_radius_viewport = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf98e6242
        lock_fire_min_radius_viewport = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb8995dc4
        lock_fire_max_radius_viewport = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5009c614
        lock_dagger_min_radius_viewport = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x111ef992
        lock_dagger_max_radius_viewport = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xec0ff888
        grapple_icon_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf229e05e
        grapple_icon_scale_inactive = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x498d794a
        grapple_icon_min_radius_viewport = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x089a46cc
        grapple_icon_max_radius_viewport = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf7998e63
        grapple_icon_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3ce853e3
        grapple_icon_color_inactive = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf593614f
        grapple_icon_color_inactive_out_of_range = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x083b1cc8
        unknown_0x083b1cc8 = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x966982b1
        unknown_0x966982b1 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x34915075
        grapple_max_visible_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf9799f5f
        charge_gauge_glow_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9b980788
        charge_gauge_glow_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3523a47f
        orbit_point_model_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x27358b4d
        crosshairs_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2ff52290
        crosshairs_fade_in_out_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8a548cc9
        is_draw_orbit_point_default = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x65d449e1
        charge_gauge_glow_color_b = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42c7fbe4
        charge_gauge_flash_cycle_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13820c03
        x_ray_seeker_min_radius_viewport = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x52953385
        x_ray_seeker_max_radius_viewport = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0cd8fe5d
        x_ray_seeker_reticle_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdd8cf478
        x_ray_seeker_target_reticle_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcbac6d52
        unknown_0xcbac6d52 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x980a75b6
        unknown_0x980a75b6 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcd1e0e91
        unknown_0xcd1e0e91 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa3e32481
        unknown_0xa3e32481 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8bfd0783
        aiming_cursor_clamp_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xca3a8d19
        aiming_cursor_clamp_secondary_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbc9e3bf9
        aiming_cursor_clamp_offset = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x18675e4e
        aiming_cursor_clamp_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9db1ddb6
        aiming_cursor_center_ring_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x45b717df
        aiming_cursor_center_ring_outline_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6f659cdb
        aiming_cursor_center_ring_secondary_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe97e5ba3
        aiming_cursor_center_ring_outline_secondary_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfec02688
        aiming_cursor_center_ring_color_transition_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x84709ab2
        aiming_cursor_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbf7aa2d0
        aiming_cursor_depth_ring_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc35b6f6b
        aiming_cursor_depth_ring_outline_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb1128885
        aiming_cursor_depth_ring_secondary_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8faa7bb1
        aiming_cursor_depth_ring_outline_secondary_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xae50c432
        aiming_cursor_depth_ring_min_size = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3e23d4d8
        aiming_cursor_depth_ring_max_size = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb0522ac7
        x_ray_aiming_cursor_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa4995c5c
        x_ray_depth_cursor_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6363d78d
        x_ray_depth_cursor_min_size = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf310c767
        x_ray_depth_cursor_max_size = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc29882b7
        unknown_0xc29882b7 = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd33fcc91
        unknown_0xd33fcc91 = Color.from_stream(data, game, property_size)
    
        return cls(instance_name, combat_reticules, charge_beam, orbit_lock, tweak_targeting_outer_beam_icon, power_beam_icon_configurations, ice_beam_icon_configurations, wave_beam_icon_configurations, plasma_beam_icon_configurations, charge_gauge, lock_fire, lock_dagger, scan, unknown_0xc3410560, orbit_lock_on_acquire_target_interpolation_time, orbit_lock_on_lose_target_interpolation_time, orbit_lock_on_switch_target_interpolation_time, lock_on_confirm_reticle_scale, seeker_acquire_target_interpolation_time, seeker_lose_target_interpolation_time, seeker_switch_target_interpolation_time, seeker_target_reticle_scale, seeker_z_rotation_rate, unknown_0xdcbd7bf8, orbit_point_primary_color_red, orbit_point_primary_color_green, orbit_point_primary_color_blue, orbit_point_secondary_color_red, orbit_point_secondary_color_green, orbit_point_secondary_color_blue, orbit_point_occluded_opacity, orbit_point_non_occluded_opacity, orbit_point_z_offset, orbit_point_interpolate_in_time, orbit_point_interpolate_out_time, orbit_point_color_animate_period, jump_target_possible_primary_color_red, jump_target_possible_primary_color_green, jump_target_possible_primary_color_blue, jump_target_possible_secondary_color_red, jump_target_possible_secondary_color_green, jump_target_possible_secondary_color_blue, jump_target_impossible_primary_color_red, jump_target_impossible_primary_color_green, jump_target_impossible_primary_color_blue, jump_target_impossible_secondary_color_red, jump_target_impossible_secondary_color_green, jump_target_impossible_secondary_color_blue, jump_target_occluded_opacity, jump_target_non_occluded_opacity, jump_target_height, jump_target_interpolate_in_time, jump_target_interpolate_out_time, jump_target_color_animate_period, jump_target_z_rotate_speed, orbit_point_z_rotate_speed, unknown_0x42420f6e, flower_reticle_scale, flower_reticle_color, missile_bracket_open_holster_time, unknown_0x4c73a43d, unknown_0x6543d31b, missile_bracket_missile_fire_anim_time, missile_bracket_color, inner_beam_icon_open_time, inner_beam_icon_scale, inner_beam_icon_color_power_beam, inner_beam_icon_color_ice_beam, inner_beam_icon_color_wave_beam, inner_beam_icon_color_plasma_beam, lock_on_confirm_reticle_color, seeker_reticle_color, lock_on_confirm_min_radius_viewport, lock_on_confirm_max_radius_viewport, flower_min_radius_viewport, flower_max_radius_viewport, seeker_min_radius_viewport, seeker_max_radius_viewport, missile_bracket_min_radius_viewport, missile_bracket_max_radius_viewport, inner_icon_min_radius_viewport, inner_icon_max_radius_viewport, outer_icon_min_radius_viewport, outer_icon_max_radius_viewport, lock_fire_min_radius_viewport, lock_fire_max_radius_viewport, lock_dagger_min_radius_viewport, lock_dagger_max_radius_viewport, grapple_icon_scale, grapple_icon_scale_inactive, grapple_icon_min_radius_viewport, grapple_icon_max_radius_viewport, grapple_icon_color, grapple_icon_color_inactive, grapple_icon_color_inactive_out_of_range, unknown_0x083b1cc8, unknown_0x966982b1, grapple_max_visible_distance, charge_gauge_glow_color, charge_gauge_glow_time, orbit_point_model_color, crosshairs_color, crosshairs_fade_in_out_time, is_draw_orbit_point_default, charge_gauge_glow_color_b, charge_gauge_flash_cycle_time, x_ray_seeker_min_radius_viewport, x_ray_seeker_max_radius_viewport, x_ray_seeker_reticle_color, x_ray_seeker_target_reticle_scale, unknown_0xcbac6d52, unknown_0x980a75b6, unknown_0xcd1e0e91, unknown_0xa3e32481, aiming_cursor_clamp_color, aiming_cursor_clamp_secondary_color, aiming_cursor_clamp_offset, aiming_cursor_clamp_time, aiming_cursor_center_ring_color, aiming_cursor_center_ring_outline_color, aiming_cursor_center_ring_secondary_color, aiming_cursor_center_ring_outline_secondary_color, aiming_cursor_center_ring_color_transition_time, aiming_cursor_radius, aiming_cursor_depth_ring_color, aiming_cursor_depth_ring_outline_color, aiming_cursor_depth_ring_secondary_color, aiming_cursor_depth_ring_outline_secondary_color, aiming_cursor_depth_ring_min_size, aiming_cursor_depth_ring_max_size, x_ray_aiming_cursor_color, x_ray_depth_cursor_color, x_ray_depth_cursor_min_size, x_ray_depth_cursor_max_size, unknown_0xc29882b7, unknown_0xd33fcc91)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x88')  # 136 properties

        data.write(b'\x7f\xda\x14f')  # 0x7fda1466
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.instance_name.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd1[jT')  # 0xd15b6a54
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.combat_reticules.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe8~!4')  # 0xe87e2134
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.charge_beam.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc6\x91]i')  # 0xc6915d69
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.orbit_lock.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'Qs\x93/')  # 0x5173932f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.tweak_targeting_outer_beam_icon.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'#\xffK\xe4')  # 0x23ff4be4
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.power_beam_icon_configurations.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x92\xe9\x86\x13')  # 0x92e98613
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ice_beam_icon_configurations.to_stream(data, game, default_override={'something0_angle': 90.0, 'something1_angle': 90.0, 'something2_angle': 90.0, 'something3_angle': 90.0, 'something4_angle': 90.0, 'something5_angle': 90.0, 'something6_angle': 90.0, 'something7_angle': 90.0, 'something8_angle': 90.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'd\x838B')  # 0x64833842
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.wave_beam_icon_configurations.to_stream(data, game, default_override={'something0_angle': 150.0, 'something1_angle': 150.0, 'something2_angle': 150.0, 'something3_angle': 150.0, 'something4_angle': 150.0, 'something5_angle': 150.0, 'something6_angle': 150.0, 'something7_angle': 150.0, 'something8_angle': 150.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8d\xfdn<')  # 0x8dfd6e3c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.plasma_beam_icon_configurations.to_stream(data, game, default_override={'something0_angle': 210.0, 'something1_angle': 210.0, 'something2_angle': 210.0, 'something3_angle': 210.0, 'something4_angle': 210.0, 'something5_angle': 210.0, 'something6_angle': 210.0, 'something7_angle': 210.0, 'something8_angle': 210.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbcZA\xb2')  # 0xbc5a41b2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.charge_gauge.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x00\x185\x89')  # 0x183589
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.lock_fire.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd2\x0e\xcc\x07')  # 0xd20ecc07
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.lock_dagger.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'e\xef\x9f*')  # 0x65ef9f2a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.scan.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc3A\x05`')  # 0xc3410560
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xc3410560))

        data.write(b'>\xb10A')  # 0x3eb13041
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_on_acquire_target_interpolation_time))

        data.write(b'^g\xca\xb0')  # 0x5e67cab0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_on_lose_target_interpolation_time))

        data.write(b'\xe0\xca\x98\xac')  # 0xe0ca98ac
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_lock_on_switch_target_interpolation_time))

        data.write(b'\xc1\xe3Z\xbb')  # 0xc1e35abb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.lock_on_confirm_reticle_scale))

        data.write(b'\x9f\x8db\xc1')  # 0x9f8d62c1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.seeker_acquire_target_interpolation_time))

        data.write(b'\xff^\xee\xb9')  # 0xff5eeeb9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.seeker_lose_target_interpolation_time))

        data.write(b'\r\x0bf\r')  # 0xd0b660d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.seeker_switch_target_interpolation_time))

        data.write(b'\x13-\xd0\x9e')  # 0x132dd09e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.seeker_target_reticle_scale))

        data.write(b'\x03\xef\xc7\x83')  # 0x3efc783
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.seeker_z_rotation_rate))

        data.write(b'\xdc\xbd{\xf8')  # 0xdcbd7bf8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xdcbd7bf8))

        data.write(b'*\xcdkK')  # 0x2acd6b4b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_point_primary_color_red))

        data.write(b'\xb4\xc6\xc31')  # 0xb4c6c331
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_point_primary_color_green))

        data.write(b"'\xd0 \x89")  # 0x27d02089
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_point_primary_color_blue))

        data.write(b'\xae\x891\x0e')  # 0xae89310e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_point_secondary_color_red))

        data.write(b'\xb2vD\xdf')  # 0xb27644df
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_point_secondary_color_green))

        data.write(b'!\xe2\xd1\xcc')  # 0x21e2d1cc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_point_secondary_color_blue))

        data.write(b'\x8e:\xfe\xf8')  # 0x8e3afef8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_point_occluded_opacity))

        data.write(b'\\H\x9c\xb5')  # 0x5c489cb5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_point_non_occluded_opacity))

        data.write(b'\xef,\x84.')  # 0xef2c842e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_point_z_offset))

        data.write(b'a\xa6\xa3\x8e')  # 0x61a6a38e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_point_interpolate_in_time))

        data.write(b'\xfb\xdf1\xf9')  # 0xfbdf31f9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_point_interpolate_out_time))

        data.write(b'\xf7o}\x0b')  # 0xf76f7d0b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_point_color_animate_period))

        data.write(b'\x81\x0b:\x08')  # 0x810b3a08
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_target_possible_primary_color_red))

        data.write(b's\xfe\x15S')  # 0x73fe1553
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_target_possible_primary_color_green))

        data.write(b'\xc8\xae\xf6\xf2')  # 0xc8aef6f2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_target_possible_primary_color_blue))

        data.write(b'i\xb1\xe7l')  # 0x69b1e76c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_target_possible_secondary_color_red))

        data.write(b'\x8a\r\xfd#')  # 0x8a0dfd23
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_target_possible_secondary_color_green))

        data.write(b'\x82\x99\xe9n')  # 0x8299e96e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_target_possible_secondary_color_blue))

        data.write(b'\xa1\x8a?%')  # 0xa18a3f25
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_target_impossible_primary_color_red))

        data.write(b'#\xbe\x9b\xb2')  # 0x23be9bb2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_target_impossible_primary_color_green))

        data.write(b'\x8dQ+\x82')  # 0x8d512b82
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_target_impossible_primary_color_blue))

        data.write(b'9\xf1i\x8d')  # 0x39f1698d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_target_impossible_secondary_color_red))

        data.write(b'\xc7h\xc1\xe9')  # 0xc768c1e9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_target_impossible_secondary_color_green))

        data.write(b'U\xc4{\x0e')  # 0x55c47b0e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_target_impossible_secondary_color_blue))

        data.write(b'\xa0\t\xae\xa2')  # 0xa009aea2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_target_occluded_opacity))

        data.write(b'8\x08\x0b\xbf')  # 0x38080bbf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_target_non_occluded_opacity))

        data.write(b'q\x01}\xbe')  # 0x71017dbe
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_target_height))

        data.write(b'J\x99i\x97')  # 0x4a996997
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_target_interpolate_in_time))

        data.write(b'\x9f\x9f\xa6\xf3')  # 0x9f9fa6f3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_target_interpolate_out_time))

        data.write(b'\x93/\xea\x01')  # 0x932fea01
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_target_color_animate_period))

        data.write(b'\x16_\x0f\xa8')  # 0x165f0fa8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_target_z_rotate_speed))

        data.write(b'k\xd6\xb1\x1f')  # 0x6bd6b11f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orbit_point_z_rotate_speed))

        data.write(b'BB\x0fn')  # 0x42420f6e
        data.write(b'\x00\x10')  # size
        self.unknown_0x42420f6e.to_stream(data, game)

        data.write(b'\xa62)\xf1')  # 0xa63229f1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flower_reticle_scale))

        data.write(b'\xbd\xa4_\x1a')  # 0xbda45f1a
        data.write(b'\x00\x10')  # size
        self.flower_reticle_color.to_stream(data, game)

        data.write(b'\xb0\x90\xe1G')  # 0xb090e147
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.missile_bracket_open_holster_time))

        data.write(b'Ls\xa4=')  # 0x4c73a43d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4c73a43d))

        data.write(b'eC\xd3\x1b')  # 0x6543d31b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6543d31b))

        data.write(b'\x8c\xd2\xd1\xce')  # 0x8cd2d1ce
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.missile_bracket_missile_fire_anim_time))

        data.write(b'\xe4/k\xe0')  # 0xe42f6be0
        data.write(b'\x00\x10')  # size
        self.missile_bracket_color.to_stream(data, game)

        data.write(b'E\x91\x0e]')  # 0x45910e5d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.inner_beam_icon_open_time))

        data.write(b'\x07\xb3\x0f\xa0')  # 0x7b30fa0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.inner_beam_icon_scale))

        data.write(b'\x13\xce\x85\x00')  # 0x13ce8500
        data.write(b'\x00\x10')  # size
        self.inner_beam_icon_color_power_beam.to_stream(data, game)

        data.write(b'\x98)\xf2V')  # 0x9829f256
        data.write(b'\x00\x10')  # size
        self.inner_beam_icon_color_ice_beam.to_stream(data, game)

        data.write(b'w\xa6\x13\xb9')  # 0x77a613b9
        data.write(b'\x00\x10')  # size
        self.inner_beam_icon_color_wave_beam.to_stream(data, game)

        data.write(b'\xdf\xa8\x12\x87')  # 0xdfa81287
        data.write(b'\x00\x10')  # size
        self.inner_beam_icon_color_plasma_beam.to_stream(data, game)

        data.write(b'\xdau,P')  # 0xda752c50
        data.write(b'\x00\x10')  # size
        self.lock_on_confirm_reticle_color.to_stream(data, game)

        data.write(b'{TN\x14')  # 0x7b544e14
        data.write(b'\x00\x10')  # size
        self.seeker_reticle_color.to_stream(data, game)

        data.write(b'a\x8d\x15\n')  # 0x618d150a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.lock_on_confirm_min_radius_viewport))

        data.write(b' \x9a*\x8c')  # 0x209a2a8c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.lock_on_confirm_max_radius_viewport))

        data.write(b'\xac\xb3\xf8\xf7')  # 0xacb3f8f7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flower_min_radius_viewport))

        data.write(b'\xed\xa4\xc7q')  # 0xeda4c771
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flower_max_radius_viewport))

        data.write(b'\xd3But')  # 0xd3427574
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.seeker_min_radius_viewport))

        data.write(b'\x92UJ\xf2')  # 0x92554af2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.seeker_max_radius_viewport))

        data.write(b'\x1e\x13Nu')  # 0x1e134e75
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.missile_bracket_min_radius_viewport))

        data.write(b'_\x04q\xf3')  # 0x5f0471f3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.missile_bracket_max_radius_viewport))

        data.write(b'\xe9\x05H\xac')  # 0xe90548ac
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.inner_icon_min_radius_viewport))

        data.write(b'\xa8\x12w*')  # 0xa812772a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.inner_icon_max_radius_viewport))

        data.write(b'-u\xc7\xbe')  # 0x2d75c7be
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.outer_icon_min_radius_viewport))

        data.write(b'lb\xf88')  # 0x6c62f838
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.outer_icon_max_radius_viewport))

        data.write(b'\xf9\x8ebB')  # 0xf98e6242
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.lock_fire_min_radius_viewport))

        data.write(b'\xb8\x99]\xc4')  # 0xb8995dc4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.lock_fire_max_radius_viewport))

        data.write(b'P\t\xc6\x14')  # 0x5009c614
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.lock_dagger_min_radius_viewport))

        data.write(b'\x11\x1e\xf9\x92')  # 0x111ef992
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.lock_dagger_max_radius_viewport))

        data.write(b'\xec\x0f\xf8\x88')  # 0xec0ff888
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grapple_icon_scale))

        data.write(b'\xf2)\xe0^')  # 0xf229e05e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grapple_icon_scale_inactive))

        data.write(b'I\x8dyJ')  # 0x498d794a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grapple_icon_min_radius_viewport))

        data.write(b'\x08\x9aF\xcc')  # 0x89a46cc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grapple_icon_max_radius_viewport))

        data.write(b'\xf7\x99\x8ec')  # 0xf7998e63
        data.write(b'\x00\x10')  # size
        self.grapple_icon_color.to_stream(data, game)

        data.write(b'<\xe8S\xe3')  # 0x3ce853e3
        data.write(b'\x00\x10')  # size
        self.grapple_icon_color_inactive.to_stream(data, game)

        data.write(b'\xf5\x93aO')  # 0xf593614f
        data.write(b'\x00\x10')  # size
        self.grapple_icon_color_inactive_out_of_range.to_stream(data, game)

        data.write(b'\x08;\x1c\xc8')  # 0x83b1cc8
        data.write(b'\x00\x10')  # size
        self.unknown_0x083b1cc8.to_stream(data, game)

        data.write(b'\x96i\x82\xb1')  # 0x966982b1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x966982b1))

        data.write(b'4\x91Pu')  # 0x34915075
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grapple_max_visible_distance))

        data.write(b'\xf9y\x9f_')  # 0xf9799f5f
        data.write(b'\x00\x10')  # size
        self.charge_gauge_glow_color.to_stream(data, game)

        data.write(b'\x9b\x98\x07\x88')  # 0x9b980788
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_gauge_glow_time))

        data.write(b'5#\xa4\x7f')  # 0x3523a47f
        data.write(b'\x00\x10')  # size
        self.orbit_point_model_color.to_stream(data, game)

        data.write(b"'5\x8bM")  # 0x27358b4d
        data.write(b'\x00\x10')  # size
        self.crosshairs_color.to_stream(data, game)

        data.write(b'/\xf5"\x90')  # 0x2ff52290
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.crosshairs_fade_in_out_time))

        data.write(b'\x8aT\x8c\xc9')  # 0x8a548cc9
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_draw_orbit_point_default))

        data.write(b'e\xd4I\xe1')  # 0x65d449e1
        data.write(b'\x00\x10')  # size
        self.charge_gauge_glow_color_b.to_stream(data, game)

        data.write(b'B\xc7\xfb\xe4')  # 0x42c7fbe4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_gauge_flash_cycle_time))

        data.write(b'\x13\x82\x0c\x03')  # 0x13820c03
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.x_ray_seeker_min_radius_viewport))

        data.write(b'R\x953\x85')  # 0x52953385
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.x_ray_seeker_max_radius_viewport))

        data.write(b'\x0c\xd8\xfe]')  # 0xcd8fe5d
        data.write(b'\x00\x10')  # size
        self.x_ray_seeker_reticle_color.to_stream(data, game)

        data.write(b'\xdd\x8c\xf4x')  # 0xdd8cf478
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.x_ray_seeker_target_reticle_scale))

        data.write(b'\xcb\xacmR')  # 0xcbac6d52
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcbac6d52))

        data.write(b'\x98\nu\xb6')  # 0x980a75b6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x980a75b6))

        data.write(b'\xcd\x1e\x0e\x91')  # 0xcd1e0e91
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xcd1e0e91))

        data.write(b'\xa3\xe3$\x81')  # 0xa3e32481
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa3e32481))

        data.write(b'\x8b\xfd\x07\x83')  # 0x8bfd0783
        data.write(b'\x00\x10')  # size
        self.aiming_cursor_clamp_color.to_stream(data, game)

        data.write(b'\xca:\x8d\x19')  # 0xca3a8d19
        data.write(b'\x00\x10')  # size
        self.aiming_cursor_clamp_secondary_color.to_stream(data, game)

        data.write(b'\xbc\x9e;\xf9')  # 0xbc9e3bf9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aiming_cursor_clamp_offset))

        data.write(b'\x18g^N')  # 0x18675e4e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aiming_cursor_clamp_time))

        data.write(b'\x9d\xb1\xdd\xb6')  # 0x9db1ddb6
        data.write(b'\x00\x10')  # size
        self.aiming_cursor_center_ring_color.to_stream(data, game)

        data.write(b'E\xb7\x17\xdf')  # 0x45b717df
        data.write(b'\x00\x10')  # size
        self.aiming_cursor_center_ring_outline_color.to_stream(data, game)

        data.write(b'oe\x9c\xdb')  # 0x6f659cdb
        data.write(b'\x00\x10')  # size
        self.aiming_cursor_center_ring_secondary_color.to_stream(data, game)

        data.write(b'\xe9~[\xa3')  # 0xe97e5ba3
        data.write(b'\x00\x10')  # size
        self.aiming_cursor_center_ring_outline_secondary_color.to_stream(data, game)

        data.write(b'\xfe\xc0&\x88')  # 0xfec02688
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aiming_cursor_center_ring_color_transition_time))

        data.write(b'\x84p\x9a\xb2')  # 0x84709ab2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aiming_cursor_radius))

        data.write(b'\xbfz\xa2\xd0')  # 0xbf7aa2d0
        data.write(b'\x00\x10')  # size
        self.aiming_cursor_depth_ring_color.to_stream(data, game)

        data.write(b'\xc3[ok')  # 0xc35b6f6b
        data.write(b'\x00\x10')  # size
        self.aiming_cursor_depth_ring_outline_color.to_stream(data, game)

        data.write(b'\xb1\x12\x88\x85')  # 0xb1128885
        data.write(b'\x00\x10')  # size
        self.aiming_cursor_depth_ring_secondary_color.to_stream(data, game)

        data.write(b'\x8f\xaa{\xb1')  # 0x8faa7bb1
        data.write(b'\x00\x10')  # size
        self.aiming_cursor_depth_ring_outline_secondary_color.to_stream(data, game)

        data.write(b'\xaeP\xc42')  # 0xae50c432
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aiming_cursor_depth_ring_min_size))

        data.write(b'>#\xd4\xd8')  # 0x3e23d4d8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.aiming_cursor_depth_ring_max_size))

        data.write(b'\xb0R*\xc7')  # 0xb0522ac7
        data.write(b'\x00\x10')  # size
        self.x_ray_aiming_cursor_color.to_stream(data, game)

        data.write(b'\xa4\x99\\\\')  # 0xa4995c5c
        data.write(b'\x00\x10')  # size
        self.x_ray_depth_cursor_color.to_stream(data, game)

        data.write(b'cc\xd7\x8d')  # 0x6363d78d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.x_ray_depth_cursor_min_size))

        data.write(b'\xf3\x10\xc7g')  # 0xf310c767
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.x_ray_depth_cursor_max_size))

        data.write(b'\xc2\x98\x82\xb7')  # 0xc29882b7
        data.write(b'\x00\x10')  # size
        self.unknown_0xc29882b7.to_stream(data, game)

        data.write(b'\xd3?\xcc\x91')  # 0xd33fcc91
        data.write(b'\x00\x10')  # size
        self.unknown_0xd33fcc91.to_stream(data, game)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakTargetingJson", data)
        return cls(
            instance_name=json_data['instance_name'],
            combat_reticules=TweakTargeting_CombatReticules.from_json(json_data['combat_reticules']),
            charge_beam=TweakTargeting_ChargeBeam.from_json(json_data['charge_beam']),
            orbit_lock=TweakTargeting_OrbitLock.from_json(json_data['orbit_lock']),
            tweak_targeting_outer_beam_icon=TweakTargeting_OuterBeamIcon.from_json(json_data['tweak_targeting_outer_beam_icon']),
            power_beam_icon_configurations=TIcon_Configurations.from_json(json_data['power_beam_icon_configurations']),
            ice_beam_icon_configurations=TIcon_Configurations.from_json(json_data['ice_beam_icon_configurations']),
            wave_beam_icon_configurations=TIcon_Configurations.from_json(json_data['wave_beam_icon_configurations']),
            plasma_beam_icon_configurations=TIcon_Configurations.from_json(json_data['plasma_beam_icon_configurations']),
            charge_gauge=TweakTargeting_Charge_Gauge.from_json(json_data['charge_gauge']),
            lock_fire=TweakTargeting_LockFire.from_json(json_data['lock_fire']),
            lock_dagger=TweakTargeting_LockDagger.from_json(json_data['lock_dagger']),
            scan=TweakTargeting_Scan.from_json(json_data['scan']),
            unknown_0xc3410560=json_data['unknown_0xc3410560'],
            orbit_lock_on_acquire_target_interpolation_time=json_data['orbit_lock_on_acquire_target_interpolation_time'],
            orbit_lock_on_lose_target_interpolation_time=json_data['orbit_lock_on_lose_target_interpolation_time'],
            orbit_lock_on_switch_target_interpolation_time=json_data['orbit_lock_on_switch_target_interpolation_time'],
            lock_on_confirm_reticle_scale=json_data['lock_on_confirm_reticle_scale'],
            seeker_acquire_target_interpolation_time=json_data['seeker_acquire_target_interpolation_time'],
            seeker_lose_target_interpolation_time=json_data['seeker_lose_target_interpolation_time'],
            seeker_switch_target_interpolation_time=json_data['seeker_switch_target_interpolation_time'],
            seeker_target_reticle_scale=json_data['seeker_target_reticle_scale'],
            seeker_z_rotation_rate=json_data['seeker_z_rotation_rate'],
            unknown_0xdcbd7bf8=json_data['unknown_0xdcbd7bf8'],
            orbit_point_primary_color_red=json_data['orbit_point_primary_color_red'],
            orbit_point_primary_color_green=json_data['orbit_point_primary_color_green'],
            orbit_point_primary_color_blue=json_data['orbit_point_primary_color_blue'],
            orbit_point_secondary_color_red=json_data['orbit_point_secondary_color_red'],
            orbit_point_secondary_color_green=json_data['orbit_point_secondary_color_green'],
            orbit_point_secondary_color_blue=json_data['orbit_point_secondary_color_blue'],
            orbit_point_occluded_opacity=json_data['orbit_point_occluded_opacity'],
            orbit_point_non_occluded_opacity=json_data['orbit_point_non_occluded_opacity'],
            orbit_point_z_offset=json_data['orbit_point_z_offset'],
            orbit_point_interpolate_in_time=json_data['orbit_point_interpolate_in_time'],
            orbit_point_interpolate_out_time=json_data['orbit_point_interpolate_out_time'],
            orbit_point_color_animate_period=json_data['orbit_point_color_animate_period'],
            jump_target_possible_primary_color_red=json_data['jump_target_possible_primary_color_red'],
            jump_target_possible_primary_color_green=json_data['jump_target_possible_primary_color_green'],
            jump_target_possible_primary_color_blue=json_data['jump_target_possible_primary_color_blue'],
            jump_target_possible_secondary_color_red=json_data['jump_target_possible_secondary_color_red'],
            jump_target_possible_secondary_color_green=json_data['jump_target_possible_secondary_color_green'],
            jump_target_possible_secondary_color_blue=json_data['jump_target_possible_secondary_color_blue'],
            jump_target_impossible_primary_color_red=json_data['jump_target_impossible_primary_color_red'],
            jump_target_impossible_primary_color_green=json_data['jump_target_impossible_primary_color_green'],
            jump_target_impossible_primary_color_blue=json_data['jump_target_impossible_primary_color_blue'],
            jump_target_impossible_secondary_color_red=json_data['jump_target_impossible_secondary_color_red'],
            jump_target_impossible_secondary_color_green=json_data['jump_target_impossible_secondary_color_green'],
            jump_target_impossible_secondary_color_blue=json_data['jump_target_impossible_secondary_color_blue'],
            jump_target_occluded_opacity=json_data['jump_target_occluded_opacity'],
            jump_target_non_occluded_opacity=json_data['jump_target_non_occluded_opacity'],
            jump_target_height=json_data['jump_target_height'],
            jump_target_interpolate_in_time=json_data['jump_target_interpolate_in_time'],
            jump_target_interpolate_out_time=json_data['jump_target_interpolate_out_time'],
            jump_target_color_animate_period=json_data['jump_target_color_animate_period'],
            jump_target_z_rotate_speed=json_data['jump_target_z_rotate_speed'],
            orbit_point_z_rotate_speed=json_data['orbit_point_z_rotate_speed'],
            unknown_0x42420f6e=Color.from_json(json_data['unknown_0x42420f6e']),
            flower_reticle_scale=json_data['flower_reticle_scale'],
            flower_reticle_color=Color.from_json(json_data['flower_reticle_color']),
            missile_bracket_open_holster_time=json_data['missile_bracket_open_holster_time'],
            unknown_0x4c73a43d=json_data['unknown_0x4c73a43d'],
            unknown_0x6543d31b=json_data['unknown_0x6543d31b'],
            missile_bracket_missile_fire_anim_time=json_data['missile_bracket_missile_fire_anim_time'],
            missile_bracket_color=Color.from_json(json_data['missile_bracket_color']),
            inner_beam_icon_open_time=json_data['inner_beam_icon_open_time'],
            inner_beam_icon_scale=json_data['inner_beam_icon_scale'],
            inner_beam_icon_color_power_beam=Color.from_json(json_data['inner_beam_icon_color_power_beam']),
            inner_beam_icon_color_ice_beam=Color.from_json(json_data['inner_beam_icon_color_ice_beam']),
            inner_beam_icon_color_wave_beam=Color.from_json(json_data['inner_beam_icon_color_wave_beam']),
            inner_beam_icon_color_plasma_beam=Color.from_json(json_data['inner_beam_icon_color_plasma_beam']),
            lock_on_confirm_reticle_color=Color.from_json(json_data['lock_on_confirm_reticle_color']),
            seeker_reticle_color=Color.from_json(json_data['seeker_reticle_color']),
            lock_on_confirm_min_radius_viewport=json_data['lock_on_confirm_min_radius_viewport'],
            lock_on_confirm_max_radius_viewport=json_data['lock_on_confirm_max_radius_viewport'],
            flower_min_radius_viewport=json_data['flower_min_radius_viewport'],
            flower_max_radius_viewport=json_data['flower_max_radius_viewport'],
            seeker_min_radius_viewport=json_data['seeker_min_radius_viewport'],
            seeker_max_radius_viewport=json_data['seeker_max_radius_viewport'],
            missile_bracket_min_radius_viewport=json_data['missile_bracket_min_radius_viewport'],
            missile_bracket_max_radius_viewport=json_data['missile_bracket_max_radius_viewport'],
            inner_icon_min_radius_viewport=json_data['inner_icon_min_radius_viewport'],
            inner_icon_max_radius_viewport=json_data['inner_icon_max_radius_viewport'],
            outer_icon_min_radius_viewport=json_data['outer_icon_min_radius_viewport'],
            outer_icon_max_radius_viewport=json_data['outer_icon_max_radius_viewport'],
            lock_fire_min_radius_viewport=json_data['lock_fire_min_radius_viewport'],
            lock_fire_max_radius_viewport=json_data['lock_fire_max_radius_viewport'],
            lock_dagger_min_radius_viewport=json_data['lock_dagger_min_radius_viewport'],
            lock_dagger_max_radius_viewport=json_data['lock_dagger_max_radius_viewport'],
            grapple_icon_scale=json_data['grapple_icon_scale'],
            grapple_icon_scale_inactive=json_data['grapple_icon_scale_inactive'],
            grapple_icon_min_radius_viewport=json_data['grapple_icon_min_radius_viewport'],
            grapple_icon_max_radius_viewport=json_data['grapple_icon_max_radius_viewport'],
            grapple_icon_color=Color.from_json(json_data['grapple_icon_color']),
            grapple_icon_color_inactive=Color.from_json(json_data['grapple_icon_color_inactive']),
            grapple_icon_color_inactive_out_of_range=Color.from_json(json_data['grapple_icon_color_inactive_out_of_range']),
            unknown_0x083b1cc8=Color.from_json(json_data['unknown_0x083b1cc8']),
            unknown_0x966982b1=json_data['unknown_0x966982b1'],
            grapple_max_visible_distance=json_data['grapple_max_visible_distance'],
            charge_gauge_glow_color=Color.from_json(json_data['charge_gauge_glow_color']),
            charge_gauge_glow_time=json_data['charge_gauge_glow_time'],
            orbit_point_model_color=Color.from_json(json_data['orbit_point_model_color']),
            crosshairs_color=Color.from_json(json_data['crosshairs_color']),
            crosshairs_fade_in_out_time=json_data['crosshairs_fade_in_out_time'],
            is_draw_orbit_point_default=json_data['is_draw_orbit_point_default'],
            charge_gauge_glow_color_b=Color.from_json(json_data['charge_gauge_glow_color_b']),
            charge_gauge_flash_cycle_time=json_data['charge_gauge_flash_cycle_time'],
            x_ray_seeker_min_radius_viewport=json_data['x_ray_seeker_min_radius_viewport'],
            x_ray_seeker_max_radius_viewport=json_data['x_ray_seeker_max_radius_viewport'],
            x_ray_seeker_reticle_color=Color.from_json(json_data['x_ray_seeker_reticle_color']),
            x_ray_seeker_target_reticle_scale=json_data['x_ray_seeker_target_reticle_scale'],
            unknown_0xcbac6d52=json_data['unknown_0xcbac6d52'],
            unknown_0x980a75b6=json_data['unknown_0x980a75b6'],
            unknown_0xcd1e0e91=json_data['unknown_0xcd1e0e91'],
            unknown_0xa3e32481=json_data['unknown_0xa3e32481'],
            aiming_cursor_clamp_color=Color.from_json(json_data['aiming_cursor_clamp_color']),
            aiming_cursor_clamp_secondary_color=Color.from_json(json_data['aiming_cursor_clamp_secondary_color']),
            aiming_cursor_clamp_offset=json_data['aiming_cursor_clamp_offset'],
            aiming_cursor_clamp_time=json_data['aiming_cursor_clamp_time'],
            aiming_cursor_center_ring_color=Color.from_json(json_data['aiming_cursor_center_ring_color']),
            aiming_cursor_center_ring_outline_color=Color.from_json(json_data['aiming_cursor_center_ring_outline_color']),
            aiming_cursor_center_ring_secondary_color=Color.from_json(json_data['aiming_cursor_center_ring_secondary_color']),
            aiming_cursor_center_ring_outline_secondary_color=Color.from_json(json_data['aiming_cursor_center_ring_outline_secondary_color']),
            aiming_cursor_center_ring_color_transition_time=json_data['aiming_cursor_center_ring_color_transition_time'],
            aiming_cursor_radius=json_data['aiming_cursor_radius'],
            aiming_cursor_depth_ring_color=Color.from_json(json_data['aiming_cursor_depth_ring_color']),
            aiming_cursor_depth_ring_outline_color=Color.from_json(json_data['aiming_cursor_depth_ring_outline_color']),
            aiming_cursor_depth_ring_secondary_color=Color.from_json(json_data['aiming_cursor_depth_ring_secondary_color']),
            aiming_cursor_depth_ring_outline_secondary_color=Color.from_json(json_data['aiming_cursor_depth_ring_outline_secondary_color']),
            aiming_cursor_depth_ring_min_size=json_data['aiming_cursor_depth_ring_min_size'],
            aiming_cursor_depth_ring_max_size=json_data['aiming_cursor_depth_ring_max_size'],
            x_ray_aiming_cursor_color=Color.from_json(json_data['x_ray_aiming_cursor_color']),
            x_ray_depth_cursor_color=Color.from_json(json_data['x_ray_depth_cursor_color']),
            x_ray_depth_cursor_min_size=json_data['x_ray_depth_cursor_min_size'],
            x_ray_depth_cursor_max_size=json_data['x_ray_depth_cursor_max_size'],
            unknown_0xc29882b7=Color.from_json(json_data['unknown_0xc29882b7']),
            unknown_0xd33fcc91=Color.from_json(json_data['unknown_0xd33fcc91']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'instance_name': self.instance_name,
            'combat_reticules': self.combat_reticules.to_json(),
            'charge_beam': self.charge_beam.to_json(),
            'orbit_lock': self.orbit_lock.to_json(),
            'tweak_targeting_outer_beam_icon': self.tweak_targeting_outer_beam_icon.to_json(),
            'power_beam_icon_configurations': self.power_beam_icon_configurations.to_json(),
            'ice_beam_icon_configurations': self.ice_beam_icon_configurations.to_json(),
            'wave_beam_icon_configurations': self.wave_beam_icon_configurations.to_json(),
            'plasma_beam_icon_configurations': self.plasma_beam_icon_configurations.to_json(),
            'charge_gauge': self.charge_gauge.to_json(),
            'lock_fire': self.lock_fire.to_json(),
            'lock_dagger': self.lock_dagger.to_json(),
            'scan': self.scan.to_json(),
            'unknown_0xc3410560': self.unknown_0xc3410560,
            'orbit_lock_on_acquire_target_interpolation_time': self.orbit_lock_on_acquire_target_interpolation_time,
            'orbit_lock_on_lose_target_interpolation_time': self.orbit_lock_on_lose_target_interpolation_time,
            'orbit_lock_on_switch_target_interpolation_time': self.orbit_lock_on_switch_target_interpolation_time,
            'lock_on_confirm_reticle_scale': self.lock_on_confirm_reticle_scale,
            'seeker_acquire_target_interpolation_time': self.seeker_acquire_target_interpolation_time,
            'seeker_lose_target_interpolation_time': self.seeker_lose_target_interpolation_time,
            'seeker_switch_target_interpolation_time': self.seeker_switch_target_interpolation_time,
            'seeker_target_reticle_scale': self.seeker_target_reticle_scale,
            'seeker_z_rotation_rate': self.seeker_z_rotation_rate,
            'unknown_0xdcbd7bf8': self.unknown_0xdcbd7bf8,
            'orbit_point_primary_color_red': self.orbit_point_primary_color_red,
            'orbit_point_primary_color_green': self.orbit_point_primary_color_green,
            'orbit_point_primary_color_blue': self.orbit_point_primary_color_blue,
            'orbit_point_secondary_color_red': self.orbit_point_secondary_color_red,
            'orbit_point_secondary_color_green': self.orbit_point_secondary_color_green,
            'orbit_point_secondary_color_blue': self.orbit_point_secondary_color_blue,
            'orbit_point_occluded_opacity': self.orbit_point_occluded_opacity,
            'orbit_point_non_occluded_opacity': self.orbit_point_non_occluded_opacity,
            'orbit_point_z_offset': self.orbit_point_z_offset,
            'orbit_point_interpolate_in_time': self.orbit_point_interpolate_in_time,
            'orbit_point_interpolate_out_time': self.orbit_point_interpolate_out_time,
            'orbit_point_color_animate_period': self.orbit_point_color_animate_period,
            'jump_target_possible_primary_color_red': self.jump_target_possible_primary_color_red,
            'jump_target_possible_primary_color_green': self.jump_target_possible_primary_color_green,
            'jump_target_possible_primary_color_blue': self.jump_target_possible_primary_color_blue,
            'jump_target_possible_secondary_color_red': self.jump_target_possible_secondary_color_red,
            'jump_target_possible_secondary_color_green': self.jump_target_possible_secondary_color_green,
            'jump_target_possible_secondary_color_blue': self.jump_target_possible_secondary_color_blue,
            'jump_target_impossible_primary_color_red': self.jump_target_impossible_primary_color_red,
            'jump_target_impossible_primary_color_green': self.jump_target_impossible_primary_color_green,
            'jump_target_impossible_primary_color_blue': self.jump_target_impossible_primary_color_blue,
            'jump_target_impossible_secondary_color_red': self.jump_target_impossible_secondary_color_red,
            'jump_target_impossible_secondary_color_green': self.jump_target_impossible_secondary_color_green,
            'jump_target_impossible_secondary_color_blue': self.jump_target_impossible_secondary_color_blue,
            'jump_target_occluded_opacity': self.jump_target_occluded_opacity,
            'jump_target_non_occluded_opacity': self.jump_target_non_occluded_opacity,
            'jump_target_height': self.jump_target_height,
            'jump_target_interpolate_in_time': self.jump_target_interpolate_in_time,
            'jump_target_interpolate_out_time': self.jump_target_interpolate_out_time,
            'jump_target_color_animate_period': self.jump_target_color_animate_period,
            'jump_target_z_rotate_speed': self.jump_target_z_rotate_speed,
            'orbit_point_z_rotate_speed': self.orbit_point_z_rotate_speed,
            'unknown_0x42420f6e': self.unknown_0x42420f6e.to_json(),
            'flower_reticle_scale': self.flower_reticle_scale,
            'flower_reticle_color': self.flower_reticle_color.to_json(),
            'missile_bracket_open_holster_time': self.missile_bracket_open_holster_time,
            'unknown_0x4c73a43d': self.unknown_0x4c73a43d,
            'unknown_0x6543d31b': self.unknown_0x6543d31b,
            'missile_bracket_missile_fire_anim_time': self.missile_bracket_missile_fire_anim_time,
            'missile_bracket_color': self.missile_bracket_color.to_json(),
            'inner_beam_icon_open_time': self.inner_beam_icon_open_time,
            'inner_beam_icon_scale': self.inner_beam_icon_scale,
            'inner_beam_icon_color_power_beam': self.inner_beam_icon_color_power_beam.to_json(),
            'inner_beam_icon_color_ice_beam': self.inner_beam_icon_color_ice_beam.to_json(),
            'inner_beam_icon_color_wave_beam': self.inner_beam_icon_color_wave_beam.to_json(),
            'inner_beam_icon_color_plasma_beam': self.inner_beam_icon_color_plasma_beam.to_json(),
            'lock_on_confirm_reticle_color': self.lock_on_confirm_reticle_color.to_json(),
            'seeker_reticle_color': self.seeker_reticle_color.to_json(),
            'lock_on_confirm_min_radius_viewport': self.lock_on_confirm_min_radius_viewport,
            'lock_on_confirm_max_radius_viewport': self.lock_on_confirm_max_radius_viewport,
            'flower_min_radius_viewport': self.flower_min_radius_viewport,
            'flower_max_radius_viewport': self.flower_max_radius_viewport,
            'seeker_min_radius_viewport': self.seeker_min_radius_viewport,
            'seeker_max_radius_viewport': self.seeker_max_radius_viewport,
            'missile_bracket_min_radius_viewport': self.missile_bracket_min_radius_viewport,
            'missile_bracket_max_radius_viewport': self.missile_bracket_max_radius_viewport,
            'inner_icon_min_radius_viewport': self.inner_icon_min_radius_viewport,
            'inner_icon_max_radius_viewport': self.inner_icon_max_radius_viewport,
            'outer_icon_min_radius_viewport': self.outer_icon_min_radius_viewport,
            'outer_icon_max_radius_viewport': self.outer_icon_max_radius_viewport,
            'lock_fire_min_radius_viewport': self.lock_fire_min_radius_viewport,
            'lock_fire_max_radius_viewport': self.lock_fire_max_radius_viewport,
            'lock_dagger_min_radius_viewport': self.lock_dagger_min_radius_viewport,
            'lock_dagger_max_radius_viewport': self.lock_dagger_max_radius_viewport,
            'grapple_icon_scale': self.grapple_icon_scale,
            'grapple_icon_scale_inactive': self.grapple_icon_scale_inactive,
            'grapple_icon_min_radius_viewport': self.grapple_icon_min_radius_viewport,
            'grapple_icon_max_radius_viewport': self.grapple_icon_max_radius_viewport,
            'grapple_icon_color': self.grapple_icon_color.to_json(),
            'grapple_icon_color_inactive': self.grapple_icon_color_inactive.to_json(),
            'grapple_icon_color_inactive_out_of_range': self.grapple_icon_color_inactive_out_of_range.to_json(),
            'unknown_0x083b1cc8': self.unknown_0x083b1cc8.to_json(),
            'unknown_0x966982b1': self.unknown_0x966982b1,
            'grapple_max_visible_distance': self.grapple_max_visible_distance,
            'charge_gauge_glow_color': self.charge_gauge_glow_color.to_json(),
            'charge_gauge_glow_time': self.charge_gauge_glow_time,
            'orbit_point_model_color': self.orbit_point_model_color.to_json(),
            'crosshairs_color': self.crosshairs_color.to_json(),
            'crosshairs_fade_in_out_time': self.crosshairs_fade_in_out_time,
            'is_draw_orbit_point_default': self.is_draw_orbit_point_default,
            'charge_gauge_glow_color_b': self.charge_gauge_glow_color_b.to_json(),
            'charge_gauge_flash_cycle_time': self.charge_gauge_flash_cycle_time,
            'x_ray_seeker_min_radius_viewport': self.x_ray_seeker_min_radius_viewport,
            'x_ray_seeker_max_radius_viewport': self.x_ray_seeker_max_radius_viewport,
            'x_ray_seeker_reticle_color': self.x_ray_seeker_reticle_color.to_json(),
            'x_ray_seeker_target_reticle_scale': self.x_ray_seeker_target_reticle_scale,
            'unknown_0xcbac6d52': self.unknown_0xcbac6d52,
            'unknown_0x980a75b6': self.unknown_0x980a75b6,
            'unknown_0xcd1e0e91': self.unknown_0xcd1e0e91,
            'unknown_0xa3e32481': self.unknown_0xa3e32481,
            'aiming_cursor_clamp_color': self.aiming_cursor_clamp_color.to_json(),
            'aiming_cursor_clamp_secondary_color': self.aiming_cursor_clamp_secondary_color.to_json(),
            'aiming_cursor_clamp_offset': self.aiming_cursor_clamp_offset,
            'aiming_cursor_clamp_time': self.aiming_cursor_clamp_time,
            'aiming_cursor_center_ring_color': self.aiming_cursor_center_ring_color.to_json(),
            'aiming_cursor_center_ring_outline_color': self.aiming_cursor_center_ring_outline_color.to_json(),
            'aiming_cursor_center_ring_secondary_color': self.aiming_cursor_center_ring_secondary_color.to_json(),
            'aiming_cursor_center_ring_outline_secondary_color': self.aiming_cursor_center_ring_outline_secondary_color.to_json(),
            'aiming_cursor_center_ring_color_transition_time': self.aiming_cursor_center_ring_color_transition_time,
            'aiming_cursor_radius': self.aiming_cursor_radius,
            'aiming_cursor_depth_ring_color': self.aiming_cursor_depth_ring_color.to_json(),
            'aiming_cursor_depth_ring_outline_color': self.aiming_cursor_depth_ring_outline_color.to_json(),
            'aiming_cursor_depth_ring_secondary_color': self.aiming_cursor_depth_ring_secondary_color.to_json(),
            'aiming_cursor_depth_ring_outline_secondary_color': self.aiming_cursor_depth_ring_outline_secondary_color.to_json(),
            'aiming_cursor_depth_ring_min_size': self.aiming_cursor_depth_ring_min_size,
            'aiming_cursor_depth_ring_max_size': self.aiming_cursor_depth_ring_max_size,
            'x_ray_aiming_cursor_color': self.x_ray_aiming_cursor_color.to_json(),
            'x_ray_depth_cursor_color': self.x_ray_depth_cursor_color.to_json(),
            'x_ray_depth_cursor_min_size': self.x_ray_depth_cursor_min_size,
            'x_ray_depth_cursor_max_size': self.x_ray_depth_cursor_max_size,
            'unknown_0xc29882b7': self.unknown_0xc29882b7.to_json(),
            'unknown_0xd33fcc91': self.unknown_0xd33fcc91.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_instance_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_combat_reticules(data: typing.BinaryIO, game: Game, property_size: int) -> TweakTargeting_CombatReticules:
    return TweakTargeting_CombatReticules.from_stream(data, game, property_size)


def _decode_charge_beam(data: typing.BinaryIO, game: Game, property_size: int) -> TweakTargeting_ChargeBeam:
    return TweakTargeting_ChargeBeam.from_stream(data, game, property_size)


def _decode_orbit_lock(data: typing.BinaryIO, game: Game, property_size: int) -> TweakTargeting_OrbitLock:
    return TweakTargeting_OrbitLock.from_stream(data, game, property_size)


def _decode_tweak_targeting_outer_beam_icon(data: typing.BinaryIO, game: Game, property_size: int) -> TweakTargeting_OuterBeamIcon:
    return TweakTargeting_OuterBeamIcon.from_stream(data, game, property_size)


def _decode_power_beam_icon_configurations(data: typing.BinaryIO, game: Game, property_size: int) -> TIcon_Configurations:
    return TIcon_Configurations.from_stream(data, game, property_size)


def _decode_ice_beam_icon_configurations(data: typing.BinaryIO, game: Game, property_size: int) -> TIcon_Configurations:
    return TIcon_Configurations.from_stream(data, game, property_size, default_override={'something0_angle': 90.0, 'something1_angle': 90.0, 'something2_angle': 90.0, 'something3_angle': 90.0, 'something4_angle': 90.0, 'something5_angle': 90.0, 'something6_angle': 90.0, 'something7_angle': 90.0, 'something8_angle': 90.0})


def _decode_wave_beam_icon_configurations(data: typing.BinaryIO, game: Game, property_size: int) -> TIcon_Configurations:
    return TIcon_Configurations.from_stream(data, game, property_size, default_override={'something0_angle': 150.0, 'something1_angle': 150.0, 'something2_angle': 150.0, 'something3_angle': 150.0, 'something4_angle': 150.0, 'something5_angle': 150.0, 'something6_angle': 150.0, 'something7_angle': 150.0, 'something8_angle': 150.0})


def _decode_plasma_beam_icon_configurations(data: typing.BinaryIO, game: Game, property_size: int) -> TIcon_Configurations:
    return TIcon_Configurations.from_stream(data, game, property_size, default_override={'something0_angle': 210.0, 'something1_angle': 210.0, 'something2_angle': 210.0, 'something3_angle': 210.0, 'something4_angle': 210.0, 'something5_angle': 210.0, 'something6_angle': 210.0, 'something7_angle': 210.0, 'something8_angle': 210.0})


def _decode_charge_gauge(data: typing.BinaryIO, game: Game, property_size: int) -> TweakTargeting_Charge_Gauge:
    return TweakTargeting_Charge_Gauge.from_stream(data, game, property_size)


def _decode_lock_fire(data: typing.BinaryIO, game: Game, property_size: int) -> TweakTargeting_LockFire:
    return TweakTargeting_LockFire.from_stream(data, game, property_size)


def _decode_lock_dagger(data: typing.BinaryIO, game: Game, property_size: int) -> TweakTargeting_LockDagger:
    return TweakTargeting_LockDagger.from_stream(data, game, property_size)


def _decode_scan(data: typing.BinaryIO, game: Game, property_size: int) -> TweakTargeting_Scan:
    return TweakTargeting_Scan.from_stream(data, game, property_size)


def _decode_unknown_0x42420f6e(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_flower_reticle_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missile_bracket_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_inner_beam_icon_color_power_beam(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_inner_beam_icon_color_ice_beam(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_inner_beam_icon_color_wave_beam(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_inner_beam_icon_color_plasma_beam(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_lock_on_confirm_reticle_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_seeker_reticle_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_grapple_icon_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_grapple_icon_color_inactive(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_grapple_icon_color_inactive_out_of_range(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x083b1cc8(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_charge_gauge_glow_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_orbit_point_model_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_crosshairs_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_charge_gauge_glow_color_b(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_seeker_reticle_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_aiming_cursor_clamp_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_aiming_cursor_clamp_secondary_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_aiming_cursor_center_ring_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_aiming_cursor_center_ring_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_aiming_cursor_center_ring_secondary_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_aiming_cursor_center_ring_outline_secondary_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_aiming_cursor_depth_ring_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_aiming_cursor_depth_ring_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_aiming_cursor_depth_ring_secondary_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_aiming_cursor_depth_ring_outline_secondary_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_aiming_cursor_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_depth_cursor_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xc29882b7(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xd33fcc91(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x7fda1466: ('instance_name', _decode_instance_name),
    0xd15b6a54: ('combat_reticules', _decode_combat_reticules),
    0xe87e2134: ('charge_beam', _decode_charge_beam),
    0xc6915d69: ('orbit_lock', _decode_orbit_lock),
    0x5173932f: ('tweak_targeting_outer_beam_icon', _decode_tweak_targeting_outer_beam_icon),
    0x23ff4be4: ('power_beam_icon_configurations', _decode_power_beam_icon_configurations),
    0x92e98613: ('ice_beam_icon_configurations', _decode_ice_beam_icon_configurations),
    0x64833842: ('wave_beam_icon_configurations', _decode_wave_beam_icon_configurations),
    0x8dfd6e3c: ('plasma_beam_icon_configurations', _decode_plasma_beam_icon_configurations),
    0xbc5a41b2: ('charge_gauge', _decode_charge_gauge),
    0x00183589: ('lock_fire', _decode_lock_fire),
    0xd20ecc07: ('lock_dagger', _decode_lock_dagger),
    0x65ef9f2a: ('scan', _decode_scan),
    0xc3410560: ('unknown_0xc3410560', structs.decode_BIG_l),
    0x3eb13041: ('orbit_lock_on_acquire_target_interpolation_time', structs.decode_BIG_f),
    0x5e67cab0: ('orbit_lock_on_lose_target_interpolation_time', structs.decode_BIG_f),
    0xe0ca98ac: ('orbit_lock_on_switch_target_interpolation_time', structs.decode_BIG_f),
    0xc1e35abb: ('lock_on_confirm_reticle_scale', structs.decode_BIG_f),
    0x9f8d62c1: ('seeker_acquire_target_interpolation_time', structs.decode_BIG_f),
    0xff5eeeb9: ('seeker_lose_target_interpolation_time', structs.decode_BIG_f),
    0x0d0b660d: ('seeker_switch_target_interpolation_time', structs.decode_BIG_f),
    0x132dd09e: ('seeker_target_reticle_scale', structs.decode_BIG_f),
    0x03efc783: ('seeker_z_rotation_rate', structs.decode_BIG_f),
    0xdcbd7bf8: ('unknown_0xdcbd7bf8', structs.decode_BIG_f),
    0x2acd6b4b: ('orbit_point_primary_color_red', structs.decode_BIG_f),
    0xb4c6c331: ('orbit_point_primary_color_green', structs.decode_BIG_f),
    0x27d02089: ('orbit_point_primary_color_blue', structs.decode_BIG_f),
    0xae89310e: ('orbit_point_secondary_color_red', structs.decode_BIG_f),
    0xb27644df: ('orbit_point_secondary_color_green', structs.decode_BIG_f),
    0x21e2d1cc: ('orbit_point_secondary_color_blue', structs.decode_BIG_f),
    0x8e3afef8: ('orbit_point_occluded_opacity', structs.decode_BIG_f),
    0x5c489cb5: ('orbit_point_non_occluded_opacity', structs.decode_BIG_f),
    0xef2c842e: ('orbit_point_z_offset', structs.decode_BIG_f),
    0x61a6a38e: ('orbit_point_interpolate_in_time', structs.decode_BIG_f),
    0xfbdf31f9: ('orbit_point_interpolate_out_time', structs.decode_BIG_f),
    0xf76f7d0b: ('orbit_point_color_animate_period', structs.decode_BIG_f),
    0x810b3a08: ('jump_target_possible_primary_color_red', structs.decode_BIG_f),
    0x73fe1553: ('jump_target_possible_primary_color_green', structs.decode_BIG_f),
    0xc8aef6f2: ('jump_target_possible_primary_color_blue', structs.decode_BIG_f),
    0x69b1e76c: ('jump_target_possible_secondary_color_red', structs.decode_BIG_f),
    0x8a0dfd23: ('jump_target_possible_secondary_color_green', structs.decode_BIG_f),
    0x8299e96e: ('jump_target_possible_secondary_color_blue', structs.decode_BIG_f),
    0xa18a3f25: ('jump_target_impossible_primary_color_red', structs.decode_BIG_f),
    0x23be9bb2: ('jump_target_impossible_primary_color_green', structs.decode_BIG_f),
    0x8d512b82: ('jump_target_impossible_primary_color_blue', structs.decode_BIG_f),
    0x39f1698d: ('jump_target_impossible_secondary_color_red', structs.decode_BIG_f),
    0xc768c1e9: ('jump_target_impossible_secondary_color_green', structs.decode_BIG_f),
    0x55c47b0e: ('jump_target_impossible_secondary_color_blue', structs.decode_BIG_f),
    0xa009aea2: ('jump_target_occluded_opacity', structs.decode_BIG_f),
    0x38080bbf: ('jump_target_non_occluded_opacity', structs.decode_BIG_f),
    0x71017dbe: ('jump_target_height', structs.decode_BIG_f),
    0x4a996997: ('jump_target_interpolate_in_time', structs.decode_BIG_f),
    0x9f9fa6f3: ('jump_target_interpolate_out_time', structs.decode_BIG_f),
    0x932fea01: ('jump_target_color_animate_period', structs.decode_BIG_f),
    0x165f0fa8: ('jump_target_z_rotate_speed', structs.decode_BIG_f),
    0x6bd6b11f: ('orbit_point_z_rotate_speed', structs.decode_BIG_f),
    0x42420f6e: ('unknown_0x42420f6e', _decode_unknown_0x42420f6e),
    0xa63229f1: ('flower_reticle_scale', structs.decode_BIG_f),
    0xbda45f1a: ('flower_reticle_color', _decode_flower_reticle_color),
    0xb090e147: ('missile_bracket_open_holster_time', structs.decode_BIG_f),
    0x4c73a43d: ('unknown_0x4c73a43d', structs.decode_BIG_f),
    0x6543d31b: ('unknown_0x6543d31b', structs.decode_BIG_f),
    0x8cd2d1ce: ('missile_bracket_missile_fire_anim_time', structs.decode_BIG_f),
    0xe42f6be0: ('missile_bracket_color', _decode_missile_bracket_color),
    0x45910e5d: ('inner_beam_icon_open_time', structs.decode_BIG_f),
    0x07b30fa0: ('inner_beam_icon_scale', structs.decode_BIG_f),
    0x13ce8500: ('inner_beam_icon_color_power_beam', _decode_inner_beam_icon_color_power_beam),
    0x9829f256: ('inner_beam_icon_color_ice_beam', _decode_inner_beam_icon_color_ice_beam),
    0x77a613b9: ('inner_beam_icon_color_wave_beam', _decode_inner_beam_icon_color_wave_beam),
    0xdfa81287: ('inner_beam_icon_color_plasma_beam', _decode_inner_beam_icon_color_plasma_beam),
    0xda752c50: ('lock_on_confirm_reticle_color', _decode_lock_on_confirm_reticle_color),
    0x7b544e14: ('seeker_reticle_color', _decode_seeker_reticle_color),
    0x618d150a: ('lock_on_confirm_min_radius_viewport', structs.decode_BIG_f),
    0x209a2a8c: ('lock_on_confirm_max_radius_viewport', structs.decode_BIG_f),
    0xacb3f8f7: ('flower_min_radius_viewport', structs.decode_BIG_f),
    0xeda4c771: ('flower_max_radius_viewport', structs.decode_BIG_f),
    0xd3427574: ('seeker_min_radius_viewport', structs.decode_BIG_f),
    0x92554af2: ('seeker_max_radius_viewport', structs.decode_BIG_f),
    0x1e134e75: ('missile_bracket_min_radius_viewport', structs.decode_BIG_f),
    0x5f0471f3: ('missile_bracket_max_radius_viewport', structs.decode_BIG_f),
    0xe90548ac: ('inner_icon_min_radius_viewport', structs.decode_BIG_f),
    0xa812772a: ('inner_icon_max_radius_viewport', structs.decode_BIG_f),
    0x2d75c7be: ('outer_icon_min_radius_viewport', structs.decode_BIG_f),
    0x6c62f838: ('outer_icon_max_radius_viewport', structs.decode_BIG_f),
    0xf98e6242: ('lock_fire_min_radius_viewport', structs.decode_BIG_f),
    0xb8995dc4: ('lock_fire_max_radius_viewport', structs.decode_BIG_f),
    0x5009c614: ('lock_dagger_min_radius_viewport', structs.decode_BIG_f),
    0x111ef992: ('lock_dagger_max_radius_viewport', structs.decode_BIG_f),
    0xec0ff888: ('grapple_icon_scale', structs.decode_BIG_f),
    0xf229e05e: ('grapple_icon_scale_inactive', structs.decode_BIG_f),
    0x498d794a: ('grapple_icon_min_radius_viewport', structs.decode_BIG_f),
    0x089a46cc: ('grapple_icon_max_radius_viewport', structs.decode_BIG_f),
    0xf7998e63: ('grapple_icon_color', _decode_grapple_icon_color),
    0x3ce853e3: ('grapple_icon_color_inactive', _decode_grapple_icon_color_inactive),
    0xf593614f: ('grapple_icon_color_inactive_out_of_range', _decode_grapple_icon_color_inactive_out_of_range),
    0x083b1cc8: ('unknown_0x083b1cc8', _decode_unknown_0x083b1cc8),
    0x966982b1: ('unknown_0x966982b1', structs.decode_BIG_f),
    0x34915075: ('grapple_max_visible_distance', structs.decode_BIG_f),
    0xf9799f5f: ('charge_gauge_glow_color', _decode_charge_gauge_glow_color),
    0x9b980788: ('charge_gauge_glow_time', structs.decode_BIG_f),
    0x3523a47f: ('orbit_point_model_color', _decode_orbit_point_model_color),
    0x27358b4d: ('crosshairs_color', _decode_crosshairs_color),
    0x2ff52290: ('crosshairs_fade_in_out_time', structs.decode_BIG_f),
    0x8a548cc9: ('is_draw_orbit_point_default', structs.decode_BIG_bool_),
    0x65d449e1: ('charge_gauge_glow_color_b', _decode_charge_gauge_glow_color_b),
    0x42c7fbe4: ('charge_gauge_flash_cycle_time', structs.decode_BIG_f),
    0x13820c03: ('x_ray_seeker_min_radius_viewport', structs.decode_BIG_f),
    0x52953385: ('x_ray_seeker_max_radius_viewport', structs.decode_BIG_f),
    0x0cd8fe5d: ('x_ray_seeker_reticle_color', _decode_x_ray_seeker_reticle_color),
    0xdd8cf478: ('x_ray_seeker_target_reticle_scale', structs.decode_BIG_f),
    0xcbac6d52: ('unknown_0xcbac6d52', structs.decode_BIG_f),
    0x980a75b6: ('unknown_0x980a75b6', structs.decode_BIG_f),
    0xcd1e0e91: ('unknown_0xcd1e0e91', structs.decode_BIG_f),
    0xa3e32481: ('unknown_0xa3e32481', structs.decode_BIG_f),
    0x8bfd0783: ('aiming_cursor_clamp_color', _decode_aiming_cursor_clamp_color),
    0xca3a8d19: ('aiming_cursor_clamp_secondary_color', _decode_aiming_cursor_clamp_secondary_color),
    0xbc9e3bf9: ('aiming_cursor_clamp_offset', structs.decode_BIG_f),
    0x18675e4e: ('aiming_cursor_clamp_time', structs.decode_BIG_f),
    0x9db1ddb6: ('aiming_cursor_center_ring_color', _decode_aiming_cursor_center_ring_color),
    0x45b717df: ('aiming_cursor_center_ring_outline_color', _decode_aiming_cursor_center_ring_outline_color),
    0x6f659cdb: ('aiming_cursor_center_ring_secondary_color', _decode_aiming_cursor_center_ring_secondary_color),
    0xe97e5ba3: ('aiming_cursor_center_ring_outline_secondary_color', _decode_aiming_cursor_center_ring_outline_secondary_color),
    0xfec02688: ('aiming_cursor_center_ring_color_transition_time', structs.decode_BIG_f),
    0x84709ab2: ('aiming_cursor_radius', structs.decode_BIG_f),
    0xbf7aa2d0: ('aiming_cursor_depth_ring_color', _decode_aiming_cursor_depth_ring_color),
    0xc35b6f6b: ('aiming_cursor_depth_ring_outline_color', _decode_aiming_cursor_depth_ring_outline_color),
    0xb1128885: ('aiming_cursor_depth_ring_secondary_color', _decode_aiming_cursor_depth_ring_secondary_color),
    0x8faa7bb1: ('aiming_cursor_depth_ring_outline_secondary_color', _decode_aiming_cursor_depth_ring_outline_secondary_color),
    0xae50c432: ('aiming_cursor_depth_ring_min_size', structs.decode_BIG_f),
    0x3e23d4d8: ('aiming_cursor_depth_ring_max_size', structs.decode_BIG_f),
    0xb0522ac7: ('x_ray_aiming_cursor_color', _decode_x_ray_aiming_cursor_color),
    0xa4995c5c: ('x_ray_depth_cursor_color', _decode_x_ray_depth_cursor_color),
    0x6363d78d: ('x_ray_depth_cursor_min_size', structs.decode_BIG_f),
    0xf310c767: ('x_ray_depth_cursor_max_size', structs.decode_BIG_f),
    0xc29882b7: ('unknown_0xc29882b7', _decode_unknown_0xc29882b7),
    0xd33fcc91: ('unknown_0xd33fcc91', _decode_unknown_0xd33fcc91),
}
