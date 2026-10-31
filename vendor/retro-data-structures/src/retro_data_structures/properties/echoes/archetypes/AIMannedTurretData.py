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
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class AIMannedTurretDataJson(typing_extensions.TypedDict):
        max_horiz_rotation_left: float
        max_horiz_rotation_right: float
        max_vert_elevation_up: float
        max_vert_elevation_down: float
        damage_angle: float
        horiz_speed: float
        vert_speed: float
        fire_rate: float
        fire_rate_random_factor: float
        max_attack_angle: float
        max_attack_range: float
        start_attack_range: float
        attack_leash_timer: float
        weapon_damage: json_util.JsonObject
        weapon_effect: int
        health: json_util.JsonObject
        vulnerability: json_util.JsonObject
        state_machine: int
        telegraph_effect: int
    

@dataclasses.dataclass()
class AIMannedTurretData(BaseProperty):
    max_horiz_rotation_left: float = dataclasses.field(default=90.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x17cd8b2a, original_name='MaxHorizRotationLeft'
        ),
    })
    max_horiz_rotation_right: float = dataclasses.field(default=90.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1473dad2, original_name='MaxHorizRotationRight'
        ),
    })
    max_vert_elevation_up: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3650ce75, original_name='MaxVertElevationUp'
        ),
    })
    max_vert_elevation_down: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x78520e6e, original_name='MaxVertElevationDown'
        ),
    })
    damage_angle: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa39a5d72, original_name='DamageAngle'
        ),
    })
    horiz_speed: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfb2e32db, original_name='HorizSpeed'
        ),
    })
    vert_speed: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1b3c8683, original_name='VertSpeed'
        ),
    })
    fire_rate: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc6e48f18, original_name='FireRate'
        ),
    })
    fire_rate_random_factor: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf9bd253e, original_name='FireRateRandomFactor'
        ),
    })
    max_attack_angle: float = dataclasses.field(default=90.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf11f7384, original_name='MaxAttackAngle'
        ),
    })
    max_attack_range: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xff77c96f, original_name='MaxAttackRange'
        ),
    })
    start_attack_range: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb63f274c, original_name='StartAttackRange'
        ),
    })
    attack_leash_timer: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf8d1ea77, original_name='AttackLeashTimer'
        ),
    })
    weapon_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x8e5f7e96, original_name='WeaponDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    weapon_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['WPSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc43360a7, original_name='WeaponEffect'
        ),
    })
    health: HealthInfo = dataclasses.field(default_factory=HealthInfo, metadata={
        'reflection': FieldReflection[HealthInfo](
            HealthInfo, id=0xcf90d15e, original_name='Health', from_json=HealthInfo.from_json, to_json=HealthInfo.to_json
        ),
    })
    vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x7b71ae90, original_name='Vulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    state_machine: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['AFSM', 'FSM2'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x55744160, original_name='StateMachine'
        ),
    })
    telegraph_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x8f68ac21, original_name='TelegraphEffect'
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
        assert property_id == 0x17cd8b2a
        max_horiz_rotation_left = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1473dad2
        max_horiz_rotation_right = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3650ce75
        max_vert_elevation_up = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78520e6e
        max_vert_elevation_down = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa39a5d72
        damage_angle = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfb2e32db
        horiz_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1b3c8683
        vert_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc6e48f18
        fire_rate = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf9bd253e
        fire_rate_random_factor = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf11f7384
        max_attack_angle = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xff77c96f
        max_attack_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb63f274c
        start_attack_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf8d1ea77
        attack_leash_timer = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8e5f7e96
        weapon_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc43360a7
        weapon_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcf90d15e
        health = HealthInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7b71ae90
        vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x55744160
        state_machine = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8f68ac21
        telegraph_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        return cls(max_horiz_rotation_left, max_horiz_rotation_right, max_vert_elevation_up, max_vert_elevation_down, damage_angle, horiz_speed, vert_speed, fire_rate, fire_rate_random_factor, max_attack_angle, max_attack_range, start_attack_range, attack_leash_timer, weapon_damage, weapon_effect, health, vulnerability, state_machine, telegraph_effect)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x13')  # 19 properties

        data.write(b'\x17\xcd\x8b*')  # 0x17cd8b2a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_horiz_rotation_left))

        data.write(b'\x14s\xda\xd2')  # 0x1473dad2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_horiz_rotation_right))

        data.write(b'6P\xceu')  # 0x3650ce75
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_vert_elevation_up))

        data.write(b'xR\x0en')  # 0x78520e6e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_vert_elevation_down))

        data.write(b'\xa3\x9a]r')  # 0xa39a5d72
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.damage_angle))

        data.write(b'\xfb.2\xdb')  # 0xfb2e32db
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.horiz_speed))

        data.write(b'\x1b<\x86\x83')  # 0x1b3c8683
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.vert_speed))

        data.write(b'\xc6\xe4\x8f\x18')  # 0xc6e48f18
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fire_rate))

        data.write(b'\xf9\xbd%>')  # 0xf9bd253e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fire_rate_random_factor))

        data.write(b'\xf1\x1fs\x84')  # 0xf11f7384
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_attack_angle))

        data.write(b'\xffw\xc9o')  # 0xff77c96f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_attack_range))

        data.write(b"\xb6?'L")  # 0xb63f274c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.start_attack_range))

        data.write(b'\xf8\xd1\xeaw')  # 0xf8d1ea77
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.attack_leash_timer))

        data.write(b'\x8e_~\x96')  # 0x8e5f7e96
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.weapon_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc43`\xa7')  # 0xc43360a7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.weapon_effect))

        data.write(b'\xcf\x90\xd1^')  # 0xcf90d15e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.health.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'{q\xae\x90')  # 0x7b71ae90
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'UtA`')  # 0x55744160
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.state_machine))

        data.write(b'\x8fh\xac!')  # 0x8f68ac21
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.telegraph_effect))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("AIMannedTurretDataJson", data)
        return cls(
            max_horiz_rotation_left=json_data['max_horiz_rotation_left'],
            max_horiz_rotation_right=json_data['max_horiz_rotation_right'],
            max_vert_elevation_up=json_data['max_vert_elevation_up'],
            max_vert_elevation_down=json_data['max_vert_elevation_down'],
            damage_angle=json_data['damage_angle'],
            horiz_speed=json_data['horiz_speed'],
            vert_speed=json_data['vert_speed'],
            fire_rate=json_data['fire_rate'],
            fire_rate_random_factor=json_data['fire_rate_random_factor'],
            max_attack_angle=json_data['max_attack_angle'],
            max_attack_range=json_data['max_attack_range'],
            start_attack_range=json_data['start_attack_range'],
            attack_leash_timer=json_data['attack_leash_timer'],
            weapon_damage=DamageInfo.from_json(json_data['weapon_damage']),
            weapon_effect=json_data['weapon_effect'],
            health=HealthInfo.from_json(json_data['health']),
            vulnerability=DamageVulnerability.from_json(json_data['vulnerability']),
            state_machine=json_data['state_machine'],
            telegraph_effect=json_data['telegraph_effect'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'max_horiz_rotation_left': self.max_horiz_rotation_left,
            'max_horiz_rotation_right': self.max_horiz_rotation_right,
            'max_vert_elevation_up': self.max_vert_elevation_up,
            'max_vert_elevation_down': self.max_vert_elevation_down,
            'damage_angle': self.damage_angle,
            'horiz_speed': self.horiz_speed,
            'vert_speed': self.vert_speed,
            'fire_rate': self.fire_rate,
            'fire_rate_random_factor': self.fire_rate_random_factor,
            'max_attack_angle': self.max_attack_angle,
            'max_attack_range': self.max_attack_range,
            'start_attack_range': self.start_attack_range,
            'attack_leash_timer': self.attack_leash_timer,
            'weapon_damage': self.weapon_damage.to_json(),
            'weapon_effect': self.weapon_effect,
            'health': self.health.to_json(),
            'vulnerability': self.vulnerability.to_json(),
            'state_machine': self.state_machine,
            'telegraph_effect': self.telegraph_effect,
        }

    def _dependencies_for_weapon_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.weapon_effect)

    def _dependencies_for_state_machine(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.state_machine)

    def _dependencies_for_telegraph_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.telegraph_effect)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_weapon_effect, "weapon_effect", "AssetId"),
            (self._dependencies_for_state_machine, "state_machine", "AssetId"),
            (self._dependencies_for_telegraph_effect, "telegraph_effect", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for AIMannedTurretData.{field_name} ({field_type}): {e}"
                )


def _decode_weapon_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size)


def _decode_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x17cd8b2a: ('max_horiz_rotation_left', structs.decode_BIG_f),
    0x1473dad2: ('max_horiz_rotation_right', structs.decode_BIG_f),
    0x3650ce75: ('max_vert_elevation_up', structs.decode_BIG_f),
    0x78520e6e: ('max_vert_elevation_down', structs.decode_BIG_f),
    0xa39a5d72: ('damage_angle', structs.decode_BIG_f),
    0xfb2e32db: ('horiz_speed', structs.decode_BIG_f),
    0x1b3c8683: ('vert_speed', structs.decode_BIG_f),
    0xc6e48f18: ('fire_rate', structs.decode_BIG_f),
    0xf9bd253e: ('fire_rate_random_factor', structs.decode_BIG_f),
    0xf11f7384: ('max_attack_angle', structs.decode_BIG_f),
    0xff77c96f: ('max_attack_range', structs.decode_BIG_f),
    0xb63f274c: ('start_attack_range', structs.decode_BIG_f),
    0xf8d1ea77: ('attack_leash_timer', structs.decode_BIG_f),
    0x8e5f7e96: ('weapon_damage', _decode_weapon_damage),
    0xc43360a7: ('weapon_effect', structs.decode_BIG_L),
    0xcf90d15e: ('health', _decode_health),
    0x7b71ae90: ('vulnerability', _decode_vulnerability),
    0x55744160: ('state_machine', structs.decode_BIG_L),
    0x8f68ac21: ('telegraph_effect', structs.decode_BIG_L),
}
