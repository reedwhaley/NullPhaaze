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
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class ReptilicusHunterChakramJson(typing_extensions.TypedDict):
        chakram_model: int
        energy_effect: int
        trail_effect: int
        static_geometry_collision_effect: int
        in_flight_sound: int
        player_impact_sound: int
        static_geometry_collision_sound: int
        damage: json_util.JsonObject
        hyper_damage: json_util.JsonObject
        speed: float
        overshoot_dist: float
        spin_rate: float
        fade_out_time: float
        visor_effect: int
        stun_time: float
        min_chakram_attack_dist: float
        max_chakram_attack_dist: float
    

@dataclasses.dataclass()
class ReptilicusHunterChakram(BaseProperty):
    chakram_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x66ab57a4, original_name='ChakramModel'
        ),
    })
    energy_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x14143470, original_name='EnergyEffect'
        ),
    })
    trail_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x36eee791, original_name='TrailEffect'
        ),
    })
    static_geometry_collision_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x52f89bf7, original_name='StaticGeometryCollisionEffect'
        ),
    })
    in_flight_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x1a092829, original_name='InFlightSound'
        ),
    })
    player_impact_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe33a996d, original_name='PlayerImpactSound'
        ),
    })
    static_geometry_collision_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xdf64c67a, original_name='StaticGeometryCollisionSound'
        ),
    })
    damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x337f9524, original_name='Damage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    hyper_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xb3dabf84, original_name='HyperDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    speed: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x6392404e, original_name='Speed'
        ),
    })
    overshoot_dist: float = dataclasses.field(default=50.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x508c48d7, original_name='OvershootDist'
        ),
    })
    spin_rate: float = dataclasses.field(default=720.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8b4af5c4, original_name='SpinRate'
        ),
    })
    fade_out_time: float = dataclasses.field(default=0.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7c269ebc, original_name='FadeOutTime'
        ),
    })
    visor_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART', 'ELSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe9c8e2bd, original_name='VisorEffect'
        ),
    })
    stun_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x7e192395, original_name='StunTime'
        ),
    })
    min_chakram_attack_dist: float = dataclasses.field(default=20.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2f79b3d0, original_name='MinChakramAttackDist'
        ),
    })
    max_chakram_attack_dist: float = dataclasses.field(default=60.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x11cc7b58, original_name='MaxChakramAttackDist'
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
        if property_count != 17:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x66ab57a4
        chakram_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x14143470
        energy_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x36eee791
        trail_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x52f89bf7
        static_geometry_collision_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1a092829
        in_flight_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe33a996d
        player_impact_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdf64c67a
        static_geometry_collision_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337f9524
        damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3dabf84
        hyper_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6392404e
        speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x508c48d7
        overshoot_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8b4af5c4
        spin_rate = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7c269ebc
        fade_out_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe9c8e2bd
        visor_effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e192395
        stun_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2f79b3d0
        min_chakram_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x11cc7b58
        max_chakram_attack_dist = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(chakram_model, energy_effect, trail_effect, static_geometry_collision_effect, in_flight_sound, player_impact_sound, static_geometry_collision_sound, damage, hyper_damage, speed, overshoot_dist, spin_rate, fade_out_time, visor_effect, stun_time, min_chakram_attack_dist, max_chakram_attack_dist)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x11')  # 17 properties

        data.write(b'f\xabW\xa4')  # 0x66ab57a4
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.chakram_model))

        data.write(b'\x14\x144p')  # 0x14143470
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.energy_effect))

        data.write(b'6\xee\xe7\x91')  # 0x36eee791
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.trail_effect))

        data.write(b'R\xf8\x9b\xf7')  # 0x52f89bf7
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.static_geometry_collision_effect))

        data.write(b'\x1a\t()')  # 0x1a092829
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.in_flight_sound))

        data.write(b'\xe3:\x99m')  # 0xe33a996d
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.player_impact_sound))

        data.write(b'\xdfd\xc6z')  # 0xdf64c67a
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.static_geometry_collision_sound))

        data.write(b'3\x7f\x95$')  # 0x337f9524
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb3\xda\xbf\x84')  # 0xb3dabf84
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'c\x92@N')  # 0x6392404e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.speed))

        data.write(b'P\x8cH\xd7')  # 0x508c48d7
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.overshoot_dist))

        data.write(b'\x8bJ\xf5\xc4')  # 0x8b4af5c4
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.spin_rate))

        data.write(b'|&\x9e\xbc')  # 0x7c269ebc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fade_out_time))

        data.write(b'\xe9\xc8\xe2\xbd')  # 0xe9c8e2bd
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.visor_effect))

        data.write(b'~\x19#\x95')  # 0x7e192395
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stun_time))

        data.write(b'/y\xb3\xd0')  # 0x2f79b3d0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_chakram_attack_dist))

        data.write(b'\x11\xcc{X')  # 0x11cc7b58
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_chakram_attack_dist))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ReptilicusHunterChakramJson", data)
        return cls(
            chakram_model=json_data['chakram_model'],
            energy_effect=json_data['energy_effect'],
            trail_effect=json_data['trail_effect'],
            static_geometry_collision_effect=json_data['static_geometry_collision_effect'],
            in_flight_sound=json_data['in_flight_sound'],
            player_impact_sound=json_data['player_impact_sound'],
            static_geometry_collision_sound=json_data['static_geometry_collision_sound'],
            damage=DamageInfo.from_json(json_data['damage']),
            hyper_damage=DamageInfo.from_json(json_data['hyper_damage']),
            speed=json_data['speed'],
            overshoot_dist=json_data['overshoot_dist'],
            spin_rate=json_data['spin_rate'],
            fade_out_time=json_data['fade_out_time'],
            visor_effect=json_data['visor_effect'],
            stun_time=json_data['stun_time'],
            min_chakram_attack_dist=json_data['min_chakram_attack_dist'],
            max_chakram_attack_dist=json_data['max_chakram_attack_dist'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'chakram_model': self.chakram_model,
            'energy_effect': self.energy_effect,
            'trail_effect': self.trail_effect,
            'static_geometry_collision_effect': self.static_geometry_collision_effect,
            'in_flight_sound': self.in_flight_sound,
            'player_impact_sound': self.player_impact_sound,
            'static_geometry_collision_sound': self.static_geometry_collision_sound,
            'damage': self.damage.to_json(),
            'hyper_damage': self.hyper_damage.to_json(),
            'speed': self.speed,
            'overshoot_dist': self.overshoot_dist,
            'spin_rate': self.spin_rate,
            'fade_out_time': self.fade_out_time,
            'visor_effect': self.visor_effect,
            'stun_time': self.stun_time,
            'min_chakram_attack_dist': self.min_chakram_attack_dist,
            'max_chakram_attack_dist': self.max_chakram_attack_dist,
        }

    def _dependencies_for_chakram_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.chakram_model)

    def _dependencies_for_energy_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.energy_effect)

    def _dependencies_for_trail_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.trail_effect)

    def _dependencies_for_static_geometry_collision_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.static_geometry_collision_effect)

    def _dependencies_for_in_flight_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.in_flight_sound)

    def _dependencies_for_player_impact_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.player_impact_sound)

    def _dependencies_for_static_geometry_collision_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.static_geometry_collision_sound)

    def _dependencies_for_visor_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.visor_effect)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_chakram_model, "chakram_model", "AssetId"),
            (self._dependencies_for_energy_effect, "energy_effect", "AssetId"),
            (self._dependencies_for_trail_effect, "trail_effect", "AssetId"),
            (self._dependencies_for_static_geometry_collision_effect, "static_geometry_collision_effect", "AssetId"),
            (self._dependencies_for_in_flight_sound, "in_flight_sound", "AssetId"),
            (self._dependencies_for_player_impact_sound, "player_impact_sound", "AssetId"),
            (self._dependencies_for_static_geometry_collision_sound, "static_geometry_collision_sound", "AssetId"),
            (self._dependencies_for_visor_effect, "visor_effect", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for ReptilicusHunterChakram.{field_name} ({field_type}): {e}"
                )


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_hyper_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x66ab57a4: ('chakram_model', structs.decode_BIG_Q),
    0x14143470: ('energy_effect', structs.decode_BIG_Q),
    0x36eee791: ('trail_effect', structs.decode_BIG_Q),
    0x52f89bf7: ('static_geometry_collision_effect', structs.decode_BIG_Q),
    0x1a092829: ('in_flight_sound', structs.decode_BIG_Q),
    0xe33a996d: ('player_impact_sound', structs.decode_BIG_Q),
    0xdf64c67a: ('static_geometry_collision_sound', structs.decode_BIG_Q),
    0x337f9524: ('damage', _decode_damage),
    0xb3dabf84: ('hyper_damage', _decode_hyper_damage),
    0x6392404e: ('speed', structs.decode_BIG_f),
    0x508c48d7: ('overshoot_dist', structs.decode_BIG_f),
    0x8b4af5c4: ('spin_rate', structs.decode_BIG_f),
    0x7c269ebc: ('fade_out_time', structs.decode_BIG_f),
    0xe9c8e2bd: ('visor_effect', structs.decode_BIG_Q),
    0x7e192395: ('stun_time', structs.decode_BIG_f),
    0x2f79b3d0: ('min_chakram_attack_dist', structs.decode_BIG_f),
    0x11cc7b58: ('max_chakram_attack_dist', structs.decode_BIG_f),
}
