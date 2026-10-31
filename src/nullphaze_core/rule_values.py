# Selector/value evaluation stays independent of archive I/O. The same declared rule must
# resolve the same bounded value before a script record is touched. Boundary names here:
# pack, selected, Evaluator.
"""Declarative selector/value evaluation; no archive or script-format I/O."""

import random
import struct
from .binary import FormatError


def pack(fmt, *values):
    return struct.pack(">" + fmt, *values)


def selected(operation, area, layer, instance=None, connection=None):
    criteria = [("mrea_ids", area), ("layer_indexes", layer)]
    if instance is not None:
        criteria += [
            ("script_types", instance.kind),
            (
                "source_object_ids"
                if "source_object_ids" in operation
                else "object_ids",
                instance.identity,
            ),
        ]
    if connection is not None:
        criteria += [
            ("states", connection.state),
            ("messages", connection.message),
            ("target_ids", connection.target),
        ]
    return all(
        (not operation.get(key) or value in operation[key] for key, value in criteria)
    )


class Evaluator:
    def __init__(self, seed=None):
        self.random = random.Random(seed)
        self.cursors = {}
        self.propertyWrites = 0

    def value(self, expression, original):
        kind = expression["kind"]
        if kind == "BPropertyValue":
            return expression["value"]
        if kind == "U32AdditionPropertyValue":
            if len(original) < 4:
                raise FormatError("Truncated arithmetic property")
            return pack(
                "I",
                int.from_bytes(original[:4], "big")
                + int.from_bytes(expression["value"], "big")
                & 4294967295,
            )
        if kind == "RandomColorPropertyValue":
            return pack("4f", *(self.random.randrange(256) / 255 for _ in range(4)))
        if kind == "RepeatPropertyValue":
            values = expression["property_values"]
            if not values:
                raise FormatError("Empty repeating property rule")
            identity = id(expression)
            cursor = self.cursors.get(identity, 0)
            result = values[cursor]
            self.cursors[identity] = (cursor + 1) % len(values)
            return result
        raise FormatError("Unknown property expression: " + kind)
