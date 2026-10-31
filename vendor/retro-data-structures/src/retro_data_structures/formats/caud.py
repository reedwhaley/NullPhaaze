"""Corruption CAUD v9 framing and sample dependencies; opaque header facts retained."""

from __future__ import annotations

import typing

import construct as c

from retro_data_structures.base_resource import BaseResource, Dependency

CAUD = c.Struct(
    "magic" / c.Const(b"CAUD"),
    "version" / c.Const(9, c.Int32ub),
    "name" / c.CString("utf-8"),
    "volume_groups" / c.PrefixedArray(c.Int32ub, c.CString("utf-8")),
    "unknown_header" / c.Bytes(20),
    "samples"
    / c.PrefixedArray(
        c.Int32ub,
        c.Prefixed(
            c.Int32ub,
            c.Struct(
                "sample_id" / c.Int64ub,
                "unknown_data" / c.GreedyBytes,
            ),
        ),
    ),
    "trailing_padding" / c.Default(c.GreedyBytes, b""),
    c.Check(lambda x: all(v in (0, 255) for v in x.trailing_padding)),
)


class Caud(BaseResource):
    @classmethod
    def resource_type(cls):
        return "CAUD"

    @classmethod
    def construct_class(cls, target_game):
        return CAUD

    def dependencies_for(self) -> typing.Iterator[Dependency]:
        for sample in self.raw.samples:
            if self.target_game.is_valid_asset_id(sample.sample_id):
                yield from self.asset_manager.get_dependencies_for_asset(sample.sample_id, must_exist=True)
