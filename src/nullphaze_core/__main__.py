# This CLI accepts a native layout and extracted game files. The codec option is retained
# for caller compatibility; the migrated export uses the pinned RDS backend. Boundary names
# here: main.
"""Standalone native-layout CLI; the frontend can also call engine.export."""
import argparse
import json
from pathlib import Path
import sys
from . import __version__
from .engine import export
from .planner import Options


def main(argv=None):
    parser = argparse.ArgumentParser(prog='nullphaaze-core')
    parser.add_argument('--h', '-help', action='help')
    parser.add_argument('--version', action='version', version='NullPhaaze core '+__version__)
    parser.add_argument('--input-path', type=Path, required=True)
    parser.add_argument('--output-path', type=Path, required=True)
    parser.add_argument('--layout', required=True)
    parser.add_argument('--starting-items', nargs='+', default=['original-with-command'])
    parser.add_argument('--starting-location', nargs='+', default=['norion'])
    parser.add_argument('--report', type=Path)
    parser.add_argument('--codec', type=Path)
    parser.add_argument('--random-seed', type=int)
    parser.add_argument('--retain-space-assets', action='store_true',
                        help='Keep retail ship/space assets for the frontend warp addon; does not install a warp.')
    for names in [('require-launcher',), ('require-ship-missile',), ('hyper-hints',), ('fast-flying',),
                  ('phaaze-skip', 'skip-phaaze'), ('random-door-colors',), ('random-welding-colors',), ('exclude-olympus',)]:
        aliases = ['--'+name for name in names]+['-'+names[0]]
        if names[0] == 'fast-flying': aliases.append('-fast_flying')
        parser.add_argument(*aliases, action='store_true')
    args = parser.parse_args(argv)
    report_destination = None
    try:
        inventory = args.starting_items
        if inventory[0] == 'custom' and len(inventory) == 2:
            inventory = inventory[1]
        elif len(inventory) == 1 and inventory[0] in ('original-with-command', 'post-norion-no-lasso'):
            inventory = inventory[0]
        else:
            raise ValueError('Use a named inventory or custom followed by 43 hex characters')
        start = args.starting_location
        world = area = 0
        if start[0] == 'custom' and len(start) == 3:
            world, area = [int(value, 16) for value in start[1:]]
        elif len(start) != 1 or start[0] not in ('olympus', 'norion', 'valhalla'):
            raise ValueError('Use a named start or custom followed by world and area hex IDs')
        options = Options(args.layout, inventory, start[0], world, area, args.require_launcher,
                          args.require_ship_missile, args.hyper_hints, args.fast_flying, args.phaaze_skip,
                          args.random_door_colors, args.random_welding_colors, args.exclude_olympus,
                          args.retain_space_assets)
        if args.report:
            report = args.report.resolve()
            source = args.input_path.resolve()
            output = args.output_path.resolve()
            if report.exists() or not report.parent.is_dir() or report.is_relative_to(source) or report.is_relative_to(output):
                raise ValueError('Report must be a new file outside the input directory with an existing parent')
            report_destination = report
        result = export(args.input_path, args.output_path, options, progress=lambda msg: print(msg, flush=True),
                        random_seed=args.random_seed, codec=None)
        if report_destination is not None:
            with report_destination.open('x') as stream:
                stream.write(json.dumps(result, indent=2)+'\n')
        print('Patched files saved to '+str(args.output_path))
        return 0
    except (ValueError, OSError, RuntimeError) as error:
        if report_destination is not None and not report_destination.exists():
            try:
                with report_destination.open('x') as stream:
                    stream.write(json.dumps({'completed': False, 'implementation': 'nullphaze_core',
                        'error': str(error), 'output': str(args.output_path), 'recoveredRuntimeRequired': False}, indent=2)+'\n')
            except OSError:
                pass  # A full output drive must not mask the original failure.
        print('Patching failed: '+str(error), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
