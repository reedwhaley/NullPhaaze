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
from retro_data_structures.properties.corruption.archetypes.AuroraUnitCombatHatches import AuroraUnitCombatHatches
from retro_data_structures.properties.corruption.archetypes.AuroraUnitDarkSamusEcho import AuroraUnitDarkSamusEcho
from retro_data_structures.properties.corruption.archetypes.AuroraUnitGravityBuster import AuroraUnitGravityBuster
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.ModIncaData import ModIncaData
from retro_data_structures.properties.corruption.archetypes.UnknownStruct3 import UnknownStruct3
from retro_data_structures.properties.corruption.archetypes.UnknownStruct6 import UnknownStruct6
from retro_data_structures.properties.corruption.archetypes.UnknownStruct9 import UnknownStruct9
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class AuroraUnit1DataJson(typing_extensions.TypedDict):
        turn_to_target_threshold: float
        max_turn_angle: float
        left_brain_door: int
        right_brain_door: int
        brain_vulnerability: json_util.JsonObject
        max_brain_damage: float
        max_brain_exposed_time: float
        combat_hatches: json_util.JsonObject
        unknown_struct3: json_util.JsonObject
        dark_samus_echo_properties: json_util.JsonObject
        gravity_buster_properties: json_util.JsonObject
        unknown_struct9: json_util.JsonObject
        unknown_struct6_0x7cc2a36e: json_util.JsonObject
        unknown_struct6_0x12d3165c: json_util.JsonObject
        initial_attack_time: float
        initial_attack_time_variance: float
        time_between_attacks: float
        time_between_attack_variance: float
        mod_inca_data: json_util.JsonObject
    

@dataclasses.dataclass()
class AuroraUnit1Data(BaseProperty):
    turn_to_target_threshold: float = dataclasses.field(default=45.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4a1e8961, original_name='TurnToTargetThreshold'
        ),
    })
    max_turn_angle: float = dataclasses.field(default=120.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x50e46527, original_name='MaxTurnAngle'
        ),
    })
    left_brain_door: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x073842e7, original_name='LeftBrainDoor'
        ),
    })
    right_brain_door: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xddd72aad, original_name='RightBrainDoor'
        ),
    })
    brain_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x243ab10d, original_name='BrainVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    max_brain_damage: float = dataclasses.field(default=700.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7b4c8a7f, original_name='MaxBrainDamage'
        ),
    })
    max_brain_exposed_time: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa33bd3df, original_name='MaxBrainExposedTime'
        ),
    })
    combat_hatches: AuroraUnitCombatHatches = dataclasses.field(default_factory=AuroraUnitCombatHatches, metadata={
        'reflection': FieldReflection[AuroraUnitCombatHatches](
            AuroraUnitCombatHatches, id=0x5b514e8c, original_name='CombatHatches', from_json=AuroraUnitCombatHatches.from_json, to_json=AuroraUnitCombatHatches.to_json
        ),
    })
    unknown_struct3: UnknownStruct3 = dataclasses.field(default_factory=UnknownStruct3, metadata={
        'reflection': FieldReflection[UnknownStruct3](
            UnknownStruct3, id=0x828c2238, original_name='UnknownStruct3', from_json=UnknownStruct3.from_json, to_json=UnknownStruct3.to_json
        ),
    })
    dark_samus_echo_properties: AuroraUnitDarkSamusEcho = dataclasses.field(default_factory=AuroraUnitDarkSamusEcho, metadata={
        'reflection': FieldReflection[AuroraUnitDarkSamusEcho](
            AuroraUnitDarkSamusEcho, id=0x97d16aa1, original_name='DarkSamusEchoProperties', from_json=AuroraUnitDarkSamusEcho.from_json, to_json=AuroraUnitDarkSamusEcho.to_json
        ),
    })
    gravity_buster_properties: AuroraUnitGravityBuster = dataclasses.field(default_factory=AuroraUnitGravityBuster, metadata={
        'reflection': FieldReflection[AuroraUnitGravityBuster](
            AuroraUnitGravityBuster, id=0xfaed98db, original_name='GravityBusterProperties', from_json=AuroraUnitGravityBuster.from_json, to_json=AuroraUnitGravityBuster.to_json
        ),
    })
    unknown_struct9: UnknownStruct9 = dataclasses.field(default_factory=UnknownStruct9, metadata={
        'reflection': FieldReflection[UnknownStruct9](
            UnknownStruct9, id=0x9a9eb786, original_name='UnknownStruct9', from_json=UnknownStruct9.from_json, to_json=UnknownStruct9.to_json
        ),
    })
    unknown_struct6_0x7cc2a36e: UnknownStruct6 = dataclasses.field(default_factory=UnknownStruct6, metadata={
        'reflection': FieldReflection[UnknownStruct6](
            UnknownStruct6, id=0x7cc2a36e, original_name='UnknownStruct6', from_json=UnknownStruct6.from_json, to_json=UnknownStruct6.to_json
        ),
    })
    unknown_struct6_0x12d3165c: UnknownStruct6 = dataclasses.field(default_factory=UnknownStruct6, metadata={
        'reflection': FieldReflection[UnknownStruct6](
            UnknownStruct6, id=0x12d3165c, original_name='UnknownStruct6', from_json=UnknownStruct6.from_json, to_json=UnknownStruct6.to_json
        ),
    })
    initial_attack_time: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x446efcad, original_name='InitialAttackTime'
        ),
    })
    initial_attack_time_variance: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2caec304, original_name='InitialAttackTimeVariance'
        ),
    })
    time_between_attacks: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2c68fedf, original_name='TimeBetweenAttacks'
        ),
    })
    time_between_attack_variance: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1a79e5d6, original_name='TimeBetweenAttackVariance'
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
        if property_count != 19:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4a1e8961
        turn_to_target_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x50e46527
        max_turn_angle = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x073842e7
        left_brain_door = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xddd72aad
        right_brain_door = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x243ab10d
        brain_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7b4c8a7f
        max_brain_damage = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa33bd3df
        max_brain_exposed_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5b514e8c
        combat_hatches = AuroraUnitCombatHatches.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x828c2238
        unknown_struct3 = UnknownStruct3.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x97d16aa1
        dark_samus_echo_properties = AuroraUnitDarkSamusEcho.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfaed98db
        gravity_buster_properties = AuroraUnitGravityBuster.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9a9eb786
        unknown_struct9 = UnknownStruct9.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7cc2a36e
        unknown_struct6_0x7cc2a36e = UnknownStruct6.from_stream(data, game, property_size, default_override={'gravity_buster_chance': 40.0, 'combat_hatches_chance': 40.0, 'dark_samus_echoes_chance': 20.0, 'turret_chance': 0.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x12d3165c
        unknown_struct6_0x12d3165c = UnknownStruct6.from_stream(data, game, property_size, default_override={'gravity_buster_chance': 20.0, 'combat_hatches_chance': 20.0, 'dark_samus_echoes_chance': 20.0, 'turret_chance': 40.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x446efcad
        initial_attack_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2caec304
        initial_attack_time_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2c68fedf
        time_between_attacks = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1a79e5d6
        time_between_attack_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb4c02854
        mod_inca_data = ModIncaData.from_stream(data, game, property_size)
    
        return cls(turn_to_target_threshold, max_turn_angle, left_brain_door, right_brain_door, brain_vulnerability, max_brain_damage, max_brain_exposed_time, combat_hatches, unknown_struct3, dark_samus_echo_properties, gravity_buster_properties, unknown_struct9, unknown_struct6_0x7cc2a36e, unknown_struct6_0x12d3165c, initial_attack_time, initial_attack_time_variance, time_between_attacks, time_between_attack_variance, mod_inca_data)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x13')  # 19 properties

        data.write(b'J\x1e\x89a')  # 0x4a1e8961
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.turn_to_target_threshold))

        data.write(b"P\xe4e'")  # 0x50e46527
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_turn_angle))

        data.write(b'\x078B\xe7')  # 0x73842e7
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.left_brain_door))

        data.write(b'\xdd\xd7*\xad')  # 0xddd72aad
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.right_brain_door))

        data.write(b'$:\xb1\r')  # 0x243ab10d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.brain_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'{L\x8a\x7f')  # 0x7b4c8a7f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_brain_damage))

        data.write(b'\xa3;\xd3\xdf')  # 0xa33bd3df
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_brain_exposed_time))

        data.write(b'[QN\x8c')  # 0x5b514e8c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.combat_hatches.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x82\x8c"8')  # 0x828c2238
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.unknown_struct3.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x97\xd1j\xa1')  # 0x97d16aa1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.dark_samus_echo_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfa\xed\x98\xdb')  # 0xfaed98db
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.gravity_buster_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9a\x9e\xb7\x86')  # 0x9a9eb786
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.unknown_struct9.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'|\xc2\xa3n')  # 0x7cc2a36e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.unknown_struct6_0x7cc2a36e.to_stream(data, game, default_override={'gravity_buster_chance': 40.0, 'combat_hatches_chance': 40.0, 'dark_samus_echoes_chance': 20.0, 'turret_chance': 0.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x12\xd3\x16\\')  # 0x12d3165c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.unknown_struct6_0x12d3165c.to_stream(data, game, default_override={'gravity_buster_chance': 20.0, 'combat_hatches_chance': 20.0, 'dark_samus_echoes_chance': 20.0, 'turret_chance': 40.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'Dn\xfc\xad')  # 0x446efcad
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.initial_attack_time))

        data.write(b',\xae\xc3\x04')  # 0x2caec304
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.initial_attack_time_variance))

        data.write(b',h\xfe\xdf')  # 0x2c68fedf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.time_between_attacks))

        data.write(b'\x1ay\xe5\xd6')  # 0x1a79e5d6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.time_between_attack_variance))

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
        json_data = typing.cast("AuroraUnit1DataJson", data)
        return cls(
            turn_to_target_threshold=json_data['turn_to_target_threshold'],
            max_turn_angle=json_data['max_turn_angle'],
            left_brain_door=json_data['left_brain_door'],
            right_brain_door=json_data['right_brain_door'],
            brain_vulnerability=DamageVulnerability.from_json(json_data['brain_vulnerability']),
            max_brain_damage=json_data['max_brain_damage'],
            max_brain_exposed_time=json_data['max_brain_exposed_time'],
            combat_hatches=AuroraUnitCombatHatches.from_json(json_data['combat_hatches']),
            unknown_struct3=UnknownStruct3.from_json(json_data['unknown_struct3']),
            dark_samus_echo_properties=AuroraUnitDarkSamusEcho.from_json(json_data['dark_samus_echo_properties']),
            gravity_buster_properties=AuroraUnitGravityBuster.from_json(json_data['gravity_buster_properties']),
            unknown_struct9=UnknownStruct9.from_json(json_data['unknown_struct9']),
            unknown_struct6_0x7cc2a36e=UnknownStruct6.from_json(json_data['unknown_struct6_0x7cc2a36e']),
            unknown_struct6_0x12d3165c=UnknownStruct6.from_json(json_data['unknown_struct6_0x12d3165c']),
            initial_attack_time=json_data['initial_attack_time'],
            initial_attack_time_variance=json_data['initial_attack_time_variance'],
            time_between_attacks=json_data['time_between_attacks'],
            time_between_attack_variance=json_data['time_between_attack_variance'],
            mod_inca_data=ModIncaData.from_json(json_data['mod_inca_data']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'turn_to_target_threshold': self.turn_to_target_threshold,
            'max_turn_angle': self.max_turn_angle,
            'left_brain_door': self.left_brain_door,
            'right_brain_door': self.right_brain_door,
            'brain_vulnerability': self.brain_vulnerability.to_json(),
            'max_brain_damage': self.max_brain_damage,
            'max_brain_exposed_time': self.max_brain_exposed_time,
            'combat_hatches': self.combat_hatches.to_json(),
            'unknown_struct3': self.unknown_struct3.to_json(),
            'dark_samus_echo_properties': self.dark_samus_echo_properties.to_json(),
            'gravity_buster_properties': self.gravity_buster_properties.to_json(),
            'unknown_struct9': self.unknown_struct9.to_json(),
            'unknown_struct6_0x7cc2a36e': self.unknown_struct6_0x7cc2a36e.to_json(),
            'unknown_struct6_0x12d3165c': self.unknown_struct6_0x12d3165c.to_json(),
            'initial_attack_time': self.initial_attack_time,
            'initial_attack_time_variance': self.initial_attack_time_variance,
            'time_between_attacks': self.time_between_attacks,
            'time_between_attack_variance': self.time_between_attack_variance,
            'mod_inca_data': self.mod_inca_data.to_json(),
        }

    def _dependencies_for_left_brain_door(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.left_brain_door)

    def _dependencies_for_right_brain_door(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.right_brain_door)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_left_brain_door, "left_brain_door", "AssetId"),
            (self._dependencies_for_right_brain_door, "right_brain_door", "AssetId"),
            (self.combat_hatches.dependencies_for, "combat_hatches", "AuroraUnitCombatHatches"),
            (self.unknown_struct3.dependencies_for, "unknown_struct3", "UnknownStruct3"),
            (self.gravity_buster_properties.dependencies_for, "gravity_buster_properties", "AuroraUnitGravityBuster"),
            (self.unknown_struct9.dependencies_for, "unknown_struct9", "UnknownStruct9"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for AuroraUnit1Data.{field_name} ({field_type}): {e}"
                )


def _decode_brain_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_combat_hatches(data: typing.BinaryIO, game: Game, property_size: int) -> AuroraUnitCombatHatches:
    return AuroraUnitCombatHatches.from_stream(data, game, property_size)


def _decode_unknown_struct3(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct3:
    return UnknownStruct3.from_stream(data, game, property_size)


def _decode_dark_samus_echo_properties(data: typing.BinaryIO, game: Game, property_size: int) -> AuroraUnitDarkSamusEcho:
    return AuroraUnitDarkSamusEcho.from_stream(data, game, property_size)


def _decode_gravity_buster_properties(data: typing.BinaryIO, game: Game, property_size: int) -> AuroraUnitGravityBuster:
    return AuroraUnitGravityBuster.from_stream(data, game, property_size)


def _decode_unknown_struct9(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct9:
    return UnknownStruct9.from_stream(data, game, property_size)


def _decode_unknown_struct6_0x7cc2a36e(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct6:
    return UnknownStruct6.from_stream(data, game, property_size, default_override={'gravity_buster_chance': 40.0, 'combat_hatches_chance': 40.0, 'dark_samus_echoes_chance': 20.0, 'turret_chance': 0.0})


def _decode_unknown_struct6_0x12d3165c(data: typing.BinaryIO, game: Game, property_size: int) -> UnknownStruct6:
    return UnknownStruct6.from_stream(data, game, property_size, default_override={'gravity_buster_chance': 20.0, 'combat_hatches_chance': 20.0, 'dark_samus_echoes_chance': 20.0, 'turret_chance': 40.0})


def _decode_mod_inca_data(data: typing.BinaryIO, game: Game, property_size: int) -> ModIncaData:
    return ModIncaData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x4a1e8961: ('turn_to_target_threshold', structs.decode_BIG_f),
    0x50e46527: ('max_turn_angle', structs.decode_BIG_f),
    0x073842e7: ('left_brain_door', structs.decode_BIG_Q),
    0xddd72aad: ('right_brain_door', structs.decode_BIG_Q),
    0x243ab10d: ('brain_vulnerability', _decode_brain_vulnerability),
    0x7b4c8a7f: ('max_brain_damage', structs.decode_BIG_f),
    0xa33bd3df: ('max_brain_exposed_time', structs.decode_BIG_f),
    0x5b514e8c: ('combat_hatches', _decode_combat_hatches),
    0x828c2238: ('unknown_struct3', _decode_unknown_struct3),
    0x97d16aa1: ('dark_samus_echo_properties', _decode_dark_samus_echo_properties),
    0xfaed98db: ('gravity_buster_properties', _decode_gravity_buster_properties),
    0x9a9eb786: ('unknown_struct9', _decode_unknown_struct9),
    0x7cc2a36e: ('unknown_struct6_0x7cc2a36e', _decode_unknown_struct6_0x7cc2a36e),
    0x12d3165c: ('unknown_struct6_0x12d3165c', _decode_unknown_struct6_0x12d3165c),
    0x446efcad: ('initial_attack_time', structs.decode_BIG_f),
    0x2caec304: ('initial_attack_time_variance', structs.decode_BIG_f),
    0x2c68fedf: ('time_between_attacks', structs.decode_BIG_f),
    0x1a79e5d6: ('time_between_attack_variance', structs.decode_BIG_f),
    0xb4c02854: ('mod_inca_data', _decode_mod_inca_data),
}
