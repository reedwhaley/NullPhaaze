# Persist the server's ordered recipe history before granting. Reconcile from the loaded
# receipt and its history hash; host high-water marks cannot skip items after checkpoint
# rollback. Boundary names here: next_history, DeliveryLedger.
"""Durable host queue; game/save receipts, not host counters, govern replay."""
from __future__ import annotations

import hashlib
import copy
from collections import Counter
import json
import os
from pathlib import Path
import tempfile

from randovania.games.prime3.multiworld.manifest import canonical, validate_manifest


def next_history(previous: bytes, sequence: int, recipe: str) -> bytes:
    # Match multiworld_service.c: H(previous || sequence_BE32 || recipe_key).
    # The chain distinguishes equal cursor numbers with different item order.
    # It is an agreement check against this seed's queue, not a secret MAC.
    if len(previous) != 32 or not 1 <= sequence <= 256:
        raise ValueError("Invalid receipt history/sequence")
    key = bytes.fromhex(recipe)
    if len(key) != 32:
        raise ValueError("Invalid receipt recipe key")
    return hashlib.sha256(previous + sequence.to_bytes(4, "big") + key).digest()


class DeliveryLedger:
    def __init__(self, path: Path, manifest: dict):
        validate_manifest(manifest)
        self.path = Path(path)
        self.manifest = manifest
        self.binding = {key: manifest[key] for key in ("world_uuid", "seed_fingerprint", "save_slot")}
        self.data = {"schema": 1, "binding": self.binding, "incoming": [], "collected": [],
                     "uploaded": [], "saved_cursor": 0, "incoming_synchronized": False}
        if self.path.exists():
            self.data = json.loads(self.path.read_text(encoding="utf-8"))
            self.data.setdefault("incoming_synchronized", bool(self.data.get("incoming")))
            self._validate()

    def _validate(self):
        if self.data["schema"] != 1 or self.data["binding"] != self.binding:
            raise ValueError("Host ledger belongs to another world/seed/save slot")
        incoming = self.data["incoming"]
        if type(self.data["incoming_synchronized"]) is not bool:
            raise ValueError("Invalid incoming synchronization state")
        if len(incoming) > 256 or any(key not in self.manifest["incoming_recipes"] for key in incoming):
            raise ValueError("Unrecognized incoming delivery")
        self._validate_counts(incoming)
        if type(self.data["saved_cursor"]) is not int or not 0 <= self.data["saved_cursor"] <= len(incoming):
            raise ValueError("Invalid saved receipt cursor")
        for field in ("collected", "uploaded"):
            values = self.data[field]
            if values != sorted(set(values)) or any(type(i) is not int or not 0 <= i < 100 for i in values):
                raise ValueError("Invalid outgoing location list")
        if not set(self.data["uploaded"]).issubset(self.data["collected"]):
            raise ValueError("Uncollected locations marked uploaded")

    def _persist(self):
        # I write and fsync the replacement in the same directory before the
        # rename. If persistence fails, no newly accepted queue should be used
        # to authorize a grant; _commit restores the prior in-memory state.
        self._validate()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        descriptor, name = tempfile.mkstemp(prefix=self.path.name + ".", dir=self.path.parent)
        try:
            with os.fdopen(descriptor, "wb") as stream:
                stream.write(canonical(self.data) + b"\n")
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(name, self.path)
        finally:
            if os.path.exists(name):
                os.unlink(name)

    def _validate_counts(self, incoming):
        for key, count in Counter(incoming).items():
            sources = self.manifest["incoming_recipes"][key].get("sources")
            if sources is not None and count > len(sources):
                raise ValueError("Server repeated a pickup beyond its seed-authorized count")

    def _commit(self, **changes):
        prior = self.data
        self.data = {**copy.deepcopy(prior), **changes}
        try:
            self._persist()
        except BaseException:
            self.data = prior
            raise

    def accept_incoming(self, keys: list[str]):
        prior = self.data["incoming"]
        if len(keys) < len(prior) or keys[:len(prior)] != prior:
            raise ValueError("Server delivery history was truncated or reordered")
        if len(keys) > 256 or any(key not in self.manifest["incoming_recipes"] for key in keys):
            raise ValueError("Server sent a pickup outside the exported seed")
        self._validate_counts(keys)
        self._commit(incoming=list(keys), incoming_synchronized=True)  # Disk BEFORE sending a grant.

    def history(self, cursor: int) -> bytes:
        if not 0 <= cursor <= len(self.data["incoming"]):
            raise ValueError("Receipt exceeds retained server delivery history")
        value = bytes(32)
        for sequence, key in enumerate(self.data["incoming"][:cursor], 1):
            value = next_history(value, sequence, key)
        return value

    def reconcile(self, status) -> tuple[int, str] | None:
        # cursor is applied in the current game; saved_cursor is the runtime's
        # validated disk anchor. Neither the server queue length nor the last
        # host observation can replace the receipt loaded with the inventory.
        if status.binding != self.binding:
            raise ValueError("Runtime identity does not match this exported world/seed/save")
        if status.history != self.history(status.cursor):
            raise ValueError("Runtime receipt history conflicts with the retained queue")
        if not 0 <= status.saved_cursor <= status.cursor:
            raise ValueError("Invalid saved/runtime receipt relationship")
        # A genuine load of an older checkpoint may lower both cursors. Do not
        # use the host's previously observed high-water mark to skip its items.
        if self.data["saved_cursor"] != status.saved_cursor:
            self._commit(saved_cursor=status.saved_cursor)
        if not status.ready or status.pending or status.cursor == len(self.data["incoming"]):
            return None
        return status.cursor + 1, self.data["incoming"][status.cursor]

    def collect(self, indices):
        values = set(indices)
        if any(type(i) is not int or not 0 <= i < 100 for i in values):
            raise ValueError("Invalid reported location index")
        collected = sorted(set(self.data["collected"]) | values)
        if collected != self.data["collected"]:
            self._commit(collected=collected)

    def mark_uploaded(self, indices):
        values = set(indices)
        if not values.issubset(self.data["collected"]):
            raise ValueError("Cannot acknowledge uncollected locations")
        uploaded = sorted(set(self.data["uploaded"]) | values)
        if uploaded != self.data["uploaded"]:
            self._commit(uploaded=uploaded)

    @property
    def pending_locations(self):
        return tuple(i for i in self.data["collected"] if i not in self.data["uploaded"])
