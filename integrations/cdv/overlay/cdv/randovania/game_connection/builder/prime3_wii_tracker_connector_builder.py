# Construct the explicitly configured read-only CP3W tracker connection. Telemetry
# configuration does not itself authorize semantic item delivery. Boundary names here:
# Prime3WiiTrackerConnectorBuilder.
from __future__ import annotations

import asyncio

from randovania.game_connection.builder.connector_builder import ConnectorBuilder
from randovania.game_connection.connector_builder_choice import ConnectorBuilderChoice
from randovania.game_connection.prime3_wii_tracker_client import Prime3TrackerClient


class Prime3WiiTrackerConnectorBuilder(ConnectorBuilder):
    def __init__(self, ip: str, profile_hex: str, port: int = 43674):
        super().__init__()
        # Validate configuration before persisting it, without opening a socket.
        Prime3TrackerClient(ip, profile_hex, port=port)
        self.ip, self.profile_hex, self.port = ip, profile_hex, port
        self.status = "Waiting for read-only CP3W tracker"

    @property
    def connector_builder_choice(self):
        return ConnectorBuilderChoice.PRIME3_WII_TRACKER

    def configuration_params(self):
        return {"ip": self.ip, "profile_hex": self.profile_hex, "port": self.port}

    def get_status_message(self):
        return self.status

    def create_client(self):
        return Prime3TrackerClient(self.ip, self.profile_hex, port=self.port)

    async def build_connector(self):
        from randovania.game_connection.connector.prime3_wii_tracker_connector import (  # noqa: PLC0415
            Prime3WiiTrackerConnector,
        )

        client = self.create_client()
        self.status = "Waiting for console startup (read-only)"
        self.StatusUpdate.emit(self.status)
        try:
            await client.connect()
            connector = Prime3WiiTrackerConnector(client)
            # Verify the profile and complete page pair before publishing a connector.
            await client.snapshot()
        except asyncio.CancelledError:
            client.close()
            raise
        except (OSError, ValueError) as error:
            client.close()
            self.status = str(error)
            self.StatusUpdate.emit(self.status)
            return None
        self.status = "Connected: read-only CP3W, no item delivery"
        self.StatusUpdate.emit(self.status)
        connector._timer.start()
        return connector
