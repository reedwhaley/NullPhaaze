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
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.archetypes.LayerInfo import LayerInfo
from retro_data_structures.properties.echoes.archetypes.TriggerInfo import TriggerInfo
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class WaterJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        trigger: json_util.JsonObject
        alpha_fadein_time: float
        alpha_fadeout_time: float
        morph_time_to: float
        morph_time_restore: float
        fluid_type: int
        light_map: int
        color_map: int
        color_warp_map: int
        gloss_map: int
        env_map: int
        env_map_size: float
        refract_warp_map: int
        foam_map: int
        alpha_map: int
        base_color: json_util.JsonValue
        alpha: float
        gloss_flat: float
        gloss_top_down: float
        refract_warp_flat: float
        refract_warp_top_down: float
        flow_color: json_util.JsonObject
        flow_color_warp: json_util.JsonObject
        flow_gloss1: json_util.JsonObject
        flow_gloss2: json_util.JsonObject
        flow_refract_warp: json_util.JsonObject
        flow_speed: float
        flow_orientation: float
        underwater_fog_color: json_util.JsonValue
        splash_color: json_util.JsonValue
        splash_small: int
        splash_medium: int
        splash_big: int
        visor_runoff: int
        visor_runoff_ball: int
        sound_sound_runoff: int
        sound_sound_runoff_ball: int
        sound_splash_small: int
        sound_splash_medium: int
        sound_splash_big: int
        fog_color: json_util.JsonValue
        fog_height: float
        fog_bob_height: float
        fog_bob_freq: float
        fog_no_grav_suit_dist: float
        fog_no_grav_suit_factor: float
        fog_grav_suit_dist: float
        fog_grav_suit_factor: float
        viscosity: float
        render_surface: bool
        use_dynamic_lights: bool
        render_tile_scale_x: float
        render_tile_scale_y: float
        light_map_resolution: float
        light_map_scale_x: float
        light_map_scale_y: float
        light_map_offset_x: float
        light_map_offset_y: float
        unknown: bool
        filter_sound_effects: bool
        filter_cutoff_frequency: int
    

@dataclasses.dataclass()
class Water(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    trigger: TriggerInfo = dataclasses.field(default_factory=TriggerInfo, metadata={
        'reflection': FieldReflection[TriggerInfo](
            TriggerInfo, id=0x77a27411, original_name='Trigger', from_json=TriggerInfo.from_json, to_json=TriggerInfo.to_json
        ),
    })
    alpha_fadein_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xde5ea267, original_name='AlphaFadeinTime'
        ),
    })
    alpha_fadeout_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x22b69324, original_name='AlphaFadeoutTime'
        ),
    })
    morph_time_to: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4c60077e, original_name='MorphTimeTo'
        ),
    })
    morph_time_restore: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8518047a, original_name='MorphTimeRestore'
        ),
    })
    fluid_type: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x7d606b78, original_name='FluidType'
        ),
    })  # Choice
    light_map: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['TXTR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2421a2bf, original_name='LightMap'
        ),
    })
    color_map: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['TXTR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5e8b37dd, original_name='ColorMap'
        ),
    })
    color_warp_map: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['TXTR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x031d987e, original_name='ColorWarpMap'
        ),
    })
    gloss_map: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['TXTR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5aa79c9f, original_name='GlossMap'
        ),
    })
    env_map: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['TXTR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2f0645cf, original_name='EnvMap'
        ),
    })
    env_map_size: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xde054447, original_name='EnvMapSize'
        ),
    })
    refract_warp_map: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['TXTR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x7a4b4685, original_name='RefractWarpMap'
        ),
    })
    foam_map: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['TXTR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5ba7702e, original_name='FoamMap'
        ),
    })
    alpha_map: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['TXTR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x9a3463a7, original_name='AlphaMap'
        ),
    })
    base_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.5, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x041398d5, original_name='BaseColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    alpha: float = dataclasses.field(default=0.6000000238418579, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0f7c6fc2, original_name='Alpha'
        ),
    })
    gloss_flat: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0x26382fcb, original_name='GlossFlat'
        ),
    })
    gloss_top_down: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc63a0616, original_name='GlossTopDown'
        ),
    })
    refract_warp_flat: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdb7a3a6b, original_name='RefractWarpFlat'
        ),
    })
    refract_warp_top_down: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb0259d23, original_name='RefractWarpTopDown'
        ),
    })
    flow_color: LayerInfo = dataclasses.field(default_factory=LayerInfo, metadata={
        'reflection': FieldReflection[LayerInfo](
            LayerInfo, id=0x244e9e6d, original_name='FlowColor', from_json=LayerInfo.from_json, to_json=LayerInfo.to_json
        ),
    })
    flow_color_warp: LayerInfo = dataclasses.field(default_factory=LayerInfo, metadata={
        'reflection': FieldReflection[LayerInfo](
            LayerInfo, id=0xe75248e4, original_name='FlowColorWarp', from_json=LayerInfo.from_json, to_json=LayerInfo.to_json
        ),
    })
    flow_gloss1: LayerInfo = dataclasses.field(default_factory=LayerInfo, metadata={
        'reflection': FieldReflection[LayerInfo](
            LayerInfo, id=0x385e0d43, original_name='FlowGloss1', from_json=LayerInfo.from_json, to_json=LayerInfo.to_json
        ),
    })
    flow_gloss2: LayerInfo = dataclasses.field(default_factory=LayerInfo, metadata={
        'reflection': FieldReflection[LayerInfo](
            LayerInfo, id=0xd369b640, original_name='FlowGloss2', from_json=LayerInfo.from_json, to_json=LayerInfo.to_json
        ),
    })
    flow_refract_warp: LayerInfo = dataclasses.field(default_factory=LayerInfo, metadata={
        'reflection': FieldReflection[LayerInfo](
            LayerInfo, id=0x6ddea66d, original_name='FlowRefractWarp', from_json=LayerInfo.from_json, to_json=LayerInfo.to_json
        ),
    })
    flow_speed: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf14e3a14, original_name='FlowSpeed'
        ),
    })
    flow_orientation: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x33eecdfd, original_name='FlowOrientation'
        ),
    })
    underwater_fog_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.5, b=1.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x5a96218c, original_name='UnderwaterFogColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    splash_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x13b56c22, original_name='SplashColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    splash_small: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3027043c, original_name='Splash_Small'
        ),
    })
    splash_medium: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x41c12be2, original_name='Splash_Medium'
        ),
    })
    splash_big: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd6e82200, original_name='Splash_Big'
        ),
    })
    visor_runoff: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x94a23bf9, original_name='VisorRunoff'
        ),
    })
    visor_runoff_ball: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x43a704fb, original_name='VisorRunoffBall'
        ),
    })
    sound_sound_runoff: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xba717f19, original_name='Sound_SoundRunoff'
        ),
    })
    sound_sound_runoff_ball: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xae7c7efc, original_name='Sound_SoundRunoffBall'
        ),
    })
    sound_splash_small: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xeef81e4c, original_name='Sound_Splash_Small'
        ),
    })
    sound_splash_medium: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x63c96763, original_name='Sound_Splash_Medium'
        ),
    })
    sound_splash_big: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xd36209bc, original_name='Sound_Splash_Big'
        ),
    })
    fog_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xe578c0dd, original_name='FogColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    fog_height: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb4b0fd8d, original_name='FogHeight'
        ),
    })
    fog_bob_height: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb90dff44, original_name='FogBobHeight'
        ),
    })
    fog_bob_freq: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf608d35c, original_name='FogBobFreq'
        ),
    })
    fog_no_grav_suit_dist: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd8521c1c, original_name='FogNoGravSuitDist'
        ),
    })
    fog_no_grav_suit_factor: float = dataclasses.field(default=125.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7dce5dc2, original_name='FogNoGravSuitFactor'
        ),
    })
    fog_grav_suit_dist: float = dataclasses.field(default=150.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x71819b3c, original_name='FogGravSuitDist'
        ),
    })
    fog_grav_suit_factor: float = dataclasses.field(default=300.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9b96c630, original_name='FogGravSuitFactor'
        ),
    })
    viscosity: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xffe26f5c, original_name='Viscosity'
        ),
    })
    render_surface: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xb5e9859f, original_name='RenderSurface'
        ),
    })
    use_dynamic_lights: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x3ddca674, original_name='UseDynamicLights'
        ),
    })
    render_tile_scale_x: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0e791782, original_name='RenderTileScaleX'
        ),
    })
    render_tile_scale_y: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc525c427, original_name='RenderTileScaleY'
        ),
    })
    light_map_resolution: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3425e83f, original_name='LightMapResolution'
        ),
    })
    light_map_scale_x: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2293fdb0, original_name='LightMapScaleX'
        ),
    })
    light_map_scale_y: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe9cf2e15, original_name='LightMapScaleY'
        ),
    })
    light_map_offset_x: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x268846d6, original_name='LightMapOffsetX'
        ),
    })
    light_map_offset_y: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xedd49573, original_name='LightMapOffsetY'
        ),
    })
    unknown: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xc71c0d63, original_name='Unknown'
        ),
    })
    filter_sound_effects: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x822118b4, original_name='FilterSoundEffects'
        ),
    })
    filter_cutoff_frequency: int = dataclasses.field(default=300, metadata={
        'reflection': FieldReflection[int](
            int, id=0x414379ea, original_name='FilterCutoffFrequency'
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'WATR'

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
        if property_count != 62:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77a27411
        trigger = TriggerInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xde5ea267
        alpha_fadein_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x22b69324
        alpha_fadeout_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4c60077e
        morph_time_to = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8518047a
        morph_time_restore = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7d606b78
        fluid_type = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2421a2bf
        light_map = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5e8b37dd
        color_map = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x031d987e
        color_warp_map = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5aa79c9f
        gloss_map = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2f0645cf
        env_map = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xde054447
        env_map_size = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7a4b4685
        refract_warp_map = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5ba7702e
        foam_map = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9a3463a7
        alpha_map = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x041398d5
        base_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0f7c6fc2
        alpha = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x26382fcb
        gloss_flat = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc63a0616
        gloss_top_down = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdb7a3a6b
        refract_warp_flat = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb0259d23
        refract_warp_top_down = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x244e9e6d
        flow_color = LayerInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe75248e4
        flow_color_warp = LayerInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x385e0d43
        flow_gloss1 = LayerInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd369b640
        flow_gloss2 = LayerInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6ddea66d
        flow_refract_warp = LayerInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf14e3a14
        flow_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33eecdfd
        flow_orientation = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5a96218c
        underwater_fog_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13b56c22
        splash_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3027043c
        splash_small = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x41c12be2
        splash_medium = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd6e82200
        splash_big = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x94a23bf9
        visor_runoff = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x43a704fb
        visor_runoff_ball = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xba717f19
        sound_sound_runoff = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xae7c7efc
        sound_sound_runoff_ball = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xeef81e4c
        sound_splash_small = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x63c96763
        sound_splash_medium = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd36209bc
        sound_splash_big = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe578c0dd
        fog_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb4b0fd8d
        fog_height = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb90dff44
        fog_bob_height = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf608d35c
        fog_bob_freq = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd8521c1c
        fog_no_grav_suit_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7dce5dc2
        fog_no_grav_suit_factor = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71819b3c
        fog_grav_suit_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9b96c630
        fog_grav_suit_factor = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xffe26f5c
        viscosity = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb5e9859f
        render_surface = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3ddca674
        use_dynamic_lights = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0e791782
        render_tile_scale_x = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc525c427
        render_tile_scale_y = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3425e83f
        light_map_resolution = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2293fdb0
        light_map_scale_x = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe9cf2e15
        light_map_scale_y = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x268846d6
        light_map_offset_x = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xedd49573
        light_map_offset_y = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc71c0d63
        unknown = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x822118b4
        filter_sound_effects = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x414379ea
        filter_cutoff_frequency = structs.BIG_l.unpack(data.read(4))[0]
    
        return cls(editor_properties, trigger, alpha_fadein_time, alpha_fadeout_time, morph_time_to, morph_time_restore, fluid_type, light_map, color_map, color_warp_map, gloss_map, env_map, env_map_size, refract_warp_map, foam_map, alpha_map, base_color, alpha, gloss_flat, gloss_top_down, refract_warp_flat, refract_warp_top_down, flow_color, flow_color_warp, flow_gloss1, flow_gloss2, flow_refract_warp, flow_speed, flow_orientation, underwater_fog_color, splash_color, splash_small, splash_medium, splash_big, visor_runoff, visor_runoff_ball, sound_sound_runoff, sound_sound_runoff_ball, sound_splash_small, sound_splash_medium, sound_splash_big, fog_color, fog_height, fog_bob_height, fog_bob_freq, fog_no_grav_suit_dist, fog_no_grav_suit_factor, fog_grav_suit_dist, fog_grav_suit_factor, viscosity, render_surface, use_dynamic_lights, render_tile_scale_x, render_tile_scale_y, light_map_resolution, light_map_scale_x, light_map_scale_y, light_map_offset_x, light_map_offset_y, unknown, filter_sound_effects, filter_cutoff_frequency)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00>')  # 62 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game, default_override={'misc_flags': 3})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'w\xa2t\x11')  # 0x77a27411
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.trigger.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xde^\xa2g')  # 0xde5ea267
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.alpha_fadein_time))

        data.write(b'"\xb6\x93$')  # 0x22b69324
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.alpha_fadeout_time))

        data.write(b'L`\x07~')  # 0x4c60077e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.morph_time_to))

        data.write(b'\x85\x18\x04z')  # 0x8518047a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.morph_time_restore))

        data.write(b'}`kx')  # 0x7d606b78
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.fluid_type))

        data.write(b'$!\xa2\xbf')  # 0x2421a2bf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.light_map))

        data.write(b'^\x8b7\xdd')  # 0x5e8b37dd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.color_map))

        data.write(b'\x03\x1d\x98~')  # 0x31d987e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.color_warp_map))

        data.write(b'Z\xa7\x9c\x9f')  # 0x5aa79c9f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.gloss_map))

        data.write(b'/\x06E\xcf')  # 0x2f0645cf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.env_map))

        data.write(b'\xde\x05DG')  # 0xde054447
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.env_map_size))

        data.write(b'zKF\x85')  # 0x7a4b4685
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.refract_warp_map))

        data.write(b'[\xa7p.')  # 0x5ba7702e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.foam_map))

        data.write(b'\x9a4c\xa7')  # 0x9a3463a7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.alpha_map))

        data.write(b'\x04\x13\x98\xd5')  # 0x41398d5
        data.write(b'\x00\x10')  # size
        self.base_color.to_stream(data, game)

        data.write(b'\x0f|o\xc2')  # 0xf7c6fc2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.alpha))

        data.write(b'&8/\xcb')  # 0x26382fcb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.gloss_flat))

        data.write(b'\xc6:\x06\x16')  # 0xc63a0616
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.gloss_top_down))

        data.write(b'\xdbz:k')  # 0xdb7a3a6b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.refract_warp_flat))

        data.write(b'\xb0%\x9d#')  # 0xb0259d23
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.refract_warp_top_down))

        data.write(b'$N\x9em')  # 0x244e9e6d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.flow_color.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe7RH\xe4')  # 0xe75248e4
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.flow_color_warp.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'8^\rC')  # 0x385e0d43
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.flow_gloss1.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd3i\xb6@')  # 0xd369b640
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.flow_gloss2.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'm\xde\xa6m')  # 0x6ddea66d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.flow_refract_warp.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf1N:\x14')  # 0xf14e3a14
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flow_speed))

        data.write(b'3\xee\xcd\xfd')  # 0x33eecdfd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flow_orientation))

        data.write(b'Z\x96!\x8c')  # 0x5a96218c
        data.write(b'\x00\x10')  # size
        self.underwater_fog_color.to_stream(data, game)

        data.write(b'\x13\xb5l"')  # 0x13b56c22
        data.write(b'\x00\x10')  # size
        self.splash_color.to_stream(data, game)

        data.write(b"0'\x04<")  # 0x3027043c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.splash_small))

        data.write(b'A\xc1+\xe2')  # 0x41c12be2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.splash_medium))

        data.write(b'\xd6\xe8"\x00')  # 0xd6e82200
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.splash_big))

        data.write(b'\x94\xa2;\xf9')  # 0x94a23bf9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.visor_runoff))

        data.write(b'C\xa7\x04\xfb')  # 0x43a704fb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.visor_runoff_ball))

        data.write(b'\xbaq\x7f\x19')  # 0xba717f19
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_sound_runoff))

        data.write(b'\xae|~\xfc')  # 0xae7c7efc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_sound_runoff_ball))

        data.write(b'\xee\xf8\x1eL')  # 0xeef81e4c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_splash_small))

        data.write(b'c\xc9gc')  # 0x63c96763
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_splash_medium))

        data.write(b'\xd3b\t\xbc')  # 0xd36209bc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_splash_big))

        data.write(b'\xe5x\xc0\xdd')  # 0xe578c0dd
        data.write(b'\x00\x10')  # size
        self.fog_color.to_stream(data, game)

        data.write(b'\xb4\xb0\xfd\x8d')  # 0xb4b0fd8d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fog_height))

        data.write(b'\xb9\r\xffD')  # 0xb90dff44
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fog_bob_height))

        data.write(b'\xf6\x08\xd3\\')  # 0xf608d35c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fog_bob_freq))

        data.write(b'\xd8R\x1c\x1c')  # 0xd8521c1c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fog_no_grav_suit_dist))

        data.write(b'}\xce]\xc2')  # 0x7dce5dc2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fog_no_grav_suit_factor))

        data.write(b'q\x81\x9b<')  # 0x71819b3c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fog_grav_suit_dist))

        data.write(b'\x9b\x96\xc60')  # 0x9b96c630
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fog_grav_suit_factor))

        data.write(b'\xff\xe2o\\')  # 0xffe26f5c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.viscosity))

        data.write(b'\xb5\xe9\x85\x9f')  # 0xb5e9859f
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.render_surface))

        data.write(b'=\xdc\xa6t')  # 0x3ddca674
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.use_dynamic_lights))

        data.write(b'\x0ey\x17\x82')  # 0xe791782
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.render_tile_scale_x))

        data.write(b"\xc5%\xc4'")  # 0xc525c427
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.render_tile_scale_y))

        data.write(b'4%\xe8?')  # 0x3425e83f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.light_map_resolution))

        data.write(b'"\x93\xfd\xb0')  # 0x2293fdb0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.light_map_scale_x))

        data.write(b'\xe9\xcf.\x15')  # 0xe9cf2e15
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.light_map_scale_y))

        data.write(b'&\x88F\xd6')  # 0x268846d6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.light_map_offset_x))

        data.write(b'\xed\xd4\x95s')  # 0xedd49573
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.light_map_offset_y))

        data.write(b'\xc7\x1c\rc')  # 0xc71c0d63
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown))

        data.write(b'\x82!\x18\xb4')  # 0x822118b4
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.filter_sound_effects))

        data.write(b'ACy\xea')  # 0x414379ea
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.filter_cutoff_frequency))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("WaterJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            trigger=TriggerInfo.from_json(json_data['trigger']),
            alpha_fadein_time=json_data['alpha_fadein_time'],
            alpha_fadeout_time=json_data['alpha_fadeout_time'],
            morph_time_to=json_data['morph_time_to'],
            morph_time_restore=json_data['morph_time_restore'],
            fluid_type=json_data['fluid_type'],
            light_map=json_data['light_map'],
            color_map=json_data['color_map'],
            color_warp_map=json_data['color_warp_map'],
            gloss_map=json_data['gloss_map'],
            env_map=json_data['env_map'],
            env_map_size=json_data['env_map_size'],
            refract_warp_map=json_data['refract_warp_map'],
            foam_map=json_data['foam_map'],
            alpha_map=json_data['alpha_map'],
            base_color=Color.from_json(json_data['base_color']),
            alpha=json_data['alpha'],
            gloss_flat=json_data['gloss_flat'],
            gloss_top_down=json_data['gloss_top_down'],
            refract_warp_flat=json_data['refract_warp_flat'],
            refract_warp_top_down=json_data['refract_warp_top_down'],
            flow_color=LayerInfo.from_json(json_data['flow_color']),
            flow_color_warp=LayerInfo.from_json(json_data['flow_color_warp']),
            flow_gloss1=LayerInfo.from_json(json_data['flow_gloss1']),
            flow_gloss2=LayerInfo.from_json(json_data['flow_gloss2']),
            flow_refract_warp=LayerInfo.from_json(json_data['flow_refract_warp']),
            flow_speed=json_data['flow_speed'],
            flow_orientation=json_data['flow_orientation'],
            underwater_fog_color=Color.from_json(json_data['underwater_fog_color']),
            splash_color=Color.from_json(json_data['splash_color']),
            splash_small=json_data['splash_small'],
            splash_medium=json_data['splash_medium'],
            splash_big=json_data['splash_big'],
            visor_runoff=json_data['visor_runoff'],
            visor_runoff_ball=json_data['visor_runoff_ball'],
            sound_sound_runoff=json_data['sound_sound_runoff'],
            sound_sound_runoff_ball=json_data['sound_sound_runoff_ball'],
            sound_splash_small=json_data['sound_splash_small'],
            sound_splash_medium=json_data['sound_splash_medium'],
            sound_splash_big=json_data['sound_splash_big'],
            fog_color=Color.from_json(json_data['fog_color']),
            fog_height=json_data['fog_height'],
            fog_bob_height=json_data['fog_bob_height'],
            fog_bob_freq=json_data['fog_bob_freq'],
            fog_no_grav_suit_dist=json_data['fog_no_grav_suit_dist'],
            fog_no_grav_suit_factor=json_data['fog_no_grav_suit_factor'],
            fog_grav_suit_dist=json_data['fog_grav_suit_dist'],
            fog_grav_suit_factor=json_data['fog_grav_suit_factor'],
            viscosity=json_data['viscosity'],
            render_surface=json_data['render_surface'],
            use_dynamic_lights=json_data['use_dynamic_lights'],
            render_tile_scale_x=json_data['render_tile_scale_x'],
            render_tile_scale_y=json_data['render_tile_scale_y'],
            light_map_resolution=json_data['light_map_resolution'],
            light_map_scale_x=json_data['light_map_scale_x'],
            light_map_scale_y=json_data['light_map_scale_y'],
            light_map_offset_x=json_data['light_map_offset_x'],
            light_map_offset_y=json_data['light_map_offset_y'],
            unknown=json_data['unknown'],
            filter_sound_effects=json_data['filter_sound_effects'],
            filter_cutoff_frequency=json_data['filter_cutoff_frequency'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'trigger': self.trigger.to_json(),
            'alpha_fadein_time': self.alpha_fadein_time,
            'alpha_fadeout_time': self.alpha_fadeout_time,
            'morph_time_to': self.morph_time_to,
            'morph_time_restore': self.morph_time_restore,
            'fluid_type': self.fluid_type,
            'light_map': self.light_map,
            'color_map': self.color_map,
            'color_warp_map': self.color_warp_map,
            'gloss_map': self.gloss_map,
            'env_map': self.env_map,
            'env_map_size': self.env_map_size,
            'refract_warp_map': self.refract_warp_map,
            'foam_map': self.foam_map,
            'alpha_map': self.alpha_map,
            'base_color': self.base_color.to_json(),
            'alpha': self.alpha,
            'gloss_flat': self.gloss_flat,
            'gloss_top_down': self.gloss_top_down,
            'refract_warp_flat': self.refract_warp_flat,
            'refract_warp_top_down': self.refract_warp_top_down,
            'flow_color': self.flow_color.to_json(),
            'flow_color_warp': self.flow_color_warp.to_json(),
            'flow_gloss1': self.flow_gloss1.to_json(),
            'flow_gloss2': self.flow_gloss2.to_json(),
            'flow_refract_warp': self.flow_refract_warp.to_json(),
            'flow_speed': self.flow_speed,
            'flow_orientation': self.flow_orientation,
            'underwater_fog_color': self.underwater_fog_color.to_json(),
            'splash_color': self.splash_color.to_json(),
            'splash_small': self.splash_small,
            'splash_medium': self.splash_medium,
            'splash_big': self.splash_big,
            'visor_runoff': self.visor_runoff,
            'visor_runoff_ball': self.visor_runoff_ball,
            'sound_sound_runoff': self.sound_sound_runoff,
            'sound_sound_runoff_ball': self.sound_sound_runoff_ball,
            'sound_splash_small': self.sound_splash_small,
            'sound_splash_medium': self.sound_splash_medium,
            'sound_splash_big': self.sound_splash_big,
            'fog_color': self.fog_color.to_json(),
            'fog_height': self.fog_height,
            'fog_bob_height': self.fog_bob_height,
            'fog_bob_freq': self.fog_bob_freq,
            'fog_no_grav_suit_dist': self.fog_no_grav_suit_dist,
            'fog_no_grav_suit_factor': self.fog_no_grav_suit_factor,
            'fog_grav_suit_dist': self.fog_grav_suit_dist,
            'fog_grav_suit_factor': self.fog_grav_suit_factor,
            'viscosity': self.viscosity,
            'render_surface': self.render_surface,
            'use_dynamic_lights': self.use_dynamic_lights,
            'render_tile_scale_x': self.render_tile_scale_x,
            'render_tile_scale_y': self.render_tile_scale_y,
            'light_map_resolution': self.light_map_resolution,
            'light_map_scale_x': self.light_map_scale_x,
            'light_map_scale_y': self.light_map_scale_y,
            'light_map_offset_x': self.light_map_offset_x,
            'light_map_offset_y': self.light_map_offset_y,
            'unknown': self.unknown,
            'filter_sound_effects': self.filter_sound_effects,
            'filter_cutoff_frequency': self.filter_cutoff_frequency,
        }

    def _dependencies_for_light_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.light_map)

    def _dependencies_for_color_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.color_map)

    def _dependencies_for_color_warp_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.color_warp_map)

    def _dependencies_for_gloss_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.gloss_map)

    def _dependencies_for_env_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.env_map)

    def _dependencies_for_refract_warp_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.refract_warp_map)

    def _dependencies_for_foam_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.foam_map)

    def _dependencies_for_alpha_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.alpha_map)

    def _dependencies_for_splash_small(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.splash_small)

    def _dependencies_for_splash_medium(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.splash_medium)

    def _dependencies_for_splash_big(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.splash_big)

    def _dependencies_for_visor_runoff(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.visor_runoff)

    def _dependencies_for_visor_runoff_ball(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.visor_runoff_ball)

    def _dependencies_for_sound_sound_runoff(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_sound_runoff)

    def _dependencies_for_sound_sound_runoff_ball(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_sound_runoff_ball)

    def _dependencies_for_sound_splash_small(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_splash_small)

    def _dependencies_for_sound_splash_medium(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_splash_medium)

    def _dependencies_for_sound_splash_big(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_splash_big)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_light_map, "light_map", "AssetId"),
            (self._dependencies_for_color_map, "color_map", "AssetId"),
            (self._dependencies_for_color_warp_map, "color_warp_map", "AssetId"),
            (self._dependencies_for_gloss_map, "gloss_map", "AssetId"),
            (self._dependencies_for_env_map, "env_map", "AssetId"),
            (self._dependencies_for_refract_warp_map, "refract_warp_map", "AssetId"),
            (self._dependencies_for_foam_map, "foam_map", "AssetId"),
            (self._dependencies_for_alpha_map, "alpha_map", "AssetId"),
            (self._dependencies_for_splash_small, "splash_small", "AssetId"),
            (self._dependencies_for_splash_medium, "splash_medium", "AssetId"),
            (self._dependencies_for_splash_big, "splash_big", "AssetId"),
            (self._dependencies_for_visor_runoff, "visor_runoff", "AssetId"),
            (self._dependencies_for_visor_runoff_ball, "visor_runoff_ball", "AssetId"),
            (self._dependencies_for_sound_sound_runoff, "sound_sound_runoff", "int"),
            (self._dependencies_for_sound_sound_runoff_ball, "sound_sound_runoff_ball", "int"),
            (self._dependencies_for_sound_splash_small, "sound_splash_small", "int"),
            (self._dependencies_for_sound_splash_medium, "sound_splash_medium", "int"),
            (self._dependencies_for_sound_splash_big, "sound_splash_big", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for Water.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})


def _decode_trigger(data: typing.BinaryIO, game: Game, property_size: int) -> TriggerInfo:
    return TriggerInfo.from_stream(data, game, property_size)


def _decode_base_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_flow_color(data: typing.BinaryIO, game: Game, property_size: int) -> LayerInfo:
    return LayerInfo.from_stream(data, game, property_size)


def _decode_flow_color_warp(data: typing.BinaryIO, game: Game, property_size: int) -> LayerInfo:
    return LayerInfo.from_stream(data, game, property_size)


def _decode_flow_gloss1(data: typing.BinaryIO, game: Game, property_size: int) -> LayerInfo:
    return LayerInfo.from_stream(data, game, property_size)


def _decode_flow_gloss2(data: typing.BinaryIO, game: Game, property_size: int) -> LayerInfo:
    return LayerInfo.from_stream(data, game, property_size)


def _decode_flow_refract_warp(data: typing.BinaryIO, game: Game, property_size: int) -> LayerInfo:
    return LayerInfo.from_stream(data, game, property_size)


def _decode_underwater_fog_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_splash_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_fog_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0x77a27411: ('trigger', _decode_trigger),
    0xde5ea267: ('alpha_fadein_time', structs.decode_BIG_f),
    0x22b69324: ('alpha_fadeout_time', structs.decode_BIG_f),
    0x4c60077e: ('morph_time_to', structs.decode_BIG_f),
    0x8518047a: ('morph_time_restore', structs.decode_BIG_f),
    0x7d606b78: ('fluid_type', structs.decode_BIG_L),
    0x2421a2bf: ('light_map', structs.decode_BIG_L),
    0x5e8b37dd: ('color_map', structs.decode_BIG_L),
    0x031d987e: ('color_warp_map', structs.decode_BIG_L),
    0x5aa79c9f: ('gloss_map', structs.decode_BIG_L),
    0x2f0645cf: ('env_map', structs.decode_BIG_L),
    0xde054447: ('env_map_size', structs.decode_BIG_f),
    0x7a4b4685: ('refract_warp_map', structs.decode_BIG_L),
    0x5ba7702e: ('foam_map', structs.decode_BIG_L),
    0x9a3463a7: ('alpha_map', structs.decode_BIG_L),
    0x041398d5: ('base_color', _decode_base_color),
    0x0f7c6fc2: ('alpha', structs.decode_BIG_f),
    0x26382fcb: ('gloss_flat', structs.decode_BIG_f),
    0xc63a0616: ('gloss_top_down', structs.decode_BIG_f),
    0xdb7a3a6b: ('refract_warp_flat', structs.decode_BIG_f),
    0xb0259d23: ('refract_warp_top_down', structs.decode_BIG_f),
    0x244e9e6d: ('flow_color', _decode_flow_color),
    0xe75248e4: ('flow_color_warp', _decode_flow_color_warp),
    0x385e0d43: ('flow_gloss1', _decode_flow_gloss1),
    0xd369b640: ('flow_gloss2', _decode_flow_gloss2),
    0x6ddea66d: ('flow_refract_warp', _decode_flow_refract_warp),
    0xf14e3a14: ('flow_speed', structs.decode_BIG_f),
    0x33eecdfd: ('flow_orientation', structs.decode_BIG_f),
    0x5a96218c: ('underwater_fog_color', _decode_underwater_fog_color),
    0x13b56c22: ('splash_color', _decode_splash_color),
    0x3027043c: ('splash_small', structs.decode_BIG_L),
    0x41c12be2: ('splash_medium', structs.decode_BIG_L),
    0xd6e82200: ('splash_big', structs.decode_BIG_L),
    0x94a23bf9: ('visor_runoff', structs.decode_BIG_L),
    0x43a704fb: ('visor_runoff_ball', structs.decode_BIG_L),
    0xba717f19: ('sound_sound_runoff', structs.decode_BIG_l),
    0xae7c7efc: ('sound_sound_runoff_ball', structs.decode_BIG_l),
    0xeef81e4c: ('sound_splash_small', structs.decode_BIG_l),
    0x63c96763: ('sound_splash_medium', structs.decode_BIG_l),
    0xd36209bc: ('sound_splash_big', structs.decode_BIG_l),
    0xe578c0dd: ('fog_color', _decode_fog_color),
    0xb4b0fd8d: ('fog_height', structs.decode_BIG_f),
    0xb90dff44: ('fog_bob_height', structs.decode_BIG_f),
    0xf608d35c: ('fog_bob_freq', structs.decode_BIG_f),
    0xd8521c1c: ('fog_no_grav_suit_dist', structs.decode_BIG_f),
    0x7dce5dc2: ('fog_no_grav_suit_factor', structs.decode_BIG_f),
    0x71819b3c: ('fog_grav_suit_dist', structs.decode_BIG_f),
    0x9b96c630: ('fog_grav_suit_factor', structs.decode_BIG_f),
    0xffe26f5c: ('viscosity', structs.decode_BIG_f),
    0xb5e9859f: ('render_surface', structs.decode_BIG_bool_),
    0x3ddca674: ('use_dynamic_lights', structs.decode_BIG_bool_),
    0x0e791782: ('render_tile_scale_x', structs.decode_BIG_f),
    0xc525c427: ('render_tile_scale_y', structs.decode_BIG_f),
    0x3425e83f: ('light_map_resolution', structs.decode_BIG_f),
    0x2293fdb0: ('light_map_scale_x', structs.decode_BIG_f),
    0xe9cf2e15: ('light_map_scale_y', structs.decode_BIG_f),
    0x268846d6: ('light_map_offset_x', structs.decode_BIG_f),
    0xedd49573: ('light_map_offset_y', structs.decode_BIG_f),
    0xc71c0d63: ('unknown', structs.decode_BIG_bool_),
    0x822118b4: ('filter_sound_effects', structs.decode_BIG_bool_),
    0x414379ea: ('filter_cutoff_frequency', structs.decode_BIG_l),
}
