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
from retro_data_structures.properties.echoes.archetypes.AudioPlaybackParms import AudioPlaybackParms
from retro_data_structures.properties.echoes.archetypes.EmperorIngStage1BeamAttackData import EmperorIngStage1BeamAttackData
from retro_data_structures.properties.echoes.archetypes.EmperorIngStage1MeleeData import EmperorIngStage1MeleeData
from retro_data_structures.properties.echoes.archetypes.EmperorIngStage1ProjectileAttackData import EmperorIngStage1ProjectileAttackData
from retro_data_structures.properties.echoes.archetypes.EmperorIngStage1TauntAttackData import EmperorIngStage1TauntAttackData
from retro_data_structures.properties.echoes.archetypes.EmperorIngStage1TentacleData import EmperorIngStage1TentacleData
from retro_data_structures.properties.echoes.archetypes.EmperorIngStage1WarpAttackData import EmperorIngStage1WarpAttackData

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class EmperorIngStage1DataJson(typing_extensions.TypedDict):
        tentacle: json_util.JsonObject
        melee: json_util.JsonObject
        projectile: json_util.JsonObject
        warp: json_util.JsonObject
        taunt_attack: json_util.JsonObject
        beam_attack: json_util.JsonObject
        heart_exposed_time: float
        unknown_0x905938b8: float
        unknown_0xb826317a: float
        heart_damage_sound: json_util.JsonObject
        turn_speed_accel: float
        max_turn_speed_normal: float
        max_turn_speed_melee: float
        max_turn_speed_jump_rope: float
        vulnerability_change_sound: int
        taunt_frequency: float
        attack_interval_min: float
        attack_interval_max: float
    

@dataclasses.dataclass()
class EmperorIngStage1Data(BaseProperty):
    tentacle: EmperorIngStage1TentacleData = dataclasses.field(default_factory=EmperorIngStage1TentacleData, metadata={
        'reflection': FieldReflection[EmperorIngStage1TentacleData](
            EmperorIngStage1TentacleData, id=0xb3c6398f, original_name='Tentacle', from_json=EmperorIngStage1TentacleData.from_json, to_json=EmperorIngStage1TentacleData.to_json
        ),
    })
    melee: EmperorIngStage1MeleeData = dataclasses.field(default_factory=EmperorIngStage1MeleeData, metadata={
        'reflection': FieldReflection[EmperorIngStage1MeleeData](
            EmperorIngStage1MeleeData, id=0xf59f9a60, original_name='Melee', from_json=EmperorIngStage1MeleeData.from_json, to_json=EmperorIngStage1MeleeData.to_json
        ),
    })
    projectile: EmperorIngStage1ProjectileAttackData = dataclasses.field(default_factory=EmperorIngStage1ProjectileAttackData, metadata={
        'reflection': FieldReflection[EmperorIngStage1ProjectileAttackData](
            EmperorIngStage1ProjectileAttackData, id=0xa1cda0b6, original_name='Projectile', from_json=EmperorIngStage1ProjectileAttackData.from_json, to_json=EmperorIngStage1ProjectileAttackData.to_json
        ),
    })
    warp: EmperorIngStage1WarpAttackData = dataclasses.field(default_factory=EmperorIngStage1WarpAttackData, metadata={
        'reflection': FieldReflection[EmperorIngStage1WarpAttackData](
            EmperorIngStage1WarpAttackData, id=0x85f36473, original_name='Warp', from_json=EmperorIngStage1WarpAttackData.from_json, to_json=EmperorIngStage1WarpAttackData.to_json
        ),
    })
    taunt_attack: EmperorIngStage1TauntAttackData = dataclasses.field(default_factory=EmperorIngStage1TauntAttackData, metadata={
        'reflection': FieldReflection[EmperorIngStage1TauntAttackData](
            EmperorIngStage1TauntAttackData, id=0xb4bc04c4, original_name='TauntAttack', from_json=EmperorIngStage1TauntAttackData.from_json, to_json=EmperorIngStage1TauntAttackData.to_json
        ),
    })
    beam_attack: EmperorIngStage1BeamAttackData = dataclasses.field(default_factory=EmperorIngStage1BeamAttackData, metadata={
        'reflection': FieldReflection[EmperorIngStage1BeamAttackData](
            EmperorIngStage1BeamAttackData, id=0x8e6d20ec, original_name='BeamAttack', from_json=EmperorIngStage1BeamAttackData.from_json, to_json=EmperorIngStage1BeamAttackData.to_json
        ),
    })
    heart_exposed_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa588afd1, original_name='HeartExposedTime'
        ),
    })
    unknown_0x905938b8: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x905938b8, original_name='Unknown'
        ),
    })
    unknown_0xb826317a: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb826317a, original_name='Unknown'
        ),
    })
    heart_damage_sound: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x88232388, original_name='HeartDamageSound', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    turn_speed_accel: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc36ae5ca, original_name='TurnSpeedAccel'
        ),
    })
    max_turn_speed_normal: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd30d9bb9, original_name='MaxTurnSpeedNormal'
        ),
    })
    max_turn_speed_melee: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb02cd31f, original_name='MaxTurnSpeedMelee'
        ),
    })
    max_turn_speed_jump_rope: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe5a7c358, original_name='MaxTurnSpeedJumpRope'
        ),
    })
    vulnerability_change_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x93357240, original_name='VulnerabilityChangeSound'
        ),
    })
    taunt_frequency: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x293a0c19, original_name='TauntFrequency'
        ),
    })
    attack_interval_min: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x31ebf869, original_name='AttackIntervalMin'
        ),
    })
    attack_interval_max: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd78b5788, original_name='AttackIntervalMax'
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
        if property_count != 18:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3c6398f
        tentacle = EmperorIngStage1TentacleData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf59f9a60
        melee = EmperorIngStage1MeleeData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa1cda0b6
        projectile = EmperorIngStage1ProjectileAttackData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x85f36473
        warp = EmperorIngStage1WarpAttackData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb4bc04c4
        taunt_attack = EmperorIngStage1TauntAttackData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8e6d20ec
        beam_attack = EmperorIngStage1BeamAttackData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa588afd1
        heart_exposed_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x905938b8
        unknown_0x905938b8 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb826317a
        unknown_0xb826317a = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x88232388
        heart_damage_sound = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc36ae5ca
        turn_speed_accel = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd30d9bb9
        max_turn_speed_normal = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb02cd31f
        max_turn_speed_melee = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe5a7c358
        max_turn_speed_jump_rope = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x93357240
        vulnerability_change_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x293a0c19
        taunt_frequency = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x31ebf869
        attack_interval_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd78b5788
        attack_interval_max = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(tentacle, melee, projectile, warp, taunt_attack, beam_attack, heart_exposed_time, unknown_0x905938b8, unknown_0xb826317a, heart_damage_sound, turn_speed_accel, max_turn_speed_normal, max_turn_speed_melee, max_turn_speed_jump_rope, vulnerability_change_sound, taunt_frequency, attack_interval_min, attack_interval_max)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x12')  # 18 properties

        data.write(b'\xb3\xc69\x8f')  # 0xb3c6398f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.tentacle.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf5\x9f\x9a`')  # 0xf59f9a60
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.melee.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa1\xcd\xa0\xb6')  # 0xa1cda0b6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.projectile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x85\xf3ds')  # 0x85f36473
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.warp.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb4\xbc\x04\xc4')  # 0xb4bc04c4
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.taunt_attack.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8em \xec')  # 0x8e6d20ec
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.beam_attack.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa5\x88\xaf\xd1')  # 0xa588afd1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.heart_exposed_time))

        data.write(b'\x90Y8\xb8')  # 0x905938b8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x905938b8))

        data.write(b'\xb8&1z')  # 0xb826317a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xb826317a))

        data.write(b'\x88##\x88')  # 0x88232388
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.heart_damage_sound.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc3j\xe5\xca')  # 0xc36ae5ca
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.turn_speed_accel))

        data.write(b'\xd3\r\x9b\xb9')  # 0xd30d9bb9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_turn_speed_normal))

        data.write(b'\xb0,\xd3\x1f')  # 0xb02cd31f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_turn_speed_melee))

        data.write(b'\xe5\xa7\xc3X')  # 0xe5a7c358
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_turn_speed_jump_rope))

        data.write(b'\x935r@')  # 0x93357240
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.vulnerability_change_sound))

        data.write(b'):\x0c\x19')  # 0x293a0c19
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.taunt_frequency))

        data.write(b'1\xeb\xf8i')  # 0x31ebf869
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.attack_interval_min))

        data.write(b'\xd7\x8bW\x88')  # 0xd78b5788
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.attack_interval_max))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("EmperorIngStage1DataJson", data)
        return cls(
            tentacle=EmperorIngStage1TentacleData.from_json(json_data['tentacle']),
            melee=EmperorIngStage1MeleeData.from_json(json_data['melee']),
            projectile=EmperorIngStage1ProjectileAttackData.from_json(json_data['projectile']),
            warp=EmperorIngStage1WarpAttackData.from_json(json_data['warp']),
            taunt_attack=EmperorIngStage1TauntAttackData.from_json(json_data['taunt_attack']),
            beam_attack=EmperorIngStage1BeamAttackData.from_json(json_data['beam_attack']),
            heart_exposed_time=json_data['heart_exposed_time'],
            unknown_0x905938b8=json_data['unknown_0x905938b8'],
            unknown_0xb826317a=json_data['unknown_0xb826317a'],
            heart_damage_sound=AudioPlaybackParms.from_json(json_data['heart_damage_sound']),
            turn_speed_accel=json_data['turn_speed_accel'],
            max_turn_speed_normal=json_data['max_turn_speed_normal'],
            max_turn_speed_melee=json_data['max_turn_speed_melee'],
            max_turn_speed_jump_rope=json_data['max_turn_speed_jump_rope'],
            vulnerability_change_sound=json_data['vulnerability_change_sound'],
            taunt_frequency=json_data['taunt_frequency'],
            attack_interval_min=json_data['attack_interval_min'],
            attack_interval_max=json_data['attack_interval_max'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'tentacle': self.tentacle.to_json(),
            'melee': self.melee.to_json(),
            'projectile': self.projectile.to_json(),
            'warp': self.warp.to_json(),
            'taunt_attack': self.taunt_attack.to_json(),
            'beam_attack': self.beam_attack.to_json(),
            'heart_exposed_time': self.heart_exposed_time,
            'unknown_0x905938b8': self.unknown_0x905938b8,
            'unknown_0xb826317a': self.unknown_0xb826317a,
            'heart_damage_sound': self.heart_damage_sound.to_json(),
            'turn_speed_accel': self.turn_speed_accel,
            'max_turn_speed_normal': self.max_turn_speed_normal,
            'max_turn_speed_melee': self.max_turn_speed_melee,
            'max_turn_speed_jump_rope': self.max_turn_speed_jump_rope,
            'vulnerability_change_sound': self.vulnerability_change_sound,
            'taunt_frequency': self.taunt_frequency,
            'attack_interval_min': self.attack_interval_min,
            'attack_interval_max': self.attack_interval_max,
        }

    def _dependencies_for_vulnerability_change_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.vulnerability_change_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.tentacle.dependencies_for, "tentacle", "EmperorIngStage1TentacleData"),
            (self.projectile.dependencies_for, "projectile", "EmperorIngStage1ProjectileAttackData"),
            (self.warp.dependencies_for, "warp", "EmperorIngStage1WarpAttackData"),
            (self.taunt_attack.dependencies_for, "taunt_attack", "EmperorIngStage1TauntAttackData"),
            (self.beam_attack.dependencies_for, "beam_attack", "EmperorIngStage1BeamAttackData"),
            (self.heart_damage_sound.dependencies_for, "heart_damage_sound", "AudioPlaybackParms"),
            (self._dependencies_for_vulnerability_change_sound, "vulnerability_change_sound", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for EmperorIngStage1Data.{field_name} ({field_type}): {e}"
                )


def _decode_tentacle(data: typing.BinaryIO, game: Game, property_size: int) -> EmperorIngStage1TentacleData:
    return EmperorIngStage1TentacleData.from_stream(data, game, property_size)


def _decode_melee(data: typing.BinaryIO, game: Game, property_size: int) -> EmperorIngStage1MeleeData:
    return EmperorIngStage1MeleeData.from_stream(data, game, property_size)


def _decode_projectile(data: typing.BinaryIO, game: Game, property_size: int) -> EmperorIngStage1ProjectileAttackData:
    return EmperorIngStage1ProjectileAttackData.from_stream(data, game, property_size)


def _decode_warp(data: typing.BinaryIO, game: Game, property_size: int) -> EmperorIngStage1WarpAttackData:
    return EmperorIngStage1WarpAttackData.from_stream(data, game, property_size)


def _decode_taunt_attack(data: typing.BinaryIO, game: Game, property_size: int) -> EmperorIngStage1TauntAttackData:
    return EmperorIngStage1TauntAttackData.from_stream(data, game, property_size)


def _decode_beam_attack(data: typing.BinaryIO, game: Game, property_size: int) -> EmperorIngStage1BeamAttackData:
    return EmperorIngStage1BeamAttackData.from_stream(data, game, property_size)


def _decode_heart_damage_sound(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xb3c6398f: ('tentacle', _decode_tentacle),
    0xf59f9a60: ('melee', _decode_melee),
    0xa1cda0b6: ('projectile', _decode_projectile),
    0x85f36473: ('warp', _decode_warp),
    0xb4bc04c4: ('taunt_attack', _decode_taunt_attack),
    0x8e6d20ec: ('beam_attack', _decode_beam_attack),
    0xa588afd1: ('heart_exposed_time', structs.decode_BIG_f),
    0x905938b8: ('unknown_0x905938b8', structs.decode_BIG_f),
    0xb826317a: ('unknown_0xb826317a', structs.decode_BIG_f),
    0x88232388: ('heart_damage_sound', _decode_heart_damage_sound),
    0xc36ae5ca: ('turn_speed_accel', structs.decode_BIG_f),
    0xd30d9bb9: ('max_turn_speed_normal', structs.decode_BIG_f),
    0xb02cd31f: ('max_turn_speed_melee', structs.decode_BIG_f),
    0xe5a7c358: ('max_turn_speed_jump_rope', structs.decode_BIG_f),
    0x93357240: ('vulnerability_change_sound', structs.decode_BIG_l),
    0x293a0c19: ('taunt_frequency', structs.decode_BIG_f),
    0x31ebf869: ('attack_interval_min', structs.decode_BIG_f),
    0xd78b5788: ('attack_interval_max', structs.decode_BIG_f),
}
