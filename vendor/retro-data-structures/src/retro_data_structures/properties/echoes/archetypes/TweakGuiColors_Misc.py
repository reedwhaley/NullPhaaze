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

if typing.TYPE_CHECKING:
    class TweakGuiColors_MiscJson(typing_extensions.TypedDict):
        pause_screen_bg_modulate_color: json_util.JsonValue
        radar_boundary_ring_color: json_util.JsonValue
        radar_player_paint_color: json_util.JsonValue
        radar_enemy_paint_color: json_util.JsonValue
        echo_ping_radar_color: json_util.JsonValue
        radar_friend_team_paint_color: json_util.JsonValue
        radar_enemy_team_paint_color: json_util.JsonValue
        hud_memo_text_foreground_color: json_util.JsonValue
        hud_memo_text_outline_color: json_util.JsonValue
        hud_decorative_color: json_util.JsonValue
        hud_glow_color: json_util.JsonValue
        hud_energy_deco_color: json_util.JsonValue
        hud_missile_group_active_color: json_util.JsonValue
        selected_visor_beam_color: json_util.JsonValue
        unselected_visor_beam_color: json_util.JsonValue
        energy_bar_low_filled_color: json_util.JsonValue
        energy_bar_low_shadow_color: json_util.JsonValue
        energy_bar_low_empty_color: json_util.JsonValue
        hud_damage_modulate_color: json_util.JsonValue
        damage_indicator_color: json_util.JsonValue
        hud_title_foreground_color: json_util.JsonValue
        hud_title_outline_color: json_util.JsonValue
        visor_menu_title_foreground_color: json_util.JsonValue
        visor_menu_title_outline_color: json_util.JsonValue
        beam_menu_title_foreground_color: json_util.JsonValue
        beam_menu_title_outline_color: json_util.JsonValue
        visor_beam_menu_icon_selected_color: json_util.JsonValue
        visor_beam_menu_icon_unselected_color: json_util.JsonValue
        visor_menu_icon_color0: json_util.JsonValue
        visor_menu_icon_color1: json_util.JsonValue
        visor_menu_icon_color2: json_util.JsonValue
        visor_menu_icon_color3: json_util.JsonValue
        beam_menu_icon_color0: json_util.JsonValue
        beam_menu_icon_color1: json_util.JsonValue
        beam_menu_icon_color2: json_util.JsonValue
        beam_menu_icon_color3: json_util.JsonValue
        energy_warning_color: json_util.JsonValue
        threat_warning_color: json_util.JsonValue
        missile_warning_color: json_util.JsonValue
        missle_depletion_color: json_util.JsonValue
        threat_bar_filled_color: json_util.JsonValue
        threat_bar_shadow_color: json_util.JsonValue
        threat_bar_empty_color: json_util.JsonValue
        missile_bar_filled_color: json_util.JsonValue
        missile_bar_shadow_color: json_util.JsonValue
        missile_bar_empty_color: json_util.JsonValue
        threat_group_color: json_util.JsonValue
        free_look_bar_color: json_util.JsonValue
        hud_bar_deco_color: json_util.JsonValue
        unknown_0xf4379cf4: json_util.JsonValue
        threat_group_inactive_color: json_util.JsonValue
        missile_group_inactive_color: json_util.JsonValue
        missile_group_combo_charge_color: json_util.JsonValue
        missile_group_non_combo_charge_color: json_util.JsonValue
        missile_group_combo_activated_color: json_util.JsonValue
        free_look_tick_color: json_util.JsonValue
        free_look_digits_foreground_color: json_util.JsonValue
        free_look_digits_outline_color: json_util.JsonValue
        unknown_0x8b0a4c90: json_util.JsonValue
        energy_warning_outline_color: json_util.JsonValue
        threat_warning_outline_color: json_util.JsonValue
        missile_warning_outline_color: json_util.JsonValue
        helmet_light_ambient_color: json_util.JsonValue
        flash_pass_color: json_util.JsonValue
        scan_window_frame_base_color: json_util.JsonValue
        scan_window_frame_active_color: json_util.JsonValue
        scan_window_frame_flash_add_color: json_util.JsonValue
        unknown_0x18717fa7: json_util.JsonValue
        unknown_0x8b7d7378: json_util.JsonValue
        unknown_0x867b01a2: json_util.JsonValue
        scan_hud_hierarchy_frame_color: json_util.JsonValue
        scan_hud_hierarchy_inactive_frame_color: json_util.JsonValue
        scan_hud_hierarchy_text_frame_color: json_util.JsonValue
        scan_hud_hierarchy_final_text_frame_color: json_util.JsonValue
        scan_hud_hierarchy_flash_icon_color: json_util.JsonValue
        scan_hud_hierarchy_complete_flash_icon_color: json_util.JsonValue
        scan_hud_hierarchy_flash_flash_icon_color: json_util.JsonValue
        scan_hud_hierarchy_text_color: json_util.JsonValue
        scan_hud_hierarchy_final_text_color: json_util.JsonValue
        scan_hud_hierarchy_percent_text_color: json_util.JsonValue
        scan_hud_hierarchy_bar_meter_color: json_util.JsonValue
        dark_visor_helmet_light_modulate_color: json_util.JsonValue
        metroid_suck_pulse_color: json_util.JsonValue
        unknown_0xce7c9d8d: json_util.JsonValue
        energy_bar_damage_color: json_util.JsonValue
        x_ray_clamps_color: json_util.JsonValue
        x_ray_holo_grid_color: json_util.JsonValue
        x_ray_seeker_color: json_util.JsonValue
        x_ray_seeker_ticks_color: json_util.JsonValue
        x_ray_seeker_ticks_outer_color: json_util.JsonValue
        x_ray_top_puzzle_color: json_util.JsonValue
        x_ray_bottom_puzzle_color: json_util.JsonValue
        x_ray_left_puzzle_color: json_util.JsonValue
        x_ray_right_puzzle_color: json_util.JsonValue
        x_ray_corner_color: json_util.JsonValue
        x_ray_threat_digits_foreground_color: json_util.JsonValue
        x_ray_threat_digits_outline_color: json_util.JsonValue
        x_ray_missile_digits_foreground_color: json_util.JsonValue
        x_ray_missile_digits_outline_color: json_util.JsonValue
        x_ray_threat_bar_filled_color: json_util.JsonValue
        x_ray_threat_bar_empty_color: json_util.JsonValue
        x_ray_missile_bar_filled_color: json_util.JsonValue
        x_ray_missile_bar_empty_color: json_util.JsonValue
        scan_download_square_color: json_util.JsonValue
        scan_dot_color: json_util.JsonValue
        morph_ball_power_bomb_digits_foreground_color: json_util.JsonValue
        morph_ball_power_bomb_digits_outline_color: json_util.JsonValue
        morph_ball_energy_word_color: json_util.JsonValue
        morph_ball_bomb_counter_filled_color: json_util.JsonValue
        morph_ball_bomb_counter_empty_color: json_util.JsonValue
        morph_ball_power_bomb_icon_color: json_util.JsonValue
        morph_ball_bomb_word_color: json_util.JsonValue
        morph_ball_energy_deco_color: json_util.JsonValue
        morph_ball_bomb_deco_color: json_util.JsonValue
        morph_ball_empty_power_bomb_digits_foreground_colorr: json_util.JsonValue
        morph_ball_empty_power_bomb_digits_outline_color: json_util.JsonValue
        morph_ball_empty_power_bomb_icon_color: json_util.JsonValue
        scan_panel_color: json_util.JsonValue
        unknown_0x96f650c3: json_util.JsonValue
        scan_images_color: json_util.JsonValue
        unknown_0xd3bafaf5: json_util.JsonValue
        threat_group_damage_color: json_util.JsonValue
        coundown_foreground_color: json_util.JsonValue
        coundown_outline_color: json_util.JsonValue
        critical_scan_object_indicator_in_range_color: json_util.JsonValue
        critical_scan_object_indicator_out_of_range_color: json_util.JsonValue
        noncritical_scan_object_indicator_in_range_color: json_util.JsonValue
        noncritical_scan_object_indicator_out_of_range_color: json_util.JsonValue
        scan_seeker_color: json_util.JsonValue
        thermal_threat_digits_outline_color: json_util.JsonValue
        thermal_missile_digits_outline_color: json_util.JsonValue
        combat_missile_digits_foreground_color: json_util.JsonValue
        combat_missile_digits_outline_color: json_util.JsonValue
        thermal_deco_color: json_util.JsonValue
        thermal_deco_outline_color: json_util.JsonValue
        thermal_trackers_color: json_util.JsonValue
        thermal_lock_color: json_util.JsonValue
        log_book_color: json_util.JsonValue
        inventory_equipped_color: json_util.JsonValue
        dark_visor_deco_color: json_util.JsonValue
        light_ammo_tank_full_selected_color: json_util.JsonValue
        light_ammo_tank_full_unselected_color: json_util.JsonValue
        light_ammo_tank_emptyl_selected_color: json_util.JsonValue
        light_ammo_tank_empty_unselected_color: json_util.JsonValue
        light_ammo_meter_selected_fill_color: json_util.JsonValue
        light_ammo_meter_selected_shadow_color: json_util.JsonValue
        light_ammo_meter_unselected_fill_color: json_util.JsonValue
        light_ammo_meter_unselected_shadow_color: json_util.JsonValue
        light_ammo_icon_selected_color: json_util.JsonValue
        light_ammo_icon_unselected_color: json_util.JsonValue
        light_ammo_digits_outline_color: json_util.JsonValue
        light_ammo_digits_selected_color: json_util.JsonValue
        light_ammo_digits_unselected_color: json_util.JsonValue
        light_ammo_change_flash: json_util.JsonValue
        light_ammo_tank_warning_color: json_util.JsonValue
        light_ammo_meter_warning_color: json_util.JsonValue
        light_ammo_digit_warning_color: json_util.JsonValue
        light_ammo_depletion_color: json_util.JsonValue
        light_ammo_empty_tank_warning_color: json_util.JsonValue
        dark_ammo_tank_full_selected_color: json_util.JsonValue
        dark_ammo_tank_full_unselected_color: json_util.JsonValue
        dark_ammo_tank_emptyl_selected_color: json_util.JsonValue
        dark_ammo_tank_empty_unselected_color: json_util.JsonValue
        dark_ammo_meter_selected_fill_color: json_util.JsonValue
        dark_ammo_meter_selected_shadow_color: json_util.JsonValue
        dark_ammo_meter_unselected_fill_color: json_util.JsonValue
        dark_ammo_meter_unselected_shadow_color: json_util.JsonValue
        dark_ammo_icon_selected_color: json_util.JsonValue
        dark_ammo_icon_unselected_color: json_util.JsonValue
        dark_ammo_digits_outline_color: json_util.JsonValue
        dark_ammo_digits_selected_color: json_util.JsonValue
        dark_ammo_digits_unselected_color: json_util.JsonValue
        dark_ammo_change_flash: json_util.JsonValue
        num_huds: int
        dark_ammo_tank_warning_color: json_util.JsonValue
        dark_ammo_meter_warning_color: json_util.JsonValue
        dark_ammo_digit_warning_color: json_util.JsonValue
        dark_ammo_depletion_color: json_util.JsonValue
        dark_ammo_empty_tank_warning_color: json_util.JsonValue
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x8ed04c36, 0x166c22e0, 0xcec78e81, 0x91338f72, 0xd24ae6b, 0xddc561eb, 0x9be28150, 0x2df1eb03, 0xb5da30f4, 0xc8ddc662, 0x6991e2cd, 0x5c336f85, 0xdefca700, 0xcb7ddaf4, 0xf17911aa, 0xa14c8d20, 0xb4135cdd, 0xe0290c48, 0x1ec7f863, 0xae1317d8, 0x22b9b01e, 0x70a2cd6e, 0xe7070332, 0x779c7b9c, 0x13bd3b64, 0x1531edd3, 0x27d0c234, 0xbaa6d6a1, 0x59e416aa, 0x92b8c50f, 0x142cb7a1, 0xdf706404, 0x81269ee0, 0x4a7a4d45, 0xccee3feb, 0x7b2ec4e, 0x6f6e9d6d, 0xca68f68f, 0xc00a29f, 0x83040135, 0x1adea12b, 0xf8170d6, 0x794204fd, 0x3c1ae0ff, 0x29453102, 0x64337ccd, 0x4b86c539, 0xa6609cc5, 0xbe3c29a1, 0xf4379cf4, 0x74e5ffa1, 0xd110a12f, 0xceb17cdf, 0x4c5aff4f, 0xb17b693, 0xfad063d5, 0x2eafedf7, 0x2a01734f, 0x8b0a4c90, 0xc4e17ca8, 0xc7182898, 0xcdbd73e1, 0x78522461, 0x6a839a97, 0x79ea6f12, 0xdc901206, 0xc54fa7bc, 0x18717fa7, 0x8b7d7378, 0x867b01a2, 0x8be8347, 0xe6ec3c8d, 0x591cd695, 0x26e1eb8c, 0x63e9e374, 0x738d9c43, 0xba6c75a2, 0xc37d11b7, 0xef1ec40e, 0xca7beb2, 0x87d3ce8a, 0xeb7eb756, 0xe4c1bbeb, 0xce7c9d8d, 0x13490420, 0xafe2d45d, 0x2af5aa06, 0xd3cbe846, 0x507b51da, 0xc61d97ef, 0xaf0001cf, 0x150a9b17, 0xd66d715f, 0xa8698fe8, 0x4cb38e71, 0x51c5aad9, 0x60e8322b, 0xa947a67c, 0x421bae2a, 0xf0049167, 0x76357179, 0x439a3774, 0x8ee94c81, 0xbb0897ea, 0xc12cbab9, 0x716e6398, 0xdaca46d4, 0xf37e756, 0xf7283644, 0x37564b7d, 0x66b7eda3, 0xf895098f, 0x9b27be10, 0x6c8550c9, 0x5368a35f, 0x5a807b81, 0xeb63afed, 0x92f59138, 0x96f650c3, 0xabdbfa5b, 0xd3bafaf5, 0xf8b971fa, 0x4f1d443e, 0xf6451da, 0xc1ec3637, 0xb6a61e34, 0xfdcd9589, 0xb0253266, 0x345e5b4e, 0xe8401c5a, 0x659147ae, 0x43ed3310, 0xa781ed1d, 0x35402188, 0x223058b5, 0xe846d37f, 0x8c9f2a1a, 0x1b0f3a85, 0x149369fd, 0x2d5344f, 0xf37f8deb, 0x5a6587df, 0xc18bdc67, 0x4d916bb8, 0x5ba76807, 0xa42f6495, 0x448156ae, 0x1a8b61b8, 0xf36adacb, 0x3aee673f, 0xf9c88b05, 0x3bffe826, 0x19e9738b, 0x9329c6ff, 0xf9e7e0df, 0x4e77411, 0x3c5d7111, 0x42e2dfc1, 0xc758541f, 0xde649e48, 0x5bf10430, 0xc01f5f88, 0x7d2500d2, 0x14558146, 0x949b0fff, 0x74353dc4, 0x5ff96af1, 0x74bb42f, 0xaaf6e9a9, 0x5e5b8c0a, 0xabe766b0, 0x34f26028, 0xa59b3320, 0xbfffe95a, 0xc3c55c9, 0xf0c61af5, 0xc87c1ff5, 0x88936aa2, 0xea4347bc)


@dataclasses.dataclass()
class TweakGuiColors_Misc(BaseProperty):
    pause_screen_bg_modulate_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.7098039984703064, b=0.3960779905319214, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x8ed04c36, original_name='PauseScreenBGModulateColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    radar_boundary_ring_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=0.6274510025978088), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x166c22e0, original_name='RadarBoundaryRingColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    radar_player_paint_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=0.4000000059604645), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xcec78e81, original_name='RadarPlayerPaintColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    radar_enemy_paint_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4039219915866852, b=0.01960800029337406, a=0.784313976764679), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x91338f72, original_name='RadarEnemyPaintColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    echo_ping_radar_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x0d24ae6b, original_name='EchoPingRadarColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    radar_friend_team_paint_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=1.0, a=0.7829999923706055), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xddc561eb, original_name='RadarFriendTeamPaintColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    radar_enemy_team_paint_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.0, b=0.0, a=0.7829999923706055), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x9be28150, original_name='RadarEnemyTeamPaintColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    hud_memo_text_foreground_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.5372549891471863, g=0.8392159938812256, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x2df1eb03, original_name='HUDMemoTextForegroundColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    hud_memo_text_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xb5da30f4, original_name='HUDMemoTextOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    hud_decorative_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=0.6274510025978088), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xc8ddc662, original_name='HUDDecorativeColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    hud_glow_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4078429937362671, b=0.01960800029337406, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x6991e2cd, original_name='HUDGlowColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    hud_energy_deco_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.5372549891471863, g=0.8392159938812256, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x5c336f85, original_name='HUDEnergyDecoColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    hud_missile_group_active_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.5372549891471863, g=0.8392159938812256, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xdefca700, original_name='HUDMissileGroupActiveColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    selected_visor_beam_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.6627449989318848, g=0.6627449989318848, b=0.6627449989318848, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xcb7ddaf4, original_name='SelectedVisorBeamColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    unselected_visor_beam_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.564706027507782, g=0.564706027507782, b=0.564706027507782, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf17911aa, original_name='UnselectedVisorBeamColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    energy_bar_low_filled_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4078429937362671, b=0.01960800029337406, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xa14c8d20, original_name='EnergyBarLowFilledColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    energy_bar_low_shadow_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xb4135cdd, original_name='EnergyBarLowShadowColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    energy_bar_low_empty_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.17254899442195892, g=0.2901960015296936, b=0.37254899740219116, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xe0290c48, original_name='EnergyBarLowEmptyColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    hud_damage_modulate_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4039219915866852, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x1ec7f863, original_name='HUDDamageModulateColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    damage_indicator_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xae1317d8, original_name='DamageIndicatorColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    hud_title_foreground_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.20000000298023224, g=0.33725500106811523, b=0.4392159879207611, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x22b9b01e, original_name='HudTitleForegroundColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    hud_title_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.4000000059604645), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x70a2cd6e, original_name='HudTitleOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    visor_menu_title_foreground_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.5372549891471863, g=0.8392159938812256, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xe7070332, original_name='VisorMenuTitleForegroundColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    visor_menu_title_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x779c7b9c, original_name='VisorMenuTitleOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    beam_menu_title_foreground_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.5372549891471863, g=0.8392159938812256, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x13bd3b64, original_name='BeamMenuTitleForegroundColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    beam_menu_title_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x1531edd3, original_name='BeamMenuTitleOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    visor_beam_menu_icon_selected_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x27d0c234, original_name='VisorBeamMenuIconSelectedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    visor_beam_menu_icon_unselected_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.5, g=0.5, b=0.5, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xbaa6d6a1, original_name='VisorBeamMenuIconUnselectedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    visor_menu_icon_color0: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x59e416aa, original_name='VisorMenuIconColor0', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    visor_menu_icon_color1: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=1.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x92b8c50f, original_name='VisorMenuIconColor1', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    visor_menu_icon_color2: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x142cb7a1, original_name='VisorMenuIconColor2', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    visor_menu_icon_color3: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xdf706404, original_name='VisorMenuIconColor3', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    beam_menu_icon_color0: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x81269ee0, original_name='BeamMenuIconColor0', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    beam_menu_icon_color1: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=1.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x4a7a4d45, original_name='BeamMenuIconColor1', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    beam_menu_icon_color2: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xccee3feb, original_name='BeamMenuIconColor2', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    beam_menu_icon_color3: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x07b2ec4e, original_name='BeamMenuIconColor3', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    energy_warning_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4078429937362671, b=0.01960800029337406, a=0.49803900718688965), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x6f6e9d6d, original_name='EnergyWarningColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    threat_warning_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4039219915866852, b=0.01960800029337406, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xca68f68f, original_name='ThreatWarningColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    missile_warning_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4039219915866852, b=0.01960800029337406, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x0c00a29f, original_name='MissileWarningColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    missle_depletion_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x83040135, original_name='MissleDepletionColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    threat_bar_filled_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x1adea12b, original_name='ThreatBarFilledColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    threat_bar_shadow_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x0f8170d6, original_name='ThreatBarShadowColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    threat_bar_empty_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.16862699389457703, g=0.2862749993801117, b=0.36862701177597046, a=0.49803900718688965), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x794204fd, original_name='ThreatBarEmptyColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    missile_bar_filled_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x3c1ae0ff, original_name='MissileBarFilledColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    missile_bar_shadow_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x29453102, original_name='MissileBarShadowColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    missile_bar_empty_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.16862699389457703, g=0.2862749993801117, b=0.36862701177597046, a=0.49803900718688965), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x64337ccd, original_name='MissileBarEmptyColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    threat_group_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.5372549891471863, g=0.8392159938812256, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x4b86c539, original_name='ThreatGroupColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    free_look_bar_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=0.6274510025978088), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xa6609cc5, original_name='FreeLookBarColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    hud_bar_deco_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=0.313726007938385), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xbe3c29a1, original_name='HudBarDecoColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    unknown_0xf4379cf4: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf4379cf4, original_name='Unknown', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    threat_group_inactive_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=0.4000000059604645), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x74e5ffa1, original_name='ThreatGroupInactiveColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    missile_group_inactive_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=0.4000000059604645), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xd110a12f, original_name='MissileGroupInactiveColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    missile_group_combo_charge_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xceb17cdf, original_name='MissileGroupComboChargeColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    missile_group_non_combo_charge_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x4c5aff4f, original_name='MissileGroupNonComboChargeColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    missile_group_combo_activated_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.5372549891471863, g=0.8392159938812256, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x0b17b693, original_name='MissileGroupComboActivatedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    free_look_tick_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.5372549891471863, g=0.8392159938812256, b=1.0, a=0.19607800245285034), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xfad063d5, original_name='FreeLookTickColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    free_look_digits_foreground_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.5372549891471863, g=0.8392159938812256, b=1.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x2eafedf7, original_name='FreeLookDigitsForegroundColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    free_look_digits_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.00392200006172061, g=0.00392200006172061, b=0.00392200006172061, a=0.4000000059604645), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x2a01734f, original_name='FreeLookDigitsOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    unknown_0x8b0a4c90: Color = dataclasses.field(default_factory=lambda: Color(r=0.16862699389457703, g=0.2862749993801117, b=0.36862701177597046, a=0.5), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x8b0a4c90, original_name='Unknown', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    energy_warning_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xc4e17ca8, original_name='EnergyWarningOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    threat_warning_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xc7182898, original_name='ThreatWarningOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    missile_warning_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xcdbd73e1, original_name='MissileWarningOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    helmet_light_ambient_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4000000059604645, g=0.4000000059604645, b=0.4000000059604645, a=0.4000000059604645), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x78522461, original_name='HelmetLightAmbientColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    flash_pass_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4039219915866852, b=0.01960800029337406, a=0.7058820128440857), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x6a839a97, original_name='FlashPassColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_window_frame_base_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2862749993801117, g=0.48235300183296204, b=0.6235290169715881, a=0.4666669964790344), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x79ea6f12, original_name='ScanWindowFrameBaseColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_window_frame_active_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.5372549891471863, g=0.8392159938812256, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xdc901206, original_name='ScanWindowFrameActiveColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_window_frame_flash_add_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.33725500106811523, g=0.4313730001449585, b=0.7372549772262573, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xc54fa7bc, original_name='ScanWindowFrameFlashAddColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    unknown_0x18717fa7: Color = dataclasses.field(default_factory=lambda: Color(r=0.7098039984703064, g=0.7098039984703064, b=0.7098039984703064, a=0.5843139886856079), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x18717fa7, original_name='Unknown', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    unknown_0x8b7d7378: Color = dataclasses.field(default_factory=lambda: Color(r=0.3921569883823395, g=0.3921569883823395, b=0.3921569883823395, a=0.5843139886856079), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x8b7d7378, original_name='Unknown', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    unknown_0x867b01a2: Color = dataclasses.field(default_factory=lambda: Color(r=0.20000000298023224, g=0.20000000298023224, b=0.20000000298023224, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x867b01a2, original_name='Unknown', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_hud_hierarchy_frame_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4000000059604645, b=0.4000000059604645, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x08be8347, original_name='ScanHudHierarchyFrameColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_hud_hierarchy_inactive_frame_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4000000059604645, b=0.4000000059604645, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xe6ec3c8d, original_name='ScanHudHierarchyInactiveFrameColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_hud_hierarchy_text_frame_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4000000059604645, b=0.4000000059604645, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x591cd695, original_name='ScanHudHierarchyTextFrameColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_hud_hierarchy_final_text_frame_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4000000059604645, b=0.4000000059604645, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x26e1eb8c, original_name='ScanHudHierarchyFinalTextFrameColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_hud_hierarchy_flash_icon_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4000000059604645, b=0.4000000059604645, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x63e9e374, original_name='ScanHudHierarchyFlashIconColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_hud_hierarchy_complete_flash_icon_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4000000059604645, b=0.4000000059604645, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x738d9c43, original_name='ScanHudHierarchyCompleteFlashIconColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_hud_hierarchy_flash_flash_icon_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4000000059604645, b=0.4000000059604645, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xba6c75a2, original_name='ScanHudHierarchyFlashFlashIconColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_hud_hierarchy_text_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4000000059604645, b=0.4000000059604645, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xc37d11b7, original_name='ScanHudHierarchyTextColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_hud_hierarchy_final_text_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4000000059604645, b=0.4000000059604645, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xef1ec40e, original_name='ScanHudHierarchyFinalTextColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_hud_hierarchy_percent_text_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4000000059604645, b=0.4000000059604645, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x0ca7beb2, original_name='ScanHudHierarchyPercentTextColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_hud_hierarchy_bar_meter_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x87d3ce8a, original_name='ScanHudHierarchyBarMeterColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_visor_helmet_light_modulate_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4000000059604645, b=0.4000000059604645, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xeb7eb756, original_name='DarkVisorHelmetLightModulateColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    metroid_suck_pulse_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4196079969406128, g=0.0, b=0.0, a=0.3921569883823395), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xe4c1bbeb, original_name='MetroidSuckPulseColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    unknown_0xce7c9d8d: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.699999988079071, b=0.4000000059604645, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xce7c9d8d, original_name='Unknown', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    energy_bar_damage_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4039219915866852, b=0.01960800029337406, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x13490420, original_name='EnergyBarDamageColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    x_ray_clamps_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.49411800503730774, a=0.784313976764679), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xafe2d45d, original_name='XRayClampsColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    x_ray_holo_grid_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=0.3921569883823395), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x2af5aa06, original_name='XRayHoloGridColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    x_ray_seeker_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=0.313726007938385), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xd3cbe846, original_name='XRaySeekerColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    x_ray_seeker_ticks_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=0.5019609928131104), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x507b51da, original_name='XRaySeekerTicksColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    x_ray_seeker_ticks_outer_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=0.07451000064611435), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xc61d97ef, original_name='XRaySeekerTicksOuterColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    x_ray_top_puzzle_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.549019992351532, g=0.6078429818153381, b=0.8823530077934265, a=0.4666669964790344), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xaf0001cf, original_name='XRayTopPuzzleColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    x_ray_bottom_puzzle_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.549019992351532, g=0.6078429818153381, b=0.8823530077934265, a=0.4666669964790344), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x150a9b17, original_name='XRayBottomPuzzleColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    x_ray_left_puzzle_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.549019992351532, g=0.6078429818153381, b=0.8823530077934265, a=0.4666669964790344), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xd66d715f, original_name='XRayLeftPuzzleColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    x_ray_right_puzzle_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.549019992351532, g=0.6078429818153381, b=0.8823530077934265, a=0.4666669964790344), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xa8698fe8, original_name='XRayRightPuzzleColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    x_ray_corner_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=0.3921569883823395), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x4cb38e71, original_name='XRayCornerColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    x_ray_threat_digits_foreground_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x51c5aad9, original_name='XRayThreatDigitsForegroundColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    x_ray_threat_digits_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x60e8322b, original_name='XRayThreatDigitsOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    x_ray_missile_digits_foreground_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xa947a67c, original_name='XRayMissileDigitsForegroundColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    x_ray_missile_digits_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x421bae2a, original_name='XRayMissileDigitsOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    x_ray_threat_bar_filled_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.49411800503730774, a=0.6666669845581055), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf0049167, original_name='XRayThreatBarFilledColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    x_ray_threat_bar_empty_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.7372549772262573, b=0.01176500041037798, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x76357179, original_name='XRayThreatBarEmptyColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    x_ray_missile_bar_filled_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.49411800503730774, a=0.6666669845581055), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x439a3774, original_name='XRayMissileBarFilledColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    x_ray_missile_bar_empty_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.7372549772262573, b=0.01176500041037798, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x8ee94c81, original_name='XRayMissileBarEmptyColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_download_square_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.20000000298023224, g=0.33725500106811523, b=0.4392159879207611, a=0.4313730001449585), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xbb0897ea, original_name='ScanDownloadSquareColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_dot_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.38431400060653687, g=0.48627498745918274, b=0.5764709711074829, a=0.3921569883823395), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xc12cbab9, original_name='ScanDotColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    morph_ball_power_bomb_digits_foreground_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x716e6398, original_name='MorphBallPowerBombDigitsForegroundColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    morph_ball_power_bomb_digits_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xdaca46d4, original_name='MorphBallPowerBombDigitsOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    morph_ball_energy_word_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x0f37e756, original_name='MorphBallEnergyWordColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    morph_ball_bomb_counter_filled_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf7283644, original_name='MorphBallBombCounterFilledColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    morph_ball_bomb_counter_empty_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=0.49803900718688965), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x37564b7d, original_name='MorphBallBombCounterEmptyColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    morph_ball_power_bomb_icon_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x66b7eda3, original_name='MorphBallPowerBombIconColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    morph_ball_bomb_word_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf895098f, original_name='MorphBallBombWordColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    morph_ball_energy_deco_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x9b27be10, original_name='MorphBallEnergyDecoColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    morph_ball_bomb_deco_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x6c8550c9, original_name='MorphBallBombDecoColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    morph_ball_empty_power_bomb_digits_foreground_colorr: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x5368a35f, original_name='MorphBallEmptyPowerBombDigitsForegroundColorr', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    morph_ball_empty_power_bomb_digits_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.5), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x5a807b81, original_name='MorphBallEmptyPowerBombDigitsOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    morph_ball_empty_power_bomb_icon_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=0.5), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xeb63afed, original_name='MorphBallEmptyPowerBombIconColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_panel_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x92f59138, original_name='ScanPanelColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    unknown_0x96f650c3: Color = dataclasses.field(default_factory=lambda: Color(r=0.20000000298023224, g=0.33725500106811523, b=0.4392159879207611, a=0.3921569883823395), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x96f650c3, original_name='Unknown', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_images_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.5882350206375122), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xabdbfa5b, original_name='ScanImagesColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    unknown_0xd3bafaf5: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=1.0, a=0.10000000149011612), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xd3bafaf5, original_name='Unknown', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    threat_group_damage_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4039219915866852, b=0.01960800029337406, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf8b971fa, original_name='ThreatGroupDamageColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    coundown_foreground_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.5, g=0.699999988079071, b=1.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x4f1d443e, original_name='CoundownForegroundColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    coundown_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.699999988079071), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x0f6451da, original_name='CoundownOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    critical_scan_object_indicator_in_range_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.0, b=0.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xc1ec3637, original_name='CriticalScanObjectIndicatorInRangeColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    critical_scan_object_indicator_out_of_range_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.49411800503730774, g=0.20392200350761414, b=0.00392200006172061, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xb6a61e34, original_name='CriticalScanObjectIndicatorOutOfRangeColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    noncritical_scan_object_indicator_in_range_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4039219915866852, b=0.01960800029337406, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xfdcd9589, original_name='NoncriticalScanObjectIndicatorInRangeColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    noncritical_scan_object_indicator_out_of_range_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.49411800503730774, g=0.20392200350761414, b=0.007842999882996082, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xb0253266, original_name='NoncriticalScanObjectIndicatorOutOfRangeColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_seeker_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.20000000298023224, g=0.33725500106811523, b=0.4392159879207611, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x345e5b4e, original_name='ScanSeekerColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    thermal_threat_digits_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xe8401c5a, original_name='ThermalThreatDigitsOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    thermal_missile_digits_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x659147ae, original_name='ThermalMissileDigitsOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    combat_missile_digits_foreground_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x43ed3310, original_name='CombatMissileDigitsForegroundColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    combat_missile_digits_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xa781ed1d, original_name='CombatMissileDigitsOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    thermal_deco_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=0.784313976764679), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x35402188, original_name='ThermalDecoColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    thermal_deco_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=0.8235290050506592), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x223058b5, original_name='ThermalDecoOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    thermal_trackers_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xe846d37f, original_name='ThermalTrackersColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    thermal_lock_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039219915866852, g=0.6823530197143555, b=0.8823530077934265, a=0.49019598960876465), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x8c9f2a1a, original_name='ThermalLockColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    log_book_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.4039219915866852, b=0.01960800029337406, a=0.7058820128440857), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x1b0f3a85, original_name='LogBookColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    inventory_equipped_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4039210081100464, g=0.6823520064353943, b=0.8823519945144653, a=0.701960027217865), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x149369fd, original_name='InventoryEquippedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_visor_deco_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x02d5344f, original_name='DarkVisorDecoColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    light_ammo_tank_full_selected_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf37f8deb, original_name='LightAmmoTankFullSelectedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    light_ammo_tank_full_unselected_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x5a6587df, original_name='LightAmmoTankFullUnselectedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    light_ammo_tank_emptyl_selected_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xc18bdc67, original_name='LightAmmoTankEmptylSelectedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    light_ammo_tank_empty_unselected_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x4d916bb8, original_name='LightAmmoTankEmptyUnselectedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    light_ammo_meter_selected_fill_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x5ba76807, original_name='LightAmmoMeterSelectedFillColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    light_ammo_meter_selected_shadow_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xa42f6495, original_name='LightAmmoMeterSelectedShadowColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    light_ammo_meter_unselected_fill_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x448156ae, original_name='LightAmmoMeterUnselectedFillColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    light_ammo_meter_unselected_shadow_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x1a8b61b8, original_name='LightAmmoMeterUnselectedShadowColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    light_ammo_icon_selected_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf36adacb, original_name='LightAmmoIconSelectedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    light_ammo_icon_unselected_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x3aee673f, original_name='LightAmmoIconUnselectedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    light_ammo_digits_outline_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf9c88b05, original_name='LightAmmoDigitsOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    light_ammo_digits_selected_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x3bffe826, original_name='LightAmmoDigitsSelectedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    light_ammo_digits_unselected_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x19e9738b, original_name='LightAmmoDigitsUnselectedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    light_ammo_change_flash: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x9329c6ff, original_name='LightAmmoChangeFlash', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    light_ammo_tank_warning_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf9e7e0df, original_name='LightAmmoTankWarningColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    light_ammo_meter_warning_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x04e77411, original_name='LightAmmoMeterWarningColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    light_ammo_digit_warning_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x3c5d7111, original_name='LightAmmoDigitWarningColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    light_ammo_depletion_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x42e2dfc1, original_name='LightAmmoDepletionColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    light_ammo_empty_tank_warning_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xc758541f, original_name='LightAmmoEmptyTankWarningColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_ammo_tank_full_selected_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xde649e48, original_name='DarkAmmoTankFullSelectedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_ammo_tank_full_unselected_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x5bf10430, original_name='DarkAmmoTankFullUnselectedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_ammo_tank_emptyl_selected_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xc01f5f88, original_name='DarkAmmoTankEmptylSelectedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_ammo_tank_empty_unselected_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x7d2500d2, original_name='DarkAmmoTankEmptyUnselectedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_ammo_meter_selected_fill_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x14558146, original_name='DarkAmmoMeterSelectedFillColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_ammo_meter_selected_shadow_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x949b0fff, original_name='DarkAmmoMeterSelectedShadowColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_ammo_meter_unselected_fill_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x74353dc4, original_name='DarkAmmoMeterUnselectedFillColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_ammo_meter_unselected_shadow_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x5ff96af1, original_name='DarkAmmoMeterUnselectedShadowColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_ammo_icon_selected_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x074bb42f, original_name='DarkAmmoIconSelectedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_ammo_icon_unselected_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xaaf6e9a9, original_name='DarkAmmoIconUnselectedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_ammo_digits_outline_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x5e5b8c0a, original_name='DarkAmmoDigitsOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_ammo_digits_selected_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xabe766b0, original_name='DarkAmmoDigitsSelectedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_ammo_digits_unselected_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x34f26028, original_name='DarkAmmoDigitsUnselectedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_ammo_change_flash: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xa59b3320, original_name='DarkAmmoChangeFlash', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    num_huds: int = dataclasses.field(default=5, metadata={
        'reflection': FieldReflection[int](
            int, id=0xbfffe95a, original_name='NumHuds'
        ),
    })
    dark_ammo_tank_warning_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x0c3c55c9, original_name='DarkAmmoTankWarningColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_ammo_meter_warning_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf0c61af5, original_name='DarkAmmoMeterWarningColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_ammo_digit_warning_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xc87c1ff5, original_name='DarkAmmoDigitWarningColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_ammo_depletion_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x88936aa2, original_name='DarkAmmoDepletionColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_ammo_empty_tank_warning_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xea4347bc, original_name='DarkAmmoEmptyTankWarningColor', from_json=Color.from_json, to_json=Color.to_json
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
        if property_count != 179:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHlLHffffLHffffLHffffLHffffLHffff')
    
        dec = _FAST_FORMAT.unpack(data.read(3926))
        assert (dec[0], dec[6], dec[12], dec[18], dec[24], dec[30], dec[36], dec[42], dec[48], dec[54], dec[60], dec[66], dec[72], dec[78], dec[84], dec[90], dec[96], dec[102], dec[108], dec[114], dec[120], dec[126], dec[132], dec[138], dec[144], dec[150], dec[156], dec[162], dec[168], dec[174], dec[180], dec[186], dec[192], dec[198], dec[204], dec[210], dec[216], dec[222], dec[228], dec[234], dec[240], dec[246], dec[252], dec[258], dec[264], dec[270], dec[276], dec[282], dec[288], dec[294], dec[300], dec[306], dec[312], dec[318], dec[324], dec[330], dec[336], dec[342], dec[348], dec[354], dec[360], dec[366], dec[372], dec[378], dec[384], dec[390], dec[396], dec[402], dec[408], dec[414], dec[420], dec[426], dec[432], dec[438], dec[444], dec[450], dec[456], dec[462], dec[468], dec[474], dec[480], dec[486], dec[492], dec[498], dec[504], dec[510], dec[516], dec[522], dec[528], dec[534], dec[540], dec[546], dec[552], dec[558], dec[564], dec[570], dec[576], dec[582], dec[588], dec[594], dec[600], dec[606], dec[612], dec[618], dec[624], dec[630], dec[636], dec[642], dec[648], dec[654], dec[660], dec[666], dec[672], dec[678], dec[684], dec[690], dec[696], dec[702], dec[708], dec[714], dec[720], dec[726], dec[732], dec[738], dec[744], dec[750], dec[756], dec[762], dec[768], dec[774], dec[780], dec[786], dec[792], dec[798], dec[804], dec[810], dec[816], dec[822], dec[828], dec[834], dec[840], dec[846], dec[852], dec[858], dec[864], dec[870], dec[876], dec[882], dec[888], dec[894], dec[900], dec[906], dec[912], dec[918], dec[924], dec[930], dec[936], dec[942], dec[948], dec[954], dec[960], dec[966], dec[972], dec[978], dec[984], dec[990], dec[996], dec[1002], dec[1008], dec[1014], dec[1020], dec[1026], dec[1032], dec[1038], dec[1041], dec[1047], dec[1053], dec[1059], dec[1065]) == _FAST_IDS
        return cls(
            Color(*dec[2:6]),
            Color(*dec[8:12]),
            Color(*dec[14:18]),
            Color(*dec[20:24]),
            Color(*dec[26:30]),
            Color(*dec[32:36]),
            Color(*dec[38:42]),
            Color(*dec[44:48]),
            Color(*dec[50:54]),
            Color(*dec[56:60]),
            Color(*dec[62:66]),
            Color(*dec[68:72]),
            Color(*dec[74:78]),
            Color(*dec[80:84]),
            Color(*dec[86:90]),
            Color(*dec[92:96]),
            Color(*dec[98:102]),
            Color(*dec[104:108]),
            Color(*dec[110:114]),
            Color(*dec[116:120]),
            Color(*dec[122:126]),
            Color(*dec[128:132]),
            Color(*dec[134:138]),
            Color(*dec[140:144]),
            Color(*dec[146:150]),
            Color(*dec[152:156]),
            Color(*dec[158:162]),
            Color(*dec[164:168]),
            Color(*dec[170:174]),
            Color(*dec[176:180]),
            Color(*dec[182:186]),
            Color(*dec[188:192]),
            Color(*dec[194:198]),
            Color(*dec[200:204]),
            Color(*dec[206:210]),
            Color(*dec[212:216]),
            Color(*dec[218:222]),
            Color(*dec[224:228]),
            Color(*dec[230:234]),
            Color(*dec[236:240]),
            Color(*dec[242:246]),
            Color(*dec[248:252]),
            Color(*dec[254:258]),
            Color(*dec[260:264]),
            Color(*dec[266:270]),
            Color(*dec[272:276]),
            Color(*dec[278:282]),
            Color(*dec[284:288]),
            Color(*dec[290:294]),
            Color(*dec[296:300]),
            Color(*dec[302:306]),
            Color(*dec[308:312]),
            Color(*dec[314:318]),
            Color(*dec[320:324]),
            Color(*dec[326:330]),
            Color(*dec[332:336]),
            Color(*dec[338:342]),
            Color(*dec[344:348]),
            Color(*dec[350:354]),
            Color(*dec[356:360]),
            Color(*dec[362:366]),
            Color(*dec[368:372]),
            Color(*dec[374:378]),
            Color(*dec[380:384]),
            Color(*dec[386:390]),
            Color(*dec[392:396]),
            Color(*dec[398:402]),
            Color(*dec[404:408]),
            Color(*dec[410:414]),
            Color(*dec[416:420]),
            Color(*dec[422:426]),
            Color(*dec[428:432]),
            Color(*dec[434:438]),
            Color(*dec[440:444]),
            Color(*dec[446:450]),
            Color(*dec[452:456]),
            Color(*dec[458:462]),
            Color(*dec[464:468]),
            Color(*dec[470:474]),
            Color(*dec[476:480]),
            Color(*dec[482:486]),
            Color(*dec[488:492]),
            Color(*dec[494:498]),
            Color(*dec[500:504]),
            Color(*dec[506:510]),
            Color(*dec[512:516]),
            Color(*dec[518:522]),
            Color(*dec[524:528]),
            Color(*dec[530:534]),
            Color(*dec[536:540]),
            Color(*dec[542:546]),
            Color(*dec[548:552]),
            Color(*dec[554:558]),
            Color(*dec[560:564]),
            Color(*dec[566:570]),
            Color(*dec[572:576]),
            Color(*dec[578:582]),
            Color(*dec[584:588]),
            Color(*dec[590:594]),
            Color(*dec[596:600]),
            Color(*dec[602:606]),
            Color(*dec[608:612]),
            Color(*dec[614:618]),
            Color(*dec[620:624]),
            Color(*dec[626:630]),
            Color(*dec[632:636]),
            Color(*dec[638:642]),
            Color(*dec[644:648]),
            Color(*dec[650:654]),
            Color(*dec[656:660]),
            Color(*dec[662:666]),
            Color(*dec[668:672]),
            Color(*dec[674:678]),
            Color(*dec[680:684]),
            Color(*dec[686:690]),
            Color(*dec[692:696]),
            Color(*dec[698:702]),
            Color(*dec[704:708]),
            Color(*dec[710:714]),
            Color(*dec[716:720]),
            Color(*dec[722:726]),
            Color(*dec[728:732]),
            Color(*dec[734:738]),
            Color(*dec[740:744]),
            Color(*dec[746:750]),
            Color(*dec[752:756]),
            Color(*dec[758:762]),
            Color(*dec[764:768]),
            Color(*dec[770:774]),
            Color(*dec[776:780]),
            Color(*dec[782:786]),
            Color(*dec[788:792]),
            Color(*dec[794:798]),
            Color(*dec[800:804]),
            Color(*dec[806:810]),
            Color(*dec[812:816]),
            Color(*dec[818:822]),
            Color(*dec[824:828]),
            Color(*dec[830:834]),
            Color(*dec[836:840]),
            Color(*dec[842:846]),
            Color(*dec[848:852]),
            Color(*dec[854:858]),
            Color(*dec[860:864]),
            Color(*dec[866:870]),
            Color(*dec[872:876]),
            Color(*dec[878:882]),
            Color(*dec[884:888]),
            Color(*dec[890:894]),
            Color(*dec[896:900]),
            Color(*dec[902:906]),
            Color(*dec[908:912]),
            Color(*dec[914:918]),
            Color(*dec[920:924]),
            Color(*dec[926:930]),
            Color(*dec[932:936]),
            Color(*dec[938:942]),
            Color(*dec[944:948]),
            Color(*dec[950:954]),
            Color(*dec[956:960]),
            Color(*dec[962:966]),
            Color(*dec[968:972]),
            Color(*dec[974:978]),
            Color(*dec[980:984]),
            Color(*dec[986:990]),
            Color(*dec[992:996]),
            Color(*dec[998:1002]),
            Color(*dec[1004:1008]),
            Color(*dec[1010:1014]),
            Color(*dec[1016:1020]),
            Color(*dec[1022:1026]),
            Color(*dec[1028:1032]),
            Color(*dec[1034:1038]),
            dec[1040],
            Color(*dec[1043:1047]),
            Color(*dec[1049:1053]),
            Color(*dec[1055:1059]),
            Color(*dec[1061:1065]),
            Color(*dec[1067:1071]),
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\xb3')  # 179 properties

        data.write(b'\x8e\xd0L6')  # 0x8ed04c36
        data.write(b'\x00\x10')  # size
        self.pause_screen_bg_modulate_color.to_stream(data, game)

        data.write(b'\x16l"\xe0')  # 0x166c22e0
        data.write(b'\x00\x10')  # size
        self.radar_boundary_ring_color.to_stream(data, game)

        data.write(b'\xce\xc7\x8e\x81')  # 0xcec78e81
        data.write(b'\x00\x10')  # size
        self.radar_player_paint_color.to_stream(data, game)

        data.write(b'\x913\x8fr')  # 0x91338f72
        data.write(b'\x00\x10')  # size
        self.radar_enemy_paint_color.to_stream(data, game)

        data.write(b'\r$\xaek')  # 0xd24ae6b
        data.write(b'\x00\x10')  # size
        self.echo_ping_radar_color.to_stream(data, game)

        data.write(b'\xdd\xc5a\xeb')  # 0xddc561eb
        data.write(b'\x00\x10')  # size
        self.radar_friend_team_paint_color.to_stream(data, game)

        data.write(b'\x9b\xe2\x81P')  # 0x9be28150
        data.write(b'\x00\x10')  # size
        self.radar_enemy_team_paint_color.to_stream(data, game)

        data.write(b'-\xf1\xeb\x03')  # 0x2df1eb03
        data.write(b'\x00\x10')  # size
        self.hud_memo_text_foreground_color.to_stream(data, game)

        data.write(b'\xb5\xda0\xf4')  # 0xb5da30f4
        data.write(b'\x00\x10')  # size
        self.hud_memo_text_outline_color.to_stream(data, game)

        data.write(b'\xc8\xdd\xc6b')  # 0xc8ddc662
        data.write(b'\x00\x10')  # size
        self.hud_decorative_color.to_stream(data, game)

        data.write(b'i\x91\xe2\xcd')  # 0x6991e2cd
        data.write(b'\x00\x10')  # size
        self.hud_glow_color.to_stream(data, game)

        data.write(b'\\3o\x85')  # 0x5c336f85
        data.write(b'\x00\x10')  # size
        self.hud_energy_deco_color.to_stream(data, game)

        data.write(b'\xde\xfc\xa7\x00')  # 0xdefca700
        data.write(b'\x00\x10')  # size
        self.hud_missile_group_active_color.to_stream(data, game)

        data.write(b'\xcb}\xda\xf4')  # 0xcb7ddaf4
        data.write(b'\x00\x10')  # size
        self.selected_visor_beam_color.to_stream(data, game)

        data.write(b'\xf1y\x11\xaa')  # 0xf17911aa
        data.write(b'\x00\x10')  # size
        self.unselected_visor_beam_color.to_stream(data, game)

        data.write(b'\xa1L\x8d ')  # 0xa14c8d20
        data.write(b'\x00\x10')  # size
        self.energy_bar_low_filled_color.to_stream(data, game)

        data.write(b'\xb4\x13\\\xdd')  # 0xb4135cdd
        data.write(b'\x00\x10')  # size
        self.energy_bar_low_shadow_color.to_stream(data, game)

        data.write(b'\xe0)\x0cH')  # 0xe0290c48
        data.write(b'\x00\x10')  # size
        self.energy_bar_low_empty_color.to_stream(data, game)

        data.write(b'\x1e\xc7\xf8c')  # 0x1ec7f863
        data.write(b'\x00\x10')  # size
        self.hud_damage_modulate_color.to_stream(data, game)

        data.write(b'\xae\x13\x17\xd8')  # 0xae1317d8
        data.write(b'\x00\x10')  # size
        self.damage_indicator_color.to_stream(data, game)

        data.write(b'"\xb9\xb0\x1e')  # 0x22b9b01e
        data.write(b'\x00\x10')  # size
        self.hud_title_foreground_color.to_stream(data, game)

        data.write(b'p\xa2\xcdn')  # 0x70a2cd6e
        data.write(b'\x00\x10')  # size
        self.hud_title_outline_color.to_stream(data, game)

        data.write(b'\xe7\x07\x032')  # 0xe7070332
        data.write(b'\x00\x10')  # size
        self.visor_menu_title_foreground_color.to_stream(data, game)

        data.write(b'w\x9c{\x9c')  # 0x779c7b9c
        data.write(b'\x00\x10')  # size
        self.visor_menu_title_outline_color.to_stream(data, game)

        data.write(b'\x13\xbd;d')  # 0x13bd3b64
        data.write(b'\x00\x10')  # size
        self.beam_menu_title_foreground_color.to_stream(data, game)

        data.write(b'\x151\xed\xd3')  # 0x1531edd3
        data.write(b'\x00\x10')  # size
        self.beam_menu_title_outline_color.to_stream(data, game)

        data.write(b"'\xd0\xc24")  # 0x27d0c234
        data.write(b'\x00\x10')  # size
        self.visor_beam_menu_icon_selected_color.to_stream(data, game)

        data.write(b'\xba\xa6\xd6\xa1')  # 0xbaa6d6a1
        data.write(b'\x00\x10')  # size
        self.visor_beam_menu_icon_unselected_color.to_stream(data, game)

        data.write(b'Y\xe4\x16\xaa')  # 0x59e416aa
        data.write(b'\x00\x10')  # size
        self.visor_menu_icon_color0.to_stream(data, game)

        data.write(b'\x92\xb8\xc5\x0f')  # 0x92b8c50f
        data.write(b'\x00\x10')  # size
        self.visor_menu_icon_color1.to_stream(data, game)

        data.write(b'\x14,\xb7\xa1')  # 0x142cb7a1
        data.write(b'\x00\x10')  # size
        self.visor_menu_icon_color2.to_stream(data, game)

        data.write(b'\xdfpd\x04')  # 0xdf706404
        data.write(b'\x00\x10')  # size
        self.visor_menu_icon_color3.to_stream(data, game)

        data.write(b'\x81&\x9e\xe0')  # 0x81269ee0
        data.write(b'\x00\x10')  # size
        self.beam_menu_icon_color0.to_stream(data, game)

        data.write(b'JzME')  # 0x4a7a4d45
        data.write(b'\x00\x10')  # size
        self.beam_menu_icon_color1.to_stream(data, game)

        data.write(b'\xcc\xee?\xeb')  # 0xccee3feb
        data.write(b'\x00\x10')  # size
        self.beam_menu_icon_color2.to_stream(data, game)

        data.write(b'\x07\xb2\xecN')  # 0x7b2ec4e
        data.write(b'\x00\x10')  # size
        self.beam_menu_icon_color3.to_stream(data, game)

        data.write(b'on\x9dm')  # 0x6f6e9d6d
        data.write(b'\x00\x10')  # size
        self.energy_warning_color.to_stream(data, game)

        data.write(b'\xcah\xf6\x8f')  # 0xca68f68f
        data.write(b'\x00\x10')  # size
        self.threat_warning_color.to_stream(data, game)

        data.write(b'\x0c\x00\xa2\x9f')  # 0xc00a29f
        data.write(b'\x00\x10')  # size
        self.missile_warning_color.to_stream(data, game)

        data.write(b'\x83\x04\x015')  # 0x83040135
        data.write(b'\x00\x10')  # size
        self.missle_depletion_color.to_stream(data, game)

        data.write(b'\x1a\xde\xa1+')  # 0x1adea12b
        data.write(b'\x00\x10')  # size
        self.threat_bar_filled_color.to_stream(data, game)

        data.write(b'\x0f\x81p\xd6')  # 0xf8170d6
        data.write(b'\x00\x10')  # size
        self.threat_bar_shadow_color.to_stream(data, game)

        data.write(b'yB\x04\xfd')  # 0x794204fd
        data.write(b'\x00\x10')  # size
        self.threat_bar_empty_color.to_stream(data, game)

        data.write(b'<\x1a\xe0\xff')  # 0x3c1ae0ff
        data.write(b'\x00\x10')  # size
        self.missile_bar_filled_color.to_stream(data, game)

        data.write(b')E1\x02')  # 0x29453102
        data.write(b'\x00\x10')  # size
        self.missile_bar_shadow_color.to_stream(data, game)

        data.write(b'd3|\xcd')  # 0x64337ccd
        data.write(b'\x00\x10')  # size
        self.missile_bar_empty_color.to_stream(data, game)

        data.write(b'K\x86\xc59')  # 0x4b86c539
        data.write(b'\x00\x10')  # size
        self.threat_group_color.to_stream(data, game)

        data.write(b'\xa6`\x9c\xc5')  # 0xa6609cc5
        data.write(b'\x00\x10')  # size
        self.free_look_bar_color.to_stream(data, game)

        data.write(b'\xbe<)\xa1')  # 0xbe3c29a1
        data.write(b'\x00\x10')  # size
        self.hud_bar_deco_color.to_stream(data, game)

        data.write(b'\xf47\x9c\xf4')  # 0xf4379cf4
        data.write(b'\x00\x10')  # size
        self.unknown_0xf4379cf4.to_stream(data, game)

        data.write(b't\xe5\xff\xa1')  # 0x74e5ffa1
        data.write(b'\x00\x10')  # size
        self.threat_group_inactive_color.to_stream(data, game)

        data.write(b'\xd1\x10\xa1/')  # 0xd110a12f
        data.write(b'\x00\x10')  # size
        self.missile_group_inactive_color.to_stream(data, game)

        data.write(b'\xce\xb1|\xdf')  # 0xceb17cdf
        data.write(b'\x00\x10')  # size
        self.missile_group_combo_charge_color.to_stream(data, game)

        data.write(b'LZ\xffO')  # 0x4c5aff4f
        data.write(b'\x00\x10')  # size
        self.missile_group_non_combo_charge_color.to_stream(data, game)

        data.write(b'\x0b\x17\xb6\x93')  # 0xb17b693
        data.write(b'\x00\x10')  # size
        self.missile_group_combo_activated_color.to_stream(data, game)

        data.write(b'\xfa\xd0c\xd5')  # 0xfad063d5
        data.write(b'\x00\x10')  # size
        self.free_look_tick_color.to_stream(data, game)

        data.write(b'.\xaf\xed\xf7')  # 0x2eafedf7
        data.write(b'\x00\x10')  # size
        self.free_look_digits_foreground_color.to_stream(data, game)

        data.write(b'*\x01sO')  # 0x2a01734f
        data.write(b'\x00\x10')  # size
        self.free_look_digits_outline_color.to_stream(data, game)

        data.write(b'\x8b\nL\x90')  # 0x8b0a4c90
        data.write(b'\x00\x10')  # size
        self.unknown_0x8b0a4c90.to_stream(data, game)

        data.write(b'\xc4\xe1|\xa8')  # 0xc4e17ca8
        data.write(b'\x00\x10')  # size
        self.energy_warning_outline_color.to_stream(data, game)

        data.write(b'\xc7\x18(\x98')  # 0xc7182898
        data.write(b'\x00\x10')  # size
        self.threat_warning_outline_color.to_stream(data, game)

        data.write(b'\xcd\xbds\xe1')  # 0xcdbd73e1
        data.write(b'\x00\x10')  # size
        self.missile_warning_outline_color.to_stream(data, game)

        data.write(b'xR$a')  # 0x78522461
        data.write(b'\x00\x10')  # size
        self.helmet_light_ambient_color.to_stream(data, game)

        data.write(b'j\x83\x9a\x97')  # 0x6a839a97
        data.write(b'\x00\x10')  # size
        self.flash_pass_color.to_stream(data, game)

        data.write(b'y\xeao\x12')  # 0x79ea6f12
        data.write(b'\x00\x10')  # size
        self.scan_window_frame_base_color.to_stream(data, game)

        data.write(b'\xdc\x90\x12\x06')  # 0xdc901206
        data.write(b'\x00\x10')  # size
        self.scan_window_frame_active_color.to_stream(data, game)

        data.write(b'\xc5O\xa7\xbc')  # 0xc54fa7bc
        data.write(b'\x00\x10')  # size
        self.scan_window_frame_flash_add_color.to_stream(data, game)

        data.write(b'\x18q\x7f\xa7')  # 0x18717fa7
        data.write(b'\x00\x10')  # size
        self.unknown_0x18717fa7.to_stream(data, game)

        data.write(b'\x8b}sx')  # 0x8b7d7378
        data.write(b'\x00\x10')  # size
        self.unknown_0x8b7d7378.to_stream(data, game)

        data.write(b'\x86{\x01\xa2')  # 0x867b01a2
        data.write(b'\x00\x10')  # size
        self.unknown_0x867b01a2.to_stream(data, game)

        data.write(b'\x08\xbe\x83G')  # 0x8be8347
        data.write(b'\x00\x10')  # size
        self.scan_hud_hierarchy_frame_color.to_stream(data, game)

        data.write(b'\xe6\xec<\x8d')  # 0xe6ec3c8d
        data.write(b'\x00\x10')  # size
        self.scan_hud_hierarchy_inactive_frame_color.to_stream(data, game)

        data.write(b'Y\x1c\xd6\x95')  # 0x591cd695
        data.write(b'\x00\x10')  # size
        self.scan_hud_hierarchy_text_frame_color.to_stream(data, game)

        data.write(b'&\xe1\xeb\x8c')  # 0x26e1eb8c
        data.write(b'\x00\x10')  # size
        self.scan_hud_hierarchy_final_text_frame_color.to_stream(data, game)

        data.write(b'c\xe9\xe3t')  # 0x63e9e374
        data.write(b'\x00\x10')  # size
        self.scan_hud_hierarchy_flash_icon_color.to_stream(data, game)

        data.write(b's\x8d\x9cC')  # 0x738d9c43
        data.write(b'\x00\x10')  # size
        self.scan_hud_hierarchy_complete_flash_icon_color.to_stream(data, game)

        data.write(b'\xbalu\xa2')  # 0xba6c75a2
        data.write(b'\x00\x10')  # size
        self.scan_hud_hierarchy_flash_flash_icon_color.to_stream(data, game)

        data.write(b'\xc3}\x11\xb7')  # 0xc37d11b7
        data.write(b'\x00\x10')  # size
        self.scan_hud_hierarchy_text_color.to_stream(data, game)

        data.write(b'\xef\x1e\xc4\x0e')  # 0xef1ec40e
        data.write(b'\x00\x10')  # size
        self.scan_hud_hierarchy_final_text_color.to_stream(data, game)

        data.write(b'\x0c\xa7\xbe\xb2')  # 0xca7beb2
        data.write(b'\x00\x10')  # size
        self.scan_hud_hierarchy_percent_text_color.to_stream(data, game)

        data.write(b'\x87\xd3\xce\x8a')  # 0x87d3ce8a
        data.write(b'\x00\x10')  # size
        self.scan_hud_hierarchy_bar_meter_color.to_stream(data, game)

        data.write(b'\xeb~\xb7V')  # 0xeb7eb756
        data.write(b'\x00\x10')  # size
        self.dark_visor_helmet_light_modulate_color.to_stream(data, game)

        data.write(b'\xe4\xc1\xbb\xeb')  # 0xe4c1bbeb
        data.write(b'\x00\x10')  # size
        self.metroid_suck_pulse_color.to_stream(data, game)

        data.write(b'\xce|\x9d\x8d')  # 0xce7c9d8d
        data.write(b'\x00\x10')  # size
        self.unknown_0xce7c9d8d.to_stream(data, game)

        data.write(b'\x13I\x04 ')  # 0x13490420
        data.write(b'\x00\x10')  # size
        self.energy_bar_damage_color.to_stream(data, game)

        data.write(b'\xaf\xe2\xd4]')  # 0xafe2d45d
        data.write(b'\x00\x10')  # size
        self.x_ray_clamps_color.to_stream(data, game)

        data.write(b'*\xf5\xaa\x06')  # 0x2af5aa06
        data.write(b'\x00\x10')  # size
        self.x_ray_holo_grid_color.to_stream(data, game)

        data.write(b'\xd3\xcb\xe8F')  # 0xd3cbe846
        data.write(b'\x00\x10')  # size
        self.x_ray_seeker_color.to_stream(data, game)

        data.write(b'P{Q\xda')  # 0x507b51da
        data.write(b'\x00\x10')  # size
        self.x_ray_seeker_ticks_color.to_stream(data, game)

        data.write(b'\xc6\x1d\x97\xef')  # 0xc61d97ef
        data.write(b'\x00\x10')  # size
        self.x_ray_seeker_ticks_outer_color.to_stream(data, game)

        data.write(b'\xaf\x00\x01\xcf')  # 0xaf0001cf
        data.write(b'\x00\x10')  # size
        self.x_ray_top_puzzle_color.to_stream(data, game)

        data.write(b'\x15\n\x9b\x17')  # 0x150a9b17
        data.write(b'\x00\x10')  # size
        self.x_ray_bottom_puzzle_color.to_stream(data, game)

        data.write(b'\xd6mq_')  # 0xd66d715f
        data.write(b'\x00\x10')  # size
        self.x_ray_left_puzzle_color.to_stream(data, game)

        data.write(b'\xa8i\x8f\xe8')  # 0xa8698fe8
        data.write(b'\x00\x10')  # size
        self.x_ray_right_puzzle_color.to_stream(data, game)

        data.write(b'L\xb3\x8eq')  # 0x4cb38e71
        data.write(b'\x00\x10')  # size
        self.x_ray_corner_color.to_stream(data, game)

        data.write(b'Q\xc5\xaa\xd9')  # 0x51c5aad9
        data.write(b'\x00\x10')  # size
        self.x_ray_threat_digits_foreground_color.to_stream(data, game)

        data.write(b'`\xe82+')  # 0x60e8322b
        data.write(b'\x00\x10')  # size
        self.x_ray_threat_digits_outline_color.to_stream(data, game)

        data.write(b'\xa9G\xa6|')  # 0xa947a67c
        data.write(b'\x00\x10')  # size
        self.x_ray_missile_digits_foreground_color.to_stream(data, game)

        data.write(b'B\x1b\xae*')  # 0x421bae2a
        data.write(b'\x00\x10')  # size
        self.x_ray_missile_digits_outline_color.to_stream(data, game)

        data.write(b'\xf0\x04\x91g')  # 0xf0049167
        data.write(b'\x00\x10')  # size
        self.x_ray_threat_bar_filled_color.to_stream(data, game)

        data.write(b'v5qy')  # 0x76357179
        data.write(b'\x00\x10')  # size
        self.x_ray_threat_bar_empty_color.to_stream(data, game)

        data.write(b'C\x9a7t')  # 0x439a3774
        data.write(b'\x00\x10')  # size
        self.x_ray_missile_bar_filled_color.to_stream(data, game)

        data.write(b'\x8e\xe9L\x81')  # 0x8ee94c81
        data.write(b'\x00\x10')  # size
        self.x_ray_missile_bar_empty_color.to_stream(data, game)

        data.write(b'\xbb\x08\x97\xea')  # 0xbb0897ea
        data.write(b'\x00\x10')  # size
        self.scan_download_square_color.to_stream(data, game)

        data.write(b'\xc1,\xba\xb9')  # 0xc12cbab9
        data.write(b'\x00\x10')  # size
        self.scan_dot_color.to_stream(data, game)

        data.write(b'qnc\x98')  # 0x716e6398
        data.write(b'\x00\x10')  # size
        self.morph_ball_power_bomb_digits_foreground_color.to_stream(data, game)

        data.write(b'\xda\xcaF\xd4')  # 0xdaca46d4
        data.write(b'\x00\x10')  # size
        self.morph_ball_power_bomb_digits_outline_color.to_stream(data, game)

        data.write(b'\x0f7\xe7V')  # 0xf37e756
        data.write(b'\x00\x10')  # size
        self.morph_ball_energy_word_color.to_stream(data, game)

        data.write(b'\xf7(6D')  # 0xf7283644
        data.write(b'\x00\x10')  # size
        self.morph_ball_bomb_counter_filled_color.to_stream(data, game)

        data.write(b'7VK}')  # 0x37564b7d
        data.write(b'\x00\x10')  # size
        self.morph_ball_bomb_counter_empty_color.to_stream(data, game)

        data.write(b'f\xb7\xed\xa3')  # 0x66b7eda3
        data.write(b'\x00\x10')  # size
        self.morph_ball_power_bomb_icon_color.to_stream(data, game)

        data.write(b'\xf8\x95\t\x8f')  # 0xf895098f
        data.write(b'\x00\x10')  # size
        self.morph_ball_bomb_word_color.to_stream(data, game)

        data.write(b"\x9b'\xbe\x10")  # 0x9b27be10
        data.write(b'\x00\x10')  # size
        self.morph_ball_energy_deco_color.to_stream(data, game)

        data.write(b'l\x85P\xc9')  # 0x6c8550c9
        data.write(b'\x00\x10')  # size
        self.morph_ball_bomb_deco_color.to_stream(data, game)

        data.write(b'Sh\xa3_')  # 0x5368a35f
        data.write(b'\x00\x10')  # size
        self.morph_ball_empty_power_bomb_digits_foreground_colorr.to_stream(data, game)

        data.write(b'Z\x80{\x81')  # 0x5a807b81
        data.write(b'\x00\x10')  # size
        self.morph_ball_empty_power_bomb_digits_outline_color.to_stream(data, game)

        data.write(b'\xebc\xaf\xed')  # 0xeb63afed
        data.write(b'\x00\x10')  # size
        self.morph_ball_empty_power_bomb_icon_color.to_stream(data, game)

        data.write(b'\x92\xf5\x918')  # 0x92f59138
        data.write(b'\x00\x10')  # size
        self.scan_panel_color.to_stream(data, game)

        data.write(b'\x96\xf6P\xc3')  # 0x96f650c3
        data.write(b'\x00\x10')  # size
        self.unknown_0x96f650c3.to_stream(data, game)

        data.write(b'\xab\xdb\xfa[')  # 0xabdbfa5b
        data.write(b'\x00\x10')  # size
        self.scan_images_color.to_stream(data, game)

        data.write(b'\xd3\xba\xfa\xf5')  # 0xd3bafaf5
        data.write(b'\x00\x10')  # size
        self.unknown_0xd3bafaf5.to_stream(data, game)

        data.write(b'\xf8\xb9q\xfa')  # 0xf8b971fa
        data.write(b'\x00\x10')  # size
        self.threat_group_damage_color.to_stream(data, game)

        data.write(b'O\x1dD>')  # 0x4f1d443e
        data.write(b'\x00\x10')  # size
        self.coundown_foreground_color.to_stream(data, game)

        data.write(b'\x0fdQ\xda')  # 0xf6451da
        data.write(b'\x00\x10')  # size
        self.coundown_outline_color.to_stream(data, game)

        data.write(b'\xc1\xec67')  # 0xc1ec3637
        data.write(b'\x00\x10')  # size
        self.critical_scan_object_indicator_in_range_color.to_stream(data, game)

        data.write(b'\xb6\xa6\x1e4')  # 0xb6a61e34
        data.write(b'\x00\x10')  # size
        self.critical_scan_object_indicator_out_of_range_color.to_stream(data, game)

        data.write(b'\xfd\xcd\x95\x89')  # 0xfdcd9589
        data.write(b'\x00\x10')  # size
        self.noncritical_scan_object_indicator_in_range_color.to_stream(data, game)

        data.write(b'\xb0%2f')  # 0xb0253266
        data.write(b'\x00\x10')  # size
        self.noncritical_scan_object_indicator_out_of_range_color.to_stream(data, game)

        data.write(b'4^[N')  # 0x345e5b4e
        data.write(b'\x00\x10')  # size
        self.scan_seeker_color.to_stream(data, game)

        data.write(b'\xe8@\x1cZ')  # 0xe8401c5a
        data.write(b'\x00\x10')  # size
        self.thermal_threat_digits_outline_color.to_stream(data, game)

        data.write(b'e\x91G\xae')  # 0x659147ae
        data.write(b'\x00\x10')  # size
        self.thermal_missile_digits_outline_color.to_stream(data, game)

        data.write(b'C\xed3\x10')  # 0x43ed3310
        data.write(b'\x00\x10')  # size
        self.combat_missile_digits_foreground_color.to_stream(data, game)

        data.write(b'\xa7\x81\xed\x1d')  # 0xa781ed1d
        data.write(b'\x00\x10')  # size
        self.combat_missile_digits_outline_color.to_stream(data, game)

        data.write(b'5@!\x88')  # 0x35402188
        data.write(b'\x00\x10')  # size
        self.thermal_deco_color.to_stream(data, game)

        data.write(b'"0X\xb5')  # 0x223058b5
        data.write(b'\x00\x10')  # size
        self.thermal_deco_outline_color.to_stream(data, game)

        data.write(b'\xe8F\xd3\x7f')  # 0xe846d37f
        data.write(b'\x00\x10')  # size
        self.thermal_trackers_color.to_stream(data, game)

        data.write(b'\x8c\x9f*\x1a')  # 0x8c9f2a1a
        data.write(b'\x00\x10')  # size
        self.thermal_lock_color.to_stream(data, game)

        data.write(b'\x1b\x0f:\x85')  # 0x1b0f3a85
        data.write(b'\x00\x10')  # size
        self.log_book_color.to_stream(data, game)

        data.write(b'\x14\x93i\xfd')  # 0x149369fd
        data.write(b'\x00\x10')  # size
        self.inventory_equipped_color.to_stream(data, game)

        data.write(b'\x02\xd54O')  # 0x2d5344f
        data.write(b'\x00\x10')  # size
        self.dark_visor_deco_color.to_stream(data, game)

        data.write(b'\xf3\x7f\x8d\xeb')  # 0xf37f8deb
        data.write(b'\x00\x10')  # size
        self.light_ammo_tank_full_selected_color.to_stream(data, game)

        data.write(b'Ze\x87\xdf')  # 0x5a6587df
        data.write(b'\x00\x10')  # size
        self.light_ammo_tank_full_unselected_color.to_stream(data, game)

        data.write(b'\xc1\x8b\xdcg')  # 0xc18bdc67
        data.write(b'\x00\x10')  # size
        self.light_ammo_tank_emptyl_selected_color.to_stream(data, game)

        data.write(b'M\x91k\xb8')  # 0x4d916bb8
        data.write(b'\x00\x10')  # size
        self.light_ammo_tank_empty_unselected_color.to_stream(data, game)

        data.write(b'[\xa7h\x07')  # 0x5ba76807
        data.write(b'\x00\x10')  # size
        self.light_ammo_meter_selected_fill_color.to_stream(data, game)

        data.write(b'\xa4/d\x95')  # 0xa42f6495
        data.write(b'\x00\x10')  # size
        self.light_ammo_meter_selected_shadow_color.to_stream(data, game)

        data.write(b'D\x81V\xae')  # 0x448156ae
        data.write(b'\x00\x10')  # size
        self.light_ammo_meter_unselected_fill_color.to_stream(data, game)

        data.write(b'\x1a\x8ba\xb8')  # 0x1a8b61b8
        data.write(b'\x00\x10')  # size
        self.light_ammo_meter_unselected_shadow_color.to_stream(data, game)

        data.write(b'\xf3j\xda\xcb')  # 0xf36adacb
        data.write(b'\x00\x10')  # size
        self.light_ammo_icon_selected_color.to_stream(data, game)

        data.write(b':\xeeg?')  # 0x3aee673f
        data.write(b'\x00\x10')  # size
        self.light_ammo_icon_unselected_color.to_stream(data, game)

        data.write(b'\xf9\xc8\x8b\x05')  # 0xf9c88b05
        data.write(b'\x00\x10')  # size
        self.light_ammo_digits_outline_color.to_stream(data, game)

        data.write(b';\xff\xe8&')  # 0x3bffe826
        data.write(b'\x00\x10')  # size
        self.light_ammo_digits_selected_color.to_stream(data, game)

        data.write(b'\x19\xe9s\x8b')  # 0x19e9738b
        data.write(b'\x00\x10')  # size
        self.light_ammo_digits_unselected_color.to_stream(data, game)

        data.write(b'\x93)\xc6\xff')  # 0x9329c6ff
        data.write(b'\x00\x10')  # size
        self.light_ammo_change_flash.to_stream(data, game)

        data.write(b'\xf9\xe7\xe0\xdf')  # 0xf9e7e0df
        data.write(b'\x00\x10')  # size
        self.light_ammo_tank_warning_color.to_stream(data, game)

        data.write(b'\x04\xe7t\x11')  # 0x4e77411
        data.write(b'\x00\x10')  # size
        self.light_ammo_meter_warning_color.to_stream(data, game)

        data.write(b'<]q\x11')  # 0x3c5d7111
        data.write(b'\x00\x10')  # size
        self.light_ammo_digit_warning_color.to_stream(data, game)

        data.write(b'B\xe2\xdf\xc1')  # 0x42e2dfc1
        data.write(b'\x00\x10')  # size
        self.light_ammo_depletion_color.to_stream(data, game)

        data.write(b'\xc7XT\x1f')  # 0xc758541f
        data.write(b'\x00\x10')  # size
        self.light_ammo_empty_tank_warning_color.to_stream(data, game)

        data.write(b'\xded\x9eH')  # 0xde649e48
        data.write(b'\x00\x10')  # size
        self.dark_ammo_tank_full_selected_color.to_stream(data, game)

        data.write(b'[\xf1\x040')  # 0x5bf10430
        data.write(b'\x00\x10')  # size
        self.dark_ammo_tank_full_unselected_color.to_stream(data, game)

        data.write(b'\xc0\x1f_\x88')  # 0xc01f5f88
        data.write(b'\x00\x10')  # size
        self.dark_ammo_tank_emptyl_selected_color.to_stream(data, game)

        data.write(b'}%\x00\xd2')  # 0x7d2500d2
        data.write(b'\x00\x10')  # size
        self.dark_ammo_tank_empty_unselected_color.to_stream(data, game)

        data.write(b'\x14U\x81F')  # 0x14558146
        data.write(b'\x00\x10')  # size
        self.dark_ammo_meter_selected_fill_color.to_stream(data, game)

        data.write(b'\x94\x9b\x0f\xff')  # 0x949b0fff
        data.write(b'\x00\x10')  # size
        self.dark_ammo_meter_selected_shadow_color.to_stream(data, game)

        data.write(b't5=\xc4')  # 0x74353dc4
        data.write(b'\x00\x10')  # size
        self.dark_ammo_meter_unselected_fill_color.to_stream(data, game)

        data.write(b'_\xf9j\xf1')  # 0x5ff96af1
        data.write(b'\x00\x10')  # size
        self.dark_ammo_meter_unselected_shadow_color.to_stream(data, game)

        data.write(b'\x07K\xb4/')  # 0x74bb42f
        data.write(b'\x00\x10')  # size
        self.dark_ammo_icon_selected_color.to_stream(data, game)

        data.write(b'\xaa\xf6\xe9\xa9')  # 0xaaf6e9a9
        data.write(b'\x00\x10')  # size
        self.dark_ammo_icon_unselected_color.to_stream(data, game)

        data.write(b'^[\x8c\n')  # 0x5e5b8c0a
        data.write(b'\x00\x10')  # size
        self.dark_ammo_digits_outline_color.to_stream(data, game)

        data.write(b'\xab\xe7f\xb0')  # 0xabe766b0
        data.write(b'\x00\x10')  # size
        self.dark_ammo_digits_selected_color.to_stream(data, game)

        data.write(b'4\xf2`(')  # 0x34f26028
        data.write(b'\x00\x10')  # size
        self.dark_ammo_digits_unselected_color.to_stream(data, game)

        data.write(b'\xa5\x9b3 ')  # 0xa59b3320
        data.write(b'\x00\x10')  # size
        self.dark_ammo_change_flash.to_stream(data, game)

        data.write(b'\xbf\xff\xe9Z')  # 0xbfffe95a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.num_huds))

        data.write(b'\x0c<U\xc9')  # 0xc3c55c9
        data.write(b'\x00\x10')  # size
        self.dark_ammo_tank_warning_color.to_stream(data, game)

        data.write(b'\xf0\xc6\x1a\xf5')  # 0xf0c61af5
        data.write(b'\x00\x10')  # size
        self.dark_ammo_meter_warning_color.to_stream(data, game)

        data.write(b'\xc8|\x1f\xf5')  # 0xc87c1ff5
        data.write(b'\x00\x10')  # size
        self.dark_ammo_digit_warning_color.to_stream(data, game)

        data.write(b'\x88\x93j\xa2')  # 0x88936aa2
        data.write(b'\x00\x10')  # size
        self.dark_ammo_depletion_color.to_stream(data, game)

        data.write(b'\xeaCG\xbc')  # 0xea4347bc
        data.write(b'\x00\x10')  # size
        self.dark_ammo_empty_tank_warning_color.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGuiColors_MiscJson", data)
        return cls(
            pause_screen_bg_modulate_color=Color.from_json(json_data['pause_screen_bg_modulate_color']),
            radar_boundary_ring_color=Color.from_json(json_data['radar_boundary_ring_color']),
            radar_player_paint_color=Color.from_json(json_data['radar_player_paint_color']),
            radar_enemy_paint_color=Color.from_json(json_data['radar_enemy_paint_color']),
            echo_ping_radar_color=Color.from_json(json_data['echo_ping_radar_color']),
            radar_friend_team_paint_color=Color.from_json(json_data['radar_friend_team_paint_color']),
            radar_enemy_team_paint_color=Color.from_json(json_data['radar_enemy_team_paint_color']),
            hud_memo_text_foreground_color=Color.from_json(json_data['hud_memo_text_foreground_color']),
            hud_memo_text_outline_color=Color.from_json(json_data['hud_memo_text_outline_color']),
            hud_decorative_color=Color.from_json(json_data['hud_decorative_color']),
            hud_glow_color=Color.from_json(json_data['hud_glow_color']),
            hud_energy_deco_color=Color.from_json(json_data['hud_energy_deco_color']),
            hud_missile_group_active_color=Color.from_json(json_data['hud_missile_group_active_color']),
            selected_visor_beam_color=Color.from_json(json_data['selected_visor_beam_color']),
            unselected_visor_beam_color=Color.from_json(json_data['unselected_visor_beam_color']),
            energy_bar_low_filled_color=Color.from_json(json_data['energy_bar_low_filled_color']),
            energy_bar_low_shadow_color=Color.from_json(json_data['energy_bar_low_shadow_color']),
            energy_bar_low_empty_color=Color.from_json(json_data['energy_bar_low_empty_color']),
            hud_damage_modulate_color=Color.from_json(json_data['hud_damage_modulate_color']),
            damage_indicator_color=Color.from_json(json_data['damage_indicator_color']),
            hud_title_foreground_color=Color.from_json(json_data['hud_title_foreground_color']),
            hud_title_outline_color=Color.from_json(json_data['hud_title_outline_color']),
            visor_menu_title_foreground_color=Color.from_json(json_data['visor_menu_title_foreground_color']),
            visor_menu_title_outline_color=Color.from_json(json_data['visor_menu_title_outline_color']),
            beam_menu_title_foreground_color=Color.from_json(json_data['beam_menu_title_foreground_color']),
            beam_menu_title_outline_color=Color.from_json(json_data['beam_menu_title_outline_color']),
            visor_beam_menu_icon_selected_color=Color.from_json(json_data['visor_beam_menu_icon_selected_color']),
            visor_beam_menu_icon_unselected_color=Color.from_json(json_data['visor_beam_menu_icon_unselected_color']),
            visor_menu_icon_color0=Color.from_json(json_data['visor_menu_icon_color0']),
            visor_menu_icon_color1=Color.from_json(json_data['visor_menu_icon_color1']),
            visor_menu_icon_color2=Color.from_json(json_data['visor_menu_icon_color2']),
            visor_menu_icon_color3=Color.from_json(json_data['visor_menu_icon_color3']),
            beam_menu_icon_color0=Color.from_json(json_data['beam_menu_icon_color0']),
            beam_menu_icon_color1=Color.from_json(json_data['beam_menu_icon_color1']),
            beam_menu_icon_color2=Color.from_json(json_data['beam_menu_icon_color2']),
            beam_menu_icon_color3=Color.from_json(json_data['beam_menu_icon_color3']),
            energy_warning_color=Color.from_json(json_data['energy_warning_color']),
            threat_warning_color=Color.from_json(json_data['threat_warning_color']),
            missile_warning_color=Color.from_json(json_data['missile_warning_color']),
            missle_depletion_color=Color.from_json(json_data['missle_depletion_color']),
            threat_bar_filled_color=Color.from_json(json_data['threat_bar_filled_color']),
            threat_bar_shadow_color=Color.from_json(json_data['threat_bar_shadow_color']),
            threat_bar_empty_color=Color.from_json(json_data['threat_bar_empty_color']),
            missile_bar_filled_color=Color.from_json(json_data['missile_bar_filled_color']),
            missile_bar_shadow_color=Color.from_json(json_data['missile_bar_shadow_color']),
            missile_bar_empty_color=Color.from_json(json_data['missile_bar_empty_color']),
            threat_group_color=Color.from_json(json_data['threat_group_color']),
            free_look_bar_color=Color.from_json(json_data['free_look_bar_color']),
            hud_bar_deco_color=Color.from_json(json_data['hud_bar_deco_color']),
            unknown_0xf4379cf4=Color.from_json(json_data['unknown_0xf4379cf4']),
            threat_group_inactive_color=Color.from_json(json_data['threat_group_inactive_color']),
            missile_group_inactive_color=Color.from_json(json_data['missile_group_inactive_color']),
            missile_group_combo_charge_color=Color.from_json(json_data['missile_group_combo_charge_color']),
            missile_group_non_combo_charge_color=Color.from_json(json_data['missile_group_non_combo_charge_color']),
            missile_group_combo_activated_color=Color.from_json(json_data['missile_group_combo_activated_color']),
            free_look_tick_color=Color.from_json(json_data['free_look_tick_color']),
            free_look_digits_foreground_color=Color.from_json(json_data['free_look_digits_foreground_color']),
            free_look_digits_outline_color=Color.from_json(json_data['free_look_digits_outline_color']),
            unknown_0x8b0a4c90=Color.from_json(json_data['unknown_0x8b0a4c90']),
            energy_warning_outline_color=Color.from_json(json_data['energy_warning_outline_color']),
            threat_warning_outline_color=Color.from_json(json_data['threat_warning_outline_color']),
            missile_warning_outline_color=Color.from_json(json_data['missile_warning_outline_color']),
            helmet_light_ambient_color=Color.from_json(json_data['helmet_light_ambient_color']),
            flash_pass_color=Color.from_json(json_data['flash_pass_color']),
            scan_window_frame_base_color=Color.from_json(json_data['scan_window_frame_base_color']),
            scan_window_frame_active_color=Color.from_json(json_data['scan_window_frame_active_color']),
            scan_window_frame_flash_add_color=Color.from_json(json_data['scan_window_frame_flash_add_color']),
            unknown_0x18717fa7=Color.from_json(json_data['unknown_0x18717fa7']),
            unknown_0x8b7d7378=Color.from_json(json_data['unknown_0x8b7d7378']),
            unknown_0x867b01a2=Color.from_json(json_data['unknown_0x867b01a2']),
            scan_hud_hierarchy_frame_color=Color.from_json(json_data['scan_hud_hierarchy_frame_color']),
            scan_hud_hierarchy_inactive_frame_color=Color.from_json(json_data['scan_hud_hierarchy_inactive_frame_color']),
            scan_hud_hierarchy_text_frame_color=Color.from_json(json_data['scan_hud_hierarchy_text_frame_color']),
            scan_hud_hierarchy_final_text_frame_color=Color.from_json(json_data['scan_hud_hierarchy_final_text_frame_color']),
            scan_hud_hierarchy_flash_icon_color=Color.from_json(json_data['scan_hud_hierarchy_flash_icon_color']),
            scan_hud_hierarchy_complete_flash_icon_color=Color.from_json(json_data['scan_hud_hierarchy_complete_flash_icon_color']),
            scan_hud_hierarchy_flash_flash_icon_color=Color.from_json(json_data['scan_hud_hierarchy_flash_flash_icon_color']),
            scan_hud_hierarchy_text_color=Color.from_json(json_data['scan_hud_hierarchy_text_color']),
            scan_hud_hierarchy_final_text_color=Color.from_json(json_data['scan_hud_hierarchy_final_text_color']),
            scan_hud_hierarchy_percent_text_color=Color.from_json(json_data['scan_hud_hierarchy_percent_text_color']),
            scan_hud_hierarchy_bar_meter_color=Color.from_json(json_data['scan_hud_hierarchy_bar_meter_color']),
            dark_visor_helmet_light_modulate_color=Color.from_json(json_data['dark_visor_helmet_light_modulate_color']),
            metroid_suck_pulse_color=Color.from_json(json_data['metroid_suck_pulse_color']),
            unknown_0xce7c9d8d=Color.from_json(json_data['unknown_0xce7c9d8d']),
            energy_bar_damage_color=Color.from_json(json_data['energy_bar_damage_color']),
            x_ray_clamps_color=Color.from_json(json_data['x_ray_clamps_color']),
            x_ray_holo_grid_color=Color.from_json(json_data['x_ray_holo_grid_color']),
            x_ray_seeker_color=Color.from_json(json_data['x_ray_seeker_color']),
            x_ray_seeker_ticks_color=Color.from_json(json_data['x_ray_seeker_ticks_color']),
            x_ray_seeker_ticks_outer_color=Color.from_json(json_data['x_ray_seeker_ticks_outer_color']),
            x_ray_top_puzzle_color=Color.from_json(json_data['x_ray_top_puzzle_color']),
            x_ray_bottom_puzzle_color=Color.from_json(json_data['x_ray_bottom_puzzle_color']),
            x_ray_left_puzzle_color=Color.from_json(json_data['x_ray_left_puzzle_color']),
            x_ray_right_puzzle_color=Color.from_json(json_data['x_ray_right_puzzle_color']),
            x_ray_corner_color=Color.from_json(json_data['x_ray_corner_color']),
            x_ray_threat_digits_foreground_color=Color.from_json(json_data['x_ray_threat_digits_foreground_color']),
            x_ray_threat_digits_outline_color=Color.from_json(json_data['x_ray_threat_digits_outline_color']),
            x_ray_missile_digits_foreground_color=Color.from_json(json_data['x_ray_missile_digits_foreground_color']),
            x_ray_missile_digits_outline_color=Color.from_json(json_data['x_ray_missile_digits_outline_color']),
            x_ray_threat_bar_filled_color=Color.from_json(json_data['x_ray_threat_bar_filled_color']),
            x_ray_threat_bar_empty_color=Color.from_json(json_data['x_ray_threat_bar_empty_color']),
            x_ray_missile_bar_filled_color=Color.from_json(json_data['x_ray_missile_bar_filled_color']),
            x_ray_missile_bar_empty_color=Color.from_json(json_data['x_ray_missile_bar_empty_color']),
            scan_download_square_color=Color.from_json(json_data['scan_download_square_color']),
            scan_dot_color=Color.from_json(json_data['scan_dot_color']),
            morph_ball_power_bomb_digits_foreground_color=Color.from_json(json_data['morph_ball_power_bomb_digits_foreground_color']),
            morph_ball_power_bomb_digits_outline_color=Color.from_json(json_data['morph_ball_power_bomb_digits_outline_color']),
            morph_ball_energy_word_color=Color.from_json(json_data['morph_ball_energy_word_color']),
            morph_ball_bomb_counter_filled_color=Color.from_json(json_data['morph_ball_bomb_counter_filled_color']),
            morph_ball_bomb_counter_empty_color=Color.from_json(json_data['morph_ball_bomb_counter_empty_color']),
            morph_ball_power_bomb_icon_color=Color.from_json(json_data['morph_ball_power_bomb_icon_color']),
            morph_ball_bomb_word_color=Color.from_json(json_data['morph_ball_bomb_word_color']),
            morph_ball_energy_deco_color=Color.from_json(json_data['morph_ball_energy_deco_color']),
            morph_ball_bomb_deco_color=Color.from_json(json_data['morph_ball_bomb_deco_color']),
            morph_ball_empty_power_bomb_digits_foreground_colorr=Color.from_json(json_data['morph_ball_empty_power_bomb_digits_foreground_colorr']),
            morph_ball_empty_power_bomb_digits_outline_color=Color.from_json(json_data['morph_ball_empty_power_bomb_digits_outline_color']),
            morph_ball_empty_power_bomb_icon_color=Color.from_json(json_data['morph_ball_empty_power_bomb_icon_color']),
            scan_panel_color=Color.from_json(json_data['scan_panel_color']),
            unknown_0x96f650c3=Color.from_json(json_data['unknown_0x96f650c3']),
            scan_images_color=Color.from_json(json_data['scan_images_color']),
            unknown_0xd3bafaf5=Color.from_json(json_data['unknown_0xd3bafaf5']),
            threat_group_damage_color=Color.from_json(json_data['threat_group_damage_color']),
            coundown_foreground_color=Color.from_json(json_data['coundown_foreground_color']),
            coundown_outline_color=Color.from_json(json_data['coundown_outline_color']),
            critical_scan_object_indicator_in_range_color=Color.from_json(json_data['critical_scan_object_indicator_in_range_color']),
            critical_scan_object_indicator_out_of_range_color=Color.from_json(json_data['critical_scan_object_indicator_out_of_range_color']),
            noncritical_scan_object_indicator_in_range_color=Color.from_json(json_data['noncritical_scan_object_indicator_in_range_color']),
            noncritical_scan_object_indicator_out_of_range_color=Color.from_json(json_data['noncritical_scan_object_indicator_out_of_range_color']),
            scan_seeker_color=Color.from_json(json_data['scan_seeker_color']),
            thermal_threat_digits_outline_color=Color.from_json(json_data['thermal_threat_digits_outline_color']),
            thermal_missile_digits_outline_color=Color.from_json(json_data['thermal_missile_digits_outline_color']),
            combat_missile_digits_foreground_color=Color.from_json(json_data['combat_missile_digits_foreground_color']),
            combat_missile_digits_outline_color=Color.from_json(json_data['combat_missile_digits_outline_color']),
            thermal_deco_color=Color.from_json(json_data['thermal_deco_color']),
            thermal_deco_outline_color=Color.from_json(json_data['thermal_deco_outline_color']),
            thermal_trackers_color=Color.from_json(json_data['thermal_trackers_color']),
            thermal_lock_color=Color.from_json(json_data['thermal_lock_color']),
            log_book_color=Color.from_json(json_data['log_book_color']),
            inventory_equipped_color=Color.from_json(json_data['inventory_equipped_color']),
            dark_visor_deco_color=Color.from_json(json_data['dark_visor_deco_color']),
            light_ammo_tank_full_selected_color=Color.from_json(json_data['light_ammo_tank_full_selected_color']),
            light_ammo_tank_full_unselected_color=Color.from_json(json_data['light_ammo_tank_full_unselected_color']),
            light_ammo_tank_emptyl_selected_color=Color.from_json(json_data['light_ammo_tank_emptyl_selected_color']),
            light_ammo_tank_empty_unselected_color=Color.from_json(json_data['light_ammo_tank_empty_unselected_color']),
            light_ammo_meter_selected_fill_color=Color.from_json(json_data['light_ammo_meter_selected_fill_color']),
            light_ammo_meter_selected_shadow_color=Color.from_json(json_data['light_ammo_meter_selected_shadow_color']),
            light_ammo_meter_unselected_fill_color=Color.from_json(json_data['light_ammo_meter_unselected_fill_color']),
            light_ammo_meter_unselected_shadow_color=Color.from_json(json_data['light_ammo_meter_unselected_shadow_color']),
            light_ammo_icon_selected_color=Color.from_json(json_data['light_ammo_icon_selected_color']),
            light_ammo_icon_unselected_color=Color.from_json(json_data['light_ammo_icon_unselected_color']),
            light_ammo_digits_outline_color=Color.from_json(json_data['light_ammo_digits_outline_color']),
            light_ammo_digits_selected_color=Color.from_json(json_data['light_ammo_digits_selected_color']),
            light_ammo_digits_unselected_color=Color.from_json(json_data['light_ammo_digits_unselected_color']),
            light_ammo_change_flash=Color.from_json(json_data['light_ammo_change_flash']),
            light_ammo_tank_warning_color=Color.from_json(json_data['light_ammo_tank_warning_color']),
            light_ammo_meter_warning_color=Color.from_json(json_data['light_ammo_meter_warning_color']),
            light_ammo_digit_warning_color=Color.from_json(json_data['light_ammo_digit_warning_color']),
            light_ammo_depletion_color=Color.from_json(json_data['light_ammo_depletion_color']),
            light_ammo_empty_tank_warning_color=Color.from_json(json_data['light_ammo_empty_tank_warning_color']),
            dark_ammo_tank_full_selected_color=Color.from_json(json_data['dark_ammo_tank_full_selected_color']),
            dark_ammo_tank_full_unselected_color=Color.from_json(json_data['dark_ammo_tank_full_unselected_color']),
            dark_ammo_tank_emptyl_selected_color=Color.from_json(json_data['dark_ammo_tank_emptyl_selected_color']),
            dark_ammo_tank_empty_unselected_color=Color.from_json(json_data['dark_ammo_tank_empty_unselected_color']),
            dark_ammo_meter_selected_fill_color=Color.from_json(json_data['dark_ammo_meter_selected_fill_color']),
            dark_ammo_meter_selected_shadow_color=Color.from_json(json_data['dark_ammo_meter_selected_shadow_color']),
            dark_ammo_meter_unselected_fill_color=Color.from_json(json_data['dark_ammo_meter_unselected_fill_color']),
            dark_ammo_meter_unselected_shadow_color=Color.from_json(json_data['dark_ammo_meter_unselected_shadow_color']),
            dark_ammo_icon_selected_color=Color.from_json(json_data['dark_ammo_icon_selected_color']),
            dark_ammo_icon_unselected_color=Color.from_json(json_data['dark_ammo_icon_unselected_color']),
            dark_ammo_digits_outline_color=Color.from_json(json_data['dark_ammo_digits_outline_color']),
            dark_ammo_digits_selected_color=Color.from_json(json_data['dark_ammo_digits_selected_color']),
            dark_ammo_digits_unselected_color=Color.from_json(json_data['dark_ammo_digits_unselected_color']),
            dark_ammo_change_flash=Color.from_json(json_data['dark_ammo_change_flash']),
            num_huds=json_data['num_huds'],
            dark_ammo_tank_warning_color=Color.from_json(json_data['dark_ammo_tank_warning_color']),
            dark_ammo_meter_warning_color=Color.from_json(json_data['dark_ammo_meter_warning_color']),
            dark_ammo_digit_warning_color=Color.from_json(json_data['dark_ammo_digit_warning_color']),
            dark_ammo_depletion_color=Color.from_json(json_data['dark_ammo_depletion_color']),
            dark_ammo_empty_tank_warning_color=Color.from_json(json_data['dark_ammo_empty_tank_warning_color']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'pause_screen_bg_modulate_color': self.pause_screen_bg_modulate_color.to_json(),
            'radar_boundary_ring_color': self.radar_boundary_ring_color.to_json(),
            'radar_player_paint_color': self.radar_player_paint_color.to_json(),
            'radar_enemy_paint_color': self.radar_enemy_paint_color.to_json(),
            'echo_ping_radar_color': self.echo_ping_radar_color.to_json(),
            'radar_friend_team_paint_color': self.radar_friend_team_paint_color.to_json(),
            'radar_enemy_team_paint_color': self.radar_enemy_team_paint_color.to_json(),
            'hud_memo_text_foreground_color': self.hud_memo_text_foreground_color.to_json(),
            'hud_memo_text_outline_color': self.hud_memo_text_outline_color.to_json(),
            'hud_decorative_color': self.hud_decorative_color.to_json(),
            'hud_glow_color': self.hud_glow_color.to_json(),
            'hud_energy_deco_color': self.hud_energy_deco_color.to_json(),
            'hud_missile_group_active_color': self.hud_missile_group_active_color.to_json(),
            'selected_visor_beam_color': self.selected_visor_beam_color.to_json(),
            'unselected_visor_beam_color': self.unselected_visor_beam_color.to_json(),
            'energy_bar_low_filled_color': self.energy_bar_low_filled_color.to_json(),
            'energy_bar_low_shadow_color': self.energy_bar_low_shadow_color.to_json(),
            'energy_bar_low_empty_color': self.energy_bar_low_empty_color.to_json(),
            'hud_damage_modulate_color': self.hud_damage_modulate_color.to_json(),
            'damage_indicator_color': self.damage_indicator_color.to_json(),
            'hud_title_foreground_color': self.hud_title_foreground_color.to_json(),
            'hud_title_outline_color': self.hud_title_outline_color.to_json(),
            'visor_menu_title_foreground_color': self.visor_menu_title_foreground_color.to_json(),
            'visor_menu_title_outline_color': self.visor_menu_title_outline_color.to_json(),
            'beam_menu_title_foreground_color': self.beam_menu_title_foreground_color.to_json(),
            'beam_menu_title_outline_color': self.beam_menu_title_outline_color.to_json(),
            'visor_beam_menu_icon_selected_color': self.visor_beam_menu_icon_selected_color.to_json(),
            'visor_beam_menu_icon_unselected_color': self.visor_beam_menu_icon_unselected_color.to_json(),
            'visor_menu_icon_color0': self.visor_menu_icon_color0.to_json(),
            'visor_menu_icon_color1': self.visor_menu_icon_color1.to_json(),
            'visor_menu_icon_color2': self.visor_menu_icon_color2.to_json(),
            'visor_menu_icon_color3': self.visor_menu_icon_color3.to_json(),
            'beam_menu_icon_color0': self.beam_menu_icon_color0.to_json(),
            'beam_menu_icon_color1': self.beam_menu_icon_color1.to_json(),
            'beam_menu_icon_color2': self.beam_menu_icon_color2.to_json(),
            'beam_menu_icon_color3': self.beam_menu_icon_color3.to_json(),
            'energy_warning_color': self.energy_warning_color.to_json(),
            'threat_warning_color': self.threat_warning_color.to_json(),
            'missile_warning_color': self.missile_warning_color.to_json(),
            'missle_depletion_color': self.missle_depletion_color.to_json(),
            'threat_bar_filled_color': self.threat_bar_filled_color.to_json(),
            'threat_bar_shadow_color': self.threat_bar_shadow_color.to_json(),
            'threat_bar_empty_color': self.threat_bar_empty_color.to_json(),
            'missile_bar_filled_color': self.missile_bar_filled_color.to_json(),
            'missile_bar_shadow_color': self.missile_bar_shadow_color.to_json(),
            'missile_bar_empty_color': self.missile_bar_empty_color.to_json(),
            'threat_group_color': self.threat_group_color.to_json(),
            'free_look_bar_color': self.free_look_bar_color.to_json(),
            'hud_bar_deco_color': self.hud_bar_deco_color.to_json(),
            'unknown_0xf4379cf4': self.unknown_0xf4379cf4.to_json(),
            'threat_group_inactive_color': self.threat_group_inactive_color.to_json(),
            'missile_group_inactive_color': self.missile_group_inactive_color.to_json(),
            'missile_group_combo_charge_color': self.missile_group_combo_charge_color.to_json(),
            'missile_group_non_combo_charge_color': self.missile_group_non_combo_charge_color.to_json(),
            'missile_group_combo_activated_color': self.missile_group_combo_activated_color.to_json(),
            'free_look_tick_color': self.free_look_tick_color.to_json(),
            'free_look_digits_foreground_color': self.free_look_digits_foreground_color.to_json(),
            'free_look_digits_outline_color': self.free_look_digits_outline_color.to_json(),
            'unknown_0x8b0a4c90': self.unknown_0x8b0a4c90.to_json(),
            'energy_warning_outline_color': self.energy_warning_outline_color.to_json(),
            'threat_warning_outline_color': self.threat_warning_outline_color.to_json(),
            'missile_warning_outline_color': self.missile_warning_outline_color.to_json(),
            'helmet_light_ambient_color': self.helmet_light_ambient_color.to_json(),
            'flash_pass_color': self.flash_pass_color.to_json(),
            'scan_window_frame_base_color': self.scan_window_frame_base_color.to_json(),
            'scan_window_frame_active_color': self.scan_window_frame_active_color.to_json(),
            'scan_window_frame_flash_add_color': self.scan_window_frame_flash_add_color.to_json(),
            'unknown_0x18717fa7': self.unknown_0x18717fa7.to_json(),
            'unknown_0x8b7d7378': self.unknown_0x8b7d7378.to_json(),
            'unknown_0x867b01a2': self.unknown_0x867b01a2.to_json(),
            'scan_hud_hierarchy_frame_color': self.scan_hud_hierarchy_frame_color.to_json(),
            'scan_hud_hierarchy_inactive_frame_color': self.scan_hud_hierarchy_inactive_frame_color.to_json(),
            'scan_hud_hierarchy_text_frame_color': self.scan_hud_hierarchy_text_frame_color.to_json(),
            'scan_hud_hierarchy_final_text_frame_color': self.scan_hud_hierarchy_final_text_frame_color.to_json(),
            'scan_hud_hierarchy_flash_icon_color': self.scan_hud_hierarchy_flash_icon_color.to_json(),
            'scan_hud_hierarchy_complete_flash_icon_color': self.scan_hud_hierarchy_complete_flash_icon_color.to_json(),
            'scan_hud_hierarchy_flash_flash_icon_color': self.scan_hud_hierarchy_flash_flash_icon_color.to_json(),
            'scan_hud_hierarchy_text_color': self.scan_hud_hierarchy_text_color.to_json(),
            'scan_hud_hierarchy_final_text_color': self.scan_hud_hierarchy_final_text_color.to_json(),
            'scan_hud_hierarchy_percent_text_color': self.scan_hud_hierarchy_percent_text_color.to_json(),
            'scan_hud_hierarchy_bar_meter_color': self.scan_hud_hierarchy_bar_meter_color.to_json(),
            'dark_visor_helmet_light_modulate_color': self.dark_visor_helmet_light_modulate_color.to_json(),
            'metroid_suck_pulse_color': self.metroid_suck_pulse_color.to_json(),
            'unknown_0xce7c9d8d': self.unknown_0xce7c9d8d.to_json(),
            'energy_bar_damage_color': self.energy_bar_damage_color.to_json(),
            'x_ray_clamps_color': self.x_ray_clamps_color.to_json(),
            'x_ray_holo_grid_color': self.x_ray_holo_grid_color.to_json(),
            'x_ray_seeker_color': self.x_ray_seeker_color.to_json(),
            'x_ray_seeker_ticks_color': self.x_ray_seeker_ticks_color.to_json(),
            'x_ray_seeker_ticks_outer_color': self.x_ray_seeker_ticks_outer_color.to_json(),
            'x_ray_top_puzzle_color': self.x_ray_top_puzzle_color.to_json(),
            'x_ray_bottom_puzzle_color': self.x_ray_bottom_puzzle_color.to_json(),
            'x_ray_left_puzzle_color': self.x_ray_left_puzzle_color.to_json(),
            'x_ray_right_puzzle_color': self.x_ray_right_puzzle_color.to_json(),
            'x_ray_corner_color': self.x_ray_corner_color.to_json(),
            'x_ray_threat_digits_foreground_color': self.x_ray_threat_digits_foreground_color.to_json(),
            'x_ray_threat_digits_outline_color': self.x_ray_threat_digits_outline_color.to_json(),
            'x_ray_missile_digits_foreground_color': self.x_ray_missile_digits_foreground_color.to_json(),
            'x_ray_missile_digits_outline_color': self.x_ray_missile_digits_outline_color.to_json(),
            'x_ray_threat_bar_filled_color': self.x_ray_threat_bar_filled_color.to_json(),
            'x_ray_threat_bar_empty_color': self.x_ray_threat_bar_empty_color.to_json(),
            'x_ray_missile_bar_filled_color': self.x_ray_missile_bar_filled_color.to_json(),
            'x_ray_missile_bar_empty_color': self.x_ray_missile_bar_empty_color.to_json(),
            'scan_download_square_color': self.scan_download_square_color.to_json(),
            'scan_dot_color': self.scan_dot_color.to_json(),
            'morph_ball_power_bomb_digits_foreground_color': self.morph_ball_power_bomb_digits_foreground_color.to_json(),
            'morph_ball_power_bomb_digits_outline_color': self.morph_ball_power_bomb_digits_outline_color.to_json(),
            'morph_ball_energy_word_color': self.morph_ball_energy_word_color.to_json(),
            'morph_ball_bomb_counter_filled_color': self.morph_ball_bomb_counter_filled_color.to_json(),
            'morph_ball_bomb_counter_empty_color': self.morph_ball_bomb_counter_empty_color.to_json(),
            'morph_ball_power_bomb_icon_color': self.morph_ball_power_bomb_icon_color.to_json(),
            'morph_ball_bomb_word_color': self.morph_ball_bomb_word_color.to_json(),
            'morph_ball_energy_deco_color': self.morph_ball_energy_deco_color.to_json(),
            'morph_ball_bomb_deco_color': self.morph_ball_bomb_deco_color.to_json(),
            'morph_ball_empty_power_bomb_digits_foreground_colorr': self.morph_ball_empty_power_bomb_digits_foreground_colorr.to_json(),
            'morph_ball_empty_power_bomb_digits_outline_color': self.morph_ball_empty_power_bomb_digits_outline_color.to_json(),
            'morph_ball_empty_power_bomb_icon_color': self.morph_ball_empty_power_bomb_icon_color.to_json(),
            'scan_panel_color': self.scan_panel_color.to_json(),
            'unknown_0x96f650c3': self.unknown_0x96f650c3.to_json(),
            'scan_images_color': self.scan_images_color.to_json(),
            'unknown_0xd3bafaf5': self.unknown_0xd3bafaf5.to_json(),
            'threat_group_damage_color': self.threat_group_damage_color.to_json(),
            'coundown_foreground_color': self.coundown_foreground_color.to_json(),
            'coundown_outline_color': self.coundown_outline_color.to_json(),
            'critical_scan_object_indicator_in_range_color': self.critical_scan_object_indicator_in_range_color.to_json(),
            'critical_scan_object_indicator_out_of_range_color': self.critical_scan_object_indicator_out_of_range_color.to_json(),
            'noncritical_scan_object_indicator_in_range_color': self.noncritical_scan_object_indicator_in_range_color.to_json(),
            'noncritical_scan_object_indicator_out_of_range_color': self.noncritical_scan_object_indicator_out_of_range_color.to_json(),
            'scan_seeker_color': self.scan_seeker_color.to_json(),
            'thermal_threat_digits_outline_color': self.thermal_threat_digits_outline_color.to_json(),
            'thermal_missile_digits_outline_color': self.thermal_missile_digits_outline_color.to_json(),
            'combat_missile_digits_foreground_color': self.combat_missile_digits_foreground_color.to_json(),
            'combat_missile_digits_outline_color': self.combat_missile_digits_outline_color.to_json(),
            'thermal_deco_color': self.thermal_deco_color.to_json(),
            'thermal_deco_outline_color': self.thermal_deco_outline_color.to_json(),
            'thermal_trackers_color': self.thermal_trackers_color.to_json(),
            'thermal_lock_color': self.thermal_lock_color.to_json(),
            'log_book_color': self.log_book_color.to_json(),
            'inventory_equipped_color': self.inventory_equipped_color.to_json(),
            'dark_visor_deco_color': self.dark_visor_deco_color.to_json(),
            'light_ammo_tank_full_selected_color': self.light_ammo_tank_full_selected_color.to_json(),
            'light_ammo_tank_full_unselected_color': self.light_ammo_tank_full_unselected_color.to_json(),
            'light_ammo_tank_emptyl_selected_color': self.light_ammo_tank_emptyl_selected_color.to_json(),
            'light_ammo_tank_empty_unselected_color': self.light_ammo_tank_empty_unselected_color.to_json(),
            'light_ammo_meter_selected_fill_color': self.light_ammo_meter_selected_fill_color.to_json(),
            'light_ammo_meter_selected_shadow_color': self.light_ammo_meter_selected_shadow_color.to_json(),
            'light_ammo_meter_unselected_fill_color': self.light_ammo_meter_unselected_fill_color.to_json(),
            'light_ammo_meter_unselected_shadow_color': self.light_ammo_meter_unselected_shadow_color.to_json(),
            'light_ammo_icon_selected_color': self.light_ammo_icon_selected_color.to_json(),
            'light_ammo_icon_unselected_color': self.light_ammo_icon_unselected_color.to_json(),
            'light_ammo_digits_outline_color': self.light_ammo_digits_outline_color.to_json(),
            'light_ammo_digits_selected_color': self.light_ammo_digits_selected_color.to_json(),
            'light_ammo_digits_unselected_color': self.light_ammo_digits_unselected_color.to_json(),
            'light_ammo_change_flash': self.light_ammo_change_flash.to_json(),
            'light_ammo_tank_warning_color': self.light_ammo_tank_warning_color.to_json(),
            'light_ammo_meter_warning_color': self.light_ammo_meter_warning_color.to_json(),
            'light_ammo_digit_warning_color': self.light_ammo_digit_warning_color.to_json(),
            'light_ammo_depletion_color': self.light_ammo_depletion_color.to_json(),
            'light_ammo_empty_tank_warning_color': self.light_ammo_empty_tank_warning_color.to_json(),
            'dark_ammo_tank_full_selected_color': self.dark_ammo_tank_full_selected_color.to_json(),
            'dark_ammo_tank_full_unselected_color': self.dark_ammo_tank_full_unselected_color.to_json(),
            'dark_ammo_tank_emptyl_selected_color': self.dark_ammo_tank_emptyl_selected_color.to_json(),
            'dark_ammo_tank_empty_unselected_color': self.dark_ammo_tank_empty_unselected_color.to_json(),
            'dark_ammo_meter_selected_fill_color': self.dark_ammo_meter_selected_fill_color.to_json(),
            'dark_ammo_meter_selected_shadow_color': self.dark_ammo_meter_selected_shadow_color.to_json(),
            'dark_ammo_meter_unselected_fill_color': self.dark_ammo_meter_unselected_fill_color.to_json(),
            'dark_ammo_meter_unselected_shadow_color': self.dark_ammo_meter_unselected_shadow_color.to_json(),
            'dark_ammo_icon_selected_color': self.dark_ammo_icon_selected_color.to_json(),
            'dark_ammo_icon_unselected_color': self.dark_ammo_icon_unselected_color.to_json(),
            'dark_ammo_digits_outline_color': self.dark_ammo_digits_outline_color.to_json(),
            'dark_ammo_digits_selected_color': self.dark_ammo_digits_selected_color.to_json(),
            'dark_ammo_digits_unselected_color': self.dark_ammo_digits_unselected_color.to_json(),
            'dark_ammo_change_flash': self.dark_ammo_change_flash.to_json(),
            'num_huds': self.num_huds,
            'dark_ammo_tank_warning_color': self.dark_ammo_tank_warning_color.to_json(),
            'dark_ammo_meter_warning_color': self.dark_ammo_meter_warning_color.to_json(),
            'dark_ammo_digit_warning_color': self.dark_ammo_digit_warning_color.to_json(),
            'dark_ammo_depletion_color': self.dark_ammo_depletion_color.to_json(),
            'dark_ammo_empty_tank_warning_color': self.dark_ammo_empty_tank_warning_color.to_json(),
        }


def _decode_pause_screen_bg_modulate_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_radar_boundary_ring_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_radar_player_paint_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_radar_enemy_paint_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_echo_ping_radar_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_radar_friend_team_paint_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_radar_enemy_team_paint_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_hud_memo_text_foreground_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_hud_memo_text_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_hud_decorative_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_hud_glow_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_hud_energy_deco_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_hud_missile_group_active_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_selected_visor_beam_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unselected_visor_beam_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_bar_low_filled_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_bar_low_shadow_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_bar_low_empty_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_hud_damage_modulate_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_damage_indicator_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_hud_title_foreground_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_hud_title_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_visor_menu_title_foreground_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_visor_menu_title_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_beam_menu_title_foreground_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_beam_menu_title_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_visor_beam_menu_icon_selected_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_visor_beam_menu_icon_unselected_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_visor_menu_icon_color0(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_visor_menu_icon_color1(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_visor_menu_icon_color2(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_visor_menu_icon_color3(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_beam_menu_icon_color0(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_beam_menu_icon_color1(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_beam_menu_icon_color2(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_beam_menu_icon_color3(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_warning_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_threat_warning_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missile_warning_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missle_depletion_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_threat_bar_filled_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_threat_bar_shadow_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_threat_bar_empty_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missile_bar_filled_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missile_bar_shadow_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missile_bar_empty_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_threat_group_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_free_look_bar_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_hud_bar_deco_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xf4379cf4(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_threat_group_inactive_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missile_group_inactive_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missile_group_combo_charge_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missile_group_non_combo_charge_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missile_group_combo_activated_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_free_look_tick_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_free_look_digits_foreground_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_free_look_digits_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x8b0a4c90(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_warning_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_threat_warning_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_missile_warning_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_helmet_light_ambient_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_flash_pass_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_window_frame_base_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_window_frame_active_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_window_frame_flash_add_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x18717fa7(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x8b7d7378(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x867b01a2(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_hud_hierarchy_frame_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_hud_hierarchy_inactive_frame_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_hud_hierarchy_text_frame_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_hud_hierarchy_final_text_frame_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_hud_hierarchy_flash_icon_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_hud_hierarchy_complete_flash_icon_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_hud_hierarchy_flash_flash_icon_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_hud_hierarchy_text_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_hud_hierarchy_final_text_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_hud_hierarchy_percent_text_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_hud_hierarchy_bar_meter_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_visor_helmet_light_modulate_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_metroid_suck_pulse_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xce7c9d8d(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_energy_bar_damage_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_clamps_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_holo_grid_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_seeker_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_seeker_ticks_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_seeker_ticks_outer_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_top_puzzle_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_bottom_puzzle_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_left_puzzle_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_right_puzzle_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_corner_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_threat_digits_foreground_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_threat_digits_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_missile_digits_foreground_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_missile_digits_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_threat_bar_filled_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_threat_bar_empty_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_missile_bar_filled_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_x_ray_missile_bar_empty_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_download_square_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_dot_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_morph_ball_power_bomb_digits_foreground_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_morph_ball_power_bomb_digits_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_morph_ball_energy_word_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_morph_ball_bomb_counter_filled_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_morph_ball_bomb_counter_empty_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_morph_ball_power_bomb_icon_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_morph_ball_bomb_word_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_morph_ball_energy_deco_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_morph_ball_bomb_deco_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_morph_ball_empty_power_bomb_digits_foreground_colorr(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_morph_ball_empty_power_bomb_digits_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_morph_ball_empty_power_bomb_icon_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_panel_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0x96f650c3(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_images_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown_0xd3bafaf5(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_threat_group_damage_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_coundown_foreground_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_coundown_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_critical_scan_object_indicator_in_range_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_critical_scan_object_indicator_out_of_range_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_noncritical_scan_object_indicator_in_range_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_noncritical_scan_object_indicator_out_of_range_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_seeker_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_thermal_threat_digits_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_thermal_missile_digits_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_combat_missile_digits_foreground_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_combat_missile_digits_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_thermal_deco_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_thermal_deco_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_thermal_trackers_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_thermal_lock_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_log_book_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_inventory_equipped_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_visor_deco_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_light_ammo_tank_full_selected_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_light_ammo_tank_full_unselected_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_light_ammo_tank_emptyl_selected_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_light_ammo_tank_empty_unselected_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_light_ammo_meter_selected_fill_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_light_ammo_meter_selected_shadow_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_light_ammo_meter_unselected_fill_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_light_ammo_meter_unselected_shadow_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_light_ammo_icon_selected_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_light_ammo_icon_unselected_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_light_ammo_digits_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_light_ammo_digits_selected_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_light_ammo_digits_unselected_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_light_ammo_change_flash(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_light_ammo_tank_warning_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_light_ammo_meter_warning_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_light_ammo_digit_warning_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_light_ammo_depletion_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_light_ammo_empty_tank_warning_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_ammo_tank_full_selected_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_ammo_tank_full_unselected_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_ammo_tank_emptyl_selected_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_ammo_tank_empty_unselected_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_ammo_meter_selected_fill_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_ammo_meter_selected_shadow_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_ammo_meter_unselected_fill_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_ammo_meter_unselected_shadow_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_ammo_icon_selected_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_ammo_icon_unselected_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_ammo_digits_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_ammo_digits_selected_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_ammo_digits_unselected_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_ammo_change_flash(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_ammo_tank_warning_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_ammo_meter_warning_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_ammo_digit_warning_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_ammo_depletion_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_ammo_empty_tank_warning_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x8ed04c36: ('pause_screen_bg_modulate_color', _decode_pause_screen_bg_modulate_color),
    0x166c22e0: ('radar_boundary_ring_color', _decode_radar_boundary_ring_color),
    0xcec78e81: ('radar_player_paint_color', _decode_radar_player_paint_color),
    0x91338f72: ('radar_enemy_paint_color', _decode_radar_enemy_paint_color),
    0x0d24ae6b: ('echo_ping_radar_color', _decode_echo_ping_radar_color),
    0xddc561eb: ('radar_friend_team_paint_color', _decode_radar_friend_team_paint_color),
    0x9be28150: ('radar_enemy_team_paint_color', _decode_radar_enemy_team_paint_color),
    0x2df1eb03: ('hud_memo_text_foreground_color', _decode_hud_memo_text_foreground_color),
    0xb5da30f4: ('hud_memo_text_outline_color', _decode_hud_memo_text_outline_color),
    0xc8ddc662: ('hud_decorative_color', _decode_hud_decorative_color),
    0x6991e2cd: ('hud_glow_color', _decode_hud_glow_color),
    0x5c336f85: ('hud_energy_deco_color', _decode_hud_energy_deco_color),
    0xdefca700: ('hud_missile_group_active_color', _decode_hud_missile_group_active_color),
    0xcb7ddaf4: ('selected_visor_beam_color', _decode_selected_visor_beam_color),
    0xf17911aa: ('unselected_visor_beam_color', _decode_unselected_visor_beam_color),
    0xa14c8d20: ('energy_bar_low_filled_color', _decode_energy_bar_low_filled_color),
    0xb4135cdd: ('energy_bar_low_shadow_color', _decode_energy_bar_low_shadow_color),
    0xe0290c48: ('energy_bar_low_empty_color', _decode_energy_bar_low_empty_color),
    0x1ec7f863: ('hud_damage_modulate_color', _decode_hud_damage_modulate_color),
    0xae1317d8: ('damage_indicator_color', _decode_damage_indicator_color),
    0x22b9b01e: ('hud_title_foreground_color', _decode_hud_title_foreground_color),
    0x70a2cd6e: ('hud_title_outline_color', _decode_hud_title_outline_color),
    0xe7070332: ('visor_menu_title_foreground_color', _decode_visor_menu_title_foreground_color),
    0x779c7b9c: ('visor_menu_title_outline_color', _decode_visor_menu_title_outline_color),
    0x13bd3b64: ('beam_menu_title_foreground_color', _decode_beam_menu_title_foreground_color),
    0x1531edd3: ('beam_menu_title_outline_color', _decode_beam_menu_title_outline_color),
    0x27d0c234: ('visor_beam_menu_icon_selected_color', _decode_visor_beam_menu_icon_selected_color),
    0xbaa6d6a1: ('visor_beam_menu_icon_unselected_color', _decode_visor_beam_menu_icon_unselected_color),
    0x59e416aa: ('visor_menu_icon_color0', _decode_visor_menu_icon_color0),
    0x92b8c50f: ('visor_menu_icon_color1', _decode_visor_menu_icon_color1),
    0x142cb7a1: ('visor_menu_icon_color2', _decode_visor_menu_icon_color2),
    0xdf706404: ('visor_menu_icon_color3', _decode_visor_menu_icon_color3),
    0x81269ee0: ('beam_menu_icon_color0', _decode_beam_menu_icon_color0),
    0x4a7a4d45: ('beam_menu_icon_color1', _decode_beam_menu_icon_color1),
    0xccee3feb: ('beam_menu_icon_color2', _decode_beam_menu_icon_color2),
    0x07b2ec4e: ('beam_menu_icon_color3', _decode_beam_menu_icon_color3),
    0x6f6e9d6d: ('energy_warning_color', _decode_energy_warning_color),
    0xca68f68f: ('threat_warning_color', _decode_threat_warning_color),
    0x0c00a29f: ('missile_warning_color', _decode_missile_warning_color),
    0x83040135: ('missle_depletion_color', _decode_missle_depletion_color),
    0x1adea12b: ('threat_bar_filled_color', _decode_threat_bar_filled_color),
    0x0f8170d6: ('threat_bar_shadow_color', _decode_threat_bar_shadow_color),
    0x794204fd: ('threat_bar_empty_color', _decode_threat_bar_empty_color),
    0x3c1ae0ff: ('missile_bar_filled_color', _decode_missile_bar_filled_color),
    0x29453102: ('missile_bar_shadow_color', _decode_missile_bar_shadow_color),
    0x64337ccd: ('missile_bar_empty_color', _decode_missile_bar_empty_color),
    0x4b86c539: ('threat_group_color', _decode_threat_group_color),
    0xa6609cc5: ('free_look_bar_color', _decode_free_look_bar_color),
    0xbe3c29a1: ('hud_bar_deco_color', _decode_hud_bar_deco_color),
    0xf4379cf4: ('unknown_0xf4379cf4', _decode_unknown_0xf4379cf4),
    0x74e5ffa1: ('threat_group_inactive_color', _decode_threat_group_inactive_color),
    0xd110a12f: ('missile_group_inactive_color', _decode_missile_group_inactive_color),
    0xceb17cdf: ('missile_group_combo_charge_color', _decode_missile_group_combo_charge_color),
    0x4c5aff4f: ('missile_group_non_combo_charge_color', _decode_missile_group_non_combo_charge_color),
    0x0b17b693: ('missile_group_combo_activated_color', _decode_missile_group_combo_activated_color),
    0xfad063d5: ('free_look_tick_color', _decode_free_look_tick_color),
    0x2eafedf7: ('free_look_digits_foreground_color', _decode_free_look_digits_foreground_color),
    0x2a01734f: ('free_look_digits_outline_color', _decode_free_look_digits_outline_color),
    0x8b0a4c90: ('unknown_0x8b0a4c90', _decode_unknown_0x8b0a4c90),
    0xc4e17ca8: ('energy_warning_outline_color', _decode_energy_warning_outline_color),
    0xc7182898: ('threat_warning_outline_color', _decode_threat_warning_outline_color),
    0xcdbd73e1: ('missile_warning_outline_color', _decode_missile_warning_outline_color),
    0x78522461: ('helmet_light_ambient_color', _decode_helmet_light_ambient_color),
    0x6a839a97: ('flash_pass_color', _decode_flash_pass_color),
    0x79ea6f12: ('scan_window_frame_base_color', _decode_scan_window_frame_base_color),
    0xdc901206: ('scan_window_frame_active_color', _decode_scan_window_frame_active_color),
    0xc54fa7bc: ('scan_window_frame_flash_add_color', _decode_scan_window_frame_flash_add_color),
    0x18717fa7: ('unknown_0x18717fa7', _decode_unknown_0x18717fa7),
    0x8b7d7378: ('unknown_0x8b7d7378', _decode_unknown_0x8b7d7378),
    0x867b01a2: ('unknown_0x867b01a2', _decode_unknown_0x867b01a2),
    0x08be8347: ('scan_hud_hierarchy_frame_color', _decode_scan_hud_hierarchy_frame_color),
    0xe6ec3c8d: ('scan_hud_hierarchy_inactive_frame_color', _decode_scan_hud_hierarchy_inactive_frame_color),
    0x591cd695: ('scan_hud_hierarchy_text_frame_color', _decode_scan_hud_hierarchy_text_frame_color),
    0x26e1eb8c: ('scan_hud_hierarchy_final_text_frame_color', _decode_scan_hud_hierarchy_final_text_frame_color),
    0x63e9e374: ('scan_hud_hierarchy_flash_icon_color', _decode_scan_hud_hierarchy_flash_icon_color),
    0x738d9c43: ('scan_hud_hierarchy_complete_flash_icon_color', _decode_scan_hud_hierarchy_complete_flash_icon_color),
    0xba6c75a2: ('scan_hud_hierarchy_flash_flash_icon_color', _decode_scan_hud_hierarchy_flash_flash_icon_color),
    0xc37d11b7: ('scan_hud_hierarchy_text_color', _decode_scan_hud_hierarchy_text_color),
    0xef1ec40e: ('scan_hud_hierarchy_final_text_color', _decode_scan_hud_hierarchy_final_text_color),
    0x0ca7beb2: ('scan_hud_hierarchy_percent_text_color', _decode_scan_hud_hierarchy_percent_text_color),
    0x87d3ce8a: ('scan_hud_hierarchy_bar_meter_color', _decode_scan_hud_hierarchy_bar_meter_color),
    0xeb7eb756: ('dark_visor_helmet_light_modulate_color', _decode_dark_visor_helmet_light_modulate_color),
    0xe4c1bbeb: ('metroid_suck_pulse_color', _decode_metroid_suck_pulse_color),
    0xce7c9d8d: ('unknown_0xce7c9d8d', _decode_unknown_0xce7c9d8d),
    0x13490420: ('energy_bar_damage_color', _decode_energy_bar_damage_color),
    0xafe2d45d: ('x_ray_clamps_color', _decode_x_ray_clamps_color),
    0x2af5aa06: ('x_ray_holo_grid_color', _decode_x_ray_holo_grid_color),
    0xd3cbe846: ('x_ray_seeker_color', _decode_x_ray_seeker_color),
    0x507b51da: ('x_ray_seeker_ticks_color', _decode_x_ray_seeker_ticks_color),
    0xc61d97ef: ('x_ray_seeker_ticks_outer_color', _decode_x_ray_seeker_ticks_outer_color),
    0xaf0001cf: ('x_ray_top_puzzle_color', _decode_x_ray_top_puzzle_color),
    0x150a9b17: ('x_ray_bottom_puzzle_color', _decode_x_ray_bottom_puzzle_color),
    0xd66d715f: ('x_ray_left_puzzle_color', _decode_x_ray_left_puzzle_color),
    0xa8698fe8: ('x_ray_right_puzzle_color', _decode_x_ray_right_puzzle_color),
    0x4cb38e71: ('x_ray_corner_color', _decode_x_ray_corner_color),
    0x51c5aad9: ('x_ray_threat_digits_foreground_color', _decode_x_ray_threat_digits_foreground_color),
    0x60e8322b: ('x_ray_threat_digits_outline_color', _decode_x_ray_threat_digits_outline_color),
    0xa947a67c: ('x_ray_missile_digits_foreground_color', _decode_x_ray_missile_digits_foreground_color),
    0x421bae2a: ('x_ray_missile_digits_outline_color', _decode_x_ray_missile_digits_outline_color),
    0xf0049167: ('x_ray_threat_bar_filled_color', _decode_x_ray_threat_bar_filled_color),
    0x76357179: ('x_ray_threat_bar_empty_color', _decode_x_ray_threat_bar_empty_color),
    0x439a3774: ('x_ray_missile_bar_filled_color', _decode_x_ray_missile_bar_filled_color),
    0x8ee94c81: ('x_ray_missile_bar_empty_color', _decode_x_ray_missile_bar_empty_color),
    0xbb0897ea: ('scan_download_square_color', _decode_scan_download_square_color),
    0xc12cbab9: ('scan_dot_color', _decode_scan_dot_color),
    0x716e6398: ('morph_ball_power_bomb_digits_foreground_color', _decode_morph_ball_power_bomb_digits_foreground_color),
    0xdaca46d4: ('morph_ball_power_bomb_digits_outline_color', _decode_morph_ball_power_bomb_digits_outline_color),
    0x0f37e756: ('morph_ball_energy_word_color', _decode_morph_ball_energy_word_color),
    0xf7283644: ('morph_ball_bomb_counter_filled_color', _decode_morph_ball_bomb_counter_filled_color),
    0x37564b7d: ('morph_ball_bomb_counter_empty_color', _decode_morph_ball_bomb_counter_empty_color),
    0x66b7eda3: ('morph_ball_power_bomb_icon_color', _decode_morph_ball_power_bomb_icon_color),
    0xf895098f: ('morph_ball_bomb_word_color', _decode_morph_ball_bomb_word_color),
    0x9b27be10: ('morph_ball_energy_deco_color', _decode_morph_ball_energy_deco_color),
    0x6c8550c9: ('morph_ball_bomb_deco_color', _decode_morph_ball_bomb_deco_color),
    0x5368a35f: ('morph_ball_empty_power_bomb_digits_foreground_colorr', _decode_morph_ball_empty_power_bomb_digits_foreground_colorr),
    0x5a807b81: ('morph_ball_empty_power_bomb_digits_outline_color', _decode_morph_ball_empty_power_bomb_digits_outline_color),
    0xeb63afed: ('morph_ball_empty_power_bomb_icon_color', _decode_morph_ball_empty_power_bomb_icon_color),
    0x92f59138: ('scan_panel_color', _decode_scan_panel_color),
    0x96f650c3: ('unknown_0x96f650c3', _decode_unknown_0x96f650c3),
    0xabdbfa5b: ('scan_images_color', _decode_scan_images_color),
    0xd3bafaf5: ('unknown_0xd3bafaf5', _decode_unknown_0xd3bafaf5),
    0xf8b971fa: ('threat_group_damage_color', _decode_threat_group_damage_color),
    0x4f1d443e: ('coundown_foreground_color', _decode_coundown_foreground_color),
    0x0f6451da: ('coundown_outline_color', _decode_coundown_outline_color),
    0xc1ec3637: ('critical_scan_object_indicator_in_range_color', _decode_critical_scan_object_indicator_in_range_color),
    0xb6a61e34: ('critical_scan_object_indicator_out_of_range_color', _decode_critical_scan_object_indicator_out_of_range_color),
    0xfdcd9589: ('noncritical_scan_object_indicator_in_range_color', _decode_noncritical_scan_object_indicator_in_range_color),
    0xb0253266: ('noncritical_scan_object_indicator_out_of_range_color', _decode_noncritical_scan_object_indicator_out_of_range_color),
    0x345e5b4e: ('scan_seeker_color', _decode_scan_seeker_color),
    0xe8401c5a: ('thermal_threat_digits_outline_color', _decode_thermal_threat_digits_outline_color),
    0x659147ae: ('thermal_missile_digits_outline_color', _decode_thermal_missile_digits_outline_color),
    0x43ed3310: ('combat_missile_digits_foreground_color', _decode_combat_missile_digits_foreground_color),
    0xa781ed1d: ('combat_missile_digits_outline_color', _decode_combat_missile_digits_outline_color),
    0x35402188: ('thermal_deco_color', _decode_thermal_deco_color),
    0x223058b5: ('thermal_deco_outline_color', _decode_thermal_deco_outline_color),
    0xe846d37f: ('thermal_trackers_color', _decode_thermal_trackers_color),
    0x8c9f2a1a: ('thermal_lock_color', _decode_thermal_lock_color),
    0x1b0f3a85: ('log_book_color', _decode_log_book_color),
    0x149369fd: ('inventory_equipped_color', _decode_inventory_equipped_color),
    0x02d5344f: ('dark_visor_deco_color', _decode_dark_visor_deco_color),
    0xf37f8deb: ('light_ammo_tank_full_selected_color', _decode_light_ammo_tank_full_selected_color),
    0x5a6587df: ('light_ammo_tank_full_unselected_color', _decode_light_ammo_tank_full_unselected_color),
    0xc18bdc67: ('light_ammo_tank_emptyl_selected_color', _decode_light_ammo_tank_emptyl_selected_color),
    0x4d916bb8: ('light_ammo_tank_empty_unselected_color', _decode_light_ammo_tank_empty_unselected_color),
    0x5ba76807: ('light_ammo_meter_selected_fill_color', _decode_light_ammo_meter_selected_fill_color),
    0xa42f6495: ('light_ammo_meter_selected_shadow_color', _decode_light_ammo_meter_selected_shadow_color),
    0x448156ae: ('light_ammo_meter_unselected_fill_color', _decode_light_ammo_meter_unselected_fill_color),
    0x1a8b61b8: ('light_ammo_meter_unselected_shadow_color', _decode_light_ammo_meter_unselected_shadow_color),
    0xf36adacb: ('light_ammo_icon_selected_color', _decode_light_ammo_icon_selected_color),
    0x3aee673f: ('light_ammo_icon_unselected_color', _decode_light_ammo_icon_unselected_color),
    0xf9c88b05: ('light_ammo_digits_outline_color', _decode_light_ammo_digits_outline_color),
    0x3bffe826: ('light_ammo_digits_selected_color', _decode_light_ammo_digits_selected_color),
    0x19e9738b: ('light_ammo_digits_unselected_color', _decode_light_ammo_digits_unselected_color),
    0x9329c6ff: ('light_ammo_change_flash', _decode_light_ammo_change_flash),
    0xf9e7e0df: ('light_ammo_tank_warning_color', _decode_light_ammo_tank_warning_color),
    0x04e77411: ('light_ammo_meter_warning_color', _decode_light_ammo_meter_warning_color),
    0x3c5d7111: ('light_ammo_digit_warning_color', _decode_light_ammo_digit_warning_color),
    0x42e2dfc1: ('light_ammo_depletion_color', _decode_light_ammo_depletion_color),
    0xc758541f: ('light_ammo_empty_tank_warning_color', _decode_light_ammo_empty_tank_warning_color),
    0xde649e48: ('dark_ammo_tank_full_selected_color', _decode_dark_ammo_tank_full_selected_color),
    0x5bf10430: ('dark_ammo_tank_full_unselected_color', _decode_dark_ammo_tank_full_unselected_color),
    0xc01f5f88: ('dark_ammo_tank_emptyl_selected_color', _decode_dark_ammo_tank_emptyl_selected_color),
    0x7d2500d2: ('dark_ammo_tank_empty_unselected_color', _decode_dark_ammo_tank_empty_unselected_color),
    0x14558146: ('dark_ammo_meter_selected_fill_color', _decode_dark_ammo_meter_selected_fill_color),
    0x949b0fff: ('dark_ammo_meter_selected_shadow_color', _decode_dark_ammo_meter_selected_shadow_color),
    0x74353dc4: ('dark_ammo_meter_unselected_fill_color', _decode_dark_ammo_meter_unselected_fill_color),
    0x5ff96af1: ('dark_ammo_meter_unselected_shadow_color', _decode_dark_ammo_meter_unselected_shadow_color),
    0x074bb42f: ('dark_ammo_icon_selected_color', _decode_dark_ammo_icon_selected_color),
    0xaaf6e9a9: ('dark_ammo_icon_unselected_color', _decode_dark_ammo_icon_unselected_color),
    0x5e5b8c0a: ('dark_ammo_digits_outline_color', _decode_dark_ammo_digits_outline_color),
    0xabe766b0: ('dark_ammo_digits_selected_color', _decode_dark_ammo_digits_selected_color),
    0x34f26028: ('dark_ammo_digits_unselected_color', _decode_dark_ammo_digits_unselected_color),
    0xa59b3320: ('dark_ammo_change_flash', _decode_dark_ammo_change_flash),
    0xbfffe95a: ('num_huds', structs.decode_BIG_l),
    0x0c3c55c9: ('dark_ammo_tank_warning_color', _decode_dark_ammo_tank_warning_color),
    0xf0c61af5: ('dark_ammo_meter_warning_color', _decode_dark_ammo_meter_warning_color),
    0xc87c1ff5: ('dark_ammo_digit_warning_color', _decode_dark_ammo_digit_warning_color),
    0x88936aa2: ('dark_ammo_depletion_color', _decode_dark_ammo_depletion_color),
    0xea4347bc: ('dark_ammo_empty_tank_warning_color', _decode_dark_ammo_empty_tank_warning_color),
}
