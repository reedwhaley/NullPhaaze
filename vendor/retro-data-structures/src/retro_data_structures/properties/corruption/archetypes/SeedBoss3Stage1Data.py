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
from retro_data_structures.properties.corruption.archetypes.GrappleData import GrappleData
from retro_data_structures.properties.corruption.archetypes.LaunchProjectileData import LaunchProjectileData
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SeedBoss3Stage1DataJson(typing_extensions.TypedDict):
        health: float
        heart_vulnerability: json_util.JsonObject
        body_vulnerability: json_util.JsonObject
        mouth_vulnerability: json_util.JsonObject
        stun_threshold: float
        stun_decay: float
        stun_delay_min: float
        stun_delay_max: float
        stun_delay_never_grappled_min: float
        stun_delay_never_grappled_max: float
        wander_distance: float
        too_far_distance: float
        dash_delay_maximum: float
        dash_delay_minimum: float
        dash_delay_variance: float
        grapple_data: json_util.JsonObject
        chest_open_time_min: float
        chest_open_time_max: float
        chest_stay_open_time_min: float
        chest_stay_open_time_max: float
        chest_close_time_min: float
        chest_close_time_max: float
        unknown_0x63f5b908: float
        stagger_threshold: float
        stagger_time_min: float
        stagger_time_max: float
        stagger_radius: float
        charge_fireball: json_util.JsonObject
        grapple_shimmer_model: int
        grapple_shimmer_joint_name: str
        unknown_0x20dc1c96: float
    

@dataclasses.dataclass()
class SeedBoss3Stage1Data(BaseProperty):
    health: float = dataclasses.field(default=750.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf0668919, original_name='Health'
        ),
    })
    heart_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xf064b3bc, original_name='HeartVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
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
    stun_delay_min: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x32b60fed, original_name='StunDelayMin'
        ),
    })
    stun_delay_max: float = dataclasses.field(default=6.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd4d6a00c, original_name='StunDelayMax'
        ),
    })
    stun_delay_never_grappled_min: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfefd7f33, original_name='StunDelayNeverGrappledMin'
        ),
    })
    stun_delay_never_grappled_max: float = dataclasses.field(default=12.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x189dd0d2, original_name='StunDelayNeverGrappledMax'
        ),
    })
    wander_distance: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xaf270c93, original_name='WanderDistance'
        ),
    })
    too_far_distance: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8819688d, original_name='TooFarDistance'
        ),
    })
    dash_delay_maximum: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1b37eda7, original_name='DashDelayMaximum'
        ),
    })
    dash_delay_minimum: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8b44fd4d, original_name='DashDelayMinimum'
        ),
    })
    dash_delay_variance: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdac05eb5, original_name='DashDelayVariance'
        ),
    })
    grapple_data: GrappleData = dataclasses.field(default_factory=GrappleData, metadata={
        'reflection': FieldReflection[GrappleData](
            GrappleData, id=0xf609c637, original_name='GrappleData', from_json=GrappleData.from_json, to_json=GrappleData.to_json
        ),
    })
    chest_open_time_min: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0fea8352, original_name='ChestOpenTimeMin'
        ),
    })
    chest_open_time_max: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe98a2cb3, original_name='ChestOpenTimeMax'
        ),
    })
    chest_stay_open_time_min: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xed52ab86, original_name='ChestStayOpenTimeMin'
        ),
    })
    chest_stay_open_time_max: float = dataclasses.field(default=7.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0b320467, original_name='ChestStayOpenTimeMax'
        ),
    })
    chest_close_time_min: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4bf067cb, original_name='ChestCloseTimeMin'
        ),
    })
    chest_close_time_max: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xad90c82a, original_name='ChestCloseTimeMax'
        ),
    })
    unknown_0x63f5b908: float = dataclasses.field(default=400.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x63f5b908, original_name='Unknown'
        ),
    })
    stagger_threshold: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5fae9a93, original_name='StaggerThreshold'
        ),
    })
    stagger_time_min: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x96ff34d5, original_name='StaggerTimeMin'
        ),
    })
    stagger_time_max: float = dataclasses.field(default=6.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x709f9b34, original_name='StaggerTimeMax'
        ),
    })
    stagger_radius: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x61e664cc, original_name='StaggerRadius'
        ),
    })
    charge_fireball: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0xb348c46b, original_name='ChargeFireball', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    grapple_shimmer_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x476d50f2, original_name='GrappleShimmerModel'
        ),
    })
    grapple_shimmer_joint_name: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x55da2ea4, original_name='GrappleShimmerJointName'
        ),
    })
    unknown_0x20dc1c96: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x20dc1c96, original_name='Unknown'
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
        if property_count != 31:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf0668919
        health = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf064b3bc
        heart_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0d9230d1
        body_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed7edca3
        mouth_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5bdd1e4c
        stun_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6082430f
        stun_decay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x32b60fed
        stun_delay_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd4d6a00c
        stun_delay_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfefd7f33
        stun_delay_never_grappled_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x189dd0d2
        stun_delay_never_grappled_max = structs.BIG_f.unpack(data.read(4))[0]
    
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
        assert property_id == 0xf609c637
        grapple_data = GrappleData.from_stream(data, game, property_size, default_override={'grapple_type': 1})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0fea8352
        chest_open_time_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe98a2cb3
        chest_open_time_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed52ab86
        chest_stay_open_time_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0b320467
        chest_stay_open_time_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4bf067cb
        chest_close_time_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xad90c82a
        chest_close_time_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x63f5b908
        unknown_0x63f5b908 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5fae9a93
        stagger_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x96ff34d5
        stagger_time_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x709f9b34
        stagger_time_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x61e664cc
        stagger_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb348c46b
        charge_fireball = LaunchProjectileData.from_stream(data, game, property_size, default_override={'burn_damage': 2.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x476d50f2
        grapple_shimmer_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x55da2ea4
        grapple_shimmer_joint_name = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x20dc1c96
        unknown_0x20dc1c96 = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(health, heart_vulnerability, body_vulnerability, mouth_vulnerability, stun_threshold, stun_decay, stun_delay_min, stun_delay_max, stun_delay_never_grappled_min, stun_delay_never_grappled_max, wander_distance, too_far_distance, dash_delay_maximum, dash_delay_minimum, dash_delay_variance, grapple_data, chest_open_time_min, chest_open_time_max, chest_stay_open_time_min, chest_stay_open_time_max, chest_close_time_min, chest_close_time_max, unknown_0x63f5b908, stagger_threshold, stagger_time_min, stagger_time_max, stagger_radius, charge_fireball, grapple_shimmer_model, grapple_shimmer_joint_name, unknown_0x20dc1c96)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x1f')  # 31 properties

        data.write(b'\xf0f\x89\x19')  # 0xf0668919
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.health))

        data.write(b'\xf0d\xb3\xbc')  # 0xf064b3bc
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.heart_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

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

        data.write(b'[\xdd\x1eL')  # 0x5bdd1e4c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stun_threshold))

        data.write(b'`\x82C\x0f')  # 0x6082430f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stun_decay))

        data.write(b'2\xb6\x0f\xed')  # 0x32b60fed
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stun_delay_min))

        data.write(b'\xd4\xd6\xa0\x0c')  # 0xd4d6a00c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stun_delay_max))

        data.write(b'\xfe\xfd\x7f3')  # 0xfefd7f33
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stun_delay_never_grappled_min))

        data.write(b'\x18\x9d\xd0\xd2')  # 0x189dd0d2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stun_delay_never_grappled_max))

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

        data.write(b'\xf6\t\xc67')  # 0xf609c637
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grapple_data.to_stream(data, game, default_override={'grapple_type': 1})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x0f\xea\x83R')  # 0xfea8352
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.chest_open_time_min))

        data.write(b'\xe9\x8a,\xb3')  # 0xe98a2cb3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.chest_open_time_max))

        data.write(b'\xedR\xab\x86')  # 0xed52ab86
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.chest_stay_open_time_min))

        data.write(b'\x0b2\x04g')  # 0xb320467
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.chest_stay_open_time_max))

        data.write(b'K\xf0g\xcb')  # 0x4bf067cb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.chest_close_time_min))

        data.write(b'\xad\x90\xc8*')  # 0xad90c82a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.chest_close_time_max))

        data.write(b'c\xf5\xb9\x08')  # 0x63f5b908
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x63f5b908))

        data.write(b'_\xae\x9a\x93')  # 0x5fae9a93
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stagger_threshold))

        data.write(b'\x96\xff4\xd5')  # 0x96ff34d5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stagger_time_min))

        data.write(b'p\x9f\x9b4')  # 0x709f9b34
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stagger_time_max))

        data.write(b'a\xe6d\xcc')  # 0x61e664cc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stagger_radius))

        data.write(b'\xb3H\xc4k')  # 0xb348c46b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.charge_fireball.to_stream(data, game, default_override={'burn_damage': 2.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'GmP\xf2')  # 0x476d50f2
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.grapple_shimmer_model))

        data.write(b'U\xda.\xa4')  # 0x55da2ea4
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.grapple_shimmer_joint_name.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b' \xdc\x1c\x96')  # 0x20dc1c96
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x20dc1c96))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SeedBoss3Stage1DataJson", data)
        return cls(
            health=json_data['health'],
            heart_vulnerability=DamageVulnerability.from_json(json_data['heart_vulnerability']),
            body_vulnerability=DamageVulnerability.from_json(json_data['body_vulnerability']),
            mouth_vulnerability=DamageVulnerability.from_json(json_data['mouth_vulnerability']),
            stun_threshold=json_data['stun_threshold'],
            stun_decay=json_data['stun_decay'],
            stun_delay_min=json_data['stun_delay_min'],
            stun_delay_max=json_data['stun_delay_max'],
            stun_delay_never_grappled_min=json_data['stun_delay_never_grappled_min'],
            stun_delay_never_grappled_max=json_data['stun_delay_never_grappled_max'],
            wander_distance=json_data['wander_distance'],
            too_far_distance=json_data['too_far_distance'],
            dash_delay_maximum=json_data['dash_delay_maximum'],
            dash_delay_minimum=json_data['dash_delay_minimum'],
            dash_delay_variance=json_data['dash_delay_variance'],
            grapple_data=GrappleData.from_json(json_data['grapple_data']),
            chest_open_time_min=json_data['chest_open_time_min'],
            chest_open_time_max=json_data['chest_open_time_max'],
            chest_stay_open_time_min=json_data['chest_stay_open_time_min'],
            chest_stay_open_time_max=json_data['chest_stay_open_time_max'],
            chest_close_time_min=json_data['chest_close_time_min'],
            chest_close_time_max=json_data['chest_close_time_max'],
            unknown_0x63f5b908=json_data['unknown_0x63f5b908'],
            stagger_threshold=json_data['stagger_threshold'],
            stagger_time_min=json_data['stagger_time_min'],
            stagger_time_max=json_data['stagger_time_max'],
            stagger_radius=json_data['stagger_radius'],
            charge_fireball=LaunchProjectileData.from_json(json_data['charge_fireball']),
            grapple_shimmer_model=json_data['grapple_shimmer_model'],
            grapple_shimmer_joint_name=json_data['grapple_shimmer_joint_name'],
            unknown_0x20dc1c96=json_data['unknown_0x20dc1c96'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'health': self.health,
            'heart_vulnerability': self.heart_vulnerability.to_json(),
            'body_vulnerability': self.body_vulnerability.to_json(),
            'mouth_vulnerability': self.mouth_vulnerability.to_json(),
            'stun_threshold': self.stun_threshold,
            'stun_decay': self.stun_decay,
            'stun_delay_min': self.stun_delay_min,
            'stun_delay_max': self.stun_delay_max,
            'stun_delay_never_grappled_min': self.stun_delay_never_grappled_min,
            'stun_delay_never_grappled_max': self.stun_delay_never_grappled_max,
            'wander_distance': self.wander_distance,
            'too_far_distance': self.too_far_distance,
            'dash_delay_maximum': self.dash_delay_maximum,
            'dash_delay_minimum': self.dash_delay_minimum,
            'dash_delay_variance': self.dash_delay_variance,
            'grapple_data': self.grapple_data.to_json(),
            'chest_open_time_min': self.chest_open_time_min,
            'chest_open_time_max': self.chest_open_time_max,
            'chest_stay_open_time_min': self.chest_stay_open_time_min,
            'chest_stay_open_time_max': self.chest_stay_open_time_max,
            'chest_close_time_min': self.chest_close_time_min,
            'chest_close_time_max': self.chest_close_time_max,
            'unknown_0x63f5b908': self.unknown_0x63f5b908,
            'stagger_threshold': self.stagger_threshold,
            'stagger_time_min': self.stagger_time_min,
            'stagger_time_max': self.stagger_time_max,
            'stagger_radius': self.stagger_radius,
            'charge_fireball': self.charge_fireball.to_json(),
            'grapple_shimmer_model': self.grapple_shimmer_model,
            'grapple_shimmer_joint_name': self.grapple_shimmer_joint_name,
            'unknown_0x20dc1c96': self.unknown_0x20dc1c96,
        }

    def _dependencies_for_grapple_shimmer_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.grapple_shimmer_model)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.grapple_data.dependencies_for, "grapple_data", "GrappleData"),
            (self.charge_fireball.dependencies_for, "charge_fireball", "LaunchProjectileData"),
            (self._dependencies_for_grapple_shimmer_model, "grapple_shimmer_model", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for SeedBoss3Stage1Data.{field_name} ({field_type}): {e}"
                )


def _decode_heart_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_body_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_mouth_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_grapple_data(data: typing.BinaryIO, game: Game, property_size: int) -> GrappleData:
    return GrappleData.from_stream(data, game, property_size, default_override={'grapple_type': 1})


def _decode_charge_fireball(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size, default_override={'burn_damage': 2.0})


def _decode_grapple_shimmer_joint_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xf0668919: ('health', structs.decode_BIG_f),
    0xf064b3bc: ('heart_vulnerability', _decode_heart_vulnerability),
    0x0d9230d1: ('body_vulnerability', _decode_body_vulnerability),
    0xed7edca3: ('mouth_vulnerability', _decode_mouth_vulnerability),
    0x5bdd1e4c: ('stun_threshold', structs.decode_BIG_f),
    0x6082430f: ('stun_decay', structs.decode_BIG_f),
    0x32b60fed: ('stun_delay_min', structs.decode_BIG_f),
    0xd4d6a00c: ('stun_delay_max', structs.decode_BIG_f),
    0xfefd7f33: ('stun_delay_never_grappled_min', structs.decode_BIG_f),
    0x189dd0d2: ('stun_delay_never_grappled_max', structs.decode_BIG_f),
    0xaf270c93: ('wander_distance', structs.decode_BIG_f),
    0x8819688d: ('too_far_distance', structs.decode_BIG_f),
    0x1b37eda7: ('dash_delay_maximum', structs.decode_BIG_f),
    0x8b44fd4d: ('dash_delay_minimum', structs.decode_BIG_f),
    0xdac05eb5: ('dash_delay_variance', structs.decode_BIG_f),
    0xf609c637: ('grapple_data', _decode_grapple_data),
    0x0fea8352: ('chest_open_time_min', structs.decode_BIG_f),
    0xe98a2cb3: ('chest_open_time_max', structs.decode_BIG_f),
    0xed52ab86: ('chest_stay_open_time_min', structs.decode_BIG_f),
    0x0b320467: ('chest_stay_open_time_max', structs.decode_BIG_f),
    0x4bf067cb: ('chest_close_time_min', structs.decode_BIG_f),
    0xad90c82a: ('chest_close_time_max', structs.decode_BIG_f),
    0x63f5b908: ('unknown_0x63f5b908', structs.decode_BIG_f),
    0x5fae9a93: ('stagger_threshold', structs.decode_BIG_f),
    0x96ff34d5: ('stagger_time_min', structs.decode_BIG_f),
    0x709f9b34: ('stagger_time_max', structs.decode_BIG_f),
    0x61e664cc: ('stagger_radius', structs.decode_BIG_f),
    0xb348c46b: ('charge_fireball', _decode_charge_fireball),
    0x476d50f2: ('grapple_shimmer_model', structs.decode_BIG_Q),
    0x55da2ea4: ('grapple_shimmer_joint_name', _decode_grapple_shimmer_joint_name),
    0x20dc1c96: ('unknown_0x20dc1c96', structs.decode_BIG_f),
}
