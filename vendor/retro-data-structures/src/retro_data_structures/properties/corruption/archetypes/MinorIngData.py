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
from retro_data_structures.properties.corruption.archetypes.GrappleData import GrappleData
from retro_data_structures.properties.corruption.archetypes.LaunchProjectileData import LaunchProjectileData
from retro_data_structures.properties.corruption.archetypes.PuddleControlData import PuddleControlData
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class MinorIngDataJson(typing_extensions.TypedDict):
        projectile: json_util.JsonObject
        projectile_delay_min: float
        projectile_delay_max: float
        min_puddle_time: float
        speed: float
        contact_damage: json_util.JsonObject
        contact_damage_frequency: float
        dot_damage: json_util.JsonObject
        dot_frequency: float
        dot_duration: float
        shell_start_duration: float
        splash_delay: float
        min_splash_speed: float
        max_splash_speed: float
        min_splash_speed_scale: float
        max_splash_speed_scale: float
        min_wake_speed: float
        texture_align_delay: float
        normal: json_util.JsonObject
        explosion: json_util.JsonObject
        contact: json_util.JsonObject
        blob_effect: int
        hit_normal_damage: int
        hit_heavy_damage: int
        death: int
        explosion_splash: int
        contact_splash: int
        ball_shell_start: int
        ball_shell_continue: int
        ball_shell_end: int
        ball_wake: int
        ball_wake_end: int
        sound_ball_shell_continue: int
        sound_ball_shell_end: int
        sound_touch: int
        sound_hit_normal_damage: int
        sound_hit_heavy_damage: int
        sound_death: int
        vulnerability: json_util.JsonObject
        grapple_data: json_util.JsonObject
    

@dataclasses.dataclass()
class MinorIngData(BaseProperty):
    projectile: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0x2c83c012, original_name='Projectile', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    projectile_delay_min: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdb254386, original_name='ProjectileDelayMin'
        ),
    })
    projectile_delay_max: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3d45ec67, original_name='ProjectileDelayMax'
        ),
    })
    min_puddle_time: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xefdc8306, original_name='MinPuddleTime'
        ),
    })
    speed: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6392404e, original_name='Speed'
        ),
    })
    contact_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xd756416e, original_name='ContactDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    contact_damage_frequency: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x49f4c4ee, original_name='ContactDamageFrequency'
        ),
    })
    dot_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xa7a47350, original_name='DotDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    dot_frequency: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x955a61ef, original_name='DotFrequency'
        ),
    })
    dot_duration: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x77a4efb5, original_name='DotDuration'
        ),
    })
    shell_start_duration: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x45134ace, original_name='ShellStartDuration'
        ),
    })
    splash_delay: float = dataclasses.field(default=0.20000000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0x308d4f23, original_name='SplashDelay'
        ),
    })
    min_splash_speed: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x26797df9, original_name='MinSplashSpeed'
        ),
    })
    max_splash_speed: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x814dfd80, original_name='MaxSplashSpeed'
        ),
    })
    min_splash_speed_scale: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa6bc177f, original_name='MinSplashSpeedScale'
        ),
    })
    max_splash_speed_scale: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7d034498, original_name='MaxSplashSpeedScale'
        ),
    })
    min_wake_speed: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa4985156, original_name='MinWakeSpeed'
        ),
    })
    texture_align_delay: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x91d5b3ca, original_name='TextureAlignDelay'
        ),
    })
    normal: PuddleControlData = dataclasses.field(default_factory=PuddleControlData, metadata={
        'reflection': FieldReflection[PuddleControlData](
            PuddleControlData, id=0x5ee136e3, original_name='Normal', from_json=PuddleControlData.from_json, to_json=PuddleControlData.to_json
        ),
    })
    explosion: PuddleControlData = dataclasses.field(default_factory=PuddleControlData, metadata={
        'reflection': FieldReflection[PuddleControlData](
            PuddleControlData, id=0xfd6d2b52, original_name='Explosion', from_json=PuddleControlData.from_json, to_json=PuddleControlData.to_json
        ),
    })
    contact: PuddleControlData = dataclasses.field(default_factory=PuddleControlData, metadata={
        'reflection': FieldReflection[PuddleControlData](
            PuddleControlData, id=0x17b1c55e, original_name='Contact', from_json=PuddleControlData.from_json, to_json=PuddleControlData.to_json
        ),
    })
    blob_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2367f689, original_name='BlobEffect'
        ),
    })
    hit_normal_damage: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd473158d, original_name='HitNormalDamage'
        ),
    })
    hit_heavy_damage: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xcca298b4, original_name='HitHeavyDamage'
        ),
    })
    death: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb99c80d3, original_name='Death'
        ),
    })
    explosion_splash: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x96ea9f4b, original_name='ExplosionSplash'
        ),
    })
    contact_splash: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x21655924, original_name='ContactSplash'
        ),
    })
    ball_shell_start: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe482bca4, original_name='BallShellStart'
        ),
    })
    ball_shell_continue: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x812e9cc8, original_name='BallShellContinue'
        ),
    })
    ball_shell_end: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xaeade325, original_name='BallShellEnd'
        ),
    })
    ball_wake: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x10cffad6, original_name='BallWake'
        ),
    })
    ball_wake_end: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x78685eb2, original_name='BallWakeEnd'
        ),
    })
    sound_ball_shell_continue: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x7027ee36, original_name='Sound_BallShellContinue'
        ),
    })
    sound_ball_shell_end: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x8a53608d, original_name='Sound_BallShellEnd'
        ),
    })
    sound_touch: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xf349baac, original_name='Sound_Touch'
        ),
    })
    sound_hit_normal_damage: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x49b30de2, original_name='Sound_HitNormalDamage'
        ),
    })
    sound_hit_heavy_damage: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xdecd5831, original_name='Sound_HitHeavyDamage'
        ),
    })
    sound_death: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x1b412c4b, original_name='Sound_Death'
        ),
    })
    vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x7b71ae90, original_name='Vulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    grapple_data: GrappleData = dataclasses.field(default_factory=GrappleData, metadata={
        'reflection': FieldReflection[GrappleData](
            GrappleData, id=0xf609c637, original_name='GrappleData', from_json=GrappleData.from_json, to_json=GrappleData.to_json
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
        if property_count != 40:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2c83c012
        projectile = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdb254386
        projectile_delay_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3d45ec67
        projectile_delay_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xefdc8306
        min_puddle_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6392404e
        speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd756416e
        contact_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49f4c4ee
        contact_damage_frequency = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa7a47350
        dot_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x955a61ef
        dot_frequency = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77a4efb5
        dot_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x45134ace
        shell_start_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x308d4f23
        splash_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x26797df9
        min_splash_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x814dfd80
        max_splash_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa6bc177f
        min_splash_speed_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7d034498
        max_splash_speed_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa4985156
        min_wake_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x91d5b3ca
        texture_align_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5ee136e3
        normal = PuddleControlData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfd6d2b52
        explosion = PuddleControlData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x17b1c55e
        contact = PuddleControlData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2367f689
        blob_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd473158d
        hit_normal_damage = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcca298b4
        hit_heavy_damage = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb99c80d3
        death = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x96ea9f4b
        explosion_splash = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21655924
        contact_splash = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe482bca4
        ball_shell_start = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x812e9cc8
        ball_shell_continue = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaeade325
        ball_shell_end = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x10cffad6
        ball_wake = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78685eb2
        ball_wake_end = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7027ee36
        sound_ball_shell_continue = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8a53608d
        sound_ball_shell_end = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf349baac
        sound_touch = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x49b30de2
        sound_hit_normal_damage = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdecd5831
        sound_hit_heavy_damage = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1b412c4b
        sound_death = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7b71ae90
        vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf609c637
        grapple_data = GrappleData.from_stream(data, game, property_size, default_override={'grapple_type': 1})
    
        return cls(projectile, projectile_delay_min, projectile_delay_max, min_puddle_time, speed, contact_damage, contact_damage_frequency, dot_damage, dot_frequency, dot_duration, shell_start_duration, splash_delay, min_splash_speed, max_splash_speed, min_splash_speed_scale, max_splash_speed_scale, min_wake_speed, texture_align_delay, normal, explosion, contact, blob_effect, hit_normal_damage, hit_heavy_damage, death, explosion_splash, contact_splash, ball_shell_start, ball_shell_continue, ball_shell_end, ball_wake, ball_wake_end, sound_ball_shell_continue, sound_ball_shell_end, sound_touch, sound_hit_normal_damage, sound_hit_heavy_damage, sound_death, vulnerability, grapple_data)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00(')  # 40 properties

        data.write(b',\x83\xc0\x12')  # 0x2c83c012
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.projectile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xdb%C\x86')  # 0xdb254386
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.projectile_delay_min))

        data.write(b'=E\xecg')  # 0x3d45ec67
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.projectile_delay_max))

        data.write(b'\xef\xdc\x83\x06')  # 0xefdc8306
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_puddle_time))

        data.write(b'c\x92@N')  # 0x6392404e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.speed))

        data.write(b'\xd7VAn')  # 0xd756416e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.contact_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'I\xf4\xc4\xee')  # 0x49f4c4ee
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.contact_damage_frequency))

        data.write(b'\xa7\xa4sP')  # 0xa7a47350
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.dot_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x95Za\xef')  # 0x955a61ef
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dot_frequency))

        data.write(b'w\xa4\xef\xb5')  # 0x77a4efb5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dot_duration))

        data.write(b'E\x13J\xce')  # 0x45134ace
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.shell_start_duration))

        data.write(b'0\x8dO#')  # 0x308d4f23
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.splash_delay))

        data.write(b'&y}\xf9')  # 0x26797df9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_splash_speed))

        data.write(b'\x81M\xfd\x80')  # 0x814dfd80
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_splash_speed))

        data.write(b'\xa6\xbc\x17\x7f')  # 0xa6bc177f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_splash_speed_scale))

        data.write(b'}\x03D\x98')  # 0x7d034498
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_splash_speed_scale))

        data.write(b'\xa4\x98QV')  # 0xa4985156
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_wake_speed))

        data.write(b'\x91\xd5\xb3\xca')  # 0x91d5b3ca
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.texture_align_delay))

        data.write(b'^\xe16\xe3')  # 0x5ee136e3
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.normal.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfdm+R')  # 0xfd6d2b52
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.explosion.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x17\xb1\xc5^')  # 0x17b1c55e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.contact.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'#g\xf6\x89')  # 0x2367f689
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.blob_effect))

        data.write(b'\xd4s\x15\x8d')  # 0xd473158d
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.hit_normal_damage))

        data.write(b'\xcc\xa2\x98\xb4')  # 0xcca298b4
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.hit_heavy_damage))

        data.write(b'\xb9\x9c\x80\xd3')  # 0xb99c80d3
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.death))

        data.write(b'\x96\xea\x9fK')  # 0x96ea9f4b
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.explosion_splash))

        data.write(b'!eY$')  # 0x21655924
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.contact_splash))

        data.write(b'\xe4\x82\xbc\xa4')  # 0xe482bca4
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ball_shell_start))

        data.write(b'\x81.\x9c\xc8')  # 0x812e9cc8
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ball_shell_continue))

        data.write(b'\xae\xad\xe3%')  # 0xaeade325
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ball_shell_end))

        data.write(b'\x10\xcf\xfa\xd6')  # 0x10cffad6
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ball_wake))

        data.write(b'xh^\xb2')  # 0x78685eb2
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ball_wake_end))

        data.write(b"p'\xee6")  # 0x7027ee36
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_ball_shell_continue))

        data.write(b'\x8aS`\x8d')  # 0x8a53608d
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_ball_shell_end))

        data.write(b'\xf3I\xba\xac')  # 0xf349baac
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_touch))

        data.write(b'I\xb3\r\xe2')  # 0x49b30de2
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_hit_normal_damage))

        data.write(b'\xde\xcdX1')  # 0xdecd5831
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_hit_heavy_damage))

        data.write(b'\x1bA,K')  # 0x1b412c4b
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_death))

        data.write(b'{q\xae\x90')  # 0x7b71ae90
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf6\t\xc67')  # 0xf609c637
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grapple_data.to_stream(data, game, default_override={'grapple_type': 1})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MinorIngDataJson", data)
        return cls(
            projectile=LaunchProjectileData.from_json(json_data['projectile']),
            projectile_delay_min=json_data['projectile_delay_min'],
            projectile_delay_max=json_data['projectile_delay_max'],
            min_puddle_time=json_data['min_puddle_time'],
            speed=json_data['speed'],
            contact_damage=DamageInfo.from_json(json_data['contact_damage']),
            contact_damage_frequency=json_data['contact_damage_frequency'],
            dot_damage=DamageInfo.from_json(json_data['dot_damage']),
            dot_frequency=json_data['dot_frequency'],
            dot_duration=json_data['dot_duration'],
            shell_start_duration=json_data['shell_start_duration'],
            splash_delay=json_data['splash_delay'],
            min_splash_speed=json_data['min_splash_speed'],
            max_splash_speed=json_data['max_splash_speed'],
            min_splash_speed_scale=json_data['min_splash_speed_scale'],
            max_splash_speed_scale=json_data['max_splash_speed_scale'],
            min_wake_speed=json_data['min_wake_speed'],
            texture_align_delay=json_data['texture_align_delay'],
            normal=PuddleControlData.from_json(json_data['normal']),
            explosion=PuddleControlData.from_json(json_data['explosion']),
            contact=PuddleControlData.from_json(json_data['contact']),
            blob_effect=json_data['blob_effect'],
            hit_normal_damage=json_data['hit_normal_damage'],
            hit_heavy_damage=json_data['hit_heavy_damage'],
            death=json_data['death'],
            explosion_splash=json_data['explosion_splash'],
            contact_splash=json_data['contact_splash'],
            ball_shell_start=json_data['ball_shell_start'],
            ball_shell_continue=json_data['ball_shell_continue'],
            ball_shell_end=json_data['ball_shell_end'],
            ball_wake=json_data['ball_wake'],
            ball_wake_end=json_data['ball_wake_end'],
            sound_ball_shell_continue=json_data['sound_ball_shell_continue'],
            sound_ball_shell_end=json_data['sound_ball_shell_end'],
            sound_touch=json_data['sound_touch'],
            sound_hit_normal_damage=json_data['sound_hit_normal_damage'],
            sound_hit_heavy_damage=json_data['sound_hit_heavy_damage'],
            sound_death=json_data['sound_death'],
            vulnerability=DamageVulnerability.from_json(json_data['vulnerability']),
            grapple_data=GrappleData.from_json(json_data['grapple_data']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'projectile': self.projectile.to_json(),
            'projectile_delay_min': self.projectile_delay_min,
            'projectile_delay_max': self.projectile_delay_max,
            'min_puddle_time': self.min_puddle_time,
            'speed': self.speed,
            'contact_damage': self.contact_damage.to_json(),
            'contact_damage_frequency': self.contact_damage_frequency,
            'dot_damage': self.dot_damage.to_json(),
            'dot_frequency': self.dot_frequency,
            'dot_duration': self.dot_duration,
            'shell_start_duration': self.shell_start_duration,
            'splash_delay': self.splash_delay,
            'min_splash_speed': self.min_splash_speed,
            'max_splash_speed': self.max_splash_speed,
            'min_splash_speed_scale': self.min_splash_speed_scale,
            'max_splash_speed_scale': self.max_splash_speed_scale,
            'min_wake_speed': self.min_wake_speed,
            'texture_align_delay': self.texture_align_delay,
            'normal': self.normal.to_json(),
            'explosion': self.explosion.to_json(),
            'contact': self.contact.to_json(),
            'blob_effect': self.blob_effect,
            'hit_normal_damage': self.hit_normal_damage,
            'hit_heavy_damage': self.hit_heavy_damage,
            'death': self.death,
            'explosion_splash': self.explosion_splash,
            'contact_splash': self.contact_splash,
            'ball_shell_start': self.ball_shell_start,
            'ball_shell_continue': self.ball_shell_continue,
            'ball_shell_end': self.ball_shell_end,
            'ball_wake': self.ball_wake,
            'ball_wake_end': self.ball_wake_end,
            'sound_ball_shell_continue': self.sound_ball_shell_continue,
            'sound_ball_shell_end': self.sound_ball_shell_end,
            'sound_touch': self.sound_touch,
            'sound_hit_normal_damage': self.sound_hit_normal_damage,
            'sound_hit_heavy_damage': self.sound_hit_heavy_damage,
            'sound_death': self.sound_death,
            'vulnerability': self.vulnerability.to_json(),
            'grapple_data': self.grapple_data.to_json(),
        }

    def _dependencies_for_blob_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.blob_effect)

    def _dependencies_for_hit_normal_damage(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.hit_normal_damage)

    def _dependencies_for_hit_heavy_damage(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.hit_heavy_damage)

    def _dependencies_for_death(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.death)

    def _dependencies_for_explosion_splash(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.explosion_splash)

    def _dependencies_for_contact_splash(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.contact_splash)

    def _dependencies_for_ball_shell_start(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ball_shell_start)

    def _dependencies_for_ball_shell_continue(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ball_shell_continue)

    def _dependencies_for_ball_shell_end(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ball_shell_end)

    def _dependencies_for_ball_wake(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ball_wake)

    def _dependencies_for_ball_wake_end(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ball_wake_end)

    def _dependencies_for_sound_ball_shell_continue(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_ball_shell_continue)

    def _dependencies_for_sound_ball_shell_end(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_ball_shell_end)

    def _dependencies_for_sound_touch(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_touch)

    def _dependencies_for_sound_hit_normal_damage(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_hit_normal_damage)

    def _dependencies_for_sound_hit_heavy_damage(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_hit_heavy_damage)

    def _dependencies_for_sound_death(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_death)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.projectile.dependencies_for, "projectile", "LaunchProjectileData"),
            (self.normal.dependencies_for, "normal", "PuddleControlData"),
            (self.explosion.dependencies_for, "explosion", "PuddleControlData"),
            (self.contact.dependencies_for, "contact", "PuddleControlData"),
            (self._dependencies_for_blob_effect, "blob_effect", "AssetId"),
            (self._dependencies_for_hit_normal_damage, "hit_normal_damage", "AssetId"),
            (self._dependencies_for_hit_heavy_damage, "hit_heavy_damage", "AssetId"),
            (self._dependencies_for_death, "death", "AssetId"),
            (self._dependencies_for_explosion_splash, "explosion_splash", "AssetId"),
            (self._dependencies_for_contact_splash, "contact_splash", "AssetId"),
            (self._dependencies_for_ball_shell_start, "ball_shell_start", "AssetId"),
            (self._dependencies_for_ball_shell_continue, "ball_shell_continue", "AssetId"),
            (self._dependencies_for_ball_shell_end, "ball_shell_end", "AssetId"),
            (self._dependencies_for_ball_wake, "ball_wake", "AssetId"),
            (self._dependencies_for_ball_wake_end, "ball_wake_end", "AssetId"),
            (self._dependencies_for_sound_ball_shell_continue, "sound_ball_shell_continue", "AssetId"),
            (self._dependencies_for_sound_ball_shell_end, "sound_ball_shell_end", "AssetId"),
            (self._dependencies_for_sound_touch, "sound_touch", "AssetId"),
            (self._dependencies_for_sound_hit_normal_damage, "sound_hit_normal_damage", "AssetId"),
            (self._dependencies_for_sound_hit_heavy_damage, "sound_hit_heavy_damage", "AssetId"),
            (self._dependencies_for_sound_death, "sound_death", "AssetId"),
            (self.grapple_data.dependencies_for, "grapple_data", "GrappleData"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for MinorIngData.{field_name} ({field_type}): {e}"
                )


def _decode_projectile(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_contact_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_dot_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_normal(data: typing.BinaryIO, game: Game, property_size: int) -> PuddleControlData:
    return PuddleControlData.from_stream(data, game, property_size)


def _decode_explosion(data: typing.BinaryIO, game: Game, property_size: int) -> PuddleControlData:
    return PuddleControlData.from_stream(data, game, property_size)


def _decode_contact(data: typing.BinaryIO, game: Game, property_size: int) -> PuddleControlData:
    return PuddleControlData.from_stream(data, game, property_size)


def _decode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_grapple_data(data: typing.BinaryIO, game: Game, property_size: int) -> GrappleData:
    return GrappleData.from_stream(data, game, property_size, default_override={'grapple_type': 1})


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x2c83c012: ('projectile', _decode_projectile),
    0xdb254386: ('projectile_delay_min', structs.decode_BIG_f),
    0x3d45ec67: ('projectile_delay_max', structs.decode_BIG_f),
    0xefdc8306: ('min_puddle_time', structs.decode_BIG_f),
    0x6392404e: ('speed', structs.decode_BIG_f),
    0xd756416e: ('contact_damage', _decode_contact_damage),
    0x49f4c4ee: ('contact_damage_frequency', structs.decode_BIG_f),
    0xa7a47350: ('dot_damage', _decode_dot_damage),
    0x955a61ef: ('dot_frequency', structs.decode_BIG_f),
    0x77a4efb5: ('dot_duration', structs.decode_BIG_f),
    0x45134ace: ('shell_start_duration', structs.decode_BIG_f),
    0x308d4f23: ('splash_delay', structs.decode_BIG_f),
    0x26797df9: ('min_splash_speed', structs.decode_BIG_f),
    0x814dfd80: ('max_splash_speed', structs.decode_BIG_f),
    0xa6bc177f: ('min_splash_speed_scale', structs.decode_BIG_f),
    0x7d034498: ('max_splash_speed_scale', structs.decode_BIG_f),
    0xa4985156: ('min_wake_speed', structs.decode_BIG_f),
    0x91d5b3ca: ('texture_align_delay', structs.decode_BIG_f),
    0x5ee136e3: ('normal', _decode_normal),
    0xfd6d2b52: ('explosion', _decode_explosion),
    0x17b1c55e: ('contact', _decode_contact),
    0x2367f689: ('blob_effect', structs.decode_BIG_Q),
    0xd473158d: ('hit_normal_damage', structs.decode_BIG_Q),
    0xcca298b4: ('hit_heavy_damage', structs.decode_BIG_Q),
    0xb99c80d3: ('death', structs.decode_BIG_Q),
    0x96ea9f4b: ('explosion_splash', structs.decode_BIG_Q),
    0x21655924: ('contact_splash', structs.decode_BIG_Q),
    0xe482bca4: ('ball_shell_start', structs.decode_BIG_Q),
    0x812e9cc8: ('ball_shell_continue', structs.decode_BIG_Q),
    0xaeade325: ('ball_shell_end', structs.decode_BIG_Q),
    0x10cffad6: ('ball_wake', structs.decode_BIG_Q),
    0x78685eb2: ('ball_wake_end', structs.decode_BIG_Q),
    0x7027ee36: ('sound_ball_shell_continue', structs.decode_BIG_Q),
    0x8a53608d: ('sound_ball_shell_end', structs.decode_BIG_Q),
    0xf349baac: ('sound_touch', structs.decode_BIG_Q),
    0x49b30de2: ('sound_hit_normal_damage', structs.decode_BIG_Q),
    0xdecd5831: ('sound_hit_heavy_damage', structs.decode_BIG_Q),
    0x1b412c4b: ('sound_death', structs.decode_BIG_Q),
    0x7b71ae90: ('vulnerability', _decode_vulnerability),
    0xf609c637: ('grapple_data', _decode_grapple_data),
}
