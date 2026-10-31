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
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    class TriggerInfoJson(typing_extensions.TypedDict):
        damage: json_util.JsonObject
        force_field: json_util.JsonValue
        flags: int
    

class TriggerFlags(enum.IntFlag):
    DetectPlayer = 1
    DetectMorphedPlayer = 2
    DetectUnmorphedPlayer = 4
    DetectPlayer1 = 2048
    DetectPlayer2 = 4096
    DetectPlayer3 = 8192
    DetectPlayer4 = 16384
    DetectAI = 32768
    KillOnEntered = 65536
    UseCollisionImpulses = 131072
    UseBooleanIntersection = 262144
    DetectCamera = 524288
    BlockEnvironmentalEffects = 1048576
    DetectProjectiles = 2097152
    DetectBombs = 4194304
    DetectPowerBombs = 8388608
    DetectBoostBall = 16777216
    SunlightMakesLumitesAppear = 33554432
    DeleteObjects = 67108864
    DetectSpiderBall = 134217728
    DetectScrewAttack = 268435456

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
class TriggerInfo(BaseProperty):
    damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x337f9524, original_name='Damage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    force_field: Vector = dataclasses.field(default_factory=lambda: Vector(x=0.0, y=0.0, z=0.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0x20927e9b, original_name='ForceField', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    flags: TriggerFlags = dataclasses.field(default=TriggerFlags(30726), metadata={
        'reflection': FieldReflection[TriggerFlags](
            TriggerFlags, id=0x82859f46, original_name='Flags', from_json=TriggerFlags.from_json, to_json=TriggerFlags.to_json
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
        if property_count != 3:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337f9524
        damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x20927e9b
        force_field = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x82859f46
        flags = TriggerFlags.from_stream(data, game)
    
        return cls(damage, force_field, flags)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x03')  # 3 properties

        data.write(b'3\x7f\x95$')  # 0x337f9524
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b' \x92~\x9b')  # 0x20927e9b
        data.write(b'\x00\x0c')  # size
        self.force_field.to_stream(data, game)

        data.write(b'\x82\x85\x9fF')  # 0x82859f46
        data.write(b'\x00\x04')  # size
        self.flags.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TriggerInfoJson", data)
        return cls(
            damage=DamageInfo.from_json(json_data['damage']),
            force_field=Vector.from_json(json_data['force_field']),
            flags=TriggerFlags.from_json(json_data['flags']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'damage': self.damage.to_json(),
            'force_field': self.force_field.to_json(),
            'flags': self.flags.to_json(),
        }


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_force_field(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


def _decode_flags(data: typing.BinaryIO, game: Game, property_size: int) -> TriggerFlags:
    return TriggerFlags.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x337f9524: ('damage', _decode_damage),
    0x20927e9b: ('force_field', _decode_force_field),
    0x82859f46: ('flags', _decode_flags),
}
