# Use one endpoint owner, a paced request lock and validated CP3W frames. Reuse the request
# ID across timeout retries; CRC/length checks precede discarding a stale response. Boundary
# names here: Prime3TrackerClient.
"""Paced, opt-in console telemetry. No RAM access, delivery, or save commands."""

from __future__ import annotations

import asyncio
import ipaddress
import secrets
import socket
import struct
import weakref

from randovania.game_connection import prime3_wii_tracker_protocol as wire


class Prime3TrackerClient:
    _owners = weakref.WeakValueDictionary()
    hello_name = b"Nullphaze read-only"

    def _request(self, command, request_id, payload):
        return wire.request(command, request_id, payload)

    def _hello_capabilities(self):
        return 15 | wire.CAPABILITY

    def _validate_capabilities(self, caps, accepted):
        if not caps & wire.CAPABILITY or not accepted & wire.CAPABILITY or caps & (1 << 13):
            raise wire.TrackerProtocolError("Read-only tracker runtime required")

    def __init__(self, ip: str, profile_hex: str, *, port: int = 43674):
        address = ipaddress.IPv4Address(ip)
        if address.is_multicast or address.is_unspecified or int(address) == 0xFFFFFFFF:
            raise ValueError("Use an explicit unicast console address")
        self.profile = bytes.fromhex(profile_hex)
        wire.validate_profile(self.profile)
        if not 1 <= port <= 65535:
            raise ValueError("Invalid UDP port")
        self.endpoint = (str(address), port)
        self.socket = None
        self.request_id = 0
        self.session = 0
        self.lock = asyncio.Lock()

    async def _exchange(self, command, payload=b"", *, retries=3):
        # Build once for all retries. A lost reply does not tell us whether the
        # game handled the first packet; changing its ID would create a second
        # request instead of retrying the one whose result is still unknown.
        self.request_id += 1
        request_id = self.request_id
        packet = self._request(command, request_id, payload)
        loop = asyncio.get_running_loop()
        for _ in range(retries):
            await loop.sock_sendall(self.socket, packet)
            deadline = loop.time() + 5
            while loop.time() < deadline:
                try:
                    raw = await asyncio.wait_for(loop.sock_recv(self.socket, 2048), deadline - loop.time())
                except TimeoutError:
                    break
                except ConnectionResetError:
                    if command != 1:
                        raise
                    # Windows reports an unbound startup UDP port as ICMP reset.
                    await asyncio.sleep(1)
                    break
                # Validate even stale frames before ignoring delayed replies.
                if len(raw) < 20:
                    raise wire.TrackerProtocolError("Short response")
                actual_id = int.from_bytes(raw[8:12], "big")
                # Check the envelope, declared length and CRC before treating
                # a packet as stale. An old request ID does not excuse corrupt
                # data from the current peer.
                try:
                    decoded = wire.response(raw, raw[6], actual_id)
                except wire.RuntimeRequestRejected:
                    # An abandoned snapshot page can reject after a later
                    # update has already begun. Its validated error belongs
                    # only to that older request, just like a stale success.
                    if actual_id < request_id:
                        continue
                    raise
                if actual_id < request_id:
                    continue
                if actual_id != request_id or raw[6] != command:
                    raise wire.TrackerProtocolError("Unexpected response")
                # The runtime already paces its asynchronous receive/send
                # state machine. The caller's lock keeps one request in flight;
                # Use the requested half-second pacing rather than accumulating
                # the former full second after every page/grant.
                await asyncio.sleep(0.5)
                return decoded
        raise TimeoutError(
            f"Console telemetry timed out (CP3W command {command}, request {request_id}, {retries} attempts)"
        )

    async def _drain_hello(self, payload):
        loop = asyncio.get_running_loop()
        deadline = loop.time() + 90
        while loop.time() < deadline:
            try:
                raw = await asyncio.wait_for(loop.sock_recv(self.socket, 2048), min(5, deadline - loop.time()))
            except TimeoutError:
                return
            if wire.response(raw, 1, self.request_id) != payload:
                raise wire.TrackerProtocolError("Delayed HELLO changed session")
        raise TimeoutError("Startup HELLO queue did not become quiet")

    async def connect(self):
        async with self.lock:
            self.close()
            owner = self._owners.get(self.endpoint)
            # Telemetry and delivery share the same console session. A second
            # client could replace the runtime peer/session while the first
            # still owns a pending grant or a two-page snapshot.
            if owner is not None and owner is not self:
                raise ValueError("This CP3W endpoint already has a tracker/delivery connection")
            self._owners[self.endpoint] = self
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.setblocking(False)
            self.socket.connect(self.endpoint)
            self.request_id = 0
            try:
                name = self.hello_name
                nonce = secrets.randbits(32)
                hello = struct.pack(">BBII", 1, 1, self._hello_capabilities(), nonce) + bytes([len(name)]) + name
                # Retry the SAME nonce and request ID while startup completes.
                payload = await self._exchange(1, hello, retries=200)
                if len(payload) < 20:
                    raise wire.TrackerProtocolError("Short HELLO")
                version, caps, accepted, session, build, mode, metadata = struct.unpack_from(">BIIIIBB", payload)
                if (version, mode, metadata) != (1, 19, 1) or not session:
                    raise wire.TrackerProtocolError("Unsupported tracker runtime")
                self._validate_capabilities(caps, accepted)
                if len(payload) != 20 + payload[19] or payload[19] > 31:
                    raise wire.TrackerProtocolError("Invalid HELLO name")
                canonical = struct.pack(">BIIII", version, nonce, build, caps, accepted)
                if wire.zlib.crc32(canonical) != session:
                    raise wire.TrackerProtocolError("HELLO session mismatch")
                self.session = session
                await self._drain_hello(payload)
            except BaseException:
                self.close()
                raise

    async def snapshot(self):
        async with self.lock:
            if not self.session:
                raise wire.TrackerProtocolError("Not negotiated")
            chunks = []
            token = 0
            for index in range(2):
                payload = struct.pack(">I", self.session) + self.profile + struct.pack(">II", token, index)
                received = await self._exchange(wire.SNAPSHOT_COMMAND, payload)
                token, chunk = wire.page(received, self.profile, self.session, token, index)
                chunks.append(chunk)
            return wire.Snapshot.decode(b"".join(chunks))

    def close(self):
        if self._owners.get(self.endpoint) is self:
            del self._owners[self.endpoint]
        if self.socket is not None:
            if self.session:
                try:
                    self.socket.send(wire.request(4, self.request_id + 1))
                except OSError:
                    pass
            self.socket.close()
        self.socket = None
        self.session = 0
