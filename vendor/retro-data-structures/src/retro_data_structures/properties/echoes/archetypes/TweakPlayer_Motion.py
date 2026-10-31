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
    class TweakPlayer_MotionJson(typing_extensions.TypedDict):
        forward_accel_normal: float
        forward_accel_air: float
        forward_accel_ice: float
        forward_accel_organic: float
        forward_accel_water: float
        forward_accel_lava: float
        forward_accel_phazon: float
        forward_accel_shrubbery: float
        rotational_accel_normal: float
        rotational_accel_air: float
        rotational_accel_ice: float
        rotational_accel_organic: float
        rotational_accel_water: float
        rotational_accel_lava: float
        rotational_accel_phazon: float
        rotational_accel_shrubbery: float
        movement_friction_normal: float
        movement_friction_air: float
        movement_friction_ice: float
        movement_friction_organic: float
        movement_friction_water: float
        movement_friction_lava: float
        movement_friction_phazon: float
        movement_friction_shrubbery: float
        rotation_friction_normal: float
        rotation_friction_air: float
        rotation_friction_ice: float
        rotation_friction_organic: float
        rotation_friction_water: float
        rotation_friction_lava: float
        rotation_friction_phazon: float
        rotation_friction_shrubbery: float
        rotation_max_speed_normal: float
        rotation_max_speed_air: float
        rotation_max_speed_ice: float
        rotation_max_speed_organic: float
        rotation_max_speed_water: float
        rotation_max_speed_lava: float
        rotation_max_speed_phazon: float
        rotation_max_speed_shrubbery: float
        forward_max_speed_normal: float
        forward_max_speed_air: float
        forward_max_speed_ice: float
        forward_max_speed_organic: float
        forward_max_speed_water: float
        forward_max_speed_lava: float
        forward_max_speed_phazon: float
        forward_max_speed_shrubbery: float
        gravitational_accel: float
        fluid_gravitational_accel: float
        vertical_jump_accel: float
        horizontal_jump_accel: float
        vertical_double_jump_accel: float
        horizontal_double_jump_accel: float
        water_jump_factor: float
        water_ball_jump_factor: float
        lava_jump_factor: float
        lava_ball_jump_factor: float
        phazon_jump_factor: float
        phazon_ball_jump_factor: float
        allowed_jump_time: float
        allowed_double_jump_time: float
        min_double_jump_window: float
        max_double_jump_window: float
        allowed_jump_boot_time: float
        min_jump_time: float
        min_double_jump_time: float
        ledge_fall_time: float
        double_jump_impulse: float
        backwards_force_multiplier: float
        bomb_jump_height: float
        bomb_jump_radius: float
        gravity_boost_time: float
        gravity_boost_force: float
        gravity_boost_cancel_dampening: float
        gravity_boost_multiple_allowed: bool
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0x18d0b2da, 0x84f61ac5, 0xedb06c1d, 0x56f9f2af, 0xd05b643f, 0x122ce118, 0xf848dabe, 0x68ac6028, 0xcd4ee9fc, 0x3c461db2, 0x55006b6a, 0x8421e909, 0x2e41a61d, 0xdcf5b580, 0x2dd68198, 0x1a946073, 0xd4a25028, 0x2b5cb136, 0x421ac7ee, 0x586137d, 0xaece038b, 0x3637e815, 0x343a384c, 0xcaf4624, 0x34b2c148, 0xb917ae8a, 0xd051d852, 0x48d462b4, 0x6bb67d81, 0xf4725cad, 0xd42aa92c, 0x319526db, 0x4b6eb6ca, 0xc107f3db, 0xa8418503, 0x4b1d5ccf, 0xddcc44cd, 0xe8662d92, 0xabf6deae, 0x3c3f9884, 0xffd4a030, 0x59dfbcb9, 0x3099ca61, 0x16c1fddb, 0x6c648931, 0x4b42f5a9, 0x1f4cc854, 0xb3408173, 0x14b78aaf, 0x2c7620d3, 0xc2c91f7, 0x938c77d4, 0x13c95dfd, 0x8e41fed2, 0xb261fa30, 0x6ae560e9, 0x3149633, 0xd7b3f3ea, 0xaf1450a2, 0x980d701a, 0xa805feae, 0x233e3199, 0x97f30b95, 0x4c4c5872, 0x9bb73a0b, 0x4c8d664c, 0x1fc20169, 0xe7a5d759, 0x7044b295, 0xd82380a6, 0x2a2e4100, 0x905545e6, 0x229460be, 0xe238fd3, 0xdc92a0ac, 0xe1fefd3c)


@dataclasses.dataclass()
class TweakPlayer_Motion(BaseProperty):
    forward_accel_normal: float = dataclasses.field(default=35000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x18d0b2da, original_name='ForwardAccelNormal'
        ),
    })
    forward_accel_air: float = dataclasses.field(default=8000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x84f61ac5, original_name='ForwardAccelAir'
        ),
    })
    forward_accel_ice: float = dataclasses.field(default=35000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xedb06c1d, original_name='ForwardAccelIce'
        ),
    })
    forward_accel_organic: float = dataclasses.field(default=35000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x56f9f2af, original_name='ForwardAccelOrganic'
        ),
    })
    forward_accel_water: float = dataclasses.field(default=20000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd05b643f, original_name='ForwardAccelWater'
        ),
    })
    forward_accel_lava: float = dataclasses.field(default=20000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x122ce118, original_name='ForwardAccelLava'
        ),
    })
    forward_accel_phazon: float = dataclasses.field(default=20000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf848dabe, original_name='ForwardAccelPhazon'
        ),
    })
    forward_accel_shrubbery: float = dataclasses.field(default=20000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x68ac6028, original_name='ForwardAccelShrubbery'
        ),
    })
    rotational_accel_normal: float = dataclasses.field(default=14000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcd4ee9fc, original_name='RotationalAccelNormal'
        ),
    })
    rotational_accel_air: float = dataclasses.field(default=14000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3c461db2, original_name='RotationalAccelAir'
        ),
    })
    rotational_accel_ice: float = dataclasses.field(default=14000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x55006b6a, original_name='RotationalAccelIce'
        ),
    })
    rotational_accel_organic: float = dataclasses.field(default=14000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8421e909, original_name='RotationalAccelOrganic'
        ),
    })
    rotational_accel_water: float = dataclasses.field(default=14000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2e41a61d, original_name='RotationalAccelWater'
        ),
    })
    rotational_accel_lava: float = dataclasses.field(default=14000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdcf5b580, original_name='RotationalAccelLava'
        ),
    })
    rotational_accel_phazon: float = dataclasses.field(default=14000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2dd68198, original_name='RotationalAccelPhazon'
        ),
    })
    rotational_accel_shrubbery: float = dataclasses.field(default=14000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1a946073, original_name='RotationalAccelShrubbery'
        ),
    })
    movement_friction_normal: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd4a25028, original_name='MovementFrictionNormal'
        ),
    })
    movement_friction_air: float = dataclasses.field(default=0.75, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2b5cb136, original_name='MovementFrictionAir'
        ),
    })
    movement_friction_ice: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x421ac7ee, original_name='MovementFrictionIce'
        ),
    })
    movement_friction_organic: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0586137d, original_name='MovementFrictionOrganic'
        ),
    })
    movement_friction_water: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xaece038b, original_name='MovementFrictionWater'
        ),
    })
    movement_friction_lava: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3637e815, original_name='MovementFrictionLava'
        ),
    })
    movement_friction_phazon: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x343a384c, original_name='MovementFrictionPhazon'
        ),
    })
    movement_friction_shrubbery: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0caf4624, original_name='MovementFrictionShrubbery'
        ),
    })
    rotation_friction_normal: float = dataclasses.field(default=0.44999998807907104, metadata={
        'reflection': FieldReflection[float](
            float, id=0x34b2c148, original_name='RotationFrictionNormal'
        ),
    })
    rotation_friction_air: float = dataclasses.field(default=0.44999998807907104, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb917ae8a, original_name='RotationFrictionAir'
        ),
    })
    rotation_friction_ice: float = dataclasses.field(default=0.44999998807907104, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd051d852, original_name='RotationFrictionIce'
        ),
    })
    rotation_friction_organic: float = dataclasses.field(default=0.44999998807907104, metadata={
        'reflection': FieldReflection[float](
            float, id=0x48d462b4, original_name='RotationFrictionOrganic'
        ),
    })
    rotation_friction_water: float = dataclasses.field(default=0.44999998807907104, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6bb67d81, original_name='RotationFrictionWater'
        ),
    })
    rotation_friction_lava: float = dataclasses.field(default=0.44999998807907104, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf4725cad, original_name='RotationFrictionLava'
        ),
    })
    rotation_friction_phazon: float = dataclasses.field(default=0.44999998807907104, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd42aa92c, original_name='RotationFrictionPhazon'
        ),
    })
    rotation_friction_shrubbery: float = dataclasses.field(default=0.44999998807907104, metadata={
        'reflection': FieldReflection[float](
            float, id=0x319526db, original_name='RotationFrictionShrubbery'
        ),
    })
    rotation_max_speed_normal: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4b6eb6ca, original_name='RotationMaxSpeedNormal'
        ),
    })
    rotation_max_speed_air: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc107f3db, original_name='RotationMaxSpeedAir'
        ),
    })
    rotation_max_speed_ice: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa8418503, original_name='RotationMaxSpeedIce'
        ),
    })
    rotation_max_speed_organic: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4b1d5ccf, original_name='RotationMaxSpeedOrganic'
        ),
    })
    rotation_max_speed_water: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xddcc44cd, original_name='RotationMaxSpeedWater'
        ),
    })
    rotation_max_speed_lava: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe8662d92, original_name='RotationMaxSpeedLava'
        ),
    })
    rotation_max_speed_phazon: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xabf6deae, original_name='RotationMaxSpeedPhazon'
        ),
    })
    rotation_max_speed_shrubbery: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3c3f9884, original_name='RotationMaxSpeedShrubbery'
        ),
    })
    forward_max_speed_normal: float = dataclasses.field(default=16.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xffd4a030, original_name='ForwardMaxSpeedNormal'
        ),
    })
    forward_max_speed_air: float = dataclasses.field(default=16.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x59dfbcb9, original_name='ForwardMaxSpeedAir'
        ),
    })
    forward_max_speed_ice: float = dataclasses.field(default=16.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3099ca61, original_name='ForwardMaxSpeedIce'
        ),
    })
    forward_max_speed_organic: float = dataclasses.field(default=16.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x16c1fddb, original_name='ForwardMaxSpeedOrganic'
        ),
    })
    forward_max_speed_water: float = dataclasses.field(default=12.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6c648931, original_name='ForwardMaxSpeedWater'
        ),
    })
    forward_max_speed_lava: float = dataclasses.field(default=12.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4b42f5a9, original_name='ForwardMaxSpeedLava'
        ),
    })
    forward_max_speed_phazon: float = dataclasses.field(default=12.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1f4cc854, original_name='ForwardMaxSpeedPhazon'
        ),
    })
    forward_max_speed_shrubbery: float = dataclasses.field(default=12.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb3408173, original_name='ForwardMaxSpeedShrubbery'
        ),
    })
    gravitational_accel: float = dataclasses.field(default=-35.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x14b78aaf, original_name='GravitationalAccel'
        ),
    })
    fluid_gravitational_accel: float = dataclasses.field(default=-10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2c7620d3, original_name='FluidGravitationalAccel'
        ),
    })
    vertical_jump_accel: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0c2c91f7, original_name='VerticalJumpAccel'
        ),
    })
    horizontal_jump_accel: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x938c77d4, original_name='HorizontalJumpAccel'
        ),
    })
    vertical_double_jump_accel: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x13c95dfd, original_name='VerticalDoubleJumpAccel'
        ),
    })
    horizontal_double_jump_accel: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8e41fed2, original_name='HorizontalDoubleJumpAccel'
        ),
    })
    water_jump_factor: float = dataclasses.field(default=0.3700000047683716, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb261fa30, original_name='WaterJumpFactor'
        ),
    })
    water_ball_jump_factor: float = dataclasses.field(default=0.3700000047683716, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6ae560e9, original_name='WaterBallJumpFactor'
        ),
    })
    lava_jump_factor: float = dataclasses.field(default=0.3700000047683716, metadata={
        'reflection': FieldReflection[float](
            float, id=0x03149633, original_name='LavaJumpFactor'
        ),
    })
    lava_ball_jump_factor: float = dataclasses.field(default=0.3700000047683716, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd7b3f3ea, original_name='LavaBallJumpFactor'
        ),
    })
    phazon_jump_factor: float = dataclasses.field(default=0.3700000047683716, metadata={
        'reflection': FieldReflection[float](
            float, id=0xaf1450a2, original_name='PhazonJumpFactor'
        ),
    })
    phazon_ball_jump_factor: float = dataclasses.field(default=0.3700000047683716, metadata={
        'reflection': FieldReflection[float](
            float, id=0x980d701a, original_name='PhazonBallJumpFactor'
        ),
    })
    allowed_jump_time: float = dataclasses.field(default=0.24950000643730164, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa805feae, original_name='AllowedJumpTime'
        ),
    })
    allowed_double_jump_time: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x233e3199, original_name='AllowedDoubleJumpTime'
        ),
    })
    min_double_jump_window: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x97f30b95, original_name='MinDoubleJumpWindow'
        ),
    })
    max_double_jump_window: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4c4c5872, original_name='MaxDoubleJumpWindow'
        ),
    })
    allowed_jump_boot_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9bb73a0b, original_name='AllowedJumpBootTime'
        ),
    })
    min_jump_time: float = dataclasses.field(default=0.23499999940395355, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4c8d664c, original_name='MinJumpTime'
        ),
    })
    min_double_jump_time: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1fc20169, original_name='MinDoubleJumpTime'
        ),
    })
    ledge_fall_time: float = dataclasses.field(default=0.05000000074505806, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe7a5d759, original_name='LedgeFallTime'
        ),
    })
    double_jump_impulse: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7044b295, original_name='DoubleJumpImpulse'
        ),
    })
    backwards_force_multiplier: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd82380a6, original_name='BackwardsForceMultiplier'
        ),
    })
    bomb_jump_height: float = dataclasses.field(default=7.900000095367432, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2a2e4100, original_name='BombJumpHeight'
        ),
    })
    bomb_jump_radius: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x905545e6, original_name='BombJumpRadius'
        ),
    })
    gravity_boost_time: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x229460be, original_name='GravityBoostTime'
        ),
    })
    gravity_boost_force: float = dataclasses.field(default=9000.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0e238fd3, original_name='GravityBoostForce'
        ),
    })
    gravity_boost_cancel_dampening: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdc92a0ac, original_name='GravityBoostCancelDampening'
        ),
    })
    gravity_boost_multiple_allowed: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xe1fefd3c, original_name='GravityBoostMultipleAllowed'
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
        if property_count != 76:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLHfLH?')
    
        dec = _FAST_FORMAT.unpack(data.read(757))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24], dec[27], dec[30], dec[33], dec[36], dec[39], dec[42], dec[45], dec[48], dec[51], dec[54], dec[57], dec[60], dec[63], dec[66], dec[69], dec[72], dec[75], dec[78], dec[81], dec[84], dec[87], dec[90], dec[93], dec[96], dec[99], dec[102], dec[105], dec[108], dec[111], dec[114], dec[117], dec[120], dec[123], dec[126], dec[129], dec[132], dec[135], dec[138], dec[141], dec[144], dec[147], dec[150], dec[153], dec[156], dec[159], dec[162], dec[165], dec[168], dec[171], dec[174], dec[177], dec[180], dec[183], dec[186], dec[189], dec[192], dec[195], dec[198], dec[201], dec[204], dec[207], dec[210], dec[213], dec[216], dec[219], dec[222], dec[225]) == _FAST_IDS
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
            dec[65],
            dec[68],
            dec[71],
            dec[74],
            dec[77],
            dec[80],
            dec[83],
            dec[86],
            dec[89],
            dec[92],
            dec[95],
            dec[98],
            dec[101],
            dec[104],
            dec[107],
            dec[110],
            dec[113],
            dec[116],
            dec[119],
            dec[122],
            dec[125],
            dec[128],
            dec[131],
            dec[134],
            dec[137],
            dec[140],
            dec[143],
            dec[146],
            dec[149],
            dec[152],
            dec[155],
            dec[158],
            dec[161],
            dec[164],
            dec[167],
            dec[170],
            dec[173],
            dec[176],
            dec[179],
            dec[182],
            dec[185],
            dec[188],
            dec[191],
            dec[194],
            dec[197],
            dec[200],
            dec[203],
            dec[206],
            dec[209],
            dec[212],
            dec[215],
            dec[218],
            dec[221],
            dec[224],
            dec[227],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00L')  # 76 properties

        data.write(b'\x18\xd0\xb2\xda')  # 0x18d0b2da
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.forward_accel_normal))

        data.write(b'\x84\xf6\x1a\xc5')  # 0x84f61ac5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.forward_accel_air))

        data.write(b'\xed\xb0l\x1d')  # 0xedb06c1d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.forward_accel_ice))

        data.write(b'V\xf9\xf2\xaf')  # 0x56f9f2af
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.forward_accel_organic))

        data.write(b'\xd0[d?')  # 0xd05b643f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.forward_accel_water))

        data.write(b'\x12,\xe1\x18')  # 0x122ce118
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.forward_accel_lava))

        data.write(b'\xf8H\xda\xbe')  # 0xf848dabe
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.forward_accel_phazon))

        data.write(b'h\xac`(')  # 0x68ac6028
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.forward_accel_shrubbery))

        data.write(b'\xcdN\xe9\xfc')  # 0xcd4ee9fc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotational_accel_normal))

        data.write(b'<F\x1d\xb2')  # 0x3c461db2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotational_accel_air))

        data.write(b'U\x00kj')  # 0x55006b6a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotational_accel_ice))

        data.write(b'\x84!\xe9\t')  # 0x8421e909
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotational_accel_organic))

        data.write(b'.A\xa6\x1d')  # 0x2e41a61d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotational_accel_water))

        data.write(b'\xdc\xf5\xb5\x80')  # 0xdcf5b580
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotational_accel_lava))

        data.write(b'-\xd6\x81\x98')  # 0x2dd68198
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotational_accel_phazon))

        data.write(b'\x1a\x94`s')  # 0x1a946073
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotational_accel_shrubbery))

        data.write(b'\xd4\xa2P(')  # 0xd4a25028
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.movement_friction_normal))

        data.write(b'+\\\xb16')  # 0x2b5cb136
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.movement_friction_air))

        data.write(b'B\x1a\xc7\xee')  # 0x421ac7ee
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.movement_friction_ice))

        data.write(b'\x05\x86\x13}')  # 0x586137d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.movement_friction_organic))

        data.write(b'\xae\xce\x03\x8b')  # 0xaece038b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.movement_friction_water))

        data.write(b'67\xe8\x15')  # 0x3637e815
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.movement_friction_lava))

        data.write(b'4:8L')  # 0x343a384c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.movement_friction_phazon))

        data.write(b'\x0c\xafF$')  # 0xcaf4624
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.movement_friction_shrubbery))

        data.write(b'4\xb2\xc1H')  # 0x34b2c148
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotation_friction_normal))

        data.write(b'\xb9\x17\xae\x8a')  # 0xb917ae8a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotation_friction_air))

        data.write(b'\xd0Q\xd8R')  # 0xd051d852
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotation_friction_ice))

        data.write(b'H\xd4b\xb4')  # 0x48d462b4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotation_friction_organic))

        data.write(b'k\xb6}\x81')  # 0x6bb67d81
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotation_friction_water))

        data.write(b'\xf4r\\\xad')  # 0xf4725cad
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotation_friction_lava))

        data.write(b'\xd4*\xa9,')  # 0xd42aa92c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotation_friction_phazon))

        data.write(b'1\x95&\xdb')  # 0x319526db
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotation_friction_shrubbery))

        data.write(b'Kn\xb6\xca')  # 0x4b6eb6ca
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotation_max_speed_normal))

        data.write(b'\xc1\x07\xf3\xdb')  # 0xc107f3db
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotation_max_speed_air))

        data.write(b'\xa8A\x85\x03')  # 0xa8418503
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotation_max_speed_ice))

        data.write(b'K\x1d\\\xcf')  # 0x4b1d5ccf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotation_max_speed_organic))

        data.write(b'\xdd\xccD\xcd')  # 0xddcc44cd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotation_max_speed_water))

        data.write(b'\xe8f-\x92')  # 0xe8662d92
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotation_max_speed_lava))

        data.write(b'\xab\xf6\xde\xae')  # 0xabf6deae
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotation_max_speed_phazon))

        data.write(b'<?\x98\x84')  # 0x3c3f9884
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotation_max_speed_shrubbery))

        data.write(b'\xff\xd4\xa00')  # 0xffd4a030
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_normal))

        data.write(b'Y\xdf\xbc\xb9')  # 0x59dfbcb9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_air))

        data.write(b'0\x99\xcaa')  # 0x3099ca61
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_ice))

        data.write(b'\x16\xc1\xfd\xdb')  # 0x16c1fddb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_organic))

        data.write(b'ld\x891')  # 0x6c648931
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_water))

        data.write(b'KB\xf5\xa9')  # 0x4b42f5a9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_lava))

        data.write(b'\x1fL\xc8T')  # 0x1f4cc854
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_phazon))

        data.write(b'\xb3@\x81s')  # 0xb3408173
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.forward_max_speed_shrubbery))

        data.write(b'\x14\xb7\x8a\xaf')  # 0x14b78aaf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.gravitational_accel))

        data.write(b',v \xd3')  # 0x2c7620d3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fluid_gravitational_accel))

        data.write(b'\x0c,\x91\xf7')  # 0xc2c91f7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.vertical_jump_accel))

        data.write(b'\x93\x8cw\xd4')  # 0x938c77d4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.horizontal_jump_accel))

        data.write(b'\x13\xc9]\xfd')  # 0x13c95dfd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.vertical_double_jump_accel))

        data.write(b'\x8eA\xfe\xd2')  # 0x8e41fed2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.horizontal_double_jump_accel))

        data.write(b'\xb2a\xfa0')  # 0xb261fa30
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.water_jump_factor))

        data.write(b'j\xe5`\xe9')  # 0x6ae560e9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.water_ball_jump_factor))

        data.write(b'\x03\x14\x963')  # 0x3149633
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.lava_jump_factor))

        data.write(b'\xd7\xb3\xf3\xea')  # 0xd7b3f3ea
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.lava_ball_jump_factor))

        data.write(b'\xaf\x14P\xa2')  # 0xaf1450a2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_jump_factor))

        data.write(b'\x98\rp\x1a')  # 0x980d701a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_ball_jump_factor))

        data.write(b'\xa8\x05\xfe\xae')  # 0xa805feae
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.allowed_jump_time))

        data.write(b'#>1\x99')  # 0x233e3199
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.allowed_double_jump_time))

        data.write(b'\x97\xf3\x0b\x95')  # 0x97f30b95
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_double_jump_window))

        data.write(b'LLXr')  # 0x4c4c5872
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_double_jump_window))

        data.write(b'\x9b\xb7:\x0b')  # 0x9bb73a0b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.allowed_jump_boot_time))

        data.write(b'L\x8dfL')  # 0x4c8d664c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_jump_time))

        data.write(b'\x1f\xc2\x01i')  # 0x1fc20169
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_double_jump_time))

        data.write(b'\xe7\xa5\xd7Y')  # 0xe7a5d759
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ledge_fall_time))

        data.write(b'pD\xb2\x95')  # 0x7044b295
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.double_jump_impulse))

        data.write(b'\xd8#\x80\xa6')  # 0xd82380a6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.backwards_force_multiplier))

        data.write(b'*.A\x00')  # 0x2a2e4100
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.bomb_jump_height))

        data.write(b'\x90UE\xe6')  # 0x905545e6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.bomb_jump_radius))

        data.write(b'"\x94`\xbe')  # 0x229460be
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.gravity_boost_time))

        data.write(b'\x0e#\x8f\xd3')  # 0xe238fd3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.gravity_boost_force))

        data.write(b'\xdc\x92\xa0\xac')  # 0xdc92a0ac
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.gravity_boost_cancel_dampening))

        data.write(b'\xe1\xfe\xfd<')  # 0xe1fefd3c
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.gravity_boost_multiple_allowed))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayer_MotionJson", data)
        return cls(
            forward_accel_normal=json_data['forward_accel_normal'],
            forward_accel_air=json_data['forward_accel_air'],
            forward_accel_ice=json_data['forward_accel_ice'],
            forward_accel_organic=json_data['forward_accel_organic'],
            forward_accel_water=json_data['forward_accel_water'],
            forward_accel_lava=json_data['forward_accel_lava'],
            forward_accel_phazon=json_data['forward_accel_phazon'],
            forward_accel_shrubbery=json_data['forward_accel_shrubbery'],
            rotational_accel_normal=json_data['rotational_accel_normal'],
            rotational_accel_air=json_data['rotational_accel_air'],
            rotational_accel_ice=json_data['rotational_accel_ice'],
            rotational_accel_organic=json_data['rotational_accel_organic'],
            rotational_accel_water=json_data['rotational_accel_water'],
            rotational_accel_lava=json_data['rotational_accel_lava'],
            rotational_accel_phazon=json_data['rotational_accel_phazon'],
            rotational_accel_shrubbery=json_data['rotational_accel_shrubbery'],
            movement_friction_normal=json_data['movement_friction_normal'],
            movement_friction_air=json_data['movement_friction_air'],
            movement_friction_ice=json_data['movement_friction_ice'],
            movement_friction_organic=json_data['movement_friction_organic'],
            movement_friction_water=json_data['movement_friction_water'],
            movement_friction_lava=json_data['movement_friction_lava'],
            movement_friction_phazon=json_data['movement_friction_phazon'],
            movement_friction_shrubbery=json_data['movement_friction_shrubbery'],
            rotation_friction_normal=json_data['rotation_friction_normal'],
            rotation_friction_air=json_data['rotation_friction_air'],
            rotation_friction_ice=json_data['rotation_friction_ice'],
            rotation_friction_organic=json_data['rotation_friction_organic'],
            rotation_friction_water=json_data['rotation_friction_water'],
            rotation_friction_lava=json_data['rotation_friction_lava'],
            rotation_friction_phazon=json_data['rotation_friction_phazon'],
            rotation_friction_shrubbery=json_data['rotation_friction_shrubbery'],
            rotation_max_speed_normal=json_data['rotation_max_speed_normal'],
            rotation_max_speed_air=json_data['rotation_max_speed_air'],
            rotation_max_speed_ice=json_data['rotation_max_speed_ice'],
            rotation_max_speed_organic=json_data['rotation_max_speed_organic'],
            rotation_max_speed_water=json_data['rotation_max_speed_water'],
            rotation_max_speed_lava=json_data['rotation_max_speed_lava'],
            rotation_max_speed_phazon=json_data['rotation_max_speed_phazon'],
            rotation_max_speed_shrubbery=json_data['rotation_max_speed_shrubbery'],
            forward_max_speed_normal=json_data['forward_max_speed_normal'],
            forward_max_speed_air=json_data['forward_max_speed_air'],
            forward_max_speed_ice=json_data['forward_max_speed_ice'],
            forward_max_speed_organic=json_data['forward_max_speed_organic'],
            forward_max_speed_water=json_data['forward_max_speed_water'],
            forward_max_speed_lava=json_data['forward_max_speed_lava'],
            forward_max_speed_phazon=json_data['forward_max_speed_phazon'],
            forward_max_speed_shrubbery=json_data['forward_max_speed_shrubbery'],
            gravitational_accel=json_data['gravitational_accel'],
            fluid_gravitational_accel=json_data['fluid_gravitational_accel'],
            vertical_jump_accel=json_data['vertical_jump_accel'],
            horizontal_jump_accel=json_data['horizontal_jump_accel'],
            vertical_double_jump_accel=json_data['vertical_double_jump_accel'],
            horizontal_double_jump_accel=json_data['horizontal_double_jump_accel'],
            water_jump_factor=json_data['water_jump_factor'],
            water_ball_jump_factor=json_data['water_ball_jump_factor'],
            lava_jump_factor=json_data['lava_jump_factor'],
            lava_ball_jump_factor=json_data['lava_ball_jump_factor'],
            phazon_jump_factor=json_data['phazon_jump_factor'],
            phazon_ball_jump_factor=json_data['phazon_ball_jump_factor'],
            allowed_jump_time=json_data['allowed_jump_time'],
            allowed_double_jump_time=json_data['allowed_double_jump_time'],
            min_double_jump_window=json_data['min_double_jump_window'],
            max_double_jump_window=json_data['max_double_jump_window'],
            allowed_jump_boot_time=json_data['allowed_jump_boot_time'],
            min_jump_time=json_data['min_jump_time'],
            min_double_jump_time=json_data['min_double_jump_time'],
            ledge_fall_time=json_data['ledge_fall_time'],
            double_jump_impulse=json_data['double_jump_impulse'],
            backwards_force_multiplier=json_data['backwards_force_multiplier'],
            bomb_jump_height=json_data['bomb_jump_height'],
            bomb_jump_radius=json_data['bomb_jump_radius'],
            gravity_boost_time=json_data['gravity_boost_time'],
            gravity_boost_force=json_data['gravity_boost_force'],
            gravity_boost_cancel_dampening=json_data['gravity_boost_cancel_dampening'],
            gravity_boost_multiple_allowed=json_data['gravity_boost_multiple_allowed'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'forward_accel_normal': self.forward_accel_normal,
            'forward_accel_air': self.forward_accel_air,
            'forward_accel_ice': self.forward_accel_ice,
            'forward_accel_organic': self.forward_accel_organic,
            'forward_accel_water': self.forward_accel_water,
            'forward_accel_lava': self.forward_accel_lava,
            'forward_accel_phazon': self.forward_accel_phazon,
            'forward_accel_shrubbery': self.forward_accel_shrubbery,
            'rotational_accel_normal': self.rotational_accel_normal,
            'rotational_accel_air': self.rotational_accel_air,
            'rotational_accel_ice': self.rotational_accel_ice,
            'rotational_accel_organic': self.rotational_accel_organic,
            'rotational_accel_water': self.rotational_accel_water,
            'rotational_accel_lava': self.rotational_accel_lava,
            'rotational_accel_phazon': self.rotational_accel_phazon,
            'rotational_accel_shrubbery': self.rotational_accel_shrubbery,
            'movement_friction_normal': self.movement_friction_normal,
            'movement_friction_air': self.movement_friction_air,
            'movement_friction_ice': self.movement_friction_ice,
            'movement_friction_organic': self.movement_friction_organic,
            'movement_friction_water': self.movement_friction_water,
            'movement_friction_lava': self.movement_friction_lava,
            'movement_friction_phazon': self.movement_friction_phazon,
            'movement_friction_shrubbery': self.movement_friction_shrubbery,
            'rotation_friction_normal': self.rotation_friction_normal,
            'rotation_friction_air': self.rotation_friction_air,
            'rotation_friction_ice': self.rotation_friction_ice,
            'rotation_friction_organic': self.rotation_friction_organic,
            'rotation_friction_water': self.rotation_friction_water,
            'rotation_friction_lava': self.rotation_friction_lava,
            'rotation_friction_phazon': self.rotation_friction_phazon,
            'rotation_friction_shrubbery': self.rotation_friction_shrubbery,
            'rotation_max_speed_normal': self.rotation_max_speed_normal,
            'rotation_max_speed_air': self.rotation_max_speed_air,
            'rotation_max_speed_ice': self.rotation_max_speed_ice,
            'rotation_max_speed_organic': self.rotation_max_speed_organic,
            'rotation_max_speed_water': self.rotation_max_speed_water,
            'rotation_max_speed_lava': self.rotation_max_speed_lava,
            'rotation_max_speed_phazon': self.rotation_max_speed_phazon,
            'rotation_max_speed_shrubbery': self.rotation_max_speed_shrubbery,
            'forward_max_speed_normal': self.forward_max_speed_normal,
            'forward_max_speed_air': self.forward_max_speed_air,
            'forward_max_speed_ice': self.forward_max_speed_ice,
            'forward_max_speed_organic': self.forward_max_speed_organic,
            'forward_max_speed_water': self.forward_max_speed_water,
            'forward_max_speed_lava': self.forward_max_speed_lava,
            'forward_max_speed_phazon': self.forward_max_speed_phazon,
            'forward_max_speed_shrubbery': self.forward_max_speed_shrubbery,
            'gravitational_accel': self.gravitational_accel,
            'fluid_gravitational_accel': self.fluid_gravitational_accel,
            'vertical_jump_accel': self.vertical_jump_accel,
            'horizontal_jump_accel': self.horizontal_jump_accel,
            'vertical_double_jump_accel': self.vertical_double_jump_accel,
            'horizontal_double_jump_accel': self.horizontal_double_jump_accel,
            'water_jump_factor': self.water_jump_factor,
            'water_ball_jump_factor': self.water_ball_jump_factor,
            'lava_jump_factor': self.lava_jump_factor,
            'lava_ball_jump_factor': self.lava_ball_jump_factor,
            'phazon_jump_factor': self.phazon_jump_factor,
            'phazon_ball_jump_factor': self.phazon_ball_jump_factor,
            'allowed_jump_time': self.allowed_jump_time,
            'allowed_double_jump_time': self.allowed_double_jump_time,
            'min_double_jump_window': self.min_double_jump_window,
            'max_double_jump_window': self.max_double_jump_window,
            'allowed_jump_boot_time': self.allowed_jump_boot_time,
            'min_jump_time': self.min_jump_time,
            'min_double_jump_time': self.min_double_jump_time,
            'ledge_fall_time': self.ledge_fall_time,
            'double_jump_impulse': self.double_jump_impulse,
            'backwards_force_multiplier': self.backwards_force_multiplier,
            'bomb_jump_height': self.bomb_jump_height,
            'bomb_jump_radius': self.bomb_jump_radius,
            'gravity_boost_time': self.gravity_boost_time,
            'gravity_boost_force': self.gravity_boost_force,
            'gravity_boost_cancel_dampening': self.gravity_boost_cancel_dampening,
            'gravity_boost_multiple_allowed': self.gravity_boost_multiple_allowed,
        }


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x18d0b2da: ('forward_accel_normal', structs.decode_BIG_f),
    0x84f61ac5: ('forward_accel_air', structs.decode_BIG_f),
    0xedb06c1d: ('forward_accel_ice', structs.decode_BIG_f),
    0x56f9f2af: ('forward_accel_organic', structs.decode_BIG_f),
    0xd05b643f: ('forward_accel_water', structs.decode_BIG_f),
    0x122ce118: ('forward_accel_lava', structs.decode_BIG_f),
    0xf848dabe: ('forward_accel_phazon', structs.decode_BIG_f),
    0x68ac6028: ('forward_accel_shrubbery', structs.decode_BIG_f),
    0xcd4ee9fc: ('rotational_accel_normal', structs.decode_BIG_f),
    0x3c461db2: ('rotational_accel_air', structs.decode_BIG_f),
    0x55006b6a: ('rotational_accel_ice', structs.decode_BIG_f),
    0x8421e909: ('rotational_accel_organic', structs.decode_BIG_f),
    0x2e41a61d: ('rotational_accel_water', structs.decode_BIG_f),
    0xdcf5b580: ('rotational_accel_lava', structs.decode_BIG_f),
    0x2dd68198: ('rotational_accel_phazon', structs.decode_BIG_f),
    0x1a946073: ('rotational_accel_shrubbery', structs.decode_BIG_f),
    0xd4a25028: ('movement_friction_normal', structs.decode_BIG_f),
    0x2b5cb136: ('movement_friction_air', structs.decode_BIG_f),
    0x421ac7ee: ('movement_friction_ice', structs.decode_BIG_f),
    0x0586137d: ('movement_friction_organic', structs.decode_BIG_f),
    0xaece038b: ('movement_friction_water', structs.decode_BIG_f),
    0x3637e815: ('movement_friction_lava', structs.decode_BIG_f),
    0x343a384c: ('movement_friction_phazon', structs.decode_BIG_f),
    0x0caf4624: ('movement_friction_shrubbery', structs.decode_BIG_f),
    0x34b2c148: ('rotation_friction_normal', structs.decode_BIG_f),
    0xb917ae8a: ('rotation_friction_air', structs.decode_BIG_f),
    0xd051d852: ('rotation_friction_ice', structs.decode_BIG_f),
    0x48d462b4: ('rotation_friction_organic', structs.decode_BIG_f),
    0x6bb67d81: ('rotation_friction_water', structs.decode_BIG_f),
    0xf4725cad: ('rotation_friction_lava', structs.decode_BIG_f),
    0xd42aa92c: ('rotation_friction_phazon', structs.decode_BIG_f),
    0x319526db: ('rotation_friction_shrubbery', structs.decode_BIG_f),
    0x4b6eb6ca: ('rotation_max_speed_normal', structs.decode_BIG_f),
    0xc107f3db: ('rotation_max_speed_air', structs.decode_BIG_f),
    0xa8418503: ('rotation_max_speed_ice', structs.decode_BIG_f),
    0x4b1d5ccf: ('rotation_max_speed_organic', structs.decode_BIG_f),
    0xddcc44cd: ('rotation_max_speed_water', structs.decode_BIG_f),
    0xe8662d92: ('rotation_max_speed_lava', structs.decode_BIG_f),
    0xabf6deae: ('rotation_max_speed_phazon', structs.decode_BIG_f),
    0x3c3f9884: ('rotation_max_speed_shrubbery', structs.decode_BIG_f),
    0xffd4a030: ('forward_max_speed_normal', structs.decode_BIG_f),
    0x59dfbcb9: ('forward_max_speed_air', structs.decode_BIG_f),
    0x3099ca61: ('forward_max_speed_ice', structs.decode_BIG_f),
    0x16c1fddb: ('forward_max_speed_organic', structs.decode_BIG_f),
    0x6c648931: ('forward_max_speed_water', structs.decode_BIG_f),
    0x4b42f5a9: ('forward_max_speed_lava', structs.decode_BIG_f),
    0x1f4cc854: ('forward_max_speed_phazon', structs.decode_BIG_f),
    0xb3408173: ('forward_max_speed_shrubbery', structs.decode_BIG_f),
    0x14b78aaf: ('gravitational_accel', structs.decode_BIG_f),
    0x2c7620d3: ('fluid_gravitational_accel', structs.decode_BIG_f),
    0x0c2c91f7: ('vertical_jump_accel', structs.decode_BIG_f),
    0x938c77d4: ('horizontal_jump_accel', structs.decode_BIG_f),
    0x13c95dfd: ('vertical_double_jump_accel', structs.decode_BIG_f),
    0x8e41fed2: ('horizontal_double_jump_accel', structs.decode_BIG_f),
    0xb261fa30: ('water_jump_factor', structs.decode_BIG_f),
    0x6ae560e9: ('water_ball_jump_factor', structs.decode_BIG_f),
    0x03149633: ('lava_jump_factor', structs.decode_BIG_f),
    0xd7b3f3ea: ('lava_ball_jump_factor', structs.decode_BIG_f),
    0xaf1450a2: ('phazon_jump_factor', structs.decode_BIG_f),
    0x980d701a: ('phazon_ball_jump_factor', structs.decode_BIG_f),
    0xa805feae: ('allowed_jump_time', structs.decode_BIG_f),
    0x233e3199: ('allowed_double_jump_time', structs.decode_BIG_f),
    0x97f30b95: ('min_double_jump_window', structs.decode_BIG_f),
    0x4c4c5872: ('max_double_jump_window', structs.decode_BIG_f),
    0x9bb73a0b: ('allowed_jump_boot_time', structs.decode_BIG_f),
    0x4c8d664c: ('min_jump_time', structs.decode_BIG_f),
    0x1fc20169: ('min_double_jump_time', structs.decode_BIG_f),
    0xe7a5d759: ('ledge_fall_time', structs.decode_BIG_f),
    0x7044b295: ('double_jump_impulse', structs.decode_BIG_f),
    0xd82380a6: ('backwards_force_multiplier', structs.decode_BIG_f),
    0x2a2e4100: ('bomb_jump_height', structs.decode_BIG_f),
    0x905545e6: ('bomb_jump_radius', structs.decode_BIG_f),
    0x229460be: ('gravity_boost_time', structs.decode_BIG_f),
    0x0e238fd3: ('gravity_boost_force', structs.decode_BIG_f),
    0xdc92a0ac: ('gravity_boost_cancel_dampening', structs.decode_BIG_f),
    0xe1fefd3c: ('gravity_boost_multiple_allowed', structs.decode_BIG_bool_),
}
