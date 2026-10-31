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
from retro_data_structures.properties.echoes.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.echoes.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.vector import Vector

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class PortalTransitionJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        animation_information: json_util.JsonObject
        player_scale: json_util.JsonValue
        volume: int
        pan: int
        portal_sound_group_common: int
        portal_sound_group_directional: int
        start_portal: int
        in_portal1: int
        in_portal2: int
        direction: int
    

@dataclasses.dataclass()
class PortalTransition(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    animation_information: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0xe25fb08c, original_name='AnimationInformation', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    player_scale: Vector = dataclasses.field(default_factory=lambda: Vector(x=1.0, y=1.0, z=1.0), metadata={
        'reflection': FieldReflection[Vector](
            Vector, id=0xe56ba365, original_name='PlayerScale', from_json=Vector.from_json, to_json=Vector.to_json
        ),
    })
    volume: int = dataclasses.field(default=127, metadata={
        'reflection': FieldReflection[int](
            int, id=0x80c66c37, original_name='Volume'
        ),
    })
    pan: int = dataclasses.field(default=64, metadata={
        'reflection': FieldReflection[int](
            int, id=0xd6088bc5, original_name='Pan'
        ),
    })
    portal_sound_group_common: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['AGSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe08e2172, original_name='PortalSoundGroupCommon'
        ),
    })
    portal_sound_group_directional: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['AGSC'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb3e6c4e3, original_name='PortalSoundGroupDirectional'
        ),
    })
    start_portal: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x508520e1, original_name='StartPortal'
        ),
    })
    in_portal1: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0x34c7c1cc, original_name='InPortal1'
        ),
    })
    in_portal2: int = dataclasses.field(default=-1, metadata={
        'sound': True, 'reflection': FieldReflection[int](
            int, id=0xb253b362, original_name='InPortal2'
        ),
    })
    direction: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0x4406dc02, original_name='Direction'
        ),
    })  # Choice

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'PRTT'

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
        if property_count != 11:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe25fb08c
        animation_information = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe56ba365
        player_scale = Vector.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x80c66c37
        volume = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd6088bc5
        pan = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe08e2172
        portal_sound_group_common = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3e6c4e3
        portal_sound_group_directional = structs.BIG_L.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x508520e1
        start_portal = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x34c7c1cc
        in_portal1 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb253b362
        in_portal2 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4406dc02
        direction = structs.BIG_L.unpack(data.read(4))[0]
    
        return cls(editor_properties, animation_information, player_scale, volume, pan, portal_sound_group_common, portal_sound_group_directional, start_portal, in_portal1, in_portal2, direction)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x0b')  # 11 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game, default_override={'misc_flags': 3})
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe2_\xb0\x8c')  # 0xe25fb08c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.animation_information.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe5k\xa3e')  # 0xe56ba365
        data.write(b'\x00\x0c')  # size
        self.player_scale.to_stream(data, game)

        data.write(b'\x80\xc6l7')  # 0x80c66c37
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.volume))

        data.write(b'\xd6\x08\x8b\xc5')  # 0xd6088bc5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.pan))

        data.write(b'\xe0\x8e!r')  # 0xe08e2172
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.portal_sound_group_common))

        data.write(b'\xb3\xe6\xc4\xe3')  # 0xb3e6c4e3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.portal_sound_group_directional))

        data.write(b'P\x85 \xe1')  # 0x508520e1
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.start_portal))

        data.write(b'4\xc7\xc1\xcc')  # 0x34c7c1cc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.in_portal1))

        data.write(b'\xb2S\xb3b')  # 0xb253b362
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.in_portal2))

        data.write(b'D\x06\xdc\x02')  # 0x4406dc02
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_L.pack(self.direction))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("PortalTransitionJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            animation_information=AnimationParameters.from_json(json_data['animation_information']),
            player_scale=Vector.from_json(json_data['player_scale']),
            volume=json_data['volume'],
            pan=json_data['pan'],
            portal_sound_group_common=json_data['portal_sound_group_common'],
            portal_sound_group_directional=json_data['portal_sound_group_directional'],
            start_portal=json_data['start_portal'],
            in_portal1=json_data['in_portal1'],
            in_portal2=json_data['in_portal2'],
            direction=json_data['direction'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'animation_information': self.animation_information.to_json(),
            'player_scale': self.player_scale.to_json(),
            'volume': self.volume,
            'pan': self.pan,
            'portal_sound_group_common': self.portal_sound_group_common,
            'portal_sound_group_directional': self.portal_sound_group_directional,
            'start_portal': self.start_portal,
            'in_portal1': self.in_portal1,
            'in_portal2': self.in_portal2,
            'direction': self.direction,
        }

    def _dependencies_for_portal_sound_group_common(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.portal_sound_group_common)

    def _dependencies_for_portal_sound_group_directional(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.portal_sound_group_directional)

    def _dependencies_for_start_portal(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.start_portal)

    def _dependencies_for_in_portal1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.in_portal1)

    def _dependencies_for_in_portal2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_audio_group_dependency(self.in_portal2)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.animation_information.dependencies_for, "animation_information", "AnimationParameters"),
            (self._dependencies_for_portal_sound_group_common, "portal_sound_group_common", "AssetId"),
            (self._dependencies_for_portal_sound_group_directional, "portal_sound_group_directional", "AssetId"),
            (self._dependencies_for_start_portal, "start_portal", "int"),
            (self._dependencies_for_in_portal1, "in_portal1", "int"),
            (self._dependencies_for_in_portal2, "in_portal2", "int"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for PortalTransition.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size, default_override={'misc_flags': 3})


def _decode_animation_information(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_player_scale(data: typing.BinaryIO, game: Game, property_size: int) -> Vector:
    return Vector.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xe25fb08c: ('animation_information', _decode_animation_information),
    0xe56ba365: ('player_scale', _decode_player_scale),
    0x80c66c37: ('volume', structs.decode_BIG_l),
    0xd6088bc5: ('pan', structs.decode_BIG_l),
    0xe08e2172: ('portal_sound_group_common', structs.decode_BIG_L),
    0xb3e6c4e3: ('portal_sound_group_directional', structs.decode_BIG_L),
    0x508520e1: ('start_portal', structs.decode_BIG_l),
    0x34c7c1cc: ('in_portal1', structs.decode_BIG_l),
    0xb253b362: ('in_portal2', structs.decode_BIG_l),
    0x4406dc02: ('direction', structs.decode_BIG_L),
}
