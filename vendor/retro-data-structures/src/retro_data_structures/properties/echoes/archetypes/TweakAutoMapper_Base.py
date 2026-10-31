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
    class TweakAutoMapper_BaseJson(typing_extensions.TypedDict):
        unknown_0xcbe595d8: bool
        unknown_0x8ecb53a6: bool
        scale_move_speed_with_camera_distance: bool
        map_screen_camera_default_distance: float
        map_screen_camera_min_distance: float
        map_screen_camera_max_distance: float
        map_screen_camera_min_x_angle: float
        map_screen_camera_max_x_angle: float
        map_screen_camera_fov: float
        map_screen_area_opacity: float
        map_screen_bg_color: json_util.JsonValue
        mini_map_camera_distance: float
        mini_map_camera_angle: float
        mini_map_camera_fov: float
        mini_map_area_opacity: float
        mini_map_bg_color: json_util.JsonValue
        map_visited_surface_color: json_util.JsonValue
        map_visited_outline_color: json_util.JsonValue
        map_unvisited_surface_color: json_util.JsonValue
        map_unvisited_outline_color: json_util.JsonValue
        map_visited_focus_area_surface_color: json_util.JsonValue
        map_visited_focus_area_outline_color: json_util.JsonValue
        dark_map_visited_surface_color: json_util.JsonValue
        dark_map_visited_outline_color: json_util.JsonValue
        dark_map_unvisited_surface_color: json_util.JsonValue
        dark_map_unvisited_outline_color: json_util.JsonValue
        dark_map_visited_focus_area_surface_color: json_util.JsonValue
        dark_map_visited_focus_area_outline_color: json_util.JsonValue
        map_light_color_intensity: float
        map_ambient_color_intensity: float
        off_to_mini_map_time: float
        mini_map_to_map_screen_time: float
        map_screen_to_mini_map_time: float
        unknown_0x73de4110: float
        map_screen_zoom_speed: float
        map_screen_circle_speed: float
        map_screen_move_speed: float
        map_unvisited_focus_area_surface_color: json_util.JsonValue
        map_unvisited_focus_area_outline_color: json_util.JsonValue
        dark_map_unvisited_focus_area_surface_color: json_util.JsonValue
        dark_map_unvisited_focus_area_outline_color: json_util.JsonValue
        map_visited_surface_alpha_mini_map: float
        map_visited_surface_alpha_map_screen: float
        map_visited_outline_alpha_mini_map: float
        map_visited_outline_alpha_map_screen: float
        map_unvisited_surface_alpha_mini_map: float
        map_unvisited_surface_alpha_map_screen: float
        map_unvisited_outline_alpha_mini_map: float
        map_unvisited_outline_alpha_map_screen: float
        map_door_half_height: float
        map_door_half_width: float
        map_door_half_depth: float
        mini_map_viewport_position_x: float
        mini_map_viewport_position_y: float
        mini_map_viewport_width: float
        mini_map_viewport_height: float
        mini_map_dynamic_camera_distance_scalar: float
        mini_map_widget_half_width: float
        mini_map_widget_half_height: float
        unknown_0x2b97d64c: bool
        map_screen_map_universe_default_camera_distance: float
        map_screen_map_universe_min_camera_distance: float
        map_screen_map_universe_max_camera_distance: float
        map_screen_to_map_universe_time: float
        unknown_0x706f52fe: float
        map_screen_clip_window_scale_x: float
        map_screen_clip_window_scale_y: float
        map_screen_move2_d_hover_depth: float
        player_model_color: json_util.JsonValue
        player_flashed_color: json_util.JsonValue
        player_surface_color: json_util.JsonValue
        player_outline_color: json_util.JsonValue
        text_color: json_util.JsonValue
        text_outline_color: json_util.JsonValue
        scanline_color: json_util.JsonValue
        frame_color: json_util.JsonValue
        title_color: json_util.JsonValue
        legend_background_color: json_util.JsonValue
        legend_gradient_color: json_util.JsonValue
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xcbe595d8, 0x8ecb53a6, 0x30b13740, 0x6bea9324, 0x65dd754, 0x57a46c09, 0xb54255b5, 0xc64cec4, 0x335ebc7e, 0x45be3f6b, 0x533c5684, 0xeb383668, 0x27151ede, 0x434172c3, 0x68097036, 0x3adcf46, 0xd3fae283, 0x65d2cf45, 0xb5752c08, 0x35d01ce, 0x805d5fa3, 0x36757265, 0xe550fcbd, 0x5378d17b, 0xebf3cbc, 0xb897117a, 0x3e670f6a, 0x884f22ac, 0x7bdb0edf, 0x12221909, 0x38dbbc09, 0x30610062, 0xb6acea88, 0x73de4110, 0x19069725, 0x5ba0de1e, 0x310b37a1, 0xab82e268, 0x1daacfae, 0xdad161a1, 0x6cf94c67, 0x47967404, 0xece1950, 0x9ac1bdde, 0x97a19386, 0xcb9e3a54, 0x2511a49b, 0x16c9f38e, 0xbc7e2e4d, 0x15564d32, 0xf5479260, 0x271b644e, 0x52dc08c1, 0x9980db64, 0x23f59057, 0xad3d5a3f, 0x3315d22b, 0x9e4007b6, 0x7a8d3d46, 0x2b97d64c, 0xbdc57ce0, 0x7d59c854, 0x3c4ef7d2, 0x2b483e9f, 0x706f52fe, 0x62f9ebf6, 0xa9a53853, 0x722b1bc0, 0x4c3fc933, 0x5a87c156, 0x9c0c5318, 0x2a247ede, 0x44303a9c, 0xf2e13506, 0x1a4b8068, 0xa485372c, 0x536647d5, 0xa6b633fa, 0x1cea7f9)


@dataclasses.dataclass()
class TweakAutoMapper_Base(BaseProperty):
    unknown_0xcbe595d8: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xcbe595d8, original_name='Unknown'
        ),
    })
    unknown_0x8ecb53a6: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x8ecb53a6, original_name='Unknown'
        ),
    })
    scale_move_speed_with_camera_distance: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x30b13740, original_name='ScaleMoveSpeedWithCameraDistance'
        ),
    })
    map_screen_camera_default_distance: float = dataclasses.field(default=175.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6bea9324, original_name='MapScreenCameraDefaultDistance'
        ),
    })
    map_screen_camera_min_distance: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x065dd754, original_name='MapScreenCameraMinDistance'
        ),
    })
    map_screen_camera_max_distance: float = dataclasses.field(default=700.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x57a46c09, original_name='MapScreenCameraMaxDistance'
        ),
    })
    map_screen_camera_min_x_angle: float = dataclasses.field(default=-89.9000015258789, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb54255b5, original_name='MapScreenCameraMinXAngle'
        ),
    })
    map_screen_camera_max_x_angle: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0c64cec4, original_name='MapScreenCameraMaxXAngle'
        ),
    })
    map_screen_camera_fov: float = dataclasses.field(default=75.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x335ebc7e, original_name='MapScreenCameraFOV'
        ),
    })
    map_screen_area_opacity: float = dataclasses.field(default=0.699999988079071, metadata={
        'reflection': FieldReflection[float](
            float, id=0x45be3f6b, original_name='MapScreenAreaOpacity'
        ),
    })
    map_screen_bg_color: Color = dataclasses.field(default_factory=Color, metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x533c5684, original_name='MapScreenBGColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    mini_map_camera_distance: float = dataclasses.field(default=120.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xeb383668, original_name='MiniMapCameraDistance'
        ),
    })
    mini_map_camera_angle: float = dataclasses.field(default=-45.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x27151ede, original_name='MiniMapCameraAngle'
        ),
    })
    mini_map_camera_fov: float = dataclasses.field(default=45.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x434172c3, original_name='MiniMapCameraFOV'
        ),
    })
    mini_map_area_opacity: float = dataclasses.field(default=0.6000000238418579, metadata={
        'reflection': FieldReflection[float](
            float, id=0x68097036, original_name='MiniMapAreaOpacity'
        ),
    })
    mini_map_bg_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x03adcf46, original_name='MiniMapBGColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    map_visited_surface_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.9568629860877991, g=0.4078429937362671, b=0.01960800029337406, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xd3fae283, original_name='MapVisitedSurfaceColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    map_visited_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.5294119715690613, b=0.02352900058031082, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x65d2cf45, original_name='MapVisitedOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    map_unvisited_surface_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=0.09411799907684326), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xb5752c08, original_name='MapUnvisitedSurfaceColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    map_unvisited_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.38431400060653687, g=0.6470590233802795, b=0.8352940082550049, a=0.11372499912977219), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x035d01ce, original_name='MapUnvisitedOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    map_visited_focus_area_surface_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.9568629860877991, g=0.6745100021362305, b=0.01176500041037798, a=0.9019610285758972), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x805d5fa3, original_name='MapVisitedFocusAreaSurfaceColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    map_visited_focus_area_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.9800000190734863, g=0.8399999737739563, b=0.75, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x36757265, original_name='MapVisitedFocusAreaOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_map_visited_surface_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.9568629860877991, g=0.4078429937362671, b=0.01960800029337406, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xe550fcbd, original_name='DarkMapVisitedSurfaceColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_map_visited_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.5294119715690613, b=0.02352900058031082, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x5378d17b, original_name='DarkMapVisitedOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_map_unvisited_surface_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=0.09411799907684326), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x0ebf3cbc, original_name='DarkMapUnvisitedSurfaceColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_map_unvisited_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.38431400060653687, g=0.6470590233802795, b=0.8352940082550049, a=0.11372499912977219), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xb897117a, original_name='DarkMapUnvisitedOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_map_visited_focus_area_surface_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.9568629860877991, g=0.6745100021362305, b=0.01176500041037798, a=0.9019610285758972), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x3e670f6a, original_name='DarkMapVisitedFocusAreaSurfaceColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_map_visited_focus_area_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.9800000190734863, g=0.8399999737739563, b=0.75, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x884f22ac, original_name='DarkMapVisitedFocusAreaOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    map_light_color_intensity: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7bdb0edf, original_name='MapLightColorIntensity'
        ),
    })
    map_ambient_color_intensity: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0x12221909, original_name='MapAmbientColorIntensity'
        ),
    })
    off_to_mini_map_time: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x38dbbc09, original_name='OffToMiniMapTime'
        ),
    })
    mini_map_to_map_screen_time: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x30610062, original_name='MiniMapToMapScreenTime'
        ),
    })
    map_screen_to_mini_map_time: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb6acea88, original_name='MapScreenToMiniMapTime'
        ),
    })
    unknown_0x73de4110: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x73de4110, original_name='Unknown'
        ),
    })
    map_screen_zoom_speed: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x19069725, original_name='MapScreenZoomSpeed'
        ),
    })
    map_screen_circle_speed: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5ba0de1e, original_name='MapScreenCircleSpeed'
        ),
    })
    map_screen_move_speed: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x310b37a1, original_name='MapScreenMoveSpeed'
        ),
    })
    map_unvisited_focus_area_surface_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4000000059604645, g=0.6705880165100098, b=0.8627449870109558, a=0.9019610285758972), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xab82e268, original_name='MapUnvisitedFocusAreaSurfaceColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    map_unvisited_focus_area_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.5372549891471863, g=0.8392159938812256, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x1daacfae, original_name='MapUnvisitedFocusAreaOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_map_unvisited_focus_area_surface_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.4000000059604645, g=0.6705880165100098, b=0.8627449870109558, a=0.9019610285758972), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xdad161a1, original_name='DarkMapUnvisitedFocusAreaSurfaceColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    dark_map_unvisited_focus_area_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.5372549891471863, g=0.8392159938812256, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x6cf94c67, original_name='DarkMapUnvisitedFocusAreaOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    map_visited_surface_alpha_mini_map: float = dataclasses.field(default=0.6000000238418579, metadata={
        'reflection': FieldReflection[float](
            float, id=0x47967404, original_name='MapVisitedSurfaceAlphaMiniMap'
        ),
    })
    map_visited_surface_alpha_map_screen: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0ece1950, original_name='MapVisitedSurfaceAlphaMapScreen'
        ),
    })
    map_visited_outline_alpha_mini_map: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9ac1bdde, original_name='MapVisitedOutlineAlphaMiniMap'
        ),
    })
    map_visited_outline_alpha_map_screen: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x97a19386, original_name='MapVisitedOutlineAlphaMapScreen'
        ),
    })
    map_unvisited_surface_alpha_mini_map: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcb9e3a54, original_name='MapUnvisitedSurfaceAlphaMiniMap'
        ),
    })
    map_unvisited_surface_alpha_map_screen: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2511a49b, original_name='MapUnvisitedSurfaceAlphaMapScreen'
        ),
    })
    map_unvisited_outline_alpha_mini_map: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0x16c9f38e, original_name='MapUnvisitedOutlineAlphaMiniMap'
        ),
    })
    map_unvisited_outline_alpha_map_screen: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbc7e2e4d, original_name='MapUnvisitedOutlineAlphaMapScreen'
        ),
    })
    map_door_half_height: float = dataclasses.field(default=3.569999933242798, metadata={
        'reflection': FieldReflection[float](
            float, id=0x15564d32, original_name='MapDoorHalfHeight'
        ),
    })
    map_door_half_width: float = dataclasses.field(default=3.569999933242798, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf5479260, original_name='MapDoorHalfWidth'
        ),
    })
    map_door_half_depth: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x271b644e, original_name='MapDoorHalfDepth'
        ),
    })
    mini_map_viewport_position_x: float = dataclasses.field(default=24.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x52dc08c1, original_name='MiniMapViewportPositionX'
        ),
    })
    mini_map_viewport_position_y: float = dataclasses.field(default=348.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9980db64, original_name='MiniMapViewportPositionY'
        ),
    })
    mini_map_viewport_width: float = dataclasses.field(default=152.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x23f59057, original_name='MiniMapViewportWidth'
        ),
    })
    mini_map_viewport_height: float = dataclasses.field(default=114.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xad3d5a3f, original_name='MiniMapViewportHeight'
        ),
    })
    mini_map_dynamic_camera_distance_scalar: float = dataclasses.field(default=0.8500000238418579, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3315d22b, original_name='MiniMapDynamicCameraDistanceScalar'
        ),
    })
    mini_map_widget_half_width: float = dataclasses.field(default=1.850000023841858, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9e4007b6, original_name='MiniMapWidgetHalfWidth'
        ),
    })
    mini_map_widget_half_height: float = dataclasses.field(default=1.3600000143051147, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7a8d3d46, original_name='MiniMapWidgetHalfHeight'
        ),
    })
    unknown_0x2b97d64c: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x2b97d64c, original_name='Unknown'
        ),
    })
    map_screen_map_universe_default_camera_distance: float = dataclasses.field(default=800.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbdc57ce0, original_name='MapScreenMapUniverseDefaultCameraDistance'
        ),
    })
    map_screen_map_universe_min_camera_distance: float = dataclasses.field(default=400.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7d59c854, original_name='MapScreenMapUniverseMinCameraDistance'
        ),
    })
    map_screen_map_universe_max_camera_distance: float = dataclasses.field(default=2000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3c4ef7d2, original_name='MapScreenMapUniverseMaxCameraDistance'
        ),
    })
    map_screen_to_map_universe_time: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2b483e9f, original_name='MapScreenToMapUniverseTime'
        ),
    })
    unknown_0x706f52fe: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x706f52fe, original_name='Unknown'
        ),
    })
    map_screen_clip_window_scale_x: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x62f9ebf6, original_name='MapScreenClipWindowScaleX'
        ),
    })
    map_screen_clip_window_scale_y: float = dataclasses.field(default=0.6349999904632568, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa9a53853, original_name='MapScreenClipWindowScaleY'
        ),
    })
    map_screen_move2_d_hover_depth: float = dataclasses.field(default=-0.05000000074505806, metadata={
        'reflection': FieldReflection[float](
            float, id=0x722b1bc0, original_name='MapScreenMove2DHoverDepth'
        ),
    })
    player_model_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x4c3fc933, original_name='PlayerModelColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    player_flashed_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x5a87c156, original_name='PlayerFlashedColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    player_surface_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.78125, g=0.19607800245285034, b=0.19607800245285034, a=0.78125), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x9c0c5318, original_name='PlayerSurfaceColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    player_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.3921569883823395, b=0.3921569883823395, a=0.78125), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x2a247ede, original_name='PlayerOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    text_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x44303a9c, original_name='TextColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    text_outline_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xf2e13506, original_name='TextOutlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    scanline_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x1a4b8068, original_name='ScanlineColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    frame_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xa485372c, original_name='FrameColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    title_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x536647d5, original_name='TitleColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    legend_background_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xa6b633fa, original_name='LegendBackgroundColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    legend_gradient_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=1.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x01cea7f9, original_name='LegendGradientColor', from_json=Color.from_json, to_json=Color.to_json
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
        if property_count != 79:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LH?LH?LH?LHfLHfLHfLHfLHfLHfLHfLHffffLHfLHfLHfLHfLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHfLHfLHfLHfLHfLHfLHfLHfLHfLHffffLHffffLHffffLHffffLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLH?LHfLHfLHfLHfLHfLHfLHfLHfLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffffLHffff')
    
        dec = _FAST_FORMAT.unpack(data.read(1126))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24], dec[27], dec[30], dec[36], dec[39], dec[42], dec[45], dec[48], dec[54], dec[60], dec[66], dec[72], dec[78], dec[84], dec[90], dec[96], dec[102], dec[108], dec[114], dec[120], dec[126], dec[129], dec[132], dec[135], dec[138], dec[141], dec[144], dec[147], dec[150], dec[153], dec[159], dec[165], dec[171], dec[177], dec[180], dec[183], dec[186], dec[189], dec[192], dec[195], dec[198], dec[201], dec[204], dec[207], dec[210], dec[213], dec[216], dec[219], dec[222], dec[225], dec[228], dec[231], dec[234], dec[237], dec[240], dec[243], dec[246], dec[249], dec[252], dec[255], dec[258], dec[264], dec[270], dec[276], dec[282], dec[288], dec[294], dec[300], dec[306], dec[312], dec[318]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
            dec[26],
            dec[29],
            Color(*dec[32:36]),
            dec[38],
            dec[41],
            dec[44],
            dec[47],
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
            dec[128],
            dec[131],
            dec[134],
            dec[137],
            dec[140],
            dec[143],
            dec[146],
            dec[149],
            dec[152],
            Color(*dec[155:159]),
            Color(*dec[161:165]),
            Color(*dec[167:171]),
            Color(*dec[173:177]),
            dec[179],
            dec[182],
            dec[185],
            dec[188],
            dec[191],
            dec[194],
            dec[197],
            dec[200],
            dec[203],
            dec[206],
            dec[209],
            dec[212],
            dec[215],
            dec[218],
            dec[221],
            dec[224],
            dec[227],
            dec[230],
            dec[233],
            dec[236],
            dec[239],
            dec[242],
            dec[245],
            dec[248],
            dec[251],
            dec[254],
            dec[257],
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
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00O')  # 79 properties

        data.write(b'\xcb\xe5\x95\xd8')  # 0xcbe595d8
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xcbe595d8))

        data.write(b'\x8e\xcbS\xa6')  # 0x8ecb53a6
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x8ecb53a6))

        data.write(b'0\xb17@')  # 0x30b13740
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.scale_move_speed_with_camera_distance))

        data.write(b'k\xea\x93$')  # 0x6bea9324
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_screen_camera_default_distance))

        data.write(b'\x06]\xd7T')  # 0x65dd754
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_screen_camera_min_distance))

        data.write(b'W\xa4l\t')  # 0x57a46c09
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_screen_camera_max_distance))

        data.write(b'\xb5BU\xb5')  # 0xb54255b5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_screen_camera_min_x_angle))

        data.write(b'\x0cd\xce\xc4')  # 0xc64cec4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_screen_camera_max_x_angle))

        data.write(b'3^\xbc~')  # 0x335ebc7e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_screen_camera_fov))

        data.write(b'E\xbe?k')  # 0x45be3f6b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_screen_area_opacity))

        data.write(b'S<V\x84')  # 0x533c5684
        data.write(b'\x00\x10')  # size
        self.map_screen_bg_color.to_stream(data, game)

        data.write(b'\xeb86h')  # 0xeb383668
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.mini_map_camera_distance))

        data.write(b"'\x15\x1e\xde")  # 0x27151ede
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.mini_map_camera_angle))

        data.write(b'CAr\xc3')  # 0x434172c3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.mini_map_camera_fov))

        data.write(b'h\tp6')  # 0x68097036
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.mini_map_area_opacity))

        data.write(b'\x03\xad\xcfF')  # 0x3adcf46
        data.write(b'\x00\x10')  # size
        self.mini_map_bg_color.to_stream(data, game)

        data.write(b'\xd3\xfa\xe2\x83')  # 0xd3fae283
        data.write(b'\x00\x10')  # size
        self.map_visited_surface_color.to_stream(data, game)

        data.write(b'e\xd2\xcfE')  # 0x65d2cf45
        data.write(b'\x00\x10')  # size
        self.map_visited_outline_color.to_stream(data, game)

        data.write(b'\xb5u,\x08')  # 0xb5752c08
        data.write(b'\x00\x10')  # size
        self.map_unvisited_surface_color.to_stream(data, game)

        data.write(b'\x03]\x01\xce')  # 0x35d01ce
        data.write(b'\x00\x10')  # size
        self.map_unvisited_outline_color.to_stream(data, game)

        data.write(b'\x80]_\xa3')  # 0x805d5fa3
        data.write(b'\x00\x10')  # size
        self.map_visited_focus_area_surface_color.to_stream(data, game)

        data.write(b'6ure')  # 0x36757265
        data.write(b'\x00\x10')  # size
        self.map_visited_focus_area_outline_color.to_stream(data, game)

        data.write(b'\xe5P\xfc\xbd')  # 0xe550fcbd
        data.write(b'\x00\x10')  # size
        self.dark_map_visited_surface_color.to_stream(data, game)

        data.write(b'Sx\xd1{')  # 0x5378d17b
        data.write(b'\x00\x10')  # size
        self.dark_map_visited_outline_color.to_stream(data, game)

        data.write(b'\x0e\xbf<\xbc')  # 0xebf3cbc
        data.write(b'\x00\x10')  # size
        self.dark_map_unvisited_surface_color.to_stream(data, game)

        data.write(b'\xb8\x97\x11z')  # 0xb897117a
        data.write(b'\x00\x10')  # size
        self.dark_map_unvisited_outline_color.to_stream(data, game)

        data.write(b'>g\x0fj')  # 0x3e670f6a
        data.write(b'\x00\x10')  # size
        self.dark_map_visited_focus_area_surface_color.to_stream(data, game)

        data.write(b'\x88O"\xac')  # 0x884f22ac
        data.write(b'\x00\x10')  # size
        self.dark_map_visited_focus_area_outline_color.to_stream(data, game)

        data.write(b'{\xdb\x0e\xdf')  # 0x7bdb0edf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_light_color_intensity))

        data.write(b'\x12"\x19\t')  # 0x12221909
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_ambient_color_intensity))

        data.write(b'8\xdb\xbc\t')  # 0x38dbbc09
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.off_to_mini_map_time))

        data.write(b'0a\x00b')  # 0x30610062
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.mini_map_to_map_screen_time))

        data.write(b'\xb6\xac\xea\x88')  # 0xb6acea88
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_screen_to_mini_map_time))

        data.write(b's\xdeA\x10')  # 0x73de4110
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x73de4110))

        data.write(b'\x19\x06\x97%')  # 0x19069725
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_screen_zoom_speed))

        data.write(b'[\xa0\xde\x1e')  # 0x5ba0de1e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_screen_circle_speed))

        data.write(b'1\x0b7\xa1')  # 0x310b37a1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_screen_move_speed))

        data.write(b'\xab\x82\xe2h')  # 0xab82e268
        data.write(b'\x00\x10')  # size
        self.map_unvisited_focus_area_surface_color.to_stream(data, game)

        data.write(b'\x1d\xaa\xcf\xae')  # 0x1daacfae
        data.write(b'\x00\x10')  # size
        self.map_unvisited_focus_area_outline_color.to_stream(data, game)

        data.write(b'\xda\xd1a\xa1')  # 0xdad161a1
        data.write(b'\x00\x10')  # size
        self.dark_map_unvisited_focus_area_surface_color.to_stream(data, game)

        data.write(b'l\xf9Lg')  # 0x6cf94c67
        data.write(b'\x00\x10')  # size
        self.dark_map_unvisited_focus_area_outline_color.to_stream(data, game)

        data.write(b'G\x96t\x04')  # 0x47967404
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_visited_surface_alpha_mini_map))

        data.write(b'\x0e\xce\x19P')  # 0xece1950
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_visited_surface_alpha_map_screen))

        data.write(b'\x9a\xc1\xbd\xde')  # 0x9ac1bdde
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_visited_outline_alpha_mini_map))

        data.write(b'\x97\xa1\x93\x86')  # 0x97a19386
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_visited_outline_alpha_map_screen))

        data.write(b'\xcb\x9e:T')  # 0xcb9e3a54
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_unvisited_surface_alpha_mini_map))

        data.write(b'%\x11\xa4\x9b')  # 0x2511a49b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_unvisited_surface_alpha_map_screen))

        data.write(b'\x16\xc9\xf3\x8e')  # 0x16c9f38e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_unvisited_outline_alpha_mini_map))

        data.write(b'\xbc~.M')  # 0xbc7e2e4d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_unvisited_outline_alpha_map_screen))

        data.write(b'\x15VM2')  # 0x15564d32
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_door_half_height))

        data.write(b'\xf5G\x92`')  # 0xf5479260
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_door_half_width))

        data.write(b"'\x1bdN")  # 0x271b644e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_door_half_depth))

        data.write(b'R\xdc\x08\xc1')  # 0x52dc08c1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.mini_map_viewport_position_x))

        data.write(b'\x99\x80\xdbd')  # 0x9980db64
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.mini_map_viewport_position_y))

        data.write(b'#\xf5\x90W')  # 0x23f59057
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.mini_map_viewport_width))

        data.write(b'\xad=Z?')  # 0xad3d5a3f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.mini_map_viewport_height))

        data.write(b'3\x15\xd2+')  # 0x3315d22b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.mini_map_dynamic_camera_distance_scalar))

        data.write(b'\x9e@\x07\xb6')  # 0x9e4007b6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.mini_map_widget_half_width))

        data.write(b'z\x8d=F')  # 0x7a8d3d46
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.mini_map_widget_half_height))

        data.write(b'+\x97\xd6L')  # 0x2b97d64c
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x2b97d64c))

        data.write(b'\xbd\xc5|\xe0')  # 0xbdc57ce0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_screen_map_universe_default_camera_distance))

        data.write(b'}Y\xc8T')  # 0x7d59c854
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_screen_map_universe_min_camera_distance))

        data.write(b'<N\xf7\xd2')  # 0x3c4ef7d2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_screen_map_universe_max_camera_distance))

        data.write(b'+H>\x9f')  # 0x2b483e9f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_screen_to_map_universe_time))

        data.write(b'poR\xfe')  # 0x706f52fe
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x706f52fe))

        data.write(b'b\xf9\xeb\xf6')  # 0x62f9ebf6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_screen_clip_window_scale_x))

        data.write(b'\xa9\xa58S')  # 0xa9a53853
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_screen_clip_window_scale_y))

        data.write(b'r+\x1b\xc0')  # 0x722b1bc0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.map_screen_move2_d_hover_depth))

        data.write(b'L?\xc93')  # 0x4c3fc933
        data.write(b'\x00\x10')  # size
        self.player_model_color.to_stream(data, game)

        data.write(b'Z\x87\xc1V')  # 0x5a87c156
        data.write(b'\x00\x10')  # size
        self.player_flashed_color.to_stream(data, game)

        data.write(b'\x9c\x0cS\x18')  # 0x9c0c5318
        data.write(b'\x00\x10')  # size
        self.player_surface_color.to_stream(data, game)

        data.write(b'*$~\xde')  # 0x2a247ede
        data.write(b'\x00\x10')  # size
        self.player_outline_color.to_stream(data, game)

        data.write(b'D0:\x9c')  # 0x44303a9c
        data.write(b'\x00\x10')  # size
        self.text_color.to_stream(data, game)

        data.write(b'\xf2\xe15\x06')  # 0xf2e13506
        data.write(b'\x00\x10')  # size
        self.text_outline_color.to_stream(data, game)

        data.write(b'\x1aK\x80h')  # 0x1a4b8068
        data.write(b'\x00\x10')  # size
        self.scanline_color.to_stream(data, game)

        data.write(b'\xa4\x857,')  # 0xa485372c
        data.write(b'\x00\x10')  # size
        self.frame_color.to_stream(data, game)

        data.write(b'SfG\xd5')  # 0x536647d5
        data.write(b'\x00\x10')  # size
        self.title_color.to_stream(data, game)

        data.write(b'\xa6\xb63\xfa')  # 0xa6b633fa
        data.write(b'\x00\x10')  # size
        self.legend_background_color.to_stream(data, game)

        data.write(b'\x01\xce\xa7\xf9')  # 0x1cea7f9
        data.write(b'\x00\x10')  # size
        self.legend_gradient_color.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakAutoMapper_BaseJson", data)
        return cls(
            unknown_0xcbe595d8=json_data['unknown_0xcbe595d8'],
            unknown_0x8ecb53a6=json_data['unknown_0x8ecb53a6'],
            scale_move_speed_with_camera_distance=json_data['scale_move_speed_with_camera_distance'],
            map_screen_camera_default_distance=json_data['map_screen_camera_default_distance'],
            map_screen_camera_min_distance=json_data['map_screen_camera_min_distance'],
            map_screen_camera_max_distance=json_data['map_screen_camera_max_distance'],
            map_screen_camera_min_x_angle=json_data['map_screen_camera_min_x_angle'],
            map_screen_camera_max_x_angle=json_data['map_screen_camera_max_x_angle'],
            map_screen_camera_fov=json_data['map_screen_camera_fov'],
            map_screen_area_opacity=json_data['map_screen_area_opacity'],
            map_screen_bg_color=Color.from_json(json_data['map_screen_bg_color']),
            mini_map_camera_distance=json_data['mini_map_camera_distance'],
            mini_map_camera_angle=json_data['mini_map_camera_angle'],
            mini_map_camera_fov=json_data['mini_map_camera_fov'],
            mini_map_area_opacity=json_data['mini_map_area_opacity'],
            mini_map_bg_color=Color.from_json(json_data['mini_map_bg_color']),
            map_visited_surface_color=Color.from_json(json_data['map_visited_surface_color']),
            map_visited_outline_color=Color.from_json(json_data['map_visited_outline_color']),
            map_unvisited_surface_color=Color.from_json(json_data['map_unvisited_surface_color']),
            map_unvisited_outline_color=Color.from_json(json_data['map_unvisited_outline_color']),
            map_visited_focus_area_surface_color=Color.from_json(json_data['map_visited_focus_area_surface_color']),
            map_visited_focus_area_outline_color=Color.from_json(json_data['map_visited_focus_area_outline_color']),
            dark_map_visited_surface_color=Color.from_json(json_data['dark_map_visited_surface_color']),
            dark_map_visited_outline_color=Color.from_json(json_data['dark_map_visited_outline_color']),
            dark_map_unvisited_surface_color=Color.from_json(json_data['dark_map_unvisited_surface_color']),
            dark_map_unvisited_outline_color=Color.from_json(json_data['dark_map_unvisited_outline_color']),
            dark_map_visited_focus_area_surface_color=Color.from_json(json_data['dark_map_visited_focus_area_surface_color']),
            dark_map_visited_focus_area_outline_color=Color.from_json(json_data['dark_map_visited_focus_area_outline_color']),
            map_light_color_intensity=json_data['map_light_color_intensity'],
            map_ambient_color_intensity=json_data['map_ambient_color_intensity'],
            off_to_mini_map_time=json_data['off_to_mini_map_time'],
            mini_map_to_map_screen_time=json_data['mini_map_to_map_screen_time'],
            map_screen_to_mini_map_time=json_data['map_screen_to_mini_map_time'],
            unknown_0x73de4110=json_data['unknown_0x73de4110'],
            map_screen_zoom_speed=json_data['map_screen_zoom_speed'],
            map_screen_circle_speed=json_data['map_screen_circle_speed'],
            map_screen_move_speed=json_data['map_screen_move_speed'],
            map_unvisited_focus_area_surface_color=Color.from_json(json_data['map_unvisited_focus_area_surface_color']),
            map_unvisited_focus_area_outline_color=Color.from_json(json_data['map_unvisited_focus_area_outline_color']),
            dark_map_unvisited_focus_area_surface_color=Color.from_json(json_data['dark_map_unvisited_focus_area_surface_color']),
            dark_map_unvisited_focus_area_outline_color=Color.from_json(json_data['dark_map_unvisited_focus_area_outline_color']),
            map_visited_surface_alpha_mini_map=json_data['map_visited_surface_alpha_mini_map'],
            map_visited_surface_alpha_map_screen=json_data['map_visited_surface_alpha_map_screen'],
            map_visited_outline_alpha_mini_map=json_data['map_visited_outline_alpha_mini_map'],
            map_visited_outline_alpha_map_screen=json_data['map_visited_outline_alpha_map_screen'],
            map_unvisited_surface_alpha_mini_map=json_data['map_unvisited_surface_alpha_mini_map'],
            map_unvisited_surface_alpha_map_screen=json_data['map_unvisited_surface_alpha_map_screen'],
            map_unvisited_outline_alpha_mini_map=json_data['map_unvisited_outline_alpha_mini_map'],
            map_unvisited_outline_alpha_map_screen=json_data['map_unvisited_outline_alpha_map_screen'],
            map_door_half_height=json_data['map_door_half_height'],
            map_door_half_width=json_data['map_door_half_width'],
            map_door_half_depth=json_data['map_door_half_depth'],
            mini_map_viewport_position_x=json_data['mini_map_viewport_position_x'],
            mini_map_viewport_position_y=json_data['mini_map_viewport_position_y'],
            mini_map_viewport_width=json_data['mini_map_viewport_width'],
            mini_map_viewport_height=json_data['mini_map_viewport_height'],
            mini_map_dynamic_camera_distance_scalar=json_data['mini_map_dynamic_camera_distance_scalar'],
            mini_map_widget_half_width=json_data['mini_map_widget_half_width'],
            mini_map_widget_half_height=json_data['mini_map_widget_half_height'],
            unknown_0x2b97d64c=json_data['unknown_0x2b97d64c'],
            map_screen_map_universe_default_camera_distance=json_data['map_screen_map_universe_default_camera_distance'],
            map_screen_map_universe_min_camera_distance=json_data['map_screen_map_universe_min_camera_distance'],
            map_screen_map_universe_max_camera_distance=json_data['map_screen_map_universe_max_camera_distance'],
            map_screen_to_map_universe_time=json_data['map_screen_to_map_universe_time'],
            unknown_0x706f52fe=json_data['unknown_0x706f52fe'],
            map_screen_clip_window_scale_x=json_data['map_screen_clip_window_scale_x'],
            map_screen_clip_window_scale_y=json_data['map_screen_clip_window_scale_y'],
            map_screen_move2_d_hover_depth=json_data['map_screen_move2_d_hover_depth'],
            player_model_color=Color.from_json(json_data['player_model_color']),
            player_flashed_color=Color.from_json(json_data['player_flashed_color']),
            player_surface_color=Color.from_json(json_data['player_surface_color']),
            player_outline_color=Color.from_json(json_data['player_outline_color']),
            text_color=Color.from_json(json_data['text_color']),
            text_outline_color=Color.from_json(json_data['text_outline_color']),
            scanline_color=Color.from_json(json_data['scanline_color']),
            frame_color=Color.from_json(json_data['frame_color']),
            title_color=Color.from_json(json_data['title_color']),
            legend_background_color=Color.from_json(json_data['legend_background_color']),
            legend_gradient_color=Color.from_json(json_data['legend_gradient_color']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'unknown_0xcbe595d8': self.unknown_0xcbe595d8,
            'unknown_0x8ecb53a6': self.unknown_0x8ecb53a6,
            'scale_move_speed_with_camera_distance': self.scale_move_speed_with_camera_distance,
            'map_screen_camera_default_distance': self.map_screen_camera_default_distance,
            'map_screen_camera_min_distance': self.map_screen_camera_min_distance,
            'map_screen_camera_max_distance': self.map_screen_camera_max_distance,
            'map_screen_camera_min_x_angle': self.map_screen_camera_min_x_angle,
            'map_screen_camera_max_x_angle': self.map_screen_camera_max_x_angle,
            'map_screen_camera_fov': self.map_screen_camera_fov,
            'map_screen_area_opacity': self.map_screen_area_opacity,
            'map_screen_bg_color': self.map_screen_bg_color.to_json(),
            'mini_map_camera_distance': self.mini_map_camera_distance,
            'mini_map_camera_angle': self.mini_map_camera_angle,
            'mini_map_camera_fov': self.mini_map_camera_fov,
            'mini_map_area_opacity': self.mini_map_area_opacity,
            'mini_map_bg_color': self.mini_map_bg_color.to_json(),
            'map_visited_surface_color': self.map_visited_surface_color.to_json(),
            'map_visited_outline_color': self.map_visited_outline_color.to_json(),
            'map_unvisited_surface_color': self.map_unvisited_surface_color.to_json(),
            'map_unvisited_outline_color': self.map_unvisited_outline_color.to_json(),
            'map_visited_focus_area_surface_color': self.map_visited_focus_area_surface_color.to_json(),
            'map_visited_focus_area_outline_color': self.map_visited_focus_area_outline_color.to_json(),
            'dark_map_visited_surface_color': self.dark_map_visited_surface_color.to_json(),
            'dark_map_visited_outline_color': self.dark_map_visited_outline_color.to_json(),
            'dark_map_unvisited_surface_color': self.dark_map_unvisited_surface_color.to_json(),
            'dark_map_unvisited_outline_color': self.dark_map_unvisited_outline_color.to_json(),
            'dark_map_visited_focus_area_surface_color': self.dark_map_visited_focus_area_surface_color.to_json(),
            'dark_map_visited_focus_area_outline_color': self.dark_map_visited_focus_area_outline_color.to_json(),
            'map_light_color_intensity': self.map_light_color_intensity,
            'map_ambient_color_intensity': self.map_ambient_color_intensity,
            'off_to_mini_map_time': self.off_to_mini_map_time,
            'mini_map_to_map_screen_time': self.mini_map_to_map_screen_time,
            'map_screen_to_mini_map_time': self.map_screen_to_mini_map_time,
            'unknown_0x73de4110': self.unknown_0x73de4110,
            'map_screen_zoom_speed': self.map_screen_zoom_speed,
            'map_screen_circle_speed': self.map_screen_circle_speed,
            'map_screen_move_speed': self.map_screen_move_speed,
            'map_unvisited_focus_area_surface_color': self.map_unvisited_focus_area_surface_color.to_json(),
            'map_unvisited_focus_area_outline_color': self.map_unvisited_focus_area_outline_color.to_json(),
            'dark_map_unvisited_focus_area_surface_color': self.dark_map_unvisited_focus_area_surface_color.to_json(),
            'dark_map_unvisited_focus_area_outline_color': self.dark_map_unvisited_focus_area_outline_color.to_json(),
            'map_visited_surface_alpha_mini_map': self.map_visited_surface_alpha_mini_map,
            'map_visited_surface_alpha_map_screen': self.map_visited_surface_alpha_map_screen,
            'map_visited_outline_alpha_mini_map': self.map_visited_outline_alpha_mini_map,
            'map_visited_outline_alpha_map_screen': self.map_visited_outline_alpha_map_screen,
            'map_unvisited_surface_alpha_mini_map': self.map_unvisited_surface_alpha_mini_map,
            'map_unvisited_surface_alpha_map_screen': self.map_unvisited_surface_alpha_map_screen,
            'map_unvisited_outline_alpha_mini_map': self.map_unvisited_outline_alpha_mini_map,
            'map_unvisited_outline_alpha_map_screen': self.map_unvisited_outline_alpha_map_screen,
            'map_door_half_height': self.map_door_half_height,
            'map_door_half_width': self.map_door_half_width,
            'map_door_half_depth': self.map_door_half_depth,
            'mini_map_viewport_position_x': self.mini_map_viewport_position_x,
            'mini_map_viewport_position_y': self.mini_map_viewport_position_y,
            'mini_map_viewport_width': self.mini_map_viewport_width,
            'mini_map_viewport_height': self.mini_map_viewport_height,
            'mini_map_dynamic_camera_distance_scalar': self.mini_map_dynamic_camera_distance_scalar,
            'mini_map_widget_half_width': self.mini_map_widget_half_width,
            'mini_map_widget_half_height': self.mini_map_widget_half_height,
            'unknown_0x2b97d64c': self.unknown_0x2b97d64c,
            'map_screen_map_universe_default_camera_distance': self.map_screen_map_universe_default_camera_distance,
            'map_screen_map_universe_min_camera_distance': self.map_screen_map_universe_min_camera_distance,
            'map_screen_map_universe_max_camera_distance': self.map_screen_map_universe_max_camera_distance,
            'map_screen_to_map_universe_time': self.map_screen_to_map_universe_time,
            'unknown_0x706f52fe': self.unknown_0x706f52fe,
            'map_screen_clip_window_scale_x': self.map_screen_clip_window_scale_x,
            'map_screen_clip_window_scale_y': self.map_screen_clip_window_scale_y,
            'map_screen_move2_d_hover_depth': self.map_screen_move2_d_hover_depth,
            'player_model_color': self.player_model_color.to_json(),
            'player_flashed_color': self.player_flashed_color.to_json(),
            'player_surface_color': self.player_surface_color.to_json(),
            'player_outline_color': self.player_outline_color.to_json(),
            'text_color': self.text_color.to_json(),
            'text_outline_color': self.text_outline_color.to_json(),
            'scanline_color': self.scanline_color.to_json(),
            'frame_color': self.frame_color.to_json(),
            'title_color': self.title_color.to_json(),
            'legend_background_color': self.legend_background_color.to_json(),
            'legend_gradient_color': self.legend_gradient_color.to_json(),
        }


def _decode_map_screen_bg_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_mini_map_bg_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_map_visited_surface_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_map_visited_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_map_unvisited_surface_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_map_unvisited_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_map_visited_focus_area_surface_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_map_visited_focus_area_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_map_visited_surface_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_map_visited_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_map_unvisited_surface_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_map_unvisited_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_map_visited_focus_area_surface_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_map_visited_focus_area_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_map_unvisited_focus_area_surface_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_map_unvisited_focus_area_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_map_unvisited_focus_area_surface_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_dark_map_unvisited_focus_area_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_player_model_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_player_flashed_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_player_surface_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_player_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_text_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_text_outline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_scanline_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_frame_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_title_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_legend_background_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_legend_gradient_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xcbe595d8: ('unknown_0xcbe595d8', structs.decode_BIG_bool_),
    0x8ecb53a6: ('unknown_0x8ecb53a6', structs.decode_BIG_bool_),
    0x30b13740: ('scale_move_speed_with_camera_distance', structs.decode_BIG_bool_),
    0x6bea9324: ('map_screen_camera_default_distance', structs.decode_BIG_f),
    0x065dd754: ('map_screen_camera_min_distance', structs.decode_BIG_f),
    0x57a46c09: ('map_screen_camera_max_distance', structs.decode_BIG_f),
    0xb54255b5: ('map_screen_camera_min_x_angle', structs.decode_BIG_f),
    0x0c64cec4: ('map_screen_camera_max_x_angle', structs.decode_BIG_f),
    0x335ebc7e: ('map_screen_camera_fov', structs.decode_BIG_f),
    0x45be3f6b: ('map_screen_area_opacity', structs.decode_BIG_f),
    0x533c5684: ('map_screen_bg_color', _decode_map_screen_bg_color),
    0xeb383668: ('mini_map_camera_distance', structs.decode_BIG_f),
    0x27151ede: ('mini_map_camera_angle', structs.decode_BIG_f),
    0x434172c3: ('mini_map_camera_fov', structs.decode_BIG_f),
    0x68097036: ('mini_map_area_opacity', structs.decode_BIG_f),
    0x03adcf46: ('mini_map_bg_color', _decode_mini_map_bg_color),
    0xd3fae283: ('map_visited_surface_color', _decode_map_visited_surface_color),
    0x65d2cf45: ('map_visited_outline_color', _decode_map_visited_outline_color),
    0xb5752c08: ('map_unvisited_surface_color', _decode_map_unvisited_surface_color),
    0x035d01ce: ('map_unvisited_outline_color', _decode_map_unvisited_outline_color),
    0x805d5fa3: ('map_visited_focus_area_surface_color', _decode_map_visited_focus_area_surface_color),
    0x36757265: ('map_visited_focus_area_outline_color', _decode_map_visited_focus_area_outline_color),
    0xe550fcbd: ('dark_map_visited_surface_color', _decode_dark_map_visited_surface_color),
    0x5378d17b: ('dark_map_visited_outline_color', _decode_dark_map_visited_outline_color),
    0x0ebf3cbc: ('dark_map_unvisited_surface_color', _decode_dark_map_unvisited_surface_color),
    0xb897117a: ('dark_map_unvisited_outline_color', _decode_dark_map_unvisited_outline_color),
    0x3e670f6a: ('dark_map_visited_focus_area_surface_color', _decode_dark_map_visited_focus_area_surface_color),
    0x884f22ac: ('dark_map_visited_focus_area_outline_color', _decode_dark_map_visited_focus_area_outline_color),
    0x7bdb0edf: ('map_light_color_intensity', structs.decode_BIG_f),
    0x12221909: ('map_ambient_color_intensity', structs.decode_BIG_f),
    0x38dbbc09: ('off_to_mini_map_time', structs.decode_BIG_f),
    0x30610062: ('mini_map_to_map_screen_time', structs.decode_BIG_f),
    0xb6acea88: ('map_screen_to_mini_map_time', structs.decode_BIG_f),
    0x73de4110: ('unknown_0x73de4110', structs.decode_BIG_f),
    0x19069725: ('map_screen_zoom_speed', structs.decode_BIG_f),
    0x5ba0de1e: ('map_screen_circle_speed', structs.decode_BIG_f),
    0x310b37a1: ('map_screen_move_speed', structs.decode_BIG_f),
    0xab82e268: ('map_unvisited_focus_area_surface_color', _decode_map_unvisited_focus_area_surface_color),
    0x1daacfae: ('map_unvisited_focus_area_outline_color', _decode_map_unvisited_focus_area_outline_color),
    0xdad161a1: ('dark_map_unvisited_focus_area_surface_color', _decode_dark_map_unvisited_focus_area_surface_color),
    0x6cf94c67: ('dark_map_unvisited_focus_area_outline_color', _decode_dark_map_unvisited_focus_area_outline_color),
    0x47967404: ('map_visited_surface_alpha_mini_map', structs.decode_BIG_f),
    0x0ece1950: ('map_visited_surface_alpha_map_screen', structs.decode_BIG_f),
    0x9ac1bdde: ('map_visited_outline_alpha_mini_map', structs.decode_BIG_f),
    0x97a19386: ('map_visited_outline_alpha_map_screen', structs.decode_BIG_f),
    0xcb9e3a54: ('map_unvisited_surface_alpha_mini_map', structs.decode_BIG_f),
    0x2511a49b: ('map_unvisited_surface_alpha_map_screen', structs.decode_BIG_f),
    0x16c9f38e: ('map_unvisited_outline_alpha_mini_map', structs.decode_BIG_f),
    0xbc7e2e4d: ('map_unvisited_outline_alpha_map_screen', structs.decode_BIG_f),
    0x15564d32: ('map_door_half_height', structs.decode_BIG_f),
    0xf5479260: ('map_door_half_width', structs.decode_BIG_f),
    0x271b644e: ('map_door_half_depth', structs.decode_BIG_f),
    0x52dc08c1: ('mini_map_viewport_position_x', structs.decode_BIG_f),
    0x9980db64: ('mini_map_viewport_position_y', structs.decode_BIG_f),
    0x23f59057: ('mini_map_viewport_width', structs.decode_BIG_f),
    0xad3d5a3f: ('mini_map_viewport_height', structs.decode_BIG_f),
    0x3315d22b: ('mini_map_dynamic_camera_distance_scalar', structs.decode_BIG_f),
    0x9e4007b6: ('mini_map_widget_half_width', structs.decode_BIG_f),
    0x7a8d3d46: ('mini_map_widget_half_height', structs.decode_BIG_f),
    0x2b97d64c: ('unknown_0x2b97d64c', structs.decode_BIG_bool_),
    0xbdc57ce0: ('map_screen_map_universe_default_camera_distance', structs.decode_BIG_f),
    0x7d59c854: ('map_screen_map_universe_min_camera_distance', structs.decode_BIG_f),
    0x3c4ef7d2: ('map_screen_map_universe_max_camera_distance', structs.decode_BIG_f),
    0x2b483e9f: ('map_screen_to_map_universe_time', structs.decode_BIG_f),
    0x706f52fe: ('unknown_0x706f52fe', structs.decode_BIG_f),
    0x62f9ebf6: ('map_screen_clip_window_scale_x', structs.decode_BIG_f),
    0xa9a53853: ('map_screen_clip_window_scale_y', structs.decode_BIG_f),
    0x722b1bc0: ('map_screen_move2_d_hover_depth', structs.decode_BIG_f),
    0x4c3fc933: ('player_model_color', _decode_player_model_color),
    0x5a87c156: ('player_flashed_color', _decode_player_flashed_color),
    0x9c0c5318: ('player_surface_color', _decode_player_surface_color),
    0x2a247ede: ('player_outline_color', _decode_player_outline_color),
    0x44303a9c: ('text_color', _decode_text_color),
    0xf2e13506: ('text_outline_color', _decode_text_outline_color),
    0x1a4b8068: ('scanline_color', _decode_scanline_color),
    0xa485372c: ('frame_color', _decode_frame_color),
    0x536647d5: ('title_color', _decode_title_color),
    0xa6b633fa: ('legend_background_color', _decode_legend_background_color),
    0x01cea7f9: ('legend_gradient_color', _decode_legend_gradient_color),
}
