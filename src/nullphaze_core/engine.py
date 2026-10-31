# The engine composes a plan, transforms the allowed outputs and publishes through the
# export session. Keep generated STRG registration and dependency ordering with that same
# plan. Boundary names here: generated_strings, gather_dependencies, transform_archive,
# export.
"""New streaming patch engine: plans, resource transforms and publication."""
import json
from pathlib import Path
from .archives import Archive, Resource
from .binary import FormatError
from .planner import build_plan, planet
from .rules import catalog
from .resources import make_string_table, patch_mrea, patch_world, patch_tweaks
from .scripts import Evaluator
from .session import Session, verified_inputs, checksum
from .storage import available_bytes
from .rds_registration import register_generated

OUTPUT_ARCHIVES = ('Metroid1.pak', 'Metroid3.pak', 'Metroid4.pak', 'Metroid5.pak', 'Metroid6.pak',
                   'Metroid7.pak', 'Metroid8.pak', 'FrontEnd.pak', 'UniverseArea.pak', 'Worlds.pak')
DEPENDENCY_ARCHIVES = ('FrontEnd.pak', 'Metroid1.pak', 'Metroid3.pak', 'Metroid4.pak', 'Metroid5.pak',
                       'Metroid7.pak', 'Metroid8.pak', 'Logbook.pak', 'MiscData.pak')


def generated_strings(options, placements):
    names = catalog()['itemNames']
    locations = {}
    for name, key in [('HyperMissile', 'hyper_missile'), ('HyperGrapple', 'hyper_grapple')]:
        try:
            index = placements.index(names.index(name))
        except ValueError:
            index = -1
        locations[key] = planet(index)
    result = {}
    for definition in catalog()['strings']:
        strings = definition['language_modifications'][0]['strings']
        if not options.hyper_hints and any('{hyper_' in value for value in strings):
            continue
        encoded = make_string_table([value.format(**locations) for value in strings])
        identity = definition['resource_id']
        result[identity] = Resource(identity, b'STRG', 0, len(encoded), data=encoded)
    return result


def gather_dependencies(archives, plan, strings):
    requested = {item['file_id'] for values in plan['dependency_patches'].values() for item in values}
    result = {}
    for name in DEPENDENCY_ARCHIVES:
        seen = set()
        for resource in archives[name].resources:
            if resource.identity in requested and resource.identity not in seen:
                result[resource.identity] = resource
                seen.add(resource.identity)
    for identity in requested-result.keys():
        if identity not in strings:
            raise FormatError(f'Cannot resolve dependency {identity:016X}')
        result[identity] = strings[identity]
    return result


def transform_archive(archive, plan, dependencies, strings, codec, evaluator, start_index=1):
    result, current, previous = [], set(), [set(), set(), set()]
    area_index = start_index
    for resource in archive.resources:
        if resource.identity in strings:
            result.append(strings[resource.identity])
            continue
        current.add(resource.identity)
        if resource.kind == b'MLVL':
            resource = resource.updated(patch_world(resource.read(), resource.identity, plan['layer_toggle_patches']))
            area_index = start_index
        elif resource.kind == b'MREA':
            for dependency in plan['dependency_patches'].get(str(resource.identity), []):
                identity = dependency['file_id']
                if identity not in current and not any(identity in group for group in previous):
                    result.append(strings.get(identity, dependencies[identity]))
                    current.add(identity)
            if resource.compressed:
                raise FormatError('Unsupported externally compressed MREA')
            resource = resource.updated(patch_mrea(resource.read(), resource.identity, area_index, plan, codec, evaluator))
        result.append(resource)
        if resource.kind in (b'MREA', b'MLVL'):
            if resource.kind == b'MREA':
                area_index += 1
            previous = [current, previous[0], previous[1]]
            current = set()
    return result


def export(source, output, options, progress=lambda message: None, codec=None, random_seed=None):
    plan, placements = build_plan(options)
    # RDS owns LZO framing now. Keep the codec argument for caller compatibility.
    evaluator = Evaluator(random_seed)
    with Session(source, output) as session:
        progress('Verifying immutable source files')
        inputs = verified_inputs(session.source)
        expected = sum(inputs[name]['size'] for name in (*OUTPUT_ARCHIVES, 'Standard.ntwk'))+256*1024**2
        if available_bytes(session.output.parent) < expected:
            raise FormatError(f'Insufficient free space: allow {expected/1024**3:.1f} GiB for patched files')
        archives = {name: Archive(session.source/name) for name in set(OUTPUT_ARCHIVES+DEPENDENCY_ARCHIVES)}
        strings = generated_strings(options, placements)
        manager, registration = register_generated(session.source, archives, strings)
        dependencies = gather_dependencies(archives, plan, strings)
        for name in OUTPUT_ARCHIVES:
            progress('Patching '+name)
            archive = archives[name]
            remove_space = name == 'Metroid8.pak' and not options.retain_space_assets
            resources = ([] if remove_space else archive.resources) if name == 'Metroid8.pak' else transform_archive(
                archive, plan, dependencies, strings, codec, evaluator, 0 if name == 'UniverseArea.pak' else 1)
            archive.write(session.staging/name, resources, clear=remove_space)
        tweak = (session.source/'Standard.ntwk').read_bytes()
        (session.staging/'Standard.ntwk').write_bytes(patch_tweaks(tweak, evaluator))
        progress('Verifying source and output hashes')
        outputs = {path.name: checksum(path) for path in session.staging.iterdir()}
        for name, state in inputs.items():
            if checksum(session.source/name) != state['sha256']:
                raise FormatError('Input changed during export: '+name)
        if len(outputs) != 11:
            raise FormatError('Expected eleven output files')
        session.commit()
    return {'completed': True, 'implementation': 'nullphaze_core_rds', 'formatBackend': 'retro-data-structures==0.44.1+nullphaze.20261024', 'input': str(Path(source).resolve()),
            'output': str(Path(output).resolve()), 'inputFiles': inputs, 'outputs': outputs,
            'generatedAssetRegistration': registration,
            'resolvedPropertyFields': sum(evaluator.resolutions.values()),
            'absentPropertySelectors': sum(evaluator.absent.values()),
            'propertyWrites': evaluator.propertyWrites, 'recoveredRuntimeRequired': False,
            'gameplayVerified': False}
