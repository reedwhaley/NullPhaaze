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
from retro_data_structures.properties.corruption.archetypes.UnknownStruct18 import UnknownStruct18
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SeedBoss3Stage2DataJson(typing_extensions.TypedDict):
        health: float
        animation_speed: float
        body_vulnerability: json_util.JsonObject
        mouth_vulnerability: json_util.JsonObject
        joint_vulnerability: json_util.JsonObject
        orb_vulnerability: json_util.JsonObject
        stun_threshold: float
        stun_decay: float
        wander_distance: float
        too_far_distance: float
        dash_delay_maximum: float
        dash_delay_minimum: float
        dash_delay_variance: float
        initial_stun_delay_max: float
        initial_stun_delay_min: float
        stun_delay_max: float
        stun_delay_min: float
        visor_blow_out_time: float
        unknown_0x20dc1c96: float
        orb_radius_start_ratio: float
        orb_radius_end_ratio: float
        orb_radius_delta: float
        orb_damage_threshold: float
        unknown_0xd7d24bfa: int
        unknown_struct18: json_util.JsonObject
        joint_target_alpha_dim: float
        joint_target_alpha_full: float
        unknown_0x530ecf07: float
        joint_target_radius_x_ray: float
        joint_target_radius_other: float
        left_joint_collision_set_name: str
        left_target_attachment: int
        left_target_joint_name: str
        right_joint_collision_set_name: str
        right_target_attachment: int
        right_target_joint_name: str
        left_armor_attachment: int
        left_armor_joint_name: str
        right_armor_attachment: int
        right_armor_joint_name: str
        chest_armor_attachment: int
        chest_armor_joint_name: str
    

@dataclasses.dataclass()
class SeedBoss3Stage2Data(BaseProperty):
    health: float = dataclasses.field(default=750.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf0668919, original_name='Health'
        ),
    })
    animation_speed: float = dataclasses.field(default=1.0499999523162842, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc5407757, original_name='AnimationSpeed'
        ),
    })
    body_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x0d9230d1, original_name='BodyVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    mouth_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xed7edca3, original_name='MouthVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    joint_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x295cf609, original_name='JointVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    orb_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x23ddbb55, original_name='OrbVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    stun_threshold: float = dataclasses.field(default=80.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5bdd1e4c, original_name='StunThreshold'
        ),
    })
    stun_decay: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6082430f, original_name='StunDecay'
        ),
    })
    wander_distance: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xaf270c93, original_name='WanderDistance'
        ),
    })
    too_far_distance: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8819688d, original_name='TooFarDistance'
        ),
    })
    dash_delay_maximum: float = dataclasses.field(default=18.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1b37eda7, original_name='DashDelayMaximum'
        ),
    })
    dash_delay_minimum: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8b44fd4d, original_name='DashDelayMinimum'
        ),
    })
    dash_delay_variance: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdac05eb5, original_name='DashDelayVariance'
        ),
    })
    initial_stun_delay_max: float = dataclasses.field(default=24.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x673a2724, original_name='InitialStunDelayMax'
        ),
    })
    initial_stun_delay_min: float = dataclasses.field(default=16.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x815a88c5, original_name='InitialStunDelayMin'
        ),
    })
    stun_delay_max: float = dataclasses.field(default=12.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd4d6a00c, original_name='StunDelayMax'
        ),
    })
    stun_delay_min: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x32b60fed, original_name='StunDelayMin'
        ),
    })
    visor_blow_out_time: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x86e154b4, original_name='VisorBlowOutTime'
        ),
    })
    unknown_0x20dc1c96: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x20dc1c96, original_name='Unknown'
        ),
    })
    orb_radius_start_ratio: float = dataclasses.field(default=0.009999999776482582, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfba7c57b, original_name='OrbRadiusStartRatio'
        ),
    })
    orb_radius_end_ratio: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xba801f2f, original_name='OrbRadiusEndRatio'
        ),
    })
    orb_radius_delta: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe1ee4260, original_name='OrbRadiusDelta'
        ),
    })
    orb_damage_threshold: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8e080314, original_name='OrbDamageThreshold'
        ),
    })
    unknown_0xd7d24bfa: int = dataclasses.field(default=3, metadata={
        'reflection': FieldReflection[int](
            int, id=0xd7d24bfa, original_name='Unknown'
        ),
    })
    unknown_struct18: UnknownStruct18 = dataclasses.field(default_factory=UnknownStruct18, metadata={
        'reflection': FieldReflection[UnknownStruct18](
            UnknownStruct18, id=0xcccca97e, original_name='UnknownStruct18', from_json=UnknownStruct18.from_json, to_json=UnknownStruct18.to_json
        ),
    })
    joint_target_alpha_dim: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa62404dc, original_name='JointTargetAlphaDim'
        ),
    })
    joint_target_alpha_full: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbf8b57bf, original_name='JointTargetAlphaFull'
        ),
    })
    unknown_0x530ecf07: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x530ecf07, original_name='Unknown'
        ),
    })
    joint_target_radius_x_ray: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8482e270, original_name='JointTargetRadiusXRay'
        ),
    })
    joint_target_radius_other: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7128f60e, original_name='JointTargetRadiusOther'
        ),
    })
    left_joint_collision_set_name: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xd9c4aa53, original_name='LeftJointCollisionSetName'
        ),
    })
    left_target_attachment: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x8e13f1f6, original_name='LeftTargetAttachment'
        ),
    })
    left_target_joint_name: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x71c8e644, original_name='LeftTargetJointName'
        ),
    })
    right_joint_collision_set_name: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x8cb60fc9, original_name='RightJointCollisionSetName'
        ),
    })
    right_target_attachment: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x69a25f05, original_name='RightTargetAttachment'
        ),
    })
    right_target_joint_name: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x967948b7, original_name='RightTargetJointName'
        ),
    })
    left_armor_attachment: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x0a366c12, original_name='LeftArmorAttachment'
        ),
    })
    left_armor_joint_name: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xf5ed7ba0, original_name='LeftArmorJointName'
        ),
    })
    right_armor_attachment: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x03b5981c, original_name='RightArmorAttachment'
        ),
    })
    right_armor_joint_name: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xfc6e8fae, original_name='RightArmorJointName'
        ),
    })
    chest_armor_attachment: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xbb5658b3, original_name='ChestArmorAttachment'
        ),
    })
    chest_armor_joint_name: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x448d4f01, original_name='ChestArmorJointName'
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
        if property_count != 42:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf0668919
        health = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc5407757
        animation_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0d9230d1
        body_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed7edca3
        mouth_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x295cf609
        joint_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23ddbb55
        orb_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5bdd1e4c
        stun_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6082430f
        stun_decay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaf270c93
        wander_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8819688d
        too_far_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1b37eda7
        dash_delay_maximum = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8b44fd4d
        dash_delay_minimum = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdac05eb5
        dash_delay_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x673a2724
        initial_stun_delay_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x815a88c5
        initial_stun_delay_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd4d6a00c
        stun_delay_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32b60fed
        stun_delay_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x86e154b4
        visor_blow_out_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x20dc1c96
        unknown_0x20dc1c96 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfba7c57b
        orb_radius_start_ratio = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xba801f2f
        orb_radius_end_ratio = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe1ee4260
        orb_radius_delta = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8e080314
        orb_damage_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd7d24bfa
        unknown_0xd7d24bfa = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcccca97e
        unknown_struct18 = UnknownStruct18.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa62404dc
        joint_target_alpha_dim = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbf8b57bf
        joint_target_alpha_full = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x530ecf07
        unknown_0x530ecf07 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8482e270
        joint_target_radius_x_ray = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7128f60e
        joint_target_radius_other = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd9c4aa53
        left_joint_collision_set_name = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8e13f1f6
        left_target_attachment = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71c8e644
        left_target_joint_name = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8cb60fc9
        right_joint_collision_set_name = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x69a25f05
        right_target_attachment = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x967948b7
        right_target_joint_name = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0a366c12
        left_armor_attachment = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf5ed7ba0
        left_armor_joint_name = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03b5981c
        right_armor_attachment = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfc6e8fae
        right_armor_joint_name = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbb5658b3
        chest_armor_attachment = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x448d4f01
        chest_armor_joint_name = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        return cls(health, animation_speed, body_vulnerability, mouth_vulnerability, joint_vulnerability, orb_vulnerability, stun_threshold, stun_decay, wander_distance, too_far_distance, dash_delay_maximum, dash_delay_minimum, dash_delay_variance, initial_stun_delay_max, initial_stun_delay_min, stun_delay_max, stun_delay_min, visor_blow_out_time, unknown_0x20dc1c96, orb_radius_start_ratio, orb_radius_end_ratio, orb_radius_delta, orb_damage_threshold, unknown_0xd7d24bfa, unknown_struct18, joint_target_alpha_dim, joint_target_alpha_full, unknown_0x530ecf07, joint_target_radius_x_ray, joint_target_radius_other, left_joint_collision_set_name, left_target_attachment, left_target_joint_name, right_joint_collision_set_name, right_target_attachment, right_target_joint_name, left_armor_attachment, left_armor_joint_name, right_armor_attachment, right_armor_joint_name, chest_armor_attachment, chest_armor_joint_name)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00*')  # 42 properties

        data.write(b'\xf0f\x89\x19')  # 0xf0668919
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.health))

        data.write(b'\xc5@wW')  # 0xc5407757
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.animation_speed))

        data.write(b'\r\x920\xd1')  # 0xd9230d1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.body_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xed~\xdc\xa3')  # 0xed7edca3
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.mouth_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b')\\\xf6\t')  # 0x295cf609
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.joint_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'#\xdd\xbbU')  # 0x23ddbb55
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.orb_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'[\xdd\x1eL')  # 0x5bdd1e4c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stun_threshold))

        data.write(b'`\x82C\x0f')  # 0x6082430f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stun_decay))

        data.write(b"\xaf'\x0c\x93")  # 0xaf270c93
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.wander_distance))

        data.write(b'\x88\x19h\x8d')  # 0x8819688d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.too_far_distance))

        data.write(b'\x1b7\xed\xa7')  # 0x1b37eda7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dash_delay_maximum))

        data.write(b'\x8bD\xfdM')  # 0x8b44fd4d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dash_delay_minimum))

        data.write(b'\xda\xc0^\xb5')  # 0xdac05eb5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dash_delay_variance))

        data.write(b"g:'$")  # 0x673a2724
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.initial_stun_delay_max))

        data.write(b'\x81Z\x88\xc5')  # 0x815a88c5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.initial_stun_delay_min))

        data.write(b'\xd4\xd6\xa0\x0c')  # 0xd4d6a00c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stun_delay_max))

        data.write(b'2\xb6\x0f\xed')  # 0x32b60fed
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stun_delay_min))

        data.write(b'\x86\xe1T\xb4')  # 0x86e154b4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.visor_blow_out_time))

        data.write(b' \xdc\x1c\x96')  # 0x20dc1c96
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x20dc1c96))

        data.write(b'\xfb\xa7\xc5{')  # 0xfba7c57b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orb_radius_start_ratio))

        data.write(b'\xba\x80\x1f/')  # 0xba801f2f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orb_radius_end_ratio))

        data.write(b'\xe1\xeeB`')  # 0xe1ee4260
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orb_radius_delta))

        data.write(b'\x8e\x08\x03\x14')  # 0x8e080314
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.orb_damage_threshold))

        data.write(b'\xd7\xd2K\xfa')  # 0xd7d24bfa
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xd7d24bfa))

        data.write(b'\xcc\xcc\xa9~')  # 0xcccca97e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.unknown_struct18.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa6$\x04\xdc')  # 0xa62404dc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.joint_target_alpha_dim))

        data.write(b'\xbf\x8bW\xbf')  # 0xbf8b57bf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.joint_target_alpha_full))

        data.write(b'S\x0e\xcf\x07')  # 0x530ecf07
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x530ecf07))

        data.write(b'\x84\x82\xe2p')  # 0x8482e270
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.joint_target_radius_x_ray))

        data.write(b'q(\xf6\x0e')  # 0x7128f60e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.joint_target_radius_other))

        data.write(b'\xd9\xc4\xaaS')  # 0xd9c4aa53
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.left_joint_collision_set_name.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8e\x13\xf1\xf6')  # 0x8e13f1f6
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.left_target_attachment))

        data.write(b'q\xc8\xe6D')  # 0x71c8e644
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.left_target_joint_name.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8c\xb6\x0f\xc9')  # 0x8cb60fc9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.right_joint_collision_set_name.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'i\xa2_\x05')  # 0x69a25f05
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.right_target_attachment))

        data.write(b'\x96yH\xb7')  # 0x967948b7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.right_target_joint_name.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\n6l\x12')  # 0xa366c12
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.left_armor_attachment))

        data.write(b'\xf5\xed{\xa0')  # 0xf5ed7ba0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.left_armor_joint_name.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x03\xb5\x98\x1c')  # 0x3b5981c
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.right_armor_attachment))

        data.write(b'\xfcn\x8f\xae')  # 0xfc6e8fae
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.right_armor_joint_name.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbbVX\xb3')  # 0xbb5658b3
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.chest_armor_attachment))

        data.write(b'D\x8dO\x01')  # 0x448d4f01
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.chest_armor_joint_name.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SeedBoss3Stage2DataJson", data)
        return cls(
            health=json_data['health'],
            animation_speed=json_data['animation_speed'],
            body_vulnerability=DamageVulnerability.from_json(json_data['body_vulnerability']),
            mouth_vulnerability=DamageVulnerability.from_json(json_data['mouth_vulnerability']),
            joint_vulnerability=DamageVulnerability.from_json(json_data['joint_vulnerability']),
            orb_vulnerability=DamageVulnerability.from_json(json_data['orb_vulnerability']),
            stun_threshold=json_data['stun_threshold'],
            stun_decay=json_data['stun_decay'],
            wander_distance=json_data['wander_distance'],
            too_far_distance=json_data['too_far_distance'],
            dash_delay_maximum=json_data['dash_delay_maximum'],
            dash_delay_minimum=json_data['dash_delay_minimum'],
            dash_delay_variance=json_data['dash_delay_variance'],
            initial_stun_delay_max=json_data['initial_stun_delay_max'],
            initial_stun_delay_min=json_data['initial_stun_delay_min'],
            stun_delay_max=json_data['stun_delay_max'],
            stun_delay_min=json_data['stun_delay_min'],
            visor_blow_out_time=json_data['visor_blow_out_time'],
            unknown_0x20dc1c96=json_data['unknown_0x20dc1c96'],
            orb_radius_start_ratio=json_data['orb_radius_start_ratio'],
            orb_radius_end_ratio=json_data['orb_radius_end_ratio'],
            orb_radius_delta=json_data['orb_radius_delta'],
            orb_damage_threshold=json_data['orb_damage_threshold'],
            unknown_0xd7d24bfa=json_data['unknown_0xd7d24bfa'],
            unknown_struct18=UnknownStruct18.from_json(json_data['unknown_struct18']),
            joint_target_alpha_dim=json_data['joint_target_alpha_dim'],
            joint_target_alpha_full=json_data['joint_target_alpha_full'],
            unknown_0x530ecf07=json_data['unknown_0x530ecf07'],
            joint_target_radius_x_ray=json_data['joint_target_radius_x_ray'],
            joint_target_radius_other=json_data['joint_target_radius_other'],
            left_joint_collision_set_name=json_data['left_joint_collision_set_name'],
            left_target_attachment=json_data['left_target_attachment'],
            left_target_joint_name=json_data['left_target_joint_name'],
            right_joint_collision_set_name=json_data['right_joint_collision_set_name'],
            right_target_attachment=json_data['right_target_attachment'],
            right_target_joint_name=json_data['right_target_joint_name'],
            left_armor_attachment=json_data['left_armor_attachment'],
            left_armor_joint_name=json_data['left_armor_joint_name'],
            right_armor_attachment=json_data['right_armor_attachment'],
            right_armor_joint_name=json_data['right_armor_joint_name'],
            chest_armor_attachment=json_data['chest_armor_attachment'],
            chest_armor_joint_name=json_data['chest_armor_joint_name'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'health': self.health,
            'animation_speed': self.animation_speed,
            'body_vulnerability': self.body_vulnerability.to_json(),
            'mouth_vulnerability': self.mouth_vulnerability.to_json(),
            'joint_vulnerability': self.joint_vulnerability.to_json(),
            'orb_vulnerability': self.orb_vulnerability.to_json(),
            'stun_threshold': self.stun_threshold,
            'stun_decay': self.stun_decay,
            'wander_distance': self.wander_distance,
            'too_far_distance': self.too_far_distance,
            'dash_delay_maximum': self.dash_delay_maximum,
            'dash_delay_minimum': self.dash_delay_minimum,
            'dash_delay_variance': self.dash_delay_variance,
            'initial_stun_delay_max': self.initial_stun_delay_max,
            'initial_stun_delay_min': self.initial_stun_delay_min,
            'stun_delay_max': self.stun_delay_max,
            'stun_delay_min': self.stun_delay_min,
            'visor_blow_out_time': self.visor_blow_out_time,
            'unknown_0x20dc1c96': self.unknown_0x20dc1c96,
            'orb_radius_start_ratio': self.orb_radius_start_ratio,
            'orb_radius_end_ratio': self.orb_radius_end_ratio,
            'orb_radius_delta': self.orb_radius_delta,
            'orb_damage_threshold': self.orb_damage_threshold,
            'unknown_0xd7d24bfa': self.unknown_0xd7d24bfa,
            'unknown_struct18': self.unknown_struct18.to_json(),
            'joint_target_alpha_dim': self.joint_target_alpha_dim,
            'joint_target_alpha_full': self.joint_target_alpha_full,
            'unknown_0x530ecf07': self.unknown_0x530ecf07,
            'joint_target_radius_x_ray': self.joint_target_radius_x_ray,
            'joint_target_radius_other': self.joint_target_radius_other,
            'left_joint_collision_set_name': self.left_joint_collision_set_name,
            'left_target_attachment': self.left_target_attachment,
            'left_target_joint_name': self.left_target_joint_name,
            'right_joint_collision_set_name': self.right_joint_collision_set_name,
            'right_target_attachment': self.right_target_attachment,
            'right_target_joint_name': self.right_target_joint_name,
            'left_armor_attachment': self.left_armor_attachment,
            'left_armor_joint_name': self.left_armor_joint_name,
            'right_armor_attachment': self.right_armor_attachment,
            'right_armor_joint_name': self.right_armor_joint_name,
            'chest_armor_attachment': self.chest_armor_attachment,
            'chest_armor_joint_name': self.chest_armor_joint_name,
        }

    def _dependencies_for_left_target_attachment(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.left_target_attachment)

    def _dependencies_for_right_target_attachment(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.right_target_attachment)

    def _dependencies_for_left_armor_attachment(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.left_armor_attachment)

    def _dependencies_for_right_armor_attachment(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.right_armor_attachment)

    def _dependencies_for_chest_armor_attachment(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.chest_armor_attachment)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.unknown_struct18.dependencies_for, "unknown_struct18", "UnknownStruct18"),
            (self._dependencies_for_left_target_attachment, "left_target_attachment", "AssetId"),
            (self._dependencies_for_right_target_attachment, "right_target_attachment", "AssetId"),
            (self._dependencies_for_left_armor_attachment, "left_armor_attachment", "AssetId"),
            (self._dependencies_for_right_armor_attachment, "right_armor_attachment", "AssetId"),
            (self._dependencies_for_chest_armor_attachment, "chest_armor_attachment", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for SeedBoss3Stage2Data.{field_name} ({field_type}): {e}"
                )


def _decode_body_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_mouth_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_joint_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_orb_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_unknown_struct18(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct18:
    return UnknownStruct18.from_stream(data, game, property_size)


def _decode_left_joint_collision_set_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_left_target_joint_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_right_joint_collision_set_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_right_target_joint_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_left_armor_joint_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_right_armor_joint_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_chest_armor_joint_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xf0668919: ('health', structs.decode_BIG_f),
    0xc5407757: ('animation_speed', structs.decode_BIG_f),
    0x0d9230d1: ('body_vulnerability', _decode_body_vulnerability),
    0xed7edca3: ('mouth_vulnerability', _decode_mouth_vulnerability),
    0x295cf609: ('joint_vulnerability', _decode_joint_vulnerability),
    0x23ddbb55: ('orb_vulnerability', _decode_orb_vulnerability),
    0x5bdd1e4c: ('stun_threshold', structs.decode_BIG_f),
    0x6082430f: ('stun_decay', structs.decode_BIG_f),
    0xaf270c93: ('wander_distance', structs.decode_BIG_f),
    0x8819688d: ('too_far_distance', structs.decode_BIG_f),
    0x1b37eda7: ('dash_delay_maximum', structs.decode_BIG_f),
    0x8b44fd4d: ('dash_delay_minimum', structs.decode_BIG_f),
    0xdac05eb5: ('dash_delay_variance', structs.decode_BIG_f),
    0x673a2724: ('initial_stun_delay_max', structs.decode_BIG_f),
    0x815a88c5: ('initial_stun_delay_min', structs.decode_BIG_f),
    0xd4d6a00c: ('stun_delay_max', structs.decode_BIG_f),
    0x32b60fed: ('stun_delay_min', structs.decode_BIG_f),
    0x86e154b4: ('visor_blow_out_time', structs.decode_BIG_f),
    0x20dc1c96: ('unknown_0x20dc1c96', structs.decode_BIG_f),
    0xfba7c57b: ('orb_radius_start_ratio', structs.decode_BIG_f),
    0xba801f2f: ('orb_radius_end_ratio', structs.decode_BIG_f),
    0xe1ee4260: ('orb_radius_delta', structs.decode_BIG_f),
    0x8e080314: ('orb_damage_threshold', structs.decode_BIG_f),
    0xd7d24bfa: ('unknown_0xd7d24bfa', structs.decode_BIG_l),
    0xcccca97e: ('unknown_struct18', _decode_unknown_struct18),
    0xa62404dc: ('joint_target_alpha_dim', structs.decode_BIG_f),
    0xbf8b57bf: ('joint_target_alpha_full', structs.decode_BIG_f),
    0x530ecf07: ('unknown_0x530ecf07', structs.decode_BIG_f),
    0x8482e270: ('joint_target_radius_x_ray', structs.decode_BIG_f),
    0x7128f60e: ('joint_target_radius_other', structs.decode_BIG_f),
    0xd9c4aa53: ('left_joint_collision_set_name', _decode_left_joint_collision_set_name),
    0x8e13f1f6: ('left_target_attachment', structs.decode_BIG_Q),
    0x71c8e644: ('left_target_joint_name', _decode_left_target_joint_name),
    0x8cb60fc9: ('right_joint_collision_set_name', _decode_right_joint_collision_set_name),
    0x69a25f05: ('right_target_attachment', structs.decode_BIG_Q),
    0x967948b7: ('right_target_joint_name', _decode_right_target_joint_name),
    0x0a366c12: ('left_armor_attachment', structs.decode_BIG_Q),
    0xf5ed7ba0: ('left_armor_joint_name', _decode_left_armor_joint_name),
    0x03b5981c: ('right_armor_attachment', structs.decode_BIG_Q),
    0xfc6e8fae: ('right_armor_joint_name', _decode_right_armor_joint_name),
    0xbb5658b3: ('chest_armor_attachment', structs.decode_BIG_Q),
    0x448d4f01: ('chest_armor_joint_name', _decode_chest_armor_joint_name),
}
