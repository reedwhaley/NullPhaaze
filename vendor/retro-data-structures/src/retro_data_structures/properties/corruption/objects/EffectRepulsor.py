# Generated File
from __future__ import annotations

import dataclasses
import struct
import typing
import typing_extensions

from retro_data_structures import json_util
from retro_data_structures.game_check import Game
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
import retro_data_structures.enums.corruption as enums
from retro_data_structures.properties.corruption.archetypes.DamageInfo import DamageInfo
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class EffectRepulsorJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        required_item: int
        effect: int
        zap_time: float
        retrigger_time: float
        damage: json_util.JsonObject
    

@dataclasses.dataclass()
class EffectRepulsor(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    required_item: enums.PlayerItemEnum = dataclasses.field(default=enums.PlayerItemEnum.kItem_PowerBeam, metadata={
        'reflection': FieldReflection[enums.PlayerItemEnum](
            enums.PlayerItemEnum, id=0xa169d424, original_name='RequiredItem', from_json=enums.PlayerItemEnum.from_json, to_json=enums.PlayerItemEnum.to_json
        ),
    })
    effect: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb68c6d96, original_name='Effect'
        ),
    })
    zap_time: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x68b0f633, original_name='ZapTime'
        ),
    })
    retrigger_time: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa8e3aff1, original_name='RetriggerTime'
        ),
    })
    damage: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0x337f9524, original_name='Damage', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'EFTR'

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None) -> typing_extensions.Self:
        struct_id, size, property_count = structs.BIG_LHH.unpack(data.read(8))
        assert struct_id == 0xFFFFFFFF
        root_size_start = data.tell() - 2

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

        assert data.tell() - root_size_start == size
        return cls(**present_fields)

    @classmethod
    def _fast_decode(cls, data: typing.BinaryIO, game: Game, property_count: int) -> typing_extensions.Self | None:
        if property_count != 6:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa169d424
        required_item = enums.PlayerItemEnum.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb68c6d96
        effect = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68b0f633
        zap_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa8e3aff1
        retrigger_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x337f9524
        damage = DamageInfo.from_stream(data, game, property_size, default_override={'di_knock_back_power': 1.0})
    
        return cls(editor_properties, required_item, effect, zap_time, retrigger_time, damage)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x06')  # 6 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa1i\xd4$')  # 0xa169d424
        data.write(b'\x00\x04')  # size
        self.required_item.to_stream(data, game)

        data.write(b'\xb6\x8cm\x96')  # 0xb68c6d96
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.effect))

        data.write(b'h\xb0\xf63')  # 0x68b0f633
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.zap_time))

        data.write(b'\xa8\xe3\xaf\xf1')  # 0xa8e3aff1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.retrigger_time))

        data.write(b'3\x7f\x95$')  # 0x337f9524
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage.to_stream(data, game, default_override={'di_knock_back_power': 1.0})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("EffectRepulsorJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            required_item=enums.PlayerItemEnum.from_json(json_data['required_item']),
            effect=json_data['effect'],
            zap_time=json_data['zap_time'],
            retrigger_time=json_data['retrigger_time'],
            damage=DamageInfo.from_json(json_data['damage']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'required_item': self.required_item.to_json(),
            'effect': self.effect,
            'zap_time': self.zap_time,
            'retrigger_time': self.retrigger_time,
            'damage': self.damage.to_json(),
        }

    def _dependencies_for_effect(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.effect)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_effect(asset_manager)


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_required_item(data: typing.BinaryIO, game: Game, property_size: int) -> enums.PlayerItemEnum:
    return enums.PlayerItemEnum.from_stream(data, game)


def _decode_damage(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size, default_override={'di_knock_back_power': 1.0})


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xa169d424: ('required_item', _decode_required_item),
    0xb68c6d96: ('effect', structs.decode_BIG_Q),
    0x68b0f633: ('zap_time', structs.decode_BIG_f),
    0xa8e3aff1: ('retrigger_time', structs.decode_BIG_f),
    0x337f9524: ('damage', _decode_damage),
}
