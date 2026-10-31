# Choose the account-claimed, exported Corruption world and construct one CP3W delivery
# owner. The selected manifest/profile must agree with the loaded world before queue
# reconciliation. Boundary names here: Prime3MultiworldConnectorBuilder.
from __future__ import annotations

import asyncio
import json
from pathlib import Path

from randovania.game_connection.builder.connector_builder import ConnectorBuilder
from randovania.game_connection.connector_builder_choice import ConnectorBuilderChoice
from randovania.game_connection.prime3_multiworld_client import Prime3MultiworldClient
from randovania.network_common.error import BaseNetworkError, NotLoggedInError
from randovania.network_client.network_client import UnableToConnect


class Prime3MultiworldConnectorBuilder(ConnectorBuilder):
    def __init__(self, ip: str, manifest_path: str | None = None,
                 ledger_directory: str = "", port: int = 43674):
        super().__init__()
        self.ip, self.port = ip, port
        self.manifest_path = Path(manifest_path) if manifest_path else None
        self.ledger_directory = Path(ledger_directory)
        self.manifest_provider = None
        self.manifest = None
        self.status = "Waiting for the matching Corruption multiworld export"
        try:
            self.validate_configuration()
        except (OSError, ValueError, KeyError, TypeError) as error:
            # A moved/deleted manifest must not crash CDV while restoring its
            # saved connection builders. The connection panel retains the path
            # and shows the repairable configuration error.
            self.status = f"Restore or reselect the multiworld manifest: {error}"

    def validate_configuration(self):
        import ipaddress

        address = ipaddress.IPv4Address(self.ip)
        if address.is_multicast or address.is_unspecified or int(address) == 0xFFFFFFFF:
            raise ValueError("Use an explicit unicast console address")
        if not 1 <= self.port <= 65535:
            raise ValueError("Invalid UDP port")
        if self.manifest_path is None:
            self.status = "Waiting for login and a claimed Corruption world"
            return
        manifest = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        Prime3MultiworldClient(self.ip, manifest, port=self.port)  # No socket.
        self.manifest = manifest

    @property
    def connector_builder_choice(self):
        return ConnectorBuilderChoice.PRIME3_MULTIWORLD

    def configuration_params(self):
        params = {"ip": self.ip, "port": self.port,
                  "ledger_directory": str(self.ledger_directory)}
        if self.manifest_path is not None:
            params["manifest_path"] = str(self.manifest_path)
        return params

    def get_status_message(self):
        return self.status

    def _on_connection_lost(self, reason):
        self.status = str(reason)
        self.StatusUpdate.emit(self.status)

    async def build_connector(self):
        from randovania.game_connection.connector.prime3_multiworld_connector import Prime3MultiworldConnector

        client = None
        try:
            self.status = "Connecting to Corruption runtime..."
            self.StatusUpdate.emit(self.status)
            if self.manifest_path is None:
                if self.manifest_provider is None:
                    raise ValueError("Log in to multiworld and claim your Corruption world before connecting")
                manifests = await self.manifest_provider()
                if not manifests:
                    raise ValueError("Open the multiworld session window and claim your generated Corruption world.")
                if len(manifests) > 20:
                    raise ValueError("Too many claimed Corruption worlds; unclaim unused worlds before connecting")
                # Validate every candidate before opening a socket. These are
                # server-authorized seed recipes, never arbitrary memory writes.
                for manifest in manifests:
                    Prime3MultiworldClient(self.ip, manifest, port=self.port)
                client = Prime3MultiworldClient(self.ip, manifests[0], port=self.port)
            else:
                if self.manifest is None:
                    self.validate_configuration()
                client = Prime3MultiworldClient(self.ip, self.manifest, port=self.port)
            await client.connect()
            if self.manifest_path is None:
                await client.select_world(manifests)
            else:
                await client.status()  # Full identity/capability gate before publishing.
            self.manifest = client.manifest
            ledger = self.ledger_directory / (client.manifest["world_uuid"] + ".json")
            connector = Prime3MultiworldConnector(client, ledger)
            connector.ConnectionLost.connect(self._on_connection_lost)
        except asyncio.CancelledError:
            if client is not None:
                client.close()
            raise
        except (OSError, ValueError, KeyError, TypeError, BaseNetworkError, UnableToConnect) as error:
            if client is not None:
                client.close()
            self.status = ("Log in to multiworld and claim your Corruption world before connecting"
                           if isinstance(error, NotLoggedInError) else str(error))
            self.StatusUpdate.emit(self.status)
            return None
        # The connection manager publishes the connected state after registration.
        # Builder text is displayed only while there is no usable connector.
        self.status = "Runtime handshake complete"
        self.StatusUpdate.emit(self.status)
        connector._timer.start()
        return connector
