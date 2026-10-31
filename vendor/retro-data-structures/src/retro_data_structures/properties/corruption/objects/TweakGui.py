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
from retro_data_structures.properties.corruption.archetypes.TweakGui_CommandVisor import TweakGui_CommandVisor
from retro_data_structures.properties.corruption.archetypes.TweakGui_Completion import TweakGui_Completion
from retro_data_structures.properties.corruption.archetypes.TweakGui_Credits import TweakGui_Credits
from retro_data_structures.properties.corruption.archetypes.TweakGui_GrappleEffect import TweakGui_GrappleEffect
from retro_data_structures.properties.corruption.archetypes.TweakGui_Hypermode import TweakGui_Hypermode
from retro_data_structures.properties.corruption.archetypes.TweakGui_Misc import TweakGui_Misc
from retro_data_structures.properties.common.archetypes.TweakGui_MovieVolumes import TweakGui_MovieVolumes
from retro_data_structures.properties.corruption.archetypes.TweakGui_ScanVisor import TweakGui_ScanVisor
from retro_data_structures.properties.common.archetypes.TweakGui_ScannableObjectDownloadTimes import TweakGui_ScannableObjectDownloadTimes
from retro_data_structures.properties.corruption.archetypes.TweakGui_XRayVisor import TweakGui_XRayVisor

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class TweakGuiJson(typing_extensions.TypedDict):
        instance_name: str
        misc: json_util.JsonObject
        scannable_object_download_times: json_util.JsonObject
        scan_visor: json_util.JsonObject
        command_visor: json_util.JsonObject
        x_ray_visor: json_util.JsonObject
        hyper_mode: json_util.JsonObject
        grapple_effect: json_util.JsonObject
        credits: json_util.JsonObject
        completion: json_util.JsonObject
        movie_volumes: json_util.JsonObject
    

@dataclasses.dataclass()
class TweakGui(BaseObjectType):
    instance_name: str = dataclasses.field(default='', metadata={
        'reflection': FieldReflection[str](
            str, id=0x7fda1466, original_name='InstanceName'
        ),
    })
    misc: TweakGui_Misc = dataclasses.field(default_factory=TweakGui_Misc, metadata={
        'reflection': FieldReflection[TweakGui_Misc](
            TweakGui_Misc, id=0xd45f7663, original_name='Misc', from_json=TweakGui_Misc.from_json, to_json=TweakGui_Misc.to_json
        ),
    })
    scannable_object_download_times: TweakGui_ScannableObjectDownloadTimes = dataclasses.field(default_factory=TweakGui_ScannableObjectDownloadTimes, metadata={
        'reflection': FieldReflection[TweakGui_ScannableObjectDownloadTimes](
            TweakGui_ScannableObjectDownloadTimes, id=0x80b13e60, original_name='ScannableObjectDownloadTimes', from_json=TweakGui_ScannableObjectDownloadTimes.from_json, to_json=TweakGui_ScannableObjectDownloadTimes.to_json
        ),
    })
    scan_visor: TweakGui_ScanVisor = dataclasses.field(default_factory=TweakGui_ScanVisor, metadata={
        'reflection': FieldReflection[TweakGui_ScanVisor](
            TweakGui_ScanVisor, id=0x40ffb3c4, original_name='ScanVisor', from_json=TweakGui_ScanVisor.from_json, to_json=TweakGui_ScanVisor.to_json
        ),
    })
    command_visor: TweakGui_CommandVisor = dataclasses.field(default_factory=TweakGui_CommandVisor, metadata={
        'reflection': FieldReflection[TweakGui_CommandVisor](
            TweakGui_CommandVisor, id=0x7a64e529, original_name='CommandVisor', from_json=TweakGui_CommandVisor.from_json, to_json=TweakGui_CommandVisor.to_json
        ),
    })
    x_ray_visor: TweakGui_XRayVisor = dataclasses.field(default_factory=TweakGui_XRayVisor, metadata={
        'reflection': FieldReflection[TweakGui_XRayVisor](
            TweakGui_XRayVisor, id=0x68e1b284, original_name='XRayVisor', from_json=TweakGui_XRayVisor.from_json, to_json=TweakGui_XRayVisor.to_json
        ),
    })
    hyper_mode: TweakGui_Hypermode = dataclasses.field(default_factory=TweakGui_Hypermode, metadata={
        'reflection': FieldReflection[TweakGui_Hypermode](
            TweakGui_Hypermode, id=0x95fdea28, original_name='HyperMode', from_json=TweakGui_Hypermode.from_json, to_json=TweakGui_Hypermode.to_json
        ),
    })
    grapple_effect: TweakGui_GrappleEffect = dataclasses.field(default_factory=TweakGui_GrappleEffect, metadata={
        'reflection': FieldReflection[TweakGui_GrappleEffect](
            TweakGui_GrappleEffect, id=0xd0494674, original_name='GrappleEffect', from_json=TweakGui_GrappleEffect.from_json, to_json=TweakGui_GrappleEffect.to_json
        ),
    })
    credits: TweakGui_Credits = dataclasses.field(default_factory=TweakGui_Credits, metadata={
        'reflection': FieldReflection[TweakGui_Credits](
            TweakGui_Credits, id=0x77393416, original_name='Credits', from_json=TweakGui_Credits.from_json, to_json=TweakGui_Credits.to_json
        ),
    })
    completion: TweakGui_Completion = dataclasses.field(default_factory=TweakGui_Completion, metadata={
        'reflection': FieldReflection[TweakGui_Completion](
            TweakGui_Completion, id=0x02149892, original_name='Completion', from_json=TweakGui_Completion.from_json, to_json=TweakGui_Completion.to_json
        ),
    })
    movie_volumes: TweakGui_MovieVolumes = dataclasses.field(default_factory=TweakGui_MovieVolumes, metadata={
        'reflection': FieldReflection[TweakGui_MovieVolumes](
            TweakGui_MovieVolumes, id=0xa4f61e92, original_name='MovieVolumes', from_json=TweakGui_MovieVolumes.from_json, to_json=TweakGui_MovieVolumes.to_json
        ),
    })

    def get_name(self) -> str:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    def set_name(self, name: str) -> None:
        raise RuntimeError(f"{self.__class__.__name__} does not have name")

    @classmethod
    def object_type(cls) -> str:
        return 'TWGU'

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
        assert property_id == 0x7fda1466
        instance_name = data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd45f7663
        misc = TweakGui_Misc.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x80b13e60
        scannable_object_download_times = TweakGui_ScannableObjectDownloadTimes.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x40ffb3c4
        scan_visor = TweakGui_ScanVisor.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7a64e529
        command_visor = TweakGui_CommandVisor.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x68e1b284
        x_ray_visor = TweakGui_XRayVisor.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x95fdea28
        hyper_mode = TweakGui_Hypermode.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd0494674
        grapple_effect = TweakGui_GrappleEffect.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x77393416
        credits = TweakGui_Credits.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x02149892
        completion = TweakGui_Completion.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa4f61e92
        movie_volumes = TweakGui_MovieVolumes.from_stream(data, game, property_size)
    
        return cls(instance_name, misc, scannable_object_download_times, scan_visor, command_visor, x_ray_visor, hyper_mode, grapple_effect, credits, completion, movie_volumes)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\xff\xff\xff\xff')  # struct object id
        root_size_offset = data.tell()
        data.write(b'\x00\x00')  # placeholder for root struct size
        data.write(b'\x00\x0b')  # 11 properties

        data.write(b'\x7f\xda\x14f')  # 0x7fda1466
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        data.write(self.instance_name.encode("utf-8", errors="surrogateescape"))
        data.write(b'\x00')
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd4_vc')  # 0xd45f7663
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.misc.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x80\xb1>`')  # 0x80b13e60
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.scannable_object_download_times.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'@\xff\xb3\xc4')  # 0x40ffb3c4
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.scan_visor.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'zd\xe5)')  # 0x7a64e529
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.command_visor.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'h\xe1\xb2\x84')  # 0x68e1b284
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.x_ray_visor.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x95\xfd\xea(')  # 0x95fdea28
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.hyper_mode.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd0IFt')  # 0xd0494674
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grapple_effect.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'w94\x16')  # 0x77393416
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.credits.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x02\x14\x98\x92')  # 0x2149892
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.completion.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa4\xf6\x1e\x92')  # 0xa4f61e92
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.movie_volumes.to_stream(data, game)
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
        json_data = typing.cast("TweakGuiJson", data)
        return cls(
            instance_name=json_data['instance_name'],
            misc=TweakGui_Misc.from_json(json_data['misc']),
            scannable_object_download_times=TweakGui_ScannableObjectDownloadTimes.from_json(json_data['scannable_object_download_times']),
            scan_visor=TweakGui_ScanVisor.from_json(json_data['scan_visor']),
            command_visor=TweakGui_CommandVisor.from_json(json_data['command_visor']),
            x_ray_visor=TweakGui_XRayVisor.from_json(json_data['x_ray_visor']),
            hyper_mode=TweakGui_Hypermode.from_json(json_data['hyper_mode']),
            grapple_effect=TweakGui_GrappleEffect.from_json(json_data['grapple_effect']),
            credits=TweakGui_Credits.from_json(json_data['credits']),
            completion=TweakGui_Completion.from_json(json_data['completion']),
            movie_volumes=TweakGui_MovieVolumes.from_json(json_data['movie_volumes']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'instance_name': self.instance_name,
            'misc': self.misc.to_json(),
            'scannable_object_download_times': self.scannable_object_download_times.to_json(),
            'scan_visor': self.scan_visor.to_json(),
            'command_visor': self.command_visor.to_json(),
            'x_ray_visor': self.x_ray_visor.to_json(),
            'hyper_mode': self.hyper_mode.to_json(),
            'grapple_effect': self.grapple_effect.to_json(),
            'credits': self.credits.to_json(),
            'completion': self.completion.to_json(),
            'movie_volumes': self.movie_volumes.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        yield from []


def _decode_instance_name(data: typing.BinaryIO, game: Game, property_size: int) -> str:
    return data.read(property_size)[:-1].decode("utf-8", errors="surrogateescape")


def _decode_misc(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_Misc:
    return TweakGui_Misc.from_stream(data, game, property_size)


def _decode_scannable_object_download_times(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_ScannableObjectDownloadTimes:
    return TweakGui_ScannableObjectDownloadTimes.from_stream(data, game, property_size)


def _decode_scan_visor(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_ScanVisor:
    return TweakGui_ScanVisor.from_stream(data, game, property_size)


def _decode_command_visor(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_CommandVisor:
    return TweakGui_CommandVisor.from_stream(data, game, property_size)


def _decode_x_ray_visor(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_XRayVisor:
    return TweakGui_XRayVisor.from_stream(data, game, property_size)


def _decode_hyper_mode(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_Hypermode:
    return TweakGui_Hypermode.from_stream(data, game, property_size)


def _decode_grapple_effect(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_GrappleEffect:
    return TweakGui_GrappleEffect.from_stream(data, game, property_size)


def _decode_credits(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_Credits:
    return TweakGui_Credits.from_stream(data, game, property_size)


def _decode_completion(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_Completion:
    return TweakGui_Completion.from_stream(data, game, property_size)


def _decode_movie_volumes(data: typing.BinaryIO, game: Game, property_size: int) -> TweakGui_MovieVolumes:
    return TweakGui_MovieVolumes.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x7fda1466: ('instance_name', _decode_instance_name),
    0xd45f7663: ('misc', _decode_misc),
    0x80b13e60: ('scannable_object_download_times', _decode_scannable_object_download_times),
    0x40ffb3c4: ('scan_visor', _decode_scan_visor),
    0x7a64e529: ('command_visor', _decode_command_visor),
    0x68e1b284: ('x_ray_visor', _decode_x_ray_visor),
    0x95fdea28: ('hyper_mode', _decode_hyper_mode),
    0xd0494674: ('grapple_effect', _decode_grapple_effect),
    0x77393416: ('credits', _decode_credits),
    0x02149892: ('completion', _decode_completion),
    0xa4f61e92: ('movie_volumes', _decode_movie_volumes),
}
