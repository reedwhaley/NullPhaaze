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
from retro_data_structures.properties.color import Color
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class ContextActionWeldingDataJson(typing_extensions.TypedDict):
        welding_tip: json_util.JsonObject
        welding_torch: int
        welding_beam: int
        nova_welding_torch: int
        nova_welding_beam: int
        start_weld: int
        inside_collision: int
        outside_collision: int
        part: int
        weld_blobs: int
        weld_shatter: int
        weld_blob_hot_color: json_util.JsonValue
        weld_blob_cold_color: json_util.JsonValue
        weld_torch_sound: int
        weld_beam_sound: int
        inside_weld_sound: int
        outside_weld_sound: int
        unknown: int
        start_weld_sound: int
        weld_succeeded_sound: int
        weld_failed_sound: int
        weld_blob_spacing: float
        welding_good_threshold: float
        welding_break_threshold: float
        welding_time: float
    

@dataclasses.dataclass()
class ContextActionWeldingData(BaseProperty):
    welding_tip: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0x6ade8b91, original_name='WeldingTip', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    welding_torch: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xfbf9569b, original_name='WeldingTorch'
        ),
    })
    welding_beam: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x8e14567b, original_name='WeldingBeam'
        ),
    })
    nova_welding_torch: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xea2c7744, original_name='NovaWeldingTorch'
        ),
    })
    nova_welding_beam: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5a3ed5a0, original_name='NovaWeldingBeam'
        ),
    })
    start_weld: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x70bed427, original_name='StartWeld'
        ),
    })
    inside_collision: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xacd369c1, original_name='InsideCollision'
        ),
    })
    outside_collision: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x1dad13a3, original_name='OutsideCollision'
        ),
    })
    part: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5b468021, original_name='PART'
        ),
    })
    weld_blobs: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xcecad2c3, original_name='WeldBlobs'
        ),
    })
    weld_shatter: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['PART'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x7e542eaa, original_name='WeldShatter'
        ),
    })
    weld_blob_hot_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=0.0, b=0.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0xbface762, original_name='WeldBlobHotColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    weld_blob_cold_color: Color = dataclasses.field(default_factory=lambda: Color(r=1.0, g=1.0, b=1.0, a=0.0), metadata={
        'reflection': FieldReflection[Color](
            Color, id=0x3761c8e8, original_name='WeldBlobColdColor', from_json=Color.from_json, to_json=Color.to_json
        ),
    })
    weld_torch_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x31c8bcaa, original_name='WeldTorchSound'
        ),
    })
    weld_beam_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x1e1a49d5, original_name='WeldBeamSound'
        ),
    })
    inside_weld_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x4a8cf2f7, original_name='InsideWeldSound'
        ),
    })
    outside_weld_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xfbf28895, original_name='OutsideWeldSound'
        ),
    })
    unknown: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x1961d4a5, original_name='Unknown'
        ),
    })
    start_weld_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x1fe966f1, original_name='StartWeldSound'
        ),
    })
    weld_succeeded_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x7dec1aef, original_name='WeldSucceededSound'
        ),
    })
    weld_failed_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb3b5c8cb, original_name='WeldFailedSound'
        ),
    })
    weld_blob_spacing: float = dataclasses.field(default=0.25, metadata={
        'reflection': FieldReflection[float](
            float, id=0x902d66f9, original_name='WeldBlobSpacing'
        ),
    })
    welding_good_threshold: float = dataclasses.field(default=0.4000000059604645, metadata={
        'reflection': FieldReflection[float](
            float, id=0xedf4020e, original_name='WeldingGoodThreshold'
        ),
    })
    welding_break_threshold: float = dataclasses.field(default=100.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x9cf48efc, original_name='WeldingBreakThreshold'
        ),
    })
    welding_time: float = dataclasses.field(default=10.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe698941f, original_name='WeldingTime'
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
        if property_count != 25:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6ade8b91
        welding_tip = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfbf9569b
        welding_torch = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8e14567b
        welding_beam = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xea2c7744
        nova_welding_torch = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5a3ed5a0
        nova_welding_beam = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x70bed427
        start_weld = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xacd369c1
        inside_collision = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1dad13a3
        outside_collision = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5b468021
        part = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcecad2c3
        weld_blobs = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7e542eaa
        weld_shatter = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbface762
        weld_blob_hot_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3761c8e8
        weld_blob_cold_color = Color.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x31c8bcaa
        weld_torch_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1e1a49d5
        weld_beam_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4a8cf2f7
        inside_weld_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfbf28895
        outside_weld_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1961d4a5
        unknown = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1fe966f1
        start_weld_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7dec1aef
        weld_succeeded_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3b5c8cb
        weld_failed_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x902d66f9
        weld_blob_spacing = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xedf4020e
        welding_good_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9cf48efc
        welding_break_threshold = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe698941f
        welding_time = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(welding_tip, welding_torch, welding_beam, nova_welding_torch, nova_welding_beam, start_weld, inside_collision, outside_collision, part, weld_blobs, weld_shatter, weld_blob_hot_color, weld_blob_cold_color, weld_torch_sound, weld_beam_sound, inside_weld_sound, outside_weld_sound, unknown, start_weld_sound, weld_succeeded_sound, weld_failed_sound, weld_blob_spacing, welding_good_threshold, welding_break_threshold, welding_time)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x19')  # 25 properties

        data.write(b'j\xde\x8b\x91')  # 0x6ade8b91
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.welding_tip.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfb\xf9V\x9b')  # 0xfbf9569b
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.welding_torch))

        data.write(b'\x8e\x14V{')  # 0x8e14567b
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.welding_beam))

        data.write(b'\xea,wD')  # 0xea2c7744
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.nova_welding_torch))

        data.write(b'Z>\xd5\xa0')  # 0x5a3ed5a0
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.nova_welding_beam))

        data.write(b"p\xbe\xd4'")  # 0x70bed427
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.start_weld))

        data.write(b'\xac\xd3i\xc1')  # 0xacd369c1
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.inside_collision))

        data.write(b'\x1d\xad\x13\xa3')  # 0x1dad13a3
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.outside_collision))

        data.write(b'[F\x80!')  # 0x5b468021
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.part))

        data.write(b'\xce\xca\xd2\xc3')  # 0xcecad2c3
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.weld_blobs))

        data.write(b'~T.\xaa')  # 0x7e542eaa
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.weld_shatter))

        data.write(b'\xbf\xac\xe7b')  # 0xbface762
        data.write(b'\x00\x10')  # size
        self.weld_blob_hot_color.to_stream(data, game)

        data.write(b'7a\xc8\xe8')  # 0x3761c8e8
        data.write(b'\x00\x10')  # size
        self.weld_blob_cold_color.to_stream(data, game)

        data.write(b'1\xc8\xbc\xaa')  # 0x31c8bcaa
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.weld_torch_sound))

        data.write(b'\x1e\x1aI\xd5')  # 0x1e1a49d5
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.weld_beam_sound))

        data.write(b'J\x8c\xf2\xf7')  # 0x4a8cf2f7
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.inside_weld_sound))

        data.write(b'\xfb\xf2\x88\x95')  # 0xfbf28895
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.outside_weld_sound))

        data.write(b'\x19a\xd4\xa5')  # 0x1961d4a5
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.unknown))

        data.write(b'\x1f\xe9f\xf1')  # 0x1fe966f1
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.start_weld_sound))

        data.write(b'}\xec\x1a\xef')  # 0x7dec1aef
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.weld_succeeded_sound))

        data.write(b'\xb3\xb5\xc8\xcb')  # 0xb3b5c8cb
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.weld_failed_sound))

        data.write(b'\x90-f\xf9')  # 0x902d66f9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.weld_blob_spacing))

        data.write(b'\xed\xf4\x02\x0e')  # 0xedf4020e
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.welding_good_threshold))

        data.write(b'\x9c\xf4\x8e\xfc')  # 0x9cf48efc
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.welding_break_threshold))

        data.write(b'\xe6\x98\x94\x1f')  # 0xe698941f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.welding_time))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ContextActionWeldingDataJson", data)
        return cls(
            welding_tip=AnimationParameters.from_json(json_data['welding_tip']),
            welding_torch=json_data['welding_torch'],
            welding_beam=json_data['welding_beam'],
            nova_welding_torch=json_data['nova_welding_torch'],
            nova_welding_beam=json_data['nova_welding_beam'],
            start_weld=json_data['start_weld'],
            inside_collision=json_data['inside_collision'],
            outside_collision=json_data['outside_collision'],
            part=json_data['part'],
            weld_blobs=json_data['weld_blobs'],
            weld_shatter=json_data['weld_shatter'],
            weld_blob_hot_color=Color.from_json(json_data['weld_blob_hot_color']),
            weld_blob_cold_color=Color.from_json(json_data['weld_blob_cold_color']),
            weld_torch_sound=json_data['weld_torch_sound'],
            weld_beam_sound=json_data['weld_beam_sound'],
            inside_weld_sound=json_data['inside_weld_sound'],
            outside_weld_sound=json_data['outside_weld_sound'],
            unknown=json_data['unknown'],
            start_weld_sound=json_data['start_weld_sound'],
            weld_succeeded_sound=json_data['weld_succeeded_sound'],
            weld_failed_sound=json_data['weld_failed_sound'],
            weld_blob_spacing=json_data['weld_blob_spacing'],
            welding_good_threshold=json_data['welding_good_threshold'],
            welding_break_threshold=json_data['welding_break_threshold'],
            welding_time=json_data['welding_time'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'welding_tip': self.welding_tip.to_json(),
            'welding_torch': self.welding_torch,
            'welding_beam': self.welding_beam,
            'nova_welding_torch': self.nova_welding_torch,
            'nova_welding_beam': self.nova_welding_beam,
            'start_weld': self.start_weld,
            'inside_collision': self.inside_collision,
            'outside_collision': self.outside_collision,
            'part': self.part,
            'weld_blobs': self.weld_blobs,
            'weld_shatter': self.weld_shatter,
            'weld_blob_hot_color': self.weld_blob_hot_color.to_json(),
            'weld_blob_cold_color': self.weld_blob_cold_color.to_json(),
            'weld_torch_sound': self.weld_torch_sound,
            'weld_beam_sound': self.weld_beam_sound,
            'inside_weld_sound': self.inside_weld_sound,
            'outside_weld_sound': self.outside_weld_sound,
            'unknown': self.unknown,
            'start_weld_sound': self.start_weld_sound,
            'weld_succeeded_sound': self.weld_succeeded_sound,
            'weld_failed_sound': self.weld_failed_sound,
            'weld_blob_spacing': self.weld_blob_spacing,
            'welding_good_threshold': self.welding_good_threshold,
            'welding_break_threshold': self.welding_break_threshold,
            'welding_time': self.welding_time,
        }

    def _dependencies_for_welding_torch(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.welding_torch)

    def _dependencies_for_welding_beam(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.welding_beam)

    def _dependencies_for_nova_welding_torch(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.nova_welding_torch)

    def _dependencies_for_nova_welding_beam(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.nova_welding_beam)

    def _dependencies_for_start_weld(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.start_weld)

    def _dependencies_for_inside_collision(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.inside_collision)

    def _dependencies_for_outside_collision(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.outside_collision)

    def _dependencies_for_part(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.part)

    def _dependencies_for_weld_blobs(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.weld_blobs)

    def _dependencies_for_weld_shatter(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.weld_shatter)

    def _dependencies_for_weld_torch_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.weld_torch_sound)

    def _dependencies_for_weld_beam_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.weld_beam_sound)

    def _dependencies_for_inside_weld_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.inside_weld_sound)

    def _dependencies_for_outside_weld_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.outside_weld_sound)

    def _dependencies_for_unknown(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.unknown)

    def _dependencies_for_start_weld_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.start_weld_sound)

    def _dependencies_for_weld_succeeded_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.weld_succeeded_sound)

    def _dependencies_for_weld_failed_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.weld_failed_sound)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.welding_tip.dependencies_for, "welding_tip", "AnimationParameters"),
            (self._dependencies_for_welding_torch, "welding_torch", "AssetId"),
            (self._dependencies_for_welding_beam, "welding_beam", "AssetId"),
            (self._dependencies_for_nova_welding_torch, "nova_welding_torch", "AssetId"),
            (self._dependencies_for_nova_welding_beam, "nova_welding_beam", "AssetId"),
            (self._dependencies_for_start_weld, "start_weld", "AssetId"),
            (self._dependencies_for_inside_collision, "inside_collision", "AssetId"),
            (self._dependencies_for_outside_collision, "outside_collision", "AssetId"),
            (self._dependencies_for_part, "part", "AssetId"),
            (self._dependencies_for_weld_blobs, "weld_blobs", "AssetId"),
            (self._dependencies_for_weld_shatter, "weld_shatter", "AssetId"),
            (self._dependencies_for_weld_torch_sound, "weld_torch_sound", "AssetId"),
            (self._dependencies_for_weld_beam_sound, "weld_beam_sound", "AssetId"),
            (self._dependencies_for_inside_weld_sound, "inside_weld_sound", "AssetId"),
            (self._dependencies_for_outside_weld_sound, "outside_weld_sound", "AssetId"),
            (self._dependencies_for_unknown, "unknown", "AssetId"),
            (self._dependencies_for_start_weld_sound, "start_weld_sound", "AssetId"),
            (self._dependencies_for_weld_succeeded_sound, "weld_succeeded_sound", "AssetId"),
            (self._dependencies_for_weld_failed_sound, "weld_failed_sound", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for ContextActionWeldingData.{field_name} ({field_type}): {e}"
                )


def _decode_welding_tip(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_weld_blob_hot_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


def _decode_weld_blob_cold_color(data: typing.BinaryIO, game: Game, property_size: int) -> Color:
    return Color.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x6ade8b91: ('welding_tip', _decode_welding_tip),
    0xfbf9569b: ('welding_torch', structs.decode_BIG_Q),
    0x8e14567b: ('welding_beam', structs.decode_BIG_Q),
    0xea2c7744: ('nova_welding_torch', structs.decode_BIG_Q),
    0x5a3ed5a0: ('nova_welding_beam', structs.decode_BIG_Q),
    0x70bed427: ('start_weld', structs.decode_BIG_Q),
    0xacd369c1: ('inside_collision', structs.decode_BIG_Q),
    0x1dad13a3: ('outside_collision', structs.decode_BIG_Q),
    0x5b468021: ('part', structs.decode_BIG_Q),
    0xcecad2c3: ('weld_blobs', structs.decode_BIG_Q),
    0x7e542eaa: ('weld_shatter', structs.decode_BIG_Q),
    0xbface762: ('weld_blob_hot_color', _decode_weld_blob_hot_color),
    0x3761c8e8: ('weld_blob_cold_color', _decode_weld_blob_cold_color),
    0x31c8bcaa: ('weld_torch_sound', structs.decode_BIG_Q),
    0x1e1a49d5: ('weld_beam_sound', structs.decode_BIG_Q),
    0x4a8cf2f7: ('inside_weld_sound', structs.decode_BIG_Q),
    0xfbf28895: ('outside_weld_sound', structs.decode_BIG_Q),
    0x1961d4a5: ('unknown', structs.decode_BIG_Q),
    0x1fe966f1: ('start_weld_sound', structs.decode_BIG_Q),
    0x7dec1aef: ('weld_succeeded_sound', structs.decode_BIG_Q),
    0xb3b5c8cb: ('weld_failed_sound', structs.decode_BIG_Q),
    0x902d66f9: ('weld_blob_spacing', structs.decode_BIG_f),
    0xedf4020e: ('welding_good_threshold', structs.decode_BIG_f),
    0x9cf48efc: ('welding_break_threshold', structs.decode_BIG_f),
    0xe698941f: ('welding_time', structs.decode_BIG_f),
}
