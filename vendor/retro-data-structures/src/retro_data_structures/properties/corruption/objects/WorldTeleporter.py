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
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.core.AnimationParameters import AnimationParameters
from retro_data_structures.properties.corruption.core.AssetId import AssetId, default_asset_id
from retro_data_structures.properties.spline import Spline

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class WorldTeleporterJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        world: int
        area: int
        type: int
        ship: json_util.JsonObject
        camera: json_util.JsonObject
        skybox: int
        optional_model1: json_util.JsonObject
        optional_model1_alpha: json_util.JsonObject
        optional_model2: json_util.JsonObject
        optional_model2_alpha: json_util.JsonObject
        display_font: int
        string: int
        is_fade_white: bool
        character_fade_time: float
        characters_per_second: float
        start_delay: float
        audio_stream: str
        display_subtitles: bool
        end_delay: float
        subtitle_fade_in_delay: float
        subtitle_fade_time: float
        from_skybox: str
        from_ship: json_util.JsonObject
        from_camera: json_util.JsonObject
        to_skybox: str
        to_ship: json_util.JsonObject
        to_camera: json_util.JsonObject
        ship_grapple: int
        transition_sound: int
        volume: float
        pan: float
        transition_sound2: int
        volume2: float
        pan2: float
        unknown: bool
        min_transition_time: float
    

class Type(enum.IntEnum):
    kType_IntraPlanet = 4190668287
    kType_InterPlanet = 3649059742
    kType_TextTeleport = 2346587055
    kType_FromOrbit = 3272497734
    kType_BryyoWarp = 4170916833

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
class WorldTeleporter(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    world: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['MLVL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x31ec14bc, original_name='World'
        ),
    })
    area: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['MREA'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xe0c17804, original_name='Area'
        ),
    })
    type: Type = dataclasses.field(default=Type.kType_IntraPlanet, metadata={
        'reflection': FieldReflection[Type](
            Type, id=0x474bcce3, original_name='Type', from_json=Type.from_json, to_json=Type.to_json
        ),
    })
    ship: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0xa9496551, original_name='Ship', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    camera: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0xbbef4d0d, original_name='Camera', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    skybox: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xccefc618, original_name='Skybox'
        ),
    })
    optional_model1: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0x05014c61, original_name='OptionalModel1', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    optional_model1_alpha: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0xf9ef55d4, original_name='OptionalModel1Alpha', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    optional_model2: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0x3c79e121, original_name='OptionalModel2', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    optional_model2_alpha: Spline = dataclasses.field(default_factory=Spline, metadata={
        'reflection': FieldReflection[Spline](
            Spline, id=0x8e718724, original_name='OptionalModel2Alpha', from_json=Spline.from_json, to_json=Spline.to_json
        ),
    })
    display_font: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['FONT'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x6c176dd6, original_name='DisplayFont'
        ),
    })
    string: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['STRG'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x9182250c, original_name='String'
        ),
    })
    is_fade_white: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xc54082e8, original_name='IsFadeWhite'
        ),
    })
    character_fade_time: float = dataclasses.field(default=0.009999999776482582, metadata={
        'reflection': FieldReflection[float](
            float, id=0xd9b2394f, original_name='CharacterFadeTime'
        ),
    })
    characters_per_second: float = dataclasses.field(default=8.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x353582bd, original_name='CharactersPerSecond'
        ),
    })
    start_delay: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x196e17d9, original_name='StartDelay'
        ),
    })
    audio_stream: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xb28f37b1, original_name='AudioStream'
        ),
    })
    display_subtitles: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0xa1c4e7f8, original_name='DisplaySubtitles'
        ),
    })
    end_delay: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x79cda57c, original_name='EndDelay'
        ),
    })
    subtitle_fade_in_delay: float = dataclasses.field(default=2.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0b5240e3, original_name='SubtitleFadeInDelay'
        ),
    })
    subtitle_fade_time: float = dataclasses.field(default=3.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x71786711, original_name='SubtitleFadeTime'
        ),
    })
    from_skybox: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x2e26702d, original_name='From_Skybox'
        ),
    })
    from_ship: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0x53963a68, original_name='From_Ship', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    from_camera: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0x4ebf760d, original_name='From_Camera', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    to_skybox: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x61930573, original_name='To_Skybox'
        ),
    })
    to_ship: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0x5d7e79a1, original_name='To_Ship', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    to_camera: AnimationParameters = dataclasses.field(default_factory=AnimationParameters, metadata={
        'reflection': FieldReflection[AnimationParameters](
            AnimationParameters, id=0xbb5204c8, original_name='To_Camera', from_json=AnimationParameters.from_json, to_json=AnimationParameters.to_json
        ),
    })
    ship_grapple: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CMDL'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0xb7dcd0ca, original_name='ShipGrapple'
        ),
    })
    transition_sound: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x04d03e41, original_name='TransitionSound'
        ),
    })
    volume: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xc7a7f189, original_name='Volume'
        ),
    })
    pan: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xdf4353a3, original_name='Pan'
        ),
    })
    transition_sound2: AssetId = dataclasses.field(default=default_asset_id, metadata={
        'asset_types': ['CAUD'], 'reflection': FieldReflection[AssetId](
            AssetId, id=0x8dff5674, original_name='TransitionSound2'
        ),
    })
    volume2: float = dataclasses.field(default=1.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x31fa1fe0, original_name='Volume2'
        ),
    })
    pan2: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xea593294, original_name='Pan2'
        ),
    })
    unknown: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x5657ca1c, original_name='Unknown'
        ),
    })
    min_transition_time: float = dataclasses.field(default=5.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xbd6a406d, original_name='MinTransitionTime'
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'TEL1'

    @classmethod
    def modules(cls) -> list[str]:
        return ['RSO_ScriptWorldTeleporter.rso']

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
        if property_count != 37:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x255a4580
        editor_properties = EditorProperties.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x31ec14bc
        world = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe0c17804
        area = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x474bcce3
        type = Type.from_stream(data, game)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa9496551
        ship = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbbef4d0d
        camera = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xccefc618
        skybox = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x05014c61
        optional_model1 = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf9ef55d4
        optional_model1_alpha = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x3c79e121
        optional_model2 = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8e718724
        optional_model2_alpha = Spline.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6c176dd6
        display_font = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9182250c
        string = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc54082e8
        is_fade_white = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd9b2394f
        character_fade_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x353582bd
        characters_per_second = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x196e17d9
        start_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb28f37b1
        audio_stream = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa1c4e7f8
        display_subtitles = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x79cda57c
        end_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0b5240e3
        subtitle_fade_in_delay = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x71786711
        subtitle_fade_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2e26702d
        from_skybox = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x53963a68
        from_ship = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4ebf760d
        from_camera = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x61930573
        to_skybox = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5d7e79a1
        to_ship = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbb5204c8
        to_camera = AnimationParameters.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb7dcd0ca
        ship_grapple = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x04d03e41
        transition_sound = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc7a7f189
        volume = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdf4353a3
        pan = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8dff5674
        transition_sound2 = structs.BIG_Q.unpack(data.read(8))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x31fa1fe0
        volume2 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xea593294
        pan2 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5657ca1c
        unknown = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xbd6a406d
        min_transition_time = structs.BIG_f.unpack(data.read(4))[0]
    
        return cls(editor_properties, world, area, type, ship, camera, skybox, optional_model1, optional_model1_alpha, optional_model2, optional_model2_alpha, display_font, string, is_fade_white, character_fade_time, characters_per_second, start_delay, audio_stream, display_subtitles, end_delay, subtitle_fade_in_delay, subtitle_fade_time, from_skybox, from_ship, from_camera, to_skybox, to_ship, to_camera, ship_grapple, transition_sound, volume, pan, transition_sound2, volume2, pan2, unknown, min_transition_time)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00%')  # 37 properties

        data.write(b'%ZE\x80')  # 0x255a4580
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.editor_properties.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'1\xec\x14\xbc')  # 0x31ec14bc
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.world))

        data.write(b'\xe0\xc1x\x04')  # 0xe0c17804
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.area))

        data.write(b'GK\xcc\xe3')  # 0x474bcce3
        data.write(b'\x00\x04')  # size
        self.type.to_stream(data, game)

        data.write(b'\xa9IeQ')  # 0xa9496551
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ship.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbb\xefM\r')  # 0xbbef4d0d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.camera.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xcc\xef\xc6\x18')  # 0xccefc618
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.skybox))

        data.write(b'\x05\x01La')  # 0x5014c61
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.optional_model1.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf9\xefU\xd4')  # 0xf9ef55d4
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.optional_model1_alpha.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'<y\xe1!')  # 0x3c79e121
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.optional_model2.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8eq\x87$')  # 0x8e718724
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.optional_model2_alpha.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'l\x17m\xd6')  # 0x6c176dd6
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.display_font))

        data.write(b'\x91\x82%\x0c')  # 0x9182250c
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.string))

        data.write(b'\xc5@\x82\xe8')  # 0xc54082e8
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.is_fade_white))

        data.write(b'\xd9\xb29O')  # 0xd9b2394f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.character_fade_time))

        data.write(b'55\x82\xbd')  # 0x353582bd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.characters_per_second))

        data.write(b'\x19n\x17\xd9')  # 0x196e17d9
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.start_delay))

        data.write(b'\xb2\x8f7\xb1')  # 0xb28f37b1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.audio_stream.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa1\xc4\xe7\xf8')  # 0xa1c4e7f8
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.display_subtitles))

        data.write(b'y\xcd\xa5|')  # 0x79cda57c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.end_delay))

        data.write(b'\x0bR@\xe3')  # 0xb5240e3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.subtitle_fade_in_delay))

        data.write(b'qxg\x11')  # 0x71786711
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.subtitle_fade_time))

        data.write(b'.&p-')  # 0x2e26702d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.from_skybox.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'S\x96:h')  # 0x53963a68
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.from_ship.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'N\xbfv\r')  # 0x4ebf760d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.from_camera.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'a\x93\x05s')  # 0x61930573
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.to_skybox.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b']~y\xa1')  # 0x5d7e79a1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.to_ship.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xbbR\x04\xc8')  # 0xbb5204c8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.to_camera.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb7\xdc\xd0\xca')  # 0xb7dcd0ca
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.ship_grapple))

        data.write(b'\x04\xd0>A')  # 0x4d03e41
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.transition_sound))

        data.write(b'\xc7\xa7\xf1\x89')  # 0xc7a7f189
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.volume))

        data.write(b'\xdfCS\xa3')  # 0xdf4353a3
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.pan))

        data.write(b'\x8d\xffVt')  # 0x8dff5674
        data.write(b'\x00\x08')  # size
        data.write(structs.BIG_Q.pack(self.transition_sound2))

        data.write(b'1\xfa\x1f\xe0')  # 0x31fa1fe0
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.volume2))

        data.write(b'\xeaY2\x94')  # 0xea593294
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.pan2))

        data.write(b'VW\xca\x1c')  # 0x5657ca1c
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown))

        data.write(b'\xbdj@m')  # 0xbd6a406d
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.min_transition_time))

        struct_end_offset = data.tell()
        data.seek(root_size_offset)
        data.write(struct.pack(">H", struct_end_offset - root_size_offset - 2))
        data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("WorldTeleporterJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            world=json_data['world'],
            area=json_data['area'],
            type=Type.from_json(json_data['type']),
            ship=AnimationParameters.from_json(json_data['ship']),
            camera=AnimationParameters.from_json(json_data['camera']),
            skybox=json_data['skybox'],
            optional_model1=AnimationParameters.from_json(json_data['optional_model1']),
            optional_model1_alpha=Spline.from_json(json_data['optional_model1_alpha']),
            optional_model2=AnimationParameters.from_json(json_data['optional_model2']),
            optional_model2_alpha=Spline.from_json(json_data['optional_model2_alpha']),
            display_font=json_data['display_font'],
            string=json_data['string'],
            is_fade_white=json_data['is_fade_white'],
            character_fade_time=json_data['character_fade_time'],
            characters_per_second=json_data['characters_per_second'],
            start_delay=json_data['start_delay'],
            audio_stream=json_data['audio_stream'],
            display_subtitles=json_data['display_subtitles'],
            end_delay=json_data['end_delay'],
            subtitle_fade_in_delay=json_data['subtitle_fade_in_delay'],
            subtitle_fade_time=json_data['subtitle_fade_time'],
            from_skybox=json_data['from_skybox'],
            from_ship=AnimationParameters.from_json(json_data['from_ship']),
            from_camera=AnimationParameters.from_json(json_data['from_camera']),
            to_skybox=json_data['to_skybox'],
            to_ship=AnimationParameters.from_json(json_data['to_ship']),
            to_camera=AnimationParameters.from_json(json_data['to_camera']),
            ship_grapple=json_data['ship_grapple'],
            transition_sound=json_data['transition_sound'],
            volume=json_data['volume'],
            pan=json_data['pan'],
            transition_sound2=json_data['transition_sound2'],
            volume2=json_data['volume2'],
            pan2=json_data['pan2'],
            unknown=json_data['unknown'],
            min_transition_time=json_data['min_transition_time'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'world': self.world,
            'area': self.area,
            'type': self.type.to_json(),
            'ship': self.ship.to_json(),
            'camera': self.camera.to_json(),
            'skybox': self.skybox,
            'optional_model1': self.optional_model1.to_json(),
            'optional_model1_alpha': self.optional_model1_alpha.to_json(),
            'optional_model2': self.optional_model2.to_json(),
            'optional_model2_alpha': self.optional_model2_alpha.to_json(),
            'display_font': self.display_font,
            'string': self.string,
            'is_fade_white': self.is_fade_white,
            'character_fade_time': self.character_fade_time,
            'characters_per_second': self.characters_per_second,
            'start_delay': self.start_delay,
            'audio_stream': self.audio_stream,
            'display_subtitles': self.display_subtitles,
            'end_delay': self.end_delay,
            'subtitle_fade_in_delay': self.subtitle_fade_in_delay,
            'subtitle_fade_time': self.subtitle_fade_time,
            'from_skybox': self.from_skybox,
            'from_ship': self.from_ship.to_json(),
            'from_camera': self.from_camera.to_json(),
            'to_skybox': self.to_skybox,
            'to_ship': self.to_ship.to_json(),
            'to_camera': self.to_camera.to_json(),
            'ship_grapple': self.ship_grapple,
            'transition_sound': self.transition_sound,
            'volume': self.volume,
            'pan': self.pan,
            'transition_sound2': self.transition_sound2,
            'volume2': self.volume2,
            'pan2': self.pan2,
            'unknown': self.unknown,
            'min_transition_time': self.min_transition_time,
        }

    def _dependencies_for_skybox(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.skybox)

    def _dependencies_for_display_font(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.display_font)

    def _dependencies_for_string(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.string)

    def _dependencies_for_ship_grapple(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.ship_grapple)

    def _dependencies_for_transition_sound(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.transition_sound)

    def _dependencies_for_transition_sound2(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        return asset_manager.get_dependencies_for_asset(self.transition_sound2)

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.ship.dependencies_for, "ship", "AnimationParameters"),
            (self.camera.dependencies_for, "camera", "AnimationParameters"),
            (self._dependencies_for_skybox, "skybox", "AssetId"),
            (self.optional_model1.dependencies_for, "optional_model1", "AnimationParameters"),
            (self.optional_model2.dependencies_for, "optional_model2", "AnimationParameters"),
            (self._dependencies_for_display_font, "display_font", "AssetId"),
            (self._dependencies_for_string, "string", "AssetId"),
            (self.from_ship.dependencies_for, "from_ship", "AnimationParameters"),
            (self.from_camera.dependencies_for, "from_camera", "AnimationParameters"),
            (self.to_ship.dependencies_for, "to_ship", "AnimationParameters"),
            (self.to_camera.dependencies_for, "to_camera", "AnimationParameters"),
            (self._dependencies_for_ship_grapple, "ship_grapple", "AssetId"),
            (self._dependencies_for_transition_sound, "transition_sound", "AssetId"),
            (self._dependencies_for_transition_sound2, "transition_sound2", "AssetId"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for WorldTeleporter.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_type(data: typing.BinaryIO, game: Game, property_size: int) -> Type:
    return Type.from_stream(data, game)


def _decode_ship(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_camera(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_optional_model1(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_optional_model1_alpha(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_optional_model2(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_optional_model2_alpha(data: typing.BinaryIO, game: Game, property_size: int) -> Spline:
    return Spline.from_stream(data, game, property_size)


def _decode_audio_stream(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_from_skybox(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_from_ship(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_from_camera(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_to_skybox(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_to_ship(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


def _decode_to_camera(data: typing.BinaryIO, game: Game, property_size: int) -> AnimationParameters:
    return AnimationParameters.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0x31ec14bc: ('world', structs.decode_BIG_Q),
    0xe0c17804: ('area', structs.decode_BIG_Q),
    0x474bcce3: ('type', _decode_type),
    0xa9496551: ('ship', _decode_ship),
    0xbbef4d0d: ('camera', _decode_camera),
    0xccefc618: ('skybox', structs.decode_BIG_Q),
    0x05014c61: ('optional_model1', _decode_optional_model1),
    0xf9ef55d4: ('optional_model1_alpha', _decode_optional_model1_alpha),
    0x3c79e121: ('optional_model2', _decode_optional_model2),
    0x8e718724: ('optional_model2_alpha', _decode_optional_model2_alpha),
    0x6c176dd6: ('display_font', structs.decode_BIG_Q),
    0x9182250c: ('string', structs.decode_BIG_Q),
    0xc54082e8: ('is_fade_white', structs.decode_BIG_bool_),
    0xd9b2394f: ('character_fade_time', structs.decode_BIG_f),
    0x353582bd: ('characters_per_second', structs.decode_BIG_f),
    0x196e17d9: ('start_delay', structs.decode_BIG_f),
    0xb28f37b1: ('audio_stream', _decode_audio_stream),
    0xa1c4e7f8: ('display_subtitles', structs.decode_BIG_bool_),
    0x79cda57c: ('end_delay', structs.decode_BIG_f),
    0x0b5240e3: ('subtitle_fade_in_delay', structs.decode_BIG_f),
    0x71786711: ('subtitle_fade_time', structs.decode_BIG_f),
    0x2e26702d: ('from_skybox', _decode_from_skybox),
    0x53963a68: ('from_ship', _decode_from_ship),
    0x4ebf760d: ('from_camera', _decode_from_camera),
    0x61930573: ('to_skybox', _decode_to_skybox),
    0x5d7e79a1: ('to_ship', _decode_to_ship),
    0xbb5204c8: ('to_camera', _decode_to_camera),
    0xb7dcd0ca: ('ship_grapple', structs.decode_BIG_Q),
    0x04d03e41: ('transition_sound', structs.decode_BIG_Q),
    0xc7a7f189: ('volume', structs.decode_BIG_f),
    0xdf4353a3: ('pan', structs.decode_BIG_f),
    0x8dff5674: ('transition_sound2', structs.decode_BIG_Q),
    0x31fa1fe0: ('volume2', structs.decode_BIG_f),
    0xea593294: ('pan2', structs.decode_BIG_f),
    0x5657ca1c: ('unknown', structs.decode_BIG_bool_),
    0xbd6a406d: ('min_transition_time', structs.decode_BIG_f),
}
