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
from retro_data_structures.properties.echoes.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.echoes.archetypes.SandBossChargeBeamData import SandBossChargeBeamData

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SandBossMultiWormAttackDataJson(typing_extensions.TypedDict):
        double_charge: json_util.JsonObject
        triple_charge: json_util.JsonObject
        charge_beam_info: json_util.JsonObject
    

@dataclasses.dataclass()
class SandBossMultiWormAttackData(BaseProperty):
    double_charge: SandBossChargeBeamData = dataclasses.field(default_factory=SandBossChargeBeamData, metadata={
        'reflection': FieldReflection[SandBossChargeBeamData](
            SandBossChargeBeamData, id=0xb9784f0e, original_name='DoubleCharge', from_json=SandBossChargeBeamData.from_json, to_json=SandBossChargeBeamData.to_json
        ),
    })
    triple_charge: SandBossChargeBeamData = dataclasses.field(default_factory=SandBossChargeBeamData, metadata={
        'reflection': FieldReflection[SandBossChargeBeamData](
            SandBossChargeBeamData, id=0xb8ae1bdc, original_name='TripleCharge', from_json=SandBossChargeBeamData.from_json, to_json=SandBossChargeBeamData.to_json
        ),
    })
    charge_beam_info: PlasmaBeamInfo = dataclasses.field(default_factory=PlasmaBeamInfo, metadata={
        'reflection': FieldReflection[PlasmaBeamInfo](
            PlasmaBeamInfo, id=0x94da6435, original_name='ChargeBeamInfo', from_json=PlasmaBeamInfo.from_json, to_json=PlasmaBeamInfo.to_json
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
        assert property_id == 0xb9784f0e
        double_charge = SandBossChargeBeamData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb8ae1bdc
        triple_charge = SandBossChargeBeamData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x94da6435
        charge_beam_info = PlasmaBeamInfo.from_stream(data, game, property_size, default_override={'length': 500.0, 'radius': 1.0, 'expansion_speed': 4.0, 'life_time': 1.0, 'pulse_speed': 20.0, 'shutdown_time': 0.25, 'pulse_effect_scale': 2.0, 'travel_speed': 150.0, 'inner_color': Color(r=0.5, g=0.5, b=0.5, a=0.5), 'outer_color': Color(r=0.6000000238418579, g=0.6000000238418579, b=0.0, a=0.5)})
    
        return cls(double_charge, triple_charge, charge_beam_info)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x03')  # 3 properties

        data.write(b'\xb9xO\x0e')  # 0xb9784f0e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.double_charge.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb8\xae\x1b\xdc')  # 0xb8ae1bdc
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.triple_charge.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x94\xdad5')  # 0x94da6435
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.charge_beam_info.to_stream(data, game, default_override={'length': 500.0, 'radius': 1.0, 'expansion_speed': 4.0, 'life_time': 1.0, 'pulse_speed': 20.0, 'shutdown_time': 0.25, 'pulse_effect_scale': 2.0, 'travel_speed': 150.0, 'inner_color': Color(r=0.5, g=0.5, b=0.5, a=0.5), 'outer_color': Color(r=0.6000000238418579, g=0.6000000238418579, b=0.0, a=0.5)})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SandBossMultiWormAttackDataJson", data)
        return cls(
            double_charge=SandBossChargeBeamData.from_json(json_data['double_charge']),
            triple_charge=SandBossChargeBeamData.from_json(json_data['triple_charge']),
            charge_beam_info=PlasmaBeamInfo.from_json(json_data['charge_beam_info']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'double_charge': self.double_charge.to_json(),
            'triple_charge': self.triple_charge.to_json(),
            'charge_beam_info': self.charge_beam_info.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.double_charge.dependencies_for, "double_charge", "SandBossChargeBeamData"),
            (self.triple_charge.dependencies_for, "triple_charge", "SandBossChargeBeamData"),
            (self.charge_beam_info.dependencies_for, "charge_beam_info", "PlasmaBeamInfo"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for SandBossMultiWormAttackData.{field_name} ({field_type}): {e}"
                )


def _decode_double_charge(data: typing.BinaryIO, game: Game, property_size: int) -> SandBossChargeBeamData:
    return SandBossChargeBeamData.from_stream(data, game, property_size)


def _decode_triple_charge(data: typing.BinaryIO, game: Game, property_size: int) -> SandBossChargeBeamData:
    return SandBossChargeBeamData.from_stream(data, game, property_size)


def _decode_charge_beam_info(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size, default_override={'length': 500.0, 'radius': 1.0, 'expansion_speed': 4.0, 'life_time': 1.0, 'pulse_speed': 20.0, 'shutdown_time': 0.25, 'pulse_effect_scale': 2.0, 'travel_speed': 150.0, 'inner_color': Color(r=0.5, g=0.5, b=0.5, a=0.5), 'outer_color': Color(r=0.6000000238418579, g=0.6000000238418579, b=0.0, a=0.5)})


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xb9784f0e: ('double_charge', _decode_double_charge),
    0xb8ae1bdc: ('triple_charge', _decode_triple_charge),
    0x94da6435: ('charge_beam_info', _decode_charge_beam_info),
}
