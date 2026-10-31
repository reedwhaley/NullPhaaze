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
from retro_data_structures.properties.corruption.archetypes.PlasmaBeamInfo import PlasmaBeamInfo

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class AuroraUnitCuttingBeamsJson(typing_extensions.TypedDict):
        beam_info: json_util.JsonObject
        damage: json_util.JsonObject
        attack_duration: float
        attack_duration_variance: float
        turn_speed: float
        movement_speed: float
        min_fire_downward_angle: float
        max_fire_downward_angle: float
        unknown: float
        stage2_speed_scale: float
        stage3_speed_scale: float
        next_attack_chance: json_util.JsonObject
    

@dataclasses.dataclass()
class AuroraUnitCuttingBeams(BaseProperty):
    beam_info: PlasmaBeamInfo = dataclasses.field(default_factory=PlasmaBeamInfo, metadata={
        'reflection': FieldReflection[PlasmaBeamInfo](
            PlasmaBeamInfo, id=0x1598012a, original_name='BeamInfo', from_json=PlasmaBeamInfo.from_json, to_json=PlasmaBeamInfo.to_json
        ),
    })
    damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x337f9524, original_name='Damage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    attack_duration: float = dataclasses.field(default=7.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x16342c18, original_name='AttackDuration'
        ),
    })
    attack_duration_variance: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf6bdafb8, original_name='AttackDurationVariance'
        ),
    })
    turn_speed: float = dataclasses.field(default=45.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x020c78bb, original_name='TurnSpeed'
        ),
    })
    movement_speed: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x416f15e8, original_name='MovementSpeed'
        ),
    })
    min_fire_downward_angle: float = dataclasses.field(default=30.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x569e40ef, original_name='MinFireDownwardAngle'
        ),
    })
    max_fire_downward_angle: float = dataclasses.field(default=45.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x682b8867, original_name='MaxFireDownwardAngle'
        ),
    })
    unknown: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0acbf084, original_name='Unknown'
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
        if property_count != 12:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1598012a
        beam_info = PlasmaBeamInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337f9524
        damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x16342c18
        attack_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf6bdafb8
        attack_duration_variance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x020c78bb
        turn_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x416f15e8
        movement_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x569e40ef
        min_fire_downward_angle = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x682b8867
        max_fire_downward_angle = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0acbf084
        unknown = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb638cfa7
        stage2_speed_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x18505e36
        stage3_speed_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x659df76d
        next_attack_chance = AuroraUnit2AttackChance.from_stream(data, game, property_size)
    
        return cls(beam_info, damage, attack_duration, attack_duration_variance, turn_speed, movement_speed, min_fire_downward_angle, max_fire_downward_angle, unknown, stage2_speed_scale, stage3_speed_scale, next_attack_chance)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x0c')  # 12 properties

        data.write(b'\x15\x98\x01*')  # 0x1598012a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.beam_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'3\x7f\x95$')  # 0x337f9524
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x164,\x18')  # 0x16342c18
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.attack_duration))

        data.write(b'\xf6\xbd\xaf\xb8')  # 0xf6bdafb8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.attack_duration_variance))

        data.write(b'\x02\x0cx\xbb')  # 0x20c78bb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.turn_speed))

        data.write(b'Ao\x15\xe8')  # 0x416f15e8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.movement_speed))

        data.write(b'V\x9e@\xef')  # 0x569e40ef
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_fire_downward_angle))

        data.write(b'h+\x88g')  # 0x682b8867
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_fire_downward_angle))

        data.write(b'\n\xcb\xf0\x84')  # 0xacbf084
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown))

        data.write(b'\xb68\xcf\xa7')  # 0xb638cfa7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stage2_speed_scale))

        data.write(b'\x18P^6')  # 0x18505e36
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stage3_speed_scale))

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
        json_data = typing.cast("AuroraUnitCuttingBeamsJson", data)
        return cls(
            beam_info=PlasmaBeamInfo.from_json(json_data['beam_info']),
            damage=DamageInfo.from_json(json_data['damage']),
            attack_duration=json_data['attack_duration'],
            attack_duration_variance=json_data['attack_duration_variance'],
            turn_speed=json_data['turn_speed'],
            movement_speed=json_data['movement_speed'],
            min_fire_downward_angle=json_data['min_fire_downward_angle'],
            max_fire_downward_angle=json_data['max_fire_downward_angle'],
            unknown=json_data['unknown'],
            stage2_speed_scale=json_data['stage2_speed_scale'],
            stage3_speed_scale=json_data['stage3_speed_scale'],
            next_attack_chance=AuroraUnit2AttackChance.from_json(json_data['next_attack_chance']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'beam_info': self.beam_info.to_json(),
            'damage': self.damage.to_json(),
            'attack_duration': self.attack_duration,
            'attack_duration_variance': self.attack_duration_variance,
            'turn_speed': self.turn_speed,
            'movement_speed': self.movement_speed,
            'min_fire_downward_angle': self.min_fire_downward_angle,
            'max_fire_downward_angle': self.max_fire_downward_angle,
            'unknown': self.unknown,
            'stage2_speed_scale': self.stage2_speed_scale,
            'stage3_speed_scale': self.stage3_speed_scale,
            'next_attack_chance': self.next_attack_chance.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self.beam_info.dependencies_for(asset_manager)


def _decode_beam_info(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size)


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_next_attack_chance(data: typing.BinaryIO, game: Game, property_size: int) -> AuroraUnit2AttackChance:
    return AuroraUnit2AttackChance.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x1598012a: ('beam_info', _decode_beam_info),
    0x337f9524: ('damage', _decode_damage),
    0x16342c18: ('attack_duration', structs.decode_BIG_f),
    0xf6bdafb8: ('attack_duration_variance', structs.decode_BIG_f),
    0x020c78bb: ('turn_speed', structs.decode_BIG_f),
    0x416f15e8: ('movement_speed', structs.decode_BIG_f),
    0x569e40ef: ('min_fire_downward_angle', structs.decode_BIG_f),
    0x682b8867: ('max_fire_downward_angle', structs.decode_BIG_f),
    0x0acbf084: ('unknown', structs.decode_BIG_f),
    0xb638cfa7: ('stage2_speed_scale', structs.decode_BIG_f),
    0x18505e36: ('stage3_speed_scale', structs.decode_BIG_f),
    0x659df76d: ('next_attack_chance', _decode_next_attack_chance),
}
