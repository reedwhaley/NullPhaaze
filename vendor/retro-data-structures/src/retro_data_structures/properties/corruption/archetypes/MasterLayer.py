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
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
import uuid

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class MasterLayerJson(typing_extensions.TypedDict):
        area_id: int
        layer_id: str
    

def _from_json_layer_id(data: json_util.JsonValue) -> uuid.UUID:
    json_data = typing.cast(str, data)
    return uuid.UUID(json_data)


def _to_json_layer_id(obj: uuid.UUID) -> json_util.JsonValue:
    return str(obj)


@dataclasses.dataclass()
class MasterLayer(BaseProperty):
    area_id: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x00000000, original_name='AreaId'
        ),
    })
    layer_id: uuid.UUID = dataclasses.field(default_factory=lambda: uuid.UUID(int=0), metadata={
        'reflection': FieldReflection[uuid.UUID](
            uuid.UUID, id=0x00000001, original_name='LayerId', from_json=_from_json_layer_id, to_json=_to_json_layer_id
        ),
    })

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None, default_override: dict | None = None) -> typing_extensions.Self:
        property_size = None  # Atomic
        area_id = structs.BIG_Q.unpack(data.read(8))[0]
        layer_id = uuid.UUID(bytes=data.read(16))
        return cls(area_id, layer_id)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(structs.BIG_Q.pack(self.area_id))
        data.write(self.layer_id.bytes)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("MasterLayerJson", data)
        return cls(
            area_id=json_data['area_id'],
            layer_id=uuid.UUID(json_data['layer_id']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'area_id': self.area_id,
            'layer_id': str(self.layer_id),
        }

    def _dependencies_for_area_id(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.area_id)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_area_id(asset_manager)
