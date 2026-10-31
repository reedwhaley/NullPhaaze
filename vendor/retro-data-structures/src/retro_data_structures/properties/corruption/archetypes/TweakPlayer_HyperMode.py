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
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    class TweakPlayer_HyperModeJson(typing_extensions.TypedDict):
        hyper_mode_invulnerable_phazon_loss: bool
        hyper_mode_invulnerable_time: float
        hyper_mode_corruption_time: float
        hyper_mode_constant_corruption_rate: bool
        hyper_mode_spline_corruption_rate: json_util.JsonObject
        hyper_mode_corruption_rate: float
        hyper_mode_phaaze_constant_corruption_rate: bool
        hyper_mode_phaaze_spline_corruption_rate: json_util.JsonObject
        hyper_mode_phaaze_corruption_rate: float
        hyper_mode_phaaze_boss_corruption_rate: float
        hyper_mode_phazon_level: float
        hyper_mode_phazon_capacity: float
        hyper_mode_danger_percentage: float
        hyper_mode_beam_loss_amount: float
        hyper_mode_charged_beam_loss_amount: float
        hyper_mode_missile_loss_amount: float
        hyper_mode_phazon_ball_rate: float
        hyper_mode_damage_multiplier: float
        hyper_mode_charged_rate_scale: float
        hyper_mode_aggro_alert1: float
        hyper_mode_aggro_alert2: float
        hyper_mode_aggro_alert3: float
        hyper_mode_aggro_alert4: float
        hyper_mode_aggro_duration: float
        hyper_mode_aggro_warning: float
        hyper_mode_initial_damage: json_util.JsonObject
        hyper_mode_damage: json_util.JsonObject
        hyper_mode_phaaze_damage: json_util.JsonObject
        hyper_mode_critical_time: float
        hyper_mode_critical_time_tutorial: float
        hyper_mode_critical_clear: float
        hyper_mode_venting_control: json_util.JsonObject
    

@dataclasses.dataclass()
class TweakPlayer_HyperMode(BaseProperty):
    hyper_mode_invulnerable_phazon_loss: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x31ffbfe7, original_name='HyperModeInvulnerablePhazonLoss'
        ),
    })
    hyper_mode_invulnerable_time: float = dataclasses.field(default=7.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7fdfaa62, original_name='HyperModeInvulnerableTime'
        ),
    })
    hyper_mode_corruption_time: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1a75c2d0, original_name='HyperModeCorruptionTime'
        ),
    })
    hyper_mode_constant_corruption_rate: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xfb9972fc, original_name='HyperModeConstantCorruptionRate'
        ),
    })
    hyper_mode_spline_corruption_rate: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x699dff41, original_name='HyperModeSplineCorruptionRate', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    hyper_mode_corruption_rate: float = dataclasses.field(default=14.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x48cc79f2, original_name='HyperModeCorruptionRate'
        ),
    })
    hyper_mode_phaaze_constant_corruption_rate: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x128e6ecc, original_name='HyperModePhaazeConstantCorruptionRate'
        ),
    })
    hyper_mode_phaaze_spline_corruption_rate: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x808ae371, original_name='HyperModePhaazeSplineCorruptionRate', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    hyper_mode_phaaze_corruption_rate: float = dataclasses.field(default=14.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfd4c4fee, original_name='HyperModePhaazeCorruptionRate'
        ),
    })
    hyper_mode_phaaze_boss_corruption_rate: float = dataclasses.field(default=14.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x23c70cb5, original_name='HyperModePhaazeBossCorruptionRate'
        ),
    })
    hyper_mode_phazon_level: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xab40bed3, original_name='HyperModePhazonLevel'
        ),
    })
    hyper_mode_phazon_capacity: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8ed2e3fb, original_name='HyperModePhazonCapacity'
        ),
    })
    hyper_mode_danger_percentage: float = dataclasses.field(default=70.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa2482028, original_name='HyperModeDangerPercentage'
        ),
    })
    hyper_mode_beam_loss_amount: float = dataclasses.field(default=5.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa3748fa1, original_name='HyperModeBeamLossAmount'
        ),
    })
    hyper_mode_charged_beam_loss_amount: float = dataclasses.field(default=0.800000011920929, metadata={
        'reflection': FieldReflection[float](
            float, id=0x16bc1c24, original_name='HyperModeChargedBeamLossAmount'
        ),
    })
    hyper_mode_missile_loss_amount: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xedff39f1, original_name='HyperModeMissileLossAmount'
        ),
    })
    hyper_mode_phazon_ball_rate: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9cedea06, original_name='HyperModePhazonBallRate'
        ),
    })
    hyper_mode_damage_multiplier: float = dataclasses.field(default=0.30000001192092896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x56f3c854, original_name='HyperModeDamageMultiplier'
        ),
    })
    hyper_mode_charged_rate_scale: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdb1120f2, original_name='HyperModeChargedRateScale'
        ),
    })
    hyper_mode_aggro_alert1: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xba8cb0f2, original_name='HyperModeAggroAlert1'
        ),
    })
    hyper_mode_aggro_alert2: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3c18c25c, original_name='HyperModeAggroAlert2'
        ),
    })
    hyper_mode_aggro_alert3: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf74411f9, original_name='HyperModeAggroAlert3'
        ),
    })
    hyper_mode_aggro_alert4: float = dataclasses.field(default=80.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xea412141, original_name='HyperModeAggroAlert4'
        ),
    })
    hyper_mode_aggro_duration: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb03510b7, original_name='HyperModeAggroDuration'
        ),
    })
    hyper_mode_aggro_warning: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3f07961a, original_name='HyperModeAggroWarning'
        ),
    })
    hyper_mode_initial_damage: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x711296e2, original_name='HyperModeInitialDamage', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    hyper_mode_damage: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xb148913b, original_name='HyperModeDamage', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    hyper_mode_phaaze_damage: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xc5f1943d, original_name='HyperModePhaazeDamage', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    hyper_mode_critical_time: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2b6624b1, original_name='HyperModeCriticalTime'
        ),
    })
    hyper_mode_critical_time_tutorial: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xcd562633, original_name='HyperModeCriticalTimeTutorial'
        ),
    })
    hyper_mode_critical_clear: float = dataclasses.field(default=75.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbe038cbf, original_name='HyperModeCriticalClear'
        ),
    })
    hyper_mode_venting_control: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x0f35ee69, original_name='HyperModeVentingControl', from_json=Spline.from_json, to_json=Spline.to_json
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
        if property_count != 32:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x31ffbfe7
        hyper_mode_invulnerable_phazon_loss = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7fdfaa62
        hyper_mode_invulnerable_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1a75c2d0
        hyper_mode_corruption_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfb9972fc
        hyper_mode_constant_corruption_rate = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x699dff41
        hyper_mode_spline_corruption_rate = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x48cc79f2
        hyper_mode_corruption_rate = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x128e6ecc
        hyper_mode_phaaze_constant_corruption_rate = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x808ae371
        hyper_mode_phaaze_spline_corruption_rate = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfd4c4fee
        hyper_mode_phaaze_corruption_rate = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x23c70cb5
        hyper_mode_phaaze_boss_corruption_rate = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xab40bed3
        hyper_mode_phazon_level = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8ed2e3fb
        hyper_mode_phazon_capacity = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa2482028
        hyper_mode_danger_percentage = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa3748fa1
        hyper_mode_beam_loss_amount = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x16bc1c24
        hyper_mode_charged_beam_loss_amount = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xedff39f1
        hyper_mode_missile_loss_amount = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9cedea06
        hyper_mode_phazon_ball_rate = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x56f3c854
        hyper_mode_damage_multiplier = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdb1120f2
        hyper_mode_charged_rate_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xba8cb0f2
        hyper_mode_aggro_alert1 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3c18c25c
        hyper_mode_aggro_alert2 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf74411f9
        hyper_mode_aggro_alert3 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xea412141
        hyper_mode_aggro_alert4 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb03510b7
        hyper_mode_aggro_duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3f07961a
        hyper_mode_aggro_warning = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x711296e2
        hyper_mode_initial_damage = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb148913b
        hyper_mode_damage = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc5f1943d
        hyper_mode_phaaze_damage = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2b6624b1
        hyper_mode_critical_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcd562633
        hyper_mode_critical_time_tutorial = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbe038cbf
        hyper_mode_critical_clear = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0f35ee69
        hyper_mode_venting_control = Spline.from_stream(data, game, property_size)
    
        return cls(hyper_mode_invulnerable_phazon_loss, hyper_mode_invulnerable_time, hyper_mode_corruption_time, hyper_mode_constant_corruption_rate, hyper_mode_spline_corruption_rate, hyper_mode_corruption_rate, hyper_mode_phaaze_constant_corruption_rate, hyper_mode_phaaze_spline_corruption_rate, hyper_mode_phaaze_corruption_rate, hyper_mode_phaaze_boss_corruption_rate, hyper_mode_phazon_level, hyper_mode_phazon_capacity, hyper_mode_danger_percentage, hyper_mode_beam_loss_amount, hyper_mode_charged_beam_loss_amount, hyper_mode_missile_loss_amount, hyper_mode_phazon_ball_rate, hyper_mode_damage_multiplier, hyper_mode_charged_rate_scale, hyper_mode_aggro_alert1, hyper_mode_aggro_alert2, hyper_mode_aggro_alert3, hyper_mode_aggro_alert4, hyper_mode_aggro_duration, hyper_mode_aggro_warning, hyper_mode_initial_damage, hyper_mode_damage, hyper_mode_phaaze_damage, hyper_mode_critical_time, hyper_mode_critical_time_tutorial, hyper_mode_critical_clear, hyper_mode_venting_control)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00 ')  # 32 properties

        data.write(b'1\xff\xbf\xe7')  # 0x31ffbfe7
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.hyper_mode_invulnerable_phazon_loss))

        data.write(b'\x7f\xdf\xaab')  # 0x7fdfaa62
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_invulnerable_time))

        data.write(b'\x1au\xc2\xd0')  # 0x1a75c2d0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_corruption_time))

        data.write(b'\xfb\x99r\xfc')  # 0xfb9972fc
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.hyper_mode_constant_corruption_rate))

        data.write(b'i\x9d\xffA')  # 0x699dff41
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper_mode_spline_corruption_rate.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'H\xccy\xf2')  # 0x48cc79f2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_corruption_rate))

        data.write(b'\x12\x8en\xcc')  # 0x128e6ecc
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.hyper_mode_phaaze_constant_corruption_rate))

        data.write(b'\x80\x8a\xe3q')  # 0x808ae371
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper_mode_phaaze_spline_corruption_rate.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfdLO\xee')  # 0xfd4c4fee
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_phaaze_corruption_rate))

        data.write(b'#\xc7\x0c\xb5')  # 0x23c70cb5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_phaaze_boss_corruption_rate))

        data.write(b'\xab@\xbe\xd3')  # 0xab40bed3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_phazon_level))

        data.write(b'\x8e\xd2\xe3\xfb')  # 0x8ed2e3fb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_phazon_capacity))

        data.write(b'\xa2H (')  # 0xa2482028
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_danger_percentage))

        data.write(b'\xa3t\x8f\xa1')  # 0xa3748fa1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_beam_loss_amount))

        data.write(b'\x16\xbc\x1c$')  # 0x16bc1c24
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_charged_beam_loss_amount))

        data.write(b'\xed\xff9\xf1')  # 0xedff39f1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_missile_loss_amount))

        data.write(b'\x9c\xed\xea\x06')  # 0x9cedea06
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_phazon_ball_rate))

        data.write(b'V\xf3\xc8T')  # 0x56f3c854
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_damage_multiplier))

        data.write(b'\xdb\x11 \xf2')  # 0xdb1120f2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_charged_rate_scale))

        data.write(b'\xba\x8c\xb0\xf2')  # 0xba8cb0f2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_aggro_alert1))

        data.write(b'<\x18\xc2\\')  # 0x3c18c25c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_aggro_alert2))

        data.write(b'\xf7D\x11\xf9')  # 0xf74411f9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_aggro_alert3))

        data.write(b'\xeaA!A')  # 0xea412141
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_aggro_alert4))

        data.write(b'\xb05\x10\xb7')  # 0xb03510b7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_aggro_duration))

        data.write(b'?\x07\x96\x1a')  # 0x3f07961a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_aggro_warning))

        data.write(b'q\x12\x96\xe2')  # 0x711296e2
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper_mode_initial_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb1H\x91;')  # 0xb148913b
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper_mode_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc5\xf1\x94=')  # 0xc5f1943d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper_mode_phaaze_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'+f$\xb1')  # 0x2b6624b1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_critical_time))

        data.write(b'\xcdV&3')  # 0xcd562633
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_critical_time_tutorial))

        data.write(b'\xbe\x03\x8c\xbf')  # 0xbe038cbf
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.hyper_mode_critical_clear))

        data.write(b'\x0f5\xeei')  # 0xf35ee69
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper_mode_venting_control.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayer_HyperModeJson", data)
        return cls(
            hyper_mode_invulnerable_phazon_loss=json_data['hyper_mode_invulnerable_phazon_loss'],
            hyper_mode_invulnerable_time=json_data['hyper_mode_invulnerable_time'],
            hyper_mode_corruption_time=json_data['hyper_mode_corruption_time'],
            hyper_mode_constant_corruption_rate=json_data['hyper_mode_constant_corruption_rate'],
            hyper_mode_spline_corruption_rate=Spline.from_json(json_data['hyper_mode_spline_corruption_rate']),
            hyper_mode_corruption_rate=json_data['hyper_mode_corruption_rate'],
            hyper_mode_phaaze_constant_corruption_rate=json_data['hyper_mode_phaaze_constant_corruption_rate'],
            hyper_mode_phaaze_spline_corruption_rate=Spline.from_json(json_data['hyper_mode_phaaze_spline_corruption_rate']),
            hyper_mode_phaaze_corruption_rate=json_data['hyper_mode_phaaze_corruption_rate'],
            hyper_mode_phaaze_boss_corruption_rate=json_data['hyper_mode_phaaze_boss_corruption_rate'],
            hyper_mode_phazon_level=json_data['hyper_mode_phazon_level'],
            hyper_mode_phazon_capacity=json_data['hyper_mode_phazon_capacity'],
            hyper_mode_danger_percentage=json_data['hyper_mode_danger_percentage'],
            hyper_mode_beam_loss_amount=json_data['hyper_mode_beam_loss_amount'],
            hyper_mode_charged_beam_loss_amount=json_data['hyper_mode_charged_beam_loss_amount'],
            hyper_mode_missile_loss_amount=json_data['hyper_mode_missile_loss_amount'],
            hyper_mode_phazon_ball_rate=json_data['hyper_mode_phazon_ball_rate'],
            hyper_mode_damage_multiplier=json_data['hyper_mode_damage_multiplier'],
            hyper_mode_charged_rate_scale=json_data['hyper_mode_charged_rate_scale'],
            hyper_mode_aggro_alert1=json_data['hyper_mode_aggro_alert1'],
            hyper_mode_aggro_alert2=json_data['hyper_mode_aggro_alert2'],
            hyper_mode_aggro_alert3=json_data['hyper_mode_aggro_alert3'],
            hyper_mode_aggro_alert4=json_data['hyper_mode_aggro_alert4'],
            hyper_mode_aggro_duration=json_data['hyper_mode_aggro_duration'],
            hyper_mode_aggro_warning=json_data['hyper_mode_aggro_warning'],
            hyper_mode_initial_damage=DamageVulnerability.from_json(json_data['hyper_mode_initial_damage']),
            hyper_mode_damage=DamageVulnerability.from_json(json_data['hyper_mode_damage']),
            hyper_mode_phaaze_damage=DamageVulnerability.from_json(json_data['hyper_mode_phaaze_damage']),
            hyper_mode_critical_time=json_data['hyper_mode_critical_time'],
            hyper_mode_critical_time_tutorial=json_data['hyper_mode_critical_time_tutorial'],
            hyper_mode_critical_clear=json_data['hyper_mode_critical_clear'],
            hyper_mode_venting_control=Spline.from_json(json_data['hyper_mode_venting_control']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'hyper_mode_invulnerable_phazon_loss': self.hyper_mode_invulnerable_phazon_loss,
            'hyper_mode_invulnerable_time': self.hyper_mode_invulnerable_time,
            'hyper_mode_corruption_time': self.hyper_mode_corruption_time,
            'hyper_mode_constant_corruption_rate': self.hyper_mode_constant_corruption_rate,
            'hyper_mode_spline_corruption_rate': self.hyper_mode_spline_corruption_rate.to_json(),
            'hyper_mode_corruption_rate': self.hyper_mode_corruption_rate,
            'hyper_mode_phaaze_constant_corruption_rate': self.hyper_mode_phaaze_constant_corruption_rate,
            'hyper_mode_phaaze_spline_corruption_rate': self.hyper_mode_phaaze_spline_corruption_rate.to_json(),
            'hyper_mode_phaaze_corruption_rate': self.hyper_mode_phaaze_corruption_rate,
            'hyper_mode_phaaze_boss_corruption_rate': self.hyper_mode_phaaze_boss_corruption_rate,
            'hyper_mode_phazon_level': self.hyper_mode_phazon_level,
            'hyper_mode_phazon_capacity': self.hyper_mode_phazon_capacity,
            'hyper_mode_danger_percentage': self.hyper_mode_danger_percentage,
            'hyper_mode_beam_loss_amount': self.hyper_mode_beam_loss_amount,
            'hyper_mode_charged_beam_loss_amount': self.hyper_mode_charged_beam_loss_amount,
            'hyper_mode_missile_loss_amount': self.hyper_mode_missile_loss_amount,
            'hyper_mode_phazon_ball_rate': self.hyper_mode_phazon_ball_rate,
            'hyper_mode_damage_multiplier': self.hyper_mode_damage_multiplier,
            'hyper_mode_charged_rate_scale': self.hyper_mode_charged_rate_scale,
            'hyper_mode_aggro_alert1': self.hyper_mode_aggro_alert1,
            'hyper_mode_aggro_alert2': self.hyper_mode_aggro_alert2,
            'hyper_mode_aggro_alert3': self.hyper_mode_aggro_alert3,
            'hyper_mode_aggro_alert4': self.hyper_mode_aggro_alert4,
            'hyper_mode_aggro_duration': self.hyper_mode_aggro_duration,
            'hyper_mode_aggro_warning': self.hyper_mode_aggro_warning,
            'hyper_mode_initial_damage': self.hyper_mode_initial_damage.to_json(),
            'hyper_mode_damage': self.hyper_mode_damage.to_json(),
            'hyper_mode_phaaze_damage': self.hyper_mode_phaaze_damage.to_json(),
            'hyper_mode_critical_time': self.hyper_mode_critical_time,
            'hyper_mode_critical_time_tutorial': self.hyper_mode_critical_time_tutorial,
            'hyper_mode_critical_clear': self.hyper_mode_critical_clear,
            'hyper_mode_venting_control': self.hyper_mode_venting_control.to_json(),
        }


def _decode_hyper_mode_spline_corruption_rate(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_hyper_mode_phaaze_spline_corruption_rate(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_hyper_mode_initial_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_hyper_mode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_hyper_mode_phaaze_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_hyper_mode_venting_control(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x31ffbfe7: ('hyper_mode_invulnerable_phazon_loss', structs.decode_BIG_bool_),
    0x7fdfaa62: ('hyper_mode_invulnerable_time', structs.decode_BIG_f),
    0x1a75c2d0: ('hyper_mode_corruption_time', structs.decode_BIG_f),
    0xfb9972fc: ('hyper_mode_constant_corruption_rate', structs.decode_BIG_bool_),
    0x699dff41: ('hyper_mode_spline_corruption_rate', _decode_hyper_mode_spline_corruption_rate),
    0x48cc79f2: ('hyper_mode_corruption_rate', structs.decode_BIG_f),
    0x128e6ecc: ('hyper_mode_phaaze_constant_corruption_rate', structs.decode_BIG_bool_),
    0x808ae371: ('hyper_mode_phaaze_spline_corruption_rate', _decode_hyper_mode_phaaze_spline_corruption_rate),
    0xfd4c4fee: ('hyper_mode_phaaze_corruption_rate', structs.decode_BIG_f),
    0x23c70cb5: ('hyper_mode_phaaze_boss_corruption_rate', structs.decode_BIG_f),
    0xab40bed3: ('hyper_mode_phazon_level', structs.decode_BIG_f),
    0x8ed2e3fb: ('hyper_mode_phazon_capacity', structs.decode_BIG_f),
    0xa2482028: ('hyper_mode_danger_percentage', structs.decode_BIG_f),
    0xa3748fa1: ('hyper_mode_beam_loss_amount', structs.decode_BIG_f),
    0x16bc1c24: ('hyper_mode_charged_beam_loss_amount', structs.decode_BIG_f),
    0xedff39f1: ('hyper_mode_missile_loss_amount', structs.decode_BIG_f),
    0x9cedea06: ('hyper_mode_phazon_ball_rate', structs.decode_BIG_f),
    0x56f3c854: ('hyper_mode_damage_multiplier', structs.decode_BIG_f),
    0xdb1120f2: ('hyper_mode_charged_rate_scale', structs.decode_BIG_f),
    0xba8cb0f2: ('hyper_mode_aggro_alert1', structs.decode_BIG_f),
    0x3c18c25c: ('hyper_mode_aggro_alert2', structs.decode_BIG_f),
    0xf74411f9: ('hyper_mode_aggro_alert3', structs.decode_BIG_f),
    0xea412141: ('hyper_mode_aggro_alert4', structs.decode_BIG_f),
    0xb03510b7: ('hyper_mode_aggro_duration', structs.decode_BIG_f),
    0x3f07961a: ('hyper_mode_aggro_warning', structs.decode_BIG_f),
    0x711296e2: ('hyper_mode_initial_damage', _decode_hyper_mode_initial_damage),
    0xb148913b: ('hyper_mode_damage', _decode_hyper_mode_damage),
    0xc5f1943d: ('hyper_mode_phaaze_damage', _decode_hyper_mode_phaaze_damage),
    0x2b6624b1: ('hyper_mode_critical_time', structs.decode_BIG_f),
    0xcd562633: ('hyper_mode_critical_time_tutorial', structs.decode_BIG_f),
    0xbe038cbf: ('hyper_mode_critical_clear', structs.decode_BIG_f),
    0x0f35ee69: ('hyper_mode_venting_control', _decode_hyper_mode_venting_control),
}
