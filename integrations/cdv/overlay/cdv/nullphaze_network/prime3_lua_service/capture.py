# Observe retail Print arguments through Dolphin's debugger (no game memory writes).
# Boundary names here: Remote, resume_and_disconnect, parse_trace, snapshot, main.
"""Observe retail Print arguments through Dolphin's debugger (no game memory writes)."""

from __future__ import annotations

import argparse
import json
import math
import os
import socket
import struct
import sys
import time
from pathlib import Path

if __package__ in {None, ""}:
    _repository_root = os.fspath(Path(__file__).resolve().parents[2])
    if _repository_root not in sys.path:
        sys.path.insert(0, _repository_root)

from nullphaze_network.prime3_lua_service.probe import verify_image

PRINT_ADDRESS = 0x80223538
ITEMS = ("PowerBeam", "Missile", "Energy", "ShipMissile", "SeekerMissile")
ITEM_IDS = (0, 4, 18, 45, 6)
GAME_STATE_POINTER = 0x8067DC0C


class Remote:
    def __init__(self, connection: socket.socket):
        self.connection = connection

    def receive(self) -> str:
        while True:
            byte = self.connection.recv(1)
            if not byte:
                raise EOFError("Debugger disconnected")
            if byte == b"$":
                break
        # A timeout before a packet is harmless; a partial packet must be read
        # completely rather than discarded by the caller's idle timeout loop.
        timeout = self.connection.gettimeout()
        self.connection.settimeout(10)
        packet = bytearray()
        while True:
            byte = self.connection.recv(1)
            if not byte:
                raise EOFError("Debugger disconnected mid-packet")
            if byte == b"#":
                break
            packet.extend(byte)
            if len(packet) > 20000:
                raise ValueError("Debugger packet exceeds limit")
        checksum = b""
        while len(checksum) < 2:
            chunk = self.connection.recv(2 - len(checksum))
            if not chunk:
                raise EOFError("Debugger disconnected before checksum")
            checksum += chunk
        if sum(packet) % 256 != int(checksum, 16):
            self.connection.sendall(b"-")
            raise ValueError("Debugger checksum mismatch")
        self.connection.sendall(b"+")
        self.connection.settimeout(timeout)
        return packet.decode("ascii")

    def send(self, command: str) -> None:
        raw = command.encode("ascii")
        self.connection.sendall(b"$" + raw + b"#" + f"{sum(raw) % 256:02x}".encode("ascii"))

    def request(self, command: str) -> str:
        self.send(command)
        reply = self.receive()
        if reply.startswith("E"):
            raise ValueError(f"Debugger rejected {command}: {reply}")
        return reply

    def read(self, address: int, length: int) -> bytes:
        if not 0x80000000 <= address <= 0x81800000 - length or not 0 < length <= 4096:
            raise ValueError("Read outside bounded MEM1 range")
        data = bytes.fromhex(self.request(f"m{address:x},{length:x}"))
        if len(data) != length:
            raise ValueError("Short debugger memory read")
        return data

    def word(self, address: int) -> int:
        return int.from_bytes(self.read(address, 4), "big")


def resume_and_disconnect(remote: Remote) -> None:
    """Resume before socket closure; Dolphin does not implement RSP detach (D)."""
    if remote.request(f"z0,{PRINT_ADDRESS:x},4") != "OK":
        raise ValueError("Could not remove diagnostic breakpoint")
    remote.send("c")
    # The caller closes the socket. Dolphin observes EOF and disables its stub;
    # closing while stopped, or sending unsupported D, can leave it paused.


def parse_trace(text: str) -> dict | None:
    if not text.startswith("CP3W_LUA1|"):
        return None
    fields = text.split("|")
    if len(fields) != 7 or not fields[1].isdigit():
        raise ValueError("Malformed Lua trace header")
    records = {}
    for name, field in zip(ITEMS, fields[2:], strict=True):
        pair = field.split(",")
        if len(pair) != 2 or any(not value.isdigit() or int(value) > 0xFFFFFFFF for value in pair):
            raise ValueError("Malformed Lua inventory record")
        records[name] = {"amount": int(pair[0]), "capacity": int(pair[1])}
    return {"sequence": int(fields[1]), "records": records}


def snapshot(remote: Remote) -> dict | None:
    if remote.request("p40").lower() != f"{PRINT_ADDRESS:08x}":
        raise ValueError("Stopped outside the retail Print binding")
    registers = bytes.fromhex(remote.request("g"))
    if len(registers) < 128:
        raise ValueError("Missing PowerPC GPR registers")
    gpr = struct.unpack(">32I", registers[:128])
    actor, state = gpr[3], gpr[4]
    wrapper = remote.word(actor + 0xD0)
    if remote.word(wrapper) != state:
        raise ValueError("Actor/Lua state ownership mismatch")
    base = remote.word(state + 0xC)
    if remote.word(base) != 4:
        return None
    string = remote.word(base + 4)
    length = remote.word(string + 0xC)
    if not 0 < length <= 2048:
        raise ValueError("Lua string exceeds capture bound")
    text = remote.read(string + 0x10, length).decode("utf-8")
    result = parse_trace(text)
    if result is None:
        return None
    game_state = remote.word(GAME_STATE_POINTER)
    player_state = remote.word(game_state + 0x24)
    native = {}
    for name, item_id in zip(ITEMS, ITEM_IDS, strict=True):
        amount, capacity = struct.unpack(">II", remote.read(player_state + 0x54 + item_id * 12, 8))
        native[name] = {"amount": amount, "capacity": capacity}
    # Energy is accessor-derived health, not the vector's inventory amount.
    health = struct.unpack(">f", remote.read(player_state + 0xC, 4))[0]
    native["Energy"]["amount"] = math.trunc(health)
    # Capacity uses the game's two float constants and energy-tank count.
    tank_count = remote.word(player_state + 0x144)
    per_tank = struct.unpack(">f", remote.read(gpr[2] - 0x5F50, 4))[0]
    base_health = struct.unpack(">f", remote.read(gpr[2] - 0x5F54, 4))[0]
    native["Energy"]["capacity"] = math.trunc(base_health + per_tank * tank_count)
    result.update(
        {
            "actor": actor,
            "actor_id": remote.word(actor + 8),
            "lua_state": state,
            "native_records": native,
            "native_parity": native == result["records"],
            "world_id": remote.read(game_state + 8, 8).hex(),
            "wall_time": time.time(),
        }
    )
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--port", type=int, default=2159)
    parser.add_argument("--seconds", type=int, default=120)
    args = parser.parse_args()
    if args.seconds <= 0:
        parser.error("--seconds must be positive")
    manifest = json.loads((args.build / "build.json").read_text(encoding="utf-8"))
    if "inventory_profile" in manifest:
        parser.error("Full inventory probes require the GDB-free observe.py path")
    verify_image(args.build.resolve(), manifest)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with (
        args.output.open("x", encoding="utf-8") as log,
        socket.create_connection(("127.0.0.1", args.port), 10) as connection,
    ):
        remote = Remote(connection)
        log.write(
            json.dumps(
                {
                    "platform": "dolphin",
                    "probe_id": manifest["probe_id"],
                    "lua_source_sha256": manifest["lua_source_sha256"],
                    "image_sha256": manifest["image"]["sha256"],
                    "image_parts": manifest["image"].get("parts"),
                    "kind": "capture_start",
                }
            )
            + "\n"
        )
        log.flush()
        stopped = remote.request("?")
        if not stopped.startswith(("T", "S")):
            raise ValueError("Debugger did not report stopped state")
        if remote.word(PRINT_ADDRESS) != 0x9421FFE0:
            raise ValueError("Retail Print entry signature mismatch")
        if remote.request(f"Z0,{PRINT_ADDRESS:x},4") != "OK":
            raise ValueError("Could not install diagnostic breakpoint")
        deadline = time.monotonic() + args.seconds
        count = 0
        try:
            remote.send("c")
            connection.settimeout(1)
            while time.monotonic() < deadline:
                try:
                    reply = remote.receive()
                except TimeoutError:
                    continue
                if not reply.startswith(("T", "S")):
                    raise ValueError(f"Unexpected stop packet: {reply}")
                connection.settimeout(10)
                row = snapshot(remote)
                if row is not None:
                    log.write(json.dumps(row, sort_keys=True) + "\n")
                    log.flush()
                    count += 1
                # Step past the diagnostic breakpoint, then resume execution.
                remote.request("s")
                remote.send("c")
                connection.settimeout(1)
        finally:
            connection.settimeout(10)
            connection.sendall(b"\x03")
            remote.receive()
            resume_and_disconnect(remote)
            log.write(
                json.dumps(
                    {
                        "kind": "capture_end",
                        "snapshots": count,
                        "result": "captured" if count else "no_gameplay_samples",
                    }
                )
                + "\n"
            )
    print(f"Captured {count} snapshots; gameplay acceptance requires native_parity=true for every sample.")


if __name__ == "__main__":
    main()
