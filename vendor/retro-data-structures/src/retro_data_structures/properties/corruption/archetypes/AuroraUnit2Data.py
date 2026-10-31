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
from retro_data_structures.properties.corruption.archetypes.AuroraUnit2AttackChance import AuroraUnit2AttackChance
from retro_data_structures.properties.corruption.archetypes.AuroraUnitCuttingBeams import AuroraUnitCuttingBeams
from retro_data_structures.properties.corruption.archetypes.AuroraUnitGravitonWave import AuroraUnitGravitonWave
from retro_data_structures.properties.corruption.archetypes.AuroraUnitGroundSpin import AuroraUnitGroundSpin
from retro_data_structures.properties.corruption.archetypes.AuroraUnitPhazonHyperCannon import AuroraUnitPhazonHyperCannon
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class AuroraUnit2DataJson(typing_extensions.TypedDict):
        stage2_health_percent: float
        stage3_health_percent: float
        flight_max_speed: float
        flight_acceleration: float
        flight_deceleration: float
        dodge_time: float
        dodge_time_variance: float
        dodge_chance: float
        unknown: float
        hover_height: float
        min_follow_distance: float
        max_follow_distance: float
        initial_attack_time: float
        attack_time: float
        attack_time_variance: float
        low_health_attack_time: float
        low_health_attack_time_variance: float
        junction_vulnerability: json_util.JsonObject
        initial_attack_chance: json_util.JsonObject
        phazon_hyper_cannon: json_util.JsonObject
        graviton_wave: json_util.JsonObject
        cutting_beams: json_util.JsonObject
        ground_spin: json_util.JsonObject
    

@dataclasses.dataclass()
class AuroraUnit2Data(BaseProperty):
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
    flight_max_speed: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd4dec629, original_name='FlightMaxSpeed'
        ),
    })
    flight_acceleration: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7a2bb377, original_name='FlightAcceleration'
        ),
    })
    flight_deceleration: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdd14361f, original_name='FlightDeceleration'
        ),
    })
    dodge_time: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x67625bef, original_name='DodgeTime'
        ),
    })
    dodge_time_variance: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x34b97edb, original_name='DodgeTimeVariance'
        ),
    })
    dodge_chance: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x47be3298, original_name='DodgeChance'
        ),
    })
    unknown: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xefd78a41, original_name='Unknown'
        ),
    })
    hover_height: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc75998aa, original_name='HoverHeight'
        ),
    })
    min_follow_distance: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x93716a88, original_name='MinFollowDistance'
        ),
    })
    max_follow_distance: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd266550e, original_name='MaxFollowDistance'
        ),
    })
    initial_attack_time: float = dataclasses.field(default=6.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x446efcad, original_name='InitialAttackTime'
        ),
    })
    attack_time: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdca1e8b6, original_name='AttackTime'
        ),
    })
    attack_time_variance: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9f269614, original_name='AttackTimeVariance'
        ),
    })
    low_health_attack_time: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x059b46cf, original_name='LowHealthAttackTime'
        ),
    })
    low_health_attack_time_variance: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1aa98d7f, original_name='LowHealthAttackTimeVariance'
        ),
    })
    junction_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xfdd2fe20, original_name='JunctionVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    initial_attack_chance: AuroraUnit2AttackChance = dataclasses.field(default_factory=AuroraUnit2AttackChance, metadata={
        'reflection': FieldReflection[AuroraUnit2AttackChance](
            AuroraUnit2AttackChance, id=0xc108cfa0, original_name='InitialAttackChance', from_json=AuroraUnit2AttackChance.from_json, to_json=AuroraUnit2AttackChance.to_json
        ),
    })
    phazon_hyper_cannon: AuroraUnitPhazonHyperCannon = dataclasses.field(default_factory=AuroraUnitPhazonHyperCannon, metadata={
        'reflection': FieldReflection[AuroraUnitPhazonHyperCannon](
            AuroraUnitPhazonHyperCannon, id=0x91502686, original_name='PhazonHyperCannon', from_json=AuroraUnitPhazonHyperCannon.from_json, to_json=AuroraUnitPhazonHyperCannon.to_json
        ),
    })
    graviton_wave: AuroraUnitGravitonWave = dataclasses.field(default_factory=AuroraUnitGravitonWave, metadata={
        'reflection': FieldReflection[AuroraUnitGravitonWave](
            AuroraUnitGravitonWave, id=0xad62c993, original_name='GravitonWave', from_json=AuroraUnitGravitonWave.from_json, to_json=AuroraUnitGravitonWave.to_json
        ),
    })
    cutting_beams: AuroraUnitCuttingBeams = dataclasses.field(default_factory=AuroraUnitCuttingBeams, metadata={
        'reflection': FieldReflection[AuroraUnitCuttingBeams](
            AuroraUnitCuttingBeams, id=0x03a319df, original_name='CuttingBeams', from_json=AuroraUnitCuttingBeams.from_json, to_json=AuroraUnitCuttingBeams.to_json
        ),
    })
    ground_spin: AuroraUnitGroundSpin = dataclasses.field(default_factory=AuroraUnitGroundSpin, metadata={
        'reflection': FieldReflection[AuroraUnitGroundSpin](
            AuroraUnitGroundSpin, id=0x9dd3bb57, original_name='GroundSpin', from_json=AuroraUnitGroundSpin.from_json, to_json=AuroraUnitGroundSpin.to_json
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
        if property_count != 23:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0a072c48
        stage2_health_percent = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdde5ac10
        stage3_health_percent = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd4dec629
        flight_max_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7a2bb377
        flight_acceleration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdd14361f
        flight_deceleration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x67625bef
        dodge_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x34b97edb
        dodge_time_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47be3298
        dodge_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xefd78a41
        unknown = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc75998aa
        hover_height = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x93716a88
        min_follow_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd266550e
        max_follow_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x446efcad
        initial_attack_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdca1e8b6
        attack_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9f269614
        attack_time_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x059b46cf
        low_health_attack_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1aa98d7f
        low_health_attack_time_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfdd2fe20
        junction_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc108cfa0
        initial_attack_chance = AuroraUnit2AttackChance.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x91502686
        phazon_hyper_cannon = AuroraUnitPhazonHyperCannon.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xad62c993
        graviton_wave = AuroraUnitGravitonWave.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03a319df
        cutting_beams = AuroraUnitCuttingBeams.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9dd3bb57
        ground_spin = AuroraUnitGroundSpin.from_stream(data, game, property_size)
    
        return cls(stage2_health_percent, stage3_health_percent, flight_max_speed, flight_acceleration, flight_deceleration, dodge_time, dodge_time_variance, dodge_chance, unknown, hover_height, min_follow_distance, max_follow_distance, initial_attack_time, attack_time, attack_time_variance, low_health_attack_time, low_health_attack_time_variance, junction_vulnerability, initial_attack_chance, phazon_hyper_cannon, graviton_wave, cutting_beams, ground_spin)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x17')  # 23 properties

        data.write(b'\n\x07,H')  # 0xa072c48
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stage2_health_percent))

        data.write(b'\xdd\xe5\xac\x10')  # 0xdde5ac10
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stage3_health_percent))

        data.write(b'\xd4\xde\xc6)')  # 0xd4dec629
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flight_max_speed))

        data.write(b'z+\xb3w')  # 0x7a2bb377
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flight_acceleration))

        data.write(b'\xdd\x146\x1f')  # 0xdd14361f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.flight_deceleration))

        data.write(b'gb[\xef')  # 0x67625bef
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dodge_time))

        data.write(b'4\xb9~\xdb')  # 0x34b97edb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dodge_time_variance))

        data.write(b'G\xbe2\x98')  # 0x47be3298
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dodge_chance))

        data.write(b'\xef\xd7\x8aA')  # 0xefd78a41
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b'\xc7Y\x98\xaa')  # 0xc75998aa
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hover_height))

        data.write(b'\x93qj\x88')  # 0x93716a88
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_follow_distance))

        data.write(b'\xd2fU\x0e')  # 0xd266550e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_follow_distance))

        data.write(b'Dn\xfc\xad')  # 0x446efcad
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.initial_attack_time))

        data.write(b'\xdc\xa1\xe8\xb6')  # 0xdca1e8b6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.attack_time))

        data.write(b'\x9f&\x96\x14')  # 0x9f269614
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.attack_time_variance))

        data.write(b'\x05\x9bF\xcf')  # 0x59b46cf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.low_health_attack_time))

        data.write(b'\x1a\xa9\x8d\x7f')  # 0x1aa98d7f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.low_health_attack_time_variance))

        data.write(b'\xfd\xd2\xfe ')  # 0xfdd2fe20
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.junction_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc1\x08\xcf\xa0')  # 0xc108cfa0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.initial_attack_chance.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x91P&\x86')  # 0x91502686
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.phazon_hyper_cannon.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xadb\xc9\x93')  # 0xad62c993
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.graviton_wave.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x03\xa3\x19\xdf')  # 0x3a319df
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.cutting_beams.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9d\xd3\xbbW')  # 0x9dd3bb57
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ground_spin.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("AuroraUnit2DataJson", data)
        return cls(
            stage2_health_percent=json_data['stage2_health_percent'],
            stage3_health_percent=json_data['stage3_health_percent'],
            flight_max_speed=json_data['flight_max_speed'],
            flight_acceleration=json_data['flight_acceleration'],
            flight_deceleration=json_data['flight_deceleration'],
            dodge_time=json_data['dodge_time'],
            dodge_time_variance=json_data['dodge_time_variance'],
            dodge_chance=json_data['dodge_chance'],
            unknown=json_data['unknown'],
            hover_height=json_data['hover_height'],
            min_follow_distance=json_data['min_follow_distance'],
            max_follow_distance=json_data['max_follow_distance'],
            initial_attack_time=json_data['initial_attack_time'],
            attack_time=json_data['attack_time'],
            attack_time_variance=json_data['attack_time_variance'],
            low_health_attack_time=json_data['low_health_attack_time'],
            low_health_attack_time_variance=json_data['low_health_attack_time_variance'],
            junction_vulnerability=DamageVulnerability.from_json(json_data['junction_vulnerability']),
            initial_attack_chance=AuroraUnit2AttackChance.from_json(json_data['initial_attack_chance']),
            phazon_hyper_cannon=AuroraUnitPhazonHyperCannon.from_json(json_data['phazon_hyper_cannon']),
            graviton_wave=AuroraUnitGravitonWave.from_json(json_data['graviton_wave']),
            cutting_beams=AuroraUnitCuttingBeams.from_json(json_data['cutting_beams']),
            ground_spin=AuroraUnitGroundSpin.from_json(json_data['ground_spin']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'stage2_health_percent': self.stage2_health_percent,
            'stage3_health_percent': self.stage3_health_percent,
            'flight_max_speed': self.flight_max_speed,
            'flight_acceleration': self.flight_acceleration,
            'flight_deceleration': self.flight_deceleration,
            'dodge_time': self.dodge_time,
            'dodge_time_variance': self.dodge_time_variance,
            'dodge_chance': self.dodge_chance,
            'unknown': self.unknown,
            'hover_height': self.hover_height,
            'min_follow_distance': self.min_follow_distance,
            'max_follow_distance': self.max_follow_distance,
            'initial_attack_time': self.initial_attack_time,
            'attack_time': self.attack_time,
            'attack_time_variance': self.attack_time_variance,
            'low_health_attack_time': self.low_health_attack_time,
            'low_health_attack_time_variance': self.low_health_attack_time_variance,
            'junction_vulnerability': self.junction_vulnerability.to_json(),
            'initial_attack_chance': self.initial_attack_chance.to_json(),
            'phazon_hyper_cannon': self.phazon_hyper_cannon.to_json(),
            'graviton_wave': self.graviton_wave.to_json(),
            'cutting_beams': self.cutting_beams.to_json(),
            'ground_spin': self.ground_spin.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.phazon_hyper_cannon.dependencies_for, "phazon_hyper_cannon", "AuroraUnitPhazonHyperCannon"),
            (self.graviton_wave.dependencies_for, "graviton_wave", "AuroraUnitGravitonWave"),
            (self.cutting_beams.dependencies_for, "cutting_beams", "AuroraUnitCuttingBeams"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for AuroraUnit2Data.{field_name} ({field_type}): {e}"
                )


def _decode_junction_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_initial_attack_chance(data: typing.BinaryIO, game: Game, property_size: int) -> AuroraUnit2AttackChance:
    return AuroraUnit2AttackChance.from_stream(data, game, property_size)


def _decode_phazon_hyper_cannon(data: typing.BinaryIO, game: Game, property_size: int) -> AuroraUnitPhazonHyperCannon:
    return AuroraUnitPhazonHyperCannon.from_stream(data, game, property_size)


def _decode_graviton_wave(data: typing.BinaryIO, game: Game, property_size: int) -> AuroraUnitGravitonWave:
    return AuroraUnitGravitonWave.from_stream(data, game, property_size)


def _decode_cutting_beams(data: typing.BinaryIO, game: Game, property_size: int) -> AuroraUnitCuttingBeams:
    return AuroraUnitCuttingBeams.from_stream(data, game, property_size)


def _decode_ground_spin(data: typing.BinaryIO, game: Game, property_size: int) -> AuroraUnitGroundSpin:
    return AuroraUnitGroundSpin.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x0a072c48: ('stage2_health_percent', structs.decode_BIG_f),
    0xdde5ac10: ('stage3_health_percent', structs.decode_BIG_f),
    0xd4dec629: ('flight_max_speed', structs.decode_BIG_f),
    0x7a2bb377: ('flight_acceleration', structs.decode_BIG_f),
    0xdd14361f: ('flight_deceleration', structs.decode_BIG_f),
    0x67625bef: ('dodge_time', structs.decode_BIG_f),
    0x34b97edb: ('dodge_time_variance', structs.decode_BIG_f),
    0x47be3298: ('dodge_chance', structs.decode_BIG_f),
    0xefd78a41: ('unknown', structs.decode_BIG_f),
    0xc75998aa: ('hover_height', structs.decode_BIG_f),
    0x93716a88: ('min_follow_distance', structs.decode_BIG_f),
    0xd266550e: ('max_follow_distance', structs.decode_BIG_f),
    0x446efcad: ('initial_attack_time', structs.decode_BIG_f),
    0xdca1e8b6: ('attack_time', structs.decode_BIG_f),
    0x9f269614: ('attack_time_variance', structs.decode_BIG_f),
    0x059b46cf: ('low_health_attack_time', structs.decode_BIG_f),
    0x1aa98d7f: ('low_health_attack_time_variance', structs.decode_BIG_f),
    0xfdd2fe20: ('junction_vulnerability', _decode_junction_vulnerability),
    0xc108cfa0: ('initial_attack_chance', _decode_initial_attack_chance),
    0x91502686: ('phazon_hyper_cannon', _decode_phazon_hyper_cannon),
    0xad62c993: ('graviton_wave', _decode_graviton_wave),
    0x03a319df: ('cutting_beams', _decode_cutting_beams),
    0x9dd3bb57: ('ground_spin', _decode_ground_spin),
}
