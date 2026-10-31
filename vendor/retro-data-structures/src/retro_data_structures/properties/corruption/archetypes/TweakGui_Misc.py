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
from retro_data_structures.properties.corruption.archetypes.TweakGui_Misc_UnknownStruct1 import TweakGui_Misc_UnknownStruct1
from retro_data_structures.properties.spline import Spline
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    class TweakGui_MiscJson(typing_extensions.TypedDict):
        skip_front_end: bool
        min_hud_alpha: float
        unknown_0x744165c4: float
        radar_world_radius: float
        unknown_0xa585c592: float
        unknown_0x04f4a6fe: float
        unknown_0x3c327181: float
        unknown_0xa581be26: float
        radar_world_half_height: float
        unknown_0x889ef9ea: float
        energy_bar_low_threshold: float
        energy_bar_filled_drain_speed: float
        energy_bar_shadow_drain_speed: float
        energy_bar_shadow_drain_delay: float
        unknown_0x2821bbca: bool
        hud_flash_magnitude_constant: float
        hud_flash_magnitude_linear: float
        hud_flash_time_constant: float
        hud_flash_time_scale_linear: float
        hud_damage_indicator_radius: float
        unknown_0x55b323e5: float
        unknown_0x411a705e: float
        unknown_0x0a9d701d: float
        unknown_0xf4a8e8ea: float
        unknown_0x50812f49: json_util.JsonValue
        unknown_0x7edc2474: json_util.JsonValue
        unknown_0x4f0d651c: float
        unknown_0x85c31390: float
        hud_damage_jostle_magnitude_constant: float
        hud_damage_jostle_magnitude_linear: float
        hud_damage_jostle_max_offset: float
        hud_damage_jostle_return_acceleration: float
        hud_damage_distortion_magnitude_constant: float
        hud_damage_distortion_magnitude_linear: float
        hud_damage_distortion_time_constant: float
        hud_damage_distortion_time_linear: float
        hud_damage_distortion_max_magnitude: float
        unknown_0x705ed5cb: int
        unknown_0x8922af69: int
        unknown_0x9b970087: int
        lag_type: int
        unknown_0x4dd9d6d1: float
        unknown_0xad4d37cd: float
        unknown_0x95c78e5d: float
        threat_world_radius: float
        unknown_0x78174d4b: float
        unknown_0x3cb2115b: float
        unknown_0xfc30bb21: float
        missile_arrow_fade_time: float
        unknown_0xf3565ff4: int
        unknown_0x7d3c03eb: int
        unknown_0x72d4d899: int
        unknown_0xfb9a4cc7: int
        unknown_0xa1417b38: int
        unknown_0x71b207b4: int
        missile_warning_threshold: float
        unknown_0xdecc7bff: float
        free_look_tick_up_speed: float
        free_look_tick_down_speed: float
        free_look_sound_pitch_magnitude: float
        unknown_0x4ee9c251: bool
        unknown_0xa71e83d5: float
        unknown_0x3652ef32: float
        unknown_0x4ff930a5: int
        unknown_0x1c106df3: int
        unknown_0xdaadf917: int
        unknown_0xe3d55457: int
        unknown_0xdd39f60a: int
        unknown_0x9916df1c: int
        threat_warning_message: str
        threat_damage_message: str
        energy_warning_message: str
        missile_warning_message: str
        missile_empty_warning: str
        missile_warning_fade_time: float
        face_light_constant_attenuation_scalar: float
        face_light_linear_attenuation_scalar: float
        face_light_quadratic_attenuation_scalar: float
        unknown_0x2c412371: float
        unknown_0x3aaf2a8c: float
        flash_pass_magnitude_constant: float
        flash_pass_magnitude_linear: float
        flash_pass_timer_constant: float
        flash_pass_timer_linear: float
        metroid_suck_pulse_cycle_time: float
        metroid_suck_is_use_sine_wave: bool
        metroid_suck_is_additive: bool
        unknown_0xaaff9224: float
        unknown_0xfa4a836c: float
        unknown_0x23661b4f: float
        unknown_0x992b647a: float
        unknown_0x929d08cf: float
        scan_panel_z_rotation_degrees: float
        scan_panel_scale_x: float
        scan_panel_zoomed_position: float
        unknown_0x2845923c: float
        scan_panel_translate_time: float
        scan_window_zoom_time: float
        scan_panel_flash_magnitude: float
        scan_panel_flash_ramp_up_time: float
        scan_panel_flash_ramp_down_time: float
        scan_object_model_scale: float
        scan_object_translate_transition_spline: json_util.JsonObject
        scan_object_rotation_transition_spline: json_util.JsonObject
        scan_object_scale_transition_spline: json_util.JsonObject
        unknown_0xeeb7839b: float
        scan_window_idle_width_scale: float
        scan_window_idle_height_scale: float
        scan_window_zoomed_width_scale: float
        scan_window_zoomed_height_scale: float
        scan_window_idle_zoom_factor: float
        scan_window_locked_zoom_factor: float
        scan_panel_idle_position: float
        unknown_0x7103ca90: bool
        unknown_0x22d4c6a3: float
        helmet_base_ambient_color_combat: json_util.JsonValue
        helmet_base_ambient_color_scan: json_util.JsonValue
        helmet_base_ambient_color_command: json_util.JsonValue
        helmet_base_ambient_color_x_ray: json_util.JsonValue
        helmet_light_ambient_mod_combat: json_util.JsonValue
        helmet_light_ambient_mod_scan: json_util.JsonValue
        helmet_light_ambient_mod_command: json_util.JsonValue
        helmet_light_ambient_mod_x_ray: json_util.JsonValue
        unknown_0x70638eaa: json_util.JsonValue
        helmet_light_constant_attenuation_scalar: float
        helmet_light_linear_attenuation_scalar: float
        helmet_light_quadratic_attenuation_scalar: float
        ift_light_color: json_util.JsonValue
        ift_light_location: json_util.JsonValue
        ift_ambient_color: json_util.JsonValue
        ift_background_color: json_util.JsonValue
        ift_audio_visual_color: json_util.JsonValue
        unknown_0xc4d839f4: json_util.JsonObject
        unknown_0x78521add: json_util.JsonObject
        unknown_0xb40c6a3b: float
    

@dataclasses.dataclass()
class TweakGui_Misc(BaseProperty):
    skip_front_end: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x2f9d48b8, original_name='SkipFrontEnd'
        ),
    })
    min_hud_alpha: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x71b475d0, original_name='MinHUDAlpha'
        ),
    })
    unknown_0x744165c4: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x744165c4, original_name='Unknown'
        ),
    })
    radar_world_radius: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xee1ba439, original_name='RadarWorldRadius'
        ),
    })
    unknown_0xa585c592: float = dataclasses.field(default=200.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa585c592, original_name='Unknown'
        ),
    })
    unknown_0x04f4a6fe: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x04f4a6fe, original_name='Unknown'
        ),
    })
    unknown_0x3c327181: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3c327181, original_name='Unknown'
        ),
    })
    unknown_0xa581be26: float = dataclasses.field(default=0.75, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa581be26, original_name='Unknown'
        ),
    })
    radar_world_half_height: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x68d88e25, original_name='RadarWorldHalfHeight'
        ),
    })
    unknown_0x889ef9ea: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x889ef9ea, original_name='Unknown'
        ),
    })
    energy_bar_low_threshold: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb68ff81a, original_name='EnergyBarLowThreshold'
        ),
    })
    energy_bar_filled_drain_speed: float = dataclasses.field(default=99.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x04510638, original_name='EnergyBarFilledDrainSpeed'
        ),
    })
    energy_bar_shadow_drain_speed: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7a48c3b1, original_name='EnergyBarShadowDrainSpeed'
        ),
    })
    energy_bar_shadow_drain_delay: float = dataclasses.field(default=0.699999988079071, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0d257063, original_name='EnergyBarShadowDrainDelay'
        ),
    })
    unknown_0x2821bbca: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x2821bbca, original_name='Unknown'
        ),
    })
    hud_flash_magnitude_constant: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc4dd4d5b, original_name='HudFlashMagnitudeConstant'
        ),
    })
    hud_flash_magnitude_linear: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6031503e, original_name='HudFlashMagnitudeLinear'
        ),
    })
    hud_flash_time_constant: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9f5ebba2, original_name='HudFlashTimeConstant'
        ),
    })
    hud_flash_time_scale_linear: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2930d57f, original_name='HudFlashTimeScaleLinear'
        ),
    })
    hud_damage_indicator_radius: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3ac94cf1, original_name='HudDamageIndicatorRadius'
        ),
    })
    unknown_0x55b323e5: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x55b323e5, original_name='Unknown'
        ),
    })
    unknown_0x411a705e: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x411a705e, original_name='Unknown'
        ),
    })
    unknown_0x0a9d701d: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0a9d701d, original_name='Unknown'
        ),
    })
    unknown_0xf4a8e8ea: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf4a8e8ea, original_name='Unknown'
        ),
    })
    unknown_0x50812f49: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=-4.0, z=0.800000011920929), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x50812f49, original_name='Unknown', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    unknown_0x7edc2474: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=-4.0, z=0.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x7edc2474, original_name='Unknown', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    unknown_0x4f0d651c: float = dataclasses.field(default=70.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4f0d651c, original_name='Unknown'
        ),
    })
    unknown_0x85c31390: float = dataclasses.field(default=45.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x85c31390, original_name='Unknown'
        ),
    })
    hud_damage_jostle_magnitude_constant: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb93990e6, original_name='HudDamageJostleMagnitudeConstant'
        ),
    })
    hud_damage_jostle_magnitude_linear: float = dataclasses.field(default=0.009999999776482582, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4036cdb6, original_name='HudDamageJostleMagnitudeLinear'
        ),
    })
    hud_damage_jostle_max_offset: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa7cf8baa, original_name='HudDamageJostleMaxOffset'
        ),
    })
    hud_damage_jostle_return_acceleration: float = dataclasses.field(default=0.004999999888241291, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3e8e6afd, original_name='HudDamageJostleReturnAcceleration'
        ),
    })
    hud_damage_distortion_magnitude_constant: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xec040d56, original_name='HudDamageDistortionMagnitudeConstant'
        ),
    })
    hud_damage_distortion_magnitude_linear: float = dataclasses.field(default=0.009999999776482582, metadata={
        'reflection': FieldReflection[float](
            float, id=0x236bbe14, original_name='HudDamageDistortionMagnitudeLinear'
        ),
    })
    hud_damage_distortion_time_constant: float = dataclasses.field(default=0.019999999552965164, metadata={
        'reflection': FieldReflection[float](
            float, id=0x19f5c324, original_name='HudDamageDistortionTimeConstant'
        ),
    })
    hud_damage_distortion_time_linear: float = dataclasses.field(default=0.05000000074505806, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfd559f8c, original_name='HudDamageDistortionTimeLinear'
        ),
    })
    hud_damage_distortion_max_magnitude: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe4702e21, original_name='HudDamageDistortionMaxMagnitude'
        ),
    })
    unknown_0x705ed5cb: int = dataclasses.field(default=5, metadata={
        'reflection': FieldReflection[int](
            int, id=0x705ed5cb, original_name='Unknown'
        ),
    })
    unknown_0x8922af69: int = dataclasses.field(default=40, metadata={
        'reflection': FieldReflection[int](
            int, id=0x8922af69, original_name='Unknown'
        ),
    })
    unknown_0x9b970087: int = dataclasses.field(default=16, metadata={
        'reflection': FieldReflection[int](
            int, id=0x9b970087, original_name='Unknown'
        ),
    })
    lag_type: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xf4ec68ae, original_name='LagType'
        ),
    })  # Choice
    unknown_0x4dd9d6d1: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4dd9d6d1, original_name='Unknown'
        ),
    })
    unknown_0xad4d37cd: float = dataclasses.field(default=77.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xad4d37cd, original_name='Unknown'
        ),
    })
    unknown_0x95c78e5d: float = dataclasses.field(default=0.8999999761581421, metadata={
        'reflection': FieldReflection[float](
            float, id=0x95c78e5d, original_name='Unknown'
        ),
    })
    threat_world_radius: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1a8dc454, original_name='ThreatWorldRadius'
        ),
    })
    unknown_0x78174d4b: float = dataclasses.field(default=1.649999976158142, metadata={
        'reflection': FieldReflection[float](
            float, id=0x78174d4b, original_name='Unknown'
        ),
    })
    unknown_0x3cb2115b: float = dataclasses.field(default=0.03999999910593033, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3cb2115b, original_name='Unknown'
        ),
    })
    unknown_0xfc30bb21: float = dataclasses.field(default=0.03999999910593033, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfc30bb21, original_name='Unknown'
        ),
    })
    missile_arrow_fade_time: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x86cdde75, original_name='MissileArrowFadeTime'
        ),
    })
    unknown_0xf3565ff4: int = dataclasses.field(default=2, metadata={
        'reflection': FieldReflection[int](
            int, id=0xf3565ff4, original_name='Unknown'
        ),
    })
    unknown_0x7d3c03eb: int = dataclasses.field(default=3, metadata={
        'reflection': FieldReflection[int](
            int, id=0x7d3c03eb, original_name='Unknown'
        ),
    })
    unknown_0x72d4d899: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x72d4d899, original_name='Unknown'
        ),
    })
    unknown_0xfb9a4cc7: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xfb9a4cc7, original_name='Unknown'
        ),
    })
    unknown_0xa1417b38: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xa1417b38, original_name='Unknown'
        ),
    })
    unknown_0x71b207b4: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x71b207b4, original_name='Unknown'
        ),
    })
    missile_warning_threshold: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0x46d75fe1, original_name='MissileWarningThreshold'
        ),
    })
    unknown_0xdecc7bff: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdecc7bff, original_name='Unknown'
        ),
    })
    free_look_tick_up_speed: float = dataclasses.field(default=-2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcbff7b94, original_name='FreeLookTickUpSpeed'
        ),
    })
    free_look_tick_down_speed: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0babf93b, original_name='FreeLookTickDownSpeed'
        ),
    })
    free_look_sound_pitch_magnitude: float = dataclasses.field(default=3000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc0004f50, original_name='FreeLookSoundPitchMagnitude'
        ),
    })
    unknown_0x4ee9c251: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x4ee9c251, original_name='Unknown'
        ),
    })
    unknown_0xa71e83d5: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa71e83d5, original_name='Unknown'
        ),
    })
    unknown_0x3652ef32: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3652ef32, original_name='Unknown'
        ),
    })
    unknown_0x4ff930a5: int = dataclasses.field(default=15, metadata={
        'reflection': FieldReflection[int](
            int, id=0x4ff930a5, original_name='Unknown'
        ),
    })
    unknown_0x1c106df3: int = dataclasses.field(default=10, metadata={
        'reflection': FieldReflection[int](
            int, id=0x1c106df3, original_name='Unknown'
        ),
    })
    unknown_0xdaadf917: int = dataclasses.field(default=6, metadata={
        'reflection': FieldReflection[int](
            int, id=0xdaadf917, original_name='Unknown'
        ),
    })
    unknown_0xe3d55457: int = dataclasses.field(default=9, metadata={
        'reflection': FieldReflection[int](
            int, id=0xe3d55457, original_name='Unknown'
        ),
    })
    unknown_0xdd39f60a: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0xdd39f60a, original_name='Unknown'
        ),
    })
    unknown_0x9916df1c: int = dataclasses.field(default=3, metadata={
        'reflection': FieldReflection[int](
            int, id=0x9916df1c, original_name='Unknown'
        ),
    })
    threat_warning_message: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x3db45f6a, original_name='ThreatWarningMessage'
        ),
    })
    threat_damage_message: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x471f1217, original_name='ThreatDamageMessage'
        ),
    })
    energy_warning_message: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xf8b84c58, original_name='EnergyWarningMessage'
        ),
    })
    missile_warning_message: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xbc2c8de6, original_name='MissileWarningMessage'
        ),
    })
    missile_empty_warning: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x54203510, original_name='MissileEmptyWarning'
        ),
    })
    missile_warning_fade_time: float = dataclasses.field(default=7.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcf9fd47e, original_name='MissileWarningFadeTime'
        ),
    })
    face_light_constant_attenuation_scalar: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcfb88ceb, original_name='FaceLightConstantAttenuationScalar'
        ),
    })
    face_light_linear_attenuation_scalar: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5e388dd0, original_name='FaceLightLinearAttenuationScalar'
        ),
    })
    face_light_quadratic_attenuation_scalar: float = dataclasses.field(default=0.699999988079071, metadata={
        'reflection': FieldReflection[float](
            float, id=0x86bc055e, original_name='FaceLightQuadraticAttenuationScalar'
        ),
    })
    unknown_0x2c412371: float = dataclasses.field(default=0.699999988079071, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2c412371, original_name='Unknown'
        ),
    })
    unknown_0x3aaf2a8c: float = dataclasses.field(default=0.800000011920929, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3aaf2a8c, original_name='Unknown'
        ),
    })
    flash_pass_magnitude_constant: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb515dd12, original_name='FlashPassMagnitudeConstant'
        ),
    })
    flash_pass_magnitude_linear: float = dataclasses.field(default=0.05000000074505806, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa949b037, original_name='FlashPassMagnitudeLinear'
        ),
    })
    flash_pass_timer_constant: float = dataclasses.field(default=0.05000000074505806, metadata={
        'reflection': FieldReflection[float](
            float, id=0xca9d401c, original_name='FlashPassTimerConstant'
        ),
    })
    flash_pass_timer_linear: float = dataclasses.field(default=0.05000000074505806, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8186e8fe, original_name='FlashPassTimerLinear'
        ),
    })
    metroid_suck_pulse_cycle_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x02a2198a, original_name='MetroidSuckPulseCycleTime'
        ),
    })
    metroid_suck_is_use_sine_wave: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x8b64dc44, original_name='MetroidSuckIsUseSineWave'
        ),
    })
    metroid_suck_is_additive: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x7161446b, original_name='MetroidSuckIsAdditive'
        ),
    })
    unknown_0xaaff9224: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xaaff9224, original_name='Unknown'
        ),
    })
    unknown_0xfa4a836c: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfa4a836c, original_name='Unknown'
        ),
    })
    unknown_0x23661b4f: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x23661b4f, original_name='Unknown'
        ),
    })
    unknown_0x992b647a: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x992b647a, original_name='Unknown'
        ),
    })
    unknown_0x929d08cf: float = dataclasses.field(default=0.699999988079071, metadata={
        'reflection': FieldReflection[float](
            float, id=0x929d08cf, original_name='Unknown'
        ),
    })
    scan_panel_z_rotation_degrees: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xffeba1f2, original_name='ScanPanelZRotationDegrees'
        ),
    })
    scan_panel_scale_x: float = dataclasses.field(default=0.800000011920929, metadata={
        'reflection': FieldReflection[float](
            float, id=0x13654f20, original_name='ScanPanelScaleX'
        ),
    })
    scan_panel_zoomed_position: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7083faf0, original_name='ScanPanelZoomedPosition'
        ),
    })
    unknown_0x2845923c: float = dataclasses.field(default=0.8999999761581421, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2845923c, original_name='Unknown'
        ),
    })
    scan_panel_translate_time: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0xeb6a7f2a, original_name='ScanPanelTranslateTime'
        ),
    })
    scan_window_zoom_time: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd05eb27a, original_name='ScanWindowZoomTime'
        ),
    })
    scan_panel_flash_magnitude: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8b66820d, original_name='ScanPanelFlashMagnitude'
        ),
    })
    scan_panel_flash_ramp_up_time: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x138f1104, original_name='ScanPanelFlashRampUpTime'
        ),
    })
    scan_panel_flash_ramp_down_time: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd0d1760e, original_name='ScanPanelFlashRampDownTime'
        ),
    })
    scan_object_model_scale: float = dataclasses.field(default=6.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xce9f5770, original_name='ScanObjectModelScale'
        ),
    })
    scan_object_translate_transition_spline: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xeaf17d45, original_name='ScanObjectTranslateTransitionSpline', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    scan_object_rotation_transition_spline: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xd81537b6, original_name='ScanObjectRotationTransitionSpline', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    scan_object_scale_transition_spline: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x3ba84552, original_name='ScanObjectScaleTransitionSpline', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    unknown_0xeeb7839b: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0xeeb7839b, original_name='Unknown'
        ),
    })
    scan_window_idle_width_scale: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x24cf1719, original_name='ScanWindowIdleWidthScale'
        ),
    })
    scan_window_idle_height_scale: float = dataclasses.field(default=0.800000011920929, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa4adf6ea, original_name='ScanWindowIdleHeightScale'
        ),
    })
    scan_window_zoomed_width_scale: float = dataclasses.field(default=1.100000023841858, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe3755dda, original_name='ScanWindowZoomedWidthScale'
        ),
    })
    scan_window_zoomed_height_scale: float = dataclasses.field(default=1.100000023841858, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa607dfaa, original_name='ScanWindowZoomedHeightScale'
        ),
    })
    scan_window_idle_zoom_factor: float = dataclasses.field(default=1.350000023841858, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf5f7a748, original_name='ScanWindowIdleZoomFactor'
        ),
    })
    scan_window_locked_zoom_factor: float = dataclasses.field(default=1.75, metadata={
        'reflection': FieldReflection[float](
            float, id=0x61215643, original_name='ScanWindowLockedZoomFactor'
        ),
    })
    scan_panel_idle_position: float = dataclasses.field(default=-10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa3f4095e, original_name='ScanPanelIdlePosition'
        ),
    })
    unknown_0x7103ca90: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x7103ca90, original_name='Unknown'
        ),
    })
    unknown_0x22d4c6a3: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x22d4c6a3, original_name='Unknown'
        ),
    })
    helmet_base_ambient_color_combat: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.2941179871559143, b=0.2941179871559143, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf08c7e50, original_name='HelmetBaseAmbientColorCombat', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    helmet_base_ambient_color_scan: Color = dataclasses.field(default_factory=lambda: Color(r=0.274509996175766, g=0.2862749993801117, b=0.5607839822769165, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x809b480d, original_name='HelmetBaseAmbientColorScan', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    helmet_base_ambient_color_command: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.2941179871559143, b=0.2941179871559143, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x38804beb, original_name='HelmetBaseAmbientColorCommand', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    helmet_base_ambient_color_x_ray: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.2941179871559143, b=0.2941179871559143, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x557ab710, original_name='HelmetBaseAmbientColorXRay', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    helmet_light_ambient_mod_combat: Color = dataclasses.field(default_factory=lambda: Color(r=0.3330000042915344, g=0.3330000042915344, b=0.3330000042915344, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xc29b7093, original_name='HelmetLightAmbientModCombat', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    helmet_light_ambient_mod_scan: Color = dataclasses.field(default_factory=lambda: Color(r=0.039000000804662704, g=0.039000000804662704, b=0.039000000804662704, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x582efd3b, original_name='HelmetLightAmbientModScan', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    helmet_light_ambient_mod_command: Color = dataclasses.field(default_factory=lambda: Color(r=0.2540000081062317, g=0.2540000081062317, b=0.2540000081062317, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x3adfcfef, original_name='HelmetLightAmbientModCommand', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    helmet_light_ambient_mod_x_ray: Color = dataclasses.field(default_factory=lambda: Color(r=0.10000000149011612, g=0.10000000149011612, b=0.10000000149011612, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x8dcf0226, original_name='HelmetLightAmbientModXRay', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    unknown_0x70638eaa: Color = dataclasses.field(default_factory=lambda: Color(r=0.38999998569488525, g=0.38999998569488525, b=0.38999998569488525, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x70638eaa, original_name='Unknown', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    helmet_light_constant_attenuation_scalar: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5b888032, original_name='HelmetLightConstantAttenuationScalar'
        ),
    })
    helmet_light_linear_attenuation_scalar: float = dataclasses.field(default=0.699999988079071, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb7322d26, original_name='HelmetLightLinearAttenuationScalar'
        ),
    })
    helmet_light_quadratic_attenuation_scalar: float = dataclasses.field(default=0.699999988079071, metadata={
        'reflection': FieldReflection[float](
            float, id=0x79275f22, original_name='HelmetLightQuadraticAttenuationScalar'
        ),
    })
    ift_light_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xa9620c45, original_name='IFTLightColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    ift_light_location: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x7189c83e, original_name='IFTLightLocation', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    ift_ambient_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.30000001192092896, g=0.30000001192092896, b=0.30000001192092896, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xe7126099, original_name='IFTAmbientColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    ift_background_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.10000000149011612, g=0.10000000149011612, b=0.10000000149011612, a=0.5), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x934a247f, original_name='IFTBackgroundColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    ift_audio_visual_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x0530a846, original_name='IFTAudioVisualColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    unknown_0xc4d839f4: TweakGui_Misc_UnknownStruct1 = dataclasses.field(default_factory=TweakGui_Misc_UnknownStruct1, metadata={
        'reflection': FieldReflection[TweakGui_Misc_UnknownStruct1](
            TweakGui_Misc_UnknownStruct1, id=0xc4d839f4, original_name='Unknown', from_json=TweakGui_Misc_UnknownStruct1.from_json, to_json=TweakGui_Misc_UnknownStruct1.to_json
        ),
    })
    unknown_0x78521add: TweakGui_Misc_UnknownStruct1 = dataclasses.field(default_factory=TweakGui_Misc_UnknownStruct1, metadata={
        'reflection': FieldReflection[TweakGui_Misc_UnknownStruct1](
            TweakGui_Misc_UnknownStruct1, id=0x78521add, original_name='Unknown', from_json=TweakGui_Misc_UnknownStruct1.from_json, to_json=TweakGui_Misc_UnknownStruct1.to_json
        ),
    })
    unknown_0xb40c6a3b: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb40c6a3b, original_name='Unknown'
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
        if property_count != 135:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2f9d48b8
        skip_front_end = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71b475d0
        min_hud_alpha = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x744165c4
        unknown_0x744165c4 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xee1ba439
        radar_world_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa585c592
        unknown_0xa585c592 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x04f4a6fe
        unknown_0x04f4a6fe = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3c327181
        unknown_0x3c327181 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa581be26
        unknown_0xa581be26 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68d88e25
        radar_world_half_height = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x889ef9ea
        unknown_0x889ef9ea = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb68ff81a
        energy_bar_low_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x04510638
        energy_bar_filled_drain_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7a48c3b1
        energy_bar_shadow_drain_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0d257063
        energy_bar_shadow_drain_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2821bbca
        unknown_0x2821bbca = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc4dd4d5b
        hud_flash_magnitude_constant = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6031503e
        hud_flash_magnitude_linear = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9f5ebba2
        hud_flash_time_constant = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2930d57f
        hud_flash_time_scale_linear = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3ac94cf1
        hud_damage_indicator_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x55b323e5
        unknown_0x55b323e5 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x411a705e
        unknown_0x411a705e = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0a9d701d
        unknown_0x0a9d701d = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf4a8e8ea
        unknown_0xf4a8e8ea = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50812f49
        unknown_0x50812f49 = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7edc2474
        unknown_0x7edc2474 = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4f0d651c
        unknown_0x4f0d651c = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x85c31390
        unknown_0x85c31390 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb93990e6
        hud_damage_jostle_magnitude_constant = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4036cdb6
        hud_damage_jostle_magnitude_linear = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa7cf8baa
        hud_damage_jostle_max_offset = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3e8e6afd
        hud_damage_jostle_return_acceleration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xec040d56
        hud_damage_distortion_magnitude_constant = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x236bbe14
        hud_damage_distortion_magnitude_linear = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19f5c324
        hud_damage_distortion_time_constant = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfd559f8c
        hud_damage_distortion_time_linear = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe4702e21
        hud_damage_distortion_max_magnitude = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x705ed5cb
        unknown_0x705ed5cb = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8922af69
        unknown_0x8922af69 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9b970087
        unknown_0x9b970087 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf4ec68ae
        lag_type = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4dd9d6d1
        unknown_0x4dd9d6d1 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xad4d37cd
        unknown_0xad4d37cd = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95c78e5d
        unknown_0x95c78e5d = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1a8dc454
        threat_world_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78174d4b
        unknown_0x78174d4b = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3cb2115b
        unknown_0x3cb2115b = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfc30bb21
        unknown_0xfc30bb21 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x86cdde75
        missile_arrow_fade_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf3565ff4
        unknown_0xf3565ff4 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7d3c03eb
        unknown_0x7d3c03eb = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x72d4d899
        unknown_0x72d4d899 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfb9a4cc7
        unknown_0xfb9a4cc7 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa1417b38
        unknown_0xa1417b38 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71b207b4
        unknown_0x71b207b4 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x46d75fe1
        missile_warning_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdecc7bff
        unknown_0xdecc7bff = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcbff7b94
        free_look_tick_up_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0babf93b
        free_look_tick_down_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc0004f50
        free_look_sound_pitch_magnitude = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4ee9c251
        unknown_0x4ee9c251 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa71e83d5
        unknown_0xa71e83d5 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3652ef32
        unknown_0x3652ef32 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4ff930a5
        unknown_0x4ff930a5 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1c106df3
        unknown_0x1c106df3 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdaadf917
        unknown_0xdaadf917 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe3d55457
        unknown_0xe3d55457 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdd39f60a
        unknown_0xdd39f60a = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9916df1c
        unknown_0x9916df1c = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3db45f6a
        threat_warning_message = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x471f1217
        threat_damage_message = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf8b84c58
        energy_warning_message = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbc2c8de6
        missile_warning_message = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x54203510
        missile_empty_warning = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcf9fd47e
        missile_warning_fade_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcfb88ceb
        face_light_constant_attenuation_scalar = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5e388dd0
        face_light_linear_attenuation_scalar = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x86bc055e
        face_light_quadratic_attenuation_scalar = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2c412371
        unknown_0x2c412371 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3aaf2a8c
        unknown_0x3aaf2a8c = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb515dd12
        flash_pass_magnitude_constant = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa949b037
        flash_pass_magnitude_linear = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xca9d401c
        flash_pass_timer_constant = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8186e8fe
        flash_pass_timer_linear = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x02a2198a
        metroid_suck_pulse_cycle_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8b64dc44
        metroid_suck_is_use_sine_wave = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7161446b
        metroid_suck_is_additive = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaaff9224
        unknown_0xaaff9224 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfa4a836c
        unknown_0xfa4a836c = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23661b4f
        unknown_0x23661b4f = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x992b647a
        unknown_0x992b647a = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x929d08cf
        unknown_0x929d08cf = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xffeba1f2
        scan_panel_z_rotation_degrees = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13654f20
        scan_panel_scale_x = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7083faf0
        scan_panel_zoomed_position = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2845923c
        unknown_0x2845923c = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xeb6a7f2a
        scan_panel_translate_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd05eb27a
        scan_window_zoom_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8b66820d
        scan_panel_flash_magnitude = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x138f1104
        scan_panel_flash_ramp_up_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd0d1760e
        scan_panel_flash_ramp_down_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xce9f5770
        scan_object_model_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xeaf17d45
        scan_object_translate_transition_spline = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd81537b6
        scan_object_rotation_transition_spline = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3ba84552
        scan_object_scale_transition_spline = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xeeb7839b
        unknown_0xeeb7839b = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24cf1719
        scan_window_idle_width_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa4adf6ea
        scan_window_idle_height_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe3755dda
        scan_window_zoomed_width_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa607dfaa
        scan_window_zoomed_height_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf5f7a748
        scan_window_idle_zoom_factor = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x61215643
        scan_window_locked_zoom_factor = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa3f4095e
        scan_panel_idle_position = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7103ca90
        unknown_0x7103ca90 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x22d4c6a3
        unknown_0x22d4c6a3 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf08c7e50
        helmet_base_ambient_color_combat = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x809b480d
        helmet_base_ambient_color_scan = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x38804beb
        helmet_base_ambient_color_command = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x557ab710
        helmet_base_ambient_color_x_ray = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc29b7093
        helmet_light_ambient_mod_combat = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x582efd3b
        helmet_light_ambient_mod_scan = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3adfcfef
        helmet_light_ambient_mod_command = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8dcf0226
        helmet_light_ambient_mod_x_ray = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x70638eaa
        unknown_0x70638eaa = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5b888032
        helmet_light_constant_attenuation_scalar = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb7322d26
        helmet_light_linear_attenuation_scalar = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x79275f22
        helmet_light_quadratic_attenuation_scalar = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa9620c45
        ift_light_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7189c83e
        ift_light_location = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe7126099
        ift_ambient_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x934a247f
        ift_background_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0530a846
        ift_audio_visual_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc4d839f4
        unknown_0xc4d839f4 = TweakGui_Misc_UnknownStruct1.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78521add
        unknown_0x78521add = TweakGui_Misc_UnknownStruct1.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb40c6a3b
        unknown_0xb40c6a3b = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(skip_front_end, min_hud_alpha, unknown_0x744165c4, radar_world_radius, unknown_0xa585c592, unknown_0x04f4a6fe, unknown_0x3c327181, unknown_0xa581be26, radar_world_half_height, unknown_0x889ef9ea, energy_bar_low_threshold, energy_bar_filled_drain_speed, energy_bar_shadow_drain_speed, energy_bar_shadow_drain_delay, unknown_0x2821bbca, hud_flash_magnitude_constant, hud_flash_magnitude_linear, hud_flash_time_constant, hud_flash_time_scale_linear, hud_damage_indicator_radius, unknown_0x55b323e5, unknown_0x411a705e, unknown_0x0a9d701d, unknown_0xf4a8e8ea, unknown_0x50812f49, unknown_0x7edc2474, unknown_0x4f0d651c, unknown_0x85c31390, hud_damage_jostle_magnitude_constant, hud_damage_jostle_magnitude_linear, hud_damage_jostle_max_offset, hud_damage_jostle_return_acceleration, hud_damage_distortion_magnitude_constant, hud_damage_distortion_magnitude_linear, hud_damage_distortion_time_constant, hud_damage_distortion_time_linear, hud_damage_distortion_max_magnitude, unknown_0x705ed5cb, unknown_0x8922af69, unknown_0x9b970087, lag_type, unknown_0x4dd9d6d1, unknown_0xad4d37cd, unknown_0x95c78e5d, threat_world_radius, unknown_0x78174d4b, unknown_0x3cb2115b, unknown_0xfc30bb21, missile_arrow_fade_time, unknown_0xf3565ff4, unknown_0x7d3c03eb, unknown_0x72d4d899, unknown_0xfb9a4cc7, unknown_0xa1417b38, unknown_0x71b207b4, missile_warning_threshold, unknown_0xdecc7bff, free_look_tick_up_speed, free_look_tick_down_speed, free_look_sound_pitch_magnitude, unknown_0x4ee9c251, unknown_0xa71e83d5, unknown_0x3652ef32, unknown_0x4ff930a5, unknown_0x1c106df3, unknown_0xdaadf917, unknown_0xe3d55457, unknown_0xdd39f60a, unknown_0x9916df1c, threat_warning_message, threat_damage_message, energy_warning_message, missile_warning_message, missile_empty_warning, missile_warning_fade_time, face_light_constant_attenuation_scalar, face_light_linear_attenuation_scalar, face_light_quadratic_attenuation_scalar, unknown_0x2c412371, unknown_0x3aaf2a8c, flash_pass_magnitude_constant, flash_pass_magnitude_linear, flash_pass_timer_constant, flash_pass_timer_linear, metroid_suck_pulse_cycle_time, metroid_suck_is_use_sine_wave, metroid_suck_is_additive, unknown_0xaaff9224, unknown_0xfa4a836c, unknown_0x23661b4f, unknown_0x992b647a, unknown_0x929d08cf, scan_panel_z_rotation_degrees, scan_panel_scale_x, scan_panel_zoomed_position, unknown_0x2845923c, scan_panel_translate_time, scan_window_zoom_time, scan_panel_flash_magnitude, scan_panel_flash_ramp_up_time, scan_panel_flash_ramp_down_time, scan_object_model_scale, scan_object_translate_transition_spline, scan_object_rotation_transition_spline, scan_object_scale_transition_spline, unknown_0xeeb7839b, scan_window_idle_width_scale, scan_window_idle_height_scale, scan_window_zoomed_width_scale, scan_window_zoomed_height_scale, scan_window_idle_zoom_factor, scan_window_locked_zoom_factor, scan_panel_idle_position, unknown_0x7103ca90, unknown_0x22d4c6a3, helmet_base_ambient_color_combat, helmet_base_ambient_color_scan, helmet_base_ambient_color_command, helmet_base_ambient_color_x_ray, helmet_light_ambient_mod_combat, helmet_light_ambient_mod_scan, helmet_light_ambient_mod_command, helmet_light_ambient_mod_x_ray, unknown_0x70638eaa, helmet_light_constant_attenuation_scalar, helmet_light_linear_attenuation_scalar, helmet_light_quadratic_attenuation_scalar, ift_light_color, ift_light_location, ift_ambient_color, ift_background_color, ift_audio_visual_color, unknown_0xc4d839f4, unknown_0x78521add, unknown_0xb40c6a3b)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x87')  # 135 properties

        data.write(b'/\x9dH\xb8')  # 0x2f9d48b8
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.skip_front_end))

        data.write(b'q\xb4u\xd0')  # 0x71b475d0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_hud_alpha))

        data.write(b'tAe\xc4')  # 0x744165c4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x744165c4))

        data.write(b'\xee\x1b\xa49')  # 0xee1ba439
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.radar_world_radius))

        data.write(b'\xa5\x85\xc5\x92')  # 0xa585c592
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa585c592))

        data.write(b'\x04\xf4\xa6\xfe')  # 0x4f4a6fe
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x04f4a6fe))

        data.write(b'<2q\x81')  # 0x3c327181
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3c327181))

        data.write(b'\xa5\x81\xbe&')  # 0xa581be26
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa581be26))

        data.write(b'h\xd8\x8e%')  # 0x68d88e25
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.radar_world_half_height))

        data.write(b'\x88\x9e\xf9\xea')  # 0x889ef9ea
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x889ef9ea))

        data.write(b'\xb6\x8f\xf8\x1a')  # 0xb68ff81a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.energy_bar_low_threshold))

        data.write(b'\x04Q\x068')  # 0x4510638
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.energy_bar_filled_drain_speed))

        data.write(b'zH\xc3\xb1')  # 0x7a48c3b1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.energy_bar_shadow_drain_speed))

        data.write(b'\r%pc')  # 0xd257063
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.energy_bar_shadow_drain_delay))

        data.write(b'(!\xbb\xca')  # 0x2821bbca
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x2821bbca))

        data.write(b'\xc4\xddM[')  # 0xc4dd4d5b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hud_flash_magnitude_constant))

        data.write(b'`1P>')  # 0x6031503e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hud_flash_magnitude_linear))

        data.write(b'\x9f^\xbb\xa2')  # 0x9f5ebba2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hud_flash_time_constant))

        data.write(b')0\xd5\x7f')  # 0x2930d57f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hud_flash_time_scale_linear))

        data.write(b':\xc9L\xf1')  # 0x3ac94cf1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hud_damage_indicator_radius))

        data.write(b'U\xb3#\xe5')  # 0x55b323e5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x55b323e5))

        data.write(b'A\x1ap^')  # 0x411a705e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x411a705e))

        data.write(b'\n\x9dp\x1d')  # 0xa9d701d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x0a9d701d))

        data.write(b'\xf4\xa8\xe8\xea')  # 0xf4a8e8ea
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf4a8e8ea))

        data.write(b'P\x81/I')  # 0x50812f49
        data.write(b'\x00\x0c')  # size
        self.unknown_0x50812f49.to_stream(data, game)

        data.write(b'~\xdc$t')  # 0x7edc2474
        data.write(b'\x00\x0c')  # size
        self.unknown_0x7edc2474.to_stream(data, game)

        data.write(b'O\re\x1c')  # 0x4f0d651c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4f0d651c))

        data.write(b'\x85\xc3\x13\x90')  # 0x85c31390
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x85c31390))

        data.write(b'\xb99\x90\xe6')  # 0xb93990e6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hud_damage_jostle_magnitude_constant))

        data.write(b'@6\xcd\xb6')  # 0x4036cdb6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hud_damage_jostle_magnitude_linear))

        data.write(b'\xa7\xcf\x8b\xaa')  # 0xa7cf8baa
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hud_damage_jostle_max_offset))

        data.write(b'>\x8ej\xfd')  # 0x3e8e6afd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hud_damage_jostle_return_acceleration))

        data.write(b'\xec\x04\rV')  # 0xec040d56
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hud_damage_distortion_magnitude_constant))

        data.write(b'#k\xbe\x14')  # 0x236bbe14
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hud_damage_distortion_magnitude_linear))

        data.write(b'\x19\xf5\xc3$')  # 0x19f5c324
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hud_damage_distortion_time_constant))

        data.write(b'\xfdU\x9f\x8c')  # 0xfd559f8c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hud_damage_distortion_time_linear))

        data.write(b'\xe4p.!')  # 0xe4702e21
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hud_damage_distortion_max_magnitude))

        data.write(b'p^\xd5\xcb')  # 0x705ed5cb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x705ed5cb))

        data.write(b'\x89"\xafi')  # 0x8922af69
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x8922af69))

        data.write(b'\x9b\x97\x00\x87')  # 0x9b970087
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x9b970087))

        data.write(b'\xf4\xech\xae')  # 0xf4ec68ae
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.lag_type))

        data.write(b'M\xd9\xd6\xd1')  # 0x4dd9d6d1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x4dd9d6d1))

        data.write(b'\xadM7\xcd')  # 0xad4d37cd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xad4d37cd))

        data.write(b'\x95\xc7\x8e]')  # 0x95c78e5d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x95c78e5d))

        data.write(b'\x1a\x8d\xc4T')  # 0x1a8dc454
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.threat_world_radius))

        data.write(b'x\x17MK')  # 0x78174d4b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x78174d4b))

        data.write(b'<\xb2\x11[')  # 0x3cb2115b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3cb2115b))

        data.write(b'\xfc0\xbb!')  # 0xfc30bb21
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfc30bb21))

        data.write(b'\x86\xcd\xdeu')  # 0x86cdde75
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.missile_arrow_fade_time))

        data.write(b'\xf3V_\xf4')  # 0xf3565ff4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xf3565ff4))

        data.write(b'}<\x03\xeb')  # 0x7d3c03eb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x7d3c03eb))

        data.write(b'r\xd4\xd8\x99')  # 0x72d4d899
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x72d4d899))

        data.write(b'\xfb\x9aL\xc7')  # 0xfb9a4cc7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xfb9a4cc7))

        data.write(b'\xa1A{8')  # 0xa1417b38
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xa1417b38))

        data.write(b'q\xb2\x07\xb4')  # 0x71b207b4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x71b207b4))

        data.write(b'F\xd7_\xe1')  # 0x46d75fe1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.missile_warning_threshold))

        data.write(b'\xde\xcc{\xff')  # 0xdecc7bff
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xdecc7bff))

        data.write(b'\xcb\xff{\x94')  # 0xcbff7b94
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.free_look_tick_up_speed))

        data.write(b'\x0b\xab\xf9;')  # 0xbabf93b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.free_look_tick_down_speed))

        data.write(b'\xc0\x00OP')  # 0xc0004f50
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.free_look_sound_pitch_magnitude))

        data.write(b'N\xe9\xc2Q')  # 0x4ee9c251
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x4ee9c251))

        data.write(b'\xa7\x1e\x83\xd5')  # 0xa71e83d5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xa71e83d5))

        data.write(b'6R\xef2')  # 0x3652ef32
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3652ef32))

        data.write(b'O\xf90\xa5')  # 0x4ff930a5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x4ff930a5))

        data.write(b'\x1c\x10m\xf3')  # 0x1c106df3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x1c106df3))

        data.write(b'\xda\xad\xf9\x17')  # 0xdaadf917
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xdaadf917))

        data.write(b'\xe3\xd5TW')  # 0xe3d55457
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xe3d55457))

        data.write(b'\xdd9\xf6\n')  # 0xdd39f60a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xdd39f60a))

        data.write(b'\x99\x16\xdf\x1c')  # 0x9916df1c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x9916df1c))

        data.write(b'=\xb4_j')  # 0x3db45f6a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.threat_warning_message.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'G\x1f\x12\x17')  # 0x471f1217
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.threat_damage_message.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf8\xb8LX')  # 0xf8b84c58
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.energy_warning_message.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbc,\x8d\xe6')  # 0xbc2c8de6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.missile_warning_message.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'T 5\x10')  # 0x54203510
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.missile_empty_warning.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xcf\x9f\xd4~')  # 0xcf9fd47e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.missile_warning_fade_time))

        data.write(b'\xcf\xb8\x8c\xeb')  # 0xcfb88ceb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.face_light_constant_attenuation_scalar))

        data.write(b'^8\x8d\xd0')  # 0x5e388dd0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.face_light_linear_attenuation_scalar))

        data.write(b'\x86\xbc\x05^')  # 0x86bc055e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.face_light_quadratic_attenuation_scalar))

        data.write(b',A#q')  # 0x2c412371
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2c412371))

        data.write(b':\xaf*\x8c')  # 0x3aaf2a8c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3aaf2a8c))

        data.write(b'\xb5\x15\xdd\x12')  # 0xb515dd12
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flash_pass_magnitude_constant))

        data.write(b'\xa9I\xb07')  # 0xa949b037
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flash_pass_magnitude_linear))

        data.write(b'\xca\x9d@\x1c')  # 0xca9d401c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flash_pass_timer_constant))

        data.write(b'\x81\x86\xe8\xfe')  # 0x8186e8fe
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flash_pass_timer_linear))

        data.write(b'\x02\xa2\x19\x8a')  # 0x2a2198a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.metroid_suck_pulse_cycle_time))

        data.write(b'\x8bd\xdcD')  # 0x8b64dc44
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.metroid_suck_is_use_sine_wave))

        data.write(b'qaDk')  # 0x7161446b
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.metroid_suck_is_additive))

        data.write(b'\xaa\xff\x92$')  # 0xaaff9224
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xaaff9224))

        data.write(b'\xfaJ\x83l')  # 0xfa4a836c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xfa4a836c))

        data.write(b'#f\x1bO')  # 0x23661b4f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x23661b4f))

        data.write(b'\x99+dz')  # 0x992b647a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x992b647a))

        data.write(b'\x92\x9d\x08\xcf')  # 0x929d08cf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x929d08cf))

        data.write(b'\xff\xeb\xa1\xf2')  # 0xffeba1f2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_panel_z_rotation_degrees))

        data.write(b'\x13eO ')  # 0x13654f20
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_panel_scale_x))

        data.write(b'p\x83\xfa\xf0')  # 0x7083faf0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_panel_zoomed_position))

        data.write(b'(E\x92<')  # 0x2845923c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2845923c))

        data.write(b'\xebj\x7f*')  # 0xeb6a7f2a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_panel_translate_time))

        data.write(b'\xd0^\xb2z')  # 0xd05eb27a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_window_zoom_time))

        data.write(b'\x8bf\x82\r')  # 0x8b66820d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_panel_flash_magnitude))

        data.write(b'\x13\x8f\x11\x04')  # 0x138f1104
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_panel_flash_ramp_up_time))

        data.write(b'\xd0\xd1v\x0e')  # 0xd0d1760e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_panel_flash_ramp_down_time))

        data.write(b'\xce\x9fWp')  # 0xce9f5770
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_object_model_scale))

        data.write(b'\xea\xf1}E')  # 0xeaf17d45
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.scan_object_translate_transition_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd8\x157\xb6')  # 0xd81537b6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.scan_object_rotation_transition_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b';\xa8ER')  # 0x3ba84552
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.scan_object_scale_transition_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xee\xb7\x83\x9b')  # 0xeeb7839b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xeeb7839b))

        data.write(b'$\xcf\x17\x19')  # 0x24cf1719
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_window_idle_width_scale))

        data.write(b'\xa4\xad\xf6\xea')  # 0xa4adf6ea
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_window_idle_height_scale))

        data.write(b'\xe3u]\xda')  # 0xe3755dda
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_window_zoomed_width_scale))

        data.write(b'\xa6\x07\xdf\xaa')  # 0xa607dfaa
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_window_zoomed_height_scale))

        data.write(b'\xf5\xf7\xa7H')  # 0xf5f7a748
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_window_idle_zoom_factor))

        data.write(b'a!VC')  # 0x61215643
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_window_locked_zoom_factor))

        data.write(b'\xa3\xf4\t^')  # 0xa3f4095e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_panel_idle_position))

        data.write(b'q\x03\xca\x90')  # 0x7103ca90
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x7103ca90))

        data.write(b'"\xd4\xc6\xa3')  # 0x22d4c6a3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x22d4c6a3))

        data.write(b'\xf0\x8c~P')  # 0xf08c7e50
        data.write(b'\x00\x10')  # size
        self.helmet_base_ambient_color_combat.to_stream(data, game)

        data.write(b'\x80\x9bH\r')  # 0x809b480d
        data.write(b'\x00\x10')  # size
        self.helmet_base_ambient_color_scan.to_stream(data, game)

        data.write(b'8\x80K\xeb')  # 0x38804beb
        data.write(b'\x00\x10')  # size
        self.helmet_base_ambient_color_command.to_stream(data, game)

        data.write(b'Uz\xb7\x10')  # 0x557ab710
        data.write(b'\x00\x10')  # size
        self.helmet_base_ambient_color_x_ray.to_stream(data, game)

        data.write(b'\xc2\x9bp\x93')  # 0xc29b7093
        data.write(b'\x00\x10')  # size
        self.helmet_light_ambient_mod_combat.to_stream(data, game)

        data.write(b'X.\xfd;')  # 0x582efd3b
        data.write(b'\x00\x10')  # size
        self.helmet_light_ambient_mod_scan.to_stream(data, game)

        data.write(b':\xdf\xcf\xef')  # 0x3adfcfef
        data.write(b'\x00\x10')  # size
        self.helmet_light_ambient_mod_command.to_stream(data, game)

        data.write(b'\x8d\xcf\x02&')  # 0x8dcf0226
        data.write(b'\x00\x10')  # size
        self.helmet_light_ambient_mod_x_ray.to_stream(data, game)

        data.write(b'pc\x8e\xaa')  # 0x70638eaa
        data.write(b'\x00\x10')  # size
        self.unknown_0x70638eaa.to_stream(data, game)

        data.write(b'[\x88\x802')  # 0x5b888032
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.helmet_light_constant_attenuation_scalar))

        data.write(b'\xb72-&')  # 0xb7322d26
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.helmet_light_linear_attenuation_scalar))

        data.write(b'y\'_"')  # 0x79275f22
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.helmet_light_quadratic_attenuation_scalar))

        data.write(b'\xa9b\x0cE')  # 0xa9620c45
        data.write(b'\x00\x10')  # size
        self.ift_light_color.to_stream(data, game)

        data.write(b'q\x89\xc8>')  # 0x7189c83e
        data.write(b'\x00\x0c')  # size
        self.ift_light_location.to_stream(data, game)

        data.write(b'\xe7\x12`\x99')  # 0xe7126099
        data.write(b'\x00\x10')  # size
        self.ift_ambient_color.to_stream(data, game)

        data.write(b'\x93J$\x7f')  # 0x934a247f
        data.write(b'\x00\x10')  # size
        self.ift_background_color.to_stream(data, game)

        data.write(b'\x050\xa8F')  # 0x530a846
        data.write(b'\x00\x10')  # size
        self.ift_audio_visual_color.to_stream(data, game)

        data.write(b'\xc4\xd89\xf4')  # 0xc4d839f4
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.unknown_0xc4d839f4.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'xR\x1a\xdd')  # 0x78521add
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.unknown_0x78521add.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb4\x0cj;')  # 0xb40c6a3b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb40c6a3b))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGui_MiscJson", data)
        return cls(
            skip_front_end=json_data['skip_front_end'],
            min_hud_alpha=json_data['min_hud_alpha'],
            unknown_0x744165c4=json_data['unknown_0x744165c4'],
            radar_world_radius=json_data['radar_world_radius'],
            unknown_0xa585c592=json_data['unknown_0xa585c592'],
            unknown_0x04f4a6fe=json_data['unknown_0x04f4a6fe'],
            unknown_0x3c327181=json_data['unknown_0x3c327181'],
            unknown_0xa581be26=json_data['unknown_0xa581be26'],
            radar_world_half_height=json_data['radar_world_half_height'],
            unknown_0x889ef9ea=json_data['unknown_0x889ef9ea'],
            energy_bar_low_threshold=json_data['energy_bar_low_threshold'],
            energy_bar_filled_drain_speed=json_data['energy_bar_filled_drain_speed'],
            energy_bar_shadow_drain_speed=json_data['energy_bar_shadow_drain_speed'],
            energy_bar_shadow_drain_delay=json_data['energy_bar_shadow_drain_delay'],
            unknown_0x2821bbca=json_data['unknown_0x2821bbca'],
            hud_flash_magnitude_constant=json_data['hud_flash_magnitude_constant'],
            hud_flash_magnitude_linear=json_data['hud_flash_magnitude_linear'],
            hud_flash_time_constant=json_data['hud_flash_time_constant'],
            hud_flash_time_scale_linear=json_data['hud_flash_time_scale_linear'],
            hud_damage_indicator_radius=json_data['hud_damage_indicator_radius'],
            unknown_0x55b323e5=json_data['unknown_0x55b323e5'],
            unknown_0x411a705e=json_data['unknown_0x411a705e'],
            unknown_0x0a9d701d=json_data['unknown_0x0a9d701d'],
            unknown_0xf4a8e8ea=json_data['unknown_0xf4a8e8ea'],
            unknown_0x50812f49=Vector.from_json(json_data['unknown_0x50812f49']),
            unknown_0x7edc2474=Vector.from_json(json_data['unknown_0x7edc2474']),
            unknown_0x4f0d651c=json_data['unknown_0x4f0d651c'],
            unknown_0x85c31390=json_data['unknown_0x85c31390'],
            hud_damage_jostle_magnitude_constant=json_data['hud_damage_jostle_magnitude_constant'],
            hud_damage_jostle_magnitude_linear=json_data['hud_damage_jostle_magnitude_linear'],
            hud_damage_jostle_max_offset=json_data['hud_damage_jostle_max_offset'],
            hud_damage_jostle_return_acceleration=json_data['hud_damage_jostle_return_acceleration'],
            hud_damage_distortion_magnitude_constant=json_data['hud_damage_distortion_magnitude_constant'],
            hud_damage_distortion_magnitude_linear=json_data['hud_damage_distortion_magnitude_linear'],
            hud_damage_distortion_time_constant=json_data['hud_damage_distortion_time_constant'],
            hud_damage_distortion_time_linear=json_data['hud_damage_distortion_time_linear'],
            hud_damage_distortion_max_magnitude=json_data['hud_damage_distortion_max_magnitude'],
            unknown_0x705ed5cb=json_data['unknown_0x705ed5cb'],
            unknown_0x8922af69=json_data['unknown_0x8922af69'],
            unknown_0x9b970087=json_data['unknown_0x9b970087'],
            lag_type=json_data['lag_type'],
            unknown_0x4dd9d6d1=json_data['unknown_0x4dd9d6d1'],
            unknown_0xad4d37cd=json_data['unknown_0xad4d37cd'],
            unknown_0x95c78e5d=json_data['unknown_0x95c78e5d'],
            threat_world_radius=json_data['threat_world_radius'],
            unknown_0x78174d4b=json_data['unknown_0x78174d4b'],
            unknown_0x3cb2115b=json_data['unknown_0x3cb2115b'],
            unknown_0xfc30bb21=json_data['unknown_0xfc30bb21'],
            missile_arrow_fade_time=json_data['missile_arrow_fade_time'],
            unknown_0xf3565ff4=json_data['unknown_0xf3565ff4'],
            unknown_0x7d3c03eb=json_data['unknown_0x7d3c03eb'],
            unknown_0x72d4d899=json_data['unknown_0x72d4d899'],
            unknown_0xfb9a4cc7=json_data['unknown_0xfb9a4cc7'],
            unknown_0xa1417b38=json_data['unknown_0xa1417b38'],
            unknown_0x71b207b4=json_data['unknown_0x71b207b4'],
            missile_warning_threshold=json_data['missile_warning_threshold'],
            unknown_0xdecc7bff=json_data['unknown_0xdecc7bff'],
            free_look_tick_up_speed=json_data['free_look_tick_up_speed'],
            free_look_tick_down_speed=json_data['free_look_tick_down_speed'],
            free_look_sound_pitch_magnitude=json_data['free_look_sound_pitch_magnitude'],
            unknown_0x4ee9c251=json_data['unknown_0x4ee9c251'],
            unknown_0xa71e83d5=json_data['unknown_0xa71e83d5'],
            unknown_0x3652ef32=json_data['unknown_0x3652ef32'],
            unknown_0x4ff930a5=json_data['unknown_0x4ff930a5'],
            unknown_0x1c106df3=json_data['unknown_0x1c106df3'],
            unknown_0xdaadf917=json_data['unknown_0xdaadf917'],
            unknown_0xe3d55457=json_data['unknown_0xe3d55457'],
            unknown_0xdd39f60a=json_data['unknown_0xdd39f60a'],
            unknown_0x9916df1c=json_data['unknown_0x9916df1c'],
            threat_warning_message=json_data['threat_warning_message'],
            threat_damage_message=json_data['threat_damage_message'],
            energy_warning_message=json_data['energy_warning_message'],
            missile_warning_message=json_data['missile_warning_message'],
            missile_empty_warning=json_data['missile_empty_warning'],
            missile_warning_fade_time=json_data['missile_warning_fade_time'],
            face_light_constant_attenuation_scalar=json_data['face_light_constant_attenuation_scalar'],
            face_light_linear_attenuation_scalar=json_data['face_light_linear_attenuation_scalar'],
            face_light_quadratic_attenuation_scalar=json_data['face_light_quadratic_attenuation_scalar'],
            unknown_0x2c412371=json_data['unknown_0x2c412371'],
            unknown_0x3aaf2a8c=json_data['unknown_0x3aaf2a8c'],
            flash_pass_magnitude_constant=json_data['flash_pass_magnitude_constant'],
            flash_pass_magnitude_linear=json_data['flash_pass_magnitude_linear'],
            flash_pass_timer_constant=json_data['flash_pass_timer_constant'],
            flash_pass_timer_linear=json_data['flash_pass_timer_linear'],
            metroid_suck_pulse_cycle_time=json_data['metroid_suck_pulse_cycle_time'],
            metroid_suck_is_use_sine_wave=json_data['metroid_suck_is_use_sine_wave'],
            metroid_suck_is_additive=json_data['metroid_suck_is_additive'],
            unknown_0xaaff9224=json_data['unknown_0xaaff9224'],
            unknown_0xfa4a836c=json_data['unknown_0xfa4a836c'],
            unknown_0x23661b4f=json_data['unknown_0x23661b4f'],
            unknown_0x992b647a=json_data['unknown_0x992b647a'],
            unknown_0x929d08cf=json_data['unknown_0x929d08cf'],
            scan_panel_z_rotation_degrees=json_data['scan_panel_z_rotation_degrees'],
            scan_panel_scale_x=json_data['scan_panel_scale_x'],
            scan_panel_zoomed_position=json_data['scan_panel_zoomed_position'],
            unknown_0x2845923c=json_data['unknown_0x2845923c'],
            scan_panel_translate_time=json_data['scan_panel_translate_time'],
            scan_window_zoom_time=json_data['scan_window_zoom_time'],
            scan_panel_flash_magnitude=json_data['scan_panel_flash_magnitude'],
            scan_panel_flash_ramp_up_time=json_data['scan_panel_flash_ramp_up_time'],
            scan_panel_flash_ramp_down_time=json_data['scan_panel_flash_ramp_down_time'],
            scan_object_model_scale=json_data['scan_object_model_scale'],
            scan_object_translate_transition_spline=Spline.from_json(json_data['scan_object_translate_transition_spline']),
            scan_object_rotation_transition_spline=Spline.from_json(json_data['scan_object_rotation_transition_spline']),
            scan_object_scale_transition_spline=Spline.from_json(json_data['scan_object_scale_transition_spline']),
            unknown_0xeeb7839b=json_data['unknown_0xeeb7839b'],
            scan_window_idle_width_scale=json_data['scan_window_idle_width_scale'],
            scan_window_idle_height_scale=json_data['scan_window_idle_height_scale'],
            scan_window_zoomed_width_scale=json_data['scan_window_zoomed_width_scale'],
            scan_window_zoomed_height_scale=json_data['scan_window_zoomed_height_scale'],
            scan_window_idle_zoom_factor=json_data['scan_window_idle_zoom_factor'],
            scan_window_locked_zoom_factor=json_data['scan_window_locked_zoom_factor'],
            scan_panel_idle_position=json_data['scan_panel_idle_position'],
            unknown_0x7103ca90=json_data['unknown_0x7103ca90'],
            unknown_0x22d4c6a3=json_data['unknown_0x22d4c6a3'],
            helmet_base_ambient_color_combat=Color.from_json(json_data['helmet_base_ambient_color_combat']),
            helmet_base_ambient_color_scan=Color.from_json(json_data['helmet_base_ambient_color_scan']),
            helmet_base_ambient_color_command=Color.from_json(json_data['helmet_base_ambient_color_command']),
            helmet_base_ambient_color_x_ray=Color.from_json(json_data['helmet_base_ambient_color_x_ray']),
            helmet_light_ambient_mod_combat=Color.from_json(json_data['helmet_light_ambient_mod_combat']),
            helmet_light_ambient_mod_scan=Color.from_json(json_data['helmet_light_ambient_mod_scan']),
            helmet_light_ambient_mod_command=Color.from_json(json_data['helmet_light_ambient_mod_command']),
            helmet_light_ambient_mod_x_ray=Color.from_json(json_data['helmet_light_ambient_mod_x_ray']),
            unknown_0x70638eaa=Color.from_json(json_data['unknown_0x70638eaa']),
            helmet_light_constant_attenuation_scalar=json_data['helmet_light_constant_attenuation_scalar'],
            helmet_light_linear_attenuation_scalar=json_data['helmet_light_linear_attenuation_scalar'],
            helmet_light_quadratic_attenuation_scalar=json_data['helmet_light_quadratic_attenuation_scalar'],
            ift_light_color=Color.from_json(json_data['ift_light_color']),
            ift_light_location=Vector.from_json(json_data['ift_light_location']),
            ift_ambient_color=Color.from_json(json_data['ift_ambient_color']),
            ift_background_color=Color.from_json(json_data['ift_background_color']),
            ift_audio_visual_color=Color.from_json(json_data['ift_audio_visual_color']),
            unknown_0xc4d839f4=TweakGui_Misc_UnknownStruct1.from_json(json_data['unknown_0xc4d839f4']),
            unknown_0x78521add=TweakGui_Misc_UnknownStruct1.from_json(json_data['unknown_0x78521add']),
            unknown_0xb40c6a3b=json_data['unknown_0xb40c6a3b'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'skip_front_end': self.skip_front_end,
            'min_hud_alpha': self.min_hud_alpha,
            'unknown_0x744165c4': self.unknown_0x744165c4,
            'radar_world_radius': self.radar_world_radius,
            'unknown_0xa585c592': self.unknown_0xa585c592,
            'unknown_0x04f4a6fe': self.unknown_0x04f4a6fe,
            'unknown_0x3c327181': self.unknown_0x3c327181,
            'unknown_0xa581be26': self.unknown_0xa581be26,
            'radar_world_half_height': self.radar_world_half_height,
            'unknown_0x889ef9ea': self.unknown_0x889ef9ea,
            'energy_bar_low_threshold': self.energy_bar_low_threshold,
            'energy_bar_filled_drain_speed': self.energy_bar_filled_drain_speed,
            'energy_bar_shadow_drain_speed': self.energy_bar_shadow_drain_speed,
            'energy_bar_shadow_drain_delay': self.energy_bar_shadow_drain_delay,
            'unknown_0x2821bbca': self.unknown_0x2821bbca,
            'hud_flash_magnitude_constant': self.hud_flash_magnitude_constant,
            'hud_flash_magnitude_linear': self.hud_flash_magnitude_linear,
            'hud_flash_time_constant': self.hud_flash_time_constant,
            'hud_flash_time_scale_linear': self.hud_flash_time_scale_linear,
            'hud_damage_indicator_radius': self.hud_damage_indicator_radius,
            'unknown_0x55b323e5': self.unknown_0x55b323e5,
            'unknown_0x411a705e': self.unknown_0x411a705e,
            'unknown_0x0a9d701d': self.unknown_0x0a9d701d,
            'unknown_0xf4a8e8ea': self.unknown_0xf4a8e8ea,
            'unknown_0x50812f49': self.unknown_0x50812f49.to_json(),
            'unknown_0x7edc2474': self.unknown_0x7edc2474.to_json(),
            'unknown_0x4f0d651c': self.unknown_0x4f0d651c,
            'unknown_0x85c31390': self.unknown_0x85c31390,
            'hud_damage_jostle_magnitude_constant': self.hud_damage_jostle_magnitude_constant,
            'hud_damage_jostle_magnitude_linear': self.hud_damage_jostle_magnitude_linear,
            'hud_damage_jostle_max_offset': self.hud_damage_jostle_max_offset,
            'hud_damage_jostle_return_acceleration': self.hud_damage_jostle_return_acceleration,
            'hud_damage_distortion_magnitude_constant': self.hud_damage_distortion_magnitude_constant,
            'hud_damage_distortion_magnitude_linear': self.hud_damage_distortion_magnitude_linear,
            'hud_damage_distortion_time_constant': self.hud_damage_distortion_time_constant,
            'hud_damage_distortion_time_linear': self.hud_damage_distortion_time_linear,
            'hud_damage_distortion_max_magnitude': self.hud_damage_distortion_max_magnitude,
            'unknown_0x705ed5cb': self.unknown_0x705ed5cb,
            'unknown_0x8922af69': self.unknown_0x8922af69,
            'unknown_0x9b970087': self.unknown_0x9b970087,
            'lag_type': self.lag_type,
            'unknown_0x4dd9d6d1': self.unknown_0x4dd9d6d1,
            'unknown_0xad4d37cd': self.unknown_0xad4d37cd,
            'unknown_0x95c78e5d': self.unknown_0x95c78e5d,
            'threat_world_radius': self.threat_world_radius,
            'unknown_0x78174d4b': self.unknown_0x78174d4b,
            'unknown_0x3cb2115b': self.unknown_0x3cb2115b,
            'unknown_0xfc30bb21': self.unknown_0xfc30bb21,
            'missile_arrow_fade_time': self.missile_arrow_fade_time,
            'unknown_0xf3565ff4': self.unknown_0xf3565ff4,
            'unknown_0x7d3c03eb': self.unknown_0x7d3c03eb,
            'unknown_0x72d4d899': self.unknown_0x72d4d899,
            'unknown_0xfb9a4cc7': self.unknown_0xfb9a4cc7,
            'unknown_0xa1417b38': self.unknown_0xa1417b38,
            'unknown_0x71b207b4': self.unknown_0x71b207b4,
            'missile_warning_threshold': self.missile_warning_threshold,
            'unknown_0xdecc7bff': self.unknown_0xdecc7bff,
            'free_look_tick_up_speed': self.free_look_tick_up_speed,
            'free_look_tick_down_speed': self.free_look_tick_down_speed,
            'free_look_sound_pitch_magnitude': self.free_look_sound_pitch_magnitude,
            'unknown_0x4ee9c251': self.unknown_0x4ee9c251,
            'unknown_0xa71e83d5': self.unknown_0xa71e83d5,
            'unknown_0x3652ef32': self.unknown_0x3652ef32,
            'unknown_0x4ff930a5': self.unknown_0x4ff930a5,
            'unknown_0x1c106df3': self.unknown_0x1c106df3,
            'unknown_0xdaadf917': self.unknown_0xdaadf917,
            'unknown_0xe3d55457': self.unknown_0xe3d55457,
            'unknown_0xdd39f60a': self.unknown_0xdd39f60a,
            'unknown_0x9916df1c': self.unknown_0x9916df1c,
            'threat_warning_message': self.threat_warning_message,
            'threat_damage_message': self.threat_damage_message,
            'energy_warning_message': self.energy_warning_message,
            'missile_warning_message': self.missile_warning_message,
            'missile_empty_warning': self.missile_empty_warning,
            'missile_warning_fade_time': self.missile_warning_fade_time,
            'face_light_constant_attenuation_scalar': self.face_light_constant_attenuation_scalar,
            'face_light_linear_attenuation_scalar': self.face_light_linear_attenuation_scalar,
            'face_light_quadratic_attenuation_scalar': self.face_light_quadratic_attenuation_scalar,
            'unknown_0x2c412371': self.unknown_0x2c412371,
            'unknown_0x3aaf2a8c': self.unknown_0x3aaf2a8c,
            'flash_pass_magnitude_constant': self.flash_pass_magnitude_constant,
            'flash_pass_magnitude_linear': self.flash_pass_magnitude_linear,
            'flash_pass_timer_constant': self.flash_pass_timer_constant,
            'flash_pass_timer_linear': self.flash_pass_timer_linear,
            'metroid_suck_pulse_cycle_time': self.metroid_suck_pulse_cycle_time,
            'metroid_suck_is_use_sine_wave': self.metroid_suck_is_use_sine_wave,
            'metroid_suck_is_additive': self.metroid_suck_is_additive,
            'unknown_0xaaff9224': self.unknown_0xaaff9224,
            'unknown_0xfa4a836c': self.unknown_0xfa4a836c,
            'unknown_0x23661b4f': self.unknown_0x23661b4f,
            'unknown_0x992b647a': self.unknown_0x992b647a,
            'unknown_0x929d08cf': self.unknown_0x929d08cf,
            'scan_panel_z_rotation_degrees': self.scan_panel_z_rotation_degrees,
            'scan_panel_scale_x': self.scan_panel_scale_x,
            'scan_panel_zoomed_position': self.scan_panel_zoomed_position,
            'unknown_0x2845923c': self.unknown_0x2845923c,
            'scan_panel_translate_time': self.scan_panel_translate_time,
            'scan_window_zoom_time': self.scan_window_zoom_time,
            'scan_panel_flash_magnitude': self.scan_panel_flash_magnitude,
            'scan_panel_flash_ramp_up_time': self.scan_panel_flash_ramp_up_time,
            'scan_panel_flash_ramp_down_time': self.scan_panel_flash_ramp_down_time,
            'scan_object_model_scale': self.scan_object_model_scale,
            'scan_object_translate_transition_spline': self.scan_object_translate_transition_spline.to_json(),
            'scan_object_rotation_transition_spline': self.scan_object_rotation_transition_spline.to_json(),
            'scan_object_scale_transition_spline': self.scan_object_scale_transition_spline.to_json(),
            'unknown_0xeeb7839b': self.unknown_0xeeb7839b,
            'scan_window_idle_width_scale': self.scan_window_idle_width_scale,
            'scan_window_idle_height_scale': self.scan_window_idle_height_scale,
            'scan_window_zoomed_width_scale': self.scan_window_zoomed_width_scale,
            'scan_window_zoomed_height_scale': self.scan_window_zoomed_height_scale,
            'scan_window_idle_zoom_factor': self.scan_window_idle_zoom_factor,
            'scan_window_locked_zoom_factor': self.scan_window_locked_zoom_factor,
            'scan_panel_idle_position': self.scan_panel_idle_position,
            'unknown_0x7103ca90': self.unknown_0x7103ca90,
            'unknown_0x22d4c6a3': self.unknown_0x22d4c6a3,
            'helmet_base_ambient_color_combat': self.helmet_base_ambient_color_combat.to_json(),
            'helmet_base_ambient_color_scan': self.helmet_base_ambient_color_scan.to_json(),
            'helmet_base_ambient_color_command': self.helmet_base_ambient_color_command.to_json(),
            'helmet_base_ambient_color_x_ray': self.helmet_base_ambient_color_x_ray.to_json(),
            'helmet_light_ambient_mod_combat': self.helmet_light_ambient_mod_combat.to_json(),
            'helmet_light_ambient_mod_scan': self.helmet_light_ambient_mod_scan.to_json(),
            'helmet_light_ambient_mod_command': self.helmet_light_ambient_mod_command.to_json(),
            'helmet_light_ambient_mod_x_ray': self.helmet_light_ambient_mod_x_ray.to_json(),
            'unknown_0x70638eaa': self.unknown_0x70638eaa.to_json(),
            'helmet_light_constant_attenuation_scalar': self.helmet_light_constant_attenuation_scalar,
            'helmet_light_linear_attenuation_scalar': self.helmet_light_linear_attenuation_scalar,
            'helmet_light_quadratic_attenuation_scalar': self.helmet_light_quadratic_attenuation_scalar,
            'ift_light_color': self.ift_light_color.to_json(),
            'ift_light_location': self.ift_light_location.to_json(),
            'ift_ambient_color': self.ift_ambient_color.to_json(),
            'ift_background_color': self.ift_background_color.to_json(),
            'ift_audio_visual_color': self.ift_audio_visual_color.to_json(),
            'unknown_0xc4d839f4': self.unknown_0xc4d839f4.to_json(),
            'unknown_0x78521add': self.unknown_0x78521add.to_json(),
            'unknown_0xb40c6a3b': self.unknown_0xb40c6a3b,
        }


def _decode_unknown_0x50812f49(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_unknown_0x7edc2474(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_threat_warning_message(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_threat_damage_message(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_energy_warning_message(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_missile_warning_message(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_missile_empty_warning(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_scan_object_translate_transition_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_scan_object_rotation_transition_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_scan_object_scale_transition_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_helmet_base_ambient_color_combat(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_helmet_base_ambient_color_scan(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_helmet_base_ambient_color_command(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_helmet_base_ambient_color_x_ray(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_helmet_light_ambient_mod_combat(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_helmet_light_ambient_mod_scan(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_helmet_light_ambient_mod_command(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_helmet_light_ambient_mod_x_ray(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x70638eaa(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_ift_light_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_ift_light_location(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_ift_ambient_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_ift_background_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_ift_audio_visual_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xc4d839f4(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_Misc_UnknownStruct1:
    return TweakGui_Misc_UnknownStruct1.from_stream(data, game, property_size)


def _decode_unknown_0x78521add(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_Misc_UnknownStruct1:
    return TweakGui_Misc_UnknownStruct1.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x2f9d48b8: ('skip_front_end', structs.decode_BIG_bool_),
    0x71b475d0: ('min_hud_alpha', structs.decode_BIG_f),
    0x744165c4: ('unknown_0x744165c4', structs.decode_BIG_f),
    0xee1ba439: ('radar_world_radius', structs.decode_BIG_f),
    0xa585c592: ('unknown_0xa585c592', structs.decode_BIG_f),
    0x04f4a6fe: ('unknown_0x04f4a6fe', structs.decode_BIG_f),
    0x3c327181: ('unknown_0x3c327181', structs.decode_BIG_f),
    0xa581be26: ('unknown_0xa581be26', structs.decode_BIG_f),
    0x68d88e25: ('radar_world_half_height', structs.decode_BIG_f),
    0x889ef9ea: ('unknown_0x889ef9ea', structs.decode_BIG_f),
    0xb68ff81a: ('energy_bar_low_threshold', structs.decode_BIG_f),
    0x04510638: ('energy_bar_filled_drain_speed', structs.decode_BIG_f),
    0x7a48c3b1: ('energy_bar_shadow_drain_speed', structs.decode_BIG_f),
    0x0d257063: ('energy_bar_shadow_drain_delay', structs.decode_BIG_f),
    0x2821bbca: ('unknown_0x2821bbca', structs.decode_BIG_bool_),
    0xc4dd4d5b: ('hud_flash_magnitude_constant', structs.decode_BIG_f),
    0x6031503e: ('hud_flash_magnitude_linear', structs.decode_BIG_f),
    0x9f5ebba2: ('hud_flash_time_constant', structs.decode_BIG_f),
    0x2930d57f: ('hud_flash_time_scale_linear', structs.decode_BIG_f),
    0x3ac94cf1: ('hud_damage_indicator_radius', structs.decode_BIG_f),
    0x55b323e5: ('unknown_0x55b323e5', structs.decode_BIG_f),
    0x411a705e: ('unknown_0x411a705e', structs.decode_BIG_f),
    0x0a9d701d: ('unknown_0x0a9d701d', structs.decode_BIG_f),
    0xf4a8e8ea: ('unknown_0xf4a8e8ea', structs.decode_BIG_f),
    0x50812f49: ('unknown_0x50812f49', _decode_unknown_0x50812f49),
    0x7edc2474: ('unknown_0x7edc2474', _decode_unknown_0x7edc2474),
    0x4f0d651c: ('unknown_0x4f0d651c', structs.decode_BIG_f),
    0x85c31390: ('unknown_0x85c31390', structs.decode_BIG_f),
    0xb93990e6: ('hud_damage_jostle_magnitude_constant', structs.decode_BIG_f),
    0x4036cdb6: ('hud_damage_jostle_magnitude_linear', structs.decode_BIG_f),
    0xa7cf8baa: ('hud_damage_jostle_max_offset', structs.decode_BIG_f),
    0x3e8e6afd: ('hud_damage_jostle_return_acceleration', structs.decode_BIG_f),
    0xec040d56: ('hud_damage_distortion_magnitude_constant', structs.decode_BIG_f),
    0x236bbe14: ('hud_damage_distortion_magnitude_linear', structs.decode_BIG_f),
    0x19f5c324: ('hud_damage_distortion_time_constant', structs.decode_BIG_f),
    0xfd559f8c: ('hud_damage_distortion_time_linear', structs.decode_BIG_f),
    0xe4702e21: ('hud_damage_distortion_max_magnitude', structs.decode_BIG_f),
    0x705ed5cb: ('unknown_0x705ed5cb', structs.decode_BIG_l),
    0x8922af69: ('unknown_0x8922af69', structs.decode_BIG_l),
    0x9b970087: ('unknown_0x9b970087', structs.decode_BIG_l),
    0xf4ec68ae: ('lag_type', structs.decode_BIG_L),
    0x4dd9d6d1: ('unknown_0x4dd9d6d1', structs.decode_BIG_f),
    0xad4d37cd: ('unknown_0xad4d37cd', structs.decode_BIG_f),
    0x95c78e5d: ('unknown_0x95c78e5d', structs.decode_BIG_f),
    0x1a8dc454: ('threat_world_radius', structs.decode_BIG_f),
    0x78174d4b: ('unknown_0x78174d4b', structs.decode_BIG_f),
    0x3cb2115b: ('unknown_0x3cb2115b', structs.decode_BIG_f),
    0xfc30bb21: ('unknown_0xfc30bb21', structs.decode_BIG_f),
    0x86cdde75: ('missile_arrow_fade_time', structs.decode_BIG_f),
    0xf3565ff4: ('unknown_0xf3565ff4', structs.decode_BIG_l),
    0x7d3c03eb: ('unknown_0x7d3c03eb', structs.decode_BIG_l),
    0x72d4d899: ('unknown_0x72d4d899', structs.decode_BIG_l),
    0xfb9a4cc7: ('unknown_0xfb9a4cc7', structs.decode_BIG_l),
    0xa1417b38: ('unknown_0xa1417b38', structs.decode_BIG_l),
    0x71b207b4: ('unknown_0x71b207b4', structs.decode_BIG_l),
    0x46d75fe1: ('missile_warning_threshold', structs.decode_BIG_f),
    0xdecc7bff: ('unknown_0xdecc7bff', structs.decode_BIG_f),
    0xcbff7b94: ('free_look_tick_up_speed', structs.decode_BIG_f),
    0x0babf93b: ('free_look_tick_down_speed', structs.decode_BIG_f),
    0xc0004f50: ('free_look_sound_pitch_magnitude', structs.decode_BIG_f),
    0x4ee9c251: ('unknown_0x4ee9c251', structs.decode_BIG_bool_),
    0xa71e83d5: ('unknown_0xa71e83d5', structs.decode_BIG_f),
    0x3652ef32: ('unknown_0x3652ef32', structs.decode_BIG_f),
    0x4ff930a5: ('unknown_0x4ff930a5', structs.decode_BIG_l),
    0x1c106df3: ('unknown_0x1c106df3', structs.decode_BIG_l),
    0xdaadf917: ('unknown_0xdaadf917', structs.decode_BIG_l),
    0xe3d55457: ('unknown_0xe3d55457', structs.decode_BIG_l),
    0xdd39f60a: ('unknown_0xdd39f60a', structs.decode_BIG_l),
    0x9916df1c: ('unknown_0x9916df1c', structs.decode_BIG_l),
    0x3db45f6a: ('threat_warning_message', _decode_threat_warning_message),
    0x471f1217: ('threat_damage_message', _decode_threat_damage_message),
    0xf8b84c58: ('energy_warning_message', _decode_energy_warning_message),
    0xbc2c8de6: ('missile_warning_message', _decode_missile_warning_message),
    0x54203510: ('missile_empty_warning', _decode_missile_empty_warning),
    0xcf9fd47e: ('missile_warning_fade_time', structs.decode_BIG_f),
    0xcfb88ceb: ('face_light_constant_attenuation_scalar', structs.decode_BIG_f),
    0x5e388dd0: ('face_light_linear_attenuation_scalar', structs.decode_BIG_f),
    0x86bc055e: ('face_light_quadratic_attenuation_scalar', structs.decode_BIG_f),
    0x2c412371: ('unknown_0x2c412371', structs.decode_BIG_f),
    0x3aaf2a8c: ('unknown_0x3aaf2a8c', structs.decode_BIG_f),
    0xb515dd12: ('flash_pass_magnitude_constant', structs.decode_BIG_f),
    0xa949b037: ('flash_pass_magnitude_linear', structs.decode_BIG_f),
    0xca9d401c: ('flash_pass_timer_constant', structs.decode_BIG_f),
    0x8186e8fe: ('flash_pass_timer_linear', structs.decode_BIG_f),
    0x02a2198a: ('metroid_suck_pulse_cycle_time', structs.decode_BIG_f),
    0x8b64dc44: ('metroid_suck_is_use_sine_wave', structs.decode_BIG_bool_),
    0x7161446b: ('metroid_suck_is_additive', structs.decode_BIG_bool_),
    0xaaff9224: ('unknown_0xaaff9224', structs.decode_BIG_f),
    0xfa4a836c: ('unknown_0xfa4a836c', structs.decode_BIG_f),
    0x23661b4f: ('unknown_0x23661b4f', structs.decode_BIG_f),
    0x992b647a: ('unknown_0x992b647a', structs.decode_BIG_f),
    0x929d08cf: ('unknown_0x929d08cf', structs.decode_BIG_f),
    0xffeba1f2: ('scan_panel_z_rotation_degrees', structs.decode_BIG_f),
    0x13654f20: ('scan_panel_scale_x', structs.decode_BIG_f),
    0x7083faf0: ('scan_panel_zoomed_position', structs.decode_BIG_f),
    0x2845923c: ('unknown_0x2845923c', structs.decode_BIG_f),
    0xeb6a7f2a: ('scan_panel_translate_time', structs.decode_BIG_f),
    0xd05eb27a: ('scan_window_zoom_time', structs.decode_BIG_f),
    0x8b66820d: ('scan_panel_flash_magnitude', structs.decode_BIG_f),
    0x138f1104: ('scan_panel_flash_ramp_up_time', structs.decode_BIG_f),
    0xd0d1760e: ('scan_panel_flash_ramp_down_time', structs.decode_BIG_f),
    0xce9f5770: ('scan_object_model_scale', structs.decode_BIG_f),
    0xeaf17d45: ('scan_object_translate_transition_spline', _decode_scan_object_translate_transition_spline),
    0xd81537b6: ('scan_object_rotation_transition_spline', _decode_scan_object_rotation_transition_spline),
    0x3ba84552: ('scan_object_scale_transition_spline', _decode_scan_object_scale_transition_spline),
    0xeeb7839b: ('unknown_0xeeb7839b', structs.decode_BIG_f),
    0x24cf1719: ('scan_window_idle_width_scale', structs.decode_BIG_f),
    0xa4adf6ea: ('scan_window_idle_height_scale', structs.decode_BIG_f),
    0xe3755dda: ('scan_window_zoomed_width_scale', structs.decode_BIG_f),
    0xa607dfaa: ('scan_window_zoomed_height_scale', structs.decode_BIG_f),
    0xf5f7a748: ('scan_window_idle_zoom_factor', structs.decode_BIG_f),
    0x61215643: ('scan_window_locked_zoom_factor', structs.decode_BIG_f),
    0xa3f4095e: ('scan_panel_idle_position', structs.decode_BIG_f),
    0x7103ca90: ('unknown_0x7103ca90', structs.decode_BIG_bool_),
    0x22d4c6a3: ('unknown_0x22d4c6a3', structs.decode_BIG_f),
    0xf08c7e50: ('helmet_base_ambient_color_combat', _decode_helmet_base_ambient_color_combat),
    0x809b480d: ('helmet_base_ambient_color_scan', _decode_helmet_base_ambient_color_scan),
    0x38804beb: ('helmet_base_ambient_color_command', _decode_helmet_base_ambient_color_command),
    0x557ab710: ('helmet_base_ambient_color_x_ray', _decode_helmet_base_ambient_color_x_ray),
    0xc29b7093: ('helmet_light_ambient_mod_combat', _decode_helmet_light_ambient_mod_combat),
    0x582efd3b: ('helmet_light_ambient_mod_scan', _decode_helmet_light_ambient_mod_scan),
    0x3adfcfef: ('helmet_light_ambient_mod_command', _decode_helmet_light_ambient_mod_command),
    0x8dcf0226: ('helmet_light_ambient_mod_x_ray', _decode_helmet_light_ambient_mod_x_ray),
    0x70638eaa: ('unknown_0x70638eaa', _decode_unknown_0x70638eaa),
    0x5b888032: ('helmet_light_constant_attenuation_scalar', structs.decode_BIG_f),
    0xb7322d26: ('helmet_light_linear_attenuation_scalar', structs.decode_BIG_f),
    0x79275f22: ('helmet_light_quadratic_attenuation_scalar', structs.decode_BIG_f),
    0xa9620c45: ('ift_light_color', _decode_ift_light_color),
    0x7189c83e: ('ift_light_location', _decode_ift_light_location),
    0xe7126099: ('ift_ambient_color', _decode_ift_ambient_color),
    0x934a247f: ('ift_background_color', _decode_ift_background_color),
    0x0530a846: ('ift_audio_visual_color', _decode_ift_audio_visual_color),
    0xc4d839f4: ('unknown_0xc4d839f4', _decode_unknown_0xc4d839f4),
    0x78521add: ('unknown_0x78521add', _decode_unknown_0x78521add),
    0xb40c6a3b: ('unknown_0xb40c6a3b', structs.decode_BIG_f),
}
