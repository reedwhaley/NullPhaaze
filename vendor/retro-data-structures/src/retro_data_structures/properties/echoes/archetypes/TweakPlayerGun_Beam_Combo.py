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
import retro_data_structures.enums.echoes as enums
from retro_data_structures.properties.echoes.archetypes.TDamageInfo import TDamageInfo

if typing.TYPE_CHECKING:
    class TweakPlayerGun_Beam_ComboJson(typing_extensions.TypedDict):
        super_missile_power: json_util.JsonObject
        dark_combo_dark: json_util.JsonObject
        light_combo_light: json_util.JsonObject
        annihilator_combo_annihilator: json_util.JsonObject
        unknown: json_util.JsonObject
    

@dataclasses.dataclass()
class TweakPlayerGun_Beam_Combo(BaseProperty):
    super_missile_power: TDamageInfo = dataclasses.field(default_factory=TDamageInfo, metadata={
        'reflection': FieldReflection[TDamageInfo](
            TDamageInfo, id=0xc713acf9, original_name='SuperMissile_Power', from_json=TDamageInfo.from_json, to_json=TDamageInfo.to_json
        ),
    })
    dark_combo_dark: TDamageInfo = dataclasses.field(default_factory=TDamageInfo, metadata={
        'reflection': FieldReflection[TDamageInfo](
            TDamageInfo, id=0x19468f2a, original_name='DarkCombo_Dark', from_json=TDamageInfo.from_json, to_json=TDamageInfo.to_json
        ),
    })
    light_combo_light: TDamageInfo = dataclasses.field(default_factory=TDamageInfo, metadata={
        'reflection': FieldReflection[TDamageInfo](
            TDamageInfo, id=0x48ac6dd8, original_name='LightCombo_Light', from_json=TDamageInfo.from_json, to_json=TDamageInfo.to_json
        ),
    })
    annihilator_combo_annihilator: TDamageInfo = dataclasses.field(default_factory=TDamageInfo, metadata={
        'reflection': FieldReflection[TDamageInfo](
            TDamageInfo, id=0xc1c315ff, original_name='AnnihilatorCombo_Annihilator', from_json=TDamageInfo.from_json, to_json=TDamageInfo.to_json
        ),
    })
    unknown: TDamageInfo = dataclasses.field(default_factory=TDamageInfo, metadata={
        'reflection': FieldReflection[TDamageInfo](
            TDamageInfo, id=0x42885c6c, original_name='Unknown', from_json=TDamageInfo.from_json, to_json=TDamageInfo.to_json
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
        if property_count != 5:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc713acf9
        super_missile_power = TDamageInfo.from_stream(data, game, property_size, default_override={'damage_amount': 180.0, 'radius_damage_amount': 120.0, 'damage_radius': 8.0, 'knock_back_power': 8.0, 'weapon_type': enums.WeaponTypeEnum.Power})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19468f2a
        dark_combo_dark = TDamageInfo.from_stream(data, game, property_size, default_override={'weapon_type': enums.WeaponTypeEnum.Dark, 'damage_amount': 150.0, 'radius_damage_amount': 150.0, 'damage_radius': 10.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x48ac6dd8
        light_combo_light = TDamageInfo.from_stream(data, game, property_size, default_override={'weapon_type': enums.WeaponTypeEnum.Light, 'damage_amount': 300.0, 'radius_damage_amount': 150.0, 'damage_radius': 8.0, 'knock_back_power': 8.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc1c315ff
        annihilator_combo_annihilator = TDamageInfo.from_stream(data, game, property_size, default_override={'weapon_type': enums.WeaponTypeEnum.Annihilator, 'damage_amount': 1.2000000476837158, 'radius_damage_amount': 1.2000000476837158})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x42885c6c
        unknown = TDamageInfo.from_stream(data, game, property_size, default_override={'weapon_type': enums.WeaponTypeEnum.CannonBall})
    
        return cls(super_missile_power, dark_combo_dark, light_combo_light, annihilator_combo_annihilator, unknown)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x05')  # 5 properties

        data.write(b'\xc7\x13\xac\xf9')  # 0xc713acf9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.super_missile_power.to_stream(data, game, default_override={'damage_amount': 180.0, 'radius_damage_amount': 120.0, 'damage_radius': 8.0, 'knock_back_power': 8.0, 'weapon_type': enums.WeaponTypeEnum.Power})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x19F\x8f*')  # 0x19468f2a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.dark_combo_dark.to_stream(data, game, default_override={'weapon_type': enums.WeaponTypeEnum.Dark, 'damage_amount': 150.0, 'radius_damage_amount': 150.0, 'damage_radius': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'H\xacm\xd8')  # 0x48ac6dd8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.light_combo_light.to_stream(data, game, default_override={'weapon_type': enums.WeaponTypeEnum.Light, 'damage_amount': 300.0, 'radius_damage_amount': 150.0, 'damage_radius': 8.0, 'knock_back_power': 8.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc1\xc3\x15\xff')  # 0xc1c315ff
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.annihilator_combo_annihilator.to_stream(data, game, default_override={'weapon_type': enums.WeaponTypeEnum.Annihilator, 'damage_amount': 1.2000000476837158, 'radius_damage_amount': 1.2000000476837158})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'B\x88\\l')  # 0x42885c6c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.unknown.to_stream(data, game, default_override={'weapon_type': enums.WeaponTypeEnum.CannonBall})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayerGun_Beam_ComboJson", data)
        return cls(
            super_missile_power=TDamageInfo.from_json(json_data['super_missile_power']),
            dark_combo_dark=TDamageInfo.from_json(json_data['dark_combo_dark']),
            light_combo_light=TDamageInfo.from_json(json_data['light_combo_light']),
            annihilator_combo_annihilator=TDamageInfo.from_json(json_data['annihilator_combo_annihilator']),
            unknown=TDamageInfo.from_json(json_data['unknown']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'super_missile_power': self.super_missile_power.to_json(),
            'dark_combo_dark': self.dark_combo_dark.to_json(),
            'light_combo_light': self.light_combo_light.to_json(),
            'annihilator_combo_annihilator': self.annihilator_combo_annihilator.to_json(),
            'unknown': self.unknown.to_json(),
        }


def _decode_super_missile_power(data: typing.BinaryIO, game: Game, property_size: int) -> TDamageInfo:
    return TDamageInfo.from_stream(data, game, property_size, default_override={'damage_amount': 180.0, 'radius_damage_amount': 120.0, 'damage_radius': 8.0, 'knock_back_power': 8.0, 'weapon_type': enums.WeaponTypeEnum.Power})


def _decode_dark_combo_dark(data: typing.BinaryIO, game: Game, property_size: int) -> TDamageInfo:
    return TDamageInfo.from_stream(data, game, property_size, default_override={'weapon_type': enums.WeaponTypeEnum.Dark, 'damage_amount': 150.0, 'radius_damage_amount': 150.0, 'damage_radius': 10.0})


def _decode_light_combo_light(data: typing.BinaryIO, game: Game, property_size: int) -> TDamageInfo:
    return TDamageInfo.from_stream(data, game, property_size, default_override={'weapon_type': enums.WeaponTypeEnum.Light, 'damage_amount': 300.0, 'radius_damage_amount': 150.0, 'damage_radius': 8.0, 'knock_back_power': 8.0})


def _decode_annihilator_combo_annihilator(data: typing.BinaryIO, game: Game, property_size: int) -> TDamageInfo:
    return TDamageInfo.from_stream(data, game, property_size, default_override={'weapon_type': enums.WeaponTypeEnum.Annihilator, 'damage_amount': 1.2000000476837158, 'radius_damage_amount': 1.2000000476837158})


def _decode_unknown(data: typing.BinaryIO, game: Game, property_size: int) -> TDamageInfo:
    return TDamageInfo.from_stream(data, game, property_size, default_override={'weapon_type': enums.WeaponTypeEnum.CannonBall})


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xc713acf9: ('super_missile_power', _decode_super_missile_power),
    0x19468f2a: ('dark_combo_dark', _decode_dark_combo_dark),
    0x48ac6dd8: ('light_combo_light', _decode_light_combo_light),
    0xc1c315ff: ('annihilator_combo_annihilator', _decode_annihilator_combo_annihilator),
    0x42885c6c: ('unknown', _decode_unknown),
}
