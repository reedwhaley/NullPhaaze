# No diagnostic rendering or HUD events; retain the proven pickup event only. Boundary names
# here: metadata, configure_manifest, presentation, flags, lua.
"""No diagnostic rendering or HUD events; retain the proven pickup event only."""

from pathlib import Path

SPEC = {"diagnostic_panel": False, "diagnostic_hud": False, "pickup_hud": "non_modal_timed_hud"}


def metadata(enabled):
    return {"quiet_tracker": True} if enabled else {}


def configure_manifest(report, enabled):
    if enabled:
        report["presentation"] = dict(SPEC)


def presentation(source, messages, native_hash, enabled):
    if enabled:
        return lua(native_hash), tuple(item for item in messages if item[0] == "PickupMissileReceived")
    return source, messages


def flags(enabled, tracker):
    if type(enabled) is not bool or (enabled and not tracker):
        raise ValueError("Quiet presentation requires the explicit read-only tracker")
    return ("-DCP3W_NO_DIAGNOSTICS",) if enabled else ()


def lua(native_hash):
    return Path(__file__).with_suffix(".lua").read_text() + "\n-- Native service SHA256 " + native_hash + "\n"
