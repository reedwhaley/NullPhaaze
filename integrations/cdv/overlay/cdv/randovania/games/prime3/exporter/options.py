# These are the frontend's Corruption export options. Preserve their serialized
# names/defaults so an old preset does not quietly select different backend behavior.
# Boundary names here: CorruptionPerGameOptions.
from __future__ import annotations

import dataclasses
from pathlib import Path
from typing import Self

from randovania.game.game_enum import RandovaniaGame
from randovania.games.prime3.exporter.game_exporter import CorruptionOutputFormats
from randovania.interface_common.options import PerGameOptions, decode_if_not_none


@dataclasses.dataclass(frozen=True)
class CorruptionPerGameOptions(PerGameOptions):
    input_path: Path | None = None
    output_path: Path | None = None
    output_format: CorruptionOutputFormats = CorruptionOutputFormats.ISO
    use_external_models: frozenset[str] = frozenset()

    @property
    def as_json(self) -> dict:
        return {
            **super().as_json,
            "input_path": str(self.input_path) if self.input_path is not None else None,
            "output_path": str(self.output_path) if self.output_path is not None else None,
            "use_external_models": sorted(self.use_external_models),
        }

    @classmethod
    def from_json(cls, value: dict) -> Self:
        game = RandovaniaGame.METROID_PRIME_CORRUPTION
        cosmetic_patches = game.data.layout.cosmetic_patches.from_json(value["cosmetic_patches"])
        return cls(
            cosmetic_patches=cosmetic_patches,
            input_path=decode_if_not_none(value["input_path"], Path),
            output_path=decode_if_not_none(value["output_path"], Path),
            use_external_models=frozenset(value.get("use_external_models", [])),
        )
