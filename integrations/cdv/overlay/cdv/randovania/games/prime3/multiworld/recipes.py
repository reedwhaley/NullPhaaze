# Compile the exported pickup into bounded logical resource operations. The runtime table
# owns the native IDs/limits; network input never supplies a memory address or arbitrary
# mutator call. Boundary names here: Recipe, compile_recipe, evaluate, recipe_words,
# resource_limits.
"""Compile seed pickups into bounded resource operations, never addresses.

Resource indices here are CDV indices. They are not native CPlayerState indices.
The native adapter must translate through the compiled resource table, including
the suit enum, acquired/spent cells and persisted launcher/locked-ammo state.
"""
from __future__ import annotations

from dataclasses import dataclass

from randovania.game.game_enum import RandovaniaGame
from randovania.game_description import default_database
from randovania.game_description.resources.item_resource_info import ItemResourceInfo

MAX_STAGES = 4
MAX_EXTRAS = 8
RESOURCE_COUNT = 63
# Stat counters and transient engine modes are not item-delivery operations.
ITEM_RESOURCES = frozenset(range(19)) | frozenset(range(20, 36)) | {37, 38, 39, 43, 44, 46, 59, 60, 61, 62}


@dataclass(frozen=True)
class Recipe:
    progression: tuple[tuple[int, int], ...]
    extra: tuple[tuple[int, int], ...]
    lock: tuple[int, int, int] | None
    respects_lock: bool
    unlocks: bool


def compile_recipe(pickup) -> Recipe:
    database = default_database.resource_database_for(RandovaniaGame.METROID_PRIME_CORRUPTION)

    def resource(item):
        if (not isinstance(item, ItemResourceInfo) or item.resource_index not in ITEM_RESOURCES
                or database.item[item.resource_index] != item):
            raise ValueError(f"Unsupported Corruption item resource: {item}")
        return item.resource_index

    def gains(values):
        result = []
        for item, quantity in values:
            index = resource(item)
            if type(quantity) is not int or not 0 <= quantity <= item.max_capacity:
                raise ValueError("Pickup quantity exceeds compiled resource bounds")
            result.append((index, quantity))
        return tuple(result)

    progression, extra = gains(pickup.progression), gains(pickup.extra_resources)
    if len(progression) > MAX_STAGES or len(extra) > MAX_EXTRAS:
        raise ValueError("Pickup exceeds the bounded Corruption recipe format")
    lock = None
    if pickup.resource_lock is not None:
        lock = tuple(resource(item) for item in (
            pickup.resource_lock.locked_by, pickup.resource_lock.item_to_lock, pickup.resource_lock.temporary_item
        ))
        if lock not in ((59, 4, 61), (60, 44, 62)):
            raise ValueError("Unsupported Corruption launcher lock")
    if pickup.unlocks_resource and lock is None:
        raise ValueError("Unlocking pickup has no launcher lock")
    return Recipe(progression, extra, lock, pickup.respects_lock, pickup.unlocks_resource)


def evaluate(recipe: Recipe, capacities: tuple[int, ...]) -> tuple[int, ...]:
    """Reference for the bounded native planner; returns saturated logical capacities.

    This is not a live connector and performs no memory writes. Receipt/inventory
    coupling and the native special-item adapter remain responsible for applying it.
    """
    database = default_database.resource_database_for(RandovaniaGame.METROID_PRIME_CORRUPTION)
    limits = tuple(item.max_capacity for item in database.item)
    # Shield presence is boolean even though the native suit enum has six states.
    limits = limits[:17] + (1,) + limits[18:]
    if len(capacities) != RESOURCE_COUNT or any(type(n) is not int or not 0 <= n <= limit
                                               for n, limit in zip(capacities, limits, strict=True)):
        raise ValueError("Invalid logical Corruption inventory")
    result = list(capacities)
    gains = list(recipe.extra)
    if recipe.progression:
        stage = 0
        while stage + 1 < len(recipe.progression) and capacities[recipe.progression[stage][0]] > 0:
            stage += 1
        gains.insert(0, recipe.progression[stage])
    locked = recipe.lock is not None and recipe.respects_lock and not recipe.unlocks and capacities[recipe.lock[0]] == 0
    for index, quantity in gains:
        if locked and index == recipe.lock[1]:
            index = recipe.lock[2]
        result[index] = min(limits[index], result[index] + quantity)
    if recipe.unlocks:
        launcher, target, temporary = recipe.lock
        result[launcher] = 1
        result[target] = min(limits[target], result[target] + result[temporary])
        result[temporary] = 0
    return tuple(result)


def recipe_words(recipe: Recipe) -> tuple[int, ...]:
    """Stable, pointer-free C layout; populated only by the seed compiler."""
    lock = recipe.lock or (0, 0, 0)
    return (len(recipe.progression), len(recipe.extra), int(recipe.respects_lock), int(recipe.unlocks),
            *lock, *(n for pair in recipe.progression for n in pair),
            *(0 for _ in range(2 * (MAX_STAGES - len(recipe.progression)))),
            *(n for pair in recipe.extra for n in pair),
            *(0 for _ in range(2 * (MAX_EXTRAS - len(recipe.extra)))))


def resource_limits() -> tuple[int, ...]:
    database = default_database.resource_database_for(RandovaniaGame.METROID_PRIME_CORRUPTION)
    return tuple(1 if item.resource_index == 17 else item.max_capacity for item in database.item)
