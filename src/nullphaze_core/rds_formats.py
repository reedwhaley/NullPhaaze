# These adapters retain source information that generic RDS readers normalize or discard.
# The private dependency pin is part of the contract, including unknown signals, padding and
# unused layer bits. Boundary names here: parse_exact, Signal, LosslessInstance,
# AlignedMrea, Flags.
"""Corruption format adapters for the pinned RDS 0.44.1 dependency.

RDS owns the resource framing. The exceptions here preserve source data that
the generic readers otherwise normalize or discard. Keep those exceptions
visible; a successful rebuild is not evidence that the game accepts an edit.
"""
from dataclasses import dataclass
import io
import importlib.metadata
import struct

import construct as cs
from retro_data_structures.formats import mlvl, script_object
from retro_data_structures.formats.mrea import MREAConstruct
from retro_data_structures.game_check import Game
from .binary import FormatError

PINNED_RDS = '0.44.1+nullphaze.20261024'
if importlib.metadata.version('retro-data-structures') != PINNED_RDS:
    raise RuntimeError('Install the vendored RDS wheel first; this migration requires ' + PINNED_RDS)

GAME = Game.CORRUPTION


def parse_exact(schema, data, *, padding=(0, 255)):
    """Read one bounded record and reject an unexplained trailing payload."""
    stream = io.BytesIO(data)
    try:
        result = schema.parse_stream(stream, target_game=GAME)
    except (cs.ConstructError, ValueError, KeyError, IndexError, AssertionError, struct.error) as error:
        raise FormatError(f'RDS could not read the Corruption record: {error}') from error
    if any(value not in padding for value in stream.read()):
        raise FormatError('Unexplained trailing resource bytes')
    return result


@dataclass(frozen=True)
class Signal:
    value: str


class LosslessInstance(script_object._ConstructScriptInstance):
    def _parse(self, stream, context, path):
        # The stock RDS instance reader drops connections with unknown enums.
        # I want those links retained, including dormant links we do not edit.
        # Use its raw record constructs and defer signal interpretation.
        header_schema, body_schema = script_object._EchoesRawScript
        header = header_schema.defersubcon._parsereport(stream, context, path)
        body = body_schema.defersubcon._parsereport(io.BytesIO(header.raw_data), context, path)
        return script_object.ScriptInstanceRaw(
            header.type, script_object.InstanceId(body.instance_id),
            tuple(script_object.Connection(Signal(c.state), Signal(c.message),
                                          script_object.InstanceId(c.target)) for c in body.connections),
            body.base_property,
        )


# Keep the public RDS layer layout, replacing only the lossy instance adapter.
from retro_data_structures.formats.script_layer import ConstructScriptLayer
SCRIPT_LAYER = ConstructScriptLayer('SCLY')
SCRIPT_LAYER.subcons[-1] = 'script_instances' / cs.PrefixedArray(cs.Int32ub, LosslessInstance())
SCRIPT_LAYER._subcons['script_instances'] = SCRIPT_LAYER.subcons[-1]


class AlignedMrea(MREAConstruct):
    def _encode_compressed_blocks(self, data_sections, category_starts, context, path):
        # RDS pads sections during compression but records their original sizes.
        # Count the padding in both places so the next section starts correctly.
        for index, section in enumerate(data_sections):
            data_sections[index] = section + bytes(-len(section) % 32)
        return super()._encode_compressed_blocks(data_sections, category_starts, context, path)


MREA = AlignedMrea()


class Flags(list):
    def __init__(self, values, original):
        super().__init__(values)
        self.original = original


class PreservedLayerFlags(mlvl.LayerFlags):
    def _decode(self, obj, context, path):
        full = list(reversed(obj.layer_flags))
        if obj.layer_count > 64:
            raise FormatError('World layer count exceeds 64-bit mask')
        return Flags(full[:obj.layer_count], full)

    def _encode(self, obj, context, path):
        # The unused high bits are source data too. RDS normally sets them all.
        flags = list(getattr(obj, 'original', [True] * 64))
        flags[:len(obj)] = obj
        return cs.Container(layer_count=len(obj), layer_flags=list(reversed(flags)))


MLVL = mlvl.create(0x19, mlvl.AssetId64)
for index, field in enumerate(MLVL.subcons):
    if field.name == 'area_layer_flags':
        MLVL.subcons[index] = 'area_layer_flags' / cs.PrefixedArray(cs.Int32ub, PreservedLayerFlags())
        MLVL._subcons['area_layer_flags'] = MLVL.subcons[index]


def read_world(data):
    # Retail PAK entries may carry one extra FF alignment block after MLVL.
    # Strip only that verified envelope, never arbitrary unknown trailing data.
    for extra in (0, 32):
        if extra and data[-extra:] != b'\xff' * extra:
            continue
        candidate = data[:-extra] if extra else data
        try:
            return parse_exact(MLVL, candidate), extra
        except FormatError:
            if extra:
                raise
    raise FormatError('Unsupported Corruption world envelope')
