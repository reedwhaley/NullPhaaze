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
from retro_data_structures.properties.corruption.archetypes.PlasmaBeamInfo import PlasmaBeamInfo
from retro_data_structures.properties.corruption.archetypes.RagDollData import RagDollData
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class BeastRiderDataJson(typing_extensions.TypedDict):
        phazon_lance: int
        phazon_lance_beam: json_util.JsonObject
        helmet: int
        rag_doll_properties: json_util.JsonObject
        death_sound: int
    

@dataclasses.dataclass()
class BeastRiderData(BaseProperty):
    phazon_lance: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb3a26a80, original_name='PhazonLance'
        ),
    })
    phazon_lance_beam: PlasmaBeamInfo = dataclasses.field(default_factory=PlasmaBeamInfo, metadata={
        'reflection': FieldReflection[PlasmaBeamInfo](
            PlasmaBeamInfo, id=0xa6001ce0, original_name='PhazonLanceBeam', from_json=PlasmaBeamInfo.from_json, to_json=PlasmaBeamInfo.to_json
        ),
    })
    helmet: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb3343f83, original_name='Helmet'
        ),
    })
    rag_doll_properties: RagDollData = dataclasses.field(default_factory=RagDollData, metadata={
        'reflection': FieldReflection[RagDollData](
            RagDollData, id=0xa149701e, original_name='RagDollProperties', from_json=RagDollData.from_json, to_json=RagDollData.to_json
        ),
    })
    death_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc7c3f610, original_name='DeathSound'
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
        if property_count != 5:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3a26a80
        phazon_lance = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa6001ce0
        phazon_lance_beam = PlasmaBeamInfo.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3343f83
        helmet = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa149701e
        rag_doll_properties = RagDollData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc7c3f610
        death_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        return cls(phazon_lance, phazon_lance_beam, helmet, rag_doll_properties, death_sound)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x05')  # 5 properties

        data.write(b'\xb3\xa2j\x80')  # 0xb3a26a80
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.phazon_lance))

        data.write(b'\xa6\x00\x1c\xe0')  # 0xa6001ce0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.phazon_lance_beam.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb34?\x83')  # 0xb3343f83
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.helmet))

        data.write(b'\xa1Ip\x1e')  # 0xa149701e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.rag_doll_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc7\xc3\xf6\x10')  # 0xc7c3f610
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.death_sound))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("BeastRiderDataJson", data)
        return cls(
            phazon_lance=json_data['phazon_lance'],
            phazon_lance_beam=PlasmaBeamInfo.from_json(json_data['phazon_lance_beam']),
            helmet=json_data['helmet'],
            rag_doll_properties=RagDollData.from_json(json_data['rag_doll_properties']),
            death_sound=json_data['death_sound'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'phazon_lance': self.phazon_lance,
            'phazon_lance_beam': self.phazon_lance_beam.to_json(),
            'helmet': self.helmet,
            'rag_doll_properties': self.rag_doll_properties.to_json(),
            'death_sound': self.death_sound,
        }

    def _dependencies_for_phazon_lance(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.phazon_lance)

    def _dependencies_for_helmet(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.helmet)

    def _dependencies_for_death_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.death_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_phazon_lance, "phazon_lance", "AssetId"),
            (self.phazon_lance_beam.dependencies_for, "phazon_lance_beam", "PlasmaBeamInfo"),
            (self._dependencies_for_helmet, "helmet", "AssetId"),
            (self.rag_doll_properties.dependencies_for, "rag_doll_properties", "RagDollData"),
            (self._dependencies_for_death_sound, "death_sound", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for BeastRiderData.{field_name} ({field_type}): {e}"
                )


def _decode_phazon_lance_beam(data: typing.BinaryIO, game: Game, property_size: int) -> PlasmaBeamInfo:
    return PlasmaBeamInfo.from_stream(data, game, property_size)


def _decode_rag_doll_properties(data: typing.BinaryIO, game: Game, property_size: int) -> RagDollData:
    return RagDollData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xb3a26a80: ('phazon_lance', structs.decode_BIG_Q),
    0xa6001ce0: ('phazon_lance_beam', _decode_phazon_lance_beam),
    0xb3343f83: ('helmet', structs.decode_BIG_Q),
    0xa149701e: ('rag_doll_properties', _decode_rag_doll_properties),
    0xc7c3f610: ('death_sound', structs.decode_BIG_Q),
}
