# NullPhaaze modification, 2026-10-16: source backend and open NOD/WIT tools. Boundary names
# here: Prime3Toolchain, resolve_prime3_toolchain, extract_prime3_disc_image.
"""NullPhaaze modification, 2026-10-16: source backend and open NOD/WIT tools.
GPL-3.0-or-later, retaining the surrounding CDV/Randovania license.
"""
from __future__ import annotations
import dataclasses
import os
import sys
from pathlib import Path
import nod


@dataclasses.dataclass(frozen=True)
class Prime3Toolchain:
    randomizer_command: tuple[str, ...]
    hpatchz_command: tuple[str, ...] = ()
    wit_command: tuple[str, ...] = ()
    extractor_command: tuple[str, ...] = ()
    uses_python_nod: bool = True
    randomizer_environment: dict[str, str] = dataclasses.field(default_factory=dict)
    lzokay_library: Path | None = None


def resolve_prime3_toolchain() -> Prime3Toolchain:
    default = Path(__file__).resolve().parents[4]/('runtime' if getattr(sys, 'frozen', False) else 'core_runtime')
    root = Path(os.environ.get('NULLPHAZE_RUNTIME', default)).resolve()
    if sys.platform not in ('win32', 'darwin', 'linux'):
        raise RuntimeError('NullPhaaze export supports Windows, macOS and Linux only.')
    # RDS supplies compression; this backend only needs the external image tool.
    wit = root/'wit'/('wit.exe' if sys.platform == 'win32' else 'wit')
    for path in (wit,):
        if not path.is_file():
            raise FileNotFoundError(f'Missing NullPhaaze runtime file: {path}. '
                                    'Run scripts/build-cdv.ps1, scripts/build_macos.py, or scripts/build_linux.py for your platform.')
    if sys.platform != 'win32' and not os.access(wit, os.X_OK):
        raise PermissionError(f'WIT is not executable: {wit}')
    command = (sys.executable, 'core') if getattr(sys, 'frozen', False) else (sys.executable, '-m', 'nullphaze_core')
    return Prime3Toolchain(randomizer_command=command, wit_command=(str(wit),),
                           lzokay_library=None, randomizer_environment={})



def extract_prime3_disc_image(toolchain, input_path, extract_path, progress_update):
    disc, _is_wii = nod.open_disc_from_image(input_path)
    partition = disc.get_data_partition()
    if partition is None:
        raise ValueError('The input image has no Wii data partition.')
    context = nod.ExtractionContext()
    context.set_progress_callback(lambda message, fraction: progress_update(message, 0.05+0.25*fraction))
    partition.extract_to_directory(os.fspath(extract_path), context)
    if not all((extract_path/'DATA'/name).is_dir() for name in ('files', 'sys')):
        raise ValueError('Disc extraction did not produce DATA/files and DATA/sys.')
