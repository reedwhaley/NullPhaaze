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
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class RoomAcousticsJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        room_volume: int
        priority: int
        reverb_hi_enabled: bool
        reverb_hi_temp_disable_fx: bool
        reverb_hi_time: float
        reverb_hi_pre_delay: float
        reverb_hi_damping: float
        reverb_hi_coloration: float
        reverb_hi_cross_talk: float
        reverb_hi_mix: float
        chorus_enabled: bool
        chorus_base_delay: float
        chorus_variation: float
        chorus_period: float
        reverb_std_enabled: bool
        rever_std_temp_disable_fx: bool
        reverb_std_time: float
        reverb_std_pre_delay: float
        reverb_std_damping: float
        reverb_std_coloration: float
        reverb_std_mix: float
        delay_enabled: bool
        delay0: int
        delay1: int
        delay2: int
        delay_feedback0: int
        delay_feedback1: int
        delay_feedback2: int
        delay_output0: int
        delay_output1: int
        delay_output2: int
        delay_low_pass_filter: int
        delay_high_pass_filter: int
        flanger_enabled: bool
        flanger_delay: float
        flanger_delay_phase: float
        flanger_dry: float
        flanger_feedback: float
        flanger_lfo_depth: float
        flanger_lfo_frequency: float
        flanger_lfo_wave: float
        flanger_out: float
        bitcrusher_enabled: bool
        bitcrusher_distortion_type: int
        bitcrusher_gain: float
        bitcrusher_bit_depth: int
        bitcrusher_sample_rate_reduction: float
        phaser_enabled: bool
        phaser_frequency: float
        phaser_feedback: float
        phaser_invert: float
        phaser_mix: float
        phaser_sweep: float
    

@dataclasses.dataclass()
class RoomAcoustics(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    room_volume: int = dataclasses.field(default=117, metadata={
        'reflection': FieldReflection[int](
            int, id=0xbd9ea266, original_name='RoomVolume'
        ),
    })
    priority: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x86cf23f4, original_name='Priority'
        ),
    })  # Choice
    reverb_hi_enabled: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xa00360cc, original_name='ReverbHiEnabled'
        ),
    })
    reverb_hi_temp_disable_fx: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x3263c26e, original_name='ReverbHiTempDisableFx'
        ),
    })
    reverb_hi_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc5868061, original_name='ReverbHiTime'
        ),
    })
    reverb_hi_pre_delay: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc6f50032, original_name='ReverbHiPreDelay'
        ),
    })
    reverb_hi_damping: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcba5555d, original_name='ReverbHiDamping'
        ),
    })
    reverb_hi_coloration: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7319cf50, original_name='ReverbHiColoration'
        ),
    })
    reverb_hi_cross_talk: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3dc3f16f, original_name='ReverbHiCrossTalk'
        ),
    })
    reverb_hi_mix: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd5518b6c, original_name='ReverbHiMix'
        ),
    })
    chorus_enabled: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x26997ccb, original_name='ChorusEnabled'
        ),
    })
    chorus_base_delay: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x121bdfad, original_name='ChorusBaseDelay'
        ),
    })
    chorus_variation: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe8796bce, original_name='ChorusVariation'
        ),
    })
    chorus_period: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x24bbd5e4, original_name='ChorusPeriod'
        ),
    })
    reverb_std_enabled: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xff31631b, original_name='ReverbStdEnabled'
        ),
    })
    rever_std_temp_disable_fx: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x4a5bbf90, original_name='ReverStdTempDisableFX'
        ),
    })
    reverb_std_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9662498a, original_name='ReverbStdTime'
        ),
    })
    reverb_std_pre_delay: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x91855d62, original_name='ReverbStdPreDelay'
        ),
    })
    reverb_std_damping: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd34d2029, original_name='ReverbStdDamping'
        ),
    })
    reverb_std_coloration: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdc78e83d, original_name='ReverbStdColoration'
        ),
    })
    reverb_std_mix: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x820b509e, original_name='ReverbStdMix'
        ),
    })
    delay_enabled: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xe9a36031, original_name='DelayEnabled'
        ),
    })
    delay0: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x62c49457, original_name='Delay0'
        ),
    })
    delay1: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xda78f332, original_name='Delay1'
        ),
    })
    delay2: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xc8cd5cdc, original_name='Delay2'
        ),
    })
    delay_feedback0: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x7c14ff17, original_name='DelayFeedback0'
        ),
    })
    delay_feedback1: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xc4a89872, original_name='DelayFeedback1'
        ),
    })
    delay_feedback2: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xd61d379c, original_name='DelayFeedback2'
        ),
    })
    delay_output0: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x9f75987f, original_name='DelayOutput0'
        ),
    })
    delay_output1: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x27c9ff1a, original_name='DelayOutput1'
        ),
    })
    delay_output2: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x357c50f4, original_name='DelayOutput2'
        ),
    })
    delay_low_pass_filter: int = dataclasses.field(default=32000, metadata={
        'reflection': FieldReflection[int](
            int, id=0xcf45711c, original_name='DelayLowPassFilter'
        ),
    })
    delay_high_pass_filter: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x626d1e9b, original_name='DelayHighPassFilter'
        ),
    })
    flanger_enabled: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x7d8ee273, original_name='FlangerEnabled'
        ),
    })
    flanger_delay: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x83378e6a, original_name='FlangerDelay'
        ),
    })
    flanger_delay_phase: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf549d269, original_name='FlangerDelayPhase'
        ),
    })
    flanger_dry: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x11fdae16, original_name='FlangerDry'
        ),
    })
    flanger_feedback: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa3c439c1, original_name='FlangerFeedback'
        ),
    })
    flanger_lfo_depth: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2dc70efe, original_name='FlangerLFODepth'
        ),
    })
    flanger_lfo_frequency: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe2bd3706, original_name='FlangerLFOFrequency'
        ),
    })
    flanger_lfo_wave: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5e29cef8, original_name='FlangerLFOWave'
        ),
    })
    flanger_out: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x35ae9f10, original_name='FlangerOut'
        ),
    })
    bitcrusher_enabled: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x3e8d8694, original_name='BitcrusherEnabled'
        ),
    })
    bitcrusher_distortion_type: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xf51a1d6a, original_name='BitcrusherDistortionType'
        ),
    })  # Choice
    bitcrusher_gain: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbb1a0f34, original_name='BitcrusherGain'
        ),
    })
    bitcrusher_bit_depth: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xeb009039, original_name='BitcrusherBitDepth'
        ),
    })
    bitcrusher_sample_rate_reduction: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x58096e0b, original_name='BitcrusherSampleRateReduction'
        ),
    })
    phaser_enabled: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x3d8cad84, original_name='PhaserEnabled'
        ),
    })
    phaser_frequency: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x23c340f6, original_name='PhaserFrequency'
        ),
    })
    phaser_feedback: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1e5a52b8, original_name='PhaserFeedback'
        ),
    })
    phaser_invert: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1d69bec4, original_name='PhaserInvert'
        ),
    })
    phaser_mix: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x24538c4a, original_name='PhaserMix'
        ),
    })
    phaser_sweep: float = dataclasses.field(default=200.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd5388116, original_name='PhaserSweep'
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'RMAC'

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
        if property_count != 54:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbd9ea266
        room_volume = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x86cf23f4
        priority = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa00360cc
        reverb_hi_enabled = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3263c26e
        reverb_hi_temp_disable_fx = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc5868061
        reverb_hi_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc6f50032
        reverb_hi_pre_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcba5555d
        reverb_hi_damping = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7319cf50
        reverb_hi_coloration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3dc3f16f
        reverb_hi_cross_talk = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd5518b6c
        reverb_hi_mix = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x26997ccb
        chorus_enabled = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x121bdfad
        chorus_base_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe8796bce
        chorus_variation = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24bbd5e4
        chorus_period = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xff31631b
        reverb_std_enabled = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4a5bbf90
        rever_std_temp_disable_fx = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9662498a
        reverb_std_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x91855d62
        reverb_std_pre_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd34d2029
        reverb_std_damping = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdc78e83d
        reverb_std_coloration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x820b509e
        reverb_std_mix = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe9a36031
        delay_enabled = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x62c49457
        delay0 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xda78f332
        delay1 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc8cd5cdc
        delay2 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7c14ff17
        delay_feedback0 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc4a89872
        delay_feedback1 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd61d379c
        delay_feedback2 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9f75987f
        delay_output0 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x27c9ff1a
        delay_output1 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x357c50f4
        delay_output2 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcf45711c
        delay_low_pass_filter = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x626d1e9b
        delay_high_pass_filter = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7d8ee273
        flanger_enabled = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x83378e6a
        flanger_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf549d269
        flanger_delay_phase = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x11fdae16
        flanger_dry = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa3c439c1
        flanger_feedback = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2dc70efe
        flanger_lfo_depth = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe2bd3706
        flanger_lfo_frequency = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5e29cef8
        flanger_lfo_wave = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x35ae9f10
        flanger_out = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3e8d8694
        bitcrusher_enabled = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf51a1d6a
        bitcrusher_distortion_type = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbb1a0f34
        bitcrusher_gain = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xeb009039
        bitcrusher_bit_depth = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58096e0b
        bitcrusher_sample_rate_reduction = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3d8cad84
        phaser_enabled = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23c340f6
        phaser_frequency = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1e5a52b8
        phaser_feedback = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1d69bec4
        phaser_invert = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24538c4a
        phaser_mix = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd5388116
        phaser_sweep = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(editor_properties, room_volume, priority, reverb_hi_enabled, reverb_hi_temp_disable_fx, reverb_hi_time, reverb_hi_pre_delay, reverb_hi_damping, reverb_hi_coloration, reverb_hi_cross_talk, reverb_hi_mix, chorus_enabled, chorus_base_delay, chorus_variation, chorus_period, reverb_std_enabled, rever_std_temp_disable_fx, reverb_std_time, reverb_std_pre_delay, reverb_std_damping, reverb_std_coloration, reverb_std_mix, delay_enabled, delay0, delay1, delay2, delay_feedback0, delay_feedback1, delay_feedback2, delay_output0, delay_output1, delay_output2, delay_low_pass_filter, delay_high_pass_filter, flanger_enabled, flanger_delay, flanger_delay_phase, flanger_dry, flanger_feedback, flanger_lfo_depth, flanger_lfo_frequency, flanger_lfo_wave, flanger_out, bitcrusher_enabled, bitcrusher_distortion_type, bitcrusher_gain, bitcrusher_bit_depth, bitcrusher_sample_rate_reduction, phaser_enabled, phaser_frequency, phaser_feedback, phaser_invert, phaser_mix, phaser_sweep)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x006')  # 54 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game, default_override={'misc_flags': 3})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbd\x9e\xa2f')  # 0xbd9ea266
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.room_volume))

        data.write(b'\x86\xcf#\xf4')  # 0x86cf23f4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.priority))

        data.write(b'\xa0\x03`\xcc')  # 0xa00360cc
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.reverb_hi_enabled))

        data.write(b'2c\xc2n')  # 0x3263c26e
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.reverb_hi_temp_disable_fx))

        data.write(b'\xc5\x86\x80a')  # 0xc5868061
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.reverb_hi_time))

        data.write(b'\xc6\xf5\x002')  # 0xc6f50032
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.reverb_hi_pre_delay))

        data.write(b'\xcb\xa5U]')  # 0xcba5555d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.reverb_hi_damping))

        data.write(b's\x19\xcfP')  # 0x7319cf50
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.reverb_hi_coloration))

        data.write(b'=\xc3\xf1o')  # 0x3dc3f16f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.reverb_hi_cross_talk))

        data.write(b'\xd5Q\x8bl')  # 0xd5518b6c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.reverb_hi_mix))

        data.write(b'&\x99|\xcb')  # 0x26997ccb
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.chorus_enabled))

        data.write(b'\x12\x1b\xdf\xad')  # 0x121bdfad
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.chorus_base_delay))

        data.write(b'\xe8yk\xce')  # 0xe8796bce
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.chorus_variation))

        data.write(b'$\xbb\xd5\xe4')  # 0x24bbd5e4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.chorus_period))

        data.write(b'\xff1c\x1b')  # 0xff31631b
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.reverb_std_enabled))

        data.write(b'J[\xbf\x90')  # 0x4a5bbf90
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.rever_std_temp_disable_fx))

        data.write(b'\x96bI\x8a')  # 0x9662498a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.reverb_std_time))

        data.write(b'\x91\x85]b')  # 0x91855d62
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.reverb_std_pre_delay))

        data.write(b'\xd3M )')  # 0xd34d2029
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.reverb_std_damping))

        data.write(b'\xdcx\xe8=')  # 0xdc78e83d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.reverb_std_coloration))

        data.write(b'\x82\x0bP\x9e')  # 0x820b509e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.reverb_std_mix))

        data.write(b'\xe9\xa3`1')  # 0xe9a36031
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.delay_enabled))

        data.write(b'b\xc4\x94W')  # 0x62c49457
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.delay0))

        data.write(b'\xdax\xf32')  # 0xda78f332
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.delay1))

        data.write(b'\xc8\xcd\\\xdc')  # 0xc8cd5cdc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.delay2))

        data.write(b'|\x14\xff\x17')  # 0x7c14ff17
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.delay_feedback0))

        data.write(b'\xc4\xa8\x98r')  # 0xc4a89872
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.delay_feedback1))

        data.write(b'\xd6\x1d7\x9c')  # 0xd61d379c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.delay_feedback2))

        data.write(b'\x9fu\x98\x7f')  # 0x9f75987f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.delay_output0))

        data.write(b"'\xc9\xff\x1a")  # 0x27c9ff1a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.delay_output1))

        data.write(b'5|P\xf4')  # 0x357c50f4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.delay_output2))

        data.write(b'\xcfEq\x1c')  # 0xcf45711c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.delay_low_pass_filter))

        data.write(b'bm\x1e\x9b')  # 0x626d1e9b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.delay_high_pass_filter))

        data.write(b'}\x8e\xe2s')  # 0x7d8ee273
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.flanger_enabled))

        data.write(b'\x837\x8ej')  # 0x83378e6a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flanger_delay))

        data.write(b'\xf5I\xd2i')  # 0xf549d269
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flanger_delay_phase))

        data.write(b'\x11\xfd\xae\x16')  # 0x11fdae16
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flanger_dry))

        data.write(b'\xa3\xc49\xc1')  # 0xa3c439c1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flanger_feedback))

        data.write(b'-\xc7\x0e\xfe')  # 0x2dc70efe
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flanger_lfo_depth))

        data.write(b'\xe2\xbd7\x06')  # 0xe2bd3706
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flanger_lfo_frequency))

        data.write(b'^)\xce\xf8')  # 0x5e29cef8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flanger_lfo_wave))

        data.write(b'5\xae\x9f\x10')  # 0x35ae9f10
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flanger_out))

        data.write(b'>\x8d\x86\x94')  # 0x3e8d8694
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.bitcrusher_enabled))

        data.write(b'\xf5\x1a\x1dj')  # 0xf51a1d6a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.bitcrusher_distortion_type))

        data.write(b'\xbb\x1a\x0f4')  # 0xbb1a0f34
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.bitcrusher_gain))

        data.write(b'\xeb\x00\x909')  # 0xeb009039
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.bitcrusher_bit_depth))

        data.write(b'X\tn\x0b')  # 0x58096e0b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.bitcrusher_sample_rate_reduction))

        data.write(b'=\x8c\xad\x84')  # 0x3d8cad84
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.phaser_enabled))

        data.write(b'#\xc3@\xf6')  # 0x23c340f6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phaser_frequency))

        data.write(b'\x1eZR\xb8')  # 0x1e5a52b8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phaser_feedback))

        data.write(b'\x1di\xbe\xc4')  # 0x1d69bec4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phaser_invert))

        data.write(b'$S\x8cJ')  # 0x24538c4a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phaser_mix))

        data.write(b'\xd58\x81\x16')  # 0xd5388116
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phaser_sweep))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("RoomAcousticsJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            room_volume=json_data['room_volume'],
            priority=json_data['priority'],
            reverb_hi_enabled=json_data['reverb_hi_enabled'],
            reverb_hi_temp_disable_fx=json_data['reverb_hi_temp_disable_fx'],
            reverb_hi_time=json_data['reverb_hi_time'],
            reverb_hi_pre_delay=json_data['reverb_hi_pre_delay'],
            reverb_hi_damping=json_data['reverb_hi_damping'],
            reverb_hi_coloration=json_data['reverb_hi_coloration'],
            reverb_hi_cross_talk=json_data['reverb_hi_cross_talk'],
            reverb_hi_mix=json_data['reverb_hi_mix'],
            chorus_enabled=json_data['chorus_enabled'],
            chorus_base_delay=json_data['chorus_base_delay'],
            chorus_variation=json_data['chorus_variation'],
            chorus_period=json_data['chorus_period'],
            reverb_std_enabled=json_data['reverb_std_enabled'],
            rever_std_temp_disable_fx=json_data['rever_std_temp_disable_fx'],
            reverb_std_time=json_data['reverb_std_time'],
            reverb_std_pre_delay=json_data['reverb_std_pre_delay'],
            reverb_std_damping=json_data['reverb_std_damping'],
            reverb_std_coloration=json_data['reverb_std_coloration'],
            reverb_std_mix=json_data['reverb_std_mix'],
            delay_enabled=json_data['delay_enabled'],
            delay0=json_data['delay0'],
            delay1=json_data['delay1'],
            delay2=json_data['delay2'],
            delay_feedback0=json_data['delay_feedback0'],
            delay_feedback1=json_data['delay_feedback1'],
            delay_feedback2=json_data['delay_feedback2'],
            delay_output0=json_data['delay_output0'],
            delay_output1=json_data['delay_output1'],
            delay_output2=json_data['delay_output2'],
            delay_low_pass_filter=json_data['delay_low_pass_filter'],
            delay_high_pass_filter=json_data['delay_high_pass_filter'],
            flanger_enabled=json_data['flanger_enabled'],
            flanger_delay=json_data['flanger_delay'],
            flanger_delay_phase=json_data['flanger_delay_phase'],
            flanger_dry=json_data['flanger_dry'],
            flanger_feedback=json_data['flanger_feedback'],
            flanger_lfo_depth=json_data['flanger_lfo_depth'],
            flanger_lfo_frequency=json_data['flanger_lfo_frequency'],
            flanger_lfo_wave=json_data['flanger_lfo_wave'],
            flanger_out=json_data['flanger_out'],
            bitcrusher_enabled=json_data['bitcrusher_enabled'],
            bitcrusher_distortion_type=json_data['bitcrusher_distortion_type'],
            bitcrusher_gain=json_data['bitcrusher_gain'],
            bitcrusher_bit_depth=json_data['bitcrusher_bit_depth'],
            bitcrusher_sample_rate_reduction=json_data['bitcrusher_sample_rate_reduction'],
            phaser_enabled=json_data['phaser_enabled'],
            phaser_frequency=json_data['phaser_frequency'],
            phaser_feedback=json_data['phaser_feedback'],
            phaser_invert=json_data['phaser_invert'],
            phaser_mix=json_data['phaser_mix'],
            phaser_sweep=json_data['phaser_sweep'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'room_volume': self.room_volume,
            'priority': self.priority,
            'reverb_hi_enabled': self.reverb_hi_enabled,
            'reverb_hi_temp_disable_fx': self.reverb_hi_temp_disable_fx,
            'reverb_hi_time': self.reverb_hi_time,
            'reverb_hi_pre_delay': self.reverb_hi_pre_delay,
            'reverb_hi_damping': self.reverb_hi_damping,
            'reverb_hi_coloration': self.reverb_hi_coloration,
            'reverb_hi_cross_talk': self.reverb_hi_cross_talk,
            'reverb_hi_mix': self.reverb_hi_mix,
            'chorus_enabled': self.chorus_enabled,
            'chorus_base_delay': self.chorus_base_delay,
            'chorus_variation': self.chorus_variation,
            'chorus_period': self.chorus_period,
            'reverb_std_enabled': self.reverb_std_enabled,
            'rever_std_temp_disable_fx': self.rever_std_temp_disable_fx,
            'reverb_std_time': self.reverb_std_time,
            'reverb_std_pre_delay': self.reverb_std_pre_delay,
            'reverb_std_damping': self.reverb_std_damping,
            'reverb_std_coloration': self.reverb_std_coloration,
            'reverb_std_mix': self.reverb_std_mix,
            'delay_enabled': self.delay_enabled,
            'delay0': self.delay0,
            'delay1': self.delay1,
            'delay2': self.delay2,
            'delay_feedback0': self.delay_feedback0,
            'delay_feedback1': self.delay_feedback1,
            'delay_feedback2': self.delay_feedback2,
            'delay_output0': self.delay_output0,
            'delay_output1': self.delay_output1,
            'delay_output2': self.delay_output2,
            'delay_low_pass_filter': self.delay_low_pass_filter,
            'delay_high_pass_filter': self.delay_high_pass_filter,
            'flanger_enabled': self.flanger_enabled,
            'flanger_delay': self.flanger_delay,
            'flanger_delay_phase': self.flanger_delay_phase,
            'flanger_dry': self.flanger_dry,
            'flanger_feedback': self.flanger_feedback,
            'flanger_lfo_depth': self.flanger_lfo_depth,
            'flanger_lfo_frequency': self.flanger_lfo_frequency,
            'flanger_lfo_wave': self.flanger_lfo_wave,
            'flanger_out': self.flanger_out,
            'bitcrusher_enabled': self.bitcrusher_enabled,
            'bitcrusher_distortion_type': self.bitcrusher_distortion_type,
            'bitcrusher_gain': self.bitcrusher_gain,
            'bitcrusher_bit_depth': self.bitcrusher_bit_depth,
            'bitcrusher_sample_rate_reduction': self.bitcrusher_sample_rate_reduction,
            'phaser_enabled': self.phaser_enabled,
            'phaser_frequency': self.phaser_frequency,
            'phaser_feedback': self.phaser_feedback,
            'phaser_invert': self.phaser_invert,
            'phaser_mix': self.phaser_mix,
            'phaser_sweep': self.phaser_sweep,
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xbd9ea266: ('room_volume', structs.decode_BIG_l),
    0x86cf23f4: ('priority', structs.decode_BIG_L),
    0xa00360cc: ('reverb_hi_enabled', structs.decode_BIG_bool_),
    0x3263c26e: ('reverb_hi_temp_disable_fx', structs.decode_BIG_bool_),
    0xc5868061: ('reverb_hi_time', structs.decode_BIG_f),
    0xc6f50032: ('reverb_hi_pre_delay', structs.decode_BIG_f),
    0xcba5555d: ('reverb_hi_damping', structs.decode_BIG_f),
    0x7319cf50: ('reverb_hi_coloration', structs.decode_BIG_f),
    0x3dc3f16f: ('reverb_hi_cross_talk', structs.decode_BIG_f),
    0xd5518b6c: ('reverb_hi_mix', structs.decode_BIG_f),
    0x26997ccb: ('chorus_enabled', structs.decode_BIG_bool_),
    0x121bdfad: ('chorus_base_delay', structs.decode_BIG_f),
    0xe8796bce: ('chorus_variation', structs.decode_BIG_f),
    0x24bbd5e4: ('chorus_period', structs.decode_BIG_f),
    0xff31631b: ('reverb_std_enabled', structs.decode_BIG_bool_),
    0x4a5bbf90: ('rever_std_temp_disable_fx', structs.decode_BIG_bool_),
    0x9662498a: ('reverb_std_time', structs.decode_BIG_f),
    0x91855d62: ('reverb_std_pre_delay', structs.decode_BIG_f),
    0xd34d2029: ('reverb_std_damping', structs.decode_BIG_f),
    0xdc78e83d: ('reverb_std_coloration', structs.decode_BIG_f),
    0x820b509e: ('reverb_std_mix', structs.decode_BIG_f),
    0xe9a36031: ('delay_enabled', structs.decode_BIG_bool_),
    0x62c49457: ('delay0', structs.decode_BIG_l),
    0xda78f332: ('delay1', structs.decode_BIG_l),
    0xc8cd5cdc: ('delay2', structs.decode_BIG_l),
    0x7c14ff17: ('delay_feedback0', structs.decode_BIG_l),
    0xc4a89872: ('delay_feedback1', structs.decode_BIG_l),
    0xd61d379c: ('delay_feedback2', structs.decode_BIG_l),
    0x9f75987f: ('delay_output0', structs.decode_BIG_l),
    0x27c9ff1a: ('delay_output1', structs.decode_BIG_l),
    0x357c50f4: ('delay_output2', structs.decode_BIG_l),
    0xcf45711c: ('delay_low_pass_filter', structs.decode_BIG_l),
    0x626d1e9b: ('delay_high_pass_filter', structs.decode_BIG_l),
    0x7d8ee273: ('flanger_enabled', structs.decode_BIG_bool_),
    0x83378e6a: ('flanger_delay', structs.decode_BIG_f),
    0xf549d269: ('flanger_delay_phase', structs.decode_BIG_f),
    0x11fdae16: ('flanger_dry', structs.decode_BIG_f),
    0xa3c439c1: ('flanger_feedback', structs.decode_BIG_f),
    0x2dc70efe: ('flanger_lfo_depth', structs.decode_BIG_f),
    0xe2bd3706: ('flanger_lfo_frequency', structs.decode_BIG_f),
    0x5e29cef8: ('flanger_lfo_wave', structs.decode_BIG_f),
    0x35ae9f10: ('flanger_out', structs.decode_BIG_f),
    0x3e8d8694: ('bitcrusher_enabled', structs.decode_BIG_bool_),
    0xf51a1d6a: ('bitcrusher_distortion_type', structs.decode_BIG_L),
    0xbb1a0f34: ('bitcrusher_gain', structs.decode_BIG_f),
    0xeb009039: ('bitcrusher_bit_depth', structs.decode_BIG_l),
    0x58096e0b: ('bitcrusher_sample_rate_reduction', structs.decode_BIG_f),
    0x3d8cad84: ('phaser_enabled', structs.decode_BIG_bool_),
    0x23c340f6: ('phaser_frequency', structs.decode_BIG_f),
    0x1e5a52b8: ('phaser_feedback', structs.decode_BIG_f),
    0x1d69bec4: ('phaser_invert', structs.decode_BIG_f),
    0x24538c4a: ('phaser_mix', structs.decode_BIG_f),
    0xd5388116: ('phaser_sweep', structs.decode_BIG_f),
}
