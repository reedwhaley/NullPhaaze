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
from retro_data_structures.properties.echoes.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class EmperorIngStage1WarpAttackDataJson(typing_extensions.TypedDict):
        portal_effect: int
        attack_tip: json_util.JsonObject
        stab_damage: json_util.JsonObject
        tentacle_enter_portal_sound: int
        tentacle_exit_portal_sound: int
        tentacle_portal_open_sound: int
        tentacle_portal_close_sound: int
    

@dataclasses.dataclass()
class EmperorIngStage1WarpAttackData(BaseProperty):
    portal_effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x4a7c4ec2, original_name='PortalEffect'
        ),
    })
    attack_tip: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0xf10b6ef6, original_name='AttackTip', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    stab_damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x946016a9, original_name='StabDamage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })
    tentacle_enter_portal_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xecfab026, original_name='TentacleEnterPortalSound'
        ),
    })
    tentacle_exit_portal_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x94880277, original_name='TentacleExitPortalSound'
        ),
    })
    tentacle_portal_open_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x1c3e84b6, original_name='TentaclePortalOpenSound'
        ),
    })
    tentacle_portal_close_sound: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xa93f0198, original_name='TentaclePortalCloseSound'
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
        assert property_id == 0x4a7c4ec2
        portal_effect = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf10b6ef6
        attack_tip = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x946016a9
        stab_damage = DamageInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xecfab026
        tentacle_enter_portal_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x94880277
        tentacle_exit_portal_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1c3e84b6
        tentacle_portal_open_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa93f0198
        tentacle_portal_close_sound = structs.BIG_l.unpack(data.read(4))[0]
    
        return cls(portal_effect, attack_tip, stab_damage, tentacle_enter_portal_sound, tentacle_exit_portal_sound, tentacle_portal_open_sound, tentacle_portal_close_sound)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x07')  # 7 properties

        data.write(b'J|N\xc2')  # 0x4a7c4ec2
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.portal_effect))

        data.write(b'\xf1\x0bn\xf6')  # 0xf10b6ef6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.attack_tip.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x94`\x16\xa9')  # 0x946016a9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.stab_damage.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xec\xfa\xb0&')  # 0xecfab026
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.tentacle_enter_portal_sound))

        data.write(b'\x94\x88\x02w')  # 0x94880277
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.tentacle_exit_portal_sound))

        data.write(b'\x1c>\x84\xb6')  # 0x1c3e84b6
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.tentacle_portal_open_sound))

        data.write(b'\xa9?\x01\x98')  # 0xa93f0198
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.tentacle_portal_close_sound))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("EmperorIngStage1WarpAttackDataJson", data)
        return cls(
            portal_effect=json_data['portal_effect'],
            attack_tip=AnimationParameters.from_json(json_data['attack_tip']),
            stab_damage=DamageInfo.from_json(json_data['stab_damage']),
            tentacle_enter_portal_sound=json_data['tentacle_enter_portal_sound'],
            tentacle_exit_portal_sound=json_data['tentacle_exit_portal_sound'],
            tentacle_portal_open_sound=json_data['tentacle_portal_open_sound'],
            tentacle_portal_close_sound=json_data['tentacle_portal_close_sound'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'portal_effect': self.portal_effect,
            'attack_tip': self.attack_tip.to_json(),
            'stab_damage': self.stab_damage.to_json(),
            'tentacle_enter_portal_sound': self.tentacle_enter_portal_sound,
            'tentacle_exit_portal_sound': self.tentacle_exit_portal_sound,
            'tentacle_portal_open_sound': self.tentacle_portal_open_sound,
            'tentacle_portal_close_sound': self.tentacle_portal_close_sound,
        }

    def _dependencies_for_portal_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.portal_effect)

    def _dependencies_for_tentacle_enter_portal_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.tentacle_enter_portal_sound)

    def _dependencies_for_tentacle_exit_portal_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.tentacle_exit_portal_sound)

    def _dependencies_for_tentacle_portal_open_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.tentacle_portal_open_sound)

    def _dependencies_for_tentacle_portal_close_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.tentacle_portal_close_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_portal_effect, "portal_effect", "AssetId"),
            (self.attack_tip.dependencies_for, "attack_tip", "AnimationParameters"),
            (self._dependencies_for_tentacle_enter_portal_sound, "tentacle_enter_portal_sound", "int"),
            (self._dependencies_for_tentacle_exit_portal_sound, "tentacle_exit_portal_sound", "int"),
            (self._dependencies_for_tentacle_portal_open_sound, "tentacle_portal_open_sound", "int"),
            (self._dependencies_for_tentacle_portal_close_sound, "tentacle_portal_close_sound", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for EmperorIngStage1WarpAttackData.{field_name} ({field_type}): {e}"
                )


def _decode_attack_tip(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_stab_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x4a7c4ec2: ('portal_effect', structs.decode_BIG_L),
    0xf10b6ef6: ('attack_tip', _decode_attack_tip),
    0x946016a9: ('stab_damage', _decode_stab_damage),
    0xecfab026: ('tentacle_enter_portal_sound', structs.decode_BIG_l),
    0x94880277: ('tentacle_exit_portal_sound', structs.decode_BIG_l),
    0x1c3e84b6: ('tentacle_portal_open_sound', structs.decode_BIG_l),
    0xa93f0198: ('tentacle_portal_close_sound', structs.decode_BIG_l),
}
