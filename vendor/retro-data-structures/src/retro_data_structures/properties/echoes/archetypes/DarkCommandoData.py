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
from retro_data_structures.properties.echoes.archetypes.AudioPlaybackParms import AudioPlaybackParms
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.archetypes.DarkCommandoChargeBeamData import DarkCommandoChargeBeamData
from retro_data_structures.properties.echoes.archetypes.DarkCommandoEMPData import DarkCommandoEMPData
from retro_data_structures.properties.echoes.archetypes.DarkCommandoShadowDashData import DarkCommandoShadowDashData

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class DarkCommandoDataJson(typing_extensions.TypedDict):
        lurk_chance: float
        taunt_chance: float
        emp_attack_chance: float
        charge_beam_attack_chance: float
        blade_damage: json_util.JsonObject
        sound_impact_rag_doll: json_util.JsonObject
        sound_hurled_death: json_util.JsonObject
        emp_grenade_attack_info: json_util.JsonObject
        charge_beam_attack_info: json_util.JsonObject
        shadow_dash_info: json_util.JsonObject
    

@dataclasses.dataclass()
class DarkCommandoData(BaseProperty):
    lurk_chance: float = dataclasses.field(default=12.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa4858f7d, original_name='LurkChance'
        ),
    })
    taunt_chance: float = dataclasses.field(default=12.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa77f6212, original_name='TauntChance'
        ),
    })
    emp_attack_chance: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x48eac726, original_name='EMPAttackChance'
        ),
    })
    charge_beam_attack_chance: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xb6921ac3, original_name='ChargeBeamAttackChance'
        ),
    })
    blade_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xa5912430, original_name='BladeDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    sound_impact_rag_doll: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xa269ea39, original_name='Sound_ImpactRagDoll', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_hurled_death: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x4eb673be, original_name='Sound_HurledDeath', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    emp_grenade_attack_info: DarkCommandoEMPData = dataclasses.field(default_factory=DarkCommandoEMPData, metadata={
        'reflection': FieldReflection[DarkCommandoEMPData](
            DarkCommandoEMPData, id=0x5ec7f2ba, original_name='EMPGrenadeAttackInfo', from_json=DarkCommandoEMPData.from_json, to_json=DarkCommandoEMPData.to_json
        ),
    })
    charge_beam_attack_info: DarkCommandoChargeBeamData = dataclasses.field(default_factory=DarkCommandoChargeBeamData, metadata={
        'reflection': FieldReflection[DarkCommandoChargeBeamData](
            DarkCommandoChargeBeamData, id=0xe6c64015, original_name='ChargeBeamAttackInfo', from_json=DarkCommandoChargeBeamData.from_json, to_json=DarkCommandoChargeBeamData.to_json
        ),
    })
    shadow_dash_info: DarkCommandoShadowDashData = dataclasses.field(default_factory=DarkCommandoShadowDashData, metadata={
        'reflection': FieldReflection[DarkCommandoShadowDashData](
            DarkCommandoShadowDashData, id=0x18247aec, original_name='ShadowDashInfo', from_json=DarkCommandoShadowDashData.from_json, to_json=DarkCommandoShadowDashData.to_json
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
        assert property_id == 0xa4858f7d
        lurk_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa77f6212
        taunt_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x48eac726
        emp_attack_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb6921ac3
        charge_beam_attack_chance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa5912430
        blade_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa269ea39
        sound_impact_rag_doll = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4eb673be
        sound_hurled_death = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5ec7f2ba
        emp_grenade_attack_info = DarkCommandoEMPData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe6c64015
        charge_beam_attack_info = DarkCommandoChargeBeamData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x18247aec
        shadow_dash_info = DarkCommandoShadowDashData.from_stream(data, game, property_size)
    
        return cls(lurk_chance, taunt_chance, emp_attack_chance, charge_beam_attack_chance, blade_damage, sound_impact_rag_doll, sound_hurled_death, emp_grenade_attack_info, charge_beam_attack_info, shadow_dash_info)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\n')  # 10 properties

        data.write(b'\xa4\x85\x8f}')  # 0xa4858f7d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.lurk_chance))

        data.write(b'\xa7\x7fb\x12')  # 0xa77f6212
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.taunt_chance))

        data.write(b'H\xea\xc7&')  # 0x48eac726
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.emp_attack_chance))

        data.write(b'\xb6\x92\x1a\xc3')  # 0xb6921ac3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.charge_beam_attack_chance))

        data.write(b'\xa5\x91$0')  # 0xa5912430
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.blade_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa2i\xea9')  # 0xa269ea39
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_impact_rag_doll.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'N\xb6s\xbe')  # 0x4eb673be
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_hurled_death.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'^\xc7\xf2\xba')  # 0x5ec7f2ba
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.emp_grenade_attack_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe6\xc6@\x15')  # 0xe6c64015
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.charge_beam_attack_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x18$z\xec')  # 0x18247aec
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shadow_dash_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DarkCommandoDataJson", data)
        return cls(
            lurk_chance=json_data['lurk_chance'],
            taunt_chance=json_data['taunt_chance'],
            emp_attack_chance=json_data['emp_attack_chance'],
            charge_beam_attack_chance=json_data['charge_beam_attack_chance'],
            blade_damage=DamageInfo.from_json(json_data['blade_damage']),
            sound_impact_rag_doll=AudioPlaybackParms.from_json(json_data['sound_impact_rag_doll']),
            sound_hurled_death=AudioPlaybackParms.from_json(json_data['sound_hurled_death']),
            emp_grenade_attack_info=DarkCommandoEMPData.from_json(json_data['emp_grenade_attack_info']),
            charge_beam_attack_info=DarkCommandoChargeBeamData.from_json(json_data['charge_beam_attack_info']),
            shadow_dash_info=DarkCommandoShadowDashData.from_json(json_data['shadow_dash_info']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'lurk_chance': self.lurk_chance,
            'taunt_chance': self.taunt_chance,
            'emp_attack_chance': self.emp_attack_chance,
            'charge_beam_attack_chance': self.charge_beam_attack_chance,
            'blade_damage': self.blade_damage.to_json(),
            'sound_impact_rag_doll': self.sound_impact_rag_doll.to_json(),
            'sound_hurled_death': self.sound_hurled_death.to_json(),
            'emp_grenade_attack_info': self.emp_grenade_attack_info.to_json(),
            'charge_beam_attack_info': self.charge_beam_attack_info.to_json(),
            'shadow_dash_info': self.shadow_dash_info.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.sound_impact_rag_doll.dependencies_for, "sound_impact_rag_doll", "AudioPlaybackParms"),
            (self.sound_hurled_death.dependencies_for, "sound_hurled_death", "AudioPlaybackParms"),
            (self.emp_grenade_attack_info.dependencies_for, "emp_grenade_attack_info", "DarkCommandoEMPData"),
            (self.charge_beam_attack_info.dependencies_for, "charge_beam_attack_info", "DarkCommandoChargeBeamData"),
            (self.shadow_dash_info.dependencies_for, "shadow_dash_info", "DarkCommandoShadowDashData"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for DarkCommandoData.{field_name} ({field_type}): {e}"
                )


def _decode_blade_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_knock_back_power': 10.0})


def _decode_sound_impact_rag_doll(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_hurled_death(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_emp_grenade_attack_info(data: typing.BinaryIO, game: Game, property_size: int) -> DarkCommandoEMPData:
    return DarkCommandoEMPData.from_stream(data, game, property_size)


def _decode_charge_beam_attack_info(data: typing.BinaryIO, game: Game, property_size: int) -> DarkCommandoChargeBeamData:
    return DarkCommandoChargeBeamData.from_stream(data, game, property_size)


def _decode_shadow_dash_info(data: typing.BinaryIO, game: Game, property_size: int) -> DarkCommandoShadowDashData:
    return DarkCommandoShadowDashData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xa4858f7d: ('lurk_chance', structs.decode_BIG_f),
    0xa77f6212: ('taunt_chance', structs.decode_BIG_f),
    0x48eac726: ('emp_attack_chance', structs.decode_BIG_f),
    0xb6921ac3: ('charge_beam_attack_chance', structs.decode_BIG_f),
    0xa5912430: ('blade_damage', _decode_blade_damage),
    0xa269ea39: ('sound_impact_rag_doll', _decode_sound_impact_rag_doll),
    0x4eb673be: ('sound_hurled_death', _decode_sound_hurled_death),
    0x5ec7f2ba: ('emp_grenade_attack_info', _decode_emp_grenade_attack_info),
    0xe6c64015: ('charge_beam_attack_info', _decode_charge_beam_attack_info),
    0x18247aec: ('shadow_dash_info', _decode_shadow_dash_info),
}
