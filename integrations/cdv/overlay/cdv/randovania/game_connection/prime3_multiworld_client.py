# One negotiated CP3W session carries status and seed-authorized delivery. Retry the same
# request after a missing reply and check the returned owner generation before accepting its
# receipt. Boundary names here: Prime3MultiworldClient.
"""One CP3W session carries both telemetry and semantic item delivery."""
from __future__ import annotations

import struct
import zlib

from randovania.game_connection import prime3_multiworld_protocol as mw
from randovania.game_connection import prime3_wii_tracker_protocol as tracker
from randovania.game_connection.prime3_wii_tracker_client import Prime3TrackerClient
from randovania.games.prime3.multiworld.manifest import validate_manifest


class Prime3MultiworldClient(Prime3TrackerClient):
    hello_name = b"Nullphaze multiworld"

    def __init__(self, ip: str, manifest: dict, *, port: int = 43674):
        validate_manifest(manifest)
        self.manifest = manifest
        super().__init__(ip, manifest["checkpoint_profile"], port=port)

    def _hello_capabilities(self):
        return super()._hello_capabilities() | mw.CAPABILITY

    def _validate_capabilities(self, caps, accepted):
        required = tracker.CAPABILITY | mw.CAPABILITY
        if caps & required != required or accepted & required != required:
            raise tracker.TrackerProtocolError("This export does not advertise Corruption multiworld support")

    def _request(self, command, request_id, payload):
        if command not in (mw.STATUS_COMMAND, mw.DELIVER_COMMAND):
            return super()._request(command, request_id, payload)
        raw = tracker.HEADER.pack(b"CP3W", 1, 1, command, 0, request_id, len(payload)) + payload
        return raw + struct.pack(">I", zlib.crc32(raw))

    async def select_world(self, manifests: list[dict]):
        """Read-only identity probes within one negotiated runtime connection."""
        for manifest in manifests:
            validate_manifest(manifest)
            self.manifest = manifest
            self.profile = bytes.fromhex(manifest["checkpoint_profile"])
            try:
                return await self.status()
            except tracker.RuntimeRequestRejected as error:
                # The runtime returns 10 for an unmatched bound profile. Other
                # errors, malformed replies and identity conflicts fail closed.
                if error.status != 10:
                    raise
        raise tracker.TrackerProtocolError(
            "This game does not match a Corruption world claimed by your account. "
            "Claim the exported world in its session and load the matching game."
        )

    async def status(self):
        # The negotiated UDP peer identifies a session, not the loaded save.
        # I check world/seed/slot again here before the ledger can choose an
        # item. A reachable console can still have the wrong world loaded.
        async with self.lock:
            if not self.session:
                raise tracker.TrackerProtocolError("Not negotiated")
            raw = await self._exchange(mw.STATUS_COMMAND, struct.pack(">I", self.session) + self.profile)
            status = mw.MultiworldStatus.decode(raw)
            expected = {key: self.manifest[key] for key in ("world_uuid", "seed_fingerprint", "save_slot")}
            if status.binding != expected:
                raise tracker.TrackerProtocolError("Runtime belongs to another world, seed or save slot")
            return status

    async def deliver(self, status, sequence, recipe):
        # Send a seed-authorized recipe key, never an address, item-ID/amount
        # pair or model ID. The exported native table owns the actual grant.
        if recipe not in self.manifest["incoming_recipes"]:
            raise ValueError("Pickup is not authorized by this seed")
        async with self.lock:
            if not self.session:
                raise tracker.TrackerProtocolError("Not negotiated")
            request = struct.pack(">I", self.session) + self.profile + mw.delivery_request(status, sequence, recipe)
            # Timeout retry retains the identical sequence, recipe and request
            # ID. A response alone is never treated as a durable-save ACK.
            raw = await self._exchange(mw.DELIVER_COMMAND, request)
            result = mw.MultiworldStatus.decode(raw)
            if result.binding != status.binding or result.generation != status.generation:
                raise tracker.TrackerProtocolError("Save owner changed while delivering")
            return result
