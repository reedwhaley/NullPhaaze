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
from retro_data_structures.properties.corruption.archetypes.RagDollData import RagDollData
from retro_data_structures.properties.corruption.archetypes.StaticGeometryTest import StaticGeometryTest
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class FriendlyDataJson(typing_extensions.TypedDict):
        flotsam: bool
        rag_doll_properties: json_util.JsonObject
        unknown_0xbf443451: bool
        invulnerable: bool
        disable_knock_back_when_invulnerable: bool
        unknown_0xef5671d6: bool
        unknown_0xa4ae2178: bool
        avoidance_range: float
        unknown_0x02ac6274: bool
        unknown_0xaed1fba2: float
        unknown_0xb9a462fd: float
        unknown_0x9888c19c: float
        unknown_0x7f1279e1: float
        can_interrupt_fidget: bool
        shot_projectile: int
        sound_projectile: int
        shot_damage: json_util.JsonObject
        projectile_static_geometry_test_during_task: json_util.JsonObject
        projectile_static_geometry_test_during_combat: json_util.JsonObject
        burst_fire: int
        gun_model: int
        use_head_tracking: bool
        head_track_player_range: float
        head_track_target_range: float
        unknown_0x679e2937: bool
        hold_initial_animation: bool
        turn_threshold_when_walking: float
        turn_threshold_when_running: float
        unknown_0x3ea5a256: bool
        is_grabbable: bool
        is_a_target: bool
    

@dataclasses.dataclass()
class FriendlyData(BaseProperty):
    flotsam: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xc1d1e465, original_name='Flotsam'
        ),
    })
    rag_doll_properties: RagDollData = dataclasses.field(default_factory=RagDollData, metadata={
        'reflection': FieldReflection[RagDollData](
            RagDollData, id=0xa149701e, original_name='RagDollProperties', from_json=RagDollData.from_json, to_json=RagDollData.to_json
        ),
    })
    unknown_0xbf443451: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xbf443451, original_name='Unknown'
        ),
    })
    invulnerable: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x6652bdd7, original_name='Invulnerable'
        ),
    })
    disable_knock_back_when_invulnerable: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x41baf88d, original_name='DisableKnockBackWhenInvulnerable'
        ),
    })
    unknown_0xef5671d6: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xef5671d6, original_name='Unknown'
        ),
    })
    unknown_0xa4ae2178: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xa4ae2178, original_name='Unknown'
        ),
    })
    avoidance_range: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x50a9bd0d, original_name='AvoidanceRange'
        ),
    })
    unknown_0x02ac6274: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x02ac6274, original_name='Unknown'
        ),
    })
    unknown_0xaed1fba2: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xaed1fba2, original_name='Unknown'
        ),
    })
    unknown_0xb9a462fd: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb9a462fd, original_name='Unknown'
        ),
    })
    unknown_0x9888c19c: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9888c19c, original_name='Unknown'
        ),
    })
    unknown_0x7f1279e1: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7f1279e1, original_name='Unknown'
        ),
    })
    can_interrupt_fidget: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x662d5cc9, original_name='CanInterruptFidget'
        ),
    })
    shot_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x51253ba3, original_name='ShotProjectile'
        ),
    })
    sound_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x10e3efdd, original_name='Sound_Projectile'
        ),
    })
    shot_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xcea30138, original_name='ShotDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    projectile_static_geometry_test_during_task: StaticGeometryTest = dataclasses.field(default_factory=StaticGeometryTest, metadata={
        'reflection': FieldReflection[StaticGeometryTest](
            StaticGeometryTest, id=0x785c41f5, original_name='ProjectileStaticGeometryTestDuringTask', from_json=StaticGeometryTest.from_json, to_json=StaticGeometryTest.to_json
        ),
    })
    projectile_static_geometry_test_during_combat: StaticGeometryTest = dataclasses.field(default_factory=StaticGeometryTest, metadata={
        'reflection': FieldReflection[StaticGeometryTest](
            StaticGeometryTest, id=0xfc5a0a21, original_name='ProjectileStaticGeometryTestDuringCombat', from_json=StaticGeometryTest.from_json, to_json=StaticGeometryTest.to_json
        ),
    })
    burst_fire: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['BFRC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xfc34473f, original_name='BurstFire'
        ),
    })
    gun_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x50340852, original_name='GunModel'
        ),
    })
    use_head_tracking: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x2ea013a6, original_name='UseHeadTracking'
        ),
    })
    head_track_player_range: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x330619ca, original_name='HeadTrackPlayerRange'
        ),
    })
    head_track_target_range: float = dataclasses.field(default=1000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa7be5edf, original_name='HeadTrackTargetRange'
        ),
    })
    unknown_0x679e2937: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x679e2937, original_name='Unknown'
        ),
    })
    hold_initial_animation: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xf484e0ae, original_name='HoldInitialAnimation'
        ),
    })
    turn_threshold_when_walking: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xec3fde21, original_name='TurnThresholdWhenWalking'
        ),
    })
    turn_threshold_when_running: float = dataclasses.field(default=90.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x24d18b0a, original_name='TurnThresholdWhenRunning'
        ),
    })
    unknown_0x3ea5a256: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x3ea5a256, original_name='Unknown'
        ),
    })
    is_grabbable: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x66b099e0, original_name='IsGrabbable'
        ),
    })
    is_a_target: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xf5acd12e, original_name='IsATarget'
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
        assert property_id == 0xc1d1e465
        flotsam = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa149701e
        rag_doll_properties = RagDollData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbf443451
        unknown_0xbf443451 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6652bdd7
        invulnerable = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x41baf88d
        disable_knock_back_when_invulnerable = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xef5671d6
        unknown_0xef5671d6 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa4ae2178
        unknown_0xa4ae2178 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50a9bd0d
        avoidance_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x02ac6274
        unknown_0x02ac6274 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaed1fba2
        unknown_0xaed1fba2 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb9a462fd
        unknown_0xb9a462fd = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9888c19c
        unknown_0x9888c19c = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7f1279e1
        unknown_0x7f1279e1 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x662d5cc9
        can_interrupt_fidget = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x51253ba3
        shot_projectile = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x10e3efdd
        sound_projectile = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcea30138
        shot_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_damage': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x785c41f5
        projectile_static_geometry_test_during_task = StaticGeometryTest.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfc5a0a21
        projectile_static_geometry_test_during_combat = StaticGeometryTest.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfc34473f
        burst_fire = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50340852
        gun_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2ea013a6
        use_head_tracking = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x330619ca
        head_track_player_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa7be5edf
        head_track_target_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x679e2937
        unknown_0x679e2937 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf484e0ae
        hold_initial_animation = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xec3fde21
        turn_threshold_when_walking = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24d18b0a
        turn_threshold_when_running = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3ea5a256
        unknown_0x3ea5a256 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x66b099e0
        is_grabbable = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf5acd12e
        is_a_target = structs.BIG_bool_.unpack(data.read(1))[0]
    
        return cls(flotsam, rag_doll_properties, unknown_0xbf443451, invulnerable, disable_knock_back_when_invulnerable, unknown_0xef5671d6, unknown_0xa4ae2178, avoidance_range, unknown_0x02ac6274, unknown_0xaed1fba2, unknown_0xb9a462fd, unknown_0x9888c19c, unknown_0x7f1279e1, can_interrupt_fidget, shot_projectile, sound_projectile, shot_damage, projectile_static_geometry_test_during_task, projectile_static_geometry_test_during_combat, burst_fire, gun_model, use_head_tracking, head_track_player_range, head_track_target_range, unknown_0x679e2937, hold_initial_animation, turn_threshold_when_walking, turn_threshold_when_running, unknown_0x3ea5a256, is_grabbable, is_a_target)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x1f')  # 31 properties

        data.write(b'\xc1\xd1\xe4e')  # 0xc1d1e465
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.flotsam))

        data.write(b'\xa1Ip\x1e')  # 0xa149701e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.rag_doll_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbfD4Q')  # 0xbf443451
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xbf443451))

        data.write(b'fR\xbd\xd7')  # 0x6652bdd7
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.invulnerable))

        data.write(b'A\xba\xf8\x8d')  # 0x41baf88d
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.disable_knock_back_when_invulnerable))

        data.write(b'\xefVq\xd6')  # 0xef5671d6
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xef5671d6))

        data.write(b'\xa4\xae!x')  # 0xa4ae2178
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0xa4ae2178))

        data.write(b'P\xa9\xbd\r')  # 0x50a9bd0d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.avoidance_range))

        data.write(b'\x02\xacbt')  # 0x2ac6274
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x02ac6274))

        data.write(b'\xae\xd1\xfb\xa2')  # 0xaed1fba2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xaed1fba2))

        data.write(b'\xb9\xa4b\xfd')  # 0xb9a462fd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb9a462fd))

        data.write(b'\x98\x88\xc1\x9c')  # 0x9888c19c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x9888c19c))

        data.write(b'\x7f\x12y\xe1')  # 0x7f1279e1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x7f1279e1))

        data.write(b'f-\\\xc9')  # 0x662d5cc9
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.can_interrupt_fidget))

        data.write(b'Q%;\xa3')  # 0x51253ba3
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shot_projectile))

        data.write(b'\x10\xe3\xef\xdd')  # 0x10e3efdd
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound_projectile))

        data.write(b'\xce\xa3\x018')  # 0xcea30138
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shot_damage.to_stream(data, game, default_override={'di_damage': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'x\\A\xf5')  # 0x785c41f5
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.projectile_static_geometry_test_during_task.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfcZ\n!')  # 0xfc5a0a21
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.projectile_static_geometry_test_during_combat.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfc4G?')  # 0xfc34473f
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.burst_fire))

        data.write(b'P4\x08R')  # 0x50340852
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.gun_model))

        data.write(b'.\xa0\x13\xa6')  # 0x2ea013a6
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.use_head_tracking))

        data.write(b'3\x06\x19\xca')  # 0x330619ca
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.head_track_player_range))

        data.write(b'\xa7\xbe^\xdf')  # 0xa7be5edf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.head_track_target_range))

        data.write(b'g\x9e)7')  # 0x679e2937
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x679e2937))

        data.write(b'\xf4\x84\xe0\xae')  # 0xf484e0ae
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.hold_initial_animation))

        data.write(b'\xec?\xde!')  # 0xec3fde21
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.turn_threshold_when_walking))

        data.write(b'$\xd1\x8b\n')  # 0x24d18b0a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.turn_threshold_when_running))

        data.write(b'>\xa5\xa2V')  # 0x3ea5a256
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x3ea5a256))

        data.write(b'f\xb0\x99\xe0')  # 0x66b099e0
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_grabbable))

        data.write(b'\xf5\xac\xd1.')  # 0xf5acd12e
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_a_target))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FriendlyDataJson", data)
        return cls(
            flotsam=json_data['flotsam'],
            rag_doll_properties=RagDollData.from_json(json_data['rag_doll_properties']),
            unknown_0xbf443451=json_data['unknown_0xbf443451'],
            invulnerable=json_data['invulnerable'],
            disable_knock_back_when_invulnerable=json_data['disable_knock_back_when_invulnerable'],
            unknown_0xef5671d6=json_data['unknown_0xef5671d6'],
            unknown_0xa4ae2178=json_data['unknown_0xa4ae2178'],
            avoidance_range=json_data['avoidance_range'],
            unknown_0x02ac6274=json_data['unknown_0x02ac6274'],
            unknown_0xaed1fba2=json_data['unknown_0xaed1fba2'],
            unknown_0xb9a462fd=json_data['unknown_0xb9a462fd'],
            unknown_0x9888c19c=json_data['unknown_0x9888c19c'],
            unknown_0x7f1279e1=json_data['unknown_0x7f1279e1'],
            can_interrupt_fidget=json_data['can_interrupt_fidget'],
            shot_projectile=json_data['shot_projectile'],
            sound_projectile=json_data['sound_projectile'],
            shot_damage=DamageInfo.from_json(json_data['shot_damage']),
            projectile_static_geometry_test_during_task=StaticGeometryTest.from_json(json_data['projectile_static_geometry_test_during_task']),
            projectile_static_geometry_test_during_combat=StaticGeometryTest.from_json(json_data['projectile_static_geometry_test_during_combat']),
            burst_fire=json_data['burst_fire'],
            gun_model=json_data['gun_model'],
            use_head_tracking=json_data['use_head_tracking'],
            head_track_player_range=json_data['head_track_player_range'],
            head_track_target_range=json_data['head_track_target_range'],
            unknown_0x679e2937=json_data['unknown_0x679e2937'],
            hold_initial_animation=json_data['hold_initial_animation'],
            turn_threshold_when_walking=json_data['turn_threshold_when_walking'],
            turn_threshold_when_running=json_data['turn_threshold_when_running'],
            unknown_0x3ea5a256=json_data['unknown_0x3ea5a256'],
            is_grabbable=json_data['is_grabbable'],
            is_a_target=json_data['is_a_target'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'flotsam': self.flotsam,
            'rag_doll_properties': self.rag_doll_properties.to_json(),
            'unknown_0xbf443451': self.unknown_0xbf443451,
            'invulnerable': self.invulnerable,
            'disable_knock_back_when_invulnerable': self.disable_knock_back_when_invulnerable,
            'unknown_0xef5671d6': self.unknown_0xef5671d6,
            'unknown_0xa4ae2178': self.unknown_0xa4ae2178,
            'avoidance_range': self.avoidance_range,
            'unknown_0x02ac6274': self.unknown_0x02ac6274,
            'unknown_0xaed1fba2': self.unknown_0xaed1fba2,
            'unknown_0xb9a462fd': self.unknown_0xb9a462fd,
            'unknown_0x9888c19c': self.unknown_0x9888c19c,
            'unknown_0x7f1279e1': self.unknown_0x7f1279e1,
            'can_interrupt_fidget': self.can_interrupt_fidget,
            'shot_projectile': self.shot_projectile,
            'sound_projectile': self.sound_projectile,
            'shot_damage': self.shot_damage.to_json(),
            'projectile_static_geometry_test_during_task': self.projectile_static_geometry_test_during_task.to_json(),
            'projectile_static_geometry_test_during_combat': self.projectile_static_geometry_test_during_combat.to_json(),
            'burst_fire': self.burst_fire,
            'gun_model': self.gun_model,
            'use_head_tracking': self.use_head_tracking,
            'head_track_player_range': self.head_track_player_range,
            'head_track_target_range': self.head_track_target_range,
            'unknown_0x679e2937': self.unknown_0x679e2937,
            'hold_initial_animation': self.hold_initial_animation,
            'turn_threshold_when_walking': self.turn_threshold_when_walking,
            'turn_threshold_when_running': self.turn_threshold_when_running,
            'unknown_0x3ea5a256': self.unknown_0x3ea5a256,
            'is_grabbable': self.is_grabbable,
            'is_a_target': self.is_a_target,
        }

    def _dependencies_for_shot_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shot_projectile)

    def _dependencies_for_sound_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound_projectile)

    def _dependencies_for_burst_fire(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.burst_fire)

    def _dependencies_for_gun_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.gun_model)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.rag_doll_properties.dependencies_for, "rag_doll_properties", "RagDollData"),
            (self._dependencies_for_shot_projectile, "shot_projectile", "AssetId"),
            (self._dependencies_for_sound_projectile, "sound_projectile", "AssetId"),
            (self._dependencies_for_burst_fire, "burst_fire", "AssetId"),
            (self._dependencies_for_gun_model, "gun_model", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for FriendlyData.{field_name} ({field_type}): {e}"
                )


def _decode_rag_doll_properties(data: typing.BinaryIO, game: Game, property_size: int) -> RagDollData:
    return RagDollData.from_stream(data, game, property_size)


def _decode_shot_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_damage': 5.0})


def _decode_projectile_static_geometry_test_during_task(data: typing.BinaryIO, game: Game, property_size: int) -> StaticGeometryTest:
    return StaticGeometryTest.from_stream(data, game, property_size)


def _decode_projectile_static_geometry_test_during_combat(data: typing.BinaryIO, game: Game, property_size: int) -> StaticGeometryTest:
    return StaticGeometryTest.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xc1d1e465: ('flotsam', structs.decode_BIG_bool_),
    0xa149701e: ('rag_doll_properties', _decode_rag_doll_properties),
    0xbf443451: ('unknown_0xbf443451', structs.decode_BIG_bool_),
    0x6652bdd7: ('invulnerable', structs.decode_BIG_bool_),
    0x41baf88d: ('disable_knock_back_when_invulnerable', structs.decode_BIG_bool_),
    0xef5671d6: ('unknown_0xef5671d6', structs.decode_BIG_bool_),
    0xa4ae2178: ('unknown_0xa4ae2178', structs.decode_BIG_bool_),
    0x50a9bd0d: ('avoidance_range', structs.decode_BIG_f),
    0x02ac6274: ('unknown_0x02ac6274', structs.decode_BIG_bool_),
    0xaed1fba2: ('unknown_0xaed1fba2', structs.decode_BIG_f),
    0xb9a462fd: ('unknown_0xb9a462fd', structs.decode_BIG_f),
    0x9888c19c: ('unknown_0x9888c19c', structs.decode_BIG_f),
    0x7f1279e1: ('unknown_0x7f1279e1', structs.decode_BIG_f),
    0x662d5cc9: ('can_interrupt_fidget', structs.decode_BIG_bool_),
    0x51253ba3: ('shot_projectile', structs.decode_BIG_Q),
    0x10e3efdd: ('sound_projectile', structs.decode_BIG_Q),
    0xcea30138: ('shot_damage', _decode_shot_damage),
    0x785c41f5: ('projectile_static_geometry_test_during_task', _decode_projectile_static_geometry_test_during_task),
    0xfc5a0a21: ('projectile_static_geometry_test_during_combat', _decode_projectile_static_geometry_test_during_combat),
    0xfc34473f: ('burst_fire', structs.decode_BIG_Q),
    0x50340852: ('gun_model', structs.decode_BIG_Q),
    0x2ea013a6: ('use_head_tracking', structs.decode_BIG_bool_),
    0x330619ca: ('head_track_player_range', structs.decode_BIG_f),
    0xa7be5edf: ('head_track_target_range', structs.decode_BIG_f),
    0x679e2937: ('unknown_0x679e2937', structs.decode_BIG_bool_),
    0xf484e0ae: ('hold_initial_animation', structs.decode_BIG_bool_),
    0xec3fde21: ('turn_threshold_when_walking', structs.decode_BIG_f),
    0x24d18b0a: ('turn_threshold_when_running', structs.decode_BIG_f),
    0x3ea5a256: ('unknown_0x3ea5a256', structs.decode_BIG_bool_),
    0x66b099e0: ('is_grabbable', structs.decode_BIG_bool_),
    0xf5acd12e: ('is_a_target', structs.decode_BIG_bool_),
}
