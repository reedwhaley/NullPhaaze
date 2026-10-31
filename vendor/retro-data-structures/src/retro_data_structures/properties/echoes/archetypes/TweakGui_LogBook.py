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
from retro_data_structures.properties.spline import Spline
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    class TweakGui_LogBookJson(typing_extensions.TypedDict):
        main_window_border_color: json_util.JsonValue
        main_window_text_color: json_util.JsonValue
        main_window_selected_text_color: json_util.JsonValue
        main_window_unviewed_color: json_util.JsonValue
        main_window_unviewed_selected_color: json_util.JsonValue
        legend_background_color: json_util.JsonValue
        node_color: json_util.JsonValue
        selected_node_color: json_util.JsonValue
        parent_node_color: json_util.JsonValue
        unknown: json_util.JsonValue
        selected_text_cursor_color: json_util.JsonValue
        branch_length: float
        text_scale: float
        selected_text_scale: float
        transition_time: float
        node_collapse_motion: json_util.JsonObject
        selected_node_collapse_motion: json_util.JsonObject
        node_expand_motion: json_util.JsonObject
        rotation_speed: float
        node_scale: float
        selected_node_scale: float
        selected_text_cursor_scale: float
        scan_model_scale: float
        scan_object_fade_in_spline: json_util.JsonObject
        scan_object_fade_in_flash_color: json_util.JsonValue
        scan_object_fade_in_time: float
        fog_near: float
        fog_far: float
        fog_color: json_util.JsonValue
        tree_camera_distance: float
        tree_vertical_translation: float
        tree_horizontal_translation: float
        scan_object_vertical_translation: float
        scan_object_horizontal_translation: float
        background_sweep_color: json_util.JsonValue
        background_sweep_radius: float
        background_sweep_time: float
        scan_text_window_background_color: json_util.JsonValue
        scan_text_window_border_color: json_util.JsonValue
        scan_text_window_font_color: json_util.JsonValue
        legend_window_background_color: json_util.JsonValue
        legend_window_border_color: json_util.JsonValue
        legend_window_font_color: json_util.JsonValue
        legend_hide_time: float
        history_unselected_title: json_util.JsonValue
        history_unselected_frame: json_util.JsonValue
        history_selected_title: json_util.JsonValue
        history_selected_frame: json_util.JsonValue
        history_cursor_color: json_util.JsonValue
        history_percent_bar_unselected: json_util.JsonValue
        history_percent_bar_selected: json_util.JsonValue
        history_percent_bar_background_selected: json_util.JsonValue
        history_percent_bar_background_unselected: json_util.JsonValue
        frame_color: json_util.JsonValue
        scanline_color: json_util.JsonValue
        slider_background_color: json_util.JsonValue
        slider_selection_color: json_util.JsonValue
        slider_scale: float
        slider_speed: float
        slider_to_text_height_ratio: float
        slider_to_text_width_ratio: float
        menu_option_color: json_util.JsonValue
        menu_option_enabled_arrow_color: json_util.JsonValue
        menu_option_disabled_arrow_color: json_util.JsonValue
        menu_option_scale: float
        menu_option_arrow_scale: float
        model_rotation_speed: float
        model_rotation_clamp_lower_limit: float
        model_rotation_clamp_upper_limit: float
        model_light1_position: json_util.JsonValue
        model_light1_color: json_util.JsonValue
        model_light2_position: json_util.JsonValue
        model_light2_color: json_util.JsonValue
        model_ambient_light_color: json_util.JsonValue
    

@dataclasses.dataclass()
class TweakGui_LogBook(BaseProperty):
    main_window_border_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xba5a65c8, original_name='MainWindowBorderColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    main_window_text_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xbff0e37b, original_name='MainWindowTextColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    main_window_selected_text_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x28b49a88, original_name='MainWindowSelectedTextColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    main_window_unviewed_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xfe98f30e, original_name='MainWindowUnviewedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    main_window_unviewed_selected_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x39e57ac0, original_name='MainWindowUnviewedSelectedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    legend_background_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.4000000059604645, b=0.699999988079071, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xa6b633fa, original_name='LegendBackgroundColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    node_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.800000011920929, g=0.800000011920929, b=0.800000011920929, a=0.800000011920929), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xac80013b, original_name='NodeColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    selected_node_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x5946b439, original_name='SelectedNodeColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    parent_node_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xc5aa728c, original_name='ParentNodeColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    unknown: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x56843943, original_name='Unknown', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    selected_text_cursor_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.699999988079071, g=0.30000001192092896, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x6bd4783a, original_name='SelectedTextCursorColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    branch_length: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x905ce2c0, original_name='BranchLength'
        ),
    })
    text_scale: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5fa64c77, original_name='TextScale'
        ),
    })
    selected_text_scale: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xaa60f975, original_name='SelectedTextScale'
        ),
    })
    transition_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1832935e, original_name='TransitionTime'
        ),
    })
    node_collapse_motion: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x165943f6, original_name='NodeCollapseMotion', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    selected_node_collapse_motion: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x9ad04dd7, original_name='SelectedNodeCollapseMotion', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    node_expand_motion: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x08719a9c, original_name='NodeExpandMotion', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    rotation_speed: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x11cd076f, original_name='RotationSpeed'
        ),
    })
    node_scale: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb71677d0, original_name='NodeScale'
        ),
    })
    selected_node_scale: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x42d0c2d2, original_name='SelectedNodeScale'
        ),
    })
    selected_text_cursor_scale: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x70420ed1, original_name='SelectedTextCursorScale'
        ),
    })
    scan_model_scale: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc0cb3936, original_name='ScanModelScale'
        ),
    })
    scan_object_fade_in_spline: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x925b9d4a, original_name='ScanObjectFadeInSpline', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    scan_object_fade_in_flash_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.75, g=0.75, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x075a0734, original_name='ScanObjectFadeInFlashColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_object_fade_in_time: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8ef43309, original_name='ScanObjectFadeInTime'
        ),
    })
    fog_near: float = dataclasses.field(default=11.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4194622e, original_name='FogNear'
        ),
    })
    fog_far: float = dataclasses.field(default=18.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3935a756, original_name='FogFar'
        ),
    })
    fog_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xe578c0dd, original_name='FogColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    tree_camera_distance: float = dataclasses.field(default=12.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xeef15783, original_name='TreeCameraDistance'
        ),
    })
    tree_vertical_translation: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x78055ab2, original_name='TreeVerticalTranslation'
        ),
    })
    tree_horizontal_translation: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x09e3197f, original_name='TreeHorizontalTranslation'
        ),
    })
    scan_object_vertical_translation: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfaffce1f, original_name='ScanObjectVerticalTranslation'
        ),
    })
    scan_object_horizontal_translation: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe5280e7c, original_name='ScanObjectHorizontalTranslation'
        ),
    })
    background_sweep_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.05000000074505806, g=0.20000000298023224, b=0.20000000298023224, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x647d9f91, original_name='BackgroundSweepColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    background_sweep_radius: float = dataclasses.field(default=0.6000000238418579, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7120f18f, original_name='BackgroundSweepRadius'
        ),
    })
    background_sweep_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4def660d, original_name='BackgroundSweepTime'
        ),
    })
    scan_text_window_background_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.30000001192092896, g=0.30000001192092896, b=0.30000001192092896, a=0.30000001192092896), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xc7c1967b, original_name='ScanTextWindowBackgroundColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_text_window_border_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.30000001192092896, g=0.30000001192092896, b=0.30000001192092896, a=0.30000001192092896), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf74bbad2, original_name='ScanTextWindowBorderColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scan_text_window_font_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.30000001192092896, g=0.30000001192092896, b=0.30000001192092896, a=0.30000001192092896), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xe31421e2, original_name='ScanTextWindowFontColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    legend_window_background_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.30000001192092896, g=0.30000001192092896, b=0.30000001192092896, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x0b8f0ddb, original_name='LegendWindowBackgroundColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    legend_window_border_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.30000001192092896, g=0.30000001192092896, b=0.30000001192092896, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x0a7a4155, original_name='LegendWindowBorderColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    legend_window_font_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.30000001192092896, g=0.30000001192092896, b=0.30000001192092896, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x527a0b10, original_name='LegendWindowFontColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    legend_hide_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7927ca67, original_name='LegendHideTime'
        ),
    })
    history_unselected_title: Color = dataclasses.field(default_factory=lambda: Color(r=0.25, g=0.36000001430511475, b=0.36000001430511475, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x7f35c573, original_name='HistoryUnselectedTitle', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    history_unselected_frame: Color = dataclasses.field(default_factory=lambda: Color(r=0.25, g=0.36000001430511475, b=0.36000001430511475, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xe0d77cf1, original_name='HistoryUnselectedFrame', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    history_selected_title: Color = dataclasses.field(default_factory=lambda: Color(r=0.699999988079071, g=0.699999988079071, b=0.699999988079071, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x903d9b7e, original_name='HistorySelectedTitle', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    history_selected_frame: Color = dataclasses.field(default_factory=lambda: Color(r=0.699999988079071, g=0.30000001192092896, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x0fdf22fc, original_name='HistorySelectedFrame', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    history_cursor_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.30000001192092896, g=0.30000001192092896, b=0.30000001192092896, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xbeaf9d6b, original_name='HistoryCursorColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    history_percent_bar_unselected: Color = dataclasses.field(default_factory=lambda: Color(r=0.30000001192092896, g=0.30000001192092896, b=0.30000001192092896, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x7e8247d6, original_name='HistoryPercentBarUnselected', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    history_percent_bar_selected: Color = dataclasses.field(default_factory=lambda: Color(r=0.30000001192092896, g=0.30000001192092896, b=0.30000001192092896, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x8b3f7902, original_name='HistoryPercentBarSelected', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    history_percent_bar_background_selected: Color = dataclasses.field(default_factory=lambda: Color(r=0.30000001192092896, g=0.30000001192092896, b=0.30000001192092896, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xdc1abb82, original_name='HistoryPercentBarBackgroundSelected', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    history_percent_bar_background_unselected: Color = dataclasses.field(default_factory=lambda: Color(r=0.30000001192092896, g=0.30000001192092896, b=0.30000001192092896, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x306b2b24, original_name='HistoryPercentBarBackgroundUnselected', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    frame_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.30000001192092896, b=0.30000001192092896, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xa485372c, original_name='FrameColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scanline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.30000001192092896, b=0.30000001192092896, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x1a4b8068, original_name='ScanlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    slider_background_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xcc2f25f1, original_name='SliderBackgroundColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    slider_selection_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xcb8d5caf, original_name='SliderSelectionColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    slider_scale: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3f44254f, original_name='SliderScale'
        ),
    })
    slider_speed: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7087c377, original_name='SliderSpeed'
        ),
    })
    slider_to_text_height_ratio: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0x58795865, original_name='SliderToTextHeightRatio'
        ),
    })
    slider_to_text_width_ratio: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0x35e0bd31, original_name='SliderToTextWidthRatio'
        ),
    })
    menu_option_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xe7c283be, original_name='MenuOptionColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    menu_option_enabled_arrow_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xdabcb730, original_name='MenuOptionEnabledArrowColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    menu_option_disabled_arrow_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.5, g=0.5, b=0.5, a=0.5), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x9c2195d7, original_name='MenuOptionDisabledArrowColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    menu_option_scale: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfc54f555, original_name='MenuOptionScale'
        ),
    })
    menu_option_arrow_scale: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0xef549530, original_name='MenuOptionArrowScale'
        ),
    })
    model_rotation_speed: float = dataclasses.field(default=120.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfa7a92b8, original_name='ModelRotationSpeed'
        ),
    })
    model_rotation_clamp_lower_limit: float = dataclasses.field(default=-80.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x60914b79, original_name='ModelRotationClampLowerLimit'
        ),
    })
    model_rotation_clamp_upper_limit: float = dataclasses.field(default=80.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1fd44d9b, original_name='ModelRotationClampUpperLimit'
        ),
    })
    model_light1_position: Vector = dataclasses.field(default_factory=lambda: Vector(x=10.0, y=0.0, z=10.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x06c93afa, original_name='ModelLight1Position', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    model_light1_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.5, g=0.5, b=0.5, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x33924afb, original_name='ModelLight1Color', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    model_light2_position: Vector = dataclasses.field(default_factory=lambda: Vector(x=10.0, y=0.0, z=10.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x17b45083, original_name='ModelLight2Position', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    model_light2_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.25, g=0.25, b=0.25, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xaa702cfa, original_name='ModelLight2Color', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    model_ambient_light_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.25, g=0.25, b=0.25, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x62ff6d72, original_name='ModelAmbientLightColor', from_json=Color.from_json, to_json=Color.to_json
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
        if property_count != 74:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xba5a65c8
        main_window_border_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbff0e37b
        main_window_text_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x28b49a88
        main_window_selected_text_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfe98f30e
        main_window_unviewed_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x39e57ac0
        main_window_unviewed_selected_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa6b633fa
        legend_background_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xac80013b
        node_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5946b439
        selected_node_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc5aa728c
        parent_node_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x56843943
        unknown = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6bd4783a
        selected_text_cursor_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x905ce2c0
        branch_length = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5fa64c77
        text_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaa60f975
        selected_text_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1832935e
        transition_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x165943f6
        node_collapse_motion = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9ad04dd7
        selected_node_collapse_motion = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08719a9c
        node_expand_motion = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x11cd076f
        rotation_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb71677d0
        node_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42d0c2d2
        selected_node_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x70420ed1
        selected_text_cursor_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc0cb3936
        scan_model_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x925b9d4a
        scan_object_fade_in_spline = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x075a0734
        scan_object_fade_in_flash_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8ef43309
        scan_object_fade_in_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4194622e
        fog_near = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3935a756
        fog_far = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe578c0dd
        fog_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xeef15783
        tree_camera_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78055ab2
        tree_vertical_translation = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x09e3197f
        tree_horizontal_translation = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfaffce1f
        scan_object_vertical_translation = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe5280e7c
        scan_object_horizontal_translation = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x647d9f91
        background_sweep_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7120f18f
        background_sweep_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4def660d
        background_sweep_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc7c1967b
        scan_text_window_background_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf74bbad2
        scan_text_window_border_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe31421e2
        scan_text_window_font_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0b8f0ddb
        legend_window_background_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0a7a4155
        legend_window_border_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x527a0b10
        legend_window_font_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7927ca67
        legend_hide_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7f35c573
        history_unselected_title = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe0d77cf1
        history_unselected_frame = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x903d9b7e
        history_selected_title = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0fdf22fc
        history_selected_frame = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbeaf9d6b
        history_cursor_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e8247d6
        history_percent_bar_unselected = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8b3f7902
        history_percent_bar_selected = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdc1abb82
        history_percent_bar_background_selected = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x306b2b24
        history_percent_bar_background_unselected = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa485372c
        frame_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1a4b8068
        scanline_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcc2f25f1
        slider_background_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcb8d5caf
        slider_selection_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3f44254f
        slider_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7087c377
        slider_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58795865
        slider_to_text_height_ratio = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x35e0bd31
        slider_to_text_width_ratio = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe7c283be
        menu_option_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdabcb730
        menu_option_enabled_arrow_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9c2195d7
        menu_option_disabled_arrow_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfc54f555
        menu_option_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xef549530
        menu_option_arrow_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfa7a92b8
        model_rotation_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x60914b79
        model_rotation_clamp_lower_limit = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1fd44d9b
        model_rotation_clamp_upper_limit = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x06c93afa
        model_light1_position = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33924afb
        model_light1_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x17b45083
        model_light2_position = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaa702cfa
        model_light2_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x62ff6d72
        model_ambient_light_color = Color.from_stream(data, game, property_size)
    
        return cls(main_window_border_color, main_window_text_color, main_window_selected_text_color, main_window_unviewed_color, main_window_unviewed_selected_color, legend_background_color, node_color, selected_node_color, parent_node_color, unknown, selected_text_cursor_color, branch_length, text_scale, selected_text_scale, transition_time, node_collapse_motion, selected_node_collapse_motion, node_expand_motion, rotation_speed, node_scale, selected_node_scale, selected_text_cursor_scale, scan_model_scale, scan_object_fade_in_spline, scan_object_fade_in_flash_color, scan_object_fade_in_time, fog_near, fog_far, fog_color, tree_camera_distance, tree_vertical_translation, tree_horizontal_translation, scan_object_vertical_translation, scan_object_horizontal_translation, background_sweep_color, background_sweep_radius, background_sweep_time, scan_text_window_background_color, scan_text_window_border_color, scan_text_window_font_color, legend_window_background_color, legend_window_border_color, legend_window_font_color, legend_hide_time, history_unselected_title, history_unselected_frame, history_selected_title, history_selected_frame, history_cursor_color, history_percent_bar_unselected, history_percent_bar_selected, history_percent_bar_background_selected, history_percent_bar_background_unselected, frame_color, scanline_color, slider_background_color, slider_selection_color, slider_scale, slider_speed, slider_to_text_height_ratio, slider_to_text_width_ratio, menu_option_color, menu_option_enabled_arrow_color, menu_option_disabled_arrow_color, menu_option_scale, menu_option_arrow_scale, model_rotation_speed, model_rotation_clamp_lower_limit, model_rotation_clamp_upper_limit, model_light1_position, model_light1_color, model_light2_position, model_light2_color, model_ambient_light_color)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00J')  # 74 properties

        data.write(b'\xbaZe\xc8')  # 0xba5a65c8
        data.write(b'\x00\x10')  # size
        self.main_window_border_color.to_stream(data, game)

        data.write(b'\xbf\xf0\xe3{')  # 0xbff0e37b
        data.write(b'\x00\x10')  # size
        self.main_window_text_color.to_stream(data, game)

        data.write(b'(\xb4\x9a\x88')  # 0x28b49a88
        data.write(b'\x00\x10')  # size
        self.main_window_selected_text_color.to_stream(data, game)

        data.write(b'\xfe\x98\xf3\x0e')  # 0xfe98f30e
        data.write(b'\x00\x10')  # size
        self.main_window_unviewed_color.to_stream(data, game)

        data.write(b'9\xe5z\xc0')  # 0x39e57ac0
        data.write(b'\x00\x10')  # size
        self.main_window_unviewed_selected_color.to_stream(data, game)

        data.write(b'\xa6\xb63\xfa')  # 0xa6b633fa
        data.write(b'\x00\x10')  # size
        self.legend_background_color.to_stream(data, game)

        data.write(b'\xac\x80\x01;')  # 0xac80013b
        data.write(b'\x00\x10')  # size
        self.node_color.to_stream(data, game)

        data.write(b'YF\xb49')  # 0x5946b439
        data.write(b'\x00\x10')  # size
        self.selected_node_color.to_stream(data, game)

        data.write(b'\xc5\xaar\x8c')  # 0xc5aa728c
        data.write(b'\x00\x10')  # size
        self.parent_node_color.to_stream(data, game)

        data.write(b'V\x849C')  # 0x56843943
        data.write(b'\x00\x10')  # size
        self.unknown.to_stream(data, game)

        data.write(b'k\xd4x:')  # 0x6bd4783a
        data.write(b'\x00\x10')  # size
        self.selected_text_cursor_color.to_stream(data, game)

        data.write(b'\x90\\\xe2\xc0')  # 0x905ce2c0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.branch_length))

        data.write(b'_\xa6Lw')  # 0x5fa64c77
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.text_scale))

        data.write(b'\xaa`\xf9u')  # 0xaa60f975
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.selected_text_scale))

        data.write(b'\x182\x93^')  # 0x1832935e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.transition_time))

        data.write(b'\x16YC\xf6')  # 0x165943f6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.node_collapse_motion.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9a\xd0M\xd7')  # 0x9ad04dd7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.selected_node_collapse_motion.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x08q\x9a\x9c')  # 0x8719a9c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.node_expand_motion.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x11\xcd\x07o')  # 0x11cd076f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotation_speed))

        data.write(b'\xb7\x16w\xd0')  # 0xb71677d0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.node_scale))

        data.write(b'B\xd0\xc2\xd2')  # 0x42d0c2d2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.selected_node_scale))

        data.write(b'pB\x0e\xd1')  # 0x70420ed1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.selected_text_cursor_scale))

        data.write(b'\xc0\xcb96')  # 0xc0cb3936
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_model_scale))

        data.write(b'\x92[\x9dJ')  # 0x925b9d4a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.scan_object_fade_in_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x07Z\x074')  # 0x75a0734
        data.write(b'\x00\x10')  # size
        self.scan_object_fade_in_flash_color.to_stream(data, game)

        data.write(b'\x8e\xf43\t')  # 0x8ef43309
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_object_fade_in_time))

        data.write(b'A\x94b.')  # 0x4194622e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fog_near))

        data.write(b'95\xa7V')  # 0x3935a756
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fog_far))

        data.write(b'\xe5x\xc0\xdd')  # 0xe578c0dd
        data.write(b'\x00\x10')  # size
        self.fog_color.to_stream(data, game)

        data.write(b'\xee\xf1W\x83')  # 0xeef15783
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.tree_camera_distance))

        data.write(b'x\x05Z\xb2')  # 0x78055ab2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.tree_vertical_translation))

        data.write(b'\t\xe3\x19\x7f')  # 0x9e3197f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.tree_horizontal_translation))

        data.write(b'\xfa\xff\xce\x1f')  # 0xfaffce1f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_object_vertical_translation))

        data.write(b'\xe5(\x0e|')  # 0xe5280e7c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_object_horizontal_translation))

        data.write(b'd}\x9f\x91')  # 0x647d9f91
        data.write(b'\x00\x10')  # size
        self.background_sweep_color.to_stream(data, game)

        data.write(b'q \xf1\x8f')  # 0x7120f18f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.background_sweep_radius))

        data.write(b'M\xeff\r')  # 0x4def660d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.background_sweep_time))

        data.write(b'\xc7\xc1\x96{')  # 0xc7c1967b
        data.write(b'\x00\x10')  # size
        self.scan_text_window_background_color.to_stream(data, game)

        data.write(b'\xf7K\xba\xd2')  # 0xf74bbad2
        data.write(b'\x00\x10')  # size
        self.scan_text_window_border_color.to_stream(data, game)

        data.write(b'\xe3\x14!\xe2')  # 0xe31421e2
        data.write(b'\x00\x10')  # size
        self.scan_text_window_font_color.to_stream(data, game)

        data.write(b'\x0b\x8f\r\xdb')  # 0xb8f0ddb
        data.write(b'\x00\x10')  # size
        self.legend_window_background_color.to_stream(data, game)

        data.write(b'\nzAU')  # 0xa7a4155
        data.write(b'\x00\x10')  # size
        self.legend_window_border_color.to_stream(data, game)

        data.write(b'Rz\x0b\x10')  # 0x527a0b10
        data.write(b'\x00\x10')  # size
        self.legend_window_font_color.to_stream(data, game)

        data.write(b"y'\xcag")  # 0x7927ca67
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.legend_hide_time))

        data.write(b'\x7f5\xc5s')  # 0x7f35c573
        data.write(b'\x00\x10')  # size
        self.history_unselected_title.to_stream(data, game)

        data.write(b'\xe0\xd7|\xf1')  # 0xe0d77cf1
        data.write(b'\x00\x10')  # size
        self.history_unselected_frame.to_stream(data, game)

        data.write(b'\x90=\x9b~')  # 0x903d9b7e
        data.write(b'\x00\x10')  # size
        self.history_selected_title.to_stream(data, game)

        data.write(b'\x0f\xdf"\xfc')  # 0xfdf22fc
        data.write(b'\x00\x10')  # size
        self.history_selected_frame.to_stream(data, game)

        data.write(b'\xbe\xaf\x9dk')  # 0xbeaf9d6b
        data.write(b'\x00\x10')  # size
        self.history_cursor_color.to_stream(data, game)

        data.write(b'~\x82G\xd6')  # 0x7e8247d6
        data.write(b'\x00\x10')  # size
        self.history_percent_bar_unselected.to_stream(data, game)

        data.write(b'\x8b?y\x02')  # 0x8b3f7902
        data.write(b'\x00\x10')  # size
        self.history_percent_bar_selected.to_stream(data, game)

        data.write(b'\xdc\x1a\xbb\x82')  # 0xdc1abb82
        data.write(b'\x00\x10')  # size
        self.history_percent_bar_background_selected.to_stream(data, game)

        data.write(b'0k+$')  # 0x306b2b24
        data.write(b'\x00\x10')  # size
        self.history_percent_bar_background_unselected.to_stream(data, game)

        data.write(b'\xa4\x857,')  # 0xa485372c
        data.write(b'\x00\x10')  # size
        self.frame_color.to_stream(data, game)

        data.write(b'\x1aK\x80h')  # 0x1a4b8068
        data.write(b'\x00\x10')  # size
        self.scanline_color.to_stream(data, game)

        data.write(b'\xcc/%\xf1')  # 0xcc2f25f1
        data.write(b'\x00\x10')  # size
        self.slider_background_color.to_stream(data, game)

        data.write(b'\xcb\x8d\\\xaf')  # 0xcb8d5caf
        data.write(b'\x00\x10')  # size
        self.slider_selection_color.to_stream(data, game)

        data.write(b'?D%O')  # 0x3f44254f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.slider_scale))

        data.write(b'p\x87\xc3w')  # 0x7087c377
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.slider_speed))

        data.write(b'XyXe')  # 0x58795865
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.slider_to_text_height_ratio))

        data.write(b'5\xe0\xbd1')  # 0x35e0bd31
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.slider_to_text_width_ratio))

        data.write(b'\xe7\xc2\x83\xbe')  # 0xe7c283be
        data.write(b'\x00\x10')  # size
        self.menu_option_color.to_stream(data, game)

        data.write(b'\xda\xbc\xb70')  # 0xdabcb730
        data.write(b'\x00\x10')  # size
        self.menu_option_enabled_arrow_color.to_stream(data, game)

        data.write(b'\x9c!\x95\xd7')  # 0x9c2195d7
        data.write(b'\x00\x10')  # size
        self.menu_option_disabled_arrow_color.to_stream(data, game)

        data.write(b'\xfcT\xf5U')  # 0xfc54f555
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.menu_option_scale))

        data.write(b'\xefT\x950')  # 0xef549530
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.menu_option_arrow_scale))

        data.write(b'\xfaz\x92\xb8')  # 0xfa7a92b8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.model_rotation_speed))

        data.write(b'`\x91Ky')  # 0x60914b79
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.model_rotation_clamp_lower_limit))

        data.write(b'\x1f\xd4M\x9b')  # 0x1fd44d9b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.model_rotation_clamp_upper_limit))

        data.write(b'\x06\xc9:\xfa')  # 0x6c93afa
        data.write(b'\x00\x0c')  # size
        self.model_light1_position.to_stream(data, game)

        data.write(b'3\x92J\xfb')  # 0x33924afb
        data.write(b'\x00\x10')  # size
        self.model_light1_color.to_stream(data, game)

        data.write(b'\x17\xb4P\x83')  # 0x17b45083
        data.write(b'\x00\x0c')  # size
        self.model_light2_position.to_stream(data, game)

        data.write(b'\xaap,\xfa')  # 0xaa702cfa
        data.write(b'\x00\x10')  # size
        self.model_light2_color.to_stream(data, game)

        data.write(b'b\xffmr')  # 0x62ff6d72
        data.write(b'\x00\x10')  # size
        self.model_ambient_light_color.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakGui_LogBookJson", data)
        return cls(
            main_window_border_color=Color.from_json(json_data['main_window_border_color']),
            main_window_text_color=Color.from_json(json_data['main_window_text_color']),
            main_window_selected_text_color=Color.from_json(json_data['main_window_selected_text_color']),
            main_window_unviewed_color=Color.from_json(json_data['main_window_unviewed_color']),
            main_window_unviewed_selected_color=Color.from_json(json_data['main_window_unviewed_selected_color']),
            legend_background_color=Color.from_json(json_data['legend_background_color']),
            node_color=Color.from_json(json_data['node_color']),
            selected_node_color=Color.from_json(json_data['selected_node_color']),
            parent_node_color=Color.from_json(json_data['parent_node_color']),
            unknown=Color.from_json(json_data['unknown']),
            selected_text_cursor_color=Color.from_json(json_data['selected_text_cursor_color']),
            branch_length=json_data['branch_length'],
            text_scale=json_data['text_scale'],
            selected_text_scale=json_data['selected_text_scale'],
            transition_time=json_data['transition_time'],
            node_collapse_motion=Spline.from_json(json_data['node_collapse_motion']),
            selected_node_collapse_motion=Spline.from_json(json_data['selected_node_collapse_motion']),
            node_expand_motion=Spline.from_json(json_data['node_expand_motion']),
            rotation_speed=json_data['rotation_speed'],
            node_scale=json_data['node_scale'],
            selected_node_scale=json_data['selected_node_scale'],
            selected_text_cursor_scale=json_data['selected_text_cursor_scale'],
            scan_model_scale=json_data['scan_model_scale'],
            scan_object_fade_in_spline=Spline.from_json(json_data['scan_object_fade_in_spline']),
            scan_object_fade_in_flash_color=Color.from_json(json_data['scan_object_fade_in_flash_color']),
            scan_object_fade_in_time=json_data['scan_object_fade_in_time'],
            fog_near=json_data['fog_near'],
            fog_far=json_data['fog_far'],
            fog_color=Color.from_json(json_data['fog_color']),
            tree_camera_distance=json_data['tree_camera_distance'],
            tree_vertical_translation=json_data['tree_vertical_translation'],
            tree_horizontal_translation=json_data['tree_horizontal_translation'],
            scan_object_vertical_translation=json_data['scan_object_vertical_translation'],
            scan_object_horizontal_translation=json_data['scan_object_horizontal_translation'],
            background_sweep_color=Color.from_json(json_data['background_sweep_color']),
            background_sweep_radius=json_data['background_sweep_radius'],
            background_sweep_time=json_data['background_sweep_time'],
            scan_text_window_background_color=Color.from_json(json_data['scan_text_window_background_color']),
            scan_text_window_border_color=Color.from_json(json_data['scan_text_window_border_color']),
            scan_text_window_font_color=Color.from_json(json_data['scan_text_window_font_color']),
            legend_window_background_color=Color.from_json(json_data['legend_window_background_color']),
            legend_window_border_color=Color.from_json(json_data['legend_window_border_color']),
            legend_window_font_color=Color.from_json(json_data['legend_window_font_color']),
            legend_hide_time=json_data['legend_hide_time'],
            history_unselected_title=Color.from_json(json_data['history_unselected_title']),
            history_unselected_frame=Color.from_json(json_data['history_unselected_frame']),
            history_selected_title=Color.from_json(json_data['history_selected_title']),
            history_selected_frame=Color.from_json(json_data['history_selected_frame']),
            history_cursor_color=Color.from_json(json_data['history_cursor_color']),
            history_percent_bar_unselected=Color.from_json(json_data['history_percent_bar_unselected']),
            history_percent_bar_selected=Color.from_json(json_data['history_percent_bar_selected']),
            history_percent_bar_background_selected=Color.from_json(json_data['history_percent_bar_background_selected']),
            history_percent_bar_background_unselected=Color.from_json(json_data['history_percent_bar_background_unselected']),
            frame_color=Color.from_json(json_data['frame_color']),
            scanline_color=Color.from_json(json_data['scanline_color']),
            slider_background_color=Color.from_json(json_data['slider_background_color']),
            slider_selection_color=Color.from_json(json_data['slider_selection_color']),
            slider_scale=json_data['slider_scale'],
            slider_speed=json_data['slider_speed'],
            slider_to_text_height_ratio=json_data['slider_to_text_height_ratio'],
            slider_to_text_width_ratio=json_data['slider_to_text_width_ratio'],
            menu_option_color=Color.from_json(json_data['menu_option_color']),
            menu_option_enabled_arrow_color=Color.from_json(json_data['menu_option_enabled_arrow_color']),
            menu_option_disabled_arrow_color=Color.from_json(json_data['menu_option_disabled_arrow_color']),
            menu_option_scale=json_data['menu_option_scale'],
            menu_option_arrow_scale=json_data['menu_option_arrow_scale'],
            model_rotation_speed=json_data['model_rotation_speed'],
            model_rotation_clamp_lower_limit=json_data['model_rotation_clamp_lower_limit'],
            model_rotation_clamp_upper_limit=json_data['model_rotation_clamp_upper_limit'],
            model_light1_position=Vector.from_json(json_data['model_light1_position']),
            model_light1_color=Color.from_json(json_data['model_light1_color']),
            model_light2_position=Vector.from_json(json_data['model_light2_position']),
            model_light2_color=Color.from_json(json_data['model_light2_color']),
            model_ambient_light_color=Color.from_json(json_data['model_ambient_light_color']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'main_window_border_color': self.main_window_border_color.to_json(),
            'main_window_text_color': self.main_window_text_color.to_json(),
            'main_window_selected_text_color': self.main_window_selected_text_color.to_json(),
            'main_window_unviewed_color': self.main_window_unviewed_color.to_json(),
            'main_window_unviewed_selected_color': self.main_window_unviewed_selected_color.to_json(),
            'legend_background_color': self.legend_background_color.to_json(),
            'node_color': self.node_color.to_json(),
            'selected_node_color': self.selected_node_color.to_json(),
            'parent_node_color': self.parent_node_color.to_json(),
            'unknown': self.unknown.to_json(),
            'selected_text_cursor_color': self.selected_text_cursor_color.to_json(),
            'branch_length': self.branch_length,
            'text_scale': self.text_scale,
            'selected_text_scale': self.selected_text_scale,
            'transition_time': self.transition_time,
            'node_collapse_motion': self.node_collapse_motion.to_json(),
            'selected_node_collapse_motion': self.selected_node_collapse_motion.to_json(),
            'node_expand_motion': self.node_expand_motion.to_json(),
            'rotation_speed': self.rotation_speed,
            'node_scale': self.node_scale,
            'selected_node_scale': self.selected_node_scale,
            'selected_text_cursor_scale': self.selected_text_cursor_scale,
            'scan_model_scale': self.scan_model_scale,
            'scan_object_fade_in_spline': self.scan_object_fade_in_spline.to_json(),
            'scan_object_fade_in_flash_color': self.scan_object_fade_in_flash_color.to_json(),
            'scan_object_fade_in_time': self.scan_object_fade_in_time,
            'fog_near': self.fog_near,
            'fog_far': self.fog_far,
            'fog_color': self.fog_color.to_json(),
            'tree_camera_distance': self.tree_camera_distance,
            'tree_vertical_translation': self.tree_vertical_translation,
            'tree_horizontal_translation': self.tree_horizontal_translation,
            'scan_object_vertical_translation': self.scan_object_vertical_translation,
            'scan_object_horizontal_translation': self.scan_object_horizontal_translation,
            'background_sweep_color': self.background_sweep_color.to_json(),
            'background_sweep_radius': self.background_sweep_radius,
            'background_sweep_time': self.background_sweep_time,
            'scan_text_window_background_color': self.scan_text_window_background_color.to_json(),
            'scan_text_window_border_color': self.scan_text_window_border_color.to_json(),
            'scan_text_window_font_color': self.scan_text_window_font_color.to_json(),
            'legend_window_background_color': self.legend_window_background_color.to_json(),
            'legend_window_border_color': self.legend_window_border_color.to_json(),
            'legend_window_font_color': self.legend_window_font_color.to_json(),
            'legend_hide_time': self.legend_hide_time,
            'history_unselected_title': self.history_unselected_title.to_json(),
            'history_unselected_frame': self.history_unselected_frame.to_json(),
            'history_selected_title': self.history_selected_title.to_json(),
            'history_selected_frame': self.history_selected_frame.to_json(),
            'history_cursor_color': self.history_cursor_color.to_json(),
            'history_percent_bar_unselected': self.history_percent_bar_unselected.to_json(),
            'history_percent_bar_selected': self.history_percent_bar_selected.to_json(),
            'history_percent_bar_background_selected': self.history_percent_bar_background_selected.to_json(),
            'history_percent_bar_background_unselected': self.history_percent_bar_background_unselected.to_json(),
            'frame_color': self.frame_color.to_json(),
            'scanline_color': self.scanline_color.to_json(),
            'slider_background_color': self.slider_background_color.to_json(),
            'slider_selection_color': self.slider_selection_color.to_json(),
            'slider_scale': self.slider_scale,
            'slider_speed': self.slider_speed,
            'slider_to_text_height_ratio': self.slider_to_text_height_ratio,
            'slider_to_text_width_ratio': self.slider_to_text_width_ratio,
            'menu_option_color': self.menu_option_color.to_json(),
            'menu_option_enabled_arrow_color': self.menu_option_enabled_arrow_color.to_json(),
            'menu_option_disabled_arrow_color': self.menu_option_disabled_arrow_color.to_json(),
            'menu_option_scale': self.menu_option_scale,
            'menu_option_arrow_scale': self.menu_option_arrow_scale,
            'model_rotation_speed': self.model_rotation_speed,
            'model_rotation_clamp_lower_limit': self.model_rotation_clamp_lower_limit,
            'model_rotation_clamp_upper_limit': self.model_rotation_clamp_upper_limit,
            'model_light1_position': self.model_light1_position.to_json(),
            'model_light1_color': self.model_light1_color.to_json(),
            'model_light2_position': self.model_light2_position.to_json(),
            'model_light2_color': self.model_light2_color.to_json(),
            'model_ambient_light_color': self.model_ambient_light_color.to_json(),
        }


def _decode_main_window_border_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_main_window_text_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_main_window_selected_text_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_main_window_unviewed_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_main_window_unviewed_selected_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_legend_background_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_node_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_selected_node_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_parent_node_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_unknown(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_selected_text_cursor_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_node_collapse_motion(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_selected_node_collapse_motion(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_node_expand_motion(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_scan_object_fade_in_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_scan_object_fade_in_flash_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_fog_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_background_sweep_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_text_window_background_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_text_window_border_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scan_text_window_font_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_legend_window_background_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_legend_window_border_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_legend_window_font_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_history_unselected_title(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_history_unselected_frame(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_history_selected_title(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_history_selected_frame(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_history_cursor_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_history_percent_bar_unselected(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_history_percent_bar_selected(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_history_percent_bar_background_selected(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_history_percent_bar_background_unselected(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_frame_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scanline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_slider_background_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_slider_selection_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_menu_option_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_menu_option_enabled_arrow_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_menu_option_disabled_arrow_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_model_light1_position(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_model_light1_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_model_light2_position(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_model_light2_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_model_ambient_light_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xba5a65c8: ('main_window_border_color', _decode_main_window_border_color),
    0xbff0e37b: ('main_window_text_color', _decode_main_window_text_color),
    0x28b49a88: ('main_window_selected_text_color', _decode_main_window_selected_text_color),
    0xfe98f30e: ('main_window_unviewed_color', _decode_main_window_unviewed_color),
    0x39e57ac0: ('main_window_unviewed_selected_color', _decode_main_window_unviewed_selected_color),
    0xa6b633fa: ('legend_background_color', _decode_legend_background_color),
    0xac80013b: ('node_color', _decode_node_color),
    0x5946b439: ('selected_node_color', _decode_selected_node_color),
    0xc5aa728c: ('parent_node_color', _decode_parent_node_color),
    0x56843943: ('unknown', _decode_unknown),
    0x6bd4783a: ('selected_text_cursor_color', _decode_selected_text_cursor_color),
    0x905ce2c0: ('branch_length', structs.decode_BIG_f),
    0x5fa64c77: ('text_scale', structs.decode_BIG_f),
    0xaa60f975: ('selected_text_scale', structs.decode_BIG_f),
    0x1832935e: ('transition_time', structs.decode_BIG_f),
    0x165943f6: ('node_collapse_motion', _decode_node_collapse_motion),
    0x9ad04dd7: ('selected_node_collapse_motion', _decode_selected_node_collapse_motion),
    0x08719a9c: ('node_expand_motion', _decode_node_expand_motion),
    0x11cd076f: ('rotation_speed', structs.decode_BIG_f),
    0xb71677d0: ('node_scale', structs.decode_BIG_f),
    0x42d0c2d2: ('selected_node_scale', structs.decode_BIG_f),
    0x70420ed1: ('selected_text_cursor_scale', structs.decode_BIG_f),
    0xc0cb3936: ('scan_model_scale', structs.decode_BIG_f),
    0x925b9d4a: ('scan_object_fade_in_spline', _decode_scan_object_fade_in_spline),
    0x075a0734: ('scan_object_fade_in_flash_color', _decode_scan_object_fade_in_flash_color),
    0x8ef43309: ('scan_object_fade_in_time', structs.decode_BIG_f),
    0x4194622e: ('fog_near', structs.decode_BIG_f),
    0x3935a756: ('fog_far', structs.decode_BIG_f),
    0xe578c0dd: ('fog_color', _decode_fog_color),
    0xeef15783: ('tree_camera_distance', structs.decode_BIG_f),
    0x78055ab2: ('tree_vertical_translation', structs.decode_BIG_f),
    0x09e3197f: ('tree_horizontal_translation', structs.decode_BIG_f),
    0xfaffce1f: ('scan_object_vertical_translation', structs.decode_BIG_f),
    0xe5280e7c: ('scan_object_horizontal_translation', structs.decode_BIG_f),
    0x647d9f91: ('background_sweep_color', _decode_background_sweep_color),
    0x7120f18f: ('background_sweep_radius', structs.decode_BIG_f),
    0x4def660d: ('background_sweep_time', structs.decode_BIG_f),
    0xc7c1967b: ('scan_text_window_background_color', _decode_scan_text_window_background_color),
    0xf74bbad2: ('scan_text_window_border_color', _decode_scan_text_window_border_color),
    0xe31421e2: ('scan_text_window_font_color', _decode_scan_text_window_font_color),
    0x0b8f0ddb: ('legend_window_background_color', _decode_legend_window_background_color),
    0x0a7a4155: ('legend_window_border_color', _decode_legend_window_border_color),
    0x527a0b10: ('legend_window_font_color', _decode_legend_window_font_color),
    0x7927ca67: ('legend_hide_time', structs.decode_BIG_f),
    0x7f35c573: ('history_unselected_title', _decode_history_unselected_title),
    0xe0d77cf1: ('history_unselected_frame', _decode_history_unselected_frame),
    0x903d9b7e: ('history_selected_title', _decode_history_selected_title),
    0x0fdf22fc: ('history_selected_frame', _decode_history_selected_frame),
    0xbeaf9d6b: ('history_cursor_color', _decode_history_cursor_color),
    0x7e8247d6: ('history_percent_bar_unselected', _decode_history_percent_bar_unselected),
    0x8b3f7902: ('history_percent_bar_selected', _decode_history_percent_bar_selected),
    0xdc1abb82: ('history_percent_bar_background_selected', _decode_history_percent_bar_background_selected),
    0x306b2b24: ('history_percent_bar_background_unselected', _decode_history_percent_bar_background_unselected),
    0xa485372c: ('frame_color', _decode_frame_color),
    0x1a4b8068: ('scanline_color', _decode_scanline_color),
    0xcc2f25f1: ('slider_background_color', _decode_slider_background_color),
    0xcb8d5caf: ('slider_selection_color', _decode_slider_selection_color),
    0x3f44254f: ('slider_scale', structs.decode_BIG_f),
    0x7087c377: ('slider_speed', structs.decode_BIG_f),
    0x58795865: ('slider_to_text_height_ratio', structs.decode_BIG_f),
    0x35e0bd31: ('slider_to_text_width_ratio', structs.decode_BIG_f),
    0xe7c283be: ('menu_option_color', _decode_menu_option_color),
    0xdabcb730: ('menu_option_enabled_arrow_color', _decode_menu_option_enabled_arrow_color),
    0x9c2195d7: ('menu_option_disabled_arrow_color', _decode_menu_option_disabled_arrow_color),
    0xfc54f555: ('menu_option_scale', structs.decode_BIG_f),
    0xef549530: ('menu_option_arrow_scale', structs.decode_BIG_f),
    0xfa7a92b8: ('model_rotation_speed', structs.decode_BIG_f),
    0x60914b79: ('model_rotation_clamp_lower_limit', structs.decode_BIG_f),
    0x1fd44d9b: ('model_rotation_clamp_upper_limit', structs.decode_BIG_f),
    0x06c93afa: ('model_light1_position', _decode_model_light1_position),
    0x33924afb: ('model_light1_color', _decode_model_light1_color),
    0x17b45083: ('model_light2_position', _decode_model_light2_position),
    0xaa702cfa: ('model_light2_color', _decode_model_light2_color),
    0x62ff6d72: ('model_ambient_light_color', _decode_model_ambient_light_color),
}
