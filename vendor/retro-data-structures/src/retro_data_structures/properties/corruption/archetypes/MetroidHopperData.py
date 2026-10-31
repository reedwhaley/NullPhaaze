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
from retro_data_structures.properties.corruption.archetypes.LaunchProjectileData import LaunchProjectileData
from retro_data_structures.properties.corruption.archetypes.MetroidHopperHypermodeData import MetroidHopperHypermodeData
from retro_data_structures.properties.corruption.archetypes.TeamAIDebugEnum import TeamAIDebugEnum
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class MetroidHopperDataJson(typing_extensions.TypedDict):
        animation_speed: float
        hearing_range: float
        alert_animation_chance: float
        unknown_0x87c38060: bool
        jump_apex: float
        gravity_constant: float
        min_melee_attack_dist: float
        max_melee_attack_dist: float
        unknown_0x68e4097e: float
        light_melee_damage_info: json_util.JsonObject
        heavy_melee_damage_info: json_util.JsonObject
        min_projectile_attack_dist: float
        max_projectile_attack_dist: float
        projectile_info: json_util.JsonObject
        melee_chance: float
        projectile_chance: float
        normal_hyper_mode: json_util.JsonObject
        hard_hyper_mode: json_util.JsonObject
        elite_hyper_mode: json_util.JsonObject
        hypermode_clear_effect: int
        hypermode_clear_sound: int
        super_hopper_explosion_radius: float
        super_hopper_explosion_fx: int
        super_hopper_explosion_damage: json_util.JsonObject
        team_ai_debug_type: json_util.JsonObject
        debug_patrol: bool
    

@dataclasses.dataclass()
class MetroidHopperData(BaseProperty):
    animation_speed: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc5407757, original_name='AnimationSpeed'
        ),
    })
    hearing_range: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x25474550, original_name='HearingRange'
        ),
    })
    alert_animation_chance: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe6496376, original_name='AlertAnimationChance'
        ),
    })
    unknown_0x87c38060: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x87c38060, original_name='Unknown'
        ),
    })
    jump_apex: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf2782501, original_name='JumpApex'
        ),
    })
    gravity_constant: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7f38dccb, original_name='GravityConstant'
        ),
    })
    min_melee_attack_dist: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x01b7d6b1, original_name='MinMeleeAttackDist'
        ),
    })
    max_melee_attack_dist: float = dataclasses.field(default=11.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x052de79b, original_name='MaxMeleeAttackDist'
        ),
    })
    unknown_0x68e4097e: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x68e4097e, original_name='Unknown'
        ),
    })
    light_melee_damage_info: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x2b76b9f1, original_name='LightMeleeDamageInfo', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    heavy_melee_damage_info: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x9ef4a101, original_name='HeavyMeleeDamageInfo', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    min_projectile_attack_dist: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x500683fc, original_name='MinProjectileAttackDist'
        ),
    })
    max_projectile_attack_dist: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0708d3bf, original_name='MaxProjectileAttackDist'
        ),
    })
    projectile_info: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0xf9ef8d5d, original_name='ProjectileInfo', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    melee_chance: float = dataclasses.field(default=0.6000000238418579, metadata={
        'reflection': FieldReflection[float](
            float, id=0xaecfea2d, original_name='MeleeChance'
        ),
    })
    projectile_chance: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2a7d0101, original_name='ProjectileChance'
        ),
    })
    normal_hyper_mode: MetroidHopperHypermodeData = dataclasses.field(default_factory=MetroidHopperHypermodeData, metadata={
        'reflection': FieldReflection[MetroidHopperHypermodeData](
            MetroidHopperHypermodeData, id=0xd5a8e2da, original_name='NormalHyperMode', from_json=MetroidHopperHypermodeData.from_json, to_json=MetroidHopperHypermodeData.to_json
        ),
    })
    hard_hyper_mode: MetroidHopperHypermodeData = dataclasses.field(default_factory=MetroidHopperHypermodeData, metadata={
        'reflection': FieldReflection[MetroidHopperHypermodeData](
            MetroidHopperHypermodeData, id=0x184991da, original_name='HardHyperMode', from_json=MetroidHopperHypermodeData.from_json, to_json=MetroidHopperHypermodeData.to_json
        ),
    })
    elite_hyper_mode: MetroidHopperHypermodeData = dataclasses.field(default_factory=MetroidHopperHypermodeData, metadata={
        'reflection': FieldReflection[MetroidHopperHypermodeData](
            MetroidHopperHypermodeData, id=0x7b07aca3, original_name='EliteHyperMode', from_json=MetroidHopperHypermodeData.from_json, to_json=MetroidHopperHypermodeData.to_json
        ),
    })
    hypermode_clear_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['ELSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5dde5b25, original_name='HypermodeClearEffect'
        ),
    })
    hypermode_clear_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xf95d2033, original_name='HypermodeClearSound'
        ),
    })
    super_hopper_explosion_radius: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1da1b117, original_name='SuperHopperExplosionRadius'
        ),
    })
    super_hopper_explosion_fx: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe0700022, original_name='SuperHopperExplosionFX'
        ),
    })
    super_hopper_explosion_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xd1f6c520, original_name='SuperHopperExplosionDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    team_ai_debug_type: TeamAIDebugEnum = dataclasses.field(default_factory=TeamAIDebugEnum, metadata={
        'reflection': FieldReflection[TeamAIDebugEnum](
            TeamAIDebugEnum, id=0xfb648831, original_name='TeamAIDebugType', from_json=TeamAIDebugEnum.from_json, to_json=TeamAIDebugEnum.to_json
        ),
    })
    debug_patrol: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xbb389a82, original_name='DebugPatrol'
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
        if property_count != 26:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc5407757
        animation_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x25474550
        hearing_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe6496376
        alert_animation_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x87c38060
        unknown_0x87c38060 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf2782501
        jump_apex = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7f38dccb
        gravity_constant = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x01b7d6b1
        min_melee_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x052de79b
        max_melee_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68e4097e
        unknown_0x68e4097e = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2b76b9f1
        light_melee_damage_info = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9ef4a101
        heavy_melee_damage_info = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x500683fc
        min_projectile_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0708d3bf
        max_projectile_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf9ef8d5d
        projectile_info = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaecfea2d
        melee_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2a7d0101
        projectile_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd5a8e2da
        normal_hyper_mode = MetroidHopperHypermodeData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x184991da
        hard_hyper_mode = MetroidHopperHypermodeData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7b07aca3
        elite_hyper_mode = MetroidHopperHypermodeData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5dde5b25
        hypermode_clear_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf95d2033
        hypermode_clear_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1da1b117
        super_hopper_explosion_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe0700022
        super_hopper_explosion_fx = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd1f6c520
        super_hopper_explosion_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfb648831
        team_ai_debug_type = TeamAIDebugEnum.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbb389a82
        debug_patrol = structs.BIG_bool_.unpack(data.read(1))[0]
    
        return cls(animation_speed, hearing_range, alert_animation_chance, unknown_0x87c38060, jump_apex, gravity_constant, min_melee_attack_dist, max_melee_attack_dist, unknown_0x68e4097e, light_melee_damage_info, heavy_melee_damage_info, min_projectile_attack_dist, max_projectile_attack_dist, projectile_info, melee_chance, projectile_chance, normal_hyper_mode, hard_hyper_mode, elite_hyper_mode, hypermode_clear_effect, hypermode_clear_sound, super_hopper_explosion_radius, super_hopper_explosion_fx, super_hopper_explosion_damage, team_ai_debug_type, debug_patrol)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x1a')  # 26 properties

        data.write(b'\xc5@wW')  # 0xc5407757
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.animation_speed))

        data.write(b'%GEP')  # 0x25474550
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hearing_range))

        data.write(b'\xe6Icv')  # 0xe6496376
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.alert_animation_chance))

        data.write(b'\x87\xc3\x80`')  # 0x87c38060
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x87c38060))

        data.write(b'\xf2x%\x01')  # 0xf2782501
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.jump_apex))

        data.write(b'\x7f8\xdc\xcb')  # 0x7f38dccb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.gravity_constant))

        data.write(b'\x01\xb7\xd6\xb1')  # 0x1b7d6b1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_melee_attack_dist))

        data.write(b'\x05-\xe7\x9b')  # 0x52de79b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_melee_attack_dist))

        data.write(b'h\xe4\t~')  # 0x68e4097e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x68e4097e))

        data.write(b'+v\xb9\xf1')  # 0x2b76b9f1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.light_melee_damage_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9e\xf4\xa1\x01')  # 0x9ef4a101
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.heavy_melee_damage_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'P\x06\x83\xfc')  # 0x500683fc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_projectile_attack_dist))

        data.write(b'\x07\x08\xd3\xbf')  # 0x708d3bf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_projectile_attack_dist))

        data.write(b'\xf9\xef\x8d]')  # 0xf9ef8d5d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.projectile_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xae\xcf\xea-')  # 0xaecfea2d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.melee_chance))

        data.write(b'*}\x01\x01')  # 0x2a7d0101
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.projectile_chance))

        data.write(b'\xd5\xa8\xe2\xda')  # 0xd5a8e2da
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.normal_hyper_mode.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x18I\x91\xda')  # 0x184991da
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hard_hyper_mode.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'{\x07\xac\xa3')  # 0x7b07aca3
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.elite_hyper_mode.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b']\xde[%')  # 0x5dde5b25
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.hypermode_clear_effect))

        data.write(b'\xf9] 3')  # 0xf95d2033
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.hypermode_clear_sound))

        data.write(b'\x1d\xa1\xb1\x17')  # 0x1da1b117
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.super_hopper_explosion_radius))

        data.write(b'\xe0p\x00"')  # 0xe0700022
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.super_hopper_explosion_fx))

        data.write(b'\xd1\xf6\xc5 ')  # 0xd1f6c520
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.super_hopper_explosion_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfbd\x881')  # 0xfb648831
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.team_ai_debug_type.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbb8\x9a\x82')  # 0xbb389a82
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.debug_patrol))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MetroidHopperDataJson", data)
        return cls(
            animation_speed=json_data['animation_speed'],
            hearing_range=json_data['hearing_range'],
            alert_animation_chance=json_data['alert_animation_chance'],
            unknown_0x87c38060=json_data['unknown_0x87c38060'],
            jump_apex=json_data['jump_apex'],
            gravity_constant=json_data['gravity_constant'],
            min_melee_attack_dist=json_data['min_melee_attack_dist'],
            max_melee_attack_dist=json_data['max_melee_attack_dist'],
            unknown_0x68e4097e=json_data['unknown_0x68e4097e'],
            light_melee_damage_info=DamageInfo.from_json(json_data['light_melee_damage_info']),
            heavy_melee_damage_info=DamageInfo.from_json(json_data['heavy_melee_damage_info']),
            min_projectile_attack_dist=json_data['min_projectile_attack_dist'],
            max_projectile_attack_dist=json_data['max_projectile_attack_dist'],
            projectile_info=LaunchProjectileData.from_json(json_data['projectile_info']),
            melee_chance=json_data['melee_chance'],
            projectile_chance=json_data['projectile_chance'],
            normal_hyper_mode=MetroidHopperHypermodeData.from_json(json_data['normal_hyper_mode']),
            hard_hyper_mode=MetroidHopperHypermodeData.from_json(json_data['hard_hyper_mode']),
            elite_hyper_mode=MetroidHopperHypermodeData.from_json(json_data['elite_hyper_mode']),
            hypermode_clear_effect=json_data['hypermode_clear_effect'],
            hypermode_clear_sound=json_data['hypermode_clear_sound'],
            super_hopper_explosion_radius=json_data['super_hopper_explosion_radius'],
            super_hopper_explosion_fx=json_data['super_hopper_explosion_fx'],
            super_hopper_explosion_damage=DamageInfo.from_json(json_data['super_hopper_explosion_damage']),
            team_ai_debug_type=TeamAIDebugEnum.from_json(json_data['team_ai_debug_type']),
            debug_patrol=json_data['debug_patrol'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'animation_speed': self.animation_speed,
            'hearing_range': self.hearing_range,
            'alert_animation_chance': self.alert_animation_chance,
            'unknown_0x87c38060': self.unknown_0x87c38060,
            'jump_apex': self.jump_apex,
            'gravity_constant': self.gravity_constant,
            'min_melee_attack_dist': self.min_melee_attack_dist,
            'max_melee_attack_dist': self.max_melee_attack_dist,
            'unknown_0x68e4097e': self.unknown_0x68e4097e,
            'light_melee_damage_info': self.light_melee_damage_info.to_json(),
            'heavy_melee_damage_info': self.heavy_melee_damage_info.to_json(),
            'min_projectile_attack_dist': self.min_projectile_attack_dist,
            'max_projectile_attack_dist': self.max_projectile_attack_dist,
            'projectile_info': self.projectile_info.to_json(),
            'melee_chance': self.melee_chance,
            'projectile_chance': self.projectile_chance,
            'normal_hyper_mode': self.normal_hyper_mode.to_json(),
            'hard_hyper_mode': self.hard_hyper_mode.to_json(),
            'elite_hyper_mode': self.elite_hyper_mode.to_json(),
            'hypermode_clear_effect': self.hypermode_clear_effect,
            'hypermode_clear_sound': self.hypermode_clear_sound,
            'super_hopper_explosion_radius': self.super_hopper_explosion_radius,
            'super_hopper_explosion_fx': self.super_hopper_explosion_fx,
            'super_hopper_explosion_damage': self.super_hopper_explosion_damage.to_json(),
            'team_ai_debug_type': self.team_ai_debug_type.to_json(),
            'debug_patrol': self.debug_patrol,
        }

    def _dependencies_for_hypermode_clear_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.hypermode_clear_effect)

    def _dependencies_for_hypermode_clear_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.hypermode_clear_sound)

    def _dependencies_for_super_hopper_explosion_fx(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.super_hopper_explosion_fx)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.projectile_info.dependencies_for, "projectile_info", "LaunchProjectileData"),
            (self.normal_hyper_mode.dependencies_for, "normal_hyper_mode", "MetroidHopperHypermodeData"),
            (self.hard_hyper_mode.dependencies_for, "hard_hyper_mode", "MetroidHopperHypermodeData"),
            (self.elite_hyper_mode.dependencies_for, "elite_hyper_mode", "MetroidHopperHypermodeData"),
            (self._dependencies_for_hypermode_clear_effect, "hypermode_clear_effect", "AssetId"),
            (self._dependencies_for_hypermode_clear_sound, "hypermode_clear_sound", "AssetId"),
            (self._dependencies_for_super_hopper_explosion_fx, "super_hopper_explosion_fx", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for MetroidHopperData.{field_name} ({field_type}): {e}"
                )


def _decode_light_melee_damage_info(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_heavy_melee_damage_info(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_projectile_info(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_normal_hyper_mode(data: typing.BinaryIO, game: Game, property_size: int) -> MetroidHopperHypermodeData:
    return MetroidHopperHypermodeData.from_stream(data, game, property_size)


def _decode_hard_hyper_mode(data: typing.BinaryIO, game: Game, property_size: int) -> MetroidHopperHypermodeData:
    return MetroidHopperHypermodeData.from_stream(data, game, property_size)


def _decode_elite_hyper_mode(data: typing.BinaryIO, game: Game, property_size: int) -> MetroidHopperHypermodeData:
    return MetroidHopperHypermodeData.from_stream(data, game, property_size)


def _decode_super_hopper_explosion_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_team_ai_debug_type(data: typing.BinaryIO, game: Game, property_size: int) -> TeamAIDebugEnum:
    return TeamAIDebugEnum.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xc5407757: ('animation_speed', structs.decode_BIG_f),
    0x25474550: ('hearing_range', structs.decode_BIG_f),
    0xe6496376: ('alert_animation_chance', structs.decode_BIG_f),
    0x87c38060: ('unknown_0x87c38060', structs.decode_BIG_bool_),
    0xf2782501: ('jump_apex', structs.decode_BIG_f),
    0x7f38dccb: ('gravity_constant', structs.decode_BIG_f),
    0x01b7d6b1: ('min_melee_attack_dist', structs.decode_BIG_f),
    0x052de79b: ('max_melee_attack_dist', structs.decode_BIG_f),
    0x68e4097e: ('unknown_0x68e4097e', structs.decode_BIG_f),
    0x2b76b9f1: ('light_melee_damage_info', _decode_light_melee_damage_info),
    0x9ef4a101: ('heavy_melee_damage_info', _decode_heavy_melee_damage_info),
    0x500683fc: ('min_projectile_attack_dist', structs.decode_BIG_f),
    0x0708d3bf: ('max_projectile_attack_dist', structs.decode_BIG_f),
    0xf9ef8d5d: ('projectile_info', _decode_projectile_info),
    0xaecfea2d: ('melee_chance', structs.decode_BIG_f),
    0x2a7d0101: ('projectile_chance', structs.decode_BIG_f),
    0xd5a8e2da: ('normal_hyper_mode', _decode_normal_hyper_mode),
    0x184991da: ('hard_hyper_mode', _decode_hard_hyper_mode),
    0x7b07aca3: ('elite_hyper_mode', _decode_elite_hyper_mode),
    0x5dde5b25: ('hypermode_clear_effect', structs.decode_BIG_Q),
    0xf95d2033: ('hypermode_clear_sound', structs.decode_BIG_Q),
    0x1da1b117: ('super_hopper_explosion_radius', structs.decode_BIG_f),
    0xe0700022: ('super_hopper_explosion_fx', structs.decode_BIG_Q),
    0xd1f6c520: ('super_hopper_explosion_damage', _decode_super_hopper_explosion_damage),
    0xfb648831: ('team_ai_debug_type', _decode_team_ai_debug_type),
    0xbb389a82: ('debug_patrol', structs.decode_BIG_bool_),
}
