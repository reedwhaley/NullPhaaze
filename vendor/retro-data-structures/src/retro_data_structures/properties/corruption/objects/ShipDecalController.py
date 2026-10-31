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
from retro_data_structures.properties.common.archetypes.EditorProperties import EditorProperties
from retro_data_structures.properties.corruption.archetypes.ShipDecalSwapPair import ShipDecalSwapPair

if typing.TYPE_CHECKING:
    from collections.abc import Iterator
    from retro_data_structures.asset_manager import AssetManager
    from retro_data_structures.base_resource import Dependency

    class ShipDecalControllerJson(typing_extensions.TypedDict):
        editor_properties: json_util.JsonObject
        paper_mario: json_util.JsonObject
        super_mario_galaxy: json_util.JsonObject
        mario_party8: json_util.JsonObject
        excite_truck: json_util.JsonObject
        legend_of_zelda_twilight_princess: json_util.JsonObject
        super_smash_brothers_brawl: json_util.JsonObject
        wii_sports: json_util.JsonObject
        wii_play: json_util.JsonObject
        wario_ware_smooth_moves: json_util.JsonObject
        metroid_prime3_1: json_util.JsonObject
        metroid_prime3_2: json_util.JsonObject
        metroid_prime_trilogy: json_util.JsonObject
        retro_studios: json_util.JsonObject
    

@dataclasses.dataclass()
class ShipDecalController(BaseObjectType):
    editor_properties: EditorProperties = dataclasses.field(default_factory=EditorProperties, metadata={
        'reflection': FieldReflection[EditorProperties](
            EditorProperties, id=0x255a4580, original_name='EditorProperties', from_json=EditorProperties.from_json, to_json=EditorProperties.to_json
        ),
    })
    paper_mario: ShipDecalSwapPair = dataclasses.field(default_factory=ShipDecalSwapPair, metadata={
        'reflection': FieldReflection[ShipDecalSwapPair](
            ShipDecalSwapPair, id=0x15fbdf30, original_name='PaperMario', from_json=ShipDecalSwapPair.from_json, to_json=ShipDecalSwapPair.to_json
        ),
    })
    super_mario_galaxy: ShipDecalSwapPair = dataclasses.field(default_factory=ShipDecalSwapPair, metadata={
        'reflection': FieldReflection[ShipDecalSwapPair](
            ShipDecalSwapPair, id=0x59b4b241, original_name='SuperMarioGalaxy', from_json=ShipDecalSwapPair.from_json, to_json=ShipDecalSwapPair.to_json
        ),
    })
    mario_party8: ShipDecalSwapPair = dataclasses.field(default_factory=ShipDecalSwapPair, metadata={
        'reflection': FieldReflection[ShipDecalSwapPair](
            ShipDecalSwapPair, id=0xb663308d, original_name='MarioParty8', from_json=ShipDecalSwapPair.from_json, to_json=ShipDecalSwapPair.to_json
        ),
    })
    excite_truck: ShipDecalSwapPair = dataclasses.field(default_factory=ShipDecalSwapPair, metadata={
        'reflection': FieldReflection[ShipDecalSwapPair](
            ShipDecalSwapPair, id=0x7640ad4c, original_name='ExciteTruck', from_json=ShipDecalSwapPair.from_json, to_json=ShipDecalSwapPair.to_json
        ),
    })
    legend_of_zelda_twilight_princess: ShipDecalSwapPair = dataclasses.field(default_factory=ShipDecalSwapPair, metadata={
        'reflection': FieldReflection[ShipDecalSwapPair](
            ShipDecalSwapPair, id=0x9b6ede52, original_name='LegendOfZeldaTwilightPrincess', from_json=ShipDecalSwapPair.from_json, to_json=ShipDecalSwapPair.to_json
        ),
    })
    super_smash_brothers_brawl: ShipDecalSwapPair = dataclasses.field(default_factory=ShipDecalSwapPair, metadata={
        'reflection': FieldReflection[ShipDecalSwapPair](
            ShipDecalSwapPair, id=0xea024af3, original_name='SuperSmashBrothersBrawl', from_json=ShipDecalSwapPair.from_json, to_json=ShipDecalSwapPair.to_json
        ),
    })
    wii_sports: ShipDecalSwapPair = dataclasses.field(default_factory=ShipDecalSwapPair, metadata={
        'reflection': FieldReflection[ShipDecalSwapPair](
            ShipDecalSwapPair, id=0xa3b7ee26, original_name='WiiSports', from_json=ShipDecalSwapPair.from_json, to_json=ShipDecalSwapPair.to_json
        ),
    })
    wii_play: ShipDecalSwapPair = dataclasses.field(default_factory=ShipDecalSwapPair, metadata={
        'reflection': FieldReflection[ShipDecalSwapPair](
            ShipDecalSwapPair, id=0xc7b1dd81, original_name='WiiPlay', from_json=ShipDecalSwapPair.from_json, to_json=ShipDecalSwapPair.to_json
        ),
    })
    wario_ware_smooth_moves: ShipDecalSwapPair = dataclasses.field(default_factory=ShipDecalSwapPair, metadata={
        'reflection': FieldReflection[ShipDecalSwapPair](
            ShipDecalSwapPair, id=0xd7c6638e, original_name='WarioWareSmoothMoves', from_json=ShipDecalSwapPair.from_json, to_json=ShipDecalSwapPair.to_json
        ),
    })
    metroid_prime3_1: ShipDecalSwapPair = dataclasses.field(default_factory=ShipDecalSwapPair, metadata={
        'reflection': FieldReflection[ShipDecalSwapPair](
            ShipDecalSwapPair, id=0x124974e5, original_name='MetroidPrime3_1', from_json=ShipDecalSwapPair.from_json, to_json=ShipDecalSwapPair.to_json
        ),
    })
    metroid_prime3_2: ShipDecalSwapPair = dataclasses.field(default_factory=ShipDecalSwapPair, metadata={
        'reflection': FieldReflection[ShipDecalSwapPair](
            ShipDecalSwapPair, id=0xf8cfa987, original_name='MetroidPrime3_2', from_json=ShipDecalSwapPair.from_json, to_json=ShipDecalSwapPair.to_json
        ),
    })
    metroid_prime_trilogy: ShipDecalSwapPair = dataclasses.field(default_factory=ShipDecalSwapPair, metadata={
        'reflection': FieldReflection[ShipDecalSwapPair](
            ShipDecalSwapPair, id=0xa77487d5, original_name='MetroidPrimeTrilogy', from_json=ShipDecalSwapPair.from_json, to_json=ShipDecalSwapPair.to_json
        ),
    })
    retro_studios: ShipDecalSwapPair = dataclasses.field(default_factory=ShipDecalSwapPair, metadata={
        'reflection': FieldReflection[ShipDecalSwapPair](
            ShipDecalSwapPair, id=0xe590a13e, original_name='RetroStudios', from_json=ShipDecalSwapPair.from_json, to_json=ShipDecalSwapPair.to_json
        ),
    })

    def get_name(self) -> str:
        return self.editor_properties.name

    def set_name(self, name: str) -> None:
        self.editor_properties.name = name

    @classmethod
    def object_type(cls) -> str:
        return 'SPDC'

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
        assert property_id == 0x15fbdf30
        paper_mario = ShipDecalSwapPair.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x59b4b241
        super_mario_galaxy = ShipDecalSwapPair.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xb663308d
        mario_party8 = ShipDecalSwapPair.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x7640ad4c
        excite_truck = ShipDecalSwapPair.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x9b6ede52
        legend_of_zelda_twilight_princess = ShipDecalSwapPair.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xea024af3
        super_smash_brothers_brawl = ShipDecalSwapPair.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa3b7ee26
        wii_sports = ShipDecalSwapPair.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xc7b1dd81
        wii_play = ShipDecalSwapPair.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xd7c6638e
        wario_ware_smooth_moves = ShipDecalSwapPair.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0x124974e5
        metroid_prime3_1 = ShipDecalSwapPair.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xf8cfa987
        metroid_prime3_2 = ShipDecalSwapPair.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xa77487d5
        metroid_prime_trilogy = ShipDecalSwapPair.from_stream(data, game, property_size)
    
        property_id, property_size = structs.BIG_LH.unpack(data.read(6))
        assert property_id == 0xe590a13e
        retro_studios = ShipDecalSwapPair.from_stream(data, game, property_size)
    
        return cls(editor_properties, paper_mario, super_mario_galaxy, mario_party8, excite_truck, legend_of_zelda_twilight_princess, super_smash_brothers_brawl, wii_sports, wii_play, wario_ware_smooth_moves, metroid_prime3_1, metroid_prime3_2, metroid_prime_trilogy, retro_studios)

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

        data.write(b'\x15\xfb\xdf0')  # 0x15fbdf30
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.paper_mario.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'Y\xb4\xb2A')  # 0x59b4b241
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.super_mario_galaxy.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xb6c0\x8d')  # 0xb663308d
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.mario_party8.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'v@\xadL')  # 0x7640ad4c
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.excite_truck.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x9bn\xdeR')  # 0x9b6ede52
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.legend_of_zelda_twilight_princess.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xea\x02J\xf3')  # 0xea024af3
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.super_smash_brothers_brawl.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa3\xb7\xee&')  # 0xa3b7ee26
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.wii_sports.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xc7\xb1\xdd\x81')  # 0xc7b1dd81
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.wii_play.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xd7\xc6c\x8e')  # 0xd7c6638e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.wario_ware_smooth_moves.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\x12It\xe5')  # 0x124974e5
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.metroid_prime3_1.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xf8\xcf\xa9\x87')  # 0xf8cfa987
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.metroid_prime3_2.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xa7t\x87\xd5')  # 0xa77487d5
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.metroid_prime_trilogy.to_stream(data, game)
        after = data.tell()
        data.seek(before)
        data.write(structs.BIG_H.pack(after - before - 2))
        data.seek(after)

        data.write(b'\xe5\x90\xa1>')  # 0xe590a13e
        before = data.tell()
        data.write(b'\x00\x00')  # size placeholder
        self.retro_studios.to_stream(data, game)
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
        json_data = typing.cast("ShipDecalControllerJson", data)
        return cls(
            editor_properties=EditorProperties.from_json(json_data['editor_properties']),
            paper_mario=ShipDecalSwapPair.from_json(json_data['paper_mario']),
            super_mario_galaxy=ShipDecalSwapPair.from_json(json_data['super_mario_galaxy']),
            mario_party8=ShipDecalSwapPair.from_json(json_data['mario_party8']),
            excite_truck=ShipDecalSwapPair.from_json(json_data['excite_truck']),
            legend_of_zelda_twilight_princess=ShipDecalSwapPair.from_json(json_data['legend_of_zelda_twilight_princess']),
            super_smash_brothers_brawl=ShipDecalSwapPair.from_json(json_data['super_smash_brothers_brawl']),
            wii_sports=ShipDecalSwapPair.from_json(json_data['wii_sports']),
            wii_play=ShipDecalSwapPair.from_json(json_data['wii_play']),
            wario_ware_smooth_moves=ShipDecalSwapPair.from_json(json_data['wario_ware_smooth_moves']),
            metroid_prime3_1=ShipDecalSwapPair.from_json(json_data['metroid_prime3_1']),
            metroid_prime3_2=ShipDecalSwapPair.from_json(json_data['metroid_prime3_2']),
            metroid_prime_trilogy=ShipDecalSwapPair.from_json(json_data['metroid_prime_trilogy']),
            retro_studios=ShipDecalSwapPair.from_json(json_data['retro_studios']),
        )

    def to_json(self) -> json_util.JsonObject:
        return {
            'editor_properties': self.editor_properties.to_json(),
            'paper_mario': self.paper_mario.to_json(),
            'super_mario_galaxy': self.super_mario_galaxy.to_json(),
            'mario_party8': self.mario_party8.to_json(),
            'excite_truck': self.excite_truck.to_json(),
            'legend_of_zelda_twilight_princess': self.legend_of_zelda_twilight_princess.to_json(),
            'super_smash_brothers_brawl': self.super_smash_brothers_brawl.to_json(),
            'wii_sports': self.wii_sports.to_json(),
            'wii_play': self.wii_play.to_json(),
            'wario_ware_smooth_moves': self.wario_ware_smooth_moves.to_json(),
            'metroid_prime3_1': self.metroid_prime3_1.to_json(),
            'metroid_prime3_2': self.metroid_prime3_2.to_json(),
            'metroid_prime_trilogy': self.metroid_prime_trilogy.to_json(),
            'retro_studios': self.retro_studios.to_json(),
        }

    def dependencies_for(self, asset_manager: AssetManager) -> Iterator[Dependency]:
        for method, field_name, field_type in [
            (self.paper_mario.dependencies_for, "paper_mario", "ShipDecalSwapPair"),
            (self.super_mario_galaxy.dependencies_for, "super_mario_galaxy", "ShipDecalSwapPair"),
            (self.mario_party8.dependencies_for, "mario_party8", "ShipDecalSwapPair"),
            (self.excite_truck.dependencies_for, "excite_truck", "ShipDecalSwapPair"),
            (self.legend_of_zelda_twilight_princess.dependencies_for, "legend_of_zelda_twilight_princess", "ShipDecalSwapPair"),
            (self.super_smash_brothers_brawl.dependencies_for, "super_smash_brothers_brawl", "ShipDecalSwapPair"),
            (self.wii_sports.dependencies_for, "wii_sports", "ShipDecalSwapPair"),
            (self.wii_play.dependencies_for, "wii_play", "ShipDecalSwapPair"),
            (self.wario_ware_smooth_moves.dependencies_for, "wario_ware_smooth_moves", "ShipDecalSwapPair"),
            (self.metroid_prime3_1.dependencies_for, "metroid_prime3_1", "ShipDecalSwapPair"),
            (self.metroid_prime3_2.dependencies_for, "metroid_prime3_2", "ShipDecalSwapPair"),
            (self.metroid_prime_trilogy.dependencies_for, "metroid_prime_trilogy", "ShipDecalSwapPair"),
            (self.retro_studios.dependencies_for, "retro_studios", "ShipDecalSwapPair"),
        ]:
            try:
                yield from method(asset_manager)
            except Exception as e:
                raise Exception(
                    f"Error finding dependencies for ShipDecalController.{field_name} ({field_type}): {e}"
                )


def _decode_editor_properties(data: typing.BinaryIO, game: Game, property_size: int) -> EditorProperties:
    return EditorProperties.from_stream(data, game, property_size)


def _decode_paper_mario(data: typing.BinaryIO, game: Game, property_size: int) -> ShipDecalSwapPair:
    return ShipDecalSwapPair.from_stream(data, game, property_size)


def _decode_super_mario_galaxy(data: typing.BinaryIO, game: Game, property_size: int) -> ShipDecalSwapPair:
    return ShipDecalSwapPair.from_stream(data, game, property_size)


def _decode_mario_party8(data: typing.BinaryIO, game: Game, property_size: int) -> ShipDecalSwapPair:
    return ShipDecalSwapPair.from_stream(data, game, property_size)


def _decode_excite_truck(data: typing.BinaryIO, game: Game, property_size: int) -> ShipDecalSwapPair:
    return ShipDecalSwapPair.from_stream(data, game, property_size)


def _decode_legend_of_zelda_twilight_princess(data: typing.BinaryIO, game: Game, property_size: int) -> ShipDecalSwapPair:
    return ShipDecalSwapPair.from_stream(data, game, property_size)


def _decode_super_smash_brothers_brawl(data: typing.BinaryIO, game: Game, property_size: int) -> ShipDecalSwapPair:
    return ShipDecalSwapPair.from_stream(data, game, property_size)


def _decode_wii_sports(data: typing.BinaryIO, game: Game, property_size: int) -> ShipDecalSwapPair:
    return ShipDecalSwapPair.from_stream(data, game, property_size)


def _decode_wii_play(data: typing.BinaryIO, game: Game, property_size: int) -> ShipDecalSwapPair:
    return ShipDecalSwapPair.from_stream(data, game, property_size)


def _decode_wario_ware_smooth_moves(data: typing.BinaryIO, game: Game, property_size: int) -> ShipDecalSwapPair:
    return ShipDecalSwapPair.from_stream(data, game, property_size)


def _decode_metroid_prime3_1(data: typing.BinaryIO, game: Game, property_size: int) -> ShipDecalSwapPair:
    return ShipDecalSwapPair.from_stream(data, game, property_size)


def _decode_metroid_prime3_2(data: typing.BinaryIO, game: Game, property_size: int) -> ShipDecalSwapPair:
    return ShipDecalSwapPair.from_stream(data, game, property_size)


def _decode_metroid_prime_trilogy(data: typing.BinaryIO, game: Game, property_size: int) -> ShipDecalSwapPair:
    return ShipDecalSwapPair.from_stream(data, game, property_size)


def _decode_retro_studios(data: typing.BinaryIO, game: Game, property_size: int) -> ShipDecalSwapPair:
    return ShipDecalSwapPair.from_stream(data, game, property_size)


_property_decoder: dict[int, tuple[str, typing.Callable[[typing.BinaryIO, Game, int], typing.Any]]] = {
    0x255a4580: ('editor_properties', _decode_editor_properties),
    0x15fbdf30: ('paper_mario', _decode_paper_mario),
    0x59b4b241: ('super_mario_galaxy', _decode_super_mario_galaxy),
    0xb663308d: ('mario_party8', _decode_mario_party8),
    0x7640ad4c: ('excite_truck', _decode_excite_truck),
    0x9b6ede52: ('legend_of_zelda_twilight_princess', _decode_legend_of_zelda_twilight_princess),
    0xea024af3: ('super_smash_brothers_brawl', _decode_super_smash_brothers_brawl),
    0xa3b7ee26: ('wii_sports', _decode_wii_sports),
    0xc7b1dd81: ('wii_play', _decode_wii_play),
    0xd7c6638e: ('wario_ware_smooth_moves', _decode_wario_ware_smooth_moves),
    0x124974e5: ('metroid_prime3_1', _decode_metroid_prime3_1),
    0xf8cfa987: ('metroid_prime3_2', _decode_metroid_prime3_2),
    0xa77487d5: ('metroid_prime_trilogy', _decode_metroid_prime_trilogy),
    0xe590a13e: ('retro_studios', _decode_retro_studios),
}
