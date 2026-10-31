# Generated File
from __future__ import annotations

import dataclasses
import enum
import struct
import typing
import typing_extensions

from retro_data_structures import json_util
from retro_data_structures.game_check import Game
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseProperty
from retro_data_structures.properties.field_reflection import FieldReflection
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.IngPossessionData import IngPossessionData

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SplitterChassisDataJson(typing_extensions.TypedDict):
        main_chassis_flags: int
        leg_stab_attack_interval: float
        leg_stab_min_attack_range: float
        leg_stab_max_attack_range: float
        leg_stab_damage: json_util.JsonObject
        min_dodge_interval: float
        dodge_chance: float
        deployment_speed: float
        scan_duration: float
        laser_sweep_interval: float
        laser_sweep_min_attack_range: float
        laser_sweep_max_attack_range: float
        spin_attack_linear_velocity: float
        spin_attack_linear_acceleration: float
        spin_attack_linear_deceleration: float
        spin_attack_turn_speed: float
        spin_attack_interval: float
        spin_attack_interval_penalty: float
        spin_attack_telegraph_time: float
        spin_attack_min_attack_range: float
        spin_attack_max_attack_range: float
        spin_attack_max_bounces: int
        spin_attack_max_time: float
        spin_attack_damage: json_util.JsonObject
        sound_alerted: int
        ing_possession_data: json_util.JsonObject
        spin_attack_vulnerability: json_util.JsonObject
    

class SplitterChassisFlags(enum.IntFlag):
    StartsCrouching = 1
    StartsLurking = 2
    CanLegStab = 4
    CanSpinAttack = 8
    CanDodgeInAnyDirection = 16
    CanDodgeDown = 32
    CanLaserSweep = 64

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


@dataclasses.dataclass()
class SplitterChassisData(BaseProperty):
    main_chassis_flags: SplitterChassisFlags = dataclasses.field(default=SplitterChassisFlags(124), metadata={
        'reflection': FieldReflection[SplitterChassisFlags](
            SplitterChassisFlags, id=0xcef5c2fe, original_name='MainChassisFlags', from_json=SplitterChassisFlags.from_json, to_json=SplitterChassisFlags.to_json
        ),
    })
    leg_stab_attack_interval: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa8fddba0, original_name='LegStabAttackInterval'
        ),
    })
    leg_stab_min_attack_range: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf6047d40, original_name='LegStabMinAttackRange'
        ),
    })
    leg_stab_max_attack_range: float = dataclasses.field(default=6.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5130fd39, original_name='LegStabMaxAttackRange'
        ),
    })
    leg_stab_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xefacfa50, original_name='LegStabDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    min_dodge_interval: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x99a55939, original_name='MinDodgeInterval'
        ),
    })
    dodge_chance: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x47be3298, original_name='DodgeChance'
        ),
    })
    deployment_speed: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xeead6b4d, original_name='DeploymentSpeed'
        ),
    })
    scan_duration: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf84d8fda, original_name='ScanDuration'
        ),
    })
    laser_sweep_interval: float = dataclasses.field(default=6.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0fba492b, original_name='LaserSweepInterval'
        ),
    })
    laser_sweep_min_attack_range: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb3ea58f8, original_name='LaserSweepMinAttackRange'
        ),
    })
    laser_sweep_max_attack_range: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x14ded881, original_name='LaserSweepMaxAttackRange'
        ),
    })
    spin_attack_linear_velocity: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x35eedd1c, original_name='SpinAttackLinearVelocity'
        ),
    })
    spin_attack_linear_acceleration: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2dde6bfb, original_name='SpinAttackLinearAcceleration'
        ),
    })
    spin_attack_linear_deceleration: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8ae1ee93, original_name='SpinAttackLinearDeceleration'
        ),
    })
    spin_attack_turn_speed: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5027d1aa, original_name='SpinAttackTurnSpeed'
        ),
    })
    spin_attack_interval: float = dataclasses.field(default=6.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd8940662, original_name='SpinAttackInterval'
        ),
    })
    spin_attack_interval_penalty: float = dataclasses.field(default=6.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf65e430f, original_name='SpinAttackIntervalPenalty'
        ),
    })
    spin_attack_telegraph_time: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x43722555, original_name='SpinAttackTelegraphTime'
        ),
    })
    spin_attack_min_attack_range: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8935377c, original_name='SpinAttackMinAttackRange'
        ),
    })
    spin_attack_max_attack_range: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2e01b705, original_name='SpinAttackMaxAttackRange'
        ),
    })
    spin_attack_max_bounces: int = dataclasses.field(default=4, metadata={
        'reflection': FieldReflection[int](
            int, id=0xd5f34476, original_name='SpinAttackMaxBounces'
        ),
    })
    spin_attack_max_time: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x21296bdc, original_name='SpinAttackMaxTime'
        ),
    })
    spin_attack_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xcfacff53, original_name='SpinAttackDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    sound_alerted: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xa61c2a66, original_name='Sound_Alerted'
        ),
    })
    ing_possession_data: IngPossessionData = dataclasses.field(default_factory=IngPossessionData, metadata={
        'reflection': FieldReflection[IngPossessionData](
            IngPossessionData, id=0xe61748ed, original_name='IngPossessionData', from_json=IngPossessionData.from_json, to_json=IngPossessionData.to_json
        ),
    })
    spin_attack_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x24e23cc5, original_name='SpinAttackVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
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
        if property_count != 27:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcef5c2fe
        main_chassis_flags = SplitterChassisFlags.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa8fddba0
        leg_stab_attack_interval = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf6047d40
        leg_stab_min_attack_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5130fd39
        leg_stab_max_attack_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xefacfa50
        leg_stab_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x99a55939
        min_dodge_interval = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47be3298
        dodge_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xeead6b4d
        deployment_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf84d8fda
        scan_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0fba492b
        laser_sweep_interval = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3ea58f8
        laser_sweep_min_attack_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x14ded881
        laser_sweep_max_attack_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x35eedd1c
        spin_attack_linear_velocity = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2dde6bfb
        spin_attack_linear_acceleration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8ae1ee93
        spin_attack_linear_deceleration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5027d1aa
        spin_attack_turn_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd8940662
        spin_attack_interval = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf65e430f
        spin_attack_interval_penalty = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x43722555
        spin_attack_telegraph_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8935377c
        spin_attack_min_attack_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2e01b705
        spin_attack_max_attack_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd5f34476
        spin_attack_max_bounces = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x21296bdc
        spin_attack_max_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcfacff53
        spin_attack_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa61c2a66
        sound_alerted = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe61748ed
        ing_possession_data = IngPossessionData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x24e23cc5
        spin_attack_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        return cls(main_chassis_flags, leg_stab_attack_interval, leg_stab_min_attack_range, leg_stab_max_attack_range, leg_stab_damage, min_dodge_interval, dodge_chance, deployment_speed, scan_duration, laser_sweep_interval, laser_sweep_min_attack_range, laser_sweep_max_attack_range, spin_attack_linear_velocity, spin_attack_linear_acceleration, spin_attack_linear_deceleration, spin_attack_turn_speed, spin_attack_interval, spin_attack_interval_penalty, spin_attack_telegraph_time, spin_attack_min_attack_range, spin_attack_max_attack_range, spin_attack_max_bounces, spin_attack_max_time, spin_attack_damage, sound_alerted, ing_possession_data, spin_attack_vulnerability)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x1b')  # 27 properties

        data.write(b'\xce\xf5\xc2\xfe')  # 0xcef5c2fe
        data.write(b'\x00\x04')  # size
        self.main_chassis_flags.to_stream(data, game)

        data.write(b'\xa8\xfd\xdb\xa0')  # 0xa8fddba0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.leg_stab_attack_interval))

        data.write(b'\xf6\x04}@')  # 0xf6047d40
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.leg_stab_min_attack_range))

        data.write(b'Q0\xfd9')  # 0x5130fd39
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.leg_stab_max_attack_range))

        data.write(b'\xef\xac\xfaP')  # 0xefacfa50
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.leg_stab_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x99\xa5Y9')  # 0x99a55939
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_dodge_interval))

        data.write(b'G\xbe2\x98')  # 0x47be3298
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dodge_chance))

        data.write(b'\xee\xadkM')  # 0xeead6b4d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.deployment_speed))

        data.write(b'\xf8M\x8f\xda')  # 0xf84d8fda
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scan_duration))

        data.write(b'\x0f\xbaI+')  # 0xfba492b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.laser_sweep_interval))

        data.write(b'\xb3\xeaX\xf8')  # 0xb3ea58f8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.laser_sweep_min_attack_range))

        data.write(b'\x14\xde\xd8\x81')  # 0x14ded881
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.laser_sweep_max_attack_range))

        data.write(b'5\xee\xdd\x1c')  # 0x35eedd1c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.spin_attack_linear_velocity))

        data.write(b'-\xdek\xfb')  # 0x2dde6bfb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.spin_attack_linear_acceleration))

        data.write(b'\x8a\xe1\xee\x93')  # 0x8ae1ee93
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.spin_attack_linear_deceleration))

        data.write(b"P'\xd1\xaa")  # 0x5027d1aa
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.spin_attack_turn_speed))

        data.write(b'\xd8\x94\x06b')  # 0xd8940662
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.spin_attack_interval))

        data.write(b'\xf6^C\x0f')  # 0xf65e430f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.spin_attack_interval_penalty))

        data.write(b'Cr%U')  # 0x43722555
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.spin_attack_telegraph_time))

        data.write(b'\x8957|')  # 0x8935377c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.spin_attack_min_attack_range))

        data.write(b'.\x01\xb7\x05')  # 0x2e01b705
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.spin_attack_max_attack_range))

        data.write(b'\xd5\xf3Dv')  # 0xd5f34476
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.spin_attack_max_bounces))

        data.write(b'!)k\xdc')  # 0x21296bdc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.spin_attack_max_time))

        data.write(b'\xcf\xac\xffS')  # 0xcfacff53
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.spin_attack_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa6\x1c*f')  # 0xa61c2a66
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_alerted))

        data.write(b'\xe6\x17H\xed')  # 0xe61748ed
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ing_possession_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'$\xe2<\xc5')  # 0x24e23cc5
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.spin_attack_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SplitterChassisDataJson", data)
        return cls(
            main_chassis_flags=SplitterChassisFlags.from_json(json_data['main_chassis_flags']),
            leg_stab_attack_interval=json_data['leg_stab_attack_interval'],
            leg_stab_min_attack_range=json_data['leg_stab_min_attack_range'],
            leg_stab_max_attack_range=json_data['leg_stab_max_attack_range'],
            leg_stab_damage=DamageInfo.from_json(json_data['leg_stab_damage']),
            min_dodge_interval=json_data['min_dodge_interval'],
            dodge_chance=json_data['dodge_chance'],
            deployment_speed=json_data['deployment_speed'],
            scan_duration=json_data['scan_duration'],
            laser_sweep_interval=json_data['laser_sweep_interval'],
            laser_sweep_min_attack_range=json_data['laser_sweep_min_attack_range'],
            laser_sweep_max_attack_range=json_data['laser_sweep_max_attack_range'],
            spin_attack_linear_velocity=json_data['spin_attack_linear_velocity'],
            spin_attack_linear_acceleration=json_data['spin_attack_linear_acceleration'],
            spin_attack_linear_deceleration=json_data['spin_attack_linear_deceleration'],
            spin_attack_turn_speed=json_data['spin_attack_turn_speed'],
            spin_attack_interval=json_data['spin_attack_interval'],
            spin_attack_interval_penalty=json_data['spin_attack_interval_penalty'],
            spin_attack_telegraph_time=json_data['spin_attack_telegraph_time'],
            spin_attack_min_attack_range=json_data['spin_attack_min_attack_range'],
            spin_attack_max_attack_range=json_data['spin_attack_max_attack_range'],
            spin_attack_max_bounces=json_data['spin_attack_max_bounces'],
            spin_attack_max_time=json_data['spin_attack_max_time'],
            spin_attack_damage=DamageInfo.from_json(json_data['spin_attack_damage']),
            sound_alerted=json_data['sound_alerted'],
            ing_possession_data=IngPossessionData.from_json(json_data['ing_possession_data']),
            spin_attack_vulnerability=DamageVulnerability.from_json(json_data['spin_attack_vulnerability']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'main_chassis_flags': self.main_chassis_flags.to_json(),
            'leg_stab_attack_interval': self.leg_stab_attack_interval,
            'leg_stab_min_attack_range': self.leg_stab_min_attack_range,
            'leg_stab_max_attack_range': self.leg_stab_max_attack_range,
            'leg_stab_damage': self.leg_stab_damage.to_json(),
            'min_dodge_interval': self.min_dodge_interval,
            'dodge_chance': self.dodge_chance,
            'deployment_speed': self.deployment_speed,
            'scan_duration': self.scan_duration,
            'laser_sweep_interval': self.laser_sweep_interval,
            'laser_sweep_min_attack_range': self.laser_sweep_min_attack_range,
            'laser_sweep_max_attack_range': self.laser_sweep_max_attack_range,
            'spin_attack_linear_velocity': self.spin_attack_linear_velocity,
            'spin_attack_linear_acceleration': self.spin_attack_linear_acceleration,
            'spin_attack_linear_deceleration': self.spin_attack_linear_deceleration,
            'spin_attack_turn_speed': self.spin_attack_turn_speed,
            'spin_attack_interval': self.spin_attack_interval,
            'spin_attack_interval_penalty': self.spin_attack_interval_penalty,
            'spin_attack_telegraph_time': self.spin_attack_telegraph_time,
            'spin_attack_min_attack_range': self.spin_attack_min_attack_range,
            'spin_attack_max_attack_range': self.spin_attack_max_attack_range,
            'spin_attack_max_bounces': self.spin_attack_max_bounces,
            'spin_attack_max_time': self.spin_attack_max_time,
            'spin_attack_damage': self.spin_attack_damage.to_json(),
            'sound_alerted': self.sound_alerted,
            'ing_possession_data': self.ing_possession_data.to_json(),
            'spin_attack_vulnerability': self.spin_attack_vulnerability.to_json(),
        }

    def _dependencies_for_sound_alerted(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_alerted)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_sound_alerted, "sound_alerted", "int"),
            (self.ing_possession_data.dependencies_for, "ing_possession_data", "IngPossessionData"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for SplitterChassisData.{field_name} ({field_type}): {e}"
                )


def _decode_main_chassis_flags(data: typing.BinaryIO, game: Game, property_size: int) -> SplitterChassisFlags:
    return SplitterChassisFlags.from_stream(data, game)


def _decode_leg_stab_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 5.0})


def _decode_spin_attack_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 5.0})


def _decode_ing_possession_data(data: typing.BinaryIO, game: Game, property_size: int) -> IngPossessionData:
    return IngPossessionData.from_stream(data, game, property_size)


def _decode_spin_attack_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xcef5c2fe: ('main_chassis_flags', _decode_main_chassis_flags),
    0xa8fddba0: ('leg_stab_attack_interval', structs.decode_BIG_f),
    0xf6047d40: ('leg_stab_min_attack_range', structs.decode_BIG_f),
    0x5130fd39: ('leg_stab_max_attack_range', structs.decode_BIG_f),
    0xefacfa50: ('leg_stab_damage', _decode_leg_stab_damage),
    0x99a55939: ('min_dodge_interval', structs.decode_BIG_f),
    0x47be3298: ('dodge_chance', structs.decode_BIG_f),
    0xeead6b4d: ('deployment_speed', structs.decode_BIG_f),
    0xf84d8fda: ('scan_duration', structs.decode_BIG_f),
    0x0fba492b: ('laser_sweep_interval', structs.decode_BIG_f),
    0xb3ea58f8: ('laser_sweep_min_attack_range', structs.decode_BIG_f),
    0x14ded881: ('laser_sweep_max_attack_range', structs.decode_BIG_f),
    0x35eedd1c: ('spin_attack_linear_velocity', structs.decode_BIG_f),
    0x2dde6bfb: ('spin_attack_linear_acceleration', structs.decode_BIG_f),
    0x8ae1ee93: ('spin_attack_linear_deceleration', structs.decode_BIG_f),
    0x5027d1aa: ('spin_attack_turn_speed', structs.decode_BIG_f),
    0xd8940662: ('spin_attack_interval', structs.decode_BIG_f),
    0xf65e430f: ('spin_attack_interval_penalty', structs.decode_BIG_f),
    0x43722555: ('spin_attack_telegraph_time', structs.decode_BIG_f),
    0x8935377c: ('spin_attack_min_attack_range', structs.decode_BIG_f),
    0x2e01b705: ('spin_attack_max_attack_range', structs.decode_BIG_f),
    0xd5f34476: ('spin_attack_max_bounces', structs.decode_BIG_l),
    0x21296bdc: ('spin_attack_max_time', structs.decode_BIG_f),
    0xcfacff53: ('spin_attack_damage', _decode_spin_attack_damage),
    0xa61c2a66: ('sound_alerted', structs.decode_BIG_l),
    0xe61748ed: ('ing_possession_data', _decode_ing_possession_data),
    0x24e23cc5: ('spin_attack_vulnerability', _decode_spin_attack_vulnerability),
}
