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

if typing.TYPE_CHECKING:
    class TweakPlayerRes_AutoMapperIconsJson(typing_extensions.TypedDict):
        save_station_icon: str
        missile_station_icon: str
        elevator_icon_icon: str
        portal_icon: str
        mines_first_break_top_icon: str
        mines_first_break_bottom_icon: str
        mines_second_break_top_icon: str
        mines_second_break_bottom_icon: str
        translator_door_icon: str
        map_icon_g: str
        map_icon_m: str
        map_icon_r: str
        map_icon_u: str
        map_icon_l: str
    

@dataclasses.dataclass()
class TweakPlayerRes_AutoMapperIcons(BaseProperty):
    save_station_icon: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xe7014cda, original_name='SaveStationIcon'
        ),
    })
    missile_station_icon: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x33c94749, original_name='MissileStationIcon'
        ),
    })
    elevator_icon_icon: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x9b36949e, original_name='ElevatorIconIcon'
        ),
    })
    portal_icon: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xafa1b87c, original_name='PortalIcon'
        ),
    })
    mines_first_break_top_icon: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xfbf479ec, original_name='MinesFirstBreakTopIcon'
        ),
    })
    mines_first_break_bottom_icon: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x5566b6e4, original_name='MinesFirstBreakBottomIcon'
        ),
    })
    mines_second_break_top_icon: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x51fe3f1f, original_name='MinesSecondBreakTopIcon'
        ),
    })
    mines_second_break_bottom_icon: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xa4127a5a, original_name='MinesSecondBreakBottomIcon'
        ),
    })
    translator_door_icon: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xf8403d18, original_name='TranslatorDoorIcon'
        ),
    })
    map_icon_g: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x5096bfa5, original_name='MapIconG'
        ),
    })
    map_icon_m: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xf4e6e0eb, original_name='MapIconM'
        ),
    })
    map_icon_r: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x65700ccc, original_name='MapIconR'
        ),
    })
    map_icon_u: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xa0d73242, original_name='MapIconU'
        ),
    })
    map_icon_l: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x5291eb5f, original_name='MapIconL'
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
        if property_count != 14:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe7014cda
        save_station_icon = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x33c94749
        missile_station_icon = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9b36949e
        elevator_icon_icon = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xafa1b87c
        portal_icon = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xfbf479ec
        mines_first_break_top_icon = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5566b6e4
        mines_first_break_bottom_icon = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x51fe3f1f
        mines_second_break_top_icon = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa4127a5a
        mines_second_break_bottom_icon = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf8403d18
        translator_door_icon = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5096bfa5
        map_icon_g = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf4e6e0eb
        map_icon_m = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x65700ccc
        map_icon_r = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa0d73242
        map_icon_u = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5291eb5f
        map_icon_l = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        return cls(save_station_icon, missile_station_icon, elevator_icon_icon, portal_icon, mines_first_break_top_icon, mines_first_break_bottom_icon, mines_second_break_top_icon, mines_second_break_bottom_icon, translator_door_icon, map_icon_g, map_icon_m, map_icon_r, map_icon_u, map_icon_l)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        num_properties_offset = data.tell()
        data.write(b'\x00\t')  # 9 properties
        num_properties_written = 9

        data.write(b'\xe7\x01L\xda')  # 0xe7014cda
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.save_station_icon.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'3\xc9GI')  # 0x33c94749
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.missile_station_icon.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9b6\x94\x9e')  # 0x9b36949e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.elevator_icon_icon.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xaf\xa1\xb8|')  # 0xafa1b87c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.portal_icon.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xfb\xf4y\xec')  # 0xfbf479ec
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.mines_first_break_top_icon.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'Uf\xb6\xe4')  # 0x5566b6e4
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.mines_first_break_bottom_icon.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'Q\xfe?\x1f')  # 0x51fe3f1f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.mines_second_break_top_icon.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa4\x12zZ')  # 0xa4127a5a
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.mines_second_break_bottom_icon.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf8@=\x18')  # 0xf8403d18
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.translator_door_icon.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        if self.map_icon_g != default_override.get('map_icon_g', ''):
            num_properties_written += 1
            data.write(b'P\x96\xbf\xa5')  # 0x5096bfa5
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            data.write(self.map_icon_g.encode("utf-8", errors="surrogateescape"))
            data.write(b'\x00')
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self.map_icon_m != default_override.get('map_icon_m', ''):
            num_properties_written += 1
            data.write(b'\xf4\xe6\xe0\xeb')  # 0xf4e6e0eb
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            data.write(self.map_icon_m.encode("utf-8", errors="surrogateescape"))
            data.write(b'\x00')
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self.map_icon_r != default_override.get('map_icon_r', ''):
            num_properties_written += 1
            data.write(b'ep\x0c\xcc')  # 0x65700ccc
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            data.write(self.map_icon_r.encode("utf-8", errors="surrogateescape"))
            data.write(b'\x00')
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self.map_icon_u != default_override.get('map_icon_u', ''):
            num_properties_written += 1
            data.write(b'\xa0\xd72B')  # 0xa0d73242
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            data.write(self.map_icon_u.encode("utf-8", errors="surrogateescape"))
            data.write(b'\x00')
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if self.map_icon_l != default_override.get('map_icon_l', ''):
            num_properties_written += 1
            data.write(b'R\x91\xeb_')  # 0x5291eb5f
            before = data.tell()
            data.write(b'\x00\x00')  # size placeholder
            data.write(self.map_icon_l.encode("utf-8", errors="surrogateescape"))
            data.write(b'\x00')
            after = data.tell()
            data.seek(before)
            data.write(structs.BIG_H.pack(after - before - 2))
            data.seek(after)

        if num_properties_written != 9:
            struct_end_offset = data.tell()
            data.seek(num_properties_offset)
            data.write(struct.pack(">H", num_properties_written))
            data.seek(struct_end_offset)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayerRes_AutoMapperIconsJson", data)
        return cls(
            save_station_icon=json_data['save_station_icon'],
            missile_station_icon=json_data['missile_station_icon'],
            elevator_icon_icon=json_data['elevator_icon_icon'],
            portal_icon=json_data['portal_icon'],
            mines_first_break_top_icon=json_data['mines_first_break_top_icon'],
            mines_first_break_bottom_icon=json_data['mines_first_break_bottom_icon'],
            mines_second_break_top_icon=json_data['mines_second_break_top_icon'],
            mines_second_break_bottom_icon=json_data['mines_second_break_bottom_icon'],
            translator_door_icon=json_data['translator_door_icon'],
            map_icon_g=json_data['map_icon_g'],
            map_icon_m=json_data['map_icon_m'],
            map_icon_r=json_data['map_icon_r'],
            map_icon_u=json_data['map_icon_u'],
            map_icon_l=json_data['map_icon_l'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'save_station_icon': self.save_station_icon,
            'missile_station_icon': self.missile_station_icon,
            'elevator_icon_icon': self.elevator_icon_icon,
            'portal_icon': self.portal_icon,
            'mines_first_break_top_icon': self.mines_first_break_top_icon,
            'mines_first_break_bottom_icon': self.mines_first_break_bottom_icon,
            'mines_second_break_top_icon': self.mines_second_break_top_icon,
            'mines_second_break_bottom_icon': self.mines_second_break_bottom_icon,
            'translator_door_icon': self.translator_door_icon,
            'map_icon_g': self.map_icon_g,
            'map_icon_m': self.map_icon_m,
            'map_icon_r': self.map_icon_r,
            'map_icon_u': self.map_icon_u,
            'map_icon_l': self.map_icon_l,
        }


def _decode_save_station_icon(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_missile_station_icon(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_elevator_icon_icon(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_portal_icon(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_mines_first_break_top_icon(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_mines_first_break_bottom_icon(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_mines_second_break_top_icon(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_mines_second_break_bottom_icon(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_translator_door_icon(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_map_icon_g(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_map_icon_m(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_map_icon_r(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_map_icon_u(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_map_icon_l(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xe7014cda: ('save_station_icon', _decode_save_station_icon),
    0x33c94749: ('missile_station_icon', _decode_missile_station_icon),
    0x9b36949e: ('elevator_icon_icon', _decode_elevator_icon_icon),
    0xafa1b87c: ('portal_icon', _decode_portal_icon),
    0xfbf479ec: ('mines_first_break_top_icon', _decode_mines_first_break_top_icon),
    0x5566b6e4: ('mines_first_break_bottom_icon', _decode_mines_first_break_bottom_icon),
    0x51fe3f1f: ('mines_second_break_top_icon', _decode_mines_second_break_top_icon),
    0xa4127a5a: ('mines_second_break_bottom_icon', _decode_mines_second_break_bottom_icon),
    0xf8403d18: ('translator_door_icon', _decode_translator_door_icon),
    0x5096bfa5: ('map_icon_g', _decode_map_icon_g),
    0xf4e6e0eb: ('map_icon_m', _decode_map_icon_m),
    0x65700ccc: ('map_icon_r', _decode_map_icon_r),
    0xa0d73242: ('map_icon_u', _decode_map_icon_u),
    0x5291eb5f: ('map_icon_l', _decode_map_icon_l),
}
