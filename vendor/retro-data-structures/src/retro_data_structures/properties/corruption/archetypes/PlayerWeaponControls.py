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
from retro_data_structures.properties.corruption.archetypes.RevolutionControl import RevolutionControl
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    class PlayerWeaponControlsJson(typing_extensions.TypedDict):
        fire_beam: json_util.JsonObject
        auto_fire_beam: json_util.JsonObject
        charge_beam: json_util.JsonObject
        fire_missile: json_util.JsonObject
        fire_seeker: json_util.JsonObject
        hyper_mode: json_util.JsonObject
        switch_weapons: json_util.JsonObject
        aim_up_control: json_util.JsonObject
        aim_down_control: json_util.JsonObject
        aim_left_control: json_util.JsonObject
        aim_right_control: json_util.JsonObject
        orbit_free_aim_control: json_util.JsonObject
        view_lock_aim_up_control: json_util.JsonObject
        view_lock_aim_down_control: json_util.JsonObject
        orbit_lock_gun: bool
    

@dataclasses.dataclass()
class PlayerWeaponControls(BaseProperty):
    fire_beam: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x82168860, original_name='FireBeam', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    auto_fire_beam: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xd55c24c4, original_name='AutoFireBeam', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    charge_beam: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x6fe93d70, original_name='ChargeBeam', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    fire_missile: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xcbb88cb7, original_name='FireMissile', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    fire_seeker: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x711804a6, original_name='FireSeeker', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    hyper_mode: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0xfad9340e, original_name='HyperMode', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    switch_weapons: RevolutionControl = dataclasses.field(default_factory=RevolutionControl, metadata={
        'reflection': FieldReflection[RevolutionControl](
            RevolutionControl, id=0x78a69a53, original_name='SwitchWeapons', from_json=RevolutionControl.from_json, to_json=RevolutionControl.to_json
        ),
    })
    aim_up_control: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x002f1e9d, original_name='AimUpControl', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    aim_down_control: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xfad945be, original_name='AimDownControl', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    aim_left_control: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xa166125c, original_name='AimLeftControl', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    aim_right_control: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xdf87aa4e, original_name='AimRightControl', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    orbit_free_aim_control: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x03b0a66b, original_name='OrbitFreeAimControl', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    view_lock_aim_up_control: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x1a86616e, original_name='ViewLockAimUpControl', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    view_lock_aim_down_control: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x05f281c4, original_name='ViewLockAimDownControl', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    orbit_lock_gun: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x42c64d90, original_name='OrbitLockGun'
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
        if property_count != 15:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x82168860
        fire_beam = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd55c24c4
        auto_fire_beam = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6fe93d70
        charge_beam = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcbb88cb7
        fire_missile = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x711804a6
        fire_seeker = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfad9340e
        hyper_mode = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x78a69a53
        switch_weapons = RevolutionControl.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x002f1e9d
        aim_up_control = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfad945be
        aim_down_control = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa166125c
        aim_left_control = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdf87aa4e
        aim_right_control = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03b0a66b
        orbit_free_aim_control = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1a86616e
        view_lock_aim_up_control = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x05f281c4
        view_lock_aim_down_control = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42c64d90
        orbit_lock_gun = structs.BIG_bool_.unpack(data.read(1))[0]
    
        return cls(fire_beam, auto_fire_beam, charge_beam, fire_missile, fire_seeker, hyper_mode, switch_weapons, aim_up_control, aim_down_control, aim_left_control, aim_right_control, orbit_free_aim_control, view_lock_aim_up_control, view_lock_aim_down_control, orbit_lock_gun)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x0f')  # 15 properties

        data.write(b'\x82\x16\x88`')  # 0x82168860
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.fire_beam.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd5\\$\xc4')  # 0xd55c24c4
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.auto_fire_beam.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'o\xe9=p')  # 0x6fe93d70
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.charge_beam.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xcb\xb8\x8c\xb7')  # 0xcbb88cb7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.fire_missile.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'q\x18\x04\xa6')  # 0x711804a6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.fire_seeker.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfa\xd94\x0e')  # 0xfad9340e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper_mode.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'x\xa6\x9aS')  # 0x78a69a53
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.switch_weapons.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x00/\x1e\x9d')  # 0x2f1e9d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.aim_up_control.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfa\xd9E\xbe')  # 0xfad945be
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.aim_down_control.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa1f\x12\\')  # 0xa166125c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.aim_left_control.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xdf\x87\xaaN')  # 0xdf87aa4e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.aim_right_control.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x03\xb0\xa6k')  # 0x3b0a66b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.orbit_free_aim_control.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x1a\x86an')  # 0x1a86616e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.view_lock_aim_up_control.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x05\xf2\x81\xc4')  # 0x5f281c4
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.view_lock_aim_down_control.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'B\xc6M\x90')  # 0x42c64d90
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.orbit_lock_gun))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PlayerWeaponControlsJson", data)
        return cls(
            fire_beam=RevolutionControl.from_json(json_data['fire_beam']),
            auto_fire_beam=RevolutionControl.from_json(json_data['auto_fire_beam']),
            charge_beam=RevolutionControl.from_json(json_data['charge_beam']),
            fire_missile=RevolutionControl.from_json(json_data['fire_missile']),
            fire_seeker=RevolutionControl.from_json(json_data['fire_seeker']),
            hyper_mode=RevolutionControl.from_json(json_data['hyper_mode']),
            switch_weapons=RevolutionControl.from_json(json_data['switch_weapons']),
            aim_up_control=Spline.from_json(json_data['aim_up_control']),
            aim_down_control=Spline.from_json(json_data['aim_down_control']),
            aim_left_control=Spline.from_json(json_data['aim_left_control']),
            aim_right_control=Spline.from_json(json_data['aim_right_control']),
            orbit_free_aim_control=Spline.from_json(json_data['orbit_free_aim_control']),
            view_lock_aim_up_control=Spline.from_json(json_data['view_lock_aim_up_control']),
            view_lock_aim_down_control=Spline.from_json(json_data['view_lock_aim_down_control']),
            orbit_lock_gun=json_data['orbit_lock_gun'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'fire_beam': self.fire_beam.to_json(),
            'auto_fire_beam': self.auto_fire_beam.to_json(),
            'charge_beam': self.charge_beam.to_json(),
            'fire_missile': self.fire_missile.to_json(),
            'fire_seeker': self.fire_seeker.to_json(),
            'hyper_mode': self.hyper_mode.to_json(),
            'switch_weapons': self.switch_weapons.to_json(),
            'aim_up_control': self.aim_up_control.to_json(),
            'aim_down_control': self.aim_down_control.to_json(),
            'aim_left_control': self.aim_left_control.to_json(),
            'aim_right_control': self.aim_right_control.to_json(),
            'orbit_free_aim_control': self.orbit_free_aim_control.to_json(),
            'view_lock_aim_up_control': self.view_lock_aim_up_control.to_json(),
            'view_lock_aim_down_control': self.view_lock_aim_down_control.to_json(),
            'orbit_lock_gun': self.orbit_lock_gun,
        }


def _decode_fire_beam(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_auto_fire_beam(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_charge_beam(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_fire_missile(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_fire_seeker(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_hyper_mode(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_switch_weapons(data: typing.BinaryIO, game: Game, property_size: int) -> RevolutionControl:
    return RevolutionControl.from_stream(data, game, property_size)


def _decode_aim_up_control(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_aim_down_control(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_aim_left_control(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_aim_right_control(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_orbit_free_aim_control(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_view_lock_aim_up_control(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_view_lock_aim_down_control(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x82168860: ('fire_beam', _decode_fire_beam),
    0xd55c24c4: ('auto_fire_beam', _decode_auto_fire_beam),
    0x6fe93d70: ('charge_beam', _decode_charge_beam),
    0xcbb88cb7: ('fire_missile', _decode_fire_missile),
    0x711804a6: ('fire_seeker', _decode_fire_seeker),
    0xfad9340e: ('hyper_mode', _decode_hyper_mode),
    0x78a69a53: ('switch_weapons', _decode_switch_weapons),
    0x002f1e9d: ('aim_up_control', _decode_aim_up_control),
    0xfad945be: ('aim_down_control', _decode_aim_down_control),
    0xa166125c: ('aim_left_control', _decode_aim_left_control),
    0xdf87aa4e: ('aim_right_control', _decode_aim_right_control),
    0x03b0a66b: ('orbit_free_aim_control', _decode_orbit_free_aim_control),
    0x1a86616e: ('view_lock_aim_up_control', _decode_view_lock_aim_up_control),
    0x05f281c4: ('view_lock_aim_down_control', _decode_view_lock_aim_down_control),
    0x42c64d90: ('orbit_lock_gun', structs.decode_BIG_bool_),
}
