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
from retro_data_structures.properties.corruption.archetypes.GhorWeakSpotData import GhorWeakSpotData

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class GhorShieldDataJson(typing_extensions.TypedDict):
        force_disable: bool
        attachment: json_util.JsonObject
        damage_info: json_util.JsonObject
    

@dataclasses.dataclass()
class GhorShieldData(BaseProperty):
    force_disable: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xa8d0ee16, original_name='ForceDisable'
        ),
    })
    attachment: GhorWeakSpotData = dataclasses.field(default_factory=GhorWeakSpotData, metadata={
        'reflection': FieldReflection[GhorWeakSpotData](
            GhorWeakSpotData, id=0xa82b5daa, original_name='Attachment', from_json=GhorWeakSpotData.from_json, to_json=GhorWeakSpotData.to_json
        ),
    })
    damage_info: DamageInfo = dataclasses.field(default_factory=DamageInfo, metadata={
        'reflection': FieldReflection[DamageInfo](
            DamageInfo, id=0xc97013d0, original_name='DamageInfo', from_json=DamageInfo.from_json, to_json=DamageInfo.to_json
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
        if property_count != 3:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa8d0ee16
        force_disable = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa82b5daa
        attachment = GhorWeakSpotData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc97013d0
        damage_info = DamageInfo.from_stream(data, game, property_size)
    
        return cls(force_disable, attachment, damage_info)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x03')  # 3 properties

        data.write(b'\xa8\xd0\xee\x16')  # 0xa8d0ee16
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.force_disable))

        data.write(b'\xa8+]\xaa')  # 0xa82b5daa
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.attachment.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc9p\x13\xd0')  # 0xc97013d0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.damage_info.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("GhorShieldDataJson", data)
        return cls(
            force_disable=json_data['force_disable'],
            attachment=GhorWeakSpotData.from_json(json_data['attachment']),
            damage_info=DamageInfo.from_json(json_data['damage_info']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'force_disable': self.force_disable,
            'attachment': self.attachment.to_json(),
            'damage_info': self.damage_info.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self.attachment.dependencies_for(asset_manager)


def _decode_attachment(data: typing.BinaryIO, game: Game, property_size: int) -> GhorWeakSpotData:
    return GhorWeakSpotData.from_stream(data, game, property_size)


def _decode_damage_info(data: typing.BinaryIO, game: Game, property_size: int) -> DamageInfo:
    return DamageInfo.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xa8d0ee16: ('force_disable', structs.decode_BIG_bool_),
    0xa82b5daa: ('attachment', _decode_attachment),
    0xc97013d0: ('damage_info', _decode_damage_info),
}
