# Install notification/service owners into the randomized room, preserving its existing
# actors. Shared ownership must retain the intended world/area guard and avoid duplicate
# notice claimants. Boundary names here: service_source, patch_area, patch_archives.
"""Install a shared notification owner while preserving seed resources."""

import copy

from nullphaze_core.archives import Archive
from retro_data_structures.formats.mrea import Mrea
from retro_data_structures.formats.script_object import InstanceId, ScriptInstanceRaw
from retro_data_structures.game_check import Game
from retro_data_structures.properties.corruption.objects.LUAScript import LUAScript

from nullphaze_network.prime3_lua_service import probe
from nullphaze_network.prime3_lua_service.mrea_build import SeedMrea, next_instance_id

CORE_REMOVED_AREAS = frozenset((0xBD0BC908940A1A0C, 0xEF19AA26828B708B))


def service_source(world, area):
    return f'''-- Seed-bound CP3W current-area service; no diagnostic displays.
local elapsed=0
function OnThink(dt)
    if type(dt)~="number" or dt~=dt or dt<=0 or dt>1 then return end
    elapsed=elapsed+dt
    if elapsed<0.5 then return end
    elapsed=0
    local location=CP3WReadLocation()
    if type(location)~="string" or string.sub(location,1,33)~="{world}:{area}" then return end
    CP3WReceiptProbeTick()
end
'''


def patch_area(raw, world, entry, *, presentation=None, templates=None, shared_targets=None):
    area = SeedMrea.parse(raw, Game.CORRUPTION)
    layers = list(area.script_layers)
    if not layers:
        raise ValueError("Service area has no default layer")
    originals = [[copy.deepcopy(actor._raw) for actor in layer.instances] for layer in layers]
    highest = max((actor.id.instance for layer in [*layers, area.generated_objects_layer]
                   for actor in layer.instances), default=0)
    if highest >= 65535:
        raise ValueError("No service instance ID available")
    if presentation is None:
        identity = next_instance_id(area, entry["index"])
        props = LUAScript(unknown_0xa1ecc54b=service_source(world, entry["mrea_id"]))
        props.editor_properties.name = "Nullphaze current-area network service"
        layers[0]._raw.script_instances.append(ScriptInstanceRaw("LUAX", identity, (), props.to_bytes(Game.CORRUPTION)))
        layers[0].mark_modified()
    if presentation is not None:
        from nullphaze_network.prime3_lua_service import multiworld_presentation
        multiworld_presentation.append(area, world, entry, presentation, templates, shared_targets=shared_targets)
    output = area.build()
    checked = Mrea.parse(output, Game.CORRUPTION)
    for index, layer in enumerate(checked.script_layers):
        actual = [actor._raw for actor in layer.instances]
        if actual[:len(originals[index])] != originals[index] or (index and actual != originals[index]):
            raise ValueError("Network service changed existing seed scripts")
    return output


def patch_archives(files, output, profile, *, resume=False, presentation=None, templates=None):
    if (output.exists() and not resume) or files.resolve() == output.resolve():
        raise ValueError("Use a new service output directory")
    output.mkdir(parents=True, exist_ok=resume)
    expected = {}
    for world, areas in profile["worlds"].items():
        for entry in areas:
            aid = int(entry["mrea_id"], 16)
            if aid == probe.UNIVERSE_AREA:
                continue
            if aid in expected:
                raise ValueError("Ambiguous current-area owner")
            expected[aid] = world, entry
    removed = set()
    present = {r.identity for p in files.glob('*.pak') for r in Archive(p).resources if r.kind == b'MREA'}
    olympus = {aid for aid, (world, _) in expected.items() if int(world, 16) == 0x37A9E86F0A0CAF6F}
    absent_olympus = olympus - present
    if absent_olympus:
        if len(absent_olympus) != 28:
            raise ValueError('Olympus service removal requires all 28 audited exclusive rooms')
        removed.update(absent_olympus)
        for aid in absent_olympus:
            del expected[aid]
    if not Archive(files / "Metroid8.pak").resources:
        if not CORE_REMOVED_AREAS <= expected.keys():
            raise ValueError("Core removal profile differs from the audited retail worlds")
        removed.update(CORE_REMOVED_AREAS)
        for aid in CORE_REMOVED_AREAS:
            del expected[aid]
    covered, archives = set(), {}
    shared_targets = persistent_raw = None
    if presentation is not None:
        from nullphaze_network.prime3_lua_service import multiworld_presentation
        matches = [resource for path in sorted(files.glob("*.pak")) for resource in Archive(path).resources
                   if resource.kind == b"MREA" and resource.identity == probe.UNIVERSE_AREA]
        if len(matches) != 1:
            raise ValueError("Networking requires exactly one shared presentation area")
        persistent = SeedMrea.parse(matches[0].read(), Game.CORRUPTION)
        originals = [[copy.deepcopy(actor._raw) for actor in layer.instances] for layer in persistent.script_layers]
        shared_targets = multiworld_presentation.append(
            persistent, None, {"index": 0, "mrea_id": f"{probe.UNIVERSE_AREA:016x}"},
            presentation, templates, targets_only=True)
        persistent_raw = persistent.build()
        checked = SeedMrea.parse(persistent_raw, Game.CORRUPTION)
        for before, layer in zip(originals, checked.script_layers, strict=True):
            if [actor._raw for actor in layer.instances][:len(before)] != before:
                raise ValueError("Shared presentation changed original universe scripts")
    for path in sorted(files.glob("*.pak")):
        archive = Archive(path)
        if presentation is not None:
            # Share text/audio actors; only lightweight polling controllers
            # remain in each room, where the game invokes Lua OnThink.
            modified = {resource.identity for resource in archive.resources
                        if resource.kind == b"MREA" and (resource.identity == probe.UNIVERSE_AREA
                                                        or resource.identity in expected)}
        else:
            modified = {resource.identity for resource in archive.resources
                        if resource.kind == b"MREA" and resource.identity in expected}
        if not modified:
            continue
        resources = []
        for resource in archive.resources:
            if resource.identity in modified:
                if resource.compressed:
                    raise ValueError("Externally compressed service area is unsupported")
                if resource.identity == probe.UNIVERSE_AREA and persistent_raw is not None:
                    resources.append(resource.updated(persistent_raw))
                    continue
                world, entry = expected[resource.identity]
                resources.append(resource.updated(patch_area(resource.read(), world, entry,
                                      presentation=presentation, templates=templates, shared_targets=shared_targets)))
                if resource.identity in expected:
                    covered.add(resource.identity)
            else:
                resources.append(resource)
        if presentation is not None and probe.UNIVERSE_AREA in modified:
            from nullphaze_network.prime3_lua_service import multiworld_presentation
            existing = {resource.identity: resource for resource in resources}
            for resource in multiworld_presentation.resources(presentation, templates):
                if resource.identity in existing:
                    if existing[resource.identity].kind != resource.kind or existing[resource.identity].read() != resource.read():
                        raise ValueError("Incoming presentation resource collision")
                else:
                    resources.append(resource)
        destination = output / path.name
        if destination.exists():
            actual = Archive(destination).resources
            if len(actual) != len(resources) or any(
                (a.identity, a.kind, a.compressed, a.read()) != (b.identity, b.kind, b.compressed, b.read())
                for a, b in zip(actual, resources, strict=True)
            ):
                raise ValueError("Existing service checkpoint differs from deterministic reconstruction")
        else:
            archive.write(destination, resources)
        originals = {(resource.identity, resource.kind): resource for resource in archive.resources}
        for resource in Archive(destination).resources:
            if ((resource.identity, resource.kind) in originals and resource.identity not in modified
                    and resource.read() != originals[resource.identity, resource.kind].read()):
                raise ValueError("Service changed an unrelated seed resource")
        archives[path.name] = {"sha256": probe.file_hash(destination), "areas": len(modified)}
    if covered != expected.keys():
        raise ValueError("Some gameplay rooms are missing from service validation")
    return {"areas": sum(record["areas"] for record in archives.values()),
            "gameplay_areas_verified": len(covered), "core_removed_areas": sorted(f"{aid:016x}" for aid in removed),
            "archives": archives, "current_area_only": True,
            "shared_presentation_targets": presentation is not None,
            "diagnostic_hud": False, "diagnostic_panel": False,
            "connection_notices": presentation is not None,
            "incoming_presentation": "pending" if presentation is None else {
                "events": len(presentation), "single_claim_owner": True, "native_streams": True}}
