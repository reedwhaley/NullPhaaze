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
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class CommandoShieldJson(typing_extensions.TypedDict):
        shield_charge_damage: json_util.JsonObject
        shield_vulnerability: json_util.JsonObject
        shield_charge_min_attack_dist: float
        shield_charge_max_attack_dist: float
        shield_charge_speed: float
        shield_explode_effect: int
        sound_shield_explode: int
        arm_shield_damage_trigger: float
        arm_shield_damage_trigger_time: float
        arm_shield_chance: float
        arm_shield_time: float
        arm_shield_time_variation: float
        arm_shield_explode_effect: int
        shield_charge_effect: int
        arm_shield_effect: int
        sound_shield_turn_on: int
        sound_shield_turn_off: int
    

@dataclasses.dataclass()
class CommandoShield(BaseProperty):
    shield_charge_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x4da4a894, original_name='ShieldChargeDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    shield_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xd34f1323, original_name='ShieldVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    shield_charge_min_attack_dist: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc1d9dbc6, original_name='ShieldChargeMinAttackDist'
        ),
    })
    shield_charge_max_attack_dist: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x927fc322, original_name='ShieldChargeMaxAttackDist'
        ),
    })
    shield_charge_speed: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x717824b4, original_name='ShieldChargeSpeed'
        ),
    })
    shield_explode_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xa41f75ef, original_name='ShieldExplodeEffect'
        ),
    })
    sound_shield_explode: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xe6e92e73, original_name='Sound_ShieldExplode'
        ),
    })
    arm_shield_damage_trigger: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6cb0da5a, original_name='ArmShieldDamageTrigger'
        ),
    })
    arm_shield_damage_trigger_time: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc3938663, original_name='ArmShieldDamageTriggerTime'
        ),
    })
    arm_shield_chance: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x865c109c, original_name='ArmShieldChance'
        ),
    })
    arm_shield_time: float = dataclasses.field(default=4.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8b48a2f8, original_name='ArmShieldTime'
        ),
    })
    arm_shield_time_variation: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe1b0efa0, original_name='ArmShieldTimeVariation'
        ),
    })
    arm_shield_explode_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5ca206ca, original_name='ArmShieldExplodeEffect'
        ),
    })
    shield_charge_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xebf69cf0, original_name='ShieldChargeEffect'
        ),
    })
    arm_shield_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x4aab4e04, original_name='ArmShieldEffect'
        ),
    })
    sound_shield_turn_on: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xbf3c59b6, original_name='Sound_ShieldTurnOn'
        ),
    })
    sound_shield_turn_off: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x78be3b8d, original_name='Sound_ShieldTurnOff'
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
        if property_count != 17:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4da4a894
        shield_charge_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 10.0, 'di_knock_back_power': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd34f1323
        shield_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc1d9dbc6
        shield_charge_min_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x927fc322
        shield_charge_max_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x717824b4
        shield_charge_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa41f75ef
        shield_explode_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe6e92e73
        sound_shield_explode = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6cb0da5a
        arm_shield_damage_trigger = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc3938663
        arm_shield_damage_trigger_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x865c109c
        arm_shield_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8b48a2f8
        arm_shield_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe1b0efa0
        arm_shield_time_variation = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5ca206ca
        arm_shield_explode_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xebf69cf0
        shield_charge_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4aab4e04
        arm_shield_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbf3c59b6
        sound_shield_turn_on = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78be3b8d
        sound_shield_turn_off = structs.BIG_l.unpack(data.read(4))[0]
    
        return cls(shield_charge_damage, shield_vulnerability, shield_charge_min_attack_dist, shield_charge_max_attack_dist, shield_charge_speed, shield_explode_effect, sound_shield_explode, arm_shield_damage_trigger, arm_shield_damage_trigger_time, arm_shield_chance, arm_shield_time, arm_shield_time_variation, arm_shield_explode_effect, shield_charge_effect, arm_shield_effect, sound_shield_turn_on, sound_shield_turn_off)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x11')  # 17 properties

        data.write(b'M\xa4\xa8\x94')  # 0x4da4a894
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shield_charge_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 10.0, 'di_knock_back_power': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd3O\x13#')  # 0xd34f1323
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shield_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc1\xd9\xdb\xc6')  # 0xc1d9dbc6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.shield_charge_min_attack_dist))

        data.write(b'\x92\x7f\xc3"')  # 0x927fc322
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.shield_charge_max_attack_dist))

        data.write(b'qx$\xb4')  # 0x717824b4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.shield_charge_speed))

        data.write(b'\xa4\x1fu\xef')  # 0xa41f75ef
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.shield_explode_effect))

        data.write(b'\xe6\xe9.s')  # 0xe6e92e73
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_shield_explode))

        data.write(b'l\xb0\xdaZ')  # 0x6cb0da5a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.arm_shield_damage_trigger))

        data.write(b'\xc3\x93\x86c')  # 0xc3938663
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.arm_shield_damage_trigger_time))

        data.write(b'\x86\\\x10\x9c')  # 0x865c109c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.arm_shield_chance))

        data.write(b'\x8bH\xa2\xf8')  # 0x8b48a2f8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.arm_shield_time))

        data.write(b'\xe1\xb0\xef\xa0')  # 0xe1b0efa0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.arm_shield_time_variation))

        data.write(b'\\\xa2\x06\xca')  # 0x5ca206ca
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.arm_shield_explode_effect))

        data.write(b'\xeb\xf6\x9c\xf0')  # 0xebf69cf0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.shield_charge_effect))

        data.write(b'J\xabN\x04')  # 0x4aab4e04
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.arm_shield_effect))

        data.write(b'\xbf<Y\xb6')  # 0xbf3c59b6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_shield_turn_on))

        data.write(b'x\xbe;\x8d')  # 0x78be3b8d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_shield_turn_off))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("CommandoShieldJson", data)
        return cls(
            shield_charge_damage=DamageInfo.from_json(json_data['shield_charge_damage']),
            shield_vulnerability=DamageVulnerability.from_json(json_data['shield_vulnerability']),
            shield_charge_min_attack_dist=json_data['shield_charge_min_attack_dist'],
            shield_charge_max_attack_dist=json_data['shield_charge_max_attack_dist'],
            shield_charge_speed=json_data['shield_charge_speed'],
            shield_explode_effect=json_data['shield_explode_effect'],
            sound_shield_explode=json_data['sound_shield_explode'],
            arm_shield_damage_trigger=json_data['arm_shield_damage_trigger'],
            arm_shield_damage_trigger_time=json_data['arm_shield_damage_trigger_time'],
            arm_shield_chance=json_data['arm_shield_chance'],
            arm_shield_time=json_data['arm_shield_time'],
            arm_shield_time_variation=json_data['arm_shield_time_variation'],
            arm_shield_explode_effect=json_data['arm_shield_explode_effect'],
            shield_charge_effect=json_data['shield_charge_effect'],
            arm_shield_effect=json_data['arm_shield_effect'],
            sound_shield_turn_on=json_data['sound_shield_turn_on'],
            sound_shield_turn_off=json_data['sound_shield_turn_off'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'shield_charge_damage': self.shield_charge_damage.to_json(),
            'shield_vulnerability': self.shield_vulnerability.to_json(),
            'shield_charge_min_attack_dist': self.shield_charge_min_attack_dist,
            'shield_charge_max_attack_dist': self.shield_charge_max_attack_dist,
            'shield_charge_speed': self.shield_charge_speed,
            'shield_explode_effect': self.shield_explode_effect,
            'sound_shield_explode': self.sound_shield_explode,
            'arm_shield_damage_trigger': self.arm_shield_damage_trigger,
            'arm_shield_damage_trigger_time': self.arm_shield_damage_trigger_time,
            'arm_shield_chance': self.arm_shield_chance,
            'arm_shield_time': self.arm_shield_time,
            'arm_shield_time_variation': self.arm_shield_time_variation,
            'arm_shield_explode_effect': self.arm_shield_explode_effect,
            'shield_charge_effect': self.shield_charge_effect,
            'arm_shield_effect': self.arm_shield_effect,
            'sound_shield_turn_on': self.sound_shield_turn_on,
            'sound_shield_turn_off': self.sound_shield_turn_off,
        }

    def _dependencies_for_shield_explode_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_explode_effect)

    def _dependencies_for_sound_shield_explode(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_shield_explode)

    def _dependencies_for_arm_shield_explode_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.arm_shield_explode_effect)

    def _dependencies_for_shield_charge_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_charge_effect)

    def _dependencies_for_arm_shield_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.arm_shield_effect)

    def _dependencies_for_sound_shield_turn_on(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_shield_turn_on)

    def _dependencies_for_sound_shield_turn_off(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_shield_turn_off)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_shield_explode_effect, "shield_explode_effect", "AssetId"),
            (self._dependencies_for_sound_shield_explode, "sound_shield_explode", "int"),
            (self._dependencies_for_arm_shield_explode_effect, "arm_shield_explode_effect", "AssetId"),
            (self._dependencies_for_shield_charge_effect, "shield_charge_effect", "AssetId"),
            (self._dependencies_for_arm_shield_effect, "arm_shield_effect", "AssetId"),
            (self._dependencies_for_sound_shield_turn_on, "sound_shield_turn_on", "int"),
            (self._dependencies_for_sound_shield_turn_off, "sound_shield_turn_off", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for CommandoShield.{field_name} ({field_type}): {e}"
                )


def _decode_shield_charge_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 10.0, 'di_knock_back_power': 5.0})


def _decode_shield_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x4da4a894: ('shield_charge_damage', _decode_shield_charge_damage),
    0xd34f1323: ('shield_vulnerability', _decode_shield_vulnerability),
    0xc1d9dbc6: ('shield_charge_min_attack_dist', structs.decode_BIG_f),
    0x927fc322: ('shield_charge_max_attack_dist', structs.decode_BIG_f),
    0x717824b4: ('shield_charge_speed', structs.decode_BIG_f),
    0xa41f75ef: ('shield_explode_effect', structs.decode_BIG_L),
    0xe6e92e73: ('sound_shield_explode', structs.decode_BIG_l),
    0x6cb0da5a: ('arm_shield_damage_trigger', structs.decode_BIG_f),
    0xc3938663: ('arm_shield_damage_trigger_time', structs.decode_BIG_f),
    0x865c109c: ('arm_shield_chance', structs.decode_BIG_f),
    0x8b48a2f8: ('arm_shield_time', structs.decode_BIG_f),
    0xe1b0efa0: ('arm_shield_time_variation', structs.decode_BIG_f),
    0x5ca206ca: ('arm_shield_explode_effect', structs.decode_BIG_L),
    0xebf69cf0: ('shield_charge_effect', structs.decode_BIG_L),
    0x4aab4e04: ('arm_shield_effect', structs.decode_BIG_L),
    0xbf3c59b6: ('sound_shield_turn_on', structs.decode_BIG_l),
    0x78be3b8d: ('sound_shield_turn_off', structs.decode_BIG_l),
}
