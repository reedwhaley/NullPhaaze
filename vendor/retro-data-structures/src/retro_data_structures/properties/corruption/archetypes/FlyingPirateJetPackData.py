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
from retro_data_structures.properties.corruption.archetypes.GrappleBlock import GrappleBlock
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class FlyingPirateJetPackDataJson(typing_extensions.TypedDict):
        grapple_jet_pack_angle: float
        grapple_stunned_time: float
        stunned_hover_height: float
        stunned_hover_speed: float
        left_remote_weapon_pod_destroyed: int
        right_remote_weapon_pod_destroyed: int
        spin_death_explosion: int
        spin_death_damage: json_util.JsonObject
        stunned_grapple_block: json_util.JsonObject
    

@dataclasses.dataclass()
class FlyingPirateJetPackData(BaseProperty):
    grapple_jet_pack_angle: float = dataclasses.field(default=120.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc6e9d30e, original_name='GrappleJetPackAngle'
        ),
    })
    grapple_stunned_time: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9e9d2bd6, original_name='GrappleStunnedTime'
        ),
    })
    stunned_hover_height: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xf3a72af9, original_name='StunnedHoverHeight'
        ),
    })
    stunned_hover_speed: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x14355be0, original_name='StunnedHoverSpeed'
        ),
    })
    left_remote_weapon_pod_destroyed: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2c79052c, original_name='LeftRemoteWeaponPodDestroyed'
        ),
    })
    right_remote_weapon_pod_destroyed: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x016b65a9, original_name='RightRemoteWeaponPodDestroyed'
        ),
    })
    spin_death_explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd8a92aaa, original_name='SpinDeathExplosion'
        ),
    })
    spin_death_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x5bf6f8e4, original_name='SpinDeathDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    stunned_grapple_block: GrappleBlock = dataclasses.field(default_factory=GrappleBlock, metadata={
        'reflection': FieldReflection[GrappleBlock](
            GrappleBlock, id=0x85543e4e, original_name='StunnedGrappleBlock', from_json=GrappleBlock.from_json, to_json=GrappleBlock.to_json
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
        assert property_id == 0xc6e9d30e
        grapple_jet_pack_angle = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9e9d2bd6
        grapple_stunned_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf3a72af9
        stunned_hover_height = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x14355be0
        stunned_hover_speed = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2c79052c
        left_remote_weapon_pod_destroyed = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x016b65a9
        right_remote_weapon_pod_destroyed = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd8a92aaa
        spin_death_explosion = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5bf6f8e4
        spin_death_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x85543e4e
        stunned_grapple_block = GrappleBlock.from_stream(data, game, property_size)
    
        return cls(grapple_jet_pack_angle, grapple_stunned_time, stunned_hover_height, stunned_hover_speed, left_remote_weapon_pod_destroyed, right_remote_weapon_pod_destroyed, spin_death_explosion, spin_death_damage, stunned_grapple_block)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\t')  # 9 properties

        data.write(b'\xc6\xe9\xd3\x0e')  # 0xc6e9d30e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grapple_jet_pack_angle))

        data.write(b'\x9e\x9d+\xd6')  # 0x9e9d2bd6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.grapple_stunned_time))

        data.write(b'\xf3\xa7*\xf9')  # 0xf3a72af9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stunned_hover_height))

        data.write(b'\x145[\xe0')  # 0x14355be0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.stunned_hover_speed))

        data.write(b',y\x05,')  # 0x2c79052c
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.left_remote_weapon_pod_destroyed))

        data.write(b'\x01ke\xa9')  # 0x16b65a9
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.right_remote_weapon_pod_destroyed))

        data.write(b'\xd8\xa9*\xaa')  # 0xd8a92aaa
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.spin_death_explosion))

        data.write(b'[\xf6\xf8\xe4')  # 0x5bf6f8e4
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.spin_death_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x85T>N')  # 0x85543e4e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stunned_grapple_block.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FlyingPirateJetPackDataJson", data)
        return cls(
            grapple_jet_pack_angle=json_data['grapple_jet_pack_angle'],
            grapple_stunned_time=json_data['grapple_stunned_time'],
            stunned_hover_height=json_data['stunned_hover_height'],
            stunned_hover_speed=json_data['stunned_hover_speed'],
            left_remote_weapon_pod_destroyed=json_data['left_remote_weapon_pod_destroyed'],
            right_remote_weapon_pod_destroyed=json_data['right_remote_weapon_pod_destroyed'],
            spin_death_explosion=json_data['spin_death_explosion'],
            spin_death_damage=DamageInfo.from_json(json_data['spin_death_damage']),
            stunned_grapple_block=GrappleBlock.from_json(json_data['stunned_grapple_block']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'grapple_jet_pack_angle': self.grapple_jet_pack_angle,
            'grapple_stunned_time': self.grapple_stunned_time,
            'stunned_hover_height': self.stunned_hover_height,
            'stunned_hover_speed': self.stunned_hover_speed,
            'left_remote_weapon_pod_destroyed': self.left_remote_weapon_pod_destroyed,
            'right_remote_weapon_pod_destroyed': self.right_remote_weapon_pod_destroyed,
            'spin_death_explosion': self.spin_death_explosion,
            'spin_death_damage': self.spin_death_damage.to_json(),
            'stunned_grapple_block': self.stunned_grapple_block.to_json(),
        }

    def _dependencies_for_left_remote_weapon_pod_destroyed(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.left_remote_weapon_pod_destroyed)

    def _dependencies_for_right_remote_weapon_pod_destroyed(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.right_remote_weapon_pod_destroyed)

    def _dependencies_for_spin_death_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.spin_death_explosion)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_left_remote_weapon_pod_destroyed, "left_remote_weapon_pod_destroyed", "AssetId"),
            (self._dependencies_for_right_remote_weapon_pod_destroyed, "right_remote_weapon_pod_destroyed", "AssetId"),
            (self._dependencies_for_spin_death_explosion, "spin_death_explosion", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for FlyingPirateJetPackData.{field_name} ({field_type}): {e}"
                )


def _decode_spin_death_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


def _decode_stunned_grapple_block(data: typing.BinaryIO, game: Game, property_size: int) -> GrappleBlock:
    return GrappleBlock.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xc6e9d30e: ('grapple_jet_pack_angle', structs.decode_BIG_f),
    0x9e9d2bd6: ('grapple_stunned_time', structs.decode_BIG_f),
    0xf3a72af9: ('stunned_hover_height', structs.decode_BIG_f),
    0x14355be0: ('stunned_hover_speed', structs.decode_BIG_f),
    0x2c79052c: ('left_remote_weapon_pod_destroyed', structs.decode_BIG_Q),
    0x016b65a9: ('right_remote_weapon_pod_destroyed', structs.decode_BIG_Q),
    0xd8a92aaa: ('spin_death_explosion', structs.decode_BIG_Q),
    0x5bf6f8e4: ('spin_death_damage', _decode_spin_death_damage),
    0x85543e4e: ('stunned_grapple_block', _decode_stunned_grapple_block),
}
