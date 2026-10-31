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
from retro_data_structures.properties.corruption.archetypes.ContextActionCombinationLockStruct import ContextActionCombinationLockStruct
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class ContextActionCombinationLockJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        fudge_angle: float
        rotation_scale: float
        movement_distance: float
        movement_time: float
        requires_x_ray: bool
        rotation_sound: int
        push_failure_sound: int
        push_correct_sound: int
        rotation_limit_sound: int
        context_action_combination_lock_struct_0x657d1325: json_util.JsonObject
        context_action_combination_lock_struct_0x5090a576: json_util.JsonObject
        context_action_combination_lock_struct_0xf51b3578: json_util.JsonObject
    

@dataclasses.dataclass()
class ContextActionCombinationLock(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    fudge_angle: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x39bd0f70, original_name='FudgeAngle'
        ),
    })
    rotation_scale: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x5e0ee157, original_name='RotationScale'
        ),
    })
    movement_distance: float = dataclasses.field(default=0.07500000298023224, metadata={
        'reflection': FieldReflection[float](
            float, id=0x1a8a45fe, original_name='MovementDistance'
        ),
    })
    movement_time: float = dataclasses.field(default=1.5, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbb704549, original_name='MovementTime'
        ),
    })
    requires_x_ray: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x61cc15cc, original_name='RequiresXRay'
        ),
    })
    rotation_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd702ebd7, original_name='RotationSound'
        ),
    })
    push_failure_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xc68afc16, original_name='PushFailureSound'
        ),
    })
    push_correct_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x69dbaa2e, original_name='PushCorrectSound'
        ),
    })
    rotation_limit_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x0ed5bc96, original_name='RotationLimitSound'
        ),
    })
    context_action_combination_lock_struct_0x657d1325: ContextActionCombinationLockStruct = dataclasses.field(default_factory=ContextActionCombinationLockStruct, metadata={
        'reflection': FieldReflection[ContextActionCombinationLockStruct](
            ContextActionCombinationLockStruct, id=0x657d1325, original_name='ContextActionCombinationLockStruct', from_json=ContextActionCombinationLockStruct.from_json, to_json=ContextActionCombinationLockStruct.to_json
        ),
    })
    context_action_combination_lock_struct_0x5090a576: ContextActionCombinationLockStruct = dataclasses.field(default_factory=ContextActionCombinationLockStruct, metadata={
        'reflection': FieldReflection[ContextActionCombinationLockStruct](
            ContextActionCombinationLockStruct, id=0x5090a576, original_name='ContextActionCombinationLockStruct', from_json=ContextActionCombinationLockStruct.from_json, to_json=ContextActionCombinationLockStruct.to_json
        ),
    })
    context_action_combination_lock_struct_0xf51b3578: ContextActionCombinationLockStruct = dataclasses.field(default_factory=ContextActionCombinationLockStruct, metadata={
        'reflection': FieldReflection[ContextActionCombinationLockStruct](
            ContextActionCombinationLockStruct, id=0xf51b3578, original_name='ContextActionCombinationLockStruct', from_json=ContextActionCombinationLockStruct.from_json, to_json=ContextActionCombinationLockStruct.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'CACL'

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
        if property_count != 13:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x39bd0f70
        fudge_angle = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5e0ee157
        rotation_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1a8a45fe
        movement_distance = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbb704549
        movement_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x61cc15cc
        requires_x_ray = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd702ebd7
        rotation_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc68afc16
        push_failure_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x69dbaa2e
        push_correct_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0ed5bc96
        rotation_limit_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x657d1325
        context_action_combination_lock_struct_0x657d1325 = ContextActionCombinationLockStruct.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5090a576
        context_action_combination_lock_struct_0x5090a576 = ContextActionCombinationLockStruct.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf51b3578
        context_action_combination_lock_struct_0xf51b3578 = ContextActionCombinationLockStruct.from_stream(data, game, property_size)
    
        return cls(editor_properties, fudge_angle, rotation_scale, movement_distance, movement_time, requires_x_ray, rotation_sound, push_failure_sound, push_correct_sound, rotation_limit_sound, context_action_combination_lock_struct_0x657d1325, context_action_combination_lock_struct_0x5090a576, context_action_combination_lock_struct_0xf51b3578)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\r')  # 13 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'9\xbd\x0fp')  # 0x39bd0f70
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.fudge_angle))

        data.write(b'^\x0e\xe1W')  # 0x5e0ee157
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.rotation_scale))

        data.write(b'\x1a\x8aE\xfe')  # 0x1a8a45fe
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.movement_distance))

        data.write(b'\xbbpEI')  # 0xbb704549
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.movement_time))

        data.write(b'a\xcc\x15\xcc')  # 0x61cc15cc
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.requires_x_ray))

        data.write(b'\xd7\x02\xeb\xd7')  # 0xd702ebd7
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.rotation_sound))

        data.write(b'\xc6\x8a\xfc\x16')  # 0xc68afc16
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.push_failure_sound))

        data.write(b'i\xdb\xaa.')  # 0x69dbaa2e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.push_correct_sound))

        data.write(b'\x0e\xd5\xbc\x96')  # 0xed5bc96
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.rotation_limit_sound))

        data.write(b'e}\x13%')  # 0x657d1325
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.context_action_combination_lock_struct_0x657d1325.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'P\x90\xa5v')  # 0x5090a576
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.context_action_combination_lock_struct_0x5090a576.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf5\x1b5x')  # 0xf51b3578
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.context_action_combination_lock_struct_0xf51b3578.to_stream(data, game)
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
        json_data = typing.cast("ContextActionCombinationLockJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            fudge_angle=json_data['fudge_angle'],
            rotation_scale=json_data['rotation_scale'],
            movement_distance=json_data['movement_distance'],
            movement_time=json_data['movement_time'],
            requires_x_ray=json_data['requires_x_ray'],
            rotation_sound=json_data['rotation_sound'],
            push_failure_sound=json_data['push_failure_sound'],
            push_correct_sound=json_data['push_correct_sound'],
            rotation_limit_sound=json_data['rotation_limit_sound'],
            context_action_combination_lock_struct_0x657d1325=ContextActionCombinationLockStruct.from_json(json_data['context_action_combination_lock_struct_0x657d1325']),
            context_action_combination_lock_struct_0x5090a576=ContextActionCombinationLockStruct.from_json(json_data['context_action_combination_lock_struct_0x5090a576']),
            context_action_combination_lock_struct_0xf51b3578=ContextActionCombinationLockStruct.from_json(json_data['context_action_combination_lock_struct_0xf51b3578']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'fudge_angle': self.fudge_angle,
            'rotation_scale': self.rotation_scale,
            'movement_distance': self.movement_distance,
            'movement_time': self.movement_time,
            'requires_x_ray': self.requires_x_ray,
            'rotation_sound': self.rotation_sound,
            'push_failure_sound': self.push_failure_sound,
            'push_correct_sound': self.push_correct_sound,
            'rotation_limit_sound': self.rotation_limit_sound,
            'context_action_combination_lock_struct_0x657d1325': self.context_action_combination_lock_struct_0x657d1325.to_json(),
            'context_action_combination_lock_struct_0x5090a576': self.context_action_combination_lock_struct_0x5090a576.to_json(),
            'context_action_combination_lock_struct_0xf51b3578': self.context_action_combination_lock_struct_0xf51b3578.to_json(),
        }

    def _dependencies_for_rotation_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.rotation_sound)

    def _dependencies_for_push_failure_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.push_failure_sound)

    def _dependencies_for_push_correct_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.push_correct_sound)

    def _dependencies_for_rotation_limit_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.rotation_limit_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_rotation_sound, "rotation_sound", "AssetId"),
            (self._dependencies_for_push_failure_sound, "push_failure_sound", "AssetId"),
            (self._dependencies_for_push_correct_sound, "push_correct_sound", "AssetId"),
            (self._dependencies_for_rotation_limit_sound, "rotation_limit_sound", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for ContextActionCombinationLock.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_context_action_combination_lock_struct_0x657d1325(data: typing.BinaryIO, game: Game, property_size: int) -> ContextActionCombinationLockStruct:
    return ContextActionCombinationLockStruct.from_stream(data, game, property_size)


def _decode_context_action_combination_lock_struct_0x5090a576(data: typing.BinaryIO, game: Game, property_size: int) -> ContextActionCombinationLockStruct:
    return ContextActionCombinationLockStruct.from_stream(data, game, property_size)


def _decode_context_action_combination_lock_struct_0xf51b3578(data: typing.BinaryIO, game: Game, property_size: int) -> ContextActionCombinationLockStruct:
    return ContextActionCombinationLockStruct.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0x39bd0f70: ('fudge_angle', structs.decode_BIG_f),
    0x5e0ee157: ('rotation_scale', structs.decode_BIG_f),
    0x1a8a45fe: ('movement_distance', structs.decode_BIG_f),
    0xbb704549: ('movement_time', structs.decode_BIG_f),
    0x61cc15cc: ('requires_x_ray', structs.decode_BIG_bool_),
    0xd702ebd7: ('rotation_sound', structs.decode_BIG_Q),
    0xc68afc16: ('push_failure_sound', structs.decode_BIG_Q),
    0x69dbaa2e: ('push_correct_sound', structs.decode_BIG_Q),
    0x0ed5bc96: ('rotation_limit_sound', structs.decode_BIG_Q),
    0x657d1325: ('context_action_combination_lock_struct_0x657d1325', _decode_context_action_combination_lock_struct_0x657d1325),
    0x5090a576: ('context_action_combination_lock_struct_0x5090a576', _decode_context_action_combination_lock_struct_0x5090a576),
    0xf51b3578: ('context_action_combination_lock_struct_0xf51b3578', _decode_context_action_combination_lock_struct_0xf51b3578),
}
