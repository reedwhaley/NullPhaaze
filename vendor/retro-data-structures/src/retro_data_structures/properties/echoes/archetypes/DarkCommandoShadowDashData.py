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
from retro_data_structures.properties.echoes.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class DarkCommandoShadowDashDataJson(typing_extensions.TypedDict):
        min_shadow_dash_search_range: float
        max_shadow_dash_search_range: float
        shadow_dash_speed: float
        shadow_decoy_hp: float
        shadow_decoy_fx: int
        sound_shadow_decoy: json_util.JsonObject
        sound_cloak: json_util.JsonObject
        sound_de_cloak: json_util.JsonObject
        shadow_decoy_vulnerability: json_util.JsonObject
        shadow_dash_vulnerability: json_util.JsonObject
    

@dataclasses.dataclass()
class DarkCommandoShadowDashData(BaseProperty):
    min_shadow_dash_search_range: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa0d037ee, original_name='MinShadowDashSearchRange'
        ),
    })
    max_shadow_dash_search_range: float = dataclasses.field(default=40.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4f522994, original_name='MaxShadowDashSearchRange'
        ),
    })
    shadow_dash_speed: float = dataclasses.field(default=25.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x87461cc6, original_name='ShadowDashSpeed'
        ),
    })
    shadow_decoy_hp: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5d02f384, original_name='ShadowDecoyHP'
        ),
    })
    shadow_decoy_fx: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2dc80b4b, original_name='ShadowDecoyFx'
        ),
    })
    sound_shadow_decoy: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x03392283, original_name='Sound_ShadowDecoy', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_cloak: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0x9dedcff1, original_name='Sound_Cloak', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    sound_de_cloak: AudioPlaybackParms = dataclasses.field(default_factory=AudioPlaybackParms, metadata={
        'reflection': FieldReflection[AudioPlaybackParms](
            AudioPlaybackParms, id=0xf740e01d, original_name='Sound_DeCloak', from_json=AudioPlaybackParms.from_json, to_json=AudioPlaybackParms.to_json
        ),
    })
    shadow_decoy_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xb2f64bb4, original_name='ShadowDecoyVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    shadow_dash_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0xed067447, original_name='ShadowDashVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
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
        assert property_id == 0xa0d037ee
        min_shadow_dash_search_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4f522994
        max_shadow_dash_search_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x87461cc6
        shadow_dash_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5d02f384
        shadow_decoy_hp = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2dc80b4b
        shadow_decoy_fx = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03392283
        sound_shadow_decoy = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9dedcff1
        sound_cloak = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf740e01d
        sound_de_cloak = AudioPlaybackParms.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb2f64bb4
        shadow_decoy_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xed067447
        shadow_dash_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        return cls(min_shadow_dash_search_range, max_shadow_dash_search_range, shadow_dash_speed, shadow_decoy_hp, shadow_decoy_fx, sound_shadow_decoy, sound_cloak, sound_de_cloak, shadow_decoy_vulnerability, shadow_dash_vulnerability)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\n')  # 10 properties

        data.write(b'\xa0\xd07\xee')  # 0xa0d037ee
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_shadow_dash_search_range))

        data.write(b'OR)\x94')  # 0x4f522994
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_shadow_dash_search_range))

        data.write(b'\x87F\x1c\xc6')  # 0x87461cc6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.shadow_dash_speed))

        data.write(b']\x02\xf3\x84')  # 0x5d02f384
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.shadow_decoy_hp))

        data.write(b'-\xc8\x0bK')  # 0x2dc80b4b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.shadow_decoy_fx))

        data.write(b'\x039"\x83')  # 0x3392283
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_shadow_decoy.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9d\xed\xcf\xf1')  # 0x9dedcff1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_cloak.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf7@\xe0\x1d')  # 0xf740e01d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.sound_de_cloak.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb2\xf6K\xb4')  # 0xb2f64bb4
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shadow_decoy_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xed\x06tG')  # 0xed067447
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.shadow_dash_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("DarkCommandoShadowDashDataJson", data)
        return cls(
            min_shadow_dash_search_range=json_data['min_shadow_dash_search_range'],
            max_shadow_dash_search_range=json_data['max_shadow_dash_search_range'],
            shadow_dash_speed=json_data['shadow_dash_speed'],
            shadow_decoy_hp=json_data['shadow_decoy_hp'],
            shadow_decoy_fx=json_data['shadow_decoy_fx'],
            sound_shadow_decoy=AudioPlaybackParms.from_json(json_data['sound_shadow_decoy']),
            sound_cloak=AudioPlaybackParms.from_json(json_data['sound_cloak']),
            sound_de_cloak=AudioPlaybackParms.from_json(json_data['sound_de_cloak']),
            shadow_decoy_vulnerability=DamageVulnerability.from_json(json_data['shadow_decoy_vulnerability']),
            shadow_dash_vulnerability=DamageVulnerability.from_json(json_data['shadow_dash_vulnerability']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'min_shadow_dash_search_range': self.min_shadow_dash_search_range,
            'max_shadow_dash_search_range': self.max_shadow_dash_search_range,
            'shadow_dash_speed': self.shadow_dash_speed,
            'shadow_decoy_hp': self.shadow_decoy_hp,
            'shadow_decoy_fx': self.shadow_decoy_fx,
            'sound_shadow_decoy': self.sound_shadow_decoy.to_json(),
            'sound_cloak': self.sound_cloak.to_json(),
            'sound_de_cloak': self.sound_de_cloak.to_json(),
            'shadow_decoy_vulnerability': self.shadow_decoy_vulnerability.to_json(),
            'shadow_dash_vulnerability': self.shadow_dash_vulnerability.to_json(),
        }

    def _dependencies_for_shadow_decoy_fx(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shadow_decoy_fx)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_shadow_decoy_fx, "shadow_decoy_fx", "AssetId"),
            (self.sound_shadow_decoy.dependencies_for, "sound_shadow_decoy", "AudioPlaybackParms"),
            (self.sound_cloak.dependencies_for, "sound_cloak", "AudioPlaybackParms"),
            (self.sound_de_cloak.dependencies_for, "sound_de_cloak", "AudioPlaybackParms"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for DarkCommandoShadowDashData.{field_name} ({field_type}): {e}"
                )


def _decode_sound_shadow_decoy(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_cloak(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_sound_de_cloak(data: typing.BinaryIO, game: Game, property_size: int) -> AudioPlaybackParms:
    return AudioPlaybackParms.from_stream(data, game, property_size)


def _decode_shadow_decoy_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_shadow_dash_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xa0d037ee: ('min_shadow_dash_search_range', structs.decode_BIG_f),
    0x4f522994: ('max_shadow_dash_search_range', structs.decode_BIG_f),
    0x87461cc6: ('shadow_dash_speed', structs.decode_BIG_f),
    0x5d02f384: ('shadow_decoy_hp', structs.decode_BIG_f),
    0x2dc80b4b: ('shadow_decoy_fx', structs.decode_BIG_L),
    0x03392283: ('sound_shadow_decoy', _decode_sound_shadow_decoy),
    0x9dedcff1: ('sound_cloak', _decode_sound_cloak),
    0xf740e01d: ('sound_de_cloak', _decode_sound_de_cloak),
    0xb2f64bb4: ('shadow_decoy_vulnerability', _decode_shadow_decoy_vulnerability),
    0xed067447: ('shadow_dash_vulnerability', _decode_shadow_dash_vulnerability),
}
