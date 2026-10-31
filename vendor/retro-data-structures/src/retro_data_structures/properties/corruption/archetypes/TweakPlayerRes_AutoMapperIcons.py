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
        landing_site: str
        non_visited_landing_site: str
        warp_portal: str
        save_station: str
        map_station: str
        split_up_arrow: str
        split_down_arrow: str
        map_icon_g: str
        map_icon_l: str
        map_icon_m: str
        map_icon_r: str
        map_icon_u: str
    

@dataclasses.dataclass()
class TweakPlayerRes_AutoMapperIcons(BaseProperty):
    landing_site: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x1eba4bd8, original_name='LandingSite'
        ),
    })
    non_visited_landing_site: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xdd1b0445, original_name='NonVisitedLandingSite'
        ),
    })
    warp_portal: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xb35b7bec, original_name='WarpPortal'
        ),
    })
    save_station: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x64667637, original_name='SaveStation'
        ),
    })
    map_station: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xd5d00133, original_name='MapStation'
        ),
    })
    split_up_arrow: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xdfac0db1, original_name='SplitUpArrow'
        ),
    })
    split_down_arrow: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0xb838c9c0, original_name='SplitDownArrow'
        ),
    })
    map_icon_g: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x5096bfa5, original_name='MapIconG'
        ),
    })
    map_icon_l: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x5291eb5f, original_name='MapIconL'
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
        if property_count != 12:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x1eba4bd8
        landing_site = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdd1b0445
        non_visited_landing_site = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb35b7bec
        warp_portal = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x64667637
        save_station = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd5d00133
        map_station = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xdfac0db1
        split_up_arrow = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb838c9c0
        split_down_arrow = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5096bfa5
        map_icon_g = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x5291eb5f
        map_icon_l = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf4e6e0eb
        map_icon_m = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x65700ccc
        map_icon_r = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa0d73242
        map_icon_u = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        return cls(landing_site, non_visited_landing_site, warp_portal, save_station, map_station, split_up_arrow, split_down_arrow, map_icon_g, map_icon_l, map_icon_m, map_icon_r, map_icon_u)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\x0c')  # 12 properties

        data.write(b'\x1e\xbaK\xd8')  # 0x1eba4bd8
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.landing_site.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xdd\x1b\x04E')  # 0xdd1b0445
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.non_visited_landing_site.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb3[{\xec')  # 0xb35b7bec
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.warp_portal.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'dfv7')  # 0x64667637
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.save_station.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd5\xd0\x013')  # 0xd5d00133
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.map_station.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xdf\xac\r\xb1')  # 0xdfac0db1
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.split_up_arrow.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb88\xc9\xc0')  # 0xb838c9c0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.split_down_arrow.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'P\x96\xbf\xa5')  # 0x5096bfa5
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.map_icon_g.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'R\x91\xeb_')  # 0x5291eb5f
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.map_icon_l.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf4\xe6\xe0\xeb')  # 0xf4e6e0eb
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.map_icon_m.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'ep\x0c\xcc')  # 0x65700ccc
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.map_icon_r.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa0\xd72B')  # 0xa0d73242
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.map_icon_u.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("TweakPlayerRes_AutoMapperIconsJson", data)
        return cls(
            landing_site=json_data['landing_site'],
            non_visited_landing_site=json_data['non_visited_landing_site'],
            warp_portal=json_data['warp_portal'],
            save_station=json_data['save_station'],
            map_station=json_data['map_station'],
            split_up_arrow=json_data['split_up_arrow'],
            split_down_arrow=json_data['split_down_arrow'],
            map_icon_g=json_data['map_icon_g'],
            map_icon_l=json_data['map_icon_l'],
            map_icon_m=json_data['map_icon_m'],
            map_icon_r=json_data['map_icon_r'],
            map_icon_u=json_data['map_icon_u'],
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'landing_site': self.landing_site,
            'non_visited_landing_site': self.non_visited_landing_site,
            'warp_portal': self.warp_portal,
            'save_station': self.save_station,
            'map_station': self.map_station,
            'split_up_arrow': self.split_up_arrow,
            'split_down_arrow': self.split_down_arrow,
            'map_icon_g': self.map_icon_g,
            'map_icon_l': self.map_icon_l,
            'map_icon_m': self.map_icon_m,
            'map_icon_r': self.map_icon_r,
            'map_icon_u': self.map_icon_u,
        }


def _decode_landing_site(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_non_visited_landing_site(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_warp_portal(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_save_station(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_map_station(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_split_up_arrow(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_split_down_arrow(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_map_icon_g(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_map_icon_l(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_map_icon_m(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_map_icon_r(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_map_icon_u(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x1eba4bd8: ('landing_site', _decode_landing_site),
    0xdd1b0445: ('non_visited_landing_site', _decode_non_visited_landing_site),
    0xb35b7bec: ('warp_portal', _decode_warp_portal),
    0x64667637: ('save_station', _decode_save_station),
    0xd5d00133: ('map_station', _decode_map_station),
    0xdfac0db1: ('split_up_arrow', _decode_split_up_arrow),
    0xb838c9c0: ('split_down_arrow', _decode_split_down_arrow),
    0x5096bfa5: ('map_icon_g', _decode_map_icon_g),
    0x5291eb5f: ('map_icon_l', _decode_map_icon_l),
    0xf4e6e0eb: ('map_icon_m', _decode_map_icon_m),
    0x65700ccc: ('map_icon_r', _decode_map_icon_r),
    0xa0d73242: ('map_icon_u', _decode_map_icon_u),
}
