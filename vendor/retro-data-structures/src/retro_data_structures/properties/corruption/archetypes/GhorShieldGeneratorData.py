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
from retro_data_structures.properties.corruption.archetypes.GhorWeakSpotData import GhorWeakSpotData
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class GhorShieldGeneratorDataJson(typing_extensions.TypedDict):
        weak_spot: json_util.JsonObject
        reset_time: float
        reset_damage: float
        activate_spline: json_util.JsonObject
        deactivate_spline: json_util.JsonObject
        active_effect: str
        hit_effect: str
        inactive_effect: str
        shield_on_loop_sound: int
        shield_off_sound: int
    

@dataclasses.dataclass()
class GhorShieldGeneratorData(BaseProperty):
    weak_spot: GhorWeakSpotData = dataclasses.field(default_factory=GhorWeakSpotData, metadata={
        'reflection': FieldReflection[GhorWeakSpotData](
            GhorWeakSpotData, id=0xfdea5d06, original_name='WeakSpot', from_json=GhorWeakSpotData.from_json, to_json=GhorWeakSpotData.to_json
        ),
    })
    reset_time: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2bcd1d77, original_name='ResetTime'
        ),
    })
    reset_damage: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7fec6162, original_name='ResetDamage'
        ),
    })
    activate_spline: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x39d64e40, original_name='ActivateSpline', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    deactivate_spline: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xfc336bed, original_name='DeactivateSpline', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    active_effect: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x60bdaa38, original_name='ActiveEffect'
        ),
    })
    hit_effect: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xc60b41b4, original_name='HitEffect'
        ),
    })
    inactive_effect: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x67808780, original_name='InactiveEffect'
        ),
    })
    shield_on_loop_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x62771f66, original_name='ShieldOnLoopSound'
        ),
    })
    shield_off_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb75b8442, original_name='ShieldOffSound'
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
        assert property_id == 0xfdea5d06
        weak_spot = GhorWeakSpotData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2bcd1d77
        reset_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7fec6162
        reset_damage = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x39d64e40
        activate_spline = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfc336bed
        deactivate_spline = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x60bdaa38
        active_effect = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc60b41b4
        hit_effect = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x67808780
        inactive_effect = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x62771f66
        shield_on_loop_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb75b8442
        shield_off_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        return cls(weak_spot, reset_time, reset_damage, activate_spline, deactivate_spline, active_effect, hit_effect, inactive_effect, shield_on_loop_sound, shield_off_sound)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\n')  # 10 properties

        data.write(b'\xfd\xea]\x06')  # 0xfdea5d06
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.weak_spot.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'+\xcd\x1dw')  # 0x2bcd1d77
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.reset_time))

        data.write(b'\x7f\xecab')  # 0x7fec6162
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.reset_damage))

        data.write(b'9\xd6N@')  # 0x39d64e40
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.activate_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfc3k\xed')  # 0xfc336bed
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.deactivate_spline.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'`\xbd\xaa8')  # 0x60bdaa38
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.active_effect.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc6\x0bA\xb4')  # 0xc60b41b4
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.hit_effect.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'g\x80\x87\x80')  # 0x67808780
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.inactive_effect.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'bw\x1ff')  # 0x62771f66
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shield_on_loop_sound))

        data.write(b'\xb7[\x84B')  # 0xb75b8442
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shield_off_sound))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GhorShieldGeneratorDataJson", data)
        return cls(
            weak_spot=GhorWeakSpotData.from_json(json_data['weak_spot']),
            reset_time=json_data['reset_time'],
            reset_damage=json_data['reset_damage'],
            activate_spline=Spline.from_json(json_data['activate_spline']),
            deactivate_spline=Spline.from_json(json_data['deactivate_spline']),
            active_effect=json_data['active_effect'],
            hit_effect=json_data['hit_effect'],
            inactive_effect=json_data['inactive_effect'],
            shield_on_loop_sound=json_data['shield_on_loop_sound'],
            shield_off_sound=json_data['shield_off_sound'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'weak_spot': self.weak_spot.to_json(),
            'reset_time': self.reset_time,
            'reset_damage': self.reset_damage,
            'activate_spline': self.activate_spline.to_json(),
            'deactivate_spline': self.deactivate_spline.to_json(),
            'active_effect': self.active_effect,
            'hit_effect': self.hit_effect,
            'inactive_effect': self.inactive_effect,
            'shield_on_loop_sound': self.shield_on_loop_sound,
            'shield_off_sound': self.shield_off_sound,
        }

    def _dependencies_for_shield_on_loop_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_on_loop_sound)

    def _dependencies_for_shield_off_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_off_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.weak_spot.dependencies_for, "weak_spot", "GhorWeakSpotData"),
            (self._dependencies_for_shield_on_loop_sound, "shield_on_loop_sound", "AssetId"),
            (self._dependencies_for_shield_off_sound, "shield_off_sound", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for GhorShieldGeneratorData.{field_name} ({field_type}): {e}"
                )


def _decode_weak_spot(data: typing.BinaryIO, game: Game, property_size: int) -> GhorWeakSpotData:
    return GhorWeakSpotData.from_stream(data, game, property_size)


def _decode_activate_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_deactivate_spline(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_active_effect(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_hit_effect(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_inactive_effect(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xfdea5d06: ('weak_spot', _decode_weak_spot),
    0x2bcd1d77: ('reset_time', structs.decode_BIG_f),
    0x7fec6162: ('reset_damage', structs.decode_BIG_f),
    0x39d64e40: ('activate_spline', _decode_activate_spline),
    0xfc336bed: ('deactivate_spline', _decode_deactivate_spline),
    0x60bdaa38: ('active_effect', _decode_active_effect),
    0xc60b41b4: ('hit_effect', _decode_hit_effect),
    0x67808780: ('inactive_effect', _decode_inactive_effect),
    0x62771f66: ('shield_on_loop_sound', structs.decode_BIG_Q),
    0xb75b8442: ('shield_off_sound', structs.decode_BIG_Q),
}
