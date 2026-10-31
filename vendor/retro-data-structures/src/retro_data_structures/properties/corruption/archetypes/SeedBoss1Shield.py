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

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SeedBoss1ShieldJson(typing_extensions.TypedDict):
        shield_head_1: int
        shield_l_ankle: int
        shield_l_elbow: int
        shield_l_hip: int
        shield_l_knee: int
        shield_l_shoulder: int
        shield_l_wrist: int
        shield_r_ankle: int
        shield_r_elbow: int
        shield_r_hip: int
        shield_r_knee: int
        shield_r_shoulder: int
        shield_r_wrist: int
        shield_spine_1: int
        shield_spine_2: int
    

_FAST_FORMAT: struct.Struct | None = None
_FAST_IDS = (0xdce1a940, 0xf4c318b3, 0xb3673269, 0xb9196d9e, 0x8c0bee98, 0x4d7984e6, 0x8fbe621d, 0x11ea2651, 0x564e0c8b, 0x807edcc5, 0x708b0155, 0xe46803dc, 0x6a975cff, 0x97e2b6c7, 0x1176c469)


@dataclasses.dataclass()
class SeedBoss1Shield(BaseProperty):
    shield_head_1: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xdce1a940, original_name='Shield_head_1'
        ),
    })
    shield_l_ankle: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xf4c318b3, original_name='Shield_l_ankle'
        ),
    })
    shield_l_elbow: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb3673269, original_name='Shield_l_elbow'
        ),
    })
    shield_l_hip: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb9196d9e, original_name='Shield_l_hip'
        ),
    })
    shield_l_knee: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x8c0bee98, original_name='Shield_l_knee'
        ),
    })
    shield_l_shoulder: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x4d7984e6, original_name='Shield_l_shoulder'
        ),
    })
    shield_l_wrist: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x8fbe621d, original_name='Shield_l_wrist'
        ),
    })
    shield_r_ankle: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x11ea2651, original_name='Shield_r_ankle'
        ),
    })
    shield_r_elbow: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x564e0c8b, original_name='Shield_r_elbow'
        ),
    })
    shield_r_hip: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x807edcc5, original_name='Shield_r_hip'
        ),
    })
    shield_r_knee: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x708b0155, original_name='Shield_r_knee'
        ),
    })
    shield_r_shoulder: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe46803dc, original_name='Shield_r_shoulder'
        ),
    })
    shield_r_wrist: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x6a975cff, original_name='Shield_r_wrist'
        ),
    })
    shield_spine_1: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x97e2b6c7, original_name='Shield_spine_1'
        ),
    })
    shield_spine_2: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x1176c469, original_name='Shield_spine_2'
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
        if property_count != 15:
            return None
    
        global _FAST_FORMAT
        if _FAST_FORMAT is None:
            _FAST_FORMAT = struct.Struct('>LHQLHQLHQLHQLHQLHQLHQLHQLHQLHQLHQLHQLHQLHQLHQ')
    
        dec = _FAST_FORMAT.unpack(data.read(210))
        assert (dec[0], dec[3], dec[6], dec[9], dec[12], dec[15], dec[18], dec[21], dec[24], dec[27], dec[30], dec[33], dec[36], dec[39], dec[42]) == _FAST_IDS
        return cls(
            dec[2],
            dec[5],
            dec[8],
            dec[11],
            dec[14],
            dec[17],
            dec[20],
            dec[23],
            dec[26],
            dec[29],
            dec[32],
            dec[35],
            dec[38],
            dec[41],
            dec[44],
        )

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x0f')  # 15 properties

        data.write(b'\xdc\xe1\xa9@')  # 0xdce1a940
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shield_head_1))

        data.write(b'\xf4\xc3\x18\xb3')  # 0xf4c318b3
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shield_l_ankle))

        data.write(b'\xb3g2i')  # 0xb3673269
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shield_l_elbow))

        data.write(b'\xb9\x19m\x9e')  # 0xb9196d9e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shield_l_hip))

        data.write(b'\x8c\x0b\xee\x98')  # 0x8c0bee98
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shield_l_knee))

        data.write(b'My\x84\xe6')  # 0x4d7984e6
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shield_l_shoulder))

        data.write(b'\x8f\xbeb\x1d')  # 0x8fbe621d
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shield_l_wrist))

        data.write(b'\x11\xea&Q')  # 0x11ea2651
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shield_r_ankle))

        data.write(b'VN\x0c\x8b')  # 0x564e0c8b
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shield_r_elbow))

        data.write(b'\x80~\xdc\xc5')  # 0x807edcc5
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shield_r_hip))

        data.write(b'p\x8b\x01U')  # 0x708b0155
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shield_r_knee))

        data.write(b'\xe4h\x03\xdc')  # 0xe46803dc
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shield_r_shoulder))

        data.write(b'j\x97\\\xff')  # 0x6a975cff
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shield_r_wrist))

        data.write(b'\x97\xe2\xb6\xc7')  # 0x97e2b6c7
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shield_spine_1))

        data.write(b'\x11v\xc4i')  # 0x1176c469
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.shield_spine_2))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SeedBoss1ShieldJson", data)
        return cls(
            shield_head_1=json_data['shield_head_1'],
            shield_l_ankle=json_data['shield_l_ankle'],
            shield_l_elbow=json_data['shield_l_elbow'],
            shield_l_hip=json_data['shield_l_hip'],
            shield_l_knee=json_data['shield_l_knee'],
            shield_l_shoulder=json_data['shield_l_shoulder'],
            shield_l_wrist=json_data['shield_l_wrist'],
            shield_r_ankle=json_data['shield_r_ankle'],
            shield_r_elbow=json_data['shield_r_elbow'],
            shield_r_hip=json_data['shield_r_hip'],
            shield_r_knee=json_data['shield_r_knee'],
            shield_r_shoulder=json_data['shield_r_shoulder'],
            shield_r_wrist=json_data['shield_r_wrist'],
            shield_spine_1=json_data['shield_spine_1'],
            shield_spine_2=json_data['shield_spine_2'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'shield_head_1': self.shield_head_1,
            'shield_l_ankle': self.shield_l_ankle,
            'shield_l_elbow': self.shield_l_elbow,
            'shield_l_hip': self.shield_l_hip,
            'shield_l_knee': self.shield_l_knee,
            'shield_l_shoulder': self.shield_l_shoulder,
            'shield_l_wrist': self.shield_l_wrist,
            'shield_r_ankle': self.shield_r_ankle,
            'shield_r_elbow': self.shield_r_elbow,
            'shield_r_hip': self.shield_r_hip,
            'shield_r_knee': self.shield_r_knee,
            'shield_r_shoulder': self.shield_r_shoulder,
            'shield_r_wrist': self.shield_r_wrist,
            'shield_spine_1': self.shield_spine_1,
            'shield_spine_2': self.shield_spine_2,
        }

    def _dependencies_for_shield_head_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_head_1)

    def _dependencies_for_shield_l_ankle(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_l_ankle)

    def _dependencies_for_shield_l_elbow(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_l_elbow)

    def _dependencies_for_shield_l_hip(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_l_hip)

    def _dependencies_for_shield_l_knee(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_l_knee)

    def _dependencies_for_shield_l_shoulder(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_l_shoulder)

    def _dependencies_for_shield_l_wrist(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_l_wrist)

    def _dependencies_for_shield_r_ankle(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_r_ankle)

    def _dependencies_for_shield_r_elbow(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_r_elbow)

    def _dependencies_for_shield_r_hip(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_r_hip)

    def _dependencies_for_shield_r_knee(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_r_knee)

    def _dependencies_for_shield_r_shoulder(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_r_shoulder)

    def _dependencies_for_shield_r_wrist(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_r_wrist)

    def _dependencies_for_shield_spine_1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_spine_1)

    def _dependencies_for_shield_spine_2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.shield_spine_2)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_shield_head_1, "shield_head_1", "AssetId"),
            (self._dependencies_for_shield_l_ankle, "shield_l_ankle", "AssetId"),
            (self._dependencies_for_shield_l_elbow, "shield_l_elbow", "AssetId"),
            (self._dependencies_for_shield_l_hip, "shield_l_hip", "AssetId"),
            (self._dependencies_for_shield_l_knee, "shield_l_knee", "AssetId"),
            (self._dependencies_for_shield_l_shoulder, "shield_l_shoulder", "AssetId"),
            (self._dependencies_for_shield_l_wrist, "shield_l_wrist", "AssetId"),
            (self._dependencies_for_shield_r_ankle, "shield_r_ankle", "AssetId"),
            (self._dependencies_for_shield_r_elbow, "shield_r_elbow", "AssetId"),
            (self._dependencies_for_shield_r_hip, "shield_r_hip", "AssetId"),
            (self._dependencies_for_shield_r_knee, "shield_r_knee", "AssetId"),
            (self._dependencies_for_shield_r_shoulder, "shield_r_shoulder", "AssetId"),
            (self._dependencies_for_shield_r_wrist, "shield_r_wrist", "AssetId"),
            (self._dependencies_for_shield_spine_1, "shield_spine_1", "AssetId"),
            (self._dependencies_for_shield_spine_2, "shield_spine_2", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for SeedBoss1Shield.{field_name} ({field_type}): {e}"
                )


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xdce1a940: ('shield_head_1', structs.decode_BIG_Q),
    0xf4c318b3: ('shield_l_ankle', structs.decode_BIG_Q),
    0xb3673269: ('shield_l_elbow', structs.decode_BIG_Q),
    0xb9196d9e: ('shield_l_hip', structs.decode_BIG_Q),
    0x8c0bee98: ('shield_l_knee', structs.decode_BIG_Q),
    0x4d7984e6: ('shield_l_shoulder', structs.decode_BIG_Q),
    0x8fbe621d: ('shield_l_wrist', structs.decode_BIG_Q),
    0x11ea2651: ('shield_r_ankle', structs.decode_BIG_Q),
    0x564e0c8b: ('shield_r_elbow', structs.decode_BIG_Q),
    0x807edcc5: ('shield_r_hip', structs.decode_BIG_Q),
    0x708b0155: ('shield_r_knee', structs.decode_BIG_Q),
    0xe46803dc: ('shield_r_shoulder', structs.decode_BIG_Q),
    0x6a975cff: ('shield_r_wrist', structs.decode_BIG_Q),
    0x97e2b6c7: ('shield_spine_1', structs.decode_BIG_Q),
    0x1176c469: ('shield_spine_2', structs.decode_BIG_Q),
}
