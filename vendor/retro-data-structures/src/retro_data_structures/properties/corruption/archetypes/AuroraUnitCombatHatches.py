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
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.UnknownStruct6 import UnknownStruct6
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class AuroraUnitCombatHatchesJson(typing_extensions.TypedDict):
        camera_animation_info: json_util.JsonObject
        overload_damage_threshold: float
        open_hatch_vulnerability: json_util.JsonObject
        empty_hatch_open_duration: float
        empty_hatch_open_duration_variance: float
        missile_destroyed_empty_hatch_open_duration: float
        missile_destroyed_empty_hatch_open_duration_variance: float
        next_empty_hatch_open_time: float
        next_empty_hatch_open_variance: float
        missile_hatch_open_duration: float
        missile_hatch_open_duration_variance: float
        tentacle_animation_info: json_util.JsonObject
        num_missile_hatches: int
        missile_weapon: int
        missile_damage: json_util.JsonObject
        missile_explode_threshold: float
        missile_expode_effect: int
        missile_explode_sound: int
        fire_missile_time: float
        next_fire_missile_time: float
        unknown_0xaa7d527d: float
        initial_camera_hatch_open_time: float
        inital_camera_hatch_open_variance: float
        camera_hatch_open_duration: float
        camera_hatch_open_duration_variance: float
        next_camera_hatch_open_time: float
        next_camera_hatch_open_variance: float
        camera_sequence_duration: float
        min_camera_sequences: int
        max_camera_sequences: int
        next_camera_sequence_time: float
        next_camera_sequence_variance: float
        unknown_0x72fb67da: float
        camera_damage_threshold: float
        camera_shock_time: float
        dizzy_state_time: float
        stage2_health_percent: float
        stage3_health_percent: float
        unknown_0x8c63f9d0: float
        unknown_0x6b7e5f47: float
        unknown_0x6afe0147: float
        unknown_0x04721a06: float
        unknown_struct6: json_util.JsonObject
    

@dataclasses.dataclass()
class AuroraUnitCombatHatches(BaseProperty):
    camera_animation_info: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0xc107a48a, original_name='CameraAnimationInfo', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    overload_damage_threshold: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa6c47cd3, original_name='OverloadDamageThreshold'
        ),
    })
    open_hatch_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x0fce03ca, original_name='OpenHatchVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    empty_hatch_open_duration: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa4b62aa9, original_name='EmptyHatchOpenDuration'
        ),
    })
    empty_hatch_open_duration_variance: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb64ea21c, original_name='EmptyHatchOpenDurationVariance'
        ),
    })
    missile_destroyed_empty_hatch_open_duration: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa13b1ba9, original_name='MissileDestroyedEmptyHatchOpenDuration'
        ),
    })
    missile_destroyed_empty_hatch_open_duration_variance: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd294848c, original_name='MissileDestroyedEmptyHatchOpenDurationVariance'
        ),
    })
    next_empty_hatch_open_time: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9c425325, original_name='NextEmptyHatchOpenTime'
        ),
    })
    next_empty_hatch_open_variance: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfa22836a, original_name='NextEmptyHatchOpenVariance'
        ),
    })
    missile_hatch_open_duration: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xed410449, original_name='MissileHatchOpenDuration'
        ),
    })
    missile_hatch_open_duration_variance: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf768d625, original_name='MissileHatchOpenDurationVariance'
        ),
    })
    tentacle_animation_info: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0xa229ff6a, original_name='TentacleAnimationInfo', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    num_missile_hatches: int = dataclasses.field(default=2, metadata={
        'reflection': FieldReflection[int](
            int, id=0x52806eff, original_name='NumMissileHatches'
        ),
    })
    missile_weapon: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2ea31f83, original_name='MissileWeapon'
        ),
    })
    missile_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x258cfb4d, original_name='MissileDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    missile_explode_threshold: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7becdb66, original_name='MissileExplodeThreshold'
        ),
    })
    missile_expode_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x87afe8d8, original_name='MissileExpodeEffect'
        ),
    })
    missile_explode_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3dfd1c4f, original_name='MissileExplodeSound'
        ),
    })
    fire_missile_time: float = dataclasses.field(default=6.75, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb8bf561e, original_name='FireMissileTime'
        ),
    })
    next_fire_missile_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa4166e3c, original_name='NextFireMissileTime'
        ),
    })
    unknown_0xaa7d527d: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xaa7d527d, original_name='Unknown'
        ),
    })
    initial_camera_hatch_open_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf707c050, original_name='InitialCameraHatchOpenTime'
        ),
    })
    inital_camera_hatch_open_variance: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4128ff6d, original_name='InitalCameraHatchOpenVariance'
        ),
    })
    camera_hatch_open_duration: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3b6218da, original_name='CameraHatchOpenDuration'
        ),
    })
    camera_hatch_open_duration_variance: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x71946eec, original_name='CameraHatchOpenDurationVariance'
        ),
    })
    next_camera_hatch_open_time: float = dataclasses.field(default=3.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa184d013, original_name='NextCameraHatchOpenTime'
        ),
    })
    next_camera_hatch_open_variance: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x09d9bd17, original_name='NextCameraHatchOpenVariance'
        ),
    })
    camera_sequence_duration: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x53c1d089, original_name='CameraSequenceDuration'
        ),
    })
    min_camera_sequences: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0x306fd39a, original_name='MinCameraSequences'
        ),
    })
    max_camera_sequences: int = dataclasses.field(default=3, metadata={
        'reflection': FieldReflection[int](
            int, id=0x232a3531, original_name='MaxCameraSequences'
        ),
    })
    next_camera_sequence_time: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x193c7751, original_name='NextCameraSequenceTime'
        ),
    })
    next_camera_sequence_variance: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0d55794a, original_name='NextCameraSequenceVariance'
        ),
    })
    unknown_0x72fb67da: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x72fb67da, original_name='Unknown'
        ),
    })
    camera_damage_threshold: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbdb18b2f, original_name='CameraDamageThreshold'
        ),
    })
    camera_shock_time: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0e958d9e, original_name='CameraShockTime'
        ),
    })
    dizzy_state_time: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x251c55e3, original_name='DizzyStateTime'
        ),
    })
    stage2_health_percent: float = dataclasses.field(default=0.6000000238418579, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0a072c48, original_name='Stage2HealthPercent'
        ),
    })
    stage3_health_percent: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdde5ac10, original_name='Stage3HealthPercent'
        ),
    })
    unknown_0x8c63f9d0: float = dataclasses.field(default=0.75, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8c63f9d0, original_name='Unknown'
        ),
    })
    unknown_0x6b7e5f47: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6b7e5f47, original_name='Unknown'
        ),
    })
    unknown_0x6afe0147: float = dataclasses.field(default=0.75, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6afe0147, original_name='Unknown'
        ),
    })
    unknown_0x04721a06: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x04721a06, original_name='Unknown'
        ),
    })
    unknown_struct6: UnknownStruct6 = dataclasses.field(default_factory=UnknownStruct6, metadata={
        'reflection': FieldReflection[UnknownStruct6](
            UnknownStruct6, id=0xd8579ba3, original_name='UnknownStruct6', from_json=UnknownStruct6.from_json, to_json=UnknownStruct6.to_json
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
        if property_count != 43:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc107a48a
        camera_animation_info = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa6c47cd3
        overload_damage_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0fce03ca
        open_hatch_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa4b62aa9
        empty_hatch_open_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb64ea21c
        empty_hatch_open_duration_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa13b1ba9
        missile_destroyed_empty_hatch_open_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd294848c
        missile_destroyed_empty_hatch_open_duration_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9c425325
        next_empty_hatch_open_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfa22836a
        next_empty_hatch_open_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed410449
        missile_hatch_open_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf768d625
        missile_hatch_open_duration_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa229ff6a
        tentacle_animation_info = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x52806eff
        num_missile_hatches = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2ea31f83
        missile_weapon = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x258cfb4d
        missile_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7becdb66
        missile_explode_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x87afe8d8
        missile_expode_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3dfd1c4f
        missile_explode_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb8bf561e
        fire_missile_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa4166e3c
        next_fire_missile_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaa7d527d
        unknown_0xaa7d527d = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf707c050
        initial_camera_hatch_open_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4128ff6d
        inital_camera_hatch_open_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3b6218da
        camera_hatch_open_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71946eec
        camera_hatch_open_duration_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa184d013
        next_camera_hatch_open_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x09d9bd17
        next_camera_hatch_open_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x53c1d089
        camera_sequence_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x306fd39a
        min_camera_sequences = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x232a3531
        max_camera_sequences = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x193c7751
        next_camera_sequence_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0d55794a
        next_camera_sequence_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x72fb67da
        unknown_0x72fb67da = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbdb18b2f
        camera_damage_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0e958d9e
        camera_shock_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x251c55e3
        dizzy_state_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0a072c48
        stage2_health_percent = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdde5ac10
        stage3_health_percent = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8c63f9d0
        unknown_0x8c63f9d0 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6b7e5f47
        unknown_0x6b7e5f47 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6afe0147
        unknown_0x6afe0147 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x04721a06
        unknown_0x04721a06 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd8579ba3
        unknown_struct6 = UnknownStruct6.from_stream(data, game, property_size)
    
        return cls(camera_animation_info, overload_damage_threshold, open_hatch_vulnerability, empty_hatch_open_duration, empty_hatch_open_duration_variance, missile_destroyed_empty_hatch_open_duration, missile_destroyed_empty_hatch_open_duration_variance, next_empty_hatch_open_time, next_empty_hatch_open_variance, missile_hatch_open_duration, missile_hatch_open_duration_variance, tentacle_animation_info, num_missile_hatches, missile_weapon, missile_damage, missile_explode_threshold, missile_expode_effect, missile_explode_sound, fire_missile_time, next_fire_missile_time, unknown_0xaa7d527d, initial_camera_hatch_open_time, inital_camera_hatch_open_variance, camera_hatch_open_duration, camera_hatch_open_duration_variance, next_camera_hatch_open_time, next_camera_hatch_open_variance, camera_sequence_duration, min_camera_sequences, max_camera_sequences, next_camera_sequence_time, next_camera_sequence_variance, unknown_0x72fb67da, camera_damage_threshold, camera_shock_time, dizzy_state_time, stage2_health_percent, stage3_health_percent, unknown_0x8c63f9d0, unknown_0x6b7e5f47, unknown_0x6afe0147, unknown_0x04721a06, unknown_struct6)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        num_properties_offset = data.tell()
        data.write(b'\x00*')  # 42 properties
        num_properties_written = 42

        data.write(b'\xc1\x07\xa4\x8a')  # 0xc107a48a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.camera_animation_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa6\xc4|\xd3')  # 0xa6c47cd3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.overload_damage_threshold))

        data.write(b'\x0f\xce\x03\xca')  # 0xfce03ca
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.open_hatch_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa4\xb6*\xa9')  # 0xa4b62aa9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.empty_hatch_open_duration))

        data.write(b'\xb6N\xa2\x1c')  # 0xb64ea21c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.empty_hatch_open_duration_variance))

        data.write(b'\xa1;\x1b\xa9')  # 0xa13b1ba9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.missile_destroyed_empty_hatch_open_duration))

        data.write(b'\xd2\x94\x84\x8c')  # 0xd294848c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.missile_destroyed_empty_hatch_open_duration_variance))

        data.write(b'\x9cBS%')  # 0x9c425325
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.next_empty_hatch_open_time))

        data.write(b'\xfa"\x83j')  # 0xfa22836a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.next_empty_hatch_open_variance))

        data.write(b'\xedA\x04I')  # 0xed410449
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.missile_hatch_open_duration))

        data.write(b'\xf7h\xd6%')  # 0xf768d625
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.missile_hatch_open_duration_variance))

        data.write(b'\xa2)\xffj')  # 0xa229ff6a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.tentacle_animation_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'R\x80n\xff')  # 0x52806eff
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.num_missile_hatches))

        data.write(b'.\xa3\x1f\x83')  # 0x2ea31f83
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.missile_weapon))

        data.write(b'%\x8c\xfbM')  # 0x258cfb4d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.missile_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'{\xec\xdbf')  # 0x7becdb66
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.missile_explode_threshold))

        data.write(b'\x87\xaf\xe8\xd8')  # 0x87afe8d8
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.missile_expode_effect))

        data.write(b'=\xfd\x1cO')  # 0x3dfd1c4f
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.missile_explode_sound))

        data.write(b'\xb8\xbfV\x1e')  # 0xb8bf561e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fire_missile_time))

        data.write(b'\xa4\x16n<')  # 0xa4166e3c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.next_fire_missile_time))

        data.write(b'\xaa}R}')  # 0xaa7d527d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xaa7d527d))

        data.write(b'\xf7\x07\xc0P')  # 0xf707c050
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.initial_camera_hatch_open_time))

        data.write(b'A(\xffm')  # 0x4128ff6d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.inital_camera_hatch_open_variance))

        data.write(b';b\x18\xda')  # 0x3b6218da
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.camera_hatch_open_duration))

        data.write(b'q\x94n\xec')  # 0x71946eec
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.camera_hatch_open_duration_variance))

        data.write(b'\xa1\x84\xd0\x13')  # 0xa184d013
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.next_camera_hatch_open_time))

        data.write(b'\t\xd9\xbd\x17')  # 0x9d9bd17
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.next_camera_hatch_open_variance))

        data.write(b'S\xc1\xd0\x89')  # 0x53c1d089
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.camera_sequence_duration))

        data.write(b'0o\xd3\x9a')  # 0x306fd39a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.min_camera_sequences))

        data.write(b'#*51')  # 0x232a3531
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_camera_sequences))

        data.write(b'\x19<wQ')  # 0x193c7751
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.next_camera_sequence_time))

        data.write(b'\rUyJ')  # 0xd55794a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.next_camera_sequence_variance))

        data.write(b'r\xfbg\xda')  # 0x72fb67da
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x72fb67da))

        data.write(b'\xbd\xb1\x8b/')  # 0xbdb18b2f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.camera_damage_threshold))

        data.write(b'\x0e\x95\x8d\x9e')  # 0xe958d9e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.camera_shock_time))

        data.write(b'%\x1cU\xe3')  # 0x251c55e3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dizzy_state_time))

        data.write(b'\n\x07,H')  # 0xa072c48
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stage2_health_percent))

        data.write(b'\xdd\xe5\xac\x10')  # 0xdde5ac10
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stage3_health_percent))

        data.write(b'\x8cc\xf9\xd0')  # 0x8c63f9d0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x8c63f9d0))

        data.write(b'k~_G')  # 0x6b7e5f47
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6b7e5f47))

        data.write(b'j\xfe\x01G')  # 0x6afe0147
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6afe0147))

        data.write(b'\x04r\x1a\x06')  # 0x4721a06
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x04721a06))

        if self.unknown_struct6 != default_override.get('unknown_struct6', UnknownStruct6()):
            num_properties_written += 1
            data.write(b'\xd8W\x9b\xa3')  # 0xd8579ba3
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            self.unknown_struct6.to_stream(data, game)
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if num_properties_written != 42:
            struct_end_offset = data.tell()
            data.seek(num_properties_offset)
            data.write(struct.pack(">H", num_properties_written))
            data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("AuroraUnitCombatHatchesJson", data)
        return cls(
            camera_animation_info=AnimationParameters.from_json(json_data['camera_animation_info']),
            overload_damage_threshold=json_data['overload_damage_threshold'],
            open_hatch_vulnerability=DamageVulnerability.from_json(json_data['open_hatch_vulnerability']),
            empty_hatch_open_duration=json_data['empty_hatch_open_duration'],
            empty_hatch_open_duration_variance=json_data['empty_hatch_open_duration_variance'],
            missile_destroyed_empty_hatch_open_duration=json_data['missile_destroyed_empty_hatch_open_duration'],
            missile_destroyed_empty_hatch_open_duration_variance=json_data['missile_destroyed_empty_hatch_open_duration_variance'],
            next_empty_hatch_open_time=json_data['next_empty_hatch_open_time'],
            next_empty_hatch_open_variance=json_data['next_empty_hatch_open_variance'],
            missile_hatch_open_duration=json_data['missile_hatch_open_duration'],
            missile_hatch_open_duration_variance=json_data['missile_hatch_open_duration_variance'],
            tentacle_animation_info=AnimationParameters.from_json(json_data['tentacle_animation_info']),
            num_missile_hatches=json_data['num_missile_hatches'],
            missile_weapon=json_data['missile_weapon'],
            missile_damage=DamageInfo.from_json(json_data['missile_damage']),
            missile_explode_threshold=json_data['missile_explode_threshold'],
            missile_expode_effect=json_data['missile_expode_effect'],
            missile_explode_sound=json_data['missile_explode_sound'],
            fire_missile_time=json_data['fire_missile_time'],
            next_fire_missile_time=json_data['next_fire_missile_time'],
            unknown_0xaa7d527d=json_data['unknown_0xaa7d527d'],
            initial_camera_hatch_open_time=json_data['initial_camera_hatch_open_time'],
            inital_camera_hatch_open_variance=json_data['inital_camera_hatch_open_variance'],
            camera_hatch_open_duration=json_data['camera_hatch_open_duration'],
            camera_hatch_open_duration_variance=json_data['camera_hatch_open_duration_variance'],
            next_camera_hatch_open_time=json_data['next_camera_hatch_open_time'],
            next_camera_hatch_open_variance=json_data['next_camera_hatch_open_variance'],
            camera_sequence_duration=json_data['camera_sequence_duration'],
            min_camera_sequences=json_data['min_camera_sequences'],
            max_camera_sequences=json_data['max_camera_sequences'],
            next_camera_sequence_time=json_data['next_camera_sequence_time'],
            next_camera_sequence_variance=json_data['next_camera_sequence_variance'],
            unknown_0x72fb67da=json_data['unknown_0x72fb67da'],
            camera_damage_threshold=json_data['camera_damage_threshold'],
            camera_shock_time=json_data['camera_shock_time'],
            dizzy_state_time=json_data['dizzy_state_time'],
            stage2_health_percent=json_data['stage2_health_percent'],
            stage3_health_percent=json_data['stage3_health_percent'],
            unknown_0x8c63f9d0=json_data['unknown_0x8c63f9d0'],
            unknown_0x6b7e5f47=json_data['unknown_0x6b7e5f47'],
            unknown_0x6afe0147=json_data['unknown_0x6afe0147'],
            unknown_0x04721a06=json_data['unknown_0x04721a06'],
            unknown_struct6=UnknownStruct6.from_json(json_data['unknown_struct6']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'camera_animation_info': self.camera_animation_info.to_json(),
            'overload_damage_threshold': self.overload_damage_threshold,
            'open_hatch_vulnerability': self.open_hatch_vulnerability.to_json(),
            'empty_hatch_open_duration': self.empty_hatch_open_duration,
            'empty_hatch_open_duration_variance': self.empty_hatch_open_duration_variance,
            'missile_destroyed_empty_hatch_open_duration': self.missile_destroyed_empty_hatch_open_duration,
            'missile_destroyed_empty_hatch_open_duration_variance': self.missile_destroyed_empty_hatch_open_duration_variance,
            'next_empty_hatch_open_time': self.next_empty_hatch_open_time,
            'next_empty_hatch_open_variance': self.next_empty_hatch_open_variance,
            'missile_hatch_open_duration': self.missile_hatch_open_duration,
            'missile_hatch_open_duration_variance': self.missile_hatch_open_duration_variance,
            'tentacle_animation_info': self.tentacle_animation_info.to_json(),
            'num_missile_hatches': self.num_missile_hatches,
            'missile_weapon': self.missile_weapon,
            'missile_damage': self.missile_damage.to_json(),
            'missile_explode_threshold': self.missile_explode_threshold,
            'missile_expode_effect': self.missile_expode_effect,
            'missile_explode_sound': self.missile_explode_sound,
            'fire_missile_time': self.fire_missile_time,
            'next_fire_missile_time': self.next_fire_missile_time,
            'unknown_0xaa7d527d': self.unknown_0xaa7d527d,
            'initial_camera_hatch_open_time': self.initial_camera_hatch_open_time,
            'inital_camera_hatch_open_variance': self.inital_camera_hatch_open_variance,
            'camera_hatch_open_duration': self.camera_hatch_open_duration,
            'camera_hatch_open_duration_variance': self.camera_hatch_open_duration_variance,
            'next_camera_hatch_open_time': self.next_camera_hatch_open_time,
            'next_camera_hatch_open_variance': self.next_camera_hatch_open_variance,
            'camera_sequence_duration': self.camera_sequence_duration,
            'min_camera_sequences': self.min_camera_sequences,
            'max_camera_sequences': self.max_camera_sequences,
            'next_camera_sequence_time': self.next_camera_sequence_time,
            'next_camera_sequence_variance': self.next_camera_sequence_variance,
            'unknown_0x72fb67da': self.unknown_0x72fb67da,
            'camera_damage_threshold': self.camera_damage_threshold,
            'camera_shock_time': self.camera_shock_time,
            'dizzy_state_time': self.dizzy_state_time,
            'stage2_health_percent': self.stage2_health_percent,
            'stage3_health_percent': self.stage3_health_percent,
            'unknown_0x8c63f9d0': self.unknown_0x8c63f9d0,
            'unknown_0x6b7e5f47': self.unknown_0x6b7e5f47,
            'unknown_0x6afe0147': self.unknown_0x6afe0147,
            'unknown_0x04721a06': self.unknown_0x04721a06,
            'unknown_struct6': self.unknown_struct6.to_json(),
        }

    def _dependencies_for_missile_weapon(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.missile_weapon)

    def _dependencies_for_missile_expode_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.missile_expode_effect)

    def _dependencies_for_missile_explode_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.missile_explode_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.camera_animation_info.dependencies_for, "camera_animation_info", "AnimationParameters"),
            (self.tentacle_animation_info.dependencies_for, "tentacle_animation_info", "AnimationParameters"),
            (self._dependencies_for_missile_weapon, "missile_weapon", "AssetId"),
            (self._dependencies_for_missile_expode_effect, "missile_expode_effect", "AssetId"),
            (self._dependencies_for_missile_explode_sound, "missile_explode_sound", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for AuroraUnitCombatHatches.{field_name} ({field_type}): {e}"
                )


def _decode_camera_animation_info(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_open_hatch_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_tentacle_animation_info(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_missile_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_unknown_struct6(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct6:
    return UnknownStruct6.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xc107a48a: ('camera_animation_info', _decode_camera_animation_info),
    0xa6c47cd3: ('overload_damage_threshold', structs.decode_BIG_f),
    0x0fce03ca: ('open_hatch_vulnerability', _decode_open_hatch_vulnerability),
    0xa4b62aa9: ('empty_hatch_open_duration', structs.decode_BIG_f),
    0xb64ea21c: ('empty_hatch_open_duration_variance', structs.decode_BIG_f),
    0xa13b1ba9: ('missile_destroyed_empty_hatch_open_duration', structs.decode_BIG_f),
    0xd294848c: ('missile_destroyed_empty_hatch_open_duration_variance', structs.decode_BIG_f),
    0x9c425325: ('next_empty_hatch_open_time', structs.decode_BIG_f),
    0xfa22836a: ('next_empty_hatch_open_variance', structs.decode_BIG_f),
    0xed410449: ('missile_hatch_open_duration', structs.decode_BIG_f),
    0xf768d625: ('missile_hatch_open_duration_variance', structs.decode_BIG_f),
    0xa229ff6a: ('tentacle_animation_info', _decode_tentacle_animation_info),
    0x52806eff: ('num_missile_hatches', structs.decode_BIG_l),
    0x2ea31f83: ('missile_weapon', structs.decode_BIG_Q),
    0x258cfb4d: ('missile_damage', _decode_missile_damage),
    0x7becdb66: ('missile_explode_threshold', structs.decode_BIG_f),
    0x87afe8d8: ('missile_expode_effect', structs.decode_BIG_Q),
    0x3dfd1c4f: ('missile_explode_sound', structs.decode_BIG_Q),
    0xb8bf561e: ('fire_missile_time', structs.decode_BIG_f),
    0xa4166e3c: ('next_fire_missile_time', structs.decode_BIG_f),
    0xaa7d527d: ('unknown_0xaa7d527d', structs.decode_BIG_f),
    0xf707c050: ('initial_camera_hatch_open_time', structs.decode_BIG_f),
    0x4128ff6d: ('inital_camera_hatch_open_variance', structs.decode_BIG_f),
    0x3b6218da: ('camera_hatch_open_duration', structs.decode_BIG_f),
    0x71946eec: ('camera_hatch_open_duration_variance', structs.decode_BIG_f),
    0xa184d013: ('next_camera_hatch_open_time', structs.decode_BIG_f),
    0x09d9bd17: ('next_camera_hatch_open_variance', structs.decode_BIG_f),
    0x53c1d089: ('camera_sequence_duration', structs.decode_BIG_f),
    0x306fd39a: ('min_camera_sequences', structs.decode_BIG_l),
    0x232a3531: ('max_camera_sequences', structs.decode_BIG_l),
    0x193c7751: ('next_camera_sequence_time', structs.decode_BIG_f),
    0x0d55794a: ('next_camera_sequence_variance', structs.decode_BIG_f),
    0x72fb67da: ('unknown_0x72fb67da', structs.decode_BIG_f),
    0xbdb18b2f: ('camera_damage_threshold', structs.decode_BIG_f),
    0x0e958d9e: ('camera_shock_time', structs.decode_BIG_f),
    0x251c55e3: ('dizzy_state_time', structs.decode_BIG_f),
    0x0a072c48: ('stage2_health_percent', structs.decode_BIG_f),
    0xdde5ac10: ('stage3_health_percent', structs.decode_BIG_f),
    0x8c63f9d0: ('unknown_0x8c63f9d0', structs.decode_BIG_f),
    0x6b7e5f47: ('unknown_0x6b7e5f47', structs.decode_BIG_f),
    0x6afe0147: ('unknown_0x6afe0147', structs.decode_BIG_f),
    0x04721a06: ('unknown_0x04721a06', structs.decode_BIG_f),
    0xd8579ba3: ('unknown_struct6', _decode_unknown_struct6),
}
