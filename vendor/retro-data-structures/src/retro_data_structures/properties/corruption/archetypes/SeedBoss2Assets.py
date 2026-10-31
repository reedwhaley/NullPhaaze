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
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SeedBoss2AssetsJson(typing_extensions.TypedDict):
        unknown_0x90aefee1: bool
        swarm_bot_animation_information: json_util.JsonObject
        swarm_bot_vulnerability: json_util.JsonObject
        swarm_bot_death_explosion: int
        unknown_0xc7dc6d3e: int
        unknown_0x41481f90: int
        giant_form_electric_effect: int
        giant_targetable_effect: int
        giant_electric_ball_effect: int
        giant_electric_ball_explosion: int
        part_0x3dcf98a5: int
        part_0xdc17fb84: int
        part_0xc35db9ce: int
        part_0xa70e1bbb: int
        part_0x7cc1b298: int
        tornado_dust: int
        ring_idle_effect: int
        ring_energize_effect: int
        ring_projectile: int
        ring_explosion_effect: int
        wheel_portal_effect: int
        wheel_tumble_effect: int
        wheel_projectile_cluster_effect: int
        wheel_burst_electricity: int
        wheel_seeker_electricity: int
        wheel_targetable_effect: int
        wheel_non_targetable_effect: int
        wheel_energy_beam: json_util.JsonObject
        wheel_tumble_world_collision: int
        wheel_muzzle_flash_effect: int
        visor_blow_out_texture: int
        visor_blow_out_max_size: float
        interface_delayed_effect: int
        scan_sphere_form: int
        scan_tornado_form: int
        scan_wheel_form: int
        scan_ring_form: int
        scan_giant_form: int
        scan_chainsaw_form: int
        caud_0x9a469187: int
        caud_0xa959b017: int
    

@dataclasses.dataclass()
class SeedBoss2Assets(BaseProperty):
    unknown_0x90aefee1: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x90aefee1, original_name='Unknown'
        ),
    })
    swarm_bot_animation_information: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0x4c64d3a6, original_name='SwarmBotAnimationInformation', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    swarm_bot_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x00dd06cc, original_name='SwarmBotVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    swarm_bot_death_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb64ed093, original_name='SwarmBotDeathExplosion'
        ),
    })
    unknown_0xc7dc6d3e: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc7dc6d3e, original_name='Unknown'
        ),
    })
    unknown_0x41481f90: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x41481f90, original_name='Unknown'
        ),
    })
    giant_form_electric_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['ELSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc5012a38, original_name='GiantFormElectricEffect'
        ),
    })
    giant_targetable_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3b5b99a8, original_name='GiantTargetableEffect'
        ),
    })
    giant_electric_ball_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x6ae0cae6, original_name='GiantElectricBallEffect'
        ),
    })
    giant_electric_ball_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2975be8d, original_name='GiantElectricBallExplosion'
        ),
    })
    part_0x3dcf98a5: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3dcf98a5, original_name='PART'
        ),
    })
    part_0xdc17fb84: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xdc17fb84, original_name='PART'
        ),
    })
    part_0xc35db9ce: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc35db9ce, original_name='PART'
        ),
    })
    part_0xa70e1bbb: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa70e1bbb, original_name='PART'
        ),
    })
    part_0x7cc1b298: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x7cc1b298, original_name='PART'
        ),
    })
    tornado_dust: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x7be868ce, original_name='TornadoDust'
        ),
    })
    ring_idle_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc90cda8c, original_name='RingIdleEffect'
        ),
    })
    ring_energize_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x4d9ed8e1, original_name='RingEnergizeEffect'
        ),
    })
    ring_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x21dc4c35, original_name='RingProjectile'
        ),
    })
    ring_explosion_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xcb673da3, original_name='RingExplosionEffect'
        ),
    })
    wheel_portal_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc1bbbed8, original_name='WheelPortalEffect'
        ),
    })
    wheel_tumble_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xf4386c42, original_name='WheelTumbleEffect'
        ),
    })
    wheel_projectile_cluster_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe3c3de5e, original_name='WheelProjectileClusterEffect'
        ),
    })
    wheel_burst_electricity: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['ELSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x1899c839, original_name='WheelBurstElectricity'
        ),
    })
    wheel_seeker_electricity: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['ELSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x6b6606b8, original_name='WheelSeekerElectricity'
        ),
    })
    wheel_targetable_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x3b6cdadb, original_name='WheelTargetableEffect'
        ),
    })
    wheel_non_targetable_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa6e942ed, original_name='WheelNonTargetableEffect'
        ),
    })
    wheel_energy_beam: PlasmaBeamInfo = dataclasses.field(default_factory=PlasmaBeamInfo, metadata={
        'reflection': FieldReflection[PlasmaBeamInfo](
            PlasmaBeamInfo, id=0x21ec3d21, original_name='WheelEnergyBeam', from_json=PlasmaBeamInfo.from_json, to_json=PlasmaBeamInfo.to_json
        ),
    })
    wheel_tumble_world_collision: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x82ee63c8, original_name='WheelTumbleWorldCollision'
        ),
    })
    wheel_muzzle_flash_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xab0a66da, original_name='WheelMuzzleFlashEffect'
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
    interface_delayed_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xad6ecc7f, original_name='InterfaceDelayedEffect'
        ),
    })
    scan_sphere_form: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SCAN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x91d5f317, original_name='Scan_SphereForm'
        ),
    })
    scan_tornado_form: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SCAN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x1ddfd45a, original_name='Scan_TornadoForm'
        ),
    })
    scan_wheel_form: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SCAN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x01fba748, original_name='Scan_WheelForm'
        ),
    })
    scan_ring_form: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SCAN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xcd2f3d00, original_name='Scan_RingForm'
        ),
    })
    scan_giant_form: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SCAN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xae813f86, original_name='Scan_GiantForm'
        ),
    })
    scan_chainsaw_form: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['SCAN'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd27e8786, original_name='Scan_ChainsawForm'
        ),
    })
    caud_0x9a469187: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x9a469187, original_name='CAUD'
        ),
    })
    caud_0xa959b017: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa959b017, original_name='CAUD'
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
        if property_count != 41:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x90aefee1
        unknown_0x90aefee1 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4c64d3a6
        swarm_bot_animation_information = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x00dd06cc
        swarm_bot_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb64ed093
        swarm_bot_death_explosion = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc7dc6d3e
        unknown_0xc7dc6d3e = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x41481f90
        unknown_0x41481f90 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc5012a38
        giant_form_electric_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3b5b99a8
        giant_targetable_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6ae0cae6
        giant_electric_ball_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2975be8d
        giant_electric_ball_explosion = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3dcf98a5
        part_0x3dcf98a5 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdc17fb84
        part_0xdc17fb84 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc35db9ce
        part_0xc35db9ce = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa70e1bbb
        part_0xa70e1bbb = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7cc1b298
        part_0x7cc1b298 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7be868ce
        tornado_dust = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc90cda8c
        ring_idle_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4d9ed8e1
        ring_energize_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21dc4c35
        ring_projectile = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcb673da3
        ring_explosion_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc1bbbed8
        wheel_portal_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf4386c42
        wheel_tumble_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe3c3de5e
        wheel_projectile_cluster_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1899c839
        wheel_burst_electricity = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6b6606b8
        wheel_seeker_electricity = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3b6cdadb
        wheel_targetable_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa6e942ed
        wheel_non_targetable_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21ec3d21
        wheel_energy_beam = PlasmaBeamInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x82ee63c8
        wheel_tumble_world_collision = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xab0a66da
        wheel_muzzle_flash_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5b67a4e7
        visor_blow_out_texture = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4f6e81a8
        visor_blow_out_max_size = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xad6ecc7f
        interface_delayed_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x91d5f317
        scan_sphere_form = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1ddfd45a
        scan_tornado_form = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x01fba748
        scan_wheel_form = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcd2f3d00
        scan_ring_form = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xae813f86
        scan_giant_form = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd27e8786
        scan_chainsaw_form = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9a469187
        caud_0x9a469187 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa959b017
        caud_0xa959b017 = structs.BIG_Q.unpack(data.read(8))[0]
    
        return cls(unknown_0x90aefee1, swarm_bot_animation_information, swarm_bot_vulnerability, swarm_bot_death_explosion, unknown_0xc7dc6d3e, unknown_0x41481f90, giant_form_electric_effect, giant_targetable_effect, giant_electric_ball_effect, giant_electric_ball_explosion, part_0x3dcf98a5, part_0xdc17fb84, part_0xc35db9ce, part_0xa70e1bbb, part_0x7cc1b298, tornado_dust, ring_idle_effect, ring_energize_effect, ring_projectile, ring_explosion_effect, wheel_portal_effect, wheel_tumble_effect, wheel_projectile_cluster_effect, wheel_burst_electricity, wheel_seeker_electricity, wheel_targetable_effect, wheel_non_targetable_effect, wheel_energy_beam, wheel_tumble_world_collision, wheel_muzzle_flash_effect, visor_blow_out_texture, visor_blow_out_max_size, interface_delayed_effect, scan_sphere_form, scan_tornado_form, scan_wheel_form, scan_ring_form, scan_giant_form, scan_chainsaw_form, caud_0x9a469187, caud_0xa959b017)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00)')  # 41 properties

        data.write(b'\x90\xae\xfe\xe1')  # 0x90aefee1
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x90aefee1))

        data.write(b'Ld\xd3\xa6')  # 0x4c64d3a6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.swarm_bot_animation_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x00\xdd\x06\xcc')  # 0xdd06cc
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.swarm_bot_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb6N\xd0\x93')  # 0xb64ed093
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.swarm_bot_death_explosion))

        data.write(b'\xc7\xdcm>')  # 0xc7dc6d3e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.unknown_0xc7dc6d3e))

        data.write(b'AH\x1f\x90')  # 0x41481f90
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.unknown_0x41481f90))

        data.write(b'\xc5\x01*8')  # 0xc5012a38
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.giant_form_electric_effect))

        data.write(b';[\x99\xa8')  # 0x3b5b99a8
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.giant_targetable_effect))

        data.write(b'j\xe0\xca\xe6')  # 0x6ae0cae6
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.giant_electric_ball_effect))

        data.write(b')u\xbe\x8d')  # 0x2975be8d
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.giant_electric_ball_explosion))

        data.write(b'=\xcf\x98\xa5')  # 0x3dcf98a5
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.part_0x3dcf98a5))

        data.write(b'\xdc\x17\xfb\x84')  # 0xdc17fb84
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.part_0xdc17fb84))

        data.write(b'\xc3]\xb9\xce')  # 0xc35db9ce
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.part_0xc35db9ce))

        data.write(b'\xa7\x0e\x1b\xbb')  # 0xa70e1bbb
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.part_0xa70e1bbb))

        data.write(b'|\xc1\xb2\x98')  # 0x7cc1b298
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.part_0x7cc1b298))

        data.write(b'{\xe8h\xce')  # 0x7be868ce
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.tornado_dust))

        data.write(b'\xc9\x0c\xda\x8c')  # 0xc90cda8c
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ring_idle_effect))

        data.write(b'M\x9e\xd8\xe1')  # 0x4d9ed8e1
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ring_energize_effect))

        data.write(b'!\xdcL5')  # 0x21dc4c35
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ring_projectile))

        data.write(b'\xcbg=\xa3')  # 0xcb673da3
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ring_explosion_effect))

        data.write(b'\xc1\xbb\xbe\xd8')  # 0xc1bbbed8
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.wheel_portal_effect))

        data.write(b'\xf48lB')  # 0xf4386c42
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.wheel_tumble_effect))

        data.write(b'\xe3\xc3\xde^')  # 0xe3c3de5e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.wheel_projectile_cluster_effect))

        data.write(b'\x18\x99\xc89')  # 0x1899c839
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.wheel_burst_electricity))

        data.write(b'kf\x06\xb8')  # 0x6b6606b8
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.wheel_seeker_electricity))

        data.write(b';l\xda\xdb')  # 0x3b6cdadb
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.wheel_targetable_effect))

        data.write(b'\xa6\xe9B\xed')  # 0xa6e942ed
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.wheel_non_targetable_effect))

        data.write(b'!\xec=!')  # 0x21ec3d21
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.wheel_energy_beam.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x82\xeec\xc8')  # 0x82ee63c8
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.wheel_tumble_world_collision))

        data.write(b'\xab\nf\xda')  # 0xab0a66da
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.wheel_muzzle_flash_effect))

        data.write(b'[g\xa4\xe7')  # 0x5b67a4e7
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.visor_blow_out_texture))

        data.write(b'On\x81\xa8')  # 0x4f6e81a8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.visor_blow_out_max_size))

        data.write(b'\xadn\xcc\x7f')  # 0xad6ecc7f
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.interface_delayed_effect))

        data.write(b'\x91\xd5\xf3\x17')  # 0x91d5f317
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.scan_sphere_form))

        data.write(b'\x1d\xdf\xd4Z')  # 0x1ddfd45a
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.scan_tornado_form))

        data.write(b'\x01\xfb\xa7H')  # 0x1fba748
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.scan_wheel_form))

        data.write(b'\xcd/=\x00')  # 0xcd2f3d00
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.scan_ring_form))

        data.write(b'\xae\x81?\x86')  # 0xae813f86
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.scan_giant_form))

        data.write(b'\xd2~\x87\x86')  # 0xd27e8786
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.scan_chainsaw_form))

        data.write(b'\x9aF\x91\x87')  # 0x9a469187
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.caud_0x9a469187))

        data.write(b'\xa9Y\xb0\x17')  # 0xa959b017
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.caud_0xa959b017))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SeedBoss2AssetsJson", data)
        return cls(
            unknown_0x90aefee1=json_data['unknown_0x90aefee1'],
            swarm_bot_animation_information=AnimationParameters.from_json(json_data['swarm_bot_animation_information']),
            swarm_bot_vulnerability=DamageVulnerability.from_json(json_data['swarm_bot_vulnerability']),
            swarm_bot_death_explosion=json_data['swarm_bot_death_explosion'],
            unknown_0xc7dc6d3e=json_data['unknown_0xc7dc6d3e'],
            unknown_0x41481f90=json_data['unknown_0x41481f90'],
            giant_form_electric_effect=json_data['giant_form_electric_effect'],
            giant_targetable_effect=json_data['giant_targetable_effect'],
            giant_electric_ball_effect=json_data['giant_electric_ball_effect'],
            giant_electric_ball_explosion=json_data['giant_electric_ball_explosion'],
            part_0x3dcf98a5=json_data['part_0x3dcf98a5'],
            part_0xdc17fb84=json_data['part_0xdc17fb84'],
            part_0xc35db9ce=json_data['part_0xc35db9ce'],
            part_0xa70e1bbb=json_data['part_0xa70e1bbb'],
            part_0x7cc1b298=json_data['part_0x7cc1b298'],
            tornado_dust=json_data['tornado_dust'],
            ring_idle_effect=json_data['ring_idle_effect'],
            ring_energize_effect=json_data['ring_energize_effect'],
            ring_projectile=json_data['ring_projectile'],
            ring_explosion_effect=json_data['ring_explosion_effect'],
            wheel_portal_effect=json_data['wheel_portal_effect'],
            wheel_tumble_effect=json_data['wheel_tumble_effect'],
            wheel_projectile_cluster_effect=json_data['wheel_projectile_cluster_effect'],
            wheel_burst_electricity=json_data['wheel_burst_electricity'],
            wheel_seeker_electricity=json_data['wheel_seeker_electricity'],
            wheel_targetable_effect=json_data['wheel_targetable_effect'],
            wheel_non_targetable_effect=json_data['wheel_non_targetable_effect'],
            wheel_energy_beam=PlasmaBeamInfo.from_json(json_data['wheel_energy_beam']),
            wheel_tumble_world_collision=json_data['wheel_tumble_world_collision'],
            wheel_muzzle_flash_effect=json_data['wheel_muzzle_flash_effect'],
            visor_blow_out_texture=json_data['visor_blow_out_texture'],
            visor_blow_out_max_size=json_data['visor_blow_out_max_size'],
            interface_delayed_effect=json_data['interface_delayed_effect'],
            scan_sphere_form=json_data['scan_sphere_form'],
            scan_tornado_form=json_data['scan_tornado_form'],
            scan_wheel_form=json_data['scan_wheel_form'],
            scan_ring_form=json_data['scan_ring_form'],
            scan_giant_form=json_data['scan_giant_form'],
            scan_chainsaw_form=json_data['scan_chainsaw_form'],
            caud_0x9a469187=json_data['caud_0x9a469187'],
            caud_0xa959b017=json_data['caud_0xa959b017'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'unknown_0x90aefee1': self.unknown_0x90aefee1,
            'swarm_bot_animation_information': self.swarm_bot_animation_information.to_json(),
            'swarm_bot_vulnerability': self.swarm_bot_vulnerability.to_json(),
            'swarm_bot_death_explosion': self.swarm_bot_death_explosion,
            'unknown_0xc7dc6d3e': self.unknown_0xc7dc6d3e,
            'unknown_0x41481f90': self.unknown_0x41481f90,
            'giant_form_electric_effect': self.giant_form_electric_effect,
            'giant_targetable_effect': self.giant_targetable_effect,
            'giant_electric_ball_effect': self.giant_electric_ball_effect,
            'giant_electric_ball_explosion': self.giant_electric_ball_explosion,
            'part_0x3dcf98a5': self.part_0x3dcf98a5,
            'part_0xdc17fb84': self.part_0xdc17fb84,
            'part_0xc35db9ce': self.part_0xc35db9ce,
            'part_0xa70e1bbb': self.part_0xa70e1bbb,
            'part_0x7cc1b298': self.part_0x7cc1b298,
            'tornado_dust': self.tornado_dust,
            'ring_idle_effect': self.ring_idle_effect,
            'ring_energize_effect': self.ring_energize_effect,
            'ring_projectile': self.ring_projectile,
            'ring_explosion_effect': self.ring_explosion_effect,
            'wheel_portal_effect': self.wheel_portal_effect,
            'wheel_tumble_effect': self.wheel_tumble_effect,
            'wheel_projectile_cluster_effect': self.wheel_projectile_cluster_effect,
            'wheel_burst_electricity': self.wheel_burst_electricity,
            'wheel_seeker_electricity': self.wheel_seeker_electricity,
            'wheel_targetable_effect': self.wheel_targetable_effect,
            'wheel_non_targetable_effect': self.wheel_non_targetable_effect,
            'wheel_energy_beam': self.wheel_energy_beam.to_json(),
            'wheel_tumble_world_collision': self.wheel_tumble_world_collision,
            'wheel_muzzle_flash_effect': self.wheel_muzzle_flash_effect,
            'visor_blow_out_texture': self.visor_blow_out_texture,
            'visor_blow_out_max_size': self.visor_blow_out_max_size,
            'interface_delayed_effect': self.interface_delayed_effect,
            'scan_sphere_form': self.scan_sphere_form,
            'scan_tornado_form': self.scan_tornado_form,
            'scan_wheel_form': self.scan_wheel_form,
            'scan_ring_form': self.scan_ring_form,
            'scan_giant_form': self.scan_giant_form,
            'scan_chainsaw_form': self.scan_chainsaw_form,
            'caud_0x9a469187': self.caud_0x9a469187,
            'caud_0xa959b017': self.caud_0xa959b017,
        }

    def _dependencies_for_swarm_bot_death_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.swarm_bot_death_explosion)

    def _dependencies_for_unknown_0xc7dc6d3e(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_0xc7dc6d3e)

    def _dependencies_for_unknown_0x41481f90(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown_0x41481f90)

    def _dependencies_for_giant_form_electric_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.giant_form_electric_effect)

    def _dependencies_for_giant_targetable_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.giant_targetable_effect)

    def _dependencies_for_giant_electric_ball_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.giant_electric_ball_effect)

    def _dependencies_for_giant_electric_ball_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.giant_electric_ball_explosion)

    def _dependencies_for_part_0x3dcf98a5(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0x3dcf98a5)

    def _dependencies_for_part_0xdc17fb84(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0xdc17fb84)

    def _dependencies_for_part_0xc35db9ce(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0xc35db9ce)

    def _dependencies_for_part_0xa70e1bbb(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0xa70e1bbb)

    def _dependencies_for_part_0x7cc1b298(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part_0x7cc1b298)

    def _dependencies_for_tornado_dust(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.tornado_dust)

    def _dependencies_for_ring_idle_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ring_idle_effect)

    def _dependencies_for_ring_energize_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ring_energize_effect)

    def _dependencies_for_ring_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ring_projectile)

    def _dependencies_for_ring_explosion_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ring_explosion_effect)

    def _dependencies_for_wheel_portal_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wheel_portal_effect)

    def _dependencies_for_wheel_tumble_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wheel_tumble_effect)

    def _dependencies_for_wheel_projectile_cluster_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wheel_projectile_cluster_effect)

    def _dependencies_for_wheel_burst_electricity(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wheel_burst_electricity)

    def _dependencies_for_wheel_seeker_electricity(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wheel_seeker_electricity)

    def _dependencies_for_wheel_targetable_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wheel_targetable_effect)

    def _dependencies_for_wheel_non_targetable_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wheel_non_targetable_effect)

    def _dependencies_for_wheel_tumble_world_collision(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wheel_tumble_world_collision)

    def _dependencies_for_wheel_muzzle_flash_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.wheel_muzzle_flash_effect)

    def _dependencies_for_visor_blow_out_texture(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.visor_blow_out_texture)

    def _dependencies_for_interface_delayed_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.interface_delayed_effect)

    def _dependencies_for_scan_sphere_form(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scan_sphere_form)

    def _dependencies_for_scan_tornado_form(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scan_tornado_form)

    def _dependencies_for_scan_wheel_form(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scan_wheel_form)

    def _dependencies_for_scan_ring_form(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scan_ring_form)

    def _dependencies_for_scan_giant_form(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scan_giant_form)

    def _dependencies_for_scan_chainsaw_form(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scan_chainsaw_form)

    def _dependencies_for_caud_0x9a469187(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.caud_0x9a469187)

    def _dependencies_for_caud_0xa959b017(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.caud_0xa959b017)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.swarm_bot_animation_information.dependencies_for, "swarm_bot_animation_information", "AnimationParameters"),
            (self._dependencies_for_swarm_bot_death_explosion, "swarm_bot_death_explosion", "AssetId"),
            (self._dependencies_for_unknown_0xc7dc6d3e, "unknown_0xc7dc6d3e", "AssetId"),
            (self._dependencies_for_unknown_0x41481f90, "unknown_0x41481f90", "AssetId"),
            (self._dependencies_for_giant_form_electric_effect, "giant_form_electric_effect", "AssetId"),
            (self._dependencies_for_giant_targetable_effect, "giant_targetable_effect", "AssetId"),
            (self._dependencies_for_giant_electric_ball_effect, "giant_electric_ball_effect", "AssetId"),
            (self._dependencies_for_giant_electric_ball_explosion, "giant_electric_ball_explosion", "AssetId"),
            (self._dependencies_for_part_0x3dcf98a5, "part_0x3dcf98a5", "AssetId"),
            (self._dependencies_for_part_0xdc17fb84, "part_0xdc17fb84", "AssetId"),
            (self._dependencies_for_part_0xc35db9ce, "part_0xc35db9ce", "AssetId"),
            (self._dependencies_for_part_0xa70e1bbb, "part_0xa70e1bbb", "AssetId"),
            (self._dependencies_for_part_0x7cc1b298, "part_0x7cc1b298", "AssetId"),
            (self._dependencies_for_tornado_dust, "tornado_dust", "AssetId"),
            (self._dependencies_for_ring_idle_effect, "ring_idle_effect", "AssetId"),
            (self._dependencies_for_ring_energize_effect, "ring_energize_effect", "AssetId"),
            (self._dependencies_for_ring_projectile, "ring_projectile", "AssetId"),
            (self._dependencies_for_ring_explosion_effect, "ring_explosion_effect", "AssetId"),
            (self._dependencies_for_wheel_portal_effect, "wheel_portal_effect", "AssetId"),
            (self._dependencies_for_wheel_tumble_effect, "wheel_tumble_effect", "AssetId"),
            (self._dependencies_for_wheel_projectile_cluster_effect, "wheel_projectile_cluster_effect", "AssetId"),
            (self._dependencies_for_wheel_burst_electricity, "wheel_burst_electricity", "AssetId"),
            (self._dependencies_for_wheel_seeker_electricity, "wheel_seeker_electricity", "AssetId"),
            (self._dependencies_for_wheel_targetable_effect, "wheel_targetable_effect", "AssetId"),
            (self._dependencies_for_wheel_non_targetable_effect, "wheel_non_targetable_effect", "AssetId"),
            (self.wheel_energy_beam.dependencies_for, "wheel_energy_beam", "PlasmaBeamInfo"),
            (self._dependencies_for_wheel_tumble_world_collision, "wheel_tumble_world_collision", "AssetId"),
            (self._dependencies_for_wheel_muzzle_flash_effect, "wheel_muzzle_flash_effect", "AssetId"),
            (self._dependencies_for_visor_blow_out_texture, "visor_blow_out_texture", "AssetId"),
            (self._dependencies_for_interface_delayed_effect, "interface_delayed_effect", "AssetId"),
            (self._dependencies_for_scan_sphere_form, "scan_sphere_form", "AssetId"),
            (self._dependencies_for_scan_tornado_form, "scan_tornado_form", "AssetId"),
            (self._dependencies_for_scan_wheel_form, "scan_wheel_form", "AssetId"),
            (self._dependencies_for_scan_ring_form, "scan_ring_form", "AssetId"),
            (self._dependencies_for_scan_giant_form, "scan_giant_form", "AssetId"),
            (self._dependencies_for_scan_chainsaw_form, "scan_chainsaw_form", "AssetId"),
            (self._dependencies_for_caud_0x9a469187, "caud_0x9a469187", "AssetId"),
            (self._dependencies_for_caud_0xa959b017, "caud_0xa959b017", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for SeedBoss2Assets.{field_name} ({field_type}): {e}"
                )


def _decode_swarm_bot_animation_information(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_swarm_bot_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_wheel_energy_beam(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x90aefee1: ('unknown_0x90aefee1', structs.decode_BIG_bool_),
    0x4c64d3a6: ('swarm_bot_animation_information', _decode_swarm_bot_animation_information),
    0x00dd06cc: ('swarm_bot_vulnerability', _decode_swarm_bot_vulnerability),
    0xb64ed093: ('swarm_bot_death_explosion', structs.decode_BIG_Q),
    0xc7dc6d3e: ('unknown_0xc7dc6d3e', structs.decode_BIG_Q),
    0x41481f90: ('unknown_0x41481f90', structs.decode_BIG_Q),
    0xc5012a38: ('giant_form_electric_effect', structs.decode_BIG_Q),
    0x3b5b99a8: ('giant_targetable_effect', structs.decode_BIG_Q),
    0x6ae0cae6: ('giant_electric_ball_effect', structs.decode_BIG_Q),
    0x2975be8d: ('giant_electric_ball_explosion', structs.decode_BIG_Q),
    0x3dcf98a5: ('part_0x3dcf98a5', structs.decode_BIG_Q),
    0xdc17fb84: ('part_0xdc17fb84', structs.decode_BIG_Q),
    0xc35db9ce: ('part_0xc35db9ce', structs.decode_BIG_Q),
    0xa70e1bbb: ('part_0xa70e1bbb', structs.decode_BIG_Q),
    0x7cc1b298: ('part_0x7cc1b298', structs.decode_BIG_Q),
    0x7be868ce: ('tornado_dust', structs.decode_BIG_Q),
    0xc90cda8c: ('ring_idle_effect', structs.decode_BIG_Q),
    0x4d9ed8e1: ('ring_energize_effect', structs.decode_BIG_Q),
    0x21dc4c35: ('ring_projectile', structs.decode_BIG_Q),
    0xcb673da3: ('ring_explosion_effect', structs.decode_BIG_Q),
    0xc1bbbed8: ('wheel_portal_effect', structs.decode_BIG_Q),
    0xf4386c42: ('wheel_tumble_effect', structs.decode_BIG_Q),
    0xe3c3de5e: ('wheel_projectile_cluster_effect', structs.decode_BIG_Q),
    0x1899c839: ('wheel_burst_electricity', structs.decode_BIG_Q),
    0x6b6606b8: ('wheel_seeker_electricity', structs.decode_BIG_Q),
    0x3b6cdadb: ('wheel_targetable_effect', structs.decode_BIG_Q),
    0xa6e942ed: ('wheel_non_targetable_effect', structs.decode_BIG_Q),
    0x21ec3d21: ('wheel_energy_beam', _decode_wheel_energy_beam),
    0x82ee63c8: ('wheel_tumble_world_collision', structs.decode_BIG_Q),
    0xab0a66da: ('wheel_muzzle_flash_effect', structs.decode_BIG_Q),
    0x5b67a4e7: ('visor_blow_out_texture', structs.decode_BIG_Q),
    0x4f6e81a8: ('visor_blow_out_max_size', structs.decode_BIG_f),
    0xad6ecc7f: ('interface_delayed_effect', structs.decode_BIG_Q),
    0x91d5f317: ('scan_sphere_form', structs.decode_BIG_Q),
    0x1ddfd45a: ('scan_tornado_form', structs.decode_BIG_Q),
    0x01fba748: ('scan_wheel_form', structs.decode_BIG_Q),
    0xcd2f3d00: ('scan_ring_form', structs.decode_BIG_Q),
    0xae813f86: ('scan_giant_form', structs.decode_BIG_Q),
    0xd27e8786: ('scan_chainsaw_form', structs.decode_BIG_Q),
    0x9a469187: ('caud_0x9a469187', structs.decode_BIG_Q),
    0xa959b017: ('caud_0xa959b017', structs.decode_BIG_Q),
}
