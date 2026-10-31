# Lower counter-indexed Wii particle tables to supported native expressions. Boundary names
# here: constant, binary, choose, table_lookup, lower_counter_curve.
"""Lower counter-indexed Wii particle tables to supported native expressions."""

import copy

from construct import Container


def constant(value):
    return Container(type="CNST", body=value)


def binary(kind, a, b):
    return Container(type=kind, body=Container(a=a, b=b))


def choose(counter, threshold, a, b):
    # CHAN compares its frame with an integer switch time. Adding that same
    # frame to threshold-counter expresses counter<threshold without changing
    # engine code. Leaves are constants, so CHAN's branch-local time is safe.
    frame = Container(type="TSCL", body=constant(1.0))
    switch = binary("ADD_", frame, binary("SUB_", constant(threshold), copy.deepcopy(counter)))
    return Container(type="CHAN", body=Container(a=a, b=b, c=switch))


def table_lookup(keys, counter, first=0):
    if len(keys) == 1:
        return Container(type="CNST", body=Container({axis: constant(v) for axis, v in zip("abcd", keys[0])}))
    middle = len(keys) // 2
    return choose(
        counter,
        first + middle,
        table_lookup(keys[:middle], counter, first),
        table_lookup(keys[middle:], counter, first + middle),
    )


def lower_counter_curve(expression):
    """Preserve the retail Wii KEYF integer-counter path, including loop seams.

    Source vector evaluation is verified at 0x803E53A0 in the standalone US
    Corruption DOL. After wrapping, interior keys interpolate to the next
    entry because the original cumulative count remains the interpolation input.
    """
    body = expression.body
    keys = body["keys"]
    if not (
        body.a == 2
        and body.g == 0.0
        and body.h == 1.0
        and body.f == 0
        and body.e == len(keys)
        and 1 <= len(keys) <= 512
        and body.i.type == "GTCP"
        and isinstance(keys[0], list)
        and len(keys[0]) in (3, 4)
    ):
        raise ValueError("Unsupported counter curve")
    counter = Container(type="GTCP", body=None)
    initial = table_lookup(keys, counter)
    if not body.c or len(keys) == 1:
        return initial
    wrapped = [keys[0], *keys[2:], keys[-1]]
    index = binary("MODU", copy.deepcopy(counter), constant(len(keys)))
    return choose(counter, len(keys), initial, table_lookup(wrapped, index))


def lower_counter_curves(value):
    count = 0
    if isinstance(value, dict):
        if value.get("type") == "KEYF":
            try:
                return lower_counter_curve(value), 1
            except ValueError:
                pass
        for key in list(value):
            if key != "_io":
                value[key], lowered = lower_counter_curves(value[key])
                count += lowered
    elif isinstance(value, list):
        for index, child in enumerate(value):
            value[index], lowered = lower_counter_curves(child)
            count += lowered
    return value, count
