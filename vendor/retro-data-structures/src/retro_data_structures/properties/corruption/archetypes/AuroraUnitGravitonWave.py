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
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.ShockWaveInfo import ShockWaveInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class AuroraUnitGravitonWaveJson(typing_extensions.TypedDict):
        projectile: int
        damage: json_util.JsonObject
        weapon_info: json_util.JsonObject
        unknown_0xc2f2b95c: int
        unknown_0xeb8c4444: int
        min_next_pulse_time: float
        max_next_pulse_time: float
        unknown_0xb84c1410: float
        unknown_0x08730e2c: float
        turn_speed: float
        stage2_speed_scale: float
        stage3_speed_scale: float
        dongle_vulnerability: json_util.JsonObject
        dongle_model: int
        dongle_hinge1_model: int
        dongle_hinge2_model: int
        dongle_hinge3_model: int
        dongle_hinge4_model: int
        dongle_health: float
        next_attack_chance: json_util.JsonObject
    

@dataclasses.dataclass()
class AuroraUnitGravitonWave(BaseProperty):
    projectile: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xef485db9, original_name='Projectile'
        ),
    })
    damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x337f9524, original_name='Damage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    weapon_info: ShockWaveInfo = dataclasses.field(default_factory=ShockWaveInfo, metadata={
        'reflection': FieldReflection[ShockWaveInfo](
            ShockWaveInfo, id=0x85dca565, original_name='WeaponInfo', from_json=ShockWaveInfo.from_json, to_json=ShockWaveInfo.to_json
        ),
    })
    unknown_0xc2f2b95c: int = dataclasses.field(default=3, metadata={
        'reflection': FieldReflection[int](
            int, id=0xc2f2b95c, original_name='Unknown'
        ),
    })
    unknown_0xeb8c4444: int = dataclasses.field(default=5, metadata={
        'reflection': FieldReflection[int](
            int, id=0xeb8c4444, original_name='Unknown'
        ),
    })
    min_next_pulse_time: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6e7f4d8c, original_name='MinNextPulseTime'
        ),
    })
    max_next_pulse_time: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7d3aab27, original_name='MaxNextPulseTime'
        ),
    })
    unknown_0xb84c1410: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb84c1410, original_name='Unknown'
        ),
    })
    unknown_0x08730e2c: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x08730e2c, original_name='Unknown'
        ),
    })
    turn_speed: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x020c78bb, original_name='TurnSpeed'
        ),
    })
    stage2_speed_scale: float = dataclasses.field(default=1.2999999523162842, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb638cfa7, original_name='Stage2SpeedScale'
        ),
    })
    stage3_speed_scale: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x18505e36, original_name='Stage3SpeedScale'
        ),
    })
    dongle_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x6a98eef6, original_name='DongleVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    dongle_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x19aaf8f3, original_name='DongleModel'
        ),
    })
    dongle_hinge1_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5fca665e, original_name='DongleHinge1Model'
        ),
    })
    dongle_hinge2_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc628005f, original_name='DongleHinge2Model'
        ),
    })
    dongle_hinge3_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x07a6df9f, original_name='DongleHinge3Model'
        ),
    })
    dongle_hinge4_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2e9dca1c, original_name='DongleHinge4Model'
        ),
    })
    dongle_health: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa90e610c, original_name='DongleHealth'
        ),
    })
    next_attack_chance: AuroraUnit2AttackChance = dataclasses.field(default_factory=AuroraUnit2AttackChance, metadata={
        'reflection': FieldReflection[AuroraUnit2AttackChance](
            AuroraUnit2AttackChance, id=0x659df76d, original_name='NextAttackChance', from_json=AuroraUnit2AttackChance.from_json, to_json=AuroraUnit2AttackChance.to_json
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
        if property_count != 20:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xef485db9
        projectile = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337f9524
        damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x85dca565
        weapon_info = ShockWaveInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc2f2b95c
        unknown_0xc2f2b95c = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xeb8c4444
        unknown_0xeb8c4444 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6e7f4d8c
        min_next_pulse_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7d3aab27
        max_next_pulse_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb84c1410
        unknown_0xb84c1410 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x08730e2c
        unknown_0x08730e2c = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x020c78bb
        turn_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb638cfa7
        stage2_speed_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x18505e36
        stage3_speed_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6a98eef6
        dongle_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19aaf8f3
        dongle_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5fca665e
        dongle_hinge1_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc628005f
        dongle_hinge2_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x07a6df9f
        dongle_hinge3_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2e9dca1c
        dongle_hinge4_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa90e610c
        dongle_health = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x659df76d
        next_attack_chance = AuroraUnit2AttackChance.from_stream(data, game, property_size)
    
        return cls(projectile, damage, weapon_info, unknown_0xc2f2b95c, unknown_0xeb8c4444, min_next_pulse_time, max_next_pulse_time, unknown_0xb84c1410, unknown_0x08730e2c, turn_speed, stage2_speed_scale, stage3_speed_scale, dongle_vulnerability, dongle_model, dongle_hinge1_model, dongle_hinge2_model, dongle_hinge3_model, dongle_hinge4_model, dongle_health, next_attack_chance)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x14')  # 20 properties

        data.write(b'\xefH]\xb9')  # 0xef485db9
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.projectile))

        data.write(b'3\x7f\x95$')  # 0x337f9524
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x85\xdc\xa5e')  # 0x85dca565
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.weapon_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc2\xf2\xb9\\')  # 0xc2f2b95c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xc2f2b95c))

        data.write(b'\xeb\x8cDD')  # 0xeb8c4444
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.unknown_0xeb8c4444))

        data.write(b'n\x7fM\x8c')  # 0x6e7f4d8c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_next_pulse_time))

        data.write(b"}:\xab'")  # 0x7d3aab27
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_next_pulse_time))

        data.write(b'\xb8L\x14\x10')  # 0xb84c1410
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb84c1410))

        data.write(b'\x08s\x0e,')  # 0x8730e2c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x08730e2c))

        data.write(b'\x02\x0cx\xbb')  # 0x20c78bb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.turn_speed))

        data.write(b'\xb68\xcf\xa7')  # 0xb638cfa7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stage2_speed_scale))

        data.write(b'\x18P^6')  # 0x18505e36
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stage3_speed_scale))

        data.write(b'j\x98\xee\xf6')  # 0x6a98eef6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.dongle_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x19\xaa\xf8\xf3')  # 0x19aaf8f3
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.dongle_model))

        data.write(b'_\xcaf^')  # 0x5fca665e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.dongle_hinge1_model))

        data.write(b'\xc6(\x00_')  # 0xc628005f
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.dongle_hinge2_model))

        data.write(b'\x07\xa6\xdf\x9f')  # 0x7a6df9f
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.dongle_hinge3_model))

        data.write(b'.\x9d\xca\x1c')  # 0x2e9dca1c
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.dongle_hinge4_model))

        data.write(b'\xa9\x0ea\x0c')  # 0xa90e610c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.dongle_health))

        data.write(b'e\x9d\xf7m')  # 0x659df76d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.next_attack_chance.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("AuroraUnitGravitonWaveJson", data)
        return cls(
            projectile=json_data['projectile'],
            damage=DamageInfo.from_json(json_data['damage']),
            weapon_info=ShockWaveInfo.from_json(json_data['weapon_info']),
            unknown_0xc2f2b95c=json_data['unknown_0xc2f2b95c'],
            unknown_0xeb8c4444=json_data['unknown_0xeb8c4444'],
            min_next_pulse_time=json_data['min_next_pulse_time'],
            max_next_pulse_time=json_data['max_next_pulse_time'],
            unknown_0xb84c1410=json_data['unknown_0xb84c1410'],
            unknown_0x08730e2c=json_data['unknown_0x08730e2c'],
            turn_speed=json_data['turn_speed'],
            stage2_speed_scale=json_data['stage2_speed_scale'],
            stage3_speed_scale=json_data['stage3_speed_scale'],
            dongle_vulnerability=DamageVulnerability.from_json(json_data['dongle_vulnerability']),
            dongle_model=json_data['dongle_model'],
            dongle_hinge1_model=json_data['dongle_hinge1_model'],
            dongle_hinge2_model=json_data['dongle_hinge2_model'],
            dongle_hinge3_model=json_data['dongle_hinge3_model'],
            dongle_hinge4_model=json_data['dongle_hinge4_model'],
            dongle_health=json_data['dongle_health'],
            next_attack_chance=AuroraUnit2AttackChance.from_json(json_data['next_attack_chance']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'projectile': self.projectile,
            'damage': self.damage.to_json(),
            'weapon_info': self.weapon_info.to_json(),
            'unknown_0xc2f2b95c': self.unknown_0xc2f2b95c,
            'unknown_0xeb8c4444': self.unknown_0xeb8c4444,
            'min_next_pulse_time': self.min_next_pulse_time,
            'max_next_pulse_time': self.max_next_pulse_time,
            'unknown_0xb84c1410': self.unknown_0xb84c1410,
            'unknown_0x08730e2c': self.unknown_0x08730e2c,
            'turn_speed': self.turn_speed,
            'stage2_speed_scale': self.stage2_speed_scale,
            'stage3_speed_scale': self.stage3_speed_scale,
            'dongle_vulnerability': self.dongle_vulnerability.to_json(),
            'dongle_model': self.dongle_model,
            'dongle_hinge1_model': self.dongle_hinge1_model,
            'dongle_hinge2_model': self.dongle_hinge2_model,
            'dongle_hinge3_model': self.dongle_hinge3_model,
            'dongle_hinge4_model': self.dongle_hinge4_model,
            'dongle_health': self.dongle_health,
            'next_attack_chance': self.next_attack_chance.to_json(),
        }

    def _dependencies_for_projectile(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.projectile)

    def _dependencies_for_dongle_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.dongle_model)

    def _dependencies_for_dongle_hinge1_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.dongle_hinge1_model)

    def _dependencies_for_dongle_hinge2_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.dongle_hinge2_model)

    def _dependencies_for_dongle_hinge3_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.dongle_hinge3_model)

    def _dependencies_for_dongle_hinge4_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.dongle_hinge4_model)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_projectile, "projectile", "AssetId"),
            (self.weapon_info.dependencies_for, "weapon_info", "ShockWaveInfo"),
            (self._dependencies_for_dongle_model, "dongle_model", "AssetId"),
            (self._dependencies_for_dongle_hinge1_model, "dongle_hinge1_model", "AssetId"),
            (self._dependencies_for_dongle_hinge2_model, "dongle_hinge2_model", "AssetId"),
            (self._dependencies_for_dongle_hinge3_model, "dongle_hinge3_model", "AssetId"),
            (self._dependencies_for_dongle_hinge4_model, "dongle_hinge4_model", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for AuroraUnitGravitonWave.{field_name} ({field_type}): {e}"
                )


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_weapon_info(data: typing.BinaryIO, game: Game, property_size: int) -> ShockWaveInfo:
    return ShockWaveInfo.from_stream(data, game, property_size)


def _decode_dongle_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_next_attack_chance(data: typing.BinaryIO, game: Game, property_size: int) -> AuroraUnit2AttackChance:
    return AuroraUnit2AttackChance.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xef485db9: ('projectile', structs.decode_BIG_Q),
    0x337f9524: ('damage', _decode_damage),
    0x85dca565: ('weapon_info', _decode_weapon_info),
    0xc2f2b95c: ('unknown_0xc2f2b95c', structs.decode_BIG_l),
    0xeb8c4444: ('unknown_0xeb8c4444', structs.decode_BIG_l),
    0x6e7f4d8c: ('min_next_pulse_time', structs.decode_BIG_f),
    0x7d3aab27: ('max_next_pulse_time', structs.decode_BIG_f),
    0xb84c1410: ('unknown_0xb84c1410', structs.decode_BIG_f),
    0x08730e2c: ('unknown_0x08730e2c', structs.decode_BIG_f),
    0x020c78bb: ('turn_speed', structs.decode_BIG_f),
    0xb638cfa7: ('stage2_speed_scale', structs.decode_BIG_f),
    0x18505e36: ('stage3_speed_scale', structs.decode_BIG_f),
    0x6a98eef6: ('dongle_vulnerability', _decode_dongle_vulnerability),
    0x19aaf8f3: ('dongle_model', structs.decode_BIG_Q),
    0x5fca665e: ('dongle_hinge1_model', structs.decode_BIG_Q),
    0xc628005f: ('dongle_hinge2_model', structs.decode_BIG_Q),
    0x07a6df9f: ('dongle_hinge3_model', structs.decode_BIG_Q),
    0x2e9dca1c: ('dongle_hinge4_model', structs.decode_BIG_Q),
    0xa90e610c: ('dongle_health', structs.decode_BIG_f),
    0x659df76d: ('next_attack_chance', _decode_next_attack_chance),
}
