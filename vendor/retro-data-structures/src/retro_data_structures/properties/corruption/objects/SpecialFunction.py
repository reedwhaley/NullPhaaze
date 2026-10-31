# Generated File
from __future__ import annotations

import dataclasses
import enum
import struct
import typing
import typing_extensions

from retro_data_structures import json_util
from retro_data_structures.game_check import Game
from retro_data_structures.properties import structs
from retro_data_structures.properties.base_property import BaseObjectType
from retro_data_structures.properties.field_reflection import FieldReflection
import retro_data_structures.enums.corruption as enums
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class SpecialFunctionJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        function: int
        string_parm: str
        value_parm: float
        value_parm2: float
        value_parm3: float
        value_parm4: float
        int_parm1: int
        int_parm2: int
        inventory_item_parm: int
        sound1: int
        sound2: int
        sound3: int
        extra_info: int
    

class Function(enum.IntEnum):
    kSF_None = 2563092183
    kSF_AreaAutoLoadController = 240618207
    kSF_AreaDamagePlayer = 1025145004
    kSF_AudioListener = 326062726
    kSF_BossEnergyBar = 923750542
    kSF_CinematicSkip = 696482924
    kSF_CinematicSkipSignal = 1225168693
    kSF_CompletionScreen = 3035969
    kSF_CoreFallDistance = 2662821358
    kSF_DemoTimeoutResetController = 347364662
    kSF_DisableHud = 1986974736
    kSF_DropBomb = 3587238547
    kSF_EndGame = 2114084116
    kSF_EndingActivator = 2285426762
    kSF_EnterLogBookScreen = 346273372
    kSF_EscapeSequenceTrigger = 3153780527
    kSF_ExtraRenderClipPlane = 749815580
    kSF_FlashHudElements = 3486029411
    kSF_FluidSurfaceEvaluator = 3631301918
    kSF_GameStateEnvVarController = 1713293792
    kSF_HUDTarget = 478141611
    kSF_HintController = 2830122522
    kSF_InventoryActivator = 3778572771
    kSF_LaunchPlayer = 2416123537
    kSF_MapStation = 740148357
    kSF_MissileStation = 3053209948
    kSF_ModifyInventoryAmount = 2527813936
    kSF_ModifyInventoryAmountAndCapacity = 1770695450
    kSF_ModifyInventoryCapacity = 2206760967
    kSF_ObjectFollowFluidSurface = 3243946594
    kSF_ObjectFollowJoint = 100545803
    kSF_ObjectFollowLocator = 2552906403
    kSF_ObjectFollowObject = 1937834755
    kSF_OcclusionRelay = 2662250874
    kSF_OverrideArmLighting = 4135506313
    kSF_Function35Unused = 1854158585
    kSF_PlayerAggro = 653498141
    kSF_PlayerFollowLocator = 4285373414
    kSF_PlayerInAreaRelay = 4265730537
    kSF_RadarRangeOverride = 1715427716
    kSF_RechargeStation = 2615468805
    kSF_SamusHelmetOverride = 2023938588
    kSF_SaveStation = 3039339760
    kSF_SetarmorformorphtoGhor = 1993807369
    kSF_SetInventoryAmount = 2401398557
    kSF_SetInventoryAmountAndCapacity = 2471085421
    kSF_SetInventoryCapacity = 1142615654
    kSF_SetInventoryAmountUsingSource = 3847325796
    kSF_SetInventoryAmountAndCapacityUsingSource = 1345026962
    kSF_SetInventoryCapacityUsingSource = 2209351239
    kSF_SkyLighting = 2131551016
    kSF_SkyboxRotate = 1875478250
    kSF_WaypointOverrider = 1385398492
    kSF_PhaazeHypermodeHUDSwitch = 1447080691
    kSF_StaticWorldRenderController = 2123107635
    kSF_SunGeneratorTeleporter = 3621975599
    kSF_SystemStateEnvVarController = 3756334726
    kSF_ViewFrustumTester = 312252864
    kSF_VisorBlowout = 4147516617
    kSF_XRayHUDControl = 3504523875
    kSF_KillPlayer = 507958412
    kSF_NonEnglishSwitch = 387758027
    kSF_CreditsScreen = 3585161948

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


class ExtraInfo(enum.IntEnum):
    kExtraInfo_None = 3424517365
    kExtraInfo_Unknown2 = 3314683043

    @classmethod
    def from_stream(cls, data: typing.BinaryIO, game: Game, size: int | None = None) -> typing_extensions.Self:
        return cls(structs.BIG_L.unpack(data.read(4))[0])

    def to_stream(self, data: typing.BinaryIO, game: Game) -> None:
        data.write(structs.BIG_L.pack(self.value))

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        assert isinstance(data, (int))
        return cls(data)

    def to_json(self) -> int:
        return self.value


@dataclasses.dataclass()
class SpecialFunction(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    function: Function = dataclasses.field(default=Function.kSF_None, metadata={
        'reflection': FieldReflection[Function](
            Function, id=0xb8afcf21, original_name='Function', from_json=Function.from_json, to_json=Function.to_json
        ),
    })
    string_parm: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x9d7a576d, original_name='StringParm'
        ),
    })
    value_parm: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x19028099, original_name='ValueParm'
        ),
    })
    value_parm2: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x2c93aaf5, original_name='ValueParm2'
        ),
    })
    value_parm3: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe7cf7950, original_name='ValueParm3'
        ),
    })
    value_parm4: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xfaca49e8, original_name='ValueParm4'
        ),
    })
    int_parm1: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xa734f8a5, original_name='IntParm1'
        ),
    })
    int_parm2: int = dataclasses.field(default=0, metadata={
        'reflection': FieldReflection[int](
            int, id=0xb581574b, original_name='IntParm2'
        ),
    })
    inventory_item_parm: enums.PlayerItemEnum = dataclasses.field(default=enums.PlayerItemEnum.kItem_PowerBeam, metadata={
        'reflection': FieldReflection[enums.PlayerItemEnum](
            enums.PlayerItemEnum, id=0x3fa164bc, original_name='InventoryItemParm', from_json=enums.PlayerItemEnum.from_json, to_json=enums.PlayerItemEnum.to_json
        ),
    })
    sound1: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x5ecf8f67, original_name='Sound1'
        ),
    })
    sound2: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xd85bfdc9, original_name='Sound2'
        ),
    })
    sound3: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': [], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x13072e6c, original_name='Sound3'
        ),
    })
    extra_info: ExtraInfo = dataclasses.field(default=ExtraInfo.kExtraInfo_None, metadata={
        'reflection': FieldReflection[ExtraInfo](
            ExtraInfo, id=0x825e1e14, original_name='ExtraInfo', from_json=ExtraInfo.from_json, to_json=ExtraInfo.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'SPFN'

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
        if property_count != 14:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb8afcf21
        function = Function.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9d7a576d
        string_parm = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x19028099
        value_parm = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2c93aaf5
        value_parm2 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe7cf7950
        value_parm3 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfaca49e8
        value_parm4 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa734f8a5
        int_parm1 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb581574b
        int_parm2 = structs.BIG_l.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3fa164bc
        inventory_item_parm = enums.PlayerItemEnum.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5ecf8f67
        sound1 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd85bfdc9
        sound2 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x13072e6c
        sound3 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x825e1e14
        extra_info = ExtraInfo.from_stream(data, game)
    
        return cls(editor_properties, function, string_parm, value_parm, value_parm2, value_parm3, value_parm4, int_parm1, int_parm2, inventory_item_parm, sound1, sound2, sound3, extra_info)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x0e')  # 14 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb8\xaf\xcf!')  # 0xb8afcf21
        data.write(b'\x00\x04')  # size
        self.function.to_stream(data, game)

        data.write(b'\x9dzWm')  # 0x9d7a576d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.string_parm.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x19\x02\x80\x99')  # 0x19028099
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.value_parm))

        data.write(b',\x93\xaa\xf5')  # 0x2c93aaf5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.value_parm2))

        data.write(b'\xe7\xcfyP')  # 0xe7cf7950
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.value_parm3))

        data.write(b'\xfa\xcaI\xe8')  # 0xfaca49e8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.value_parm4))

        data.write(b'\xa74\xf8\xa5')  # 0xa734f8a5
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.int_parm1))

        data.write(b'\xb5\x81WK')  # 0xb581574b
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_l.pack(self.int_parm2))

        data.write(b'?\xa1d\xbc')  # 0x3fa164bc
        data.write(b'\x00\x04')  # size
        self.inventory_item_parm.to_stream(data, game)

        data.write(b'^\xcf\x8fg')  # 0x5ecf8f67
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound1))

        data.write(b'\xd8[\xfd\xc9')  # 0xd85bfdc9
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound2))

        data.write(b'\x13\x07.l')  # 0x13072e6c
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.sound3))

        data.write(b'\x82^\x1e\x14')  # 0x825e1e14
        data.write(b'\x00\x04')  # size
        self.extra_info.to_stream(data, game)

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("SpecialFunctionJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            function=Function.from_json(json_data['function']),
            string_parm=json_data['string_parm'],
            value_parm=json_data['value_parm'],
            value_parm2=json_data['value_parm2'],
            value_parm3=json_data['value_parm3'],
            value_parm4=json_data['value_parm4'],
            int_parm1=json_data['int_parm1'],
            int_parm2=json_data['int_parm2'],
            inventory_item_parm=enums.PlayerItemEnum.from_json(json_data['inventory_item_parm']),
            sound1=json_data['sound1'],
            sound2=json_data['sound2'],
            sound3=json_data['sound3'],
            extra_info=ExtraInfo.from_json(json_data['extra_info']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'function': self.function.to_json(),
            'string_parm': self.string_parm,
            'value_parm': self.value_parm,
            'value_parm2': self.value_parm2,
            'value_parm3': self.value_parm3,
            'value_parm4': self.value_parm4,
            'int_parm1': self.int_parm1,
            'int_parm2': self.int_parm2,
            'inventory_item_parm': self.inventory_item_parm.to_json(),
            'sound1': self.sound1,
            'sound2': self.sound2,
            'sound3': self.sound3,
            'extra_info': self.extra_info.to_json(),
        }

    def _dependencies_for_sound1(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound1)

    def _dependencies_for_sound2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound2)

    def _dependencies_for_sound3(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.sound3)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self._dependencies_for_sound1, "sound1", "AssetId"),
            (self._dependencies_for_sound2, "sound2", "AssetId"),
            (self._dependencies_for_sound3, "sound3", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for SpecialFunction.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_function(data: typing.BinaryIO, game: Game, property_size: int) -> Function:
    return Function.from_stream(data, game)


def _decode_string_parm(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_inventory_item_parm(data: typing.BinaryIO, game: Game, property_size: int) -> enums.PlayerItemEnum:
    return enums.PlayerItemEnum.from_stream(data, game)


def _decode_extra_info(data: typing.BinaryIO, game: Game, property_size: int) -> ExtraInfo:
    return ExtraInfo.from_stream(data, game)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0xb8afcf21: ('function', _decode_function),
    0x9d7a576d: ('string_parm', _decode_string_parm),
    0x19028099: ('value_parm', structs.decode_BIG_f),
    0x2c93aaf5: ('value_parm2', structs.decode_BIG_f),
    0xe7cf7950: ('value_parm3', structs.decode_BIG_f),
    0xfaca49e8: ('value_parm4', structs.decode_BIG_f),
    0xa734f8a5: ('int_parm1', structs.decode_BIG_l),
    0xb581574b: ('int_parm2', structs.decode_BIG_l),
    0x3fa164bc: ('inventory_item_parm', _decode_inventory_item_parm),
    0x5ecf8f67: ('sound1', structs.decode_BIG_Q),
    0xd85bfdc9: ('sound2', structs.decode_BIG_Q),
    0x13072e6c: ('sound3', structs.decode_BIG_Q),
    0x825e1e14: ('extra_info', _decode_extra_info),
}
