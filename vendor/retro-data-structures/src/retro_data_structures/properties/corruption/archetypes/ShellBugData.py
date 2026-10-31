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
from retro_data_structures.properties.corruption.archetypes.DamageVulnerability import DamageVulnerability
from retro_data_structures.properties.corruption.archetypes.GrappleData import GrappleData
from retro_data_structures.properties.corruption.archetypes.LaunchProjectileData import LaunchProjectileData

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class ShellBugDataJson(typing_extensions.TypedDict):
        thorn: json_util.JsonObject
        thorn_range_min: float
        thorn_range_max: float
        ball_range: float
        ball_radius: float
        look_ahead_time: float
        unknown_0x34bbc7a5: bool
        unknown_0xe5839374: float
        unknown_0x03e33c95: float
        weak_spot_vulnerability: json_util.JsonObject
        unknown_0x84e71870: bool
        use_complex_collision: bool
        grapple_data: json_util.JsonObject
    

@dataclasses.dataclass()
class ShellBugData(BaseProperty):
    thorn: LaunchProjectileData = dataclasses.field(default_factory=LaunchProjectileData, metadata={
        'reflection': FieldReflection[LaunchProjectileData](
            LaunchProjectileData, id=0xaba9a56d, original_name='Thorn', from_json=LaunchProjectileData.from_json, to_json=LaunchProjectileData.to_json
        ),
    })
    thorn_range_min: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xa023555c, original_name='ThornRangeMin'
        ),
    })
    thorn_range_max: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x4643fabd, original_name='ThornRangeMax'
        ),
    })
    ball_range: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0057a7d8, original_name='BallRange'
        ),
    })
    ball_radius: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x0e2f537f, original_name='BallRadius'
        ),
    })
    look_ahead_time: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x8cb20c53, original_name='LookAheadTime'
        ),
    })
    unknown_0x34bbc7a5: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x34bbc7a5, original_name='Unknown'
        ),
    })
    unknown_0xe5839374: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0xe5839374, original_name='Unknown'
        ),
    })
    unknown_0x03e33c95: float = dataclasses.field(default=0.0, metadata={
        'reflection': FieldReflection[float](
            float, id=0x03e33c95, original_name='Unknown'
        ),
    })
    weak_spot_vulnerability: DamageVulnerability = dataclasses.field(default_factory=DamageVulnerability, metadata={
        'reflection': FieldReflection[DamageVulnerability](
            DamageVulnerability, id=0x950318f0, original_name='WeakSpotVulnerability', from_json=DamageVulnerability.from_json, to_json=DamageVulnerability.to_json
        ),
    })
    unknown_0x84e71870: bool = dataclasses.field(default=True, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x84e71870, original_name='Unknown'
        ),
    })
    use_complex_collision: bool = dataclasses.field(default=False, metadata={
        'reflection': FieldReflection[bool](
            bool, id=0x76264db1, original_name='UseComplexCollision'
        ),
    })
    grapple_data: GrappleData = dataclasses.field(default_factory=GrappleData, metadata={
        'reflection': FieldReflection[GrappleData](
            GrappleData, id=0xf609c637, original_name='GrappleData', from_json=GrappleData.from_json, to_json=GrappleData.to_json
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
        if property_count != 13:
            return None
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xaba9a56d
        thorn = LaunchProjectileData.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa023555c
        thorn_range_min = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x4643fabd
        thorn_range_max = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0057a7d8
        ball_range = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x0e2f537f
        ball_radius = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x8cb20c53
        look_ahead_time = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x34bbc7a5
        unknown_0x34bbc7a5 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe5839374
        unknown_0xe5839374 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x03e33c95
        unknown_0x03e33c95 = structs.BIG_f.unpack(data.read(4))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x950318f0
        weak_spot_vulnerability = DamageVulnerability.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x84e71870
        unknown_0x84e71870 = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x76264db1
        use_complex_collision = structs.BIG_bool_.unpack(data.read(1))[0]
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf609c637
        grapple_data = GrappleData.from_stream(data, game, property_size)
    
        return cls(thorn, thorn_range_min, thorn_range_max, ball_range, ball_radius, look_ahead_time, unknown_0x34bbc7a5, unknown_0xe5839374, unknown_0x03e33c95, weak_spot_vulnerability, unknown_0x84e71870, use_complex_collision, grapple_data)

    def to_stream(self, data: typing.BinaryIO, game: Game, default_override: dict | None = None) -> None:
        default_override = default_override or {}
        data.write(b'\x00\r')  # 13 properties

        data.write(b'\xab\xa9\xa5m')  # 0xaba9a56d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.thorn.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa0#U\\')  # 0xa023555c
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.thorn_range_min))

        data.write(b'FC\xfa\xbd')  # 0x4643fabd
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.thorn_range_max))

        data.write(b'\x00W\xa7\xd8')  # 0x57a7d8
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ball_range))

        data.write(b'\x0e/S\x7f')  # 0xe2f537f
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.ball_radius))

        data.write(b'\x8c\xb2\x0cS')  # 0x8cb20c53
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.look_ahead_time))

        data.write(b'4\xbb\xc7\xa5')  # 0x34bbc7a5
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x34bbc7a5))

        data.write(b'\xe5\x83\x93t')  # 0xe5839374
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0xe5839374))

        data.write(b'\x03\xe3<\x95')  # 0x3e33c95
        data.write(b'\x00\x04')  # size
        data.write(structs.BIG_f.pack(self.unknown_0x03e33c95))

        data.write(b'\x95\x03\x18\xf0')  # 0x950318f0
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.weak_spot_vulnerability.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x84\xe7\x18p')  # 0x84e71870
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.unknown_0x84e71870))

        data.write(b'v&M\xb1')  # 0x76264db1
        data.write(b'\x00\x01')  # size
        data.write(structs.BIG_bool_.pack(self.use_complex_collision))

        data.write(b'\xf6\t\xc67')  # 0xf609c637
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.grapple_data.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

    @classmethod
    def from_json(cls, data: json_util.JsonValue) -> typing_extensions.Self:
        json_data = typing.cast("ShellBugDataJson", data)
        return cls(
            thorn=LaunchProjectileData.from_json(json_data['thorn']),
            thorn_range_min=json_data['thorn_range_min'],
            thorn_range_max=json_data['thorn_range_max'],
            ball_range=json_data['ball_range'],
            ball_radius=json_data['ball_radius'],
            look_ahead_time=json_data['look_ahead_time'],
            unknown_0x34bbc7a5=json_data['unknown_0x34bbc7a5'],
            unknown_0xe5839374=json_data['unknown_0xe5839374'],
            unknown_0x03e33c95=json_data['unknown_0x03e33c95'],
            weak_spot_vulnerability=DamageVulnerability.from_json(json_data['weak_spot_vulnerability']),
            unknown_0x84e71870=json_data['unknown_0x84e71870'],
            use_complex_collision=json_data['use_complex_collision'],
            grapple_data=GrappleData.from_json(json_data['grapple_data']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'thorn': self.thorn.to_json(),
            'thorn_range_min': self.thorn_range_min,
            'thorn_range_max': self.thorn_range_max,
            'ball_range': self.ball_range,
            'ball_radius': self.ball_radius,
            'look_ahead_time': self.look_ahead_time,
            'unknown_0x34bbc7a5': self.unknown_0x34bbc7a5,
            'unknown_0xe5839374': self.unknown_0xe5839374,
            'unknown_0x03e33c95': self.unknown_0x03e33c95,
            'weak_spot_vulnerability': self.weak_spot_vulnerability.to_json(),
            'unknown_0x84e71870': self.unknown_0x84e71870,
            'use_complex_collision': self.use_complex_collision,
            'grapple_data': self.grapple_data.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.thorn.dependencies_for, "thorn", "LaunchProjectileData"),
            (self.grapple_data.dependencies_for, "grapple_data", "GrappleData"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for ShellBugData.{field_name} ({field_type}): {e}"
                )


def _decode_thorn(data: typing.BinaryIO, game: Game, property_size: int) -> LaunchProjectileData:
    return LaunchProjectileData.from_stream(data, game, property_size)


def _decode_weak_spot_vulnerability(data: typing.BinaryIO, game: Game, property_size: int) -> DamageVulnerability:
    return DamageVulnerability.from_stream(data, game, property_size)


def _decode_grapple_data(data: typing.BinaryIO, game: Game, property_size: int) -> GrappleData:
    return GrappleData.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0xaba9a56d: ('thorn', _decode_thorn),
    0xa023555c: ('thorn_range_min', structs.decode_BIG_f),
    0x4643fabd: ('thorn_range_max', structs.decode_BIG_f),
    0x0057a7d8: ('ball_range', structs.decode_BIG_f),
    0x0e2f537f: ('ball_radius', structs.decode_BIG_f),
    0x8cb20c53: ('look_ahead_time', structs.decode_BIG_f),
    0x34bbc7a5: ('unknown_0x34bbc7a5', structs.decode_BIG_bool_),
    0xe5839374: ('unknown_0xe5839374', structs.decode_BIG_f),
    0x03e33c95: ('unknown_0x03e33c95', structs.decode_BIG_f),
    0x950318f0: ('weak_spot_vulnerability', _decode_weak_spot_vulnerability),
    0x84e71870: ('unknown_0x84e71870', structs.decode_BIG_bool_),
    0x76264db1: ('use_complex_collision', structs.decode_BIG_bool_),
    0xf609c637: ('grapple_data', _decode_grapple_data),
}
