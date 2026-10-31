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

if typing.TYPE_CHECKING:
    class TweakPlayerControls_BooleansJson(typing_extensions.TypedDict):
        free_look_turns_player: bool
        hold_button_for_aim: bool
        toggle_aim_position: bool
        move_during_free_look: bool
        hold_buttons_for_free_look: bool
        two_buttons_for_free_look: bool
        fixed_vertical_aim: bool
        auto_aim_requires_orbit: bool
        orbit_around_enemies: bool
        aim_when_orbiting_point: bool
        aim_during_free_look: bool
        aim_at_orbit_point: bool
        free_look_fades_gun: bool
        orbit_point_fixed_offset: bool
        gun_button_toggles_holster: bool
        gun_not_firing_holsters_gun: bool
        falling_double_jump: bool
        impulse_double_jump: bool
        firing_cancels_camera_pitch: bool
        assisted_aiming_ignore_horizontal: bool
        assisted_aiming_ignore_vertical: bool
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xff1b0413, 0xe0c1d958, 0x55c20d58, 0x1f99c6ba, 0x18eb3ab5, 0xbdc01c71, 0x1c30f1a6, 0xda97bbcd, 0x83583abd, 0xc224d966, 0x1fcfaf3f, 0x3fb16819, 0x4fcf4b70, 0x7bb06a6, 0x4d8d57b, 0x5282c47e, 0x7304dafa, 0x7a49267d, 0xa796a8b9, 0x7c0599c8, 0x522ab1ac)


@dataclasses.dataclass()
class TweakPlayerControls_Booleans(BaseProperty):
    free_look_turns_player: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xff1b0413, original_name='FreeLookTurnsPlayer'
        ),
    })
    hold_button_for_aim: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xe0c1d958, original_name='HoldButtonForAim'
        ),
    })
    toggle_aim_position: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x55c20d58, original_name='ToggleAimPosition'
        ),
    })
    move_during_free_look: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x1f99c6ba, original_name='MoveDuringFreeLook'
        ),
    })
    hold_buttons_for_free_look: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x18eb3ab5, original_name='HoldButtonsForFreeLook'
        ),
    })
    two_buttons_for_free_look: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xbdc01c71, original_name='TwoButtonsForFreeLook'
        ),
    })
    fixed_vertical_aim: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x1c30f1a6, original_name='FixedVerticalAim'
        ),
    })
    auto_aim_requires_orbit: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xda97bbcd, original_name='AutoAimRequiresOrbit'
        ),
    })
    orbit_around_enemies: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x83583abd, original_name='OrbitAroundEnemies'
        ),
    })
    aim_when_orbiting_point: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xc224d966, original_name='AimWhenOrbitingPoint'
        ),
    })
    aim_during_free_look: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x1fcfaf3f, original_name='AimDuringFreeLook'
        ),
    })
    aim_at_orbit_point: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x3fb16819, original_name='AimAtOrbitPoint'
        ),
    })
    free_look_fades_gun: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x4fcf4b70, original_name='FreeLookFadesGun'
        ),
    })
    orbit_point_fixed_offset: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x07bb06a6, original_name='OrbitPointFixedOffset'
        ),
    })
    gun_button_toggles_holster: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x04d8d57b, original_name='GunButtonTogglesHolster'
        ),
    })
    gun_not_firing_holsters_gun: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x5282c47e, original_name='GunNotFiringHolstersGun'
        ),
    })
    falling_double_jump: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x7304dafa, original_name='FallingDoubleJump'
        ),
    })
    impulse_double_jump: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x7a49267d, original_name='ImpulseDoubleJump'
        ),
    })
    firing_cancels_camera_pitch: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xa796a8b9, original_name='FiringCancelsCameraPitch'
        ),
    })
    assisted_aiming_ignore_horizontal: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x7c0599c8, original_name='AssistedAimingIgnoreHorizontal'
        ),
    })
    assisted_aiming_ignore_vertical: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x522ab1ac, original_name='AssistedAimingIgnoreVertical'
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
        if property_count != 21:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?LH?')
    
        dec = _FAST_FORMAT.unpack(data.read(147))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24], dec[27], dec[30], dec[33], dec[36], dec[39], dec[42], dec[45], dec[48], dec[51], dec[54], dec[57], dec[60]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
            dec[26],
            dec[29],
            dec[32],
            dec[35],
            dec[38],
            dec[41],
            dec[44],
            dec[47],
            dec[50],
            dec[53],
            dec[56],
            dec[59],
            dec[62],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x15')  # 21 properties

        data.write(b'\xff\x1b\x04\x13')  # 0xff1b0413
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.free_look_turns_player))

        data.write(b'\xe0\xc1\xd9X')  # 0xe0c1d958
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.hold_button_for_aim))

        data.write(b'U\xc2\rX')  # 0x55c20d58
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.toggle_aim_position))

        data.write(b'\x1f\x99\xc6\xba')  # 0x1f99c6ba
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.move_during_free_look))

        data.write(b'\x18\xeb:\xb5')  # 0x18eb3ab5
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.hold_buttons_for_free_look))

        data.write(b'\xbd\xc0\x1cq')  # 0xbdc01c71
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.two_buttons_for_free_look))

        data.write(b'\x1c0\xf1\xa6')  # 0x1c30f1a6
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.fixed_vertical_aim))

        data.write(b'\xda\x97\xbb\xcd')  # 0xda97bbcd
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.auto_aim_requires_orbit))

        data.write(b'\x83X:\xbd')  # 0x83583abd
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.orbit_around_enemies))

        data.write(b'\xc2$\xd9f')  # 0xc224d966
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.aim_when_orbiting_point))

        data.write(b'\x1f\xcf\xaf?')  # 0x1fcfaf3f
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.aim_during_free_look))

        data.write(b'?\xb1h\x19')  # 0x3fb16819
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.aim_at_orbit_point))

        data.write(b'O\xcfKp')  # 0x4fcf4b70
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.free_look_fades_gun))

        data.write(b'\x07\xbb\x06\xa6')  # 0x7bb06a6
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.orbit_point_fixed_offset))

        data.write(b'\x04\xd8\xd5{')  # 0x4d8d57b
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.gun_button_toggles_holster))

        data.write(b'R\x82\xc4~')  # 0x5282c47e
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.gun_not_firing_holsters_gun))

        data.write(b's\x04\xda\xfa')  # 0x7304dafa
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.falling_double_jump))

        data.write(b'zI&}')  # 0x7a49267d
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.impulse_double_jump))

        data.write(b'\xa7\x96\xa8\xb9')  # 0xa796a8b9
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.firing_cancels_camera_pitch))

        data.write(b'|\x05\x99\xc8')  # 0x7c0599c8
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.assisted_aiming_ignore_horizontal))

        data.write(b'R*\xb1\xac')  # 0x522ab1ac
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.assisted_aiming_ignore_vertical))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayerControls_BooleansJson", data)
        return cls(
            free_look_turns_player=json_data['free_look_turns_player'],
            hold_button_for_aim=json_data['hold_button_for_aim'],
            toggle_aim_position=json_data['toggle_aim_position'],
            move_during_free_look=json_data['move_during_free_look'],
            hold_buttons_for_free_look=json_data['hold_buttons_for_free_look'],
            two_buttons_for_free_look=json_data['two_buttons_for_free_look'],
            fixed_vertical_aim=json_data['fixed_vertical_aim'],
            auto_aim_requires_orbit=json_data['auto_aim_requires_orbit'],
            orbit_around_enemies=json_data['orbit_around_enemies'],
            aim_when_orbiting_point=json_data['aim_when_orbiting_point'],
            aim_during_free_look=json_data['aim_during_free_look'],
            aim_at_orbit_point=json_data['aim_at_orbit_point'],
            free_look_fades_gun=json_data['free_look_fades_gun'],
            orbit_point_fixed_offset=json_data['orbit_point_fixed_offset'],
            gun_button_toggles_holster=json_data['gun_button_toggles_holster'],
            gun_not_firing_holsters_gun=json_data['gun_not_firing_holsters_gun'],
            falling_double_jump=json_data['falling_double_jump'],
            impulse_double_jump=json_data['impulse_double_jump'],
            firing_cancels_camera_pitch=json_data['firing_cancels_camera_pitch'],
            assisted_aiming_ignore_horizontal=json_data['assisted_aiming_ignore_horizontal'],
            assisted_aiming_ignore_vertical=json_data['assisted_aiming_ignore_vertical'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'free_look_turns_player': self.free_look_turns_player,
            'hold_button_for_aim': self.hold_button_for_aim,
            'toggle_aim_position': self.toggle_aim_position,
            'move_during_free_look': self.move_during_free_look,
            'hold_buttons_for_free_look': self.hold_buttons_for_free_look,
            'two_buttons_for_free_look': self.two_buttons_for_free_look,
            'fixed_vertical_aim': self.fixed_vertical_aim,
            'auto_aim_requires_orbit': self.auto_aim_requires_orbit,
            'orbit_around_enemies': self.orbit_around_enemies,
            'aim_when_orbiting_point': self.aim_when_orbiting_point,
            'aim_during_free_look': self.aim_during_free_look,
            'aim_at_orbit_point': self.aim_at_orbit_point,
            'free_look_fades_gun': self.free_look_fades_gun,
            'orbit_point_fixed_offset': self.orbit_point_fixed_offset,
            'gun_button_toggles_holster': self.gun_button_toggles_holster,
            'gun_not_firing_holsters_gun': self.gun_not_firing_holsters_gun,
            'falling_double_jump': self.falling_double_jump,
            'impulse_double_jump': self.impulse_double_jump,
            'firing_cancels_camera_pitch': self.firing_cancels_camera_pitch,
            'assisted_aiming_ignore_horizontal': self.assisted_aiming_ignore_horizontal,
            'assisted_aiming_ignore_vertical': self.assisted_aiming_ignore_vertical,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xff1b0413: ('free_look_turns_player', structs.decode_BIG_bool_),
    0xe0c1d958: ('hold_button_for_aim', structs.decode_BIG_bool_),
    0x55c20d58: ('toggle_aim_position', structs.decode_BIG_bool_),
    0x1f99c6ba: ('move_during_free_look', structs.decode_BIG_bool_),
    0x18eb3ab5: ('hold_buttons_for_free_look', structs.decode_BIG_bool_),
    0xbdc01c71: ('two_buttons_for_free_look', structs.decode_BIG_bool_),
    0x1c30f1a6: ('fixed_vertical_aim', structs.decode_BIG_bool_),
    0xda97bbcd: ('auto_aim_requires_orbit', structs.decode_BIG_bool_),
    0x83583abd: ('orbit_around_enemies', structs.decode_BIG_bool_),
    0xc224d966: ('aim_when_orbiting_point', structs.decode_BIG_bool_),
    0x1fcfaf3f: ('aim_during_free_look', structs.decode_BIG_bool_),
    0x3fb16819: ('aim_at_orbit_point', structs.decode_BIG_bool_),
    0x4fcf4b70: ('free_look_fades_gun', structs.decode_BIG_bool_),
    0x07bb06a6: ('orbit_point_fixed_offset', structs.decode_BIG_bool_),
    0x04d8d57b: ('gun_button_toggles_holster', structs.decode_BIG_bool_),
    0x5282c47e: ('gun_not_firing_holsters_gun', structs.decode_BIG_bool_),
    0x7304dafa: ('falling_double_jump', structs.decode_BIG_bool_),
    0x7a49267d: ('impulse_double_jump', structs.decode_BIG_bool_),
    0xa796a8b9: ('firing_cancels_camera_pitch', structs.decode_BIG_bool_),
    0x7c0599c8: ('assisted_aiming_ignore_horizontal', structs.decode_BIG_bool_),
    0x522ab1ac: ('assisted_aiming_ignore_vertical', structs.decode_BIG_bool_),
}
