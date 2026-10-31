# Translate a validated read-only snapshot into the existing tracker resource model. A
# timeout makes telemetry unavailable; malformed/current-request failures retain their
# terminal handling. Boundary names here: Prime3WiiTrackerConnector.
"""Read-only CP3W source for the existing CDV item tracker."""

from __future__ import annotations

import logging

from PySide6 import QtCore

from randovania.game.game_enum import RandovaniaGame
from randovania.game_connection.connector.remote_connector import PlayerLocationEvent, RemoteConnector
from randovania.game_description import default_database
from randovania.game_description.resources.inventory import Inventory, InventoryItem
from randovania.interface_common.players_configuration import INVALID_UUID
from randovania.lib.infinite_timer import InfiniteTimer


class Prime3WiiTrackerConnector(RemoteConnector):
    ConnectionLost = QtCore.Signal(str)

    def __init__(self, client):
        super().__init__()
        self.client = client
        self._layout_uuid = INVALID_UUID  # Checkpoint identity is NOT a randomized layout UUID.
        self.game = default_database.game_description_for(RandovaniaGame.METROID_PRIME_CORRUPTION)
        self._disconnected = False
        self._timer = InfiniteTimer(self.update, 2.0)
        self.last_error = None

    @property
    def game_enum(self):
        return RandovaniaGame.METROID_PRIME_CORRUPTION

    def description(self):
        return "Prime 3 Wii: CP3W read-only tracker (no multiworld)"

    def is_disconnected(self):
        return self._disconnected

    async def force_finish(self):
        self._timer.stop()
        self.client.close()
        self._disconnected = True

    async def set_remote_pickups(self, remote_pickups):
        if remote_pickups:
            raise ValueError("This connection is read-only; item delivery is disabled")

    def inventory(self, snapshot):
        database = self.game.resource_database
        result = Inventory.empty()
        for item in database.item:
            index = item.extra["item_id"]
            if index >= 1000 or item.short_name in ("Fuses", "EnergyCellsUsed"):
                continue
            if not 0 <= index < len(snapshot.records):
                raise ValueError("Unknown tracker item ID")
            amount, capacity = snapshot.records[index]
            if item.short_name == "SuitType":
                if amount > item.max_capacity:
                    raise ValueError("Invalid suit enum")
                amount = capacity = int(amount >= 5)
            elif amount > capacity or capacity > item.max_capacity:
                raise ValueError(f"Invalid inventory for {item.short_name}")
            result[item] = InventoryItem(amount, capacity)
        used = [snapshot.records[53 + i][0] for i in range(9)]
        if any(value not in (0, 1) for value in used):
            raise ValueError("Invalid Energy Cell flags")
        total = sum(bool(result[database.get_item(f"Fuse{i + 1}")].amount or used[i]) for i in range(9))
        result[database.get_item("Fuses")] = InventoryItem(total - sum(used), total)
        result[database.get_item("EnergyCellsUsed")] = InventoryItem(sum(used), sum(used))
        return result

    async def update(self):
        if self._disconnected:
            return
        try:
            snapshot = await self.client.snapshot()
            self._publish_snapshot(snapshot)
        except TimeoutError as error:
            self._telemetry_unavailable(error)
        except (OSError, ValueError) as error:
            self.last_error = str(error)
            logging.getLogger(__name__).warning("CP3W tracker disconnected: %s", error)
            self.InventoryUpdated.emit(Inventory.empty())
            self.PlayerLocationChanged.emit(PlayerLocationEvent(None, None))
            await self.force_finish()
            self.ConnectionLost.emit(str(error))

    def _telemetry_unavailable(self, error):
        # Gameplay polling can stop during menus, scans and room/ship loads.
        # Silence is not proof that the negotiated peer/session was lost. Keep
        # the socket and let the next bounded update obtain a fresh sample.
        self.last_error = str(error)
        self.InventoryUpdated.emit(Inventory.empty())
        self.PlayerLocationChanged.emit(PlayerLocationEvent(None, None))

    def _publish_snapshot(self, snapshot):
        self.last_error = None
        if not snapshot.available:
            self.InventoryUpdated.emit(Inventory.empty())
            self.PlayerLocationChanged.emit(PlayerLocationEvent(None, None))
            return
        inventory = self.inventory(snapshot)
        region = next((r for r in self.game.region_list.regions if r.extra["asset_id"] == snapshot.world), None)
        if region is None:
            raise ValueError("Unknown tracker world")
        area = next((a for a in region.areas if a.extra.get("asset_id") == snapshot.area), None)
        self.InventoryUpdated.emit(inventory)
        self.PlayerLocationChanged.emit(PlayerLocationEvent(region, area))
