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
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.HealthInfo import HealthInfo
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class FlyingPirateArmorDataJson(typing_extensions.TypedDict):
        has_armor: bool
        armor_health: json_util.JsonObject
        armor_vulnerability: json_util.JsonObject
        head_armor_model: int
        collar_armor_model: int
        left_collar_armor_model: int
        right_collar_armor_model: int
        spine1_armor_model: int
        spine2_armor_model: int
        left_hip_armor_model: int
        right_hip_armor_model: int
        skeleton_root_armor_model: int
    

@dataclasses.dataclass()
class FlyingPirateArmorData(BaseProperty):
    has_armor: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xfde9c4df, original_name='HasArmor'
        ),
    })
    armor_health: HealthInfo = dataclasses.field(default_factory=HealthInfo, metadata={
        'reflection': FieldReflection[HealthInfo](
            HealthInfo, id=0xf18384d4, original_name='ArmorHealth', from_json=HealthInfo.from_json, to_json=HealthInfo.to_json
        ),
    })
    armor_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x896d5bd9, original_name='ArmorVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    head_armor_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x68002bd7, original_name='HeadArmorModel'
        ),
    })
    collar_armor_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xad315c7c, original_name='CollarArmorModel'
        ),
    })
    left_collar_armor_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x042a25ed, original_name='LeftCollarArmorModel'
        ),
    })
    right_collar_armor_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe39b8b1e, original_name='RightCollarArmorModel'
        ),
    })
    spine1_armor_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x356c166a, original_name='Spine1ArmorModel'
        ),
    })
    spine2_armor_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x1ca4a298, original_name='Spine2ArmorModel'
        ),
    })
    left_hip_armor_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xdf44507e, original_name='LeftHipArmorModel'
        ),
    })
    right_hip_armor_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd2c9a656, original_name='RightHipArmorModel'
        ),
    })
    skeleton_root_armor_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd4e26a8e, original_name='SkeletonRootArmorModel'
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
        if property_count != 12:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfde9c4df
        has_armor = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf18384d4
        armor_health = HealthInfo.from_stream(data, game, property_size, default_override={'health': 100.0, 'hi_knock_back_resistance': 5.0})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x896d5bd9
        armor_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68002bd7
        head_armor_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xad315c7c
        collar_armor_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x042a25ed
        left_collar_armor_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe39b8b1e
        right_collar_armor_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x356c166a
        spine1_armor_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1ca4a298
        spine2_armor_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdf44507e
        left_hip_armor_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd2c9a656
        right_hip_armor_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd4e26a8e
        skeleton_root_armor_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        return cls(has_armor, armor_health, armor_vulnerability, head_armor_model, collar_armor_model, left_collar_armor_model, right_collar_armor_model, spine1_armor_model, spine2_armor_model, left_hip_armor_model, right_hip_armor_model, skeleton_root_armor_model)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x0c')  # 12 properties

        data.write(b'\xfd\xe9\xc4\xdf')  # 0xfde9c4df
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.has_armor))

        data.write(b'\xf1\x83\x84\xd4')  # 0xf18384d4
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.armor_health.to_stream(data, game, default_override={'health': 100.0, 'hi_knock_back_resistance': 5.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x89m[\xd9')  # 0x896d5bd9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.armor_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'h\x00+\xd7')  # 0x68002bd7
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.head_armor_model))

        data.write(b'\xad1\\|')  # 0xad315c7c
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.collar_armor_model))

        data.write(b'\x04*%\xed')  # 0x42a25ed
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.left_collar_armor_model))

        data.write(b'\xe3\x9b\x8b\x1e')  # 0xe39b8b1e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.right_collar_armor_model))

        data.write(b'5l\x16j')  # 0x356c166a
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.spine1_armor_model))

        data.write(b'\x1c\xa4\xa2\x98')  # 0x1ca4a298
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.spine2_armor_model))

        data.write(b'\xdfDP~')  # 0xdf44507e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.left_hip_armor_model))

        data.write(b'\xd2\xc9\xa6V')  # 0xd2c9a656
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.right_hip_armor_model))

        data.write(b'\xd4\xe2j\x8e')  # 0xd4e26a8e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.skeleton_root_armor_model))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("FlyingPirateArmorDataJson", data)
        return cls(
            has_armor=json_data['has_armor'],
            armor_health=HealthInfo.from_json(json_data['armor_health']),
            armor_vulnerability=DamageVulnerability.from_json(json_data['armor_vulnerability']),
            head_armor_model=json_data['head_armor_model'],
            collar_armor_model=json_data['collar_armor_model'],
            left_collar_armor_model=json_data['left_collar_armor_model'],
            right_collar_armor_model=json_data['right_collar_armor_model'],
            spine1_armor_model=json_data['spine1_armor_model'],
            spine2_armor_model=json_data['spine2_armor_model'],
            left_hip_armor_model=json_data['left_hip_armor_model'],
            right_hip_armor_model=json_data['right_hip_armor_model'],
            skeleton_root_armor_model=json_data['skeleton_root_armor_model'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'has_armor': self.has_armor,
            'armor_health': self.armor_health.to_json(),
            'armor_vulnerability': self.armor_vulnerability.to_json(),
            'head_armor_model': self.head_armor_model,
            'collar_armor_model': self.collar_armor_model,
            'left_collar_armor_model': self.left_collar_armor_model,
            'right_collar_armor_model': self.right_collar_armor_model,
            'spine1_armor_model': self.spine1_armor_model,
            'spine2_armor_model': self.spine2_armor_model,
            'left_hip_armor_model': self.left_hip_armor_model,
            'right_hip_armor_model': self.right_hip_armor_model,
            'skeleton_root_armor_model': self.skeleton_root_armor_model,
        }

    def _dependencies_for_head_armor_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.head_armor_model)

    def _dependencies_for_collar_armor_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.collar_armor_model)

    def _dependencies_for_left_collar_armor_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.left_collar_armor_model)

    def _dependencies_for_right_collar_armor_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.right_collar_armor_model)

    def _dependencies_for_spine1_armor_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.spine1_armor_model)

    def _dependencies_for_spine2_armor_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.spine2_armor_model)

    def _dependencies_for_left_hip_armor_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.left_hip_armor_model)

    def _dependencies_for_right_hip_armor_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.right_hip_armor_model)

    def _dependencies_for_skeleton_root_armor_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.skeleton_root_armor_model)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_head_armor_model, "head_armor_model", "AssetId"),
            (self._dependencies_for_collar_armor_model, "collar_armor_model", "AssetId"),
            (self._dependencies_for_left_collar_armor_model, "left_collar_armor_model", "AssetId"),
            (self._dependencies_for_right_collar_armor_model, "right_collar_armor_model", "AssetId"),
            (self._dependencies_for_spine1_armor_model, "spine1_armor_model", "AssetId"),
            (self._dependencies_for_spine2_armor_model, "spine2_armor_model", "AssetId"),
            (self._dependencies_for_left_hip_armor_model, "left_hip_armor_model", "AssetId"),
            (self._dependencies_for_right_hip_armor_model, "right_hip_armor_model", "AssetId"),
            (self._dependencies_for_skeleton_root_armor_model, "skeleton_root_armor_model", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for FlyingPirateArmorData.{field_name} ({field_type}): {e}"
                )


def _decode_armor_health(data: typing.BinaryIO, game: Game, property_size: int) -> HealthInfo:
    return HealthInfo.from_stream(data, game, property_size, default_override={'health': 100.0, 'hi_knock_back_resistance': 5.0})


def _decode_armor_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xfde9c4df: ('has_armor', structs.decode_BIG_bool_),
    0xf18384d4: ('armor_health', _decode_armor_health),
    0x896d5bd9: ('armor_vulnerability', _decode_armor_vulnerability),
    0x68002bd7: ('head_armor_model', structs.decode_BIG_Q),
    0xad315c7c: ('collar_armor_model', structs.decode_BIG_Q),
    0x042a25ed: ('left_collar_armor_model', structs.decode_BIG_Q),
    0xe39b8b1e: ('right_collar_armor_model', structs.decode_BIG_Q),
    0x356c166a: ('spine1_armor_model', structs.decode_BIG_Q),
    0x1ca4a298: ('spine2_armor_model', structs.decode_BIG_Q),
    0xdf44507e: ('left_hip_armor_model', structs.decode_BIG_Q),
    0xd2c9a656: ('right_hip_armor_model', structs.decode_BIG_Q),
    0xd4e26a8e: ('skeleton_root_armor_model', structs.decode_BIG_Q),
}
