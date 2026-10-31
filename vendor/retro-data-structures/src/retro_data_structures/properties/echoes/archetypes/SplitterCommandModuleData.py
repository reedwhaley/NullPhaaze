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
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.IngPossessionData import IngPossessionData
from retro_data_structures.properties.echoes.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.echoes.archetypes.SplitterScanBeamData import SplitterScanBeamData
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SplitterCommandModuleDataJson(typing_extensions.TypedDict):
        command_module_flags: int
        max_linear_velocity: float
        max_turn_speed: float
        scanning_turn_speed: float
        min_laser_pulse_attack_time: float
        min_laser_pulse_range: float
        max_laser_pulse_range: float
        max_laser_pulse_shots: int
        laser_pulse_projectile: int
        laser_pulse_damage: json_util.JsonObject
        min_dodges: int
        max_dodges: int
        dodge_chance: float
        reset_shield_time: float
        shield_hp: float
        laser_sweep_turn_speed: float
        laser_sweep_damage: json_util.JsonObject
        laser_sweep_beam_info: json_util.JsonObject
        scan_beam_data: json_util.JsonObject
        sound_laser_sweep: int
        sound_laser_charge_up: int
        sound_docking: int
        sound_scanning: int
        sound_light_shield: int
        sound_dark_shield: int
        sound_shield_on: int
        ing_possession_data: json_util.JsonObject
        light_shield_vulnerability: json_util.JsonObject
        dark_shield_vulnerability: json_util.JsonObject
    

class SplitterCommandModuleFlags(enum.IntFlag):
    StartsDocked = 1
    CanDodge = 2
    CanBreakLockOn = 4
    CanDockWithChassis = 8

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
class SplitterCommandModuleData(BaseProperty):
    command_module_flags: SplitterCommandModuleFlags = dataclasses.field(default=SplitterCommandModuleFlags(10), metadata={
        'reflection': FieldReflection[SplitterCommandModuleFlags](
            SplitterCommandModuleFlags, id=0xbd80fd94, original_name='CommandModuleFlags', from_json=SplitterCommandModuleFlags.from_json, to_json=SplitterCommandModuleFlags.to_json
        ),
    })
    max_linear_velocity: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x00d74fc3, original_name='MaxLinearVelocity'
        ),
    })
    max_turn_speed: float = dataclasses.field(default=720.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0b5c3c1a, original_name='MaxTurnSpeed'
        ),
    })
    scanning_turn_speed: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa0b3e1be, original_name='ScanningTurnSpeed'
        ),
    })
    min_laser_pulse_attack_time: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe32fcae9, original_name='MinLaserPulseAttackTime'
        ),
    })
    min_laser_pulse_range: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc5e0b92c, original_name='MinLaserPulseRange'
        ),
    })
    max_laser_pulse_range: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc17a8806, original_name='MaxLaserPulseRange'
        ),
    })
    max_laser_pulse_shots: int = dataclasses.field(default=3, metadata={
        'reflection': FieldReflection[int](
            int, id=0xe75bae9e, original_name='MaxLaserPulseShots'
        ),
    })
    laser_pulse_projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x4d77b7aa, original_name='LaserPulseProjectile'
        ),
    })
    laser_pulse_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xb763eb10, original_name='LaserPulseDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    min_dodges: int = dataclasses.field(default=1, metadata={
        'reflection': FieldReflection[int](
            int, id=0xeda45014, original_name='MinDodges'
        ),
    })
    max_dodges: int = dataclasses.field(default=3, metadata={
        'reflection': FieldReflection[int](
            int, id=0x7dd740fe, original_name='MaxDodges'
        ),
    })
    dodge_chance: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x47be3298, original_name='DodgeChance'
        ),
    })
    reset_shield_time: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd3dec6dc, original_name='ResetShieldTime'
        ),
    })
    shield_hp: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xecd9d92d, original_name='ShieldHP'
        ),
    })
    laser_sweep_turn_speed: float = dataclasses.field(default=45.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5ff006d1, original_name='LaserSweepTurnSpeed'
        ),
    })
    laser_sweep_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x1bd017ce, original_name='LaserSweepDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    laser_sweep_beam_info: PlasmaBeamInfo = dataclasses.field(default_factory=PlasmaBeamInfo, metadata={
        'reflection': FieldReflection[PlasmaBeamInfo](
            PlasmaBeamInfo, id=0x4a37c437, original_name='LaserSweepBeamInfo', from_json=PlasmaBeamInfo.from_json, to_json=PlasmaBeamInfo.to_json
        ),
    })
    scan_beam_data: SplitterScanBeamData = dataclasses.field(default_factory=SplitterScanBeamData, metadata={
        'reflection': FieldReflection[SplitterScanBeamData](
            SplitterScanBeamData, id=0x9ec51fe4, original_name='ScanBeamData', from_json=SplitterScanBeamData.from_json, to_json=SplitterScanBeamData.to_json
        ),
    })
    sound_laser_sweep: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xea307548, original_name='Sound_LaserSweep'
        ),
    })
    sound_laser_charge_up: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x3779bd93, original_name='Sound_LaserChargeUp'
        ),
    })
    sound_docking: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xc90dbdb4, original_name='Sound_Docking'
        ),
    })
    sound_scanning: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xe7724802, original_name='Sound_Scanning'
        ),
    })
    sound_light_shield: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xd4a06273, original_name='Sound_LightShield'
        ),
    })
    sound_dark_shield: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xafc20631, original_name='Sound_DarkShield'
        ),
    })
    sound_shield_on: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x2ff5a809, original_name='Sound_ShieldOn'
        ),
    })
    ing_possession_data: IngPossessionData = dataclasses.field(default_factory=IngPossessionData, metadata={
        'reflection': FieldReflection[IngPossessionData](
            IngPossessionData, id=0xe61748ed, original_name='IngPossessionData', from_json=IngPossessionData.from_json, to_json=IngPossessionData.to_json
        ),
    })
    light_shield_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x80a8ef3b, original_name='LightShieldVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    dark_shield_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xa21c90ea, original_name='DarkShieldVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
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
        if property_count != 29:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbd80fd94
        command_module_flags = SplitterCommandModuleFlags.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x00d74fc3
        max_linear_velocity = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0b5c3c1a
        max_turn_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa0b3e1be
        scanning_turn_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe32fcae9
        min_laser_pulse_attack_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc5e0b92c
        min_laser_pulse_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc17a8806
        max_laser_pulse_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe75bae9e
        max_laser_pulse_shots = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4d77b7aa
        laser_pulse_projectile = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb763eb10
        laser_pulse_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 10.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xeda45014
        min_dodges = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7dd740fe
        max_dodges = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x47be3298
        dodge_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd3dec6dc
        reset_shield_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xecd9d92d
        shield_hp = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5ff006d1
        laser_sweep_turn_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1bd017ce
        laser_sweep_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 10.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4a37c437
        laser_sweep_beam_info = PlasmaBeamInfo.from_stream(data, game, property_size, default_override={'length': 500.0, 'expansion_speed': 4.0, 'life_time': 1.0, 'pulse_speed': 20.0, 'shutdown_time': 0.25, 'pulse_effect_scale': 2.0, 'inner_color': Color(r=0.5, g=0.5, b=0.5, a=0.5), 'outer_color': Color(r=0.6000000238418579, g=0.6000000238418579, b=0.0, a=0.5)})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9ec51fe4
        scan_beam_data = SplitterScanBeamData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xea307548
        sound_laser_sweep = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3779bd93
        sound_laser_charge_up = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc90dbdb4
        sound_docking = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe7724802
        sound_scanning = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd4a06273
        sound_light_shield = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xafc20631
        sound_dark_shield = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2ff5a809
        sound_shield_on = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe61748ed
        ing_possession_data = IngPossessionData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x80a8ef3b
        light_shield_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa21c90ea
        dark_shield_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        return cls(command_module_flags, max_linear_velocity, max_turn_speed, scanning_turn_speed, min_laser_pulse_attack_time, min_laser_pulse_range, max_laser_pulse_range, max_laser_pulse_shots, laser_pulse_projectile, laser_pulse_damage, min_dodges, max_dodges, dodge_chance, reset_shield_time, shield_hp, laser_sweep_turn_speed, laser_sweep_damage, laser_sweep_beam_info, scan_beam_data, sound_laser_sweep, sound_laser_charge_up, sound_docking, sound_scanning, sound_light_shield, sound_dark_shield, sound_shield_on, ing_possession_data, light_shield_vulnerability, dark_shield_vulnerability)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x1d')  # 29 properties

        data.write(b'\xbd\x80\xfd\x94')  # 0xbd80fd94
        data.write(b'\x00\x04')  # size
        self.command_module_flags.to_stream(data, game)

        data.write(b'\x00\xd7O\xc3')  # 0xd74fc3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_linear_velocity))

        data.write(b'\x0b\\<\x1a')  # 0xb5c3c1a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_turn_speed))

        data.write(b'\xa0\xb3\xe1\xbe')  # 0xa0b3e1be
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.scanning_turn_speed))

        data.write(b'\xe3/\xca\xe9')  # 0xe32fcae9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_laser_pulse_attack_time))

        data.write(b'\xc5\xe0\xb9,')  # 0xc5e0b92c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_laser_pulse_range))

        data.write(b'\xc1z\x88\x06')  # 0xc17a8806
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_laser_pulse_range))

        data.write(b'\xe7[\xae\x9e')  # 0xe75bae9e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_laser_pulse_shots))

        data.write(b'Mw\xb7\xaa')  # 0x4d77b7aa
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.laser_pulse_projectile))

        data.write(b'\xb7c\xeb\x10')  # 0xb763eb10
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.laser_pulse_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xed\xa4P\x14')  # 0xeda45014
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.min_dodges))

        data.write(b'}\xd7@\xfe')  # 0x7dd740fe
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_dodges))

        data.write(b'G\xbe2\x98')  # 0x47be3298
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dodge_chance))

        data.write(b'\xd3\xde\xc6\xdc')  # 0xd3dec6dc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.reset_shield_time))

        data.write(b'\xec\xd9\xd9-')  # 0xecd9d92d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.shield_hp))

        data.write(b'_\xf0\x06\xd1')  # 0x5ff006d1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.laser_sweep_turn_speed))

        data.write(b'\x1b\xd0\x17\xce')  # 0x1bd017ce
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.laser_sweep_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'J7\xc47')  # 0x4a37c437
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.laser_sweep_beam_info.to_stream(data, game, default_override={'length': 500.0, 'expansion_speed': 4.0, 'life_time': 1.0, 'pulse_speed': 20.0, 'shutdown_time': 0.25, 'pulse_effect_scale': 2.0, 'inner_color': Color(r=0.5, g=0.5, b=0.5, a=0.5), 'outer_color': Color(r=0.6000000238418579, g=0.6000000238418579, b=0.0, a=0.5)})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9e\xc5\x1f\xe4')  # 0x9ec51fe4
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.scan_beam_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xea0uH')  # 0xea307548
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_laser_sweep))

        data.write(b'7y\xbd\x93')  # 0x3779bd93
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_laser_charge_up))

        data.write(b'\xc9\r\xbd\xb4')  # 0xc90dbdb4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_docking))

        data.write(b'\xe7rH\x02')  # 0xe7724802
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_scanning))

        data.write(b'\xd4\xa0bs')  # 0xd4a06273
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_light_shield))

        data.write(b'\xaf\xc2\x061')  # 0xafc20631
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_dark_shield))

        data.write(b'/\xf5\xa8\t')  # 0x2ff5a809
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_shield_on))

        data.write(b'\xe6\x17H\xed')  # 0xe61748ed
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ing_possession_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x80\xa8\xef;')  # 0x80a8ef3b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.light_shield_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa2\x1c\x90\xea')  # 0xa21c90ea
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.dark_shield_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SplitterCommandModuleDataJson", data)
        return cls(
            command_module_flags=SplitterCommandModuleFlags.from_json(json_data['command_module_flags']),
            max_linear_velocity=json_data['max_linear_velocity'],
            max_turn_speed=json_data['max_turn_speed'],
            scanning_turn_speed=json_data['scanning_turn_speed'],
            min_laser_pulse_attack_time=json_data['min_laser_pulse_attack_time'],
            min_laser_pulse_range=json_data['min_laser_pulse_range'],
            max_laser_pulse_range=json_data['max_laser_pulse_range'],
            max_laser_pulse_shots=json_data['max_laser_pulse_shots'],
            laser_pulse_projectile=json_data['laser_pulse_projectile'],
            laser_pulse_damage=DamageInfo.from_json(json_data['laser_pulse_damage']),
            min_dodges=json_data['min_dodges'],
            max_dodges=json_data['max_dodges'],
            dodge_chance=json_data['dodge_chance'],
            reset_shield_time=json_data['reset_shield_time'],
            shield_hp=json_data['shield_hp'],
            laser_sweep_turn_speed=json_data['laser_sweep_turn_speed'],
            laser_sweep_damage=DamageInfo.from_json(json_data['laser_sweep_damage']),
            laser_sweep_beam_info=PlasmaBeamInfo.from_json(json_data['laser_sweep_beam_info']),
            scan_beam_data=SplitterScanBeamData.from_json(json_data['scan_beam_data']),
            sound_laser_sweep=json_data['sound_laser_sweep'],
            sound_laser_charge_up=json_data['sound_laser_charge_up'],
            sound_docking=json_data['sound_docking'],
            sound_scanning=json_data['sound_scanning'],
            sound_light_shield=json_data['sound_light_shield'],
            sound_dark_shield=json_data['sound_dark_shield'],
            sound_shield_on=json_data['sound_shield_on'],
            ing_possession_data=IngPossessionData.from_json(json_data['ing_possession_data']),
            light_shield_vulnerability=DamageVulnerability.from_json(json_data['light_shield_vulnerability']),
            dark_shield_vulnerability=DamageVulnerability.from_json(json_data['dark_shield_vulnerability']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'command_module_flags': self.command_module_flags.to_json(),
            'max_linear_velocity': self.max_linear_velocity,
            'max_turn_speed': self.max_turn_speed,
            'scanning_turn_speed': self.scanning_turn_speed,
            'min_laser_pulse_attack_time': self.min_laser_pulse_attack_time,
            'min_laser_pulse_range': self.min_laser_pulse_range,
            'max_laser_pulse_range': self.max_laser_pulse_range,
            'max_laser_pulse_shots': self.max_laser_pulse_shots,
            'laser_pulse_projectile': self.laser_pulse_projectile,
            'laser_pulse_damage': self.laser_pulse_damage.to_json(),
            'min_dodges': self.min_dodges,
            'max_dodges': self.max_dodges,
            'dodge_chance': self.dodge_chance,
            'reset_shield_time': self.reset_shield_time,
            'shield_hp': self.shield_hp,
            'laser_sweep_turn_speed': self.laser_sweep_turn_speed,
            'laser_sweep_damage': self.laser_sweep_damage.to_json(),
            'laser_sweep_beam_info': self.laser_sweep_beam_info.to_json(),
            'scan_beam_data': self.scan_beam_data.to_json(),
            'sound_laser_sweep': self.sound_laser_sweep,
            'sound_laser_charge_up': self.sound_laser_charge_up,
            'sound_docking': self.sound_docking,
            'sound_scanning': self.sound_scanning,
            'sound_light_shield': self.sound_light_shield,
            'sound_dark_shield': self.sound_dark_shield,
            'sound_shield_on': self.sound_shield_on,
            'ing_possession_data': self.ing_possession_data.to_json(),
            'light_shield_vulnerability': self.light_shield_vulnerability.to_json(),
            'dark_shield_vulnerability': self.dark_shield_vulnerability.to_json(),
        }

    def _dependencies_for_laser_pulse_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.laser_pulse_projectile)

    def _dependencies_for_sound_laser_sweep(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_laser_sweep)

    def _dependencies_for_sound_laser_charge_up(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_laser_charge_up)

    def _dependencies_for_sound_docking(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_docking)

    def _dependencies_for_sound_scanning(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_scanning)

    def _dependencies_for_sound_light_shield(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_light_shield)

    def _dependencies_for_sound_dark_shield(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_dark_shield)

    def _dependencies_for_sound_shield_on(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_shield_on)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_laser_pulse_projectile, "laser_pulse_projectile", "AssetId"),
            (self.laser_sweep_beam_info.dependencies_for, "laser_sweep_beam_info", "PlasmaBeamInfo"),
            (self._dependencies_for_sound_laser_sweep, "sound_laser_sweep", "int"),
            (self._dependencies_for_sound_laser_charge_up, "sound_laser_charge_up", "int"),
            (self._dependencies_for_sound_docking, "sound_docking", "int"),
            (self._dependencies_for_sound_scanning, "sound_scanning", "int"),
            (self._dependencies_for_sound_light_shield, "sound_light_shield", "int"),
            (self._dependencies_for_sound_dark_shield, "sound_dark_shield", "int"),
            (self._dependencies_for_sound_shield_on, "sound_shield_on", "int"),
            (self.ing_possession_data.dependencies_for, "ing_possession_data", "IngPossessionData"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for SplitterCommandModuleData.{field_name} ({field_type}): {e}"
                )


def _decode_command_module_flags(data: typing.BinaryIO, game: Game, property_size: int) -> SplitterCommandModuleFlags:
    return SplitterCommandModuleFlags.from_stream(data, game)


def _decode_laser_pulse_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 10.0})


def _decode_laser_sweep_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 10.0})


def _decode_laser_sweep_beam_info(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size, default_override={'length': 500.0, 'expansion_speed': 4.0, 'life_time': 1.0, 'pulse_speed': 20.0, 'shutdown_time': 0.25, 'pulse_effect_scale': 2.0, 'inner_color': Color(r=0.5, g=0.5, b=0.5, a=0.5), 'outer_color': Color(r=0.6000000238418579, g=0.6000000238418579, b=0.0, a=0.5)})


def _decode_scan_beam_data(data: typing.BinaryIO, game: Game, property_size: int) -> SplitterScanBeamData:
    return SplitterScanBeamData.from_stream(data, game, property_size)


def _decode_ing_possession_data(data: typing.BinaryIO, game: Game, property_size: int) -> IngPossessionData:
    return IngPossessionData.from_stream(data, game, property_size)


def _decode_light_shield_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_dark_shield_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xbd80fd94: ('command_module_flags', _decode_command_module_flags),
    0x00d74fc3: ('max_linear_velocity', structs.decode_BIG_f),
    0x0b5c3c1a: ('max_turn_speed', structs.decode_BIG_f),
    0xa0b3e1be: ('scanning_turn_speed', structs.decode_BIG_f),
    0xe32fcae9: ('min_laser_pulse_attack_time', structs.decode_BIG_f),
    0xc5e0b92c: ('min_laser_pulse_range', structs.decode_BIG_f),
    0xc17a8806: ('max_laser_pulse_range', structs.decode_BIG_f),
    0xe75bae9e: ('max_laser_pulse_shots', structs.decode_BIG_l),
    0x4d77b7aa: ('laser_pulse_projectile', structs.decode_BIG_L),
    0xb763eb10: ('laser_pulse_damage', _decode_laser_pulse_damage),
    0xeda45014: ('min_dodges', structs.decode_BIG_l),
    0x7dd740fe: ('max_dodges', structs.decode_BIG_l),
    0x47be3298: ('dodge_chance', structs.decode_BIG_f),
    0xd3dec6dc: ('reset_shield_time', structs.decode_BIG_f),
    0xecd9d92d: ('shield_hp', structs.decode_BIG_f),
    0x5ff006d1: ('laser_sweep_turn_speed', structs.decode_BIG_f),
    0x1bd017ce: ('laser_sweep_damage', _decode_laser_sweep_damage),
    0x4a37c437: ('laser_sweep_beam_info', _decode_laser_sweep_beam_info),
    0x9ec51fe4: ('scan_beam_data', _decode_scan_beam_data),
    0xea307548: ('sound_laser_sweep', structs.decode_BIG_l),
    0x3779bd93: ('sound_laser_charge_up', structs.decode_BIG_l),
    0xc90dbdb4: ('sound_docking', structs.decode_BIG_l),
    0xe7724802: ('sound_scanning', structs.decode_BIG_l),
    0xd4a06273: ('sound_light_shield', structs.decode_BIG_l),
    0xafc20631: ('sound_dark_shield', structs.decode_BIG_l),
    0x2ff5a809: ('sound_shield_on', structs.decode_BIG_l),
    0xe61748ed: ('ing_possession_data', _decode_ing_possession_data),
    0x80a8ef3b: ('light_shield_vulnerability', _decode_light_shield_vulnerability),
    0xa21c90ea: ('dark_shield_vulnerability', _decode_dark_shield_vulnerability),
}
