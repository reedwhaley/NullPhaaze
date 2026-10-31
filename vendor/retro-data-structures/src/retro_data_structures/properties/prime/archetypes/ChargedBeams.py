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
import retro_data_structures.enums.prime as enums

if typing.TYPE_CHECKING:
    class ChargedBeamsJson(typing_extensions.TypedDict):
        power: int
        ice: int
        wave: int
        plasma: int
        deflected: int
    

@dataclasses.dataclass()
class ChargedBeams(BaseProperty):
    power: enums.VulnerabilityTypeEnum = dataclasses.field(default=enums.VulnerabilityTypeEnum.DoubleDamage, metadata={
        'reflection': FieldReflection[enums.VulnerabilityTypeEnum](
            enums.VulnerabilityTypeEnum, id=0x00000000, original_name='Power', from_json=enums.VulnerabilityTypeEnum.from_json, to_json=enums.VulnerabilityTypeEnum.to_json
        ),
    })
    ice: enums.VulnerabilityTypeEnum = dataclasses.field(default=enums.VulnerabilityTypeEnum.DoubleDamage, metadata={
        'reflection': FieldReflection[enums.VulnerabilityTypeEnum](
            enums.VulnerabilityTypeEnum, id=0x00000001, original_name='Ice', from_json=enums.VulnerabilityTypeEnum.from_json, to_json=enums.VulnerabilityTypeEnum.to_json
        ),
    })
    wave: enums.VulnerabilityTypeEnum = dataclasses.field(default=enums.VulnerabilityTypeEnum.DoubleDamage, metadata={
        'reflection': FieldReflection[enums.VulnerabilityTypeEnum](
            enums.VulnerabilityTypeEnum, id=0x00000002, original_name='Wave', from_json=enums.VulnerabilityTypeEnum.from_json, to_json=enums.VulnerabilityTypeEnum.to_json
        ),
    })
    plasma: enums.VulnerabilityTypeEnum = dataclasses.field(default=enums.VulnerabilityTypeEnum.DoubleDamage, metadata={
        'reflection': FieldReflection[enums.VulnerabilityTypeEnum](
            enums.VulnerabilityTypeEnum, id=0x00000003, original_name='Plasma', from_json=enums.VulnerabilityTypeEnum.from_json, to_json=enums.VulnerabilityTypeEnum.to_json
        ),
    })
    deflected: enums.DeflectTypeEnum = dataclasses.field(default=enums.DeflectTypeEnum._None, metadata={
        'reflection': FieldReflection[enums.DeflectTypeEnum](
            enums.DeflectTypeEnum, id=0x00000004, original_name='Deflected', from_json=enums.DeflectTypeEnum.from_json, to_json=enums.DeflectTypeEnum.to_json
        ),
    })

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None) -> typing_extensions.Self:
        property_size = None  # Atomic
        power = enums.VulnerabilityTypeEnum.from_stream(data, game)
        ice = enums.VulnerabilityTypeEnum.from_stream(data, game)
        wave = enums.VulnerabilityTypeEnum.from_stream(data, game)
        plasma = enums.VulnerabilityTypeEnum.from_stream(data, game)
        deflected = enums.DeflectTypeEnum.from_stream(data, game)
        return cls(power, ice, wave, plasma, deflected)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        self.power.to_stream(data, game)
        self.ice.to_stream(data, game)
        self.wave.to_stream(data, game)
        self.plasma.to_stream(data, game)
        self.deflected.to_stream(data, game)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ChargedBeamsJson", data)
        return cls(
            power=enums.VulnerabilityTypeEnum.from_json(json_data['power']),
            ice=enums.VulnerabilityTypeEnum.from_json(json_data['ice']),
            wave=enums.VulnerabilityTypeEnum.from_json(json_data['wave']),
            plasma=enums.VulnerabilityTypeEnum.from_json(json_data['plasma']),
            deflected=enums.DeflectTypeEnum.from_json(json_data['deflected']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'power': self.power.to_json(),
            'ice': self.ice.to_json(),
            'wave': self.wave.to_json(),
            'plasma': self.plasma.to_json(),
            'deflected': self.deflected.to_json(),
        }
