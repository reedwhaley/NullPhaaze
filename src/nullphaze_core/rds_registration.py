# Generated strings receive explicit IDs and destination PAK membership. Register only the
# declared resources; a broad asset scan must not invent a dependency or duplicate
# registration. Boundary names here: AllowlistedProvider, register_generated.
"""Explicit registration of generated STRGs with the RDS asset manager."""

from pathlib import Path
from retro_data_structures.asset_manager import AssetManager
from retro_data_structures.file_provider import PathFileProvider
from retro_data_structures.game_check import Game
from retro_data_structures.base_resource import RawResource


class AllowlistedProvider(PathFileProvider):
    def __init__(self, source, archives):
        super().__init__(Path(source).parent)
        self.archives = tuple(archives)

    def rglob(self, pattern):
        if pattern == "*.pak":
            yield from self.archives
        else:
            raise ValueError("Only allowlisted PAK enumeration is supported")


def register_generated(source, archives, strings):
    manager = AssetManager(AllowlistedProvider(source, archives), Game.CORRUPTION)
    receipt = []
    for identity, resource in strings.items():
        name = f"nullphaze/generated/{identity:016X}.STRG"
        if manager.does_asset_exists(identity):
            if manager.get_asset_type(identity) != "STRG":
                raise ValueError("Generated string collides with non-STRG asset")
            actual = manager.replace_asset(
                identity, RawResource("STRG", resource.read())
            )
            mode = "replace"
        else:
            manager.register_custom_asset_name(name, identity)
            actual = manager.add_new_asset(name, RawResource("STRG", resource.read()))
            mode = "new"
        if actual != identity:
            raise AssertionError("Generated ID changed")
        dependencies = tuple(
            manager.get_dependencies_for_asset(identity, must_exist=True)
        )
        receipt.append(
            {
                "mode": mode,
                "id": f"{identity:016X}",
                "type": manager.get_asset_type(identity),
                "dependencies": [
                    {"id": f"{d.id:016X}", "type": d.type} for d in dependencies
                ],
            }
        )
    return manager, receipt
