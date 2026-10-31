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
from retro_data_structures.properties.corruption.archetypes.TweakGuiColors_HUDColorsTypedef import TweakGuiColors_HUDColorsTypedef
from retro_data_structures.properties.corruption.archetypes.TweakGuiColors_Misc import TweakGuiColors_Misc
from retro_data_structures.properties.common.archetypes.TweakGuiColors_Multiplayer import TweakGuiColors_Multiplayer
from retro_data_structures.properties.common.archetypes.TweakGuiColors_TurretHudTypedef import TweakGuiColors_TurretHudTypedef
from retro_data_structures.properties.corruption.archetypes.TweakGui_HudColorTypedef import TweakGui_HudColorTypedef
from retro_data_structures.properties.common.archetypes.TweakGui_VisorColorSchemeTypedef import TweakGui_VisorColorSchemeTypedef

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class TweakGuiColorsJson(typing_extensions.TypedDict):
        instance_name: str
        hud_colors: json_util.JsonObject
        misc: json_util.JsonObject
        multiplayer: json_util.JsonObject
        combat_hud_color_scheme: json_util.JsonObject
        command_hud_color_scheme: json_util.JsonObject
        scan_hud_color_scheme: json_util.JsonObject
        x_ray_hud_color_scheme: json_util.JsonObject
        ball_hud_color_scheme: json_util.JsonObject
        hypermode_hud_color_scheme: json_util.JsonObject
        combat_hud: json_util.JsonObject
        command_hud: json_util.JsonObject
        scan_hud: json_util.JsonObject
        x_ray_hud: json_util.JsonObject
        ball_hud: json_util.JsonObject
        turret_hud: json_util.JsonObject
    

@dataclasses.dataclass()
class TweakGuiColors(BaseObjectType):
    instance_name: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x7fda1466, original_name='InstanceName'
        ),
    })
    hud_colors: TweakGuiColors_HUDColorsTypedef = dataclasses.field(default_factory=TweakGuiColors_HUDColorsTypedef, metadata={
        'reflection': FieldReflection[TweakGuiColors_HUDColorsTypedef](
            TweakGuiColors_HUDColorsTypedef, id=0xcb737724, original_name='HUDColors', from_json=TweakGuiColors_HUDColorsTypedef.from_json, to_json=TweakGuiColors_HUDColorsTypedef.to_json
        ),
    })
    misc: TweakGuiColors_Misc = dataclasses.field(default_factory=TweakGuiColors_Misc, metadata={
        'reflection': FieldReflection[TweakGuiColors_Misc](
            TweakGuiColors_Misc, id=0x6756d4de, original_name='Misc', from_json=TweakGuiColors_Misc.from_json, to_json=TweakGuiColors_Misc.to_json
        ),
    })
    multiplayer: TweakGuiColors_Multiplayer = dataclasses.field(default_factory=TweakGuiColors_Multiplayer, metadata={
        'reflection': FieldReflection[TweakGuiColors_Multiplayer](
            TweakGuiColors_Multiplayer, id=0x697613e9, original_name='Multiplayer', from_json=TweakGuiColors_Multiplayer.from_json, to_json=TweakGuiColors_Multiplayer.to_json
        ),
    })
    combat_hud_color_scheme: TweakGui_VisorColorSchemeTypedef = dataclasses.field(default_factory=TweakGui_VisorColorSchemeTypedef, metadata={
        'reflection': FieldReflection[TweakGui_VisorColorSchemeTypedef](
            TweakGui_VisorColorSchemeTypedef, id=0x67c70055, original_name='CombatHudColorScheme', from_json=TweakGui_VisorColorSchemeTypedef.from_json, to_json=TweakGui_VisorColorSchemeTypedef.to_json
        ),
    })
    command_hud_color_scheme: TweakGui_VisorColorSchemeTypedef = dataclasses.field(default_factory=TweakGui_VisorColorSchemeTypedef, metadata={
        'reflection': FieldReflection[TweakGui_VisorColorSchemeTypedef](
            TweakGui_VisorColorSchemeTypedef, id=0x2fecaabd, original_name='CommandHudColorScheme', from_json=TweakGui_VisorColorSchemeTypedef.from_json, to_json=TweakGui_VisorColorSchemeTypedef.to_json
        ),
    })
    scan_hud_color_scheme: TweakGui_VisorColorSchemeTypedef = dataclasses.field(default_factory=TweakGui_VisorColorSchemeTypedef, metadata={
        'reflection': FieldReflection[TweakGui_VisorColorSchemeTypedef](
            TweakGui_VisorColorSchemeTypedef, id=0x80becd6e, original_name='ScanHudColorScheme', from_json=TweakGui_VisorColorSchemeTypedef.from_json, to_json=TweakGui_VisorColorSchemeTypedef.to_json
        ),
    })
    x_ray_hud_color_scheme: TweakGui_VisorColorSchemeTypedef = dataclasses.field(default_factory=TweakGui_VisorColorSchemeTypedef, metadata={
        'reflection': FieldReflection[TweakGui_VisorColorSchemeTypedef](
            TweakGui_VisorColorSchemeTypedef, id=0x34e0e988, original_name='XRayHudColorScheme', from_json=TweakGui_VisorColorSchemeTypedef.from_json, to_json=TweakGui_VisorColorSchemeTypedef.to_json
        ),
    })
    ball_hud_color_scheme: TweakGui_VisorColorSchemeTypedef = dataclasses.field(default_factory=TweakGui_VisorColorSchemeTypedef, metadata={
        'reflection': FieldReflection[TweakGui_VisorColorSchemeTypedef](
            TweakGui_VisorColorSchemeTypedef, id=0xc0181762, original_name='BallHudColorScheme', from_json=TweakGui_VisorColorSchemeTypedef.from_json, to_json=TweakGui_VisorColorSchemeTypedef.to_json
        ),
    })
    hypermode_hud_color_scheme: TweakGui_VisorColorSchemeTypedef = dataclasses.field(default_factory=TweakGui_VisorColorSchemeTypedef, metadata={
        'reflection': FieldReflection[TweakGui_VisorColorSchemeTypedef](
            TweakGui_VisorColorSchemeTypedef, id=0x40b1ca80, original_name='HypermodeHudColorScheme', from_json=TweakGui_VisorColorSchemeTypedef.from_json, to_json=TweakGui_VisorColorSchemeTypedef.to_json
        ),
    })
    combat_hud: TweakGui_HudColorTypedef = dataclasses.field(default_factory=TweakGui_HudColorTypedef, metadata={
        'reflection': FieldReflection[TweakGui_HudColorTypedef](
            TweakGui_HudColorTypedef, id=0x45d7a40f, original_name='CombatHud', from_json=TweakGui_HudColorTypedef.from_json, to_json=TweakGui_HudColorTypedef.to_json
        ),
    })
    command_hud: TweakGui_HudColorTypedef = dataclasses.field(default_factory=TweakGui_HudColorTypedef, metadata={
        'reflection': FieldReflection[TweakGui_HudColorTypedef](
            TweakGui_HudColorTypedef, id=0x61cd918c, original_name='CommandHud', from_json=TweakGui_HudColorTypedef.from_json, to_json=TweakGui_HudColorTypedef.to_json
        ),
    })
    scan_hud: TweakGui_HudColorTypedef = dataclasses.field(default_factory=TweakGui_HudColorTypedef, metadata={
        'reflection': FieldReflection[TweakGui_HudColorTypedef](
            TweakGui_HudColorTypedef, id=0x594b44cf, original_name='ScanHud', from_json=TweakGui_HudColorTypedef.from_json, to_json=TweakGui_HudColorTypedef.to_json
        ),
    })
    x_ray_hud: TweakGui_HudColorTypedef = dataclasses.field(default_factory=TweakGui_HudColorTypedef, metadata={
        'reflection': FieldReflection[TweakGui_HudColorTypedef](
            TweakGui_HudColorTypedef, id=0x8f5ebeb9, original_name='XRayHud', from_json=TweakGui_HudColorTypedef.from_json, to_json=TweakGui_HudColorTypedef.to_json
        ),
    })
    ball_hud: TweakGui_HudColorTypedef = dataclasses.field(default_factory=TweakGui_HudColorTypedef, metadata={
        'reflection': FieldReflection[TweakGui_HudColorTypedef](
            TweakGui_HudColorTypedef, id=0x58cd6373, original_name='BallHud', from_json=TweakGui_HudColorTypedef.from_json, to_json=TweakGui_HudColorTypedef.to_json
        ),
    })
    turret_hud: TweakGuiColors_TurretHudTypedef = dataclasses.field(default_factory=TweakGuiColors_TurretHudTypedef, metadata={
        'reflection': FieldReflection[TweakGuiColors_TurretHudTypedef](
            TweakGuiColors_TurretHudTypedef, id=0xde139081, original_name='TurretHud', from_json=TweakGuiColors_TurretHudTypedef.from_json, to_json=TweakGuiColors_TurretHudTypedef.to_json
        ),
    })

    def get_name(self) -> str:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    def set_name(self, name: str) -> None:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    @classmethod
    def object_type(cls) -> str:
        return 'TWGC'

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
        if property_count != 16:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7fda1466
        instance_name = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xcb737724
        hud_colors = TweakGuiColors_HUDColorsTypedef.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x6756d4de
        misc = TweakGuiColors_Misc.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x697613e9
        multiplayer = TweakGuiColors_Multiplayer.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x67c70055
        combat_hud_color_scheme = TweakGui_VisorColorSchemeTypedef.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x2fecaabd
        command_hud_color_scheme = TweakGui_VisorColorSchemeTypedef.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x80becd6e
        scan_hud_color_scheme = TweakGui_VisorColorSchemeTypedef.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x34e0e988
        x_ray_hud_color_scheme = TweakGui_VisorColorSchemeTypedef.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc0181762
        ball_hud_color_scheme = TweakGui_VisorColorSchemeTypedef.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x40b1ca80
        hypermode_hud_color_scheme = TweakGui_VisorColorSchemeTypedef.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x45d7a40f
        combat_hud = TweakGui_HudColorTypedef.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x61cd918c
        command_hud = TweakGui_HudColorTypedef.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x594b44cf
        scan_hud = TweakGui_HudColorTypedef.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8f5ebeb9
        x_ray_hud = TweakGui_HudColorTypedef.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x58cd6373
        ball_hud = TweakGui_HudColorTypedef.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xde139081
        turret_hud = TweakGuiColors_TurretHudTypedef.from_stream(data, game, property_size)
    
        return cls(instance_name, hud_colors, misc, multiplayer, combat_hud_color_scheme, command_hud_color_scheme, scan_hud_color_scheme, x_ray_hud_color_scheme, ball_hud_color_scheme, hypermode_hud_color_scheme, combat_hud, command_hud, scan_hud, x_ray_hud, ball_hud, turret_hud)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x10')  # 16 properties

        data.write(b'\x7f\xda\x14f')  # 0x7fda1466
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.instance_name.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xcbsw$')  # 0xcb737724
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hud_colors.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'gV\xd4\xde')  # 0x6756d4de
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.misc.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'iv\x13\xe9')  # 0x697613e9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.multiplayer.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'g\xc7\x00U')  # 0x67c70055
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.combat_hud_color_scheme.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'/\xec\xaa\xbd')  # 0x2fecaabd
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.command_hud_color_scheme.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x80\xbe\xcdn')  # 0x80becd6e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.scan_hud_color_scheme.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'4\xe0\xe9\x88')  # 0x34e0e988
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.x_ray_hud_color_scheme.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc0\x18\x17b')  # 0xc0181762
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ball_hud_color_scheme.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'@\xb1\xca\x80')  # 0x40b1ca80
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hypermode_hud_color_scheme.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'E\xd7\xa4\x0f')  # 0x45d7a40f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.combat_hud.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'a\xcd\x91\x8c')  # 0x61cd918c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.command_hud.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'YKD\xcf')  # 0x594b44cf
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.scan_hud.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x8f^\xbe\xb9')  # 0x8f5ebeb9
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.x_ray_hud.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'X\xcdcs')  # 0x58cd6373
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.ball_hud.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xde\x13\x90\x81')  # 0xde139081
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.turret_hud.to_stream(data, game)
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
        json_data = typing.cast("TweakGuiColorsJson", data)
        return cls(
            instance_name=json_data['instance_name'],
            hud_colors=TweakGuiColors_HUDColorsTypedef.from_json(json_data['hud_colors']),
            misc=TweakGuiColors_Misc.from_json(json_data['misc']),
            multiplayer=TweakGuiColors_Multiplayer.from_json(json_data['multiplayer']),
            combat_hud_color_scheme=TweakGui_VisorColorSchemeTypedef.from_json(json_data['combat_hud_color_scheme']),
            command_hud_color_scheme=TweakGui_VisorColorSchemeTypedef.from_json(json_data['command_hud_color_scheme']),
            scan_hud_color_scheme=TweakGui_VisorColorSchemeTypedef.from_json(json_data['scan_hud_color_scheme']),
            x_ray_hud_color_scheme=TweakGui_VisorColorSchemeTypedef.from_json(json_data['x_ray_hud_color_scheme']),
            ball_hud_color_scheme=TweakGui_VisorColorSchemeTypedef.from_json(json_data['ball_hud_color_scheme']),
            hypermode_hud_color_scheme=TweakGui_VisorColorSchemeTypedef.from_json(json_data['hypermode_hud_color_scheme']),
            combat_hud=TweakGui_HudColorTypedef.from_json(json_data['combat_hud']),
            command_hud=TweakGui_HudColorTypedef.from_json(json_data['command_hud']),
            scan_hud=TweakGui_HudColorTypedef.from_json(json_data['scan_hud']),
            x_ray_hud=TweakGui_HudColorTypedef.from_json(json_data['x_ray_hud']),
            ball_hud=TweakGui_HudColorTypedef.from_json(json_data['ball_hud']),
            turret_hud=TweakGuiColors_TurretHudTypedef.from_json(json_data['turret_hud']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'instance_name': self.instance_name,
            'hud_colors': self.hud_colors.to_json(),
            'misc': self.misc.to_json(),
            'multiplayer': self.multiplayer.to_json(),
            'combat_hud_color_scheme': self.combat_hud_color_scheme.to_json(),
            'command_hud_color_scheme': self.command_hud_color_scheme.to_json(),
            'scan_hud_color_scheme': self.scan_hud_color_scheme.to_json(),
            'x_ray_hud_color_scheme': self.x_ray_hud_color_scheme.to_json(),
            'ball_hud_color_scheme': self.ball_hud_color_scheme.to_json(),
            'hypermode_hud_color_scheme': self.hypermode_hud_color_scheme.to_json(),
            'combat_hud': self.combat_hud.to_json(),
            'command_hud': self.command_hud.to_json(),
            'scan_hud': self.scan_hud.to_json(),
            'x_ray_hud': self.x_ray_hud.to_json(),
            'ball_hud': self.ball_hud.to_json(),
            'turret_hud': self.turret_hud.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_instance_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_hud_colors(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGuiColors_HUDColorsTypedef:
    return TweakGuiColors_HUDColorsTypedef.from_stream(data, game, property_size)


def _decode_misc(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGuiColors_Misc:
    return TweakGuiColors_Misc.from_stream(data, game, property_size)


def _decode_multiplayer(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGuiColors_Multiplayer:
    return TweakGuiColors_Multiplayer.from_stream(data, game, property_size)


def _decode_combat_hud_color_scheme(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_VisorColorSchemeTypedef:
    return TweakGui_VisorColorSchemeTypedef.from_stream(data, game, property_size)


def _decode_command_hud_color_scheme(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_VisorColorSchemeTypedef:
    return TweakGui_VisorColorSchemeTypedef.from_stream(data, game, property_size)


def _decode_scan_hud_color_scheme(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_VisorColorSchemeTypedef:
    return TweakGui_VisorColorSchemeTypedef.from_stream(data, game, property_size)


def _decode_x_ray_hud_color_scheme(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_VisorColorSchemeTypedef:
    return TweakGui_VisorColorSchemeTypedef.from_stream(data, game, property_size)


def _decode_ball_hud_color_scheme(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_VisorColorSchemeTypedef:
    return TweakGui_VisorColorSchemeTypedef.from_stream(data, game, property_size)


def _decode_hypermode_hud_color_scheme(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_VisorColorSchemeTypedef:
    return TweakGui_VisorColorSchemeTypedef.from_stream(data, game, property_size)


def _decode_combat_hud(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_HudColorTypedef:
    return TweakGui_HudColorTypedef.from_stream(data, game, property_size)


def _decode_command_hud(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_HudColorTypedef:
    return TweakGui_HudColorTypedef.from_stream(data, game, property_size)


def _decode_scan_hud(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_HudColorTypedef:
    return TweakGui_HudColorTypedef.from_stream(data, game, property_size)


def _decode_x_ray_hud(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_HudColorTypedef:
    return TweakGui_HudColorTypedef.from_stream(data, game, property_size)


def _decode_ball_hud(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_HudColorTypedef:
    return TweakGui_HudColorTypedef.from_stream(data, game, property_size)


def _decode_turret_hud(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGuiColors_TurretHudTypedef:
    return TweakGuiColors_TurretHudTypedef.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x7fda1466: ('instance_name', _decode_instance_name),
    0xcb737724: ('hud_colors', _decode_hud_colors),
    0x6756d4de: ('misc', _decode_misc),
    0x697613e9: ('multiplayer', _decode_multiplayer),
    0x67c70055: ('combat_hud_color_scheme', _decode_combat_hud_color_scheme),
    0x2fecaabd: ('command_hud_color_scheme', _decode_command_hud_color_scheme),
    0x80becd6e: ('scan_hud_color_scheme', _decode_scan_hud_color_scheme),
    0x34e0e988: ('x_ray_hud_color_scheme', _decode_x_ray_hud_color_scheme),
    0xc0181762: ('ball_hud_color_scheme', _decode_ball_hud_color_scheme),
    0x40b1ca80: ('hypermode_hud_color_scheme', _decode_hypermode_hud_color_scheme),
    0x45d7a40f: ('combat_hud', _decode_combat_hud),
    0x61cd918c: ('command_hud', _decode_command_hud),
    0x594b44cf: ('scan_hud', _decode_scan_hud),
    0x8f5ebeb9: ('x_ray_hud', _decode_x_ray_hud),
    0x58cd6373: ('ball_hud', _decode_ball_hud),
    0xde139081: ('turret_hud', _decode_turret_hud),
}
