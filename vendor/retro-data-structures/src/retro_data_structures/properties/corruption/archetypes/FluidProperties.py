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
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.corruption.archetypes.LayerInfo import LayerInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class FluidPropertiesJson(typing_extensions.TypedDict):
        fluid_type: int
        is_morph_target: bool
        render_surface: bool
        render_under_surface: bool
        use_dynamic_lights: bool
        use_fluid_dynamics: bool
        surface_displacement_scale: float
        grid_spacing: float
        morph_time_to: float
        morph_time_restore: float
        bloom: int
        base_color: json_util.JsonValue
        underwater_fog_color: json_util.JsonValue
        color_map: int
        color_warp_map: int
        gloss_map: int
        env_map: int
        light_map: int
        refract_warp_map: int
        color_warp_scalar: float
        refract_warp_scalar: float
        light_map_resolution: float
        flow_speed: float
        flow_orientation: float
        flow_color: json_util.JsonObject
        flow_color_warp: json_util.JsonObject
        flow_gloss1: json_util.JsonObject
        flow_gloss2: json_util.JsonObject
        flow_refract_warp: json_util.JsonObject
        splash_color: json_util.JsonValue
        splash_effect_tiny: int
        splash_effect_small: int
        splash_effect_medium: int
        splash_effect_big: int
        splash_sound_tiny: int
        splash_sound_small: int
        splash_sound_medium: int
        splash_sound_big: int
        caud_0x0efcdea0: int
        caud_0x78df0e7f: int
        min_splash_kinetic_energy: float
        max_splash_kinetic_energy: float
        rolling_splash_effect: int
        runoff_visor_effect: int
        runoff_ball_effect: int
        slow_exit_sound: int
        fast_exit_sound: int
        fast_exit_speed: float
        unknown_0x687df7a3: float
        unknown_0xe73aad13: float
        unknown_0xac67b7d7: float
        fog_color: json_util.JsonValue
        fog_height: float
        fog_bob_height: float
        fog_bob_freq: float
        unknown_0xfe3bc8f7: bool
        freeze_radius: float
        player_freeze_radius: float
        roll_fully_submerged_sound: int
        roll_partially_submerged_sound: int
        vertical_sound: int
        damage_sound: int
        damage_effect: int
        footstep_sound: int
        filter_sound_effects: bool
        volume_attenuation: float
        filter_cutoff_frequency: int
        fluid_lock_string: str
    

class FluidType(enum.IntEnum):
    kFluidType_Water = 1425213472
    kFluidType_SwampWater = 230544723
    kFluidType_FireGel = 1204522302

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


class Bloom(enum.IntEnum):
    kBloom_NoWrite = 1222417634
    kBloom_WriteAlpha = 759120936
    kBloom_Fixed0Pct = 413038581
    kBloom_Fixed25Pct = 3476137679
    kBloom_Fixed50Pct = 1255115501
    kBloom_Fixed75Pct = 131148223
    kBloom_Fixed100Pct = 176197152

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
class FluidProperties(BaseProperty):
    fluid_type: FluidType = dataclasses.field(default=FluidType.kFluidType_Water, metadata={
        'reflection': FieldReflection[FluidType](
            FluidType, id=0xbe253b54, original_name='FluidType', from_json=FluidType.from_json, to_json=FluidType.to_json
        ),
    })
    is_morph_target: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x7f2a8353, original_name='IsMorphTarget'
        ),
    })
    render_surface: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xb5e9859f, original_name='RenderSurface'
        ),
    })
    render_under_surface: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x1f5e78c2, original_name='RenderUnderSurface'
        ),
    })
    use_dynamic_lights: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x3ddca674, original_name='UseDynamicLights'
        ),
    })
    use_fluid_dynamics: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x4817eaa7, original_name='UseFluidDynamics'
        ),
    })
    surface_displacement_scale: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0x13013139, original_name='SurfaceDisplacementScale'
        ),
    })
    grid_spacing: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x628f03db, original_name='GridSpacing'
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
    bloom: Bloom = dataclasses.field(default=Bloom.kBloom_NoWrite, metadata={
        'reflection': FieldReflection[Bloom](
            Bloom, id=0xa4d23616, original_name='Bloom', from_json=Bloom.from_json, to_json=Bloom.to_json
        ),
    })
    base_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.0, b=0.49803900718688965, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x041398d5, original_name='BaseColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    underwater_fog_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.0, g=0.49803900718688965, b=1.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x5a96218c, original_name='UnderwaterFogColor', from_json=Color.from_json, to_json=Color.to_json
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
    light_map: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['TXTR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2421a2bf, original_name='LightMap'
        ),
    })
    refract_warp_map: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['TXTR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x7a4b4685, original_name='RefractWarpMap'
        ),
    })
    color_warp_scalar: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdd2f6dbd, original_name='ColorWarpScalar'
        ),
    })
    refract_warp_scalar: float = dataclasses.field(default=0.05000000074505806, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf90deda5, original_name='RefractWarpScalar'
        ),
    })
    light_map_resolution: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3425e83f, original_name='LightMapResolution'
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
    splash_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x13b56c22, original_name='SplashColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    splash_effect_tiny: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3da16854, original_name='SplashEffectTiny'
        ),
    })
    splash_effect_small: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x856941fe, original_name='SplashEffectSmall'
        ),
    })
    splash_effect_medium: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x341ec63b, original_name='SplashEffectMedium'
        ),
    })
    splash_effect_big: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x388e3c07, original_name='SplashEffectBig'
        ),
    })
    splash_sound_tiny: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x418643c2, original_name='SplashSoundTiny'
        ),
    })
    splash_sound_small: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x9c7950a4, original_name='SplashSoundSmall'
        ),
    })
    splash_sound_medium: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xbfb96ec0, original_name='SplashSoundMedium'
        ),
    })
    splash_sound_big: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc34a1dc9, original_name='SplashSoundBig'
        ),
    })
    caud_0x0efcdea0: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x0efcdea0, original_name='CAUD'
        ),
    })
    caud_0x78df0e7f: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x78df0e7f, original_name='CAUD'
        ),
    })
    min_splash_kinetic_energy: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x84e241ed, original_name='MinSplashKineticEnergy'
        ),
    })
    max_splash_kinetic_energy: float = dataclasses.field(default=45000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe2072799, original_name='MaxSplashKineticEnergy'
        ),
    })
    rolling_splash_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xab463f9a, original_name='RollingSplashEffect'
        ),
    })
    runoff_visor_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x66d466b5, original_name='RunoffVisorEffect'
        ),
    })
    runoff_ball_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb97ccede, original_name='RunoffBallEffect'
        ),
    })
    slow_exit_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x4d82bb1e, original_name='SlowExitSound'
        ),
    })
    fast_exit_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc51da2dc, original_name='FastExitSound'
        ),
    })
    fast_exit_speed: float = dataclasses.field(default=7.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x03d24e64, original_name='FastExitSpeed'
        ),
    })
    unknown_0x687df7a3: float = dataclasses.field(default=-0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x687df7a3, original_name='Unknown'
        ),
    })
    unknown_0xe73aad13: float = dataclasses.field(default=-1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe73aad13, original_name='Unknown'
        ),
    })
    unknown_0xac67b7d7: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xac67b7d7, original_name='Unknown'
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
    unknown_0xfe3bc8f7: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xfe3bc8f7, original_name='Unknown'
        ),
    })
    freeze_radius: float = dataclasses.field(default=6.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x318418aa, original_name='FreezeRadius'
        ),
    })
    player_freeze_radius: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7b77e31d, original_name='PlayerFreezeRadius'
        ),
    })
    roll_fully_submerged_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x84927794, original_name='RollFullySubmergedSound'
        ),
    })
    roll_partially_submerged_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa6e650a0, original_name='RollPartiallySubmergedSound'
        ),
    })
    vertical_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x90b8eb66, original_name='VerticalSound'
        ),
    })
    damage_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3eede8f7, original_name='DamageSound'
        ),
    })
    damage_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc110ed44, original_name='DamageEffect'
        ),
    })
    footstep_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb9413fe6, original_name='FootstepSound'
        ),
    })
    filter_sound_effects: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x822118b4, original_name='FilterSoundEffects'
        ),
    })
    volume_attenuation: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfe89b6e4, original_name='VolumeAttenuation'
        ),
    })
    filter_cutoff_frequency: int = dataclasses.field(default=300, metadata={
        'reflection': FieldReflection[int](
            int, id=0x414379ea, original_name='FilterCutoffFrequency'
        ),
    })
    fluid_lock_string: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x3c764739, original_name='FluidLockString'
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
        if property_count != 68:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbe253b54
        fluid_type = FluidType.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7f2a8353
        is_morph_target = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb5e9859f
        render_surface = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1f5e78c2
        render_under_surface = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3ddca674
        use_dynamic_lights = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4817eaa7
        use_fluid_dynamics = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13013139
        surface_displacement_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x628f03db
        grid_spacing = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4c60077e
        morph_time_to = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8518047a
        morph_time_restore = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa4d23616
        bloom = Bloom.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x041398d5
        base_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5a96218c
        underwater_fog_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5e8b37dd
        color_map = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x031d987e
        color_warp_map = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5aa79c9f
        gloss_map = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2f0645cf
        env_map = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2421a2bf
        light_map = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7a4b4685
        refract_warp_map = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdd2f6dbd
        color_warp_scalar = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf90deda5
        refract_warp_scalar = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3425e83f
        light_map_resolution = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf14e3a14
        flow_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33eecdfd
        flow_orientation = structs.BIG_f.unpack(data.read(4))[0]
    
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
        assert property_id == 0x13b56c22
        splash_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3da16854
        splash_effect_tiny = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x856941fe
        splash_effect_small = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x341ec63b
        splash_effect_medium = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x388e3c07
        splash_effect_big = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x418643c2
        splash_sound_tiny = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9c7950a4
        splash_sound_small = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbfb96ec0
        splash_sound_medium = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc34a1dc9
        splash_sound_big = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0efcdea0
        caud_0x0efcdea0 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78df0e7f
        caud_0x78df0e7f = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x84e241ed
        min_splash_kinetic_energy = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe2072799
        max_splash_kinetic_energy = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xab463f9a
        rolling_splash_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x66d466b5
        runoff_visor_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb97ccede
        runoff_ball_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4d82bb1e
        slow_exit_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc51da2dc
        fast_exit_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03d24e64
        fast_exit_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x687df7a3
        unknown_0x687df7a3 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe73aad13
        unknown_0xe73aad13 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xac67b7d7
        unknown_0xac67b7d7 = structs.BIG_f.unpack(data.read(4))[0]
    
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
        assert property_id == 0xfe3bc8f7
        unknown_0xfe3bc8f7 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x318418aa
        freeze_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7b77e31d
        player_freeze_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x84927794
        roll_fully_submerged_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa6e650a0
        roll_partially_submerged_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x90b8eb66
        vertical_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3eede8f7
        damage_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc110ed44
        damage_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb9413fe6
        footstep_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x822118b4
        filter_sound_effects = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfe89b6e4
        volume_attenuation = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x414379ea
        filter_cutoff_frequency = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3c764739
        fluid_lock_string = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        return cls(fluid_type, is_morph_target, render_surface, render_under_surface, use_dynamic_lights, use_fluid_dynamics, surface_displacement_scale, grid_spacing, morph_time_to, morph_time_restore, bloom, base_color, underwater_fog_color, color_map, color_warp_map, gloss_map, env_map, light_map, refract_warp_map, color_warp_scalar, refract_warp_scalar, light_map_resolution, flow_speed, flow_orientation, flow_color, flow_color_warp, flow_gloss1, flow_gloss2, flow_refract_warp, splash_color, splash_effect_tiny, splash_effect_small, splash_effect_medium, splash_effect_big, splash_sound_tiny, splash_sound_small, splash_sound_medium, splash_sound_big, caud_0x0efcdea0, caud_0x78df0e7f, min_splash_kinetic_energy, max_splash_kinetic_energy, rolling_splash_effect, runoff_visor_effect, runoff_ball_effect, slow_exit_sound, fast_exit_sound, fast_exit_speed, unknown_0x687df7a3, unknown_0xe73aad13, unknown_0xac67b7d7, fog_color, fog_height, fog_bob_height, fog_bob_freq, unknown_0xfe3bc8f7, freeze_radius, player_freeze_radius, roll_fully_submerged_sound, roll_partially_submerged_sound, vertical_sound, damage_sound, damage_effect, footstep_sound, filter_sound_effects, volume_attenuation, filter_cutoff_frequency, fluid_lock_string)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00D')  # 68 properties

        data.write(b'\xbe%;T')  # 0xbe253b54
        data.write(b'\x00\x04')  # size
        self.fluid_type.to_stream(data, game)

        data.write(b'\x7f*\x83S')  # 0x7f2a8353
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_morph_target))

        data.write(b'\xb5\xe9\x85\x9f')  # 0xb5e9859f
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.render_surface))

        data.write(b'\x1f^x\xc2')  # 0x1f5e78c2
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.render_under_surface))

        data.write(b'=\xdc\xa6t')  # 0x3ddca674
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.use_dynamic_lights))

        data.write(b'H\x17\xea\xa7')  # 0x4817eaa7
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.use_fluid_dynamics))

        data.write(b'\x13\x0119')  # 0x13013139
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.surface_displacement_scale))

        data.write(b'b\x8f\x03\xdb')  # 0x628f03db
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grid_spacing))

        data.write(b'L`\x07~')  # 0x4c60077e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.morph_time_to))

        data.write(b'\x85\x18\x04z')  # 0x8518047a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.morph_time_restore))

        data.write(b'\xa4\xd26\x16')  # 0xa4d23616
        data.write(b'\x00\x04')  # size
        self.bloom.to_stream(data, game)

        data.write(b'\x04\x13\x98\xd5')  # 0x41398d5
        data.write(b'\x00\x10')  # size
        self.base_color.to_stream(data, game)

        data.write(b'Z\x96!\x8c')  # 0x5a96218c
        data.write(b'\x00\x10')  # size
        self.underwater_fog_color.to_stream(data, game)

        data.write(b'^\x8b7\xdd')  # 0x5e8b37dd
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.color_map))

        data.write(b'\x03\x1d\x98~')  # 0x31d987e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.color_warp_map))

        data.write(b'Z\xa7\x9c\x9f')  # 0x5aa79c9f
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.gloss_map))

        data.write(b'/\x06E\xcf')  # 0x2f0645cf
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.env_map))

        data.write(b'$!\xa2\xbf')  # 0x2421a2bf
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.light_map))

        data.write(b'zKF\x85')  # 0x7a4b4685
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.refract_warp_map))

        data.write(b'\xdd/m\xbd')  # 0xdd2f6dbd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.color_warp_scalar))

        data.write(b'\xf9\r\xed\xa5')  # 0xf90deda5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.refract_warp_scalar))

        data.write(b'4%\xe8?')  # 0x3425e83f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.light_map_resolution))

        data.write(b'\xf1N:\x14')  # 0xf14e3a14
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flow_speed))

        data.write(b'3\xee\xcd\xfd')  # 0x33eecdfd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flow_orientation))

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

        data.write(b'\x13\xb5l"')  # 0x13b56c22
        data.write(b'\x00\x10')  # size
        self.splash_color.to_stream(data, game)

        data.write(b'=\xa1hT')  # 0x3da16854
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.splash_effect_tiny))

        data.write(b'\x85iA\xfe')  # 0x856941fe
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.splash_effect_small))

        data.write(b'4\x1e\xc6;')  # 0x341ec63b
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.splash_effect_medium))

        data.write(b'8\x8e<\x07')  # 0x388e3c07
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.splash_effect_big))

        data.write(b'A\x86C\xc2')  # 0x418643c2
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.splash_sound_tiny))

        data.write(b'\x9cyP\xa4')  # 0x9c7950a4
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.splash_sound_small))

        data.write(b'\xbf\xb9n\xc0')  # 0xbfb96ec0
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.splash_sound_medium))

        data.write(b'\xc3J\x1d\xc9')  # 0xc34a1dc9
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.splash_sound_big))

        data.write(b'\x0e\xfc\xde\xa0')  # 0xefcdea0
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.caud_0x0efcdea0))

        data.write(b'x\xdf\x0e\x7f')  # 0x78df0e7f
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.caud_0x78df0e7f))

        data.write(b'\x84\xe2A\xed')  # 0x84e241ed
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_splash_kinetic_energy))

        data.write(b"\xe2\x07'\x99")  # 0xe2072799
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_splash_kinetic_energy))

        data.write(b'\xabF?\x9a')  # 0xab463f9a
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.rolling_splash_effect))

        data.write(b'f\xd4f\xb5')  # 0x66d466b5
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.runoff_visor_effect))

        data.write(b'\xb9|\xce\xde')  # 0xb97ccede
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.runoff_ball_effect))

        data.write(b'M\x82\xbb\x1e')  # 0x4d82bb1e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.slow_exit_sound))

        data.write(b'\xc5\x1d\xa2\xdc')  # 0xc51da2dc
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.fast_exit_sound))

        data.write(b'\x03\xd2Nd')  # 0x3d24e64
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fast_exit_speed))

        data.write(b'h}\xf7\xa3')  # 0x687df7a3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x687df7a3))

        data.write(b'\xe7:\xad\x13')  # 0xe73aad13
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe73aad13))

        data.write(b'\xacg\xb7\xd7')  # 0xac67b7d7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xac67b7d7))

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

        data.write(b'\xfe;\xc8\xf7')  # 0xfe3bc8f7
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xfe3bc8f7))

        data.write(b'1\x84\x18\xaa')  # 0x318418aa
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.freeze_radius))

        data.write(b'{w\xe3\x1d')  # 0x7b77e31d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.player_freeze_radius))

        data.write(b'\x84\x92w\x94')  # 0x84927794
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.roll_fully_submerged_sound))

        data.write(b'\xa6\xe6P\xa0')  # 0xa6e650a0
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.roll_partially_submerged_sound))

        data.write(b'\x90\xb8\xebf')  # 0x90b8eb66
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.vertical_sound))

        data.write(b'>\xed\xe8\xf7')  # 0x3eede8f7
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.damage_sound))

        data.write(b'\xc1\x10\xedD')  # 0xc110ed44
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.damage_effect))

        data.write(b'\xb9A?\xe6')  # 0xb9413fe6
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.footstep_sound))

        data.write(b'\x82!\x18\xb4')  # 0x822118b4
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.filter_sound_effects))

        data.write(b'\xfe\x89\xb6\xe4')  # 0xfe89b6e4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.volume_attenuation))

        data.write(b'ACy\xea')  # 0x414379ea
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.filter_cutoff_frequency))

        data.write(b'<vG9')  # 0x3c764739
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.fluid_lock_string.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FluidPropertiesJson", data)
        return cls(
            fluid_type=FluidType.from_json(json_data['fluid_type']),
            is_morph_target=json_data['is_morph_target'],
            render_surface=json_data['render_surface'],
            render_under_surface=json_data['render_under_surface'],
            use_dynamic_lights=json_data['use_dynamic_lights'],
            use_fluid_dynamics=json_data['use_fluid_dynamics'],
            surface_displacement_scale=json_data['surface_displacement_scale'],
            grid_spacing=json_data['grid_spacing'],
            morph_time_to=json_data['morph_time_to'],
            morph_time_restore=json_data['morph_time_restore'],
            bloom=Bloom.from_json(json_data['bloom']),
            base_color=Color.from_json(json_data['base_color']),
            underwater_fog_color=Color.from_json(json_data['underwater_fog_color']),
            color_map=json_data['color_map'],
            color_warp_map=json_data['color_warp_map'],
            gloss_map=json_data['gloss_map'],
            env_map=json_data['env_map'],
            light_map=json_data['light_map'],
            refract_warp_map=json_data['refract_warp_map'],
            color_warp_scalar=json_data['color_warp_scalar'],
            refract_warp_scalar=json_data['refract_warp_scalar'],
            light_map_resolution=json_data['light_map_resolution'],
            flow_speed=json_data['flow_speed'],
            flow_orientation=json_data['flow_orientation'],
            flow_color=LayerInfo.from_json(json_data['flow_color']),
            flow_color_warp=LayerInfo.from_json(json_data['flow_color_warp']),
            flow_gloss1=LayerInfo.from_json(json_data['flow_gloss1']),
            flow_gloss2=LayerInfo.from_json(json_data['flow_gloss2']),
            flow_refract_warp=LayerInfo.from_json(json_data['flow_refract_warp']),
            splash_color=Color.from_json(json_data['splash_color']),
            splash_effect_tiny=json_data['splash_effect_tiny'],
            splash_effect_small=json_data['splash_effect_small'],
            splash_effect_medium=json_data['splash_effect_medium'],
            splash_effect_big=json_data['splash_effect_big'],
            splash_sound_tiny=json_data['splash_sound_tiny'],
            splash_sound_small=json_data['splash_sound_small'],
            splash_sound_medium=json_data['splash_sound_medium'],
            splash_sound_big=json_data['splash_sound_big'],
            caud_0x0efcdea0=json_data['caud_0x0efcdea0'],
            caud_0x78df0e7f=json_data['caud_0x78df0e7f'],
            min_splash_kinetic_energy=json_data['min_splash_kinetic_energy'],
            max_splash_kinetic_energy=json_data['max_splash_kinetic_energy'],
            rolling_splash_effect=json_data['rolling_splash_effect'],
            runoff_visor_effect=json_data['runoff_visor_effect'],
            runoff_ball_effect=json_data['runoff_ball_effect'],
            slow_exit_sound=json_data['slow_exit_sound'],
            fast_exit_sound=json_data['fast_exit_sound'],
            fast_exit_speed=json_data['fast_exit_speed'],
            unknown_0x687df7a3=json_data['unknown_0x687df7a3'],
            unknown_0xe73aad13=json_data['unknown_0xe73aad13'],
            unknown_0xac67b7d7=json_data['unknown_0xac67b7d7'],
            fog_color=Color.from_json(json_data['fog_color']),
            fog_height=json_data['fog_height'],
            fog_bob_height=json_data['fog_bob_height'],
            fog_bob_freq=json_data['fog_bob_freq'],
            unknown_0xfe3bc8f7=json_data['unknown_0xfe3bc8f7'],
            freeze_radius=json_data['freeze_radius'],
            player_freeze_radius=json_data['player_freeze_radius'],
            roll_fully_submerged_sound=json_data['roll_fully_submerged_sound'],
            roll_partially_submerged_sound=json_data['roll_partially_submerged_sound'],
            vertical_sound=json_data['vertical_sound'],
            damage_sound=json_data['damage_sound'],
            damage_effect=json_data['damage_effect'],
            footstep_sound=json_data['footstep_sound'],
            filter_sound_effects=json_data['filter_sound_effects'],
            volume_attenuation=json_data['volume_attenuation'],
            filter_cutoff_frequency=json_data['filter_cutoff_frequency'],
            fluid_lock_string=json_data['fluid_lock_string'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'fluid_type': self.fluid_type.to_json(),
            'is_morph_target': self.is_morph_target,
            'render_surface': self.render_surface,
            'render_under_surface': self.render_under_surface,
            'use_dynamic_lights': self.use_dynamic_lights,
            'use_fluid_dynamics': self.use_fluid_dynamics,
            'surface_displacement_scale': self.surface_displacement_scale,
            'grid_spacing': self.grid_spacing,
            'morph_time_to': self.morph_time_to,
            'morph_time_restore': self.morph_time_restore,
            'bloom': self.bloom.to_json(),
            'base_color': self.base_color.to_json(),
            'underwater_fog_color': self.underwater_fog_color.to_json(),
            'color_map': self.color_map,
            'color_warp_map': self.color_warp_map,
            'gloss_map': self.gloss_map,
            'env_map': self.env_map,
            'light_map': self.light_map,
            'refract_warp_map': self.refract_warp_map,
            'color_warp_scalar': self.color_warp_scalar,
            'refract_warp_scalar': self.refract_warp_scalar,
            'light_map_resolution': self.light_map_resolution,
            'flow_speed': self.flow_speed,
            'flow_orientation': self.flow_orientation,
            'flow_color': self.flow_color.to_json(),
            'flow_color_warp': self.flow_color_warp.to_json(),
            'flow_gloss1': self.flow_gloss1.to_json(),
            'flow_gloss2': self.flow_gloss2.to_json(),
            'flow_refract_warp': self.flow_refract_warp.to_json(),
            'splash_color': self.splash_color.to_json(),
            'splash_effect_tiny': self.splash_effect_tiny,
            'splash_effect_small': self.splash_effect_small,
            'splash_effect_medium': self.splash_effect_medium,
            'splash_effect_big': self.splash_effect_big,
            'splash_sound_tiny': self.splash_sound_tiny,
            'splash_sound_small': self.splash_sound_small,
            'splash_sound_medium': self.splash_sound_medium,
            'splash_sound_big': self.splash_sound_big,
            'caud_0x0efcdea0': self.caud_0x0efcdea0,
            'caud_0x78df0e7f': self.caud_0x78df0e7f,
            'min_splash_kinetic_energy': self.min_splash_kinetic_energy,
            'max_splash_kinetic_energy': self.max_splash_kinetic_energy,
            'rolling_splash_effect': self.rolling_splash_effect,
            'runoff_visor_effect': self.runoff_visor_effect,
            'runoff_ball_effect': self.runoff_ball_effect,
            'slow_exit_sound': self.slow_exit_sound,
            'fast_exit_sound': self.fast_exit_sound,
            'fast_exit_speed': self.fast_exit_speed,
            'unknown_0x687df7a3': self.unknown_0x687df7a3,
            'unknown_0xe73aad13': self.unknown_0xe73aad13,
            'unknown_0xac67b7d7': self.unknown_0xac67b7d7,
            'fog_color': self.fog_color.to_json(),
            'fog_height': self.fog_height,
            'fog_bob_height': self.fog_bob_height,
            'fog_bob_freq': self.fog_bob_freq,
            'unknown_0xfe3bc8f7': self.unknown_0xfe3bc8f7,
            'freeze_radius': self.freeze_radius,
            'player_freeze_radius': self.player_freeze_radius,
            'roll_fully_submerged_sound': self.roll_fully_submerged_sound,
            'roll_partially_submerged_sound': self.roll_partially_submerged_sound,
            'vertical_sound': self.vertical_sound,
            'damage_sound': self.damage_sound,
            'damage_effect': self.damage_effect,
            'footstep_sound': self.footstep_sound,
            'filter_sound_effects': self.filter_sound_effects,
            'volume_attenuation': self.volume_attenuation,
            'filter_cutoff_frequency': self.filter_cutoff_frequency,
            'fluid_lock_string': self.fluid_lock_string,
        }

    def _dependencies_for_color_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.color_map)

    def _dependencies_for_color_warp_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.color_warp_map)

    def _dependencies_for_gloss_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.gloss_map)

    def _dependencies_for_env_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.env_map)

    def _dependencies_for_light_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.light_map)

    def _dependencies_for_refract_warp_map(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.refract_warp_map)

    def _dependencies_for_splash_effect_tiny(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.splash_effect_tiny)

    def _dependencies_for_splash_effect_small(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.splash_effect_small)

    def _dependencies_for_splash_effect_medium(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.splash_effect_medium)

    def _dependencies_for_splash_effect_big(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.splash_effect_big)

    def _dependencies_for_splash_sound_tiny(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.splash_sound_tiny)

    def _dependencies_for_splash_sound_small(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.splash_sound_small)

    def _dependencies_for_splash_sound_medium(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.splash_sound_medium)

    def _dependencies_for_splash_sound_big(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.splash_sound_big)

    def _dependencies_for_caud_0x0efcdea0(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.caud_0x0efcdea0)

    def _dependencies_for_caud_0x78df0e7f(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.caud_0x78df0e7f)

    def _dependencies_for_rolling_splash_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.rolling_splash_effect)

    def _dependencies_for_runoff_visor_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.runoff_visor_effect)

    def _dependencies_for_runoff_ball_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.runoff_ball_effect)

    def _dependencies_for_slow_exit_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.slow_exit_sound)

    def _dependencies_for_fast_exit_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.fast_exit_sound)

    def _dependencies_for_roll_fully_submerged_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.roll_fully_submerged_sound)

    def _dependencies_for_roll_partially_submerged_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.roll_partially_submerged_sound)

    def _dependencies_for_vertical_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.vertical_sound)

    def _dependencies_for_damage_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.damage_sound)

    def _dependencies_for_damage_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.damage_effect)

    def _dependencies_for_footstep_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.footstep_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_color_map, "color_map", "AssetId"),
            (self._dependencies_for_color_warp_map, "color_warp_map", "AssetId"),
            (self._dependencies_for_gloss_map, "gloss_map", "AssetId"),
            (self._dependencies_for_env_map, "env_map", "AssetId"),
            (self._dependencies_for_light_map, "light_map", "AssetId"),
            (self._dependencies_for_refract_warp_map, "refract_warp_map", "AssetId"),
            (self._dependencies_for_splash_effect_tiny, "splash_effect_tiny", "AssetId"),
            (self._dependencies_for_splash_effect_small, "splash_effect_small", "AssetId"),
            (self._dependencies_for_splash_effect_medium, "splash_effect_medium", "AssetId"),
            (self._dependencies_for_splash_effect_big, "splash_effect_big", "AssetId"),
            (self._dependencies_for_splash_sound_tiny, "splash_sound_tiny", "AssetId"),
            (self._dependencies_for_splash_sound_small, "splash_sound_small", "AssetId"),
            (self._dependencies_for_splash_sound_medium, "splash_sound_medium", "AssetId"),
            (self._dependencies_for_splash_sound_big, "splash_sound_big", "AssetId"),
            (self._dependencies_for_caud_0x0efcdea0, "caud_0x0efcdea0", "AssetId"),
            (self._dependencies_for_caud_0x78df0e7f, "caud_0x78df0e7f", "AssetId"),
            (self._dependencies_for_rolling_splash_effect, "rolling_splash_effect", "AssetId"),
            (self._dependencies_for_runoff_visor_effect, "runoff_visor_effect", "AssetId"),
            (self._dependencies_for_runoff_ball_effect, "runoff_ball_effect", "AssetId"),
            (self._dependencies_for_slow_exit_sound, "slow_exit_sound", "AssetId"),
            (self._dependencies_for_fast_exit_sound, "fast_exit_sound", "AssetId"),
            (self._dependencies_for_roll_fully_submerged_sound, "roll_fully_submerged_sound", "AssetId"),
            (self._dependencies_for_roll_partially_submerged_sound, "roll_partially_submerged_sound", "AssetId"),
            (self._dependencies_for_vertical_sound, "vertical_sound", "AssetId"),
            (self._dependencies_for_damage_sound, "damage_sound", "AssetId"),
            (self._dependencies_for_damage_effect, "damage_effect", "AssetId"),
            (self._dependencies_for_footstep_sound, "footstep_sound", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for FluidProperties.{field_name} ({field_type}): {e}"
                )


def _decode_fluid_type(data: typing.BinaryIO, game: Game, property_size: int) -> FluidType:
    return FluidType.from_stream(data, game)


def _decode_bloom(data: typing.BinaryIO, game: Game, property_size: int) -> Bloom:
    return Bloom.from_stream(data, game)


def _decode_base_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_underwater_fog_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
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


def _decode_splash_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_fog_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_fluid_lock_string(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xbe253b54: ('fluid_type', _decode_fluid_type),
    0x7f2a8353: ('is_morph_target', structs.decode_BIG_bool_),
    0xb5e9859f: ('render_surface', structs.decode_BIG_bool_),
    0x1f5e78c2: ('render_under_surface', structs.decode_BIG_bool_),
    0x3ddca674: ('use_dynamic_lights', structs.decode_BIG_bool_),
    0x4817eaa7: ('use_fluid_dynamics', structs.decode_BIG_bool_),
    0x13013139: ('surface_displacement_scale', structs.decode_BIG_f),
    0x628f03db: ('grid_spacing', structs.decode_BIG_f),
    0x4c60077e: ('morph_time_to', structs.decode_BIG_f),
    0x8518047a: ('morph_time_restore', structs.decode_BIG_f),
    0xa4d23616: ('bloom', _decode_bloom),
    0x041398d5: ('base_color', _decode_base_color),
    0x5a96218c: ('underwater_fog_color', _decode_underwater_fog_color),
    0x5e8b37dd: ('color_map', structs.decode_BIG_Q),
    0x031d987e: ('color_warp_map', structs.decode_BIG_Q),
    0x5aa79c9f: ('gloss_map', structs.decode_BIG_Q),
    0x2f0645cf: ('env_map', structs.decode_BIG_Q),
    0x2421a2bf: ('light_map', structs.decode_BIG_Q),
    0x7a4b4685: ('refract_warp_map', structs.decode_BIG_Q),
    0xdd2f6dbd: ('color_warp_scalar', structs.decode_BIG_f),
    0xf90deda5: ('refract_warp_scalar', structs.decode_BIG_f),
    0x3425e83f: ('light_map_resolution', structs.decode_BIG_f),
    0xf14e3a14: ('flow_speed', structs.decode_BIG_f),
    0x33eecdfd: ('flow_orientation', structs.decode_BIG_f),
    0x244e9e6d: ('flow_color', _decode_flow_color),
    0xe75248e4: ('flow_color_warp', _decode_flow_color_warp),
    0x385e0d43: ('flow_gloss1', _decode_flow_gloss1),
    0xd369b640: ('flow_gloss2', _decode_flow_gloss2),
    0x6ddea66d: ('flow_refract_warp', _decode_flow_refract_warp),
    0x13b56c22: ('splash_color', _decode_splash_color),
    0x3da16854: ('splash_effect_tiny', structs.decode_BIG_Q),
    0x856941fe: ('splash_effect_small', structs.decode_BIG_Q),
    0x341ec63b: ('splash_effect_medium', structs.decode_BIG_Q),
    0x388e3c07: ('splash_effect_big', structs.decode_BIG_Q),
    0x418643c2: ('splash_sound_tiny', structs.decode_BIG_Q),
    0x9c7950a4: ('splash_sound_small', structs.decode_BIG_Q),
    0xbfb96ec0: ('splash_sound_medium', structs.decode_BIG_Q),
    0xc34a1dc9: ('splash_sound_big', structs.decode_BIG_Q),
    0x0efcdea0: ('caud_0x0efcdea0', structs.decode_BIG_Q),
    0x78df0e7f: ('caud_0x78df0e7f', structs.decode_BIG_Q),
    0x84e241ed: ('min_splash_kinetic_energy', structs.decode_BIG_f),
    0xe2072799: ('max_splash_kinetic_energy', structs.decode_BIG_f),
    0xab463f9a: ('rolling_splash_effect', structs.decode_BIG_Q),
    0x66d466b5: ('runoff_visor_effect', structs.decode_BIG_Q),
    0xb97ccede: ('runoff_ball_effect', structs.decode_BIG_Q),
    0x4d82bb1e: ('slow_exit_sound', structs.decode_BIG_Q),
    0xc51da2dc: ('fast_exit_sound', structs.decode_BIG_Q),
    0x03d24e64: ('fast_exit_speed', structs.decode_BIG_f),
    0x687df7a3: ('unknown_0x687df7a3', structs.decode_BIG_f),
    0xe73aad13: ('unknown_0xe73aad13', structs.decode_BIG_f),
    0xac67b7d7: ('unknown_0xac67b7d7', structs.decode_BIG_f),
    0xe578c0dd: ('fog_color', _decode_fog_color),
    0xb4b0fd8d: ('fog_height', structs.decode_BIG_f),
    0xb90dff44: ('fog_bob_height', structs.decode_BIG_f),
    0xf608d35c: ('fog_bob_freq', structs.decode_BIG_f),
    0xfe3bc8f7: ('unknown_0xfe3bc8f7', structs.decode_BIG_bool_),
    0x318418aa: ('freeze_radius', structs.decode_BIG_f),
    0x7b77e31d: ('player_freeze_radius', structs.decode_BIG_f),
    0x84927794: ('roll_fully_submerged_sound', structs.decode_BIG_Q),
    0xa6e650a0: ('roll_partially_submerged_sound', structs.decode_BIG_Q),
    0x90b8eb66: ('vertical_sound', structs.decode_BIG_Q),
    0x3eede8f7: ('damage_sound', structs.decode_BIG_Q),
    0xc110ed44: ('damage_effect', structs.decode_BIG_Q),
    0xb9413fe6: ('footstep_sound', structs.decode_BIG_Q),
    0x822118b4: ('filter_sound_effects', structs.decode_BIG_bool_),
    0xfe89b6e4: ('volume_attenuation', structs.decode_BIG_f),
    0x414379ea: ('filter_cutoff_frequency', structs.decode_BIG_l),
    0x3c764739: ('fluid_lock_string', _decode_fluid_lock_string),
}
