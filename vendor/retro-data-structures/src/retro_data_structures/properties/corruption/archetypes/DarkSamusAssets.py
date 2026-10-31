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
from retro_data_structures.properties.corruption.archetypes.HoverThenHomeProjectile import HoverThenHomeProjectile
from retro_data_structures.properties.corruption.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class DarkSamusAssetsJson(typing_extensions.TypedDict):
        unknown_0xb5049bbb: float
        unknown_0x3390e915: float
        unknown_0xf8cc3ab0: float
        unknown_0xe5c90a08: float
        unknown_0x2e95d9ad: float
        scan: int
        unknown_0x00d1aa67: int
        unknown_0xa57b4fac: int
        unknown_0x8836c426: int
        unknown_0xb87c5139: int
        unknown_0x9f566db4: int
        unknown_0xa2aac8e7: int
        unknown_0xf8aca397: int
        unknown_0x80a0b2cb: int
        unknown_0x69ed492e: int
        unknown_0x90419a55: int
        unknown_0x761db727: int
        unknown_0xdcb8af1c: int
        unknown_0x9cfddba8: int
        mega_blaster_projectile_with_collision: int
        mega_blaster_projectile_no_collision: int
        part: int
        pillar_base: int
        pillar_explosion_effect: int
        replenish_bubble_explosion: int
        phazon_barrage_beam: json_util.JsonObject
        homing_missile_projectile: int
        homing_missile_info: json_util.JsonObject
        echo_animation_information: json_util.JsonObject
        echo_explosion: int
        echo_scan: int
        energy_wave_projectile: int
        echo_blast_beam: json_util.JsonObject
        super_loop_projectile: int
        whirly_merge_effect: int
        visor_blow_out_texture: int
        visor_blow_out_max_size: float
        sound_phazon_spear_fall: int
        sound_phazon_spear_impact: int
        sound_whirly_merge_in: int
        sound_whirly_merge_out: int
        sound_shell_game_impact: int
        sound_invulnerable_loop: int
        sound_shockwave: int
    

@dataclasses.dataclass()
class DarkSamusAssets(BaseProperty):
    unknown_0xb5049bbb: float = dataclasses.field(default=80.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb5049bbb, original_name='Unknown'
        ),
    })
    unknown_0x3390e915: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3390e915, original_name='Unknown'
        ),
    })
    unknown_0xf8cc3ab0: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf8cc3ab0, original_name='Unknown'
        ),
    })
    unknown_0xe5c90a08: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe5c90a08, original_name='Unknown'
        ),
    })
    unknown_0x2e95d9ad: float = dataclasses.field(default=-1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2e95d9ad, original_name='Unknown'
        ),
    })
    scan: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SCAN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x21e4d323, original_name='SCAN'
        ),
    })
    unknown_0x00d1aa67: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x00d1aa67, original_name='Unknown'
        ),
    })
    unknown_0xa57b4fac: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xa57b4fac, original_name='Unknown'
        ),
    })
    unknown_0x8836c426: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x8836c426, original_name='Unknown'
        ),
    })
    unknown_0xb87c5139: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xb87c5139, original_name='Unknown'
        ),
    })
    unknown_0x9f566db4: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x9f566db4, original_name='Unknown'
        ),
    })
    unknown_0xa2aac8e7: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xa2aac8e7, original_name='Unknown'
        ),
    })
    unknown_0xf8aca397: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xf8aca397, original_name='Unknown'
        ),
    })
    unknown_0x80a0b2cb: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x80a0b2cb, original_name='Unknown'
        ),
    })
    unknown_0x69ed492e: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x69ed492e, original_name='Unknown'
        ),
    })
    unknown_0x90419a55: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x90419a55, original_name='Unknown'
        ),
    })
    unknown_0x761db727: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x761db727, original_name='Unknown'
        ),
    })
    unknown_0xdcb8af1c: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xdcb8af1c, original_name='Unknown'
        ),
    })
    unknown_0x9cfddba8: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x9cfddba8, original_name='Unknown'
        ),
    })
    mega_blaster_projectile_with_collision: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xf5056d9d, original_name='MegaBlasterProjectileWithCollision'
        ),
    })
    mega_blaster_projectile_no_collision: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x58dbcc52, original_name='MegaBlasterProjectileNoCollision'
        ),
    })
    part: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3a6d3a64, original_name='PART'
        ),
    })
    pillar_base: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xf3d84488, original_name='PillarBase'
        ),
    })
    pillar_explosion_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x49be8a11, original_name='PillarExplosionEffect'
        ),
    })
    replenish_bubble_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe8706e6e, original_name='ReplenishBubbleExplosion'
        ),
    })
    phazon_barrage_beam: PlasmaBeamInfo = dataclasses.field(default_factory=PlasmaBeamInfo, metadata={
        'reflection': FieldReflection[PlasmaBeamInfo](
            PlasmaBeamInfo, id=0x6cc7412a, original_name='PhazonBarrageBeam', from_json=PlasmaBeamInfo.from_json, to_json=PlasmaBeamInfo.to_json
        ),
    })
    homing_missile_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xacfd8ea8, original_name='HomingMissileProjectile'
        ),
    })
    homing_missile_info: HoverThenHomeProjectile = dataclasses.field(default_factory=HoverThenHomeProjectile, metadata={
        'reflection': FieldReflection[HoverThenHomeProjectile](
            HoverThenHomeProjectile, id=0xe8fc7798, original_name='HomingMissileInfo', from_json=HoverThenHomeProjectile.from_json, to_json=HoverThenHomeProjectile.to_json
        ),
    })
    echo_animation_information: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0x5377d4b5, original_name='EchoAnimationInformation', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    echo_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x4c8aee6d, original_name='EchoExplosion'
        ),
    })
    echo_scan: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SCAN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x0b17536c, original_name='EchoScan'
        ),
    })
    energy_wave_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x76c64459, original_name='EnergyWaveProjectile'
        ),
    })
    echo_blast_beam: PlasmaBeamInfo = dataclasses.field(default_factory=PlasmaBeamInfo, metadata={
        'reflection': FieldReflection[PlasmaBeamInfo](
            PlasmaBeamInfo, id=0xec493f59, original_name='EchoBlastBeam', from_json=PlasmaBeamInfo.from_json, to_json=PlasmaBeamInfo.to_json
        ),
    })
    super_loop_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd1d51e35, original_name='SuperLoopProjectile'
        ),
    })
    whirly_merge_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x8e96e5e4, original_name='WhirlyMergeEffect'
        ),
    })
    visor_blow_out_texture: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['TXTR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5b67a4e7, original_name='VisorBlowOutTexture'
        ),
    })
    visor_blow_out_max_size: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4f6e81a8, original_name='VisorBlowOutMaxSize'
        ),
    })
    sound_phazon_spear_fall: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe8f323f9, original_name='Sound_PhazonSpearFall'
        ),
    })
    sound_phazon_spear_impact: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x9049a2fb, original_name='Sound_PhazonSpearImpact'
        ),
    })
    sound_whirly_merge_in: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x8b8b33d9, original_name='Sound_WhirlyMergeIn'
        ),
    })
    sound_whirly_merge_out: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x09133ecd, original_name='Sound_WhirlyMergeOut'
        ),
    })
    sound_shell_game_impact: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3c67b14e, original_name='Sound_ShellGameImpact'
        ),
    })
    sound_invulnerable_loop: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xaf6889b0, original_name='Sound_InvulnerableLoop'
        ),
    })
    sound_shockwave: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa47e51d3, original_name='Sound_Shockwave'
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
        if property_count != 44:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb5049bbb
        unknown_0xb5049bbb = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3390e915
        unknown_0x3390e915 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf8cc3ab0
        unknown_0xf8cc3ab0 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe5c90a08
        unknown_0xe5c90a08 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2e95d9ad
        unknown_0x2e95d9ad = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21e4d323
        scan = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x00d1aa67
        unknown_0x00d1aa67 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa57b4fac
        unknown_0xa57b4fac = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8836c426
        unknown_0x8836c426 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb87c5139
        unknown_0xb87c5139 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9f566db4
        unknown_0x9f566db4 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa2aac8e7
        unknown_0xa2aac8e7 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf8aca397
        unknown_0xf8aca397 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x80a0b2cb
        unknown_0x80a0b2cb = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x69ed492e
        unknown_0x69ed492e = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x90419a55
        unknown_0x90419a55 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x761db727
        unknown_0x761db727 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdcb8af1c
        unknown_0xdcb8af1c = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9cfddba8
        unknown_0x9cfddba8 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf5056d9d
        mega_blaster_projectile_with_collision = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58dbcc52
        mega_blaster_projectile_no_collision = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3a6d3a64
        part = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf3d84488
        pillar_base = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49be8a11
        pillar_explosion_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe8706e6e
        replenish_bubble_explosion = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6cc7412a
        phazon_barrage_beam = PlasmaBeamInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xacfd8ea8
        homing_missile_projectile = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe8fc7798
        homing_missile_info = HoverThenHomeProjectile.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5377d4b5
        echo_animation_information = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4c8aee6d
        echo_explosion = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0b17536c
        echo_scan = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76c64459
        energy_wave_projectile = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xec493f59
        echo_blast_beam = PlasmaBeamInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd1d51e35
        super_loop_projectile = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8e96e5e4
        whirly_merge_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5b67a4e7
        visor_blow_out_texture = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4f6e81a8
        visor_blow_out_max_size = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe8f323f9
        sound_phazon_spear_fall = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9049a2fb
        sound_phazon_spear_impact = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8b8b33d9
        sound_whirly_merge_in = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x09133ecd
        sound_whirly_merge_out = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3c67b14e
        sound_shell_game_impact = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaf6889b0
        sound_invulnerable_loop = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa47e51d3
        sound_shockwave = structs.BIG_Q.unpack(data.read(8))[0]
    
        return cls(unknown_0xb5049bbb, unknown_0x3390e915, unknown_0xf8cc3ab0, unknown_0xe5c90a08, unknown_0x2e95d9ad, scan, unknown_0x00d1aa67, unknown_0xa57b4fac, unknown_0x8836c426, unknown_0xb87c5139, unknown_0x9f566db4, unknown_0xa2aac8e7, unknown_0xf8aca397, unknown_0x80a0b2cb, unknown_0x69ed492e, unknown_0x90419a55, unknown_0x761db727, unknown_0xdcb8af1c, unknown_0x9cfddba8, mega_blaster_projectile_with_collision, mega_blaster_projectile_no_collision, part, pillar_base, pillar_explosion_effect, replenish_bubble_explosion, phazon_barrage_beam, homing_missile_projectile, homing_missile_info, echo_animation_information, echo_explosion, echo_scan, energy_wave_projectile, echo_blast_beam, super_loop_projectile, whirly_merge_effect, visor_blow_out_texture, visor_blow_out_max_size, sound_phazon_spear_fall, sound_phazon_spear_impact, sound_whirly_merge_in, sound_whirly_merge_out, sound_shell_game_impact, sound_invulnerable_loop, sound_shockwave)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00,')  # 44 properties

        data.write(b'\xb5\x04\x9b\xbb')  # 0xb5049bbb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb5049bbb))

        data.write(b'3\x90\xe9\x15')  # 0x3390e915
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x3390e915))

        data.write(b'\xf8\xcc:\xb0')  # 0xf8cc3ab0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xf8cc3ab0))

        data.write(b'\xe5\xc9\n\x08')  # 0xe5c90a08
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe5c90a08))

        data.write(b'.\x95\xd9\xad')  # 0x2e95d9ad
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x2e95d9ad))

        data.write(b'!\xe4\xd3#')  # 0x21e4d323
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.scan))

        data.write(b'\x00\xd1\xaag')  # 0xd1aa67
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x00d1aa67))

        data.write(b'\xa5{O\xac')  # 0xa57b4fac
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xa57b4fac))

        data.write(b'\x886\xc4&')  # 0x8836c426
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x8836c426))

        data.write(b'\xb8|Q9')  # 0xb87c5139
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xb87c5139))

        data.write(b'\x9fVm\xb4')  # 0x9f566db4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x9f566db4))

        data.write(b'\xa2\xaa\xc8\xe7')  # 0xa2aac8e7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xa2aac8e7))

        data.write(b'\xf8\xac\xa3\x97')  # 0xf8aca397
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xf8aca397))

        data.write(b'\x80\xa0\xb2\xcb')  # 0x80a0b2cb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x80a0b2cb))

        data.write(b'i\xedI.')  # 0x69ed492e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x69ed492e))

        data.write(b'\x90A\x9aU')  # 0x90419a55
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x90419a55))

        data.write(b"v\x1d\xb7'")  # 0x761db727
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x761db727))

        data.write(b'\xdc\xb8\xaf\x1c')  # 0xdcb8af1c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xdcb8af1c))

        data.write(b'\x9c\xfd\xdb\xa8')  # 0x9cfddba8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0x9cfddba8))

        data.write(b'\xf5\x05m\x9d')  # 0xf5056d9d
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.mega_blaster_projectile_with_collision))

        data.write(b'X\xdb\xccR')  # 0x58dbcc52
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.mega_blaster_projectile_no_collision))

        data.write(b':m:d')  # 0x3a6d3a64
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.part))

        data.write(b'\xf3\xd8D\x88')  # 0xf3d84488
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.pillar_base))

        data.write(b'I\xbe\x8a\x11')  # 0x49be8a11
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.pillar_explosion_effect))

        data.write(b'\xe8pnn')  # 0xe8706e6e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.replenish_bubble_explosion))

        data.write(b'l\xc7A*')  # 0x6cc7412a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.phazon_barrage_beam.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xac\xfd\x8e\xa8')  # 0xacfd8ea8
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.homing_missile_projectile))

        data.write(b'\xe8\xfcw\x98')  # 0xe8fc7798
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.homing_missile_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'Sw\xd4\xb5')  # 0x5377d4b5
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.echo_animation_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'L\x8a\xeem')  # 0x4c8aee6d
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.echo_explosion))

        data.write(b'\x0b\x17Sl')  # 0xb17536c
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.echo_scan))

        data.write(b'v\xc6DY')  # 0x76c64459
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.energy_wave_projectile))

        data.write(b'\xecI?Y')  # 0xec493f59
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.echo_blast_beam.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd1\xd5\x1e5')  # 0xd1d51e35
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.super_loop_projectile))

        data.write(b'\x8e\x96\xe5\xe4')  # 0x8e96e5e4
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.whirly_merge_effect))

        data.write(b'[g\xa4\xe7')  # 0x5b67a4e7
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.visor_blow_out_texture))

        data.write(b'On\x81\xa8')  # 0x4f6e81a8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.visor_blow_out_max_size))

        data.write(b'\xe8\xf3#\xf9')  # 0xe8f323f9
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_phazon_spear_fall))

        data.write(b'\x90I\xa2\xfb')  # 0x9049a2fb
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_phazon_spear_impact))

        data.write(b'\x8b\x8b3\xd9')  # 0x8b8b33d9
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_whirly_merge_in))

        data.write(b'\t\x13>\xcd')  # 0x9133ecd
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_whirly_merge_out))

        data.write(b'<g\xb1N')  # 0x3c67b14e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_shell_game_impact))

        data.write(b'\xafh\x89\xb0')  # 0xaf6889b0
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_invulnerable_loop))

        data.write(b'\xa4~Q\xd3')  # 0xa47e51d3
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_shockwave))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DarkSamusAssetsJson", data)
        return cls(
            unknown_0xb5049bbb=json_data['unknown_0xb5049bbb'],
            unknown_0x3390e915=json_data['unknown_0x3390e915'],
            unknown_0xf8cc3ab0=json_data['unknown_0xf8cc3ab0'],
            unknown_0xe5c90a08=json_data['unknown_0xe5c90a08'],
            unknown_0x2e95d9ad=json_data['unknown_0x2e95d9ad'],
            scan=json_data['scan'],
            unknown_0x00d1aa67=json_data['unknown_0x00d1aa67'],
            unknown_0xa57b4fac=json_data['unknown_0xa57b4fac'],
            unknown_0x8836c426=json_data['unknown_0x8836c426'],
            unknown_0xb87c5139=json_data['unknown_0xb87c5139'],
            unknown_0x9f566db4=json_data['unknown_0x9f566db4'],
            unknown_0xa2aac8e7=json_data['unknown_0xa2aac8e7'],
            unknown_0xf8aca397=json_data['unknown_0xf8aca397'],
            unknown_0x80a0b2cb=json_data['unknown_0x80a0b2cb'],
            unknown_0x69ed492e=json_data['unknown_0x69ed492e'],
            unknown_0x90419a55=json_data['unknown_0x90419a55'],
            unknown_0x761db727=json_data['unknown_0x761db727'],
            unknown_0xdcb8af1c=json_data['unknown_0xdcb8af1c'],
            unknown_0x9cfddba8=json_data['unknown_0x9cfddba8'],
            mega_blaster_projectile_with_collision=json_data['mega_blaster_projectile_with_collision'],
            mega_blaster_projectile_no_collision=json_data['mega_blaster_projectile_no_collision'],
            part=json_data['part'],
            pillar_base=json_data['pillar_base'],
            pillar_explosion_effect=json_data['pillar_explosion_effect'],
            replenish_bubble_explosion=json_data['replenish_bubble_explosion'],
            phazon_barrage_beam=PlasmaBeamInfo.from_json(json_data['phazon_barrage_beam']),
            homing_missile_projectile=json_data['homing_missile_projectile'],
            homing_missile_info=HoverThenHomeProjectile.from_json(json_data['homing_missile_info']),
            echo_animation_information=AnimationParameters.from_json(json_data['echo_animation_information']),
            echo_explosion=json_data['echo_explosion'],
            echo_scan=json_data['echo_scan'],
            energy_wave_projectile=json_data['energy_wave_projectile'],
            echo_blast_beam=PlasmaBeamInfo.from_json(json_data['echo_blast_beam']),
            super_loop_projectile=json_data['super_loop_projectile'],
            whirly_merge_effect=json_data['whirly_merge_effect'],
            visor_blow_out_texture=json_data['visor_blow_out_texture'],
            visor_blow_out_max_size=json_data['visor_blow_out_max_size'],
            sound_phazon_spear_fall=json_data['sound_phazon_spear_fall'],
            sound_phazon_spear_impact=json_data['sound_phazon_spear_impact'],
            sound_whirly_merge_in=json_data['sound_whirly_merge_in'],
            sound_whirly_merge_out=json_data['sound_whirly_merge_out'],
            sound_shell_game_impact=json_data['sound_shell_game_impact'],
            sound_invulnerable_loop=json_data['sound_invulnerable_loop'],
            sound_shockwave=json_data['sound_shockwave'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'unknown_0xb5049bbb': self.unknown_0xb5049bbb,
            'unknown_0x3390e915': self.unknown_0x3390e915,
            'unknown_0xf8cc3ab0': self.unknown_0xf8cc3ab0,
            'unknown_0xe5c90a08': self.unknown_0xe5c90a08,
            'unknown_0x2e95d9ad': self.unknown_0x2e95d9ad,
            'scan': self.scan,
            'unknown_0x00d1aa67': self.unknown_0x00d1aa67,
            'unknown_0xa57b4fac': self.unknown_0xa57b4fac,
            'unknown_0x8836c426': self.unknown_0x8836c426,
            'unknown_0xb87c5139': self.unknown_0xb87c5139,
            'unknown_0x9f566db4': self.unknown_0x9f566db4,
            'unknown_0xa2aac8e7': self.unknown_0xa2aac8e7,
            'unknown_0xf8aca397': self.unknown_0xf8aca397,
            'unknown_0x80a0b2cb': self.unknown_0x80a0b2cb,
            'unknown_0x69ed492e': self.unknown_0x69ed492e,
            'unknown_0x90419a55': self.unknown_0x90419a55,
            'unknown_0x761db727': self.unknown_0x761db727,
            'unknown_0xdcb8af1c': self.unknown_0xdcb8af1c,
            'unknown_0x9cfddba8': self.unknown_0x9cfddba8,
            'mega_blaster_projectile_with_collision': self.mega_blaster_projectile_with_collision,
            'mega_blaster_projectile_no_collision': self.mega_blaster_projectile_no_collision,
            'part': self.part,
            'pillar_base': self.pillar_base,
            'pillar_explosion_effect': self.pillar_explosion_effect,
            'replenish_bubble_explosion': self.replenish_bubble_explosion,
            'phazon_barrage_beam': self.phazon_barrage_beam.to_json(),
            'homing_missile_projectile': self.homing_missile_projectile,
            'homing_missile_info': self.homing_missile_info.to_json(),
            'echo_animation_information': self.echo_animation_information.to_json(),
            'echo_explosion': self.echo_explosion,
            'echo_scan': self.echo_scan,
            'energy_wave_projectile': self.energy_wave_projectile,
            'echo_blast_beam': self.echo_blast_beam.to_json(),
            'super_loop_projectile': self.super_loop_projectile,
            'whirly_merge_effect': self.whirly_merge_effect,
            'visor_blow_out_texture': self.visor_blow_out_texture,
            'visor_blow_out_max_size': self.visor_blow_out_max_size,
            'sound_phazon_spear_fall': self.sound_phazon_spear_fall,
            'sound_phazon_spear_impact': self.sound_phazon_spear_impact,
            'sound_whirly_merge_in': self.sound_whirly_merge_in,
            'sound_whirly_merge_out': self.sound_whirly_merge_out,
            'sound_shell_game_impact': self.sound_shell_game_impact,
            'sound_invulnerable_loop': self.sound_invulnerable_loop,
            'sound_shockwave': self.sound_shockwave,
        }

    def _dependencies_for_scan(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scan)

    def _dependencies_for_mega_blaster_projectile_with_collision(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.mega_blaster_projectile_with_collision)

    def _dependencies_for_mega_blaster_projectile_no_collision(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.mega_blaster_projectile_no_collision)

    def _dependencies_for_part(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part)

    def _dependencies_for_pillar_base(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.pillar_base)

    def _dependencies_for_pillar_explosion_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.pillar_explosion_effect)

    def _dependencies_for_replenish_bubble_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.replenish_bubble_explosion)

    def _dependencies_for_homing_missile_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.homing_missile_projectile)

    def _dependencies_for_echo_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.echo_explosion)

    def _dependencies_for_echo_scan(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.echo_scan)

    def _dependencies_for_energy_wave_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.energy_wave_projectile)

    def _dependencies_for_super_loop_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.super_loop_projectile)

    def _dependencies_for_whirly_merge_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.whirly_merge_effect)

    def _dependencies_for_visor_blow_out_texture(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.visor_blow_out_texture)

    def _dependencies_for_sound_phazon_spear_fall(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_phazon_spear_fall)

    def _dependencies_for_sound_phazon_spear_impact(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_phazon_spear_impact)

    def _dependencies_for_sound_whirly_merge_in(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_whirly_merge_in)

    def _dependencies_for_sound_whirly_merge_out(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_whirly_merge_out)

    def _dependencies_for_sound_shell_game_impact(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_shell_game_impact)

    def _dependencies_for_sound_invulnerable_loop(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_invulnerable_loop)

    def _dependencies_for_sound_shockwave(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_shockwave)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_scan, "scan", "AssetId"),
            (self._dependencies_for_mega_blaster_projectile_with_collision, "mega_blaster_projectile_with_collision", "AssetId"),
            (self._dependencies_for_mega_blaster_projectile_no_collision, "mega_blaster_projectile_no_collision", "AssetId"),
            (self._dependencies_for_part, "part", "AssetId"),
            (self._dependencies_for_pillar_base, "pillar_base", "AssetId"),
            (self._dependencies_for_pillar_explosion_effect, "pillar_explosion_effect", "AssetId"),
            (self._dependencies_for_replenish_bubble_explosion, "replenish_bubble_explosion", "AssetId"),
            (self.phazon_barrage_beam.dependencies_for, "phazon_barrage_beam", "PlasmaBeamInfo"),
            (self._dependencies_for_homing_missile_projectile, "homing_missile_projectile", "AssetId"),
            (self.homing_missile_info.dependencies_for, "homing_missile_info", "HoverThenHomeProjectile"),
            (self.echo_animation_information.dependencies_for, "echo_animation_information", "AnimationParameters"),
            (self._dependencies_for_echo_explosion, "echo_explosion", "AssetId"),
            (self._dependencies_for_echo_scan, "echo_scan", "AssetId"),
            (self._dependencies_for_energy_wave_projectile, "energy_wave_projectile", "AssetId"),
            (self.echo_blast_beam.dependencies_for, "echo_blast_beam", "PlasmaBeamInfo"),
            (self._dependencies_for_super_loop_projectile, "super_loop_projectile", "AssetId"),
            (self._dependencies_for_whirly_merge_effect, "whirly_merge_effect", "AssetId"),
            (self._dependencies_for_visor_blow_out_texture, "visor_blow_out_texture", "AssetId"),
            (self._dependencies_for_sound_phazon_spear_fall, "sound_phazon_spear_fall", "AssetId"),
            (self._dependencies_for_sound_phazon_spear_impact, "sound_phazon_spear_impact", "AssetId"),
            (self._dependencies_for_sound_whirly_merge_in, "sound_whirly_merge_in", "AssetId"),
            (self._dependencies_for_sound_whirly_merge_out, "sound_whirly_merge_out", "AssetId"),
            (self._dependencies_for_sound_shell_game_impact, "sound_shell_game_impact", "AssetId"),
            (self._dependencies_for_sound_invulnerable_loop, "sound_invulnerable_loop", "AssetId"),
            (self._dependencies_for_sound_shockwave, "sound_shockwave", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for DarkSamusAssets.{field_name} ({field_type}): {e}"
                )


def _decode_phazon_barrage_beam(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size)


def _decode_homing_missile_info(data: typing.BinaryIO, game: Game, property_size: int) -> HoverThenHomeProjectile:
    return HoverThenHomeProjectile.from_stream(data, game, property_size)


def _decode_echo_animation_information(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_echo_blast_beam(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xb5049bbb: ('unknown_0xb5049bbb', structs.decode_BIG_f),
    0x3390e915: ('unknown_0x3390e915', structs.decode_BIG_f),
    0xf8cc3ab0: ('unknown_0xf8cc3ab0', structs.decode_BIG_f),
    0xe5c90a08: ('unknown_0xe5c90a08', structs.decode_BIG_f),
    0x2e95d9ad: ('unknown_0x2e95d9ad', structs.decode_BIG_f),
    0x21e4d323: ('scan', structs.decode_BIG_Q),
    0x00d1aa67: ('unknown_0x00d1aa67', structs.decode_BIG_l),
    0xa57b4fac: ('unknown_0xa57b4fac', structs.decode_BIG_l),
    0x8836c426: ('unknown_0x8836c426', structs.decode_BIG_l),
    0xb87c5139: ('unknown_0xb87c5139', structs.decode_BIG_l),
    0x9f566db4: ('unknown_0x9f566db4', structs.decode_BIG_l),
    0xa2aac8e7: ('unknown_0xa2aac8e7', structs.decode_BIG_l),
    0xf8aca397: ('unknown_0xf8aca397', structs.decode_BIG_l),
    0x80a0b2cb: ('unknown_0x80a0b2cb', structs.decode_BIG_l),
    0x69ed492e: ('unknown_0x69ed492e', structs.decode_BIG_l),
    0x90419a55: ('unknown_0x90419a55', structs.decode_BIG_l),
    0x761db727: ('unknown_0x761db727', structs.decode_BIG_l),
    0xdcb8af1c: ('unknown_0xdcb8af1c', structs.decode_BIG_l),
    0x9cfddba8: ('unknown_0x9cfddba8', structs.decode_BIG_l),
    0xf5056d9d: ('mega_blaster_projectile_with_collision', structs.decode_BIG_Q),
    0x58dbcc52: ('mega_blaster_projectile_no_collision', structs.decode_BIG_Q),
    0x3a6d3a64: ('part', structs.decode_BIG_Q),
    0xf3d84488: ('pillar_base', structs.decode_BIG_Q),
    0x49be8a11: ('pillar_explosion_effect', structs.decode_BIG_Q),
    0xe8706e6e: ('replenish_bubble_explosion', structs.decode_BIG_Q),
    0x6cc7412a: ('phazon_barrage_beam', _decode_phazon_barrage_beam),
    0xacfd8ea8: ('homing_missile_projectile', structs.decode_BIG_Q),
    0xe8fc7798: ('homing_missile_info', _decode_homing_missile_info),
    0x5377d4b5: ('echo_animation_information', _decode_echo_animation_information),
    0x4c8aee6d: ('echo_explosion', structs.decode_BIG_Q),
    0x0b17536c: ('echo_scan', structs.decode_BIG_Q),
    0x76c64459: ('energy_wave_projectile', structs.decode_BIG_Q),
    0xec493f59: ('echo_blast_beam', _decode_echo_blast_beam),
    0xd1d51e35: ('super_loop_projectile', structs.decode_BIG_Q),
    0x8e96e5e4: ('whirly_merge_effect', structs.decode_BIG_Q),
    0x5b67a4e7: ('visor_blow_out_texture', structs.decode_BIG_Q),
    0x4f6e81a8: ('visor_blow_out_max_size', structs.decode_BIG_f),
    0xe8f323f9: ('sound_phazon_spear_fall', structs.decode_BIG_Q),
    0x9049a2fb: ('sound_phazon_spear_impact', structs.decode_BIG_Q),
    0x8b8b33d9: ('sound_whirly_merge_in', structs.decode_BIG_Q),
    0x09133ecd: ('sound_whirly_merge_out', structs.decode_BIG_Q),
    0x3c67b14e: ('sound_shell_game_impact', structs.decode_BIG_Q),
    0xaf6889b0: ('sound_invulnerable_loop', structs.decode_BIG_Q),
    0xa47e51d3: ('sound_shockwave', structs.decode_BIG_Q),
}
