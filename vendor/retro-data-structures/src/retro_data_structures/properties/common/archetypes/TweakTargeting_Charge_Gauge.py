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
from retro_data_structures.properties.color import Color

if typing.TYPE_CHECKING:
    class TweakTargeting_Charge_GaugeJson(typing_extensions.TypedDict):
        charge_gauge_power_beam_angle: float
        charge_gauge_ice_beam_angle: float
        charge_gauge_wave_beam_angle: float
        charge_gauge_plasma_beam_angle: float
        charge_gauge_scale: float
        charge_gauge_color: json_util.JsonValue
        num_charge_gauge_ticks: int
        charge_gauge_tick_delta_angle: float
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xd032c2a1, 0xa118e250, 0xdb1ac8ee, 0xecd100f8, 0x49f8161f, 0x526e60f4, 0xed78e6eb, 0x2c3d9e27)


@dataclasses.dataclass()
class TweakTargeting_Charge_Gauge(BaseProperty):
    charge_gauge_power_beam_angle: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd032c2a1, original_name='ChargeGaugePowerBeamAngle'
        ),
    })
    charge_gauge_ice_beam_angle: float = dataclasses.field(default=90.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa118e250, original_name='ChargeGaugeIceBeamAngle'
        ),
    })
    charge_gauge_wave_beam_angle: float = dataclasses.field(default=150.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdb1ac8ee, original_name='ChargeGaugeWaveBeamAngle'
        ),
    })
    charge_gauge_plasma_beam_angle: float = dataclasses.field(default=210.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xecd100f8, original_name='ChargeGaugePlasmaBeamAngle'
        ),
    })
    charge_gauge_scale: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x49f8161f, original_name='ChargeGaugeScale'
        ),
    })
    charge_gauge_color: Color = dataclasses.field(default_factory=lambda: Color(r=0.2941179871559143, g=0.49411800503730774, b=0.6392160058021545, a=0.47058799862861633), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x526e60f4, original_name='ChargeGaugeColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    num_charge_gauge_ticks: int = dataclasses.field(default=14, metadata={
        'reflection': FieldReflection[int](
            int, id=0xed78e6eb, original_name='NumChargeGaugeTicks'
        ),
    })
    charge_gauge_tick_delta_angle: float = dataclasses.field(default=8.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2c3d9e27, original_name='ChargeGaugeTickDeltaAngle'
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
        if property_count != 8:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHfLHfLHfLHfLHfLHffffLHlLHf')
    
        dec = _FAST_FORMAT.unpack(data.read(92))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[21], dec[24]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            Color(*dec[17:21]),
            dec[23],
            dec[26],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x08')  # 8 properties

        data.write(b'\xd02\xc2\xa1')  # 0xd032c2a1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_gauge_power_beam_angle))

        data.write(b'\xa1\x18\xe2P')  # 0xa118e250
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_gauge_ice_beam_angle))

        data.write(b'\xdb\x1a\xc8\xee')  # 0xdb1ac8ee
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_gauge_wave_beam_angle))

        data.write(b'\xec\xd1\x00\xf8')  # 0xecd100f8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_gauge_plasma_beam_angle))

        data.write(b'I\xf8\x16\x1f')  # 0x49f8161f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_gauge_scale))

        data.write(b'Rn`\xf4')  # 0x526e60f4
        data.write(b'\x00\x10')  # size
        self.charge_gauge_color.to_stream(data, game)

        data.write(b'\xedx\xe6\xeb')  # 0xed78e6eb
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.num_charge_gauge_ticks))

        data.write(b",=\x9e'")  # 0x2c3d9e27
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_gauge_tick_delta_angle))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakTargeting_Charge_GaugeJson", data)
        return cls(
            charge_gauge_power_beam_angle=json_data['charge_gauge_power_beam_angle'],
            charge_gauge_ice_beam_angle=json_data['charge_gauge_ice_beam_angle'],
            charge_gauge_wave_beam_angle=json_data['charge_gauge_wave_beam_angle'],
            charge_gauge_plasma_beam_angle=json_data['charge_gauge_plasma_beam_angle'],
            charge_gauge_scale=json_data['charge_gauge_scale'],
            charge_gauge_color=Color.from_json(json_data['charge_gauge_color']),
            num_charge_gauge_ticks=json_data['num_charge_gauge_ticks'],
            charge_gauge_tick_delta_angle=json_data['charge_gauge_tick_delta_angle'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'charge_gauge_power_beam_angle': self.charge_gauge_power_beam_angle,
            'charge_gauge_ice_beam_angle': self.charge_gauge_ice_beam_angle,
            'charge_gauge_wave_beam_angle': self.charge_gauge_wave_beam_angle,
            'charge_gauge_plasma_beam_angle': self.charge_gauge_plasma_beam_angle,
            'charge_gauge_scale': self.charge_gauge_scale,
            'charge_gauge_color': self.charge_gauge_color.to_json(),
            'num_charge_gauge_ticks': self.num_charge_gauge_ticks,
            'charge_gauge_tick_delta_angle': self.charge_gauge_tick_delta_angle,
        }


def _decode_charge_gauge_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xd032c2a1: ('charge_gauge_power_beam_angle', structs.decode_BIG_f),
    0xa118e250: ('charge_gauge_ice_beam_angle', structs.decode_BIG_f),
    0xdb1ac8ee: ('charge_gauge_wave_beam_angle', structs.decode_BIG_f),
    0xecd100f8: ('charge_gauge_plasma_beam_angle', structs.decode_BIG_f),
    0x49f8161f: ('charge_gauge_scale', structs.decode_BIG_f),
    0x526e60f4: ('charge_gauge_color', _decode_charge_gauge_color),
    0xed78e6eb: ('num_charge_gauge_ticks', structs.decode_BIG_l),
    0x2c3d9e27: ('charge_gauge_tick_delta_angle', structs.decode_BIG_f),
}
