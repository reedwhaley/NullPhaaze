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
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    class TweakTargeting_ChargeBeamJson(typing_extensions.TypedDict):
        charge_weapon_max_rotation: float
        charge_weapon_alpha_fade: float
        charge_weapon_arm_scale: float
        charge_weapon_arm_position_offset: float
        charge_weapon_arm_transition_time: float
        unknown_0x70caf349: float
        unknown_0x955a5177: float
        unknown_0x95ed96c2: float
        charge_weapon_arm_post_shot_alpha: json_util.JsonObject
        charge_weapon_arm_post_shot_scale: json_util.JsonObject
    

@dataclasses.dataclass()
class TweakTargeting_ChargeBeam(BaseProperty):
    charge_weapon_max_rotation: float = dataclasses.field(default=500.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4b435047, original_name='ChargeWeaponMaxRotation'
        ),
    })
    charge_weapon_alpha_fade: float = dataclasses.field(default=-0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0ece183c, original_name='ChargeWeaponAlphaFade'
        ),
    })
    charge_weapon_arm_scale: float = dataclasses.field(default=0.6000000238418579, metadata={
        'reflection': FieldReflection[float](
            float, id=0xab03dcb9, original_name='ChargeWeaponArmScale'
        ),
    })
    charge_weapon_arm_position_offset: float = dataclasses.field(default=0.44999998807907104, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc0120b9e, original_name='ChargeWeaponArmPositionOffset'
        ),
    })
    charge_weapon_arm_transition_time: float = dataclasses.field(default=0.75, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf5230e61, original_name='ChargeWeaponArmTransitionTime'
        ),
    })
    unknown_0x70caf349: float = dataclasses.field(default=45.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x70caf349, original_name='Unknown'
        ),
    })
    unknown_0x955a5177: float = dataclasses.field(default=15.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x955a5177, original_name='Unknown'
        ),
    })
    unknown_0x95ed96c2: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x95ed96c2, original_name='Unknown'
        ),
    })
    charge_weapon_arm_post_shot_alpha: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x138b3979, original_name='ChargeWeaponArmPostShotAlpha', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    charge_weapon_arm_post_shot_scale: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xdfa46325, original_name='ChargeWeaponArmPostShotScale', from_json=Spline.from_json, to_json=Spline.to_json
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
        if property_count != 10:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4b435047
        charge_weapon_max_rotation = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0ece183c
        charge_weapon_alpha_fade = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xab03dcb9
        charge_weapon_arm_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc0120b9e
        charge_weapon_arm_position_offset = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf5230e61
        charge_weapon_arm_transition_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x70caf349
        unknown_0x70caf349 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x955a5177
        unknown_0x955a5177 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95ed96c2
        unknown_0x95ed96c2 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x138b3979
        charge_weapon_arm_post_shot_alpha = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdfa46325
        charge_weapon_arm_post_shot_scale = Spline.from_stream(data, game, property_size)
    
        return cls(charge_weapon_max_rotation, charge_weapon_alpha_fade, charge_weapon_arm_scale, charge_weapon_arm_position_offset, charge_weapon_arm_transition_time, unknown_0x70caf349, unknown_0x955a5177, unknown_0x95ed96c2, charge_weapon_arm_post_shot_alpha, charge_weapon_arm_post_shot_scale)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\n')  # 10 properties

        data.write(b'KCPG')  # 0x4b435047
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_weapon_max_rotation))

        data.write(b'\x0e\xce\x18<')  # 0xece183c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_weapon_alpha_fade))

        data.write(b'\xab\x03\xdc\xb9')  # 0xab03dcb9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_weapon_arm_scale))

        data.write(b'\xc0\x12\x0b\x9e')  # 0xc0120b9e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_weapon_arm_position_offset))

        data.write(b'\xf5#\x0ea')  # 0xf5230e61
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_weapon_arm_transition_time))

        data.write(b'p\xca\xf3I')  # 0x70caf349
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x70caf349))

        data.write(b'\x95ZQw')  # 0x955a5177
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x955a5177))

        data.write(b'\x95\xed\x96\xc2')  # 0x95ed96c2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x95ed96c2))

        data.write(b'\x13\x8b9y')  # 0x138b3979
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.charge_weapon_arm_post_shot_alpha.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xdf\xa4c%')  # 0xdfa46325
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.charge_weapon_arm_post_shot_scale.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakTargeting_ChargeBeamJson", data)
        return cls(
            charge_weapon_max_rotation=json_data['charge_weapon_max_rotation'],
            charge_weapon_alpha_fade=json_data['charge_weapon_alpha_fade'],
            charge_weapon_arm_scale=json_data['charge_weapon_arm_scale'],
            charge_weapon_arm_position_offset=json_data['charge_weapon_arm_position_offset'],
            charge_weapon_arm_transition_time=json_data['charge_weapon_arm_transition_time'],
            unknown_0x70caf349=json_data['unknown_0x70caf349'],
            unknown_0x955a5177=json_data['unknown_0x955a5177'],
            unknown_0x95ed96c2=json_data['unknown_0x95ed96c2'],
            charge_weapon_arm_post_shot_alpha=Spline.from_json(json_data['charge_weapon_arm_post_shot_alpha']),
            charge_weapon_arm_post_shot_scale=Spline.from_json(json_data['charge_weapon_arm_post_shot_scale']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'charge_weapon_max_rotation': self.charge_weapon_max_rotation,
            'charge_weapon_alpha_fade': self.charge_weapon_alpha_fade,
            'charge_weapon_arm_scale': self.charge_weapon_arm_scale,
            'charge_weapon_arm_position_offset': self.charge_weapon_arm_position_offset,
            'charge_weapon_arm_transition_time': self.charge_weapon_arm_transition_time,
            'unknown_0x70caf349': self.unknown_0x70caf349,
            'unknown_0x955a5177': self.unknown_0x955a5177,
            'unknown_0x95ed96c2': self.unknown_0x95ed96c2,
            'charge_weapon_arm_post_shot_alpha': self.charge_weapon_arm_post_shot_alpha.to_json(),
            'charge_weapon_arm_post_shot_scale': self.charge_weapon_arm_post_shot_scale.to_json(),
        }


def _decode_charge_weapon_arm_post_shot_alpha(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_charge_weapon_arm_post_shot_scale(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x4b435047: ('charge_weapon_max_rotation', structs.decode_BIG_f),
    0x0ece183c: ('charge_weapon_alpha_fade', structs.decode_BIG_f),
    0xab03dcb9: ('charge_weapon_arm_scale', structs.decode_BIG_f),
    0xc0120b9e: ('charge_weapon_arm_position_offset', structs.decode_BIG_f),
    0xf5230e61: ('charge_weapon_arm_transition_time', structs.decode_BIG_f),
    0x70caf349: ('unknown_0x70caf349', structs.decode_BIG_f),
    0x955a5177: ('unknown_0x955a5177', structs.decode_BIG_f),
    0x95ed96c2: ('unknown_0x95ed96c2', structs.decode_BIG_f),
    0x138b3979: ('charge_weapon_arm_post_shot_alpha', _decode_charge_weapon_arm_post_shot_alpha),
    0xdfa46325: ('charge_weapon_arm_post_shot_scale', _decode_charge_weapon_arm_post_shot_scale),
}
