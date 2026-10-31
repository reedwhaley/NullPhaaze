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
from retro_data_structures.properties.echoes.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SandBossStampedeDataJson(typing_extensions.TypedDict):
        unknown_0xbed8a4ba: float
        unknown_0xc2b98161: float
        unknown_0x5fb66017: float
        break_stampede_hp: float
        stampede_armor_explosion: int
        sound_stampede_armor_explode: int
        sound_stampede_armor_explode_pain: int
        stampede_damage: json_util.JsonObject
        stampede_sand_fountain_fx: int
    

@dataclasses.dataclass()
class SandBossStampedeData(BaseProperty):
    unknown_0xbed8a4ba: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbed8a4ba, original_name='Unknown'
        ),
    })
    unknown_0xc2b98161: float = dataclasses.field(default=2.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc2b98161, original_name='Unknown'
        ),
    })
    unknown_0x5fb66017: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5fb66017, original_name='Unknown'
        ),
    })
    break_stampede_hp: float = dataclasses.field(default=150.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbab42316, original_name='BreakStampedeHP'
        ),
    })
    stampede_armor_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x8f06342a, original_name='StampedeArmorExplosion'
        ),
    })
    sound_stampede_armor_explode: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xd8b11129, original_name='Sound_StampedeArmorExplode'
        ),
    })
    sound_stampede_armor_explode_pain: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xe99e5316, original_name='Sound_StampedeArmorExplodePain'
        ),
    })
    stampede_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x1440d152, original_name='StampedeDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    stampede_sand_fountain_fx: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x686489fd, original_name='StampedeSandFountainFx'
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
        if property_count != 9:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbed8a4ba
        unknown_0xbed8a4ba = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc2b98161
        unknown_0xc2b98161 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5fb66017
        unknown_0x5fb66017 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbab42316
        break_stampede_hp = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8f06342a
        stampede_armor_explosion = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd8b11129
        sound_stampede_armor_explode = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe99e5316
        sound_stampede_armor_explode_pain = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1440d152
        stampede_damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_radius': 13.0, 'di_knock_back_power': 10.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x686489fd
        stampede_sand_fountain_fx = structs.BIG_L.unpack(data.read(4))[0]
    
        return cls(unknown_0xbed8a4ba, unknown_0xc2b98161, unknown_0x5fb66017, break_stampede_hp, stampede_armor_explosion, sound_stampede_armor_explode, sound_stampede_armor_explode_pain, stampede_damage, stampede_sand_fountain_fx)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\t')  # 9 properties

        data.write(b'\xbe\xd8\xa4\xba')  # 0xbed8a4ba
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xbed8a4ba))

        data.write(b'\xc2\xb9\x81a')  # 0xc2b98161
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xc2b98161))

        data.write(b'_\xb6`\x17')  # 0x5fb66017
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x5fb66017))

        data.write(b'\xba\xb4#\x16')  # 0xbab42316
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.break_stampede_hp))

        data.write(b'\x8f\x064*')  # 0x8f06342a
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.stampede_armor_explosion))

        data.write(b'\xd8\xb1\x11)')  # 0xd8b11129
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_stampede_armor_explode))

        data.write(b'\xe9\x9eS\x16')  # 0xe99e5316
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.sound_stampede_armor_explode_pain))

        data.write(b'\x14@\xd1R')  # 0x1440d152
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stampede_damage.to_stream(data, game, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_radius': 13.0, 'di_knock_back_power': 10.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'hd\x89\xfd')  # 0x686489fd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.stampede_sand_fountain_fx))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SandBossStampedeDataJson", data)
        return cls(
            unknown_0xbed8a4ba=json_data['unknown_0xbed8a4ba'],
            unknown_0xc2b98161=json_data['unknown_0xc2b98161'],
            unknown_0x5fb66017=json_data['unknown_0x5fb66017'],
            break_stampede_hp=json_data['break_stampede_hp'],
            stampede_armor_explosion=json_data['stampede_armor_explosion'],
            sound_stampede_armor_explode=json_data['sound_stampede_armor_explode'],
            sound_stampede_armor_explode_pain=json_data['sound_stampede_armor_explode_pain'],
            stampede_damage=DamageInfo.from_json(json_data['stampede_damage']),
            stampede_sand_fountain_fx=json_data['stampede_sand_fountain_fx'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'unknown_0xbed8a4ba': self.unknown_0xbed8a4ba,
            'unknown_0xc2b98161': self.unknown_0xc2b98161,
            'unknown_0x5fb66017': self.unknown_0x5fb66017,
            'break_stampede_hp': self.break_stampede_hp,
            'stampede_armor_explosion': self.stampede_armor_explosion,
            'sound_stampede_armor_explode': self.sound_stampede_armor_explode,
            'sound_stampede_armor_explode_pain': self.sound_stampede_armor_explode_pain,
            'stampede_damage': self.stampede_damage.to_json(),
            'stampede_sand_fountain_fx': self.stampede_sand_fountain_fx,
        }

    def _dependencies_for_stampede_armor_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.stampede_armor_explosion)

    def _dependencies_for_sound_stampede_armor_explode(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_stampede_armor_explode)

    def _dependencies_for_sound_stampede_armor_explode_pain(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.sound_stampede_armor_explode_pain)

    def _dependencies_for_stampede_sand_fountain_fx(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.stampede_sand_fountain_fx)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_stampede_armor_explosion, "stampede_armor_explosion", "AssetId"),
            (self._dependencies_for_sound_stampede_armor_explode, "sound_stampede_armor_explode", "int"),
            (self._dependencies_for_sound_stampede_armor_explode_pain, "sound_stampede_armor_explode_pain", "int"),
            (self._dependencies_for_stampede_sand_fountain_fx, "stampede_sand_fountain_fx", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for SandBossStampedeData.{field_name} ({field_type}): {e}"
                )


def _decode_stampede_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_weapon_type': 11, 'di_damage': 20.0, 'di_radius': 13.0, 'di_knock_back_power': 10.0})


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xbed8a4ba: ('unknown_0xbed8a4ba', structs.decode_BIG_f),
    0xc2b98161: ('unknown_0xc2b98161', structs.decode_BIG_f),
    0x5fb66017: ('unknown_0x5fb66017', structs.decode_BIG_f),
    0xbab42316: ('break_stampede_hp', structs.decode_BIG_f),
    0x8f06342a: ('stampede_armor_explosion', structs.decode_BIG_L),
    0xd8b11129: ('sound_stampede_armor_explode', structs.decode_BIG_l),
    0xe99e5316: ('sound_stampede_armor_explode_pain', structs.decode_BIG_l),
    0x1440d152: ('stampede_damage', _decode_stampede_damage),
    0x686489fd: ('stampede_sand_fountain_fx', structs.decode_BIG_L),
}
