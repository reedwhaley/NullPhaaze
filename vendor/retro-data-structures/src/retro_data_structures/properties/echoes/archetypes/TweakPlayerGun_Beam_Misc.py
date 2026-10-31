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
    class TweakPlayerGun_Beam_MiscJson(typing_extensions.TypedDict):
        blackhole_dark: json_util.JsonObject
        sun_burst_rays_light: json_util.JsonObject
        imploder_annihilator: json_util.JsonObject
        ai_burn_damage: float
        player_burn_damage: float
        max_absorbed_phazon_shots: int
        phazon_shot_absorb_radius: float
    

@dataclasses.dataclass()
class TweakPlayerGun_Beam_Misc(BaseProperty):
    blackhole_dark: TDamageInfo = dataclasses.field(default_factory=TDamageInfo, metadata={
        'reflection': FieldReflection[TDamageInfo](
            TDamageInfo, id=0x8aacfc27, original_name='Blackhole_Dark', from_json=TDamageInfo.from_json, to_json=TDamageInfo.to_json
        ),
    })
    sun_burst_rays_light: TDamageInfo = dataclasses.field(default_factory=TDamageInfo, metadata={
        'reflection': FieldReflection[TDamageInfo](
            TDamageInfo, id=0xa054ff1c, original_name='SunBurstRays_Light', from_json=TDamageInfo.from_json, to_json=TDamageInfo.to_json
        ),
    })
    imploder_annihilator: TDamageInfo = dataclasses.field(default_factory=TDamageInfo, metadata={
        'reflection': FieldReflection[TDamageInfo](
            TDamageInfo, id=0xabfa93e9, original_name='Imploder_Annihilator', from_json=TDamageInfo.from_json, to_json=TDamageInfo.to_json
        ),
    })
    ai_burn_damage: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf8f9bf33, original_name='AIBurnDamage'
        ),
    })
    player_burn_damage: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4848f444, original_name='PlayerBurnDamage'
        ),
    })
    max_absorbed_phazon_shots: int = dataclasses.field(default=5, metadata={
        'reflection': FieldReflection[int](
            int, id=0x1e710222, original_name='MaxAbsorbedPhazonShots'
        ),
    })
    phazon_shot_absorb_radius: float = dataclasses.field(default=0.75, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3ae5d1fa, original_name='PhazonShotAbsorbRadius'
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
        if property_count != 7:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8aacfc27
        blackhole_dark = TDamageInfo.from_stream(data, game, property_size, default_override={'weapon_type': enums.WeaponTypeEnum.Dark, 'damage_amount': 1.0, 'radius_damage_amount': 1.0, 'damage_radius': 0.0, 'knock_back_power': 0.10000000149011612})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa054ff1c
        sun_burst_rays_light = TDamageInfo.from_stream(data, game, property_size, default_override={'weapon_type': enums.WeaponTypeEnum.Light, 'damage_amount': 0.800000011920929, 'radius_damage_amount': 0.800000011920929, 'damage_radius': 0.0, 'knock_back_power': 0.800000011920929})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xabfa93e9
        imploder_annihilator = TDamageInfo.from_stream(data, game, property_size, default_override={'weapon_type': enums.WeaponTypeEnum.Annihilator, 'damage_amount': 0.800000011920929, 'radius_damage_amount': 0.800000011920929, 'damage_radius': 0.0, 'knock_back_power': 0.800000011920929})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf8f9bf33
        ai_burn_damage = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4848f444
        player_burn_damage = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1e710222
        max_absorbed_phazon_shots = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3ae5d1fa
        phazon_shot_absorb_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(blackhole_dark, sun_burst_rays_light, imploder_annihilator, ai_burn_damage, player_burn_damage, max_absorbed_phazon_shots, phazon_shot_absorb_radius)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x07')  # 7 properties

        data.write(b"\x8a\xac\xfc'")  # 0x8aacfc27
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.blackhole_dark.to_stream(data, game, default_override={'weapon_type': enums.WeaponTypeEnum.Dark, 'damage_amount': 1.0, 'radius_damage_amount': 1.0, 'damage_radius': 0.0, 'knock_back_power': 0.10000000149011612})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa0T\xff\x1c')  # 0xa054ff1c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sun_burst_rays_light.to_stream(data, game, default_override={'weapon_type': enums.WeaponTypeEnum.Light, 'damage_amount': 0.800000011920929, 'radius_damage_amount': 0.800000011920929, 'damage_radius': 0.0, 'knock_back_power': 0.800000011920929})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xab\xfa\x93\xe9')  # 0xabfa93e9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.imploder_annihilator.to_stream(data, game, default_override={'weapon_type': enums.WeaponTypeEnum.Annihilator, 'damage_amount': 0.800000011920929, 'radius_damage_amount': 0.800000011920929, 'damage_radius': 0.0, 'knock_back_power': 0.800000011920929})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf8\xf9\xbf3')  # 0xf8f9bf33
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ai_burn_damage))

        data.write(b'HH\xf4D')  # 0x4848f444
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.player_burn_damage))

        data.write(b'\x1eq\x02"')  # 0x1e710222
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.max_absorbed_phazon_shots))

        data.write(b':\xe5\xd1\xfa')  # 0x3ae5d1fa
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.phazon_shot_absorb_radius))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayerGun_Beam_MiscJson", data)
        return cls(
            blackhole_dark=TDamageInfo.from_json(json_data['blackhole_dark']),
            sun_burst_rays_light=TDamageInfo.from_json(json_data['sun_burst_rays_light']),
            imploder_annihilator=TDamageInfo.from_json(json_data['imploder_annihilator']),
            ai_burn_damage=json_data['ai_burn_damage'],
            player_burn_damage=json_data['player_burn_damage'],
            max_absorbed_phazon_shots=json_data['max_absorbed_phazon_shots'],
            phazon_shot_absorb_radius=json_data['phazon_shot_absorb_radius'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'blackhole_dark': self.blackhole_dark.to_json(),
            'sun_burst_rays_light': self.sun_burst_rays_light.to_json(),
            'imploder_annihilator': self.imploder_annihilator.to_json(),
            'ai_burn_damage': self.ai_burn_damage,
            'player_burn_damage': self.player_burn_damage,
            'max_absorbed_phazon_shots': self.max_absorbed_phazon_shots,
            'phazon_shot_absorb_radius': self.phazon_shot_absorb_radius,
        }


def _decode_blackhole_dark(data: typing.BinaryIO, game: Game, property_size: int) -> TDamageInfo:
    return TDamageInfo.from_stream(data, game, property_size, default_override={'weapon_type': enums.WeaponTypeEnum.Dark, 'damage_amount': 1.0, 'radius_damage_amount': 1.0, 'damage_radius': 0.0, 'knock_back_power': 0.10000000149011612})


def _decode_sun_burst_rays_light(data: typing.BinaryIO, game: Game, property_size: int) -> TDamageInfo:
    return TDamageInfo.from_stream(data, game, property_size, default_override={'weapon_type': enums.WeaponTypeEnum.Light, 'damage_amount': 0.800000011920929, 'radius_damage_amount': 0.800000011920929, 'damage_radius': 0.0, 'knock_back_power': 0.800000011920929})


def _decode_imploder_annihilator(data: typing.BinaryIO, game: Game, property_size: int) -> TDamageInfo:
    return TDamageInfo.from_stream(data, game, property_size, default_override={'weapon_type': enums.WeaponTypeEnum.Annihilator, 'damage_amount': 0.800000011920929, 'radius_damage_amount': 0.800000011920929, 'damage_radius': 0.0, 'knock_back_power': 0.800000011920929})


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x8aacfc27: ('blackhole_dark', _decode_blackhole_dark),
    0xa054ff1c: ('sun_burst_rays_light', _decode_sun_burst_rays_light),
    0xabfa93e9: ('imploder_annihilator', _decode_imploder_annihilator),
    0xf8f9bf33: ('ai_burn_damage', structs.decode_BIG_f),
    0x4848f444: ('player_burn_damage', structs.decode_BIG_f),
    0x1e710222: ('max_absorbed_phazon_shots', structs.decode_BIG_l),
    0x3ae5d1fa: ('phazon_shot_absorb_radius', structs.decode_BIG_f),
}
