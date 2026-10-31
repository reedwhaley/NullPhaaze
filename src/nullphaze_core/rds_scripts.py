# Resolve the named property through the generated decoder and edit only its observed span.
# Whole-object rebuilding could add absent defaults or change unrelated encodings. Boundary
# names here: FieldStream, preserved_legacy_enums, prepare_readers, decode_fields,
# RdsEvaluator.
"""Resolve concrete property spans through the pinned generated RDS readers.

I keep the original encoding and change only the named field span. Rebuilding
the whole typed object would insert defaults and canonicalize unrelated fields.
These decoder hooks are private API, so the corrected RDS pin is required.
"""

import inspect
import io
import struct
import sys
import dataclasses
import threading
from contextlib import contextmanager
from collections import Counter
from dataclasses import replace
from types import SimpleNamespace
from retro_data_structures.game_check import Game
from retro_data_structures.properties import get_game_object
from retro_data_structures.formats.script_layer import SCLY
from retro_data_structures.formats.script_object import (
    ScriptInstanceRaw,
    InstanceId,
    Connection,
)
from retro_data_structures.enums.helper import STATE_PER_GAME, MESSAGE_PER_GAME
from .rule_values import selected, Evaluator
from .binary import FormatError

GAME = Game.CORRUPTION


class FieldStream(io.BytesIO):
    """Observe only schema decoder header reads, never search arbitrary payloads."""

    def __init__(self, data):
        super().__init__(data)
        self.fields = []

    def read(self, size=-1):
        start = self.tell()
        value = super().read(size)
        if size == 6 and len(value) == 6:
            frame = inspect.currentframe().f_back
            decoders = frame.f_globals.get("_property_decoder", {})
            if frame.f_code.co_name in ("from_stream", "_fast_decode"):
                identity, length = struct.unpack(">IH", value)
                if identity in decoders:
                    name, _ = decoders[identity]
                    self.fields.append(
                        dict(
                            id=identity,
                            start=start + 6,
                            end=start + 6 + length,
                            name=name,
                            schema=frame.f_globals["__name__"],
                        )
                    )
        return value


@contextmanager
def preserved_legacy_enums(kind):
    # These two exact legacy encodings are retained as unnamed values. No
    # runtime meaning or replacement item is inferred for either encoding.
    if kind not in ("CRLY", "PCKP"):
        yield
        return
    from retro_data_structures.enums.corruption import PlayerItemEnum
    from retro_data_structures.properties.corruption.archetypes.ConditionalTest import (
        AmountOrCapacity,
    )

    changes = []
    try:
        for cls, allowed in (
            (
                PlayerItemEnum,
                {1462373658} if kind == "CRLY" else {0xFFFFFFFF},
            ),
            (AmountOrCapacity, {0xFFFFFFFF}),
        ):
            previous = cls.__dict__.get("_missing_")
            changes.append((cls, previous))

            def missing(enum_cls, value, allowed=allowed):
                if value not in allowed:
                    return None
                result = int.__new__(enum_cls, value)
                result._name_ = f"PreservedUnknown_{value:08X}"
                result._value_ = value
                return result

            cls._missing_ = classmethod(missing)
        yield
    finally:
        for cls, previous in changes:
            if previous is None:
                delattr(cls, "_missing_")
            else:
                cls._missing_ = previous


_prepared = set()


def prepare_readers(cls):
    if cls in _prepared:
        return
    _prepared.add(cls)
    # The generated slow path verifies the same headers and sizes and exposes
    # field boundaries. Packed fast readers can read many headers in one call.
    for name, module in list(sys.modules.items()):
        if not name.startswith("retro_data_structures.properties."):
            continue
        for value in list(vars(module).values()):
            if (
                isinstance(value, type)
                and dataclasses.is_dataclass(value)
                and "_fast_decode" in vars(value)
            ):
                value._fast_decode = classmethod(lambda cls, *args, **kwargs: None)


_decoder_lock = threading.RLock()


def _decode_fields(kind, data):
    cls = get_game_object(GAME, kind)
    prepare_readers(cls)
    stream = FieldStream(data)
    with preserved_legacy_enums(kind):
        value = cls.from_stream(stream, GAME, len(data))
    if stream.tell() != len(data):
        raise FormatError(f"{kind}: trailing undecoded property bytes")
    for field in stream.fields:
        if field["end"] > len(data):
            raise FormatError("Schema field exceeds object")
        parents = [
            p["name"]
            for p in stream.fields
            if p["start"] < field["start"] and p["end"] >= field["end"]
        ]
        field["path"] = ".".join(parents + [field["name"]])
    return value, stream.fields


def decode_fields(kind, data):
    # Enum preservation is scoped to the exact legacy sentinels. Serialize
    # these reads so another export cannot observe a temporary enum override.
    with _decoder_lock:
        try:
            return _decode_fields(kind, data)
        except struct.error as error:
            raise FormatError(f'{kind}: truncated generated property record') from error


class RdsEvaluator(Evaluator):
    def __init__(self, seed=None):
        super().__init__(seed)
        self.resolutions = Counter()
        self.absent = Counter()

    def properties_for(self, kind, data, operations):
        if not operations:
            return data
        _, fields = decode_fields(kind, data)
        result = bytearray(data)
        for field in sorted(fields, key=lambda f: f["start"]):
            for operation in operations:
                if field["id"] != int.from_bytes(operation["property_id"], "big"):
                    continue
                start, end = field["start"], field["end"]
                value = self.value(
                    operation["property_value"], bytes(result[start:end])
                )
                if len(value) > end - start:
                    raise FormatError("Replacement exceeds schema field")
                result[start : start + len(value)] = value
                self.propertyWrites += 1
                self.resolutions[(kind, f"{field['id']:08X}", field["path"])] += 1
        for operation in operations:
            identity = int.from_bytes(operation["property_id"], "big")
            if not any(f["id"] == identity for f in fields):
                self.absent[(kind, f"{identity:08X}")] += 1
        # Strictly re-decode the edited object to validate values and framing.
        decode_fields(kind, bytes(result))
        return bytes(result)

