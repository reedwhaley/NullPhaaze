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
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class EMPulseJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        initial_size: float
        final_size: float
        duration: float
        min_hud_disable_time: float
        max_hud_disable_time: float
        min_hud_disable_amount: float
        max_hud_disable_amount: float
        explosion: int
    

@dataclasses.dataclass()
class EMPulse(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    initial_size: float = dataclasses.field(default=0.10000000149011612, metadata={
        'reflection': FieldReflection[float](
            float, id=0x636df2db, original_name='InitialSize'
        ),
    })
    final_size: float = dataclasses.field(default=34.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1e6686fe, original_name='FinalSize'
        ),
    })
    duration: float = dataclasses.field(default=1.3329999446868896, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8b51e23f, original_name='Duration'
        ),
    })
    min_hud_disable_time: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x96bd6426, original_name='MinHudDisableTime'
        ),
    })
    max_hud_disable_time: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd7aa5ba0, original_name='MaxHudDisableTime'
        ),
    })
    min_hud_disable_amount: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0x15ebb6e9, original_name='MinHudDisableAmount'
        ),
    })
    max_hud_disable_amount: float = dataclasses.field(default=0.800000011920929, metadata={
        'reflection': FieldReflection[float](
            float, id=0xce54e50e, original_name='MaxHudDisableAmount'
        ),
    })
    explosion: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd8c6d15c, original_name='Explosion'
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'EMPU'

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
        if property_count != 9:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size, default_override={'active': False})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x636df2db
        initial_size = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1e6686fe
        final_size = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8b51e23f
        duration = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x96bd6426
        min_hud_disable_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd7aa5ba0
        max_hud_disable_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x15ebb6e9
        min_hud_disable_amount = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xce54e50e
        max_hud_disable_amount = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd8c6d15c
        explosion = structs.BIG_L.unpack(data.read(4))[0]
    
        return cls(editor_properties, initial_size, final_size, duration, min_hud_disable_time, max_hud_disable_time, min_hud_disable_amount, max_hud_disable_amount, explosion)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\t')  # 9 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game, default_override={'active': False})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'cm\xf2\xdb')  # 0x636df2db
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.initial_size))

        data.write(b'\x1ef\x86\xfe')  # 0x1e6686fe
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.final_size))

        data.write(b'\x8bQ\xe2?')  # 0x8b51e23f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.duration))

        data.write(b'\x96\xbdd&')  # 0x96bd6426
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_hud_disable_time))

        data.write(b'\xd7\xaa[\xa0')  # 0xd7aa5ba0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_hud_disable_time))

        data.write(b'\x15\xeb\xb6\xe9')  # 0x15ebb6e9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_hud_disable_amount))

        data.write(b'\xceT\xe5\x0e')  # 0xce54e50e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.max_hud_disable_amount))

        data.write(b'\xd8\xc6\xd1\\')  # 0xd8c6d15c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.explosion))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("EMPulseJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            initial_size=json_data['initial_size'],
            final_size=json_data['final_size'],
            duration=json_data['duration'],
            min_hud_disable_time=json_data['min_hud_disable_time'],
            max_hud_disable_time=json_data['max_hud_disable_time'],
            min_hud_disable_amount=json_data['min_hud_disable_amount'],
            max_hud_disable_amount=json_data['max_hud_disable_amount'],
            explosion=json_data['explosion'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'initial_size': self.initial_size,
            'final_size': self.final_size,
            'duration': self.duration,
            'min_hud_disable_time': self.min_hud_disable_time,
            'max_hud_disable_time': self.max_hud_disable_time,
            'min_hud_disable_amount': self.min_hud_disable_amount,
            'max_hud_disable_amount': self.max_hud_disable_amount,
            'explosion': self.explosion,
        }

    def _dependencies_for_explosion(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.explosion)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return self._dependencies_for_explosion(asset_manager)


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={'active': False})


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0x636df2db: ('initial_size', structs.decode_BIG_f),
    0x1e6686fe: ('final_size', structs.decode_BIG_f),
    0x8b51e23f: ('duration', structs.decode_BIG_f),
    0x96bd6426: ('min_hud_disable_time', structs.decode_BIG_f),
    0xd7aa5ba0: ('max_hud_disable_time', structs.decode_BIG_f),
    0x15ebb6e9: ('min_hud_disable_amount', structs.decode_BIG_f),
    0xce54e50e: ('max_hud_disable_amount', structs.decode_BIG_f),
    0xd8c6d15c: ('explosion', structs.decode_BIG_L),
}
