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
from retro_data_structures.properties.corruption.archetypes.BonusCredit import BonusCredit
from retro_data_structures.properties.corruption.archetypes.SecondaryScanModel import SecondaryScanModel
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class ScannableObjectInfoJson(typing_extensions.TypedDict):
        scan_info_text_string_table: int
        scan_speed: int
        critical: bool
        is_mission_scan: bool
        scan_texture_in_hud: int
        category_icon_static_model: int
        bonus_credit_for_scan: json_util.JsonObject
        model_initial_pitch: float
        model_initial_yaw: float
        model_scale: float
        vertical_adjust: float
        static_model: int
        animated_model: json_util.JsonObject
        attached_model0: json_util.JsonObject
        attached_model1: json_util.JsonObject
        attached_model2: json_util.JsonObject
        attached_model3: json_util.JsonObject
        attached_model4: json_util.JsonObject
        attached_model5: json_util.JsonObject
        attached_model6: json_util.JsonObject
        attached_model7: json_util.JsonObject
        attached_model8: json_util.JsonObject
    

@dataclasses.dataclass()
class ScannableObjectInfo(BaseObjectType):
    scan_info_text_string_table: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['STRG'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x2f5b6423, original_name='ScanInfoTextStringTable'
        ),
    })
    scan_speed: enums.ScanSpeedEnum = dataclasses.field(default=enums.ScanSpeedEnum.Normal, metadata={
        'reflection': FieldReflection[enums.ScanSpeedEnum](
            enums.ScanSpeedEnum, id=0xc308a322, original_name='ScanSpeed', from_json=enums.ScanSpeedEnum.from_json, to_json=enums.ScanSpeedEnum.to_json
        ),
    })
    critical: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x7b714814, original_name='Critical'
        ),
    })
    is_mission_scan: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xd39621a0, original_name='IsMissionScan'
        ),
    })
    scan_texture_in_hud: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['TXTR'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x53336141, original_name='ScanTextureInHud'
        ),
    })
    category_icon_static_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb3b8e67e, original_name='CategoryIconStaticModel'
        ),
    })
    bonus_credit_for_scan: BonusCredit = dataclasses.field(default_factory=BonusCredit, metadata={
        'reflection': FieldReflection[BonusCredit](
            BonusCredit, id=0x1aa8d353, original_name='BonusCreditForScan', from_json=BonusCredit.from_json, to_json=BonusCredit.to_json
        ),
    })
    model_initial_pitch: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x3de0ba64, original_name='ModelInitialPitch'
        ),
    })
    model_initial_yaw: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2add6628, original_name='ModelInitialYaw'
        ),
    })
    model_scale: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd0c15066, original_name='ModelScale'
        ),
    })
    vertical_adjust: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc4c1e212, original_name='VerticalAdjust'
        ),
    })
    static_model: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb7adc418, original_name='StaticModel'
        ),
    })
    animated_model: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0xc4ad00a7, original_name='AnimatedModel', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    attached_model0: SecondaryScanModel = dataclasses.field(default_factory=SecondaryScanModel, metadata={
        'reflection': FieldReflection[SecondaryScanModel](
            SecondaryScanModel, id=0x1065769d, original_name='AttachedModel0', from_json=SecondaryScanModel.from_json, to_json=SecondaryScanModel.to_json
        ),
    })
    attached_model1: SecondaryScanModel = dataclasses.field(default_factory=SecondaryScanModel, metadata={
        'reflection': FieldReflection[SecondaryScanModel](
            SecondaryScanModel, id=0xc787f6c5, original_name='AttachedModel1', from_json=SecondaryScanModel.from_json, to_json=SecondaryScanModel.to_json
        ),
    })
    attached_model2: SecondaryScanModel = dataclasses.field(default_factory=SecondaryScanModel, metadata={
        'reflection': FieldReflection[SecondaryScanModel](
            SecondaryScanModel, id=0x64d1706c, original_name='AttachedModel2', from_json=SecondaryScanModel.from_json, to_json=SecondaryScanModel.to_json
        ),
    })
    attached_model3: SecondaryScanModel = dataclasses.field(default_factory=SecondaryScanModel, metadata={
        'reflection': FieldReflection[SecondaryScanModel](
            SecondaryScanModel, id=0xb333f034, original_name='AttachedModel3', from_json=SecondaryScanModel.from_json, to_json=SecondaryScanModel.to_json
        ),
    })
    attached_model4: SecondaryScanModel = dataclasses.field(default_factory=SecondaryScanModel, metadata={
        'reflection': FieldReflection[SecondaryScanModel](
            SecondaryScanModel, id=0xf90d7b7f, original_name='AttachedModel4', from_json=SecondaryScanModel.from_json, to_json=SecondaryScanModel.to_json
        ),
    })
    attached_model5: SecondaryScanModel = dataclasses.field(default_factory=SecondaryScanModel, metadata={
        'reflection': FieldReflection[SecondaryScanModel](
            SecondaryScanModel, id=0x2eeffb27, original_name='AttachedModel5', from_json=SecondaryScanModel.from_json, to_json=SecondaryScanModel.to_json
        ),
    })
    attached_model6: SecondaryScanModel = dataclasses.field(default_factory=SecondaryScanModel, metadata={
        'reflection': FieldReflection[SecondaryScanModel](
            SecondaryScanModel, id=0x8db97d8e, original_name='AttachedModel6', from_json=SecondaryScanModel.from_json, to_json=SecondaryScanModel.to_json
        ),
    })
    attached_model7: SecondaryScanModel = dataclasses.field(default_factory=SecondaryScanModel, metadata={
        'reflection': FieldReflection[SecondaryScanModel](
            SecondaryScanModel, id=0x5a5bfdd6, original_name='AttachedModel7', from_json=SecondaryScanModel.from_json, to_json=SecondaryScanModel.to_json
        ),
    })
    attached_model8: SecondaryScanModel = dataclasses.field(default_factory=SecondaryScanModel, metadata={
        'reflection': FieldReflection[SecondaryScanModel](
            SecondaryScanModel, id=0x19c46b18, original_name='AttachedModel8', from_json=SecondaryScanModel.from_json, to_json=SecondaryScanModel.to_json
        ),
    })

    def get_name(self) -> str:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    def set_name(self, name: str) -> None:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    @classmethod
    def object_type(cls) -> str:
        return 'SNFO'

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
        if property_count != 22:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2f5b6423
        scan_info_text_string_table = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc308a322
        scan_speed = enums.ScanSpeedEnum.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7b714814
        critical = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd39621a0
        is_mission_scan = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x53336141
        scan_texture_in_hud = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb3b8e67e
        category_icon_static_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1aa8d353
        bonus_credit_for_scan = BonusCredit.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3de0ba64
        model_initial_pitch = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2add6628
        model_initial_yaw = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd0c15066
        model_scale = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc4c1e212
        vertical_adjust = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb7adc418
        static_model = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc4ad00a7
        animated_model = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1065769d
        attached_model0 = SecondaryScanModel.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc787f6c5
        attached_model1 = SecondaryScanModel.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64d1706c
        attached_model2 = SecondaryScanModel.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb333f034
        attached_model3 = SecondaryScanModel.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf90d7b7f
        attached_model4 = SecondaryScanModel.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2eeffb27
        attached_model5 = SecondaryScanModel.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8db97d8e
        attached_model6 = SecondaryScanModel.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5a5bfdd6
        attached_model7 = SecondaryScanModel.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19c46b18
        attached_model8 = SecondaryScanModel.from_stream(data, game, property_size)
    
        return cls(scan_info_text_string_table, scan_speed, critical, is_mission_scan, scan_texture_in_hud, category_icon_static_model, bonus_credit_for_scan, model_initial_pitch, model_initial_yaw, model_scale, vertical_adjust, static_model, animated_model, attached_model0, attached_model1, attached_model2, attached_model3, attached_model4, attached_model5, attached_model6, attached_model7, attached_model8)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x16')  # 22 properties

        data.write(b'/[d#')  # 0x2f5b6423
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.scan_info_text_string_table))

        data.write(b'\xc3\x08\xa3"')  # 0xc308a322
        data.write(b'\x00\x04')  # size
        self.scan_speed.to_stream(data, game)

        data.write(b'{qH\x14')  # 0x7b714814
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.critical))

        data.write(b'\xd3\x96!\xa0')  # 0xd39621a0
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_mission_scan))

        data.write(b'S3aA')  # 0x53336141
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.scan_texture_in_hud))

        data.write(b'\xb3\xb8\xe6~')  # 0xb3b8e67e
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.category_icon_static_model))

        data.write(b'\x1a\xa8\xd3S')  # 0x1aa8d353
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.bonus_credit_for_scan.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'=\xe0\xbad')  # 0x3de0ba64
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.model_initial_pitch))

        data.write(b'*\xddf(')  # 0x2add6628
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.model_initial_yaw))

        data.write(b'\xd0\xc1Pf')  # 0xd0c15066
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.model_scale))

        data.write(b'\xc4\xc1\xe2\x12')  # 0xc4c1e212
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.vertical_adjust))

        data.write(b'\xb7\xad\xc4\x18')  # 0xb7adc418
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.static_model))

        data.write(b'\xc4\xad\x00\xa7')  # 0xc4ad00a7
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.animated_model.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x10ev\x9d')  # 0x1065769d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.attached_model0.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc7\x87\xf6\xc5')  # 0xc787f6c5
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.attached_model1.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'd\xd1pl')  # 0x64d1706c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.attached_model2.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb33\xf04')  # 0xb333f034
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.attached_model3.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf9\r{\x7f')  # 0xf90d7b7f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.attached_model4.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b".\xef\xfb'")  # 0x2eeffb27
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.attached_model5.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8d\xb9}\x8e')  # 0x8db97d8e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.attached_model6.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'Z[\xfd\xd6')  # 0x5a5bfdd6
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.attached_model7.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x19\xc4k\x18')  # 0x19c46b18
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.attached_model8.to_stream(data, game)
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
        json_data = typing.cast("ScannableObjectInfoJson", data)
        return cls(
            scan_info_text_string_table=json_data['scan_info_text_string_table'],
            scan_speed=enums.ScanSpeedEnum.from_json(json_data['scan_speed']),
            critical=json_data['critical'],
            is_mission_scan=json_data['is_mission_scan'],
            scan_texture_in_hud=json_data['scan_texture_in_hud'],
            category_icon_static_model=json_data['category_icon_static_model'],
            bonus_credit_for_scan=BonusCredit.from_json(json_data['bonus_credit_for_scan']),
            model_initial_pitch=json_data['model_initial_pitch'],
            model_initial_yaw=json_data['model_initial_yaw'],
            model_scale=json_data['model_scale'],
            vertical_adjust=json_data['vertical_adjust'],
            static_model=json_data['static_model'],
            animated_model=AnimationParameters.from_json(json_data['animated_model']),
            attached_model0=SecondaryScanModel.from_json(json_data['attached_model0']),
            attached_model1=SecondaryScanModel.from_json(json_data['attached_model1']),
            attached_model2=SecondaryScanModel.from_json(json_data['attached_model2']),
            attached_model3=SecondaryScanModel.from_json(json_data['attached_model3']),
            attached_model4=SecondaryScanModel.from_json(json_data['attached_model4']),
            attached_model5=SecondaryScanModel.from_json(json_data['attached_model5']),
            attached_model6=SecondaryScanModel.from_json(json_data['attached_model6']),
            attached_model7=SecondaryScanModel.from_json(json_data['attached_model7']),
            attached_model8=SecondaryScanModel.from_json(json_data['attached_model8']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'scan_info_text_string_table': self.scan_info_text_string_table,
            'scan_speed': self.scan_speed.to_json(),
            'critical': self.critical,
            'is_mission_scan': self.is_mission_scan,
            'scan_texture_in_hud': self.scan_texture_in_hud,
            'category_icon_static_model': self.category_icon_static_model,
            'bonus_credit_for_scan': self.bonus_credit_for_scan.to_json(),
            'model_initial_pitch': self.model_initial_pitch,
            'model_initial_yaw': self.model_initial_yaw,
            'model_scale': self.model_scale,
            'vertical_adjust': self.vertical_adjust,
            'static_model': self.static_model,
            'animated_model': self.animated_model.to_json(),
            'attached_model0': self.attached_model0.to_json(),
            'attached_model1': self.attached_model1.to_json(),
            'attached_model2': self.attached_model2.to_json(),
            'attached_model3': self.attached_model3.to_json(),
            'attached_model4': self.attached_model4.to_json(),
            'attached_model5': self.attached_model5.to_json(),
            'attached_model6': self.attached_model6.to_json(),
            'attached_model7': self.attached_model7.to_json(),
            'attached_model8': self.attached_model8.to_json(),
        }

    def _dependencies_for_scan_info_text_string_table(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scan_info_text_string_table)

    def _dependencies_for_scan_texture_in_hud(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.scan_texture_in_hud)

    def _dependencies_for_category_icon_static_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.category_icon_static_model)

    def _dependencies_for_static_model(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.static_model)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_scan_info_text_string_table, "scan_info_text_string_table", "AssetId"),
            (self._dependencies_for_scan_texture_in_hud, "scan_texture_in_hud", "AssetId"),
            (self._dependencies_for_category_icon_static_model, "category_icon_static_model", "AssetId"),
            (self._dependencies_for_static_model, "static_model", "AssetId"),
            (self.animated_model.dependencies_for, "animated_model", "AnimationParameters"),
            (self.attached_model0.dependencies_for, "attached_model0", "SecondaryScanModel"),
            (self.attached_model1.dependencies_for, "attached_model1", "SecondaryScanModel"),
            (self.attached_model2.dependencies_for, "attached_model2", "SecondaryScanModel"),
            (self.attached_model3.dependencies_for, "attached_model3", "SecondaryScanModel"),
            (self.attached_model4.dependencies_for, "attached_model4", "SecondaryScanModel"),
            (self.attached_model5.dependencies_for, "attached_model5", "SecondaryScanModel"),
            (self.attached_model6.dependencies_for, "attached_model6", "SecondaryScanModel"),
            (self.attached_model7.dependencies_for, "attached_model7", "SecondaryScanModel"),
            (self.attached_model8.dependencies_for, "attached_model8", "SecondaryScanModel"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for ScannableObjectInfo.{field_name} ({field_type}): {e}"
                )


def _decode_scan_speed(data: typing.BinaryIO, game: Game, property_size: int) -> enums.ScanSpeedEnum:
    return enums.ScanSpeedEnum.from_stream(data, game)


def _decode_bonus_credit_for_scan(data: typing.BinaryIO, game: Game, property_size: int) -> BonusCredit:
    return BonusCredit.from_stream(data, game, property_size)


def _decode_animated_model(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_attached_model0(data: typing.BinaryIO, game: Game, property_size: int) -> SecondaryScanModel:
    return SecondaryScanModel.from_stream(data, game, property_size)


def _decode_attached_model1(data: typing.BinaryIO, game: Game, property_size: int) -> SecondaryScanModel:
    return SecondaryScanModel.from_stream(data, game, property_size)


def _decode_attached_model2(data: typing.BinaryIO, game: Game, property_size: int) -> SecondaryScanModel:
    return SecondaryScanModel.from_stream(data, game, property_size)


def _decode_attached_model3(data: typing.BinaryIO, game: Game, property_size: int) -> SecondaryScanModel:
    return SecondaryScanModel.from_stream(data, game, property_size)


def _decode_attached_model4(data: typing.BinaryIO, game: Game, property_size: int) -> SecondaryScanModel:
    return SecondaryScanModel.from_stream(data, game, property_size)


def _decode_attached_model5(data: typing.BinaryIO, game: Game, property_size: int) -> SecondaryScanModel:
    return SecondaryScanModel.from_stream(data, game, property_size)


def _decode_attached_model6(data: typing.BinaryIO, game: Game, property_size: int) -> SecondaryScanModel:
    return SecondaryScanModel.from_stream(data, game, property_size)


def _decode_attached_model7(data: typing.BinaryIO, game: Game, property_size: int) -> SecondaryScanModel:
    return SecondaryScanModel.from_stream(data, game, property_size)


def _decode_attached_model8(data: typing.BinaryIO, game: Game, property_size: int) -> SecondaryScanModel:
    return SecondaryScanModel.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x2f5b6423: ('scan_info_text_string_table', structs.decode_BIG_Q),
    0xc308a322: ('scan_speed', _decode_scan_speed),
    0x7b714814: ('critical', structs.decode_BIG_bool_),
    0xd39621a0: ('is_mission_scan', structs.decode_BIG_bool_),
    0x53336141: ('scan_texture_in_hud', structs.decode_BIG_Q),
    0xb3b8e67e: ('category_icon_static_model', structs.decode_BIG_Q),
    0x1aa8d353: ('bonus_credit_for_scan', _decode_bonus_credit_for_scan),
    0x3de0ba64: ('model_initial_pitch', structs.decode_BIG_f),
    0x2add6628: ('model_initial_yaw', structs.decode_BIG_f),
    0xd0c15066: ('model_scale', structs.decode_BIG_f),
    0xc4c1e212: ('vertical_adjust', structs.decode_BIG_f),
    0xb7adc418: ('static_model', structs.decode_BIG_Q),
    0xc4ad00a7: ('animated_model', _decode_animated_model),
    0x1065769d: ('attached_model0', _decode_attached_model0),
    0xc787f6c5: ('attached_model1', _decode_attached_model1),
    0x64d1706c: ('attached_model2', _decode_attached_model2),
    0xb333f034: ('attached_model3', _decode_attached_model3),
    0xf90d7b7f: ('attached_model4', _decode_attached_model4),
    0x2eeffb27: ('attached_model5', _decode_attached_model5),
    0x8db97d8e: ('attached_model6', _decode_attached_model6),
    0x5a5bfdd6: ('attached_model7', _decode_attached_model7),
    0x19c46b18: ('attached_model8', _decode_attached_model8),
}
