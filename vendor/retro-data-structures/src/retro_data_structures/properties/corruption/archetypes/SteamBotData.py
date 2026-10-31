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
from retro_data_structures.properties.corruption.archetypes.HoverThenHomeProjectile import HoverThenHomeProjectile
from retro_data_structures.properties.corruption.archetypes.HyperModeData import HyperModeData
from retro_data_structures.properties.corruption.archetypes.LaunchProjectileData import LaunchProjectileData
from retro_data_structures.properties.corruption.archetypes.ModIncaData import ModIncaData
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.spline import Spline
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SteamBotDataJson(typing_extensions.TypedDict):
        falling_apart_anim: json_util.JsonObject
        march_distance_max: float
        march_distance_min: float
        march_turn_threshold: float
        rocket: json_util.JsonObject
        rocket_range_max: float
        rocket_range_min: float
        stop_rocket_homing_range: float
        rocket_collision_box: json_util.JsonValue
        rocket_hit_points: float
        rocket_hover_then_home: json_util.JsonObject
        ray_gun: json_util.JsonObject
        ray_gun_delay_variance_max: float
        ray_gun_delay_variance_min: float
        ray_gun_range_max: float
        ray_gun_range_min: float
        ray_gun_shot_prediction: float
        ray_gun_richochets: int
        claw_damage: json_util.JsonObject
        claw_range_max: float
        claw_range_min: float
        claw_delay: float
        steam_blast: json_util.JsonObject
        steam_texture: int
        steam_alpha: float
        steam_fade_in: float
        steam_fade_out: float
        steam_blast_damage_range: float
        steam_blast_range_max: float
        steam_blast_range_min: float
        steam_blast_damage_delay: float
        melt_time_max: float
        melt_time_min: float
        melt_speed_max: float
        melt_speed_min: float
        xy_scale: json_util.JsonObject
        z_scale: json_util.JsonObject
        model_alpha: json_util.JsonObject
        model_red: json_util.JsonObject
        model_green: json_util.JsonObject
        model_blue: json_util.JsonObject
        effects_alpha: json_util.JsonObject
        recheck_path_time: float
        recheck_path_distance: float
        avoidance_range: float
        scan_delay: float
        wake_up_delay_max: float
        wake_up_delay_min: float
        go_dormant: bool
        start_in_pieces: bool
        hyper_mode_burst_shots_max: int
        hyper_mode_burst_shots_min: int
        hyper_mode_burst_delay_max: float
        hyper_mode_burst_delay_min: float
        use_hyper_mode_timers: bool
        hyper_mode: json_util.JsonObject
        hyper_mode_hard: json_util.JsonObject
        hyper_mode_elite: json_util.JsonObject
        hurl_lerp: float
        hurl_knock_back_multiplier: float
        hurl_knock_back_resistance: float
        unknown_0x6cf3636f: float
        unknown_0x85d4691c: bool
        mod_inca_data: json_util.JsonObject
    

@dataclasses.dataclass()
class SteamBotData(BaseProperty):
    falling_apart_anim: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0xbe5e86b9, original_name='FallingApartAnim', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    march_distance_max: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf4f4a01d, original_name='MarchDistanceMax'
        ),
    })
    march_distance_min: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x12940ffc, original_name='MarchDistanceMin'
        ),
    })
    march_turn_threshold: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x303b4954, original_name='MarchTurnThreshold'
        ),
    })
    rocket: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0xab247451, original_name='Rocket', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    rocket_range_max: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x55c19435, original_name='RocketRangeMax'
        ),
    })
    rocket_range_min: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb3a13bd4, original_name='RocketRangeMin'
        ),
    })
    stop_rocket_homing_range: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0588c742, original_name='StopRocketHomingRange'
        ),
    })
    rocket_collision_box: Vector = dataclasses.field(default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x15793154, original_name='RocketCollisionBox', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    rocket_hit_points: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe8fc0acd, original_name='RocketHitPoints'
        ),
    })
    rocket_hover_then_home: HoverThenHomeProjectile = dataclasses.field(default_factory=HoverThenHomeProjectile, metadata={
        'reflection': FieldReflection[HoverThenHomeProjectile](
            HoverThenHomeProjectile, id=0x7039fb9f, original_name='RocketHoverThenHome', from_json=HoverThenHomeProjectile.from_json, to_json=HoverThenHomeProjectile.to_json
        ),
    })
    ray_gun: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0xb98cba47, original_name='RayGun', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    ray_gun_delay_variance_max: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdde5dccd, original_name='RayGunDelayVarianceMax'
        ),
    })
    ray_gun_delay_variance_min: float = dataclasses.field(default=0.014999999664723873, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3b85732c, original_name='RayGunDelayVarianceMin'
        ),
    })
    ray_gun_range_max: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x296b1195, original_name='RayGunRangeMax'
        ),
    })
    ray_gun_range_min: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcf0bbe74, original_name='RayGunRangeMin'
        ),
    })
    ray_gun_shot_prediction: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa0d2af02, original_name='RayGunShotPrediction'
        ),
    })
    ray_gun_richochets: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0xd7b53cdb, original_name='RayGunRichochets'
        ),
    })
    claw_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x8dbaeef2, original_name='ClawDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    claw_range_max: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x582b9b3b, original_name='ClawRangeMax'
        ),
    })
    claw_range_min: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbe4b34da, original_name='ClawRangeMin'
        ),
    })
    claw_delay: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xebb134b5, original_name='ClawDelay'
        ),
    })
    steam_blast: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0xca91ecb0, original_name='SteamBlast', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    steam_texture: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['TXTR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x58a21824, original_name='SteamTexture'
        ),
    })
    steam_alpha: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6c692453, original_name='SteamAlpha'
        ),
    })
    steam_fade_in: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x66a5cd17, original_name='SteamFadeIn'
        ),
    })
    steam_fade_out: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5c5b8b5d, original_name='SteamFadeOut'
        ),
    })
    steam_blast_damage_range: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa296206a, original_name='SteamBlastDamageRange'
        ),
    })
    steam_blast_range_max: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x10c7fd02, original_name='SteamBlastRangeMax'
        ),
    })
    steam_blast_range_min: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf6a752e3, original_name='SteamBlastRangeMin'
        ),
    })
    steam_blast_damage_delay: float = dataclasses.field(default=0.05000000074505806, metadata={
        'reflection': FieldReflection[float](
            float, id=0x802b706e, original_name='SteamBlastDamageDelay'
        ),
    })
    melt_time_max: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc80ac7db, original_name='MeltTimeMax'
        ),
    })
    melt_time_min: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2e6a683a, original_name='MeltTimeMin'
        ),
    })
    melt_speed_max: float = dataclasses.field(default=1.100000023841858, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3e9f0188, original_name='MeltSpeedMax'
        ),
    })
    melt_speed_min: float = dataclasses.field(default=0.8999999761581421, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd8ffae69, original_name='MeltSpeedMin'
        ),
    })
    xy_scale: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x48ba8eb1, original_name='XYScale', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    z_scale: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x180c38b0, original_name='ZScale', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    model_alpha: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x0f762790, original_name='ModelAlpha', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    model_red: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x0feadc99, original_name='ModelRed', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    model_green: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x55be3e8e, original_name='ModelGreen', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    model_blue: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x79f7cc48, original_name='ModelBlue', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    effects_alpha: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x564bd8cd, original_name='EffectsAlpha', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    recheck_path_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9aa90b6b, original_name='RecheckPathTime'
        ),
    })
    recheck_path_distance: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7626ec89, original_name='RecheckPathDistance'
        ),
    })
    avoidance_range: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x50a9bd0d, original_name='AvoidanceRange'
        ),
    })
    scan_delay: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7fc827a2, original_name='ScanDelay'
        ),
    })
    wake_up_delay_max: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x699da662, original_name='WakeUpDelayMax'
        ),
    })
    wake_up_delay_min: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8ffd0983, original_name='WakeUpDelayMin'
        ),
    })
    go_dormant: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xdedd30a4, original_name='GoDormant'
        ),
    })
    start_in_pieces: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xf8243d17, original_name='StartInPieces'
        ),
    })
    hyper_mode_burst_shots_max: int = dataclasses.field(default=5, metadata={
        'reflection': FieldReflection[int](
            int, id=0xc6943950, original_name='HyperModeBurstShotsMax'
        ),
    })
    hyper_mode_burst_shots_min: int = dataclasses.field(default=4, metadata={
        'reflection': FieldReflection[int](
            int, id=0x83967ad2, original_name='HyperModeBurstShotsMin'
        ),
    })
    hyper_mode_burst_delay_max: float = dataclasses.field(default=2.0999999046325684, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6c8ae89f, original_name='HyperModeBurstDelayMax'
        ),
    })
    hyper_mode_burst_delay_min: float = dataclasses.field(default=1.899999976158142, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8aea477e, original_name='HyperModeBurstDelayMin'
        ),
    })
    use_hyper_mode_timers: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x5f1a7dd8, original_name='UseHyperModeTimers'
        ),
    })
    hyper_mode: HyperModeData = dataclasses.field(default_factory=HyperModeData, metadata={
        'reflection': FieldReflection[HyperModeData](
            HyperModeData, id=0xb0a9b728, original_name='HyperMode', from_json=HyperModeData.from_json, to_json=HyperModeData.to_json
        ),
    })
    hyper_mode_hard: HyperModeData = dataclasses.field(default_factory=HyperModeData, metadata={
        'reflection': FieldReflection[HyperModeData](
            HyperModeData, id=0x14499fcb, original_name='HyperModeHard', from_json=HyperModeData.from_json, to_json=HyperModeData.to_json
        ),
    })
    hyper_mode_elite: HyperModeData = dataclasses.field(default_factory=HyperModeData, metadata={
        'reflection': FieldReflection[HyperModeData](
            HyperModeData, id=0xcd02221c, original_name='HyperModeElite', from_json=HyperModeData.from_json, to_json=HyperModeData.to_json
        ),
    })
    hurl_lerp: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x19863914, original_name='HurlLerp'
        ),
    })
    hurl_knock_back_multiplier: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x04ab182a, original_name='HurlKnockBackMultiplier'
        ),
    })
    hurl_knock_back_resistance: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb008320b, original_name='HurlKnockBackResistance'
        ),
    })
    unknown_0x6cf3636f: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6cf3636f, original_name='Unknown'
        ),
    })
    unknown_0x85d4691c: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x85d4691c, original_name='Unknown'
        ),
    })
    mod_inca_data: ModIncaData = dataclasses.field(default_factory=ModIncaData, metadata={
        'reflection': FieldReflection[ModIncaData](
            ModIncaData, id=0xb4c02854, original_name='ModIncaData', from_json=ModIncaData.from_json, to_json=ModIncaData.to_json
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
        if property_count != 64:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbe5e86b9
        falling_apart_anim = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf4f4a01d
        march_distance_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x12940ffc
        march_distance_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x303b4954
        march_turn_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xab247451
        rocket = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x55c19435
        rocket_range_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3a13bd4
        rocket_range_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0588c742
        stop_rocket_homing_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x15793154
        rocket_collision_box = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe8fc0acd
        rocket_hit_points = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7039fb9f
        rocket_hover_then_home = HoverThenHomeProjectile.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb98cba47
        ray_gun = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdde5dccd
        ray_gun_delay_variance_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3b85732c
        ray_gun_delay_variance_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x296b1195
        ray_gun_range_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcf0bbe74
        ray_gun_range_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa0d2af02
        ray_gun_shot_prediction = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd7b53cdb
        ray_gun_richochets = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8dbaeef2
        claw_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x582b9b3b
        claw_range_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbe4b34da
        claw_range_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xebb134b5
        claw_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xca91ecb0
        steam_blast = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58a21824
        steam_texture = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6c692453
        steam_alpha = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x66a5cd17
        steam_fade_in = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5c5b8b5d
        steam_fade_out = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa296206a
        steam_blast_damage_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x10c7fd02
        steam_blast_range_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf6a752e3
        steam_blast_range_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x802b706e
        steam_blast_damage_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc80ac7db
        melt_time_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2e6a683a
        melt_time_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3e9f0188
        melt_speed_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd8ffae69
        melt_speed_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x48ba8eb1
        xy_scale = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x180c38b0
        z_scale = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0f762790
        model_alpha = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0feadc99
        model_red = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x55be3e8e
        model_green = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x79f7cc48
        model_blue = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x564bd8cd
        effects_alpha = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9aa90b6b
        recheck_path_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7626ec89
        recheck_path_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50a9bd0d
        avoidance_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7fc827a2
        scan_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x699da662
        wake_up_delay_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8ffd0983
        wake_up_delay_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdedd30a4
        go_dormant = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf8243d17
        start_in_pieces = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc6943950
        hyper_mode_burst_shots_max = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x83967ad2
        hyper_mode_burst_shots_min = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6c8ae89f
        hyper_mode_burst_delay_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8aea477e
        hyper_mode_burst_delay_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5f1a7dd8
        use_hyper_mode_timers = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb0a9b728
        hyper_mode = HyperModeData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x14499fcb
        hyper_mode_hard = HyperModeData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcd02221c
        hyper_mode_elite = HyperModeData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19863914
        hurl_lerp = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x04ab182a
        hurl_knock_back_multiplier = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb008320b
        hurl_knock_back_resistance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6cf3636f
        unknown_0x6cf3636f = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x85d4691c
        unknown_0x85d4691c = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb4c02854
        mod_inca_data = ModIncaData.from_stream(data, game, property_size)
    
        return cls(falling_apart_anim, march_distance_max, march_distance_min, march_turn_threshold, rocket, rocket_range_max, rocket_range_min, stop_rocket_homing_range, rocket_collision_box, rocket_hit_points, rocket_hover_then_home, ray_gun, ray_gun_delay_variance_max, ray_gun_delay_variance_min, ray_gun_range_max, ray_gun_range_min, ray_gun_shot_prediction, ray_gun_richochets, claw_damage, claw_range_max, claw_range_min, claw_delay, steam_blast, steam_texture, steam_alpha, steam_fade_in, steam_fade_out, steam_blast_damage_range, steam_blast_range_max, steam_blast_range_min, steam_blast_damage_delay, melt_time_max, melt_time_min, melt_speed_max, melt_speed_min, xy_scale, z_scale, model_alpha, model_red, model_green, model_blue, effects_alpha, recheck_path_time, recheck_path_distance, avoidance_range, scan_delay, wake_up_delay_max, wake_up_delay_min, go_dormant, start_in_pieces, hyper_mode_burst_shots_max, hyper_mode_burst_shots_min, hyper_mode_burst_delay_max, hyper_mode_burst_delay_min, use_hyper_mode_timers, hyper_mode, hyper_mode_hard, hyper_mode_elite, hurl_lerp, hurl_knock_back_multiplier, hurl_knock_back_resistance, unknown_0x6cf3636f, unknown_0x85d4691c, mod_inca_data)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00@')  # 64 properties

        data.write(b'\xbe^\x86\xb9')  # 0xbe5e86b9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.falling_apart_anim.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf4\xf4\xa0\x1d')  # 0xf4f4a01d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.march_distance_max))

        data.write(b'\x12\x94\x0f\xfc')  # 0x12940ffc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.march_distance_min))

        data.write(b'0;IT')  # 0x303b4954
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.march_turn_threshold))

        data.write(b'\xab$tQ')  # 0xab247451
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.rocket.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'U\xc1\x945')  # 0x55c19435
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rocket_range_max))

        data.write(b'\xb3\xa1;\xd4')  # 0xb3a13bd4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rocket_range_min))

        data.write(b'\x05\x88\xc7B')  # 0x588c742
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stop_rocket_homing_range))

        data.write(b'\x15y1T')  # 0x15793154
        data.write(b'\x00\x0c')  # size
        self.rocket_collision_box.to_stream(data, game)

        data.write(b'\xe8\xfc\n\xcd')  # 0xe8fc0acd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rocket_hit_points))

        data.write(b'p9\xfb\x9f')  # 0x7039fb9f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.rocket_hover_then_home.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb9\x8c\xbaG')  # 0xb98cba47
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ray_gun.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xdd\xe5\xdc\xcd')  # 0xdde5dccd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ray_gun_delay_variance_max))

        data.write(b';\x85s,')  # 0x3b85732c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ray_gun_delay_variance_min))

        data.write(b')k\x11\x95')  # 0x296b1195
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ray_gun_range_max))

        data.write(b'\xcf\x0b\xbet')  # 0xcf0bbe74
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ray_gun_range_min))

        data.write(b'\xa0\xd2\xaf\x02')  # 0xa0d2af02
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ray_gun_shot_prediction))

        data.write(b'\xd7\xb5<\xdb')  # 0xd7b53cdb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.ray_gun_richochets))

        data.write(b'\x8d\xba\xee\xf2')  # 0x8dbaeef2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.claw_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'X+\x9b;')  # 0x582b9b3b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.claw_range_max))

        data.write(b'\xbeK4\xda')  # 0xbe4b34da
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.claw_range_min))

        data.write(b'\xeb\xb14\xb5')  # 0xebb134b5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.claw_delay))

        data.write(b'\xca\x91\xec\xb0')  # 0xca91ecb0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.steam_blast.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'X\xa2\x18$')  # 0x58a21824
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.steam_texture))

        data.write(b'li$S')  # 0x6c692453
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.steam_alpha))

        data.write(b'f\xa5\xcd\x17')  # 0x66a5cd17
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.steam_fade_in))

        data.write(b'\\[\x8b]')  # 0x5c5b8b5d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.steam_fade_out))

        data.write(b'\xa2\x96 j')  # 0xa296206a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.steam_blast_damage_range))

        data.write(b'\x10\xc7\xfd\x02')  # 0x10c7fd02
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.steam_blast_range_max))

        data.write(b'\xf6\xa7R\xe3')  # 0xf6a752e3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.steam_blast_range_min))

        data.write(b'\x80+pn')  # 0x802b706e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.steam_blast_damage_delay))

        data.write(b'\xc8\n\xc7\xdb')  # 0xc80ac7db
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.melt_time_max))

        data.write(b'.jh:')  # 0x2e6a683a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.melt_time_min))

        data.write(b'>\x9f\x01\x88')  # 0x3e9f0188
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.melt_speed_max))

        data.write(b'\xd8\xff\xaei')  # 0xd8ffae69
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.melt_speed_min))

        data.write(b'H\xba\x8e\xb1')  # 0x48ba8eb1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.xy_scale.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x18\x0c8\xb0')  # 0x180c38b0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.z_scale.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b"\x0fv'\x90")  # 0xf762790
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.model_alpha.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x0f\xea\xdc\x99')  # 0xfeadc99
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.model_red.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'U\xbe>\x8e')  # 0x55be3e8e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.model_green.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'y\xf7\xccH')  # 0x79f7cc48
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.model_blue.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'VK\xd8\xcd')  # 0x564bd8cd
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.effects_alpha.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9a\xa9\x0bk')  # 0x9aa90b6b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.recheck_path_time))

        data.write(b'v&\xec\x89')  # 0x7626ec89
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.recheck_path_distance))

        data.write(b'P\xa9\xbd\r')  # 0x50a9bd0d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.avoidance_range))

        data.write(b"\x7f\xc8'\xa2")  # 0x7fc827a2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_delay))

        data.write(b'i\x9d\xa6b')  # 0x699da662
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.wake_up_delay_max))

        data.write(b'\x8f\xfd\t\x83')  # 0x8ffd0983
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.wake_up_delay_min))

        data.write(b'\xde\xdd0\xa4')  # 0xdedd30a4
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.go_dormant))

        data.write(b'\xf8$=\x17')  # 0xf8243d17
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.start_in_pieces))

        data.write(b'\xc6\x949P')  # 0xc6943950
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.hyper_mode_burst_shots_max))

        data.write(b'\x83\x96z\xd2')  # 0x83967ad2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.hyper_mode_burst_shots_min))

        data.write(b'l\x8a\xe8\x9f')  # 0x6c8ae89f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_burst_delay_max))

        data.write(b'\x8a\xeaG~')  # 0x8aea477e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_burst_delay_min))

        data.write(b'_\x1a}\xd8')  # 0x5f1a7dd8
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.use_hyper_mode_timers))

        data.write(b'\xb0\xa9\xb7(')  # 0xb0a9b728
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper_mode.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x14I\x9f\xcb')  # 0x14499fcb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper_mode_hard.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xcd\x02"\x1c')  # 0xcd02221c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper_mode_elite.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x19\x869\x14')  # 0x19863914
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hurl_lerp))

        data.write(b'\x04\xab\x18*')  # 0x4ab182a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hurl_knock_back_multiplier))

        data.write(b'\xb0\x082\x0b')  # 0xb008320b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hurl_knock_back_resistance))

        data.write(b'l\xf3co')  # 0x6cf3636f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x6cf3636f))

        data.write(b'\x85\xd4i\x1c')  # 0x85d4691c
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x85d4691c))

        data.write(b'\xb4\xc0(T')  # 0xb4c02854
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.mod_inca_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SteamBotDataJson", data)
        return cls(
            falling_apart_anim=AnimationParameters.from_json(json_data['falling_apart_anim']),
            march_distance_max=json_data['march_distance_max'],
            march_distance_min=json_data['march_distance_min'],
            march_turn_threshold=json_data['march_turn_threshold'],
            rocket=LaunchProjectileData.from_json(json_data['rocket']),
            rocket_range_max=json_data['rocket_range_max'],
            rocket_range_min=json_data['rocket_range_min'],
            stop_rocket_homing_range=json_data['stop_rocket_homing_range'],
            rocket_collision_box=Vector.from_json(json_data['rocket_collision_box']),
            rocket_hit_points=json_data['rocket_hit_points'],
            rocket_hover_then_home=HoverThenHomeProjectile.from_json(json_data['rocket_hover_then_home']),
            ray_gun=LaunchProjectileData.from_json(json_data['ray_gun']),
            ray_gun_delay_variance_max=json_data['ray_gun_delay_variance_max'],
            ray_gun_delay_variance_min=json_data['ray_gun_delay_variance_min'],
            ray_gun_range_max=json_data['ray_gun_range_max'],
            ray_gun_range_min=json_data['ray_gun_range_min'],
            ray_gun_shot_prediction=json_data['ray_gun_shot_prediction'],
            ray_gun_richochets=json_data['ray_gun_richochets'],
            claw_damage=DamageInfo.from_json(json_data['claw_damage']),
            claw_range_max=json_data['claw_range_max'],
            claw_range_min=json_data['claw_range_min'],
            claw_delay=json_data['claw_delay'],
            steam_blast=LaunchProjectileData.from_json(json_data['steam_blast']),
            steam_texture=json_data['steam_texture'],
            steam_alpha=json_data['steam_alpha'],
            steam_fade_in=json_data['steam_fade_in'],
            steam_fade_out=json_data['steam_fade_out'],
            steam_blast_damage_range=json_data['steam_blast_damage_range'],
            steam_blast_range_max=json_data['steam_blast_range_max'],
            steam_blast_range_min=json_data['steam_blast_range_min'],
            steam_blast_damage_delay=json_data['steam_blast_damage_delay'],
            melt_time_max=json_data['melt_time_max'],
            melt_time_min=json_data['melt_time_min'],
            melt_speed_max=json_data['melt_speed_max'],
            melt_speed_min=json_data['melt_speed_min'],
            xy_scale=Spline.from_json(json_data['xy_scale']),
            z_scale=Spline.from_json(json_data['z_scale']),
            model_alpha=Spline.from_json(json_data['model_alpha']),
            model_red=Spline.from_json(json_data['model_red']),
            model_green=Spline.from_json(json_data['model_green']),
            model_blue=Spline.from_json(json_data['model_blue']),
            effects_alpha=Spline.from_json(json_data['effects_alpha']),
            recheck_path_time=json_data['recheck_path_time'],
            recheck_path_distance=json_data['recheck_path_distance'],
            avoidance_range=json_data['avoidance_range'],
            scan_delay=json_data['scan_delay'],
            wake_up_delay_max=json_data['wake_up_delay_max'],
            wake_up_delay_min=json_data['wake_up_delay_min'],
            go_dormant=json_data['go_dormant'],
            start_in_pieces=json_data['start_in_pieces'],
            hyper_mode_burst_shots_max=json_data['hyper_mode_burst_shots_max'],
            hyper_mode_burst_shots_min=json_data['hyper_mode_burst_shots_min'],
            hyper_mode_burst_delay_max=json_data['hyper_mode_burst_delay_max'],
            hyper_mode_burst_delay_min=json_data['hyper_mode_burst_delay_min'],
            use_hyper_mode_timers=json_data['use_hyper_mode_timers'],
            hyper_mode=HyperModeData.from_json(json_data['hyper_mode']),
            hyper_mode_hard=HyperModeData.from_json(json_data['hyper_mode_hard']),
            hyper_mode_elite=HyperModeData.from_json(json_data['hyper_mode_elite']),
            hurl_lerp=json_data['hurl_lerp'],
            hurl_knock_back_multiplier=json_data['hurl_knock_back_multiplier'],
            hurl_knock_back_resistance=json_data['hurl_knock_back_resistance'],
            unknown_0x6cf3636f=json_data['unknown_0x6cf3636f'],
            unknown_0x85d4691c=json_data['unknown_0x85d4691c'],
            mod_inca_data=ModIncaData.from_json(json_data['mod_inca_data']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'falling_apart_anim': self.falling_apart_anim.to_json(),
            'march_distance_max': self.march_distance_max,
            'march_distance_min': self.march_distance_min,
            'march_turn_threshold': self.march_turn_threshold,
            'rocket': self.rocket.to_json(),
            'rocket_range_max': self.rocket_range_max,
            'rocket_range_min': self.rocket_range_min,
            'stop_rocket_homing_range': self.stop_rocket_homing_range,
            'rocket_collision_box': self.rocket_collision_box.to_json(),
            'rocket_hit_points': self.rocket_hit_points,
            'rocket_hover_then_home': self.rocket_hover_then_home.to_json(),
            'ray_gun': self.ray_gun.to_json(),
            'ray_gun_delay_variance_max': self.ray_gun_delay_variance_max,
            'ray_gun_delay_variance_min': self.ray_gun_delay_variance_min,
            'ray_gun_range_max': self.ray_gun_range_max,
            'ray_gun_range_min': self.ray_gun_range_min,
            'ray_gun_shot_prediction': self.ray_gun_shot_prediction,
            'ray_gun_richochets': self.ray_gun_richochets,
            'claw_damage': self.claw_damage.to_json(),
            'claw_range_max': self.claw_range_max,
            'claw_range_min': self.claw_range_min,
            'claw_delay': self.claw_delay,
            'steam_blast': self.steam_blast.to_json(),
            'steam_texture': self.steam_texture,
            'steam_alpha': self.steam_alpha,
            'steam_fade_in': self.steam_fade_in,
            'steam_fade_out': self.steam_fade_out,
            'steam_blast_damage_range': self.steam_blast_damage_range,
            'steam_blast_range_max': self.steam_blast_range_max,
            'steam_blast_range_min': self.steam_blast_range_min,
            'steam_blast_damage_delay': self.steam_blast_damage_delay,
            'melt_time_max': self.melt_time_max,
            'melt_time_min': self.melt_time_min,
            'melt_speed_max': self.melt_speed_max,
            'melt_speed_min': self.melt_speed_min,
            'xy_scale': self.xy_scale.to_json(),
            'z_scale': self.z_scale.to_json(),
            'model_alpha': self.model_alpha.to_json(),
            'model_red': self.model_red.to_json(),
            'model_green': self.model_green.to_json(),
            'model_blue': self.model_blue.to_json(),
            'effects_alpha': self.effects_alpha.to_json(),
            'recheck_path_time': self.recheck_path_time,
            'recheck_path_distance': self.recheck_path_distance,
            'avoidance_range': self.avoidance_range,
            'scan_delay': self.scan_delay,
            'wake_up_delay_max': self.wake_up_delay_max,
            'wake_up_delay_min': self.wake_up_delay_min,
            'go_dormant': self.go_dormant,
            'start_in_pieces': self.start_in_pieces,
            'hyper_mode_burst_shots_max': self.hyper_mode_burst_shots_max,
            'hyper_mode_burst_shots_min': self.hyper_mode_burst_shots_min,
            'hyper_mode_burst_delay_max': self.hyper_mode_burst_delay_max,
            'hyper_mode_burst_delay_min': self.hyper_mode_burst_delay_min,
            'use_hyper_mode_timers': self.use_hyper_mode_timers,
            'hyper_mode': self.hyper_mode.to_json(),
            'hyper_mode_hard': self.hyper_mode_hard.to_json(),
            'hyper_mode_elite': self.hyper_mode_elite.to_json(),
            'hurl_lerp': self.hurl_lerp,
            'hurl_knock_back_multiplier': self.hurl_knock_back_multiplier,
            'hurl_knock_back_resistance': self.hurl_knock_back_resistance,
            'unknown_0x6cf3636f': self.unknown_0x6cf3636f,
            'unknown_0x85d4691c': self.unknown_0x85d4691c,
            'mod_inca_data': self.mod_inca_data.to_json(),
        }

    def _dependencies_for_steam_texture(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.steam_texture)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.falling_apart_anim.dependencies_for, "falling_apart_anim", "AnimationParameters"),
            (self.rocket.dependencies_for, "rocket", "LaunchProjectileData"),
            (self.rocket_hover_then_home.dependencies_for, "rocket_hover_then_home", "HoverThenHomeProjectile"),
            (self.ray_gun.dependencies_for, "ray_gun", "LaunchProjectileData"),
            (self.steam_blast.dependencies_for, "steam_blast", "LaunchProjectileData"),
            (self._dependencies_for_steam_texture, "steam_texture", "AssetId"),
            (self.hyper_mode.dependencies_for, "hyper_mode", "HyperModeData"),
            (self.hyper_mode_hard.dependencies_for, "hyper_mode_hard", "HyperModeData"),
            (self.hyper_mode_elite.dependencies_for, "hyper_mode_elite", "HyperModeData"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for SteamBotData.{field_name} ({field_type}): {e}"
                )


def _decode_falling_apart_anim(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_rocket(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_rocket_collision_box(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_rocket_hover_then_home(data: typing.BinaryIO, game: Game, property_size: int) -> HoverThenHomeProjectile:
    return HoverThenHomeProjectile.from_stream(data, game, property_size)


def _decode_ray_gun(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_claw_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_steam_blast(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_xy_scale(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_z_scale(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_model_alpha(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_model_red(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_model_green(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_model_blue(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_effects_alpha(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_hyper_mode(data: typing.BinaryIO, game: Game, property_size: int) -> HyperModeData:
    return HyperModeData.from_stream(data, game, property_size)


def _decode_hyper_mode_hard(data: typing.BinaryIO, game: Game, property_size: int) -> HyperModeData:
    return HyperModeData.from_stream(data, game, property_size)


def _decode_hyper_mode_elite(data: typing.BinaryIO, game: Game, property_size: int) -> HyperModeData:
    return HyperModeData.from_stream(data, game, property_size)


def _decode_mod_inca_data(data: typing.BinaryIO, game: Game, property_size: int) -> ModIncaData:
    return ModIncaData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xbe5e86b9: ('falling_apart_anim', _decode_falling_apart_anim),
    0xf4f4a01d: ('march_distance_max', structs.decode_BIG_f),
    0x12940ffc: ('march_distance_min', structs.decode_BIG_f),
    0x303b4954: ('march_turn_threshold', structs.decode_BIG_f),
    0xab247451: ('rocket', _decode_rocket),
    0x55c19435: ('rocket_range_max', structs.decode_BIG_f),
    0xb3a13bd4: ('rocket_range_min', structs.decode_BIG_f),
    0x0588c742: ('stop_rocket_homing_range', structs.decode_BIG_f),
    0x15793154: ('rocket_collision_box', _decode_rocket_collision_box),
    0xe8fc0acd: ('rocket_hit_points', structs.decode_BIG_f),
    0x7039fb9f: ('rocket_hover_then_home', _decode_rocket_hover_then_home),
    0xb98cba47: ('ray_gun', _decode_ray_gun),
    0xdde5dccd: ('ray_gun_delay_variance_max', structs.decode_BIG_f),
    0x3b85732c: ('ray_gun_delay_variance_min', structs.decode_BIG_f),
    0x296b1195: ('ray_gun_range_max', structs.decode_BIG_f),
    0xcf0bbe74: ('ray_gun_range_min', structs.decode_BIG_f),
    0xa0d2af02: ('ray_gun_shot_prediction', structs.decode_BIG_f),
    0xd7b53cdb: ('ray_gun_richochets', structs.decode_BIG_l),
    0x8dbaeef2: ('claw_damage', _decode_claw_damage),
    0x582b9b3b: ('claw_range_max', structs.decode_BIG_f),
    0xbe4b34da: ('claw_range_min', structs.decode_BIG_f),
    0xebb134b5: ('claw_delay', structs.decode_BIG_f),
    0xca91ecb0: ('steam_blast', _decode_steam_blast),
    0x58a21824: ('steam_texture', structs.decode_BIG_Q),
    0x6c692453: ('steam_alpha', structs.decode_BIG_f),
    0x66a5cd17: ('steam_fade_in', structs.decode_BIG_f),
    0x5c5b8b5d: ('steam_fade_out', structs.decode_BIG_f),
    0xa296206a: ('steam_blast_damage_range', structs.decode_BIG_f),
    0x10c7fd02: ('steam_blast_range_max', structs.decode_BIG_f),
    0xf6a752e3: ('steam_blast_range_min', structs.decode_BIG_f),
    0x802b706e: ('steam_blast_damage_delay', structs.decode_BIG_f),
    0xc80ac7db: ('melt_time_max', structs.decode_BIG_f),
    0x2e6a683a: ('melt_time_min', structs.decode_BIG_f),
    0x3e9f0188: ('melt_speed_max', structs.decode_BIG_f),
    0xd8ffae69: ('melt_speed_min', structs.decode_BIG_f),
    0x48ba8eb1: ('xy_scale', _decode_xy_scale),
    0x180c38b0: ('z_scale', _decode_z_scale),
    0x0f762790: ('model_alpha', _decode_model_alpha),
    0x0feadc99: ('model_red', _decode_model_red),
    0x55be3e8e: ('model_green', _decode_model_green),
    0x79f7cc48: ('model_blue', _decode_model_blue),
    0x564bd8cd: ('effects_alpha', _decode_effects_alpha),
    0x9aa90b6b: ('recheck_path_time', structs.decode_BIG_f),
    0x7626ec89: ('recheck_path_distance', structs.decode_BIG_f),
    0x50a9bd0d: ('avoidance_range', structs.decode_BIG_f),
    0x7fc827a2: ('scan_delay', structs.decode_BIG_f),
    0x699da662: ('wake_up_delay_max', structs.decode_BIG_f),
    0x8ffd0983: ('wake_up_delay_min', structs.decode_BIG_f),
    0xdedd30a4: ('go_dormant', structs.decode_BIG_bool_),
    0xf8243d17: ('start_in_pieces', structs.decode_BIG_bool_),
    0xc6943950: ('hyper_mode_burst_shots_max', structs.decode_BIG_l),
    0x83967ad2: ('hyper_mode_burst_shots_min', structs.decode_BIG_l),
    0x6c8ae89f: ('hyper_mode_burst_delay_max', structs.decode_BIG_f),
    0x8aea477e: ('hyper_mode_burst_delay_min', structs.decode_BIG_f),
    0x5f1a7dd8: ('use_hyper_mode_timers', structs.decode_BIG_bool_),
    0xb0a9b728: ('hyper_mode', _decode_hyper_mode),
    0x14499fcb: ('hyper_mode_hard', _decode_hyper_mode_hard),
    0xcd02221c: ('hyper_mode_elite', _decode_hyper_mode_elite),
    0x19863914: ('hurl_lerp', structs.decode_BIG_f),
    0x04ab182a: ('hurl_knock_back_multiplier', structs.decode_BIG_f),
    0xb008320b: ('hurl_knock_back_resistance', structs.decode_BIG_f),
    0x6cf3636f: ('unknown_0x6cf3636f', structs.decode_BIG_f),
    0x85d4691c: ('unknown_0x85d4691c', structs.decode_BIG_bool_),
    0xb4c02854: ('mod_inca_data', _decode_mod_inca_data),
}
