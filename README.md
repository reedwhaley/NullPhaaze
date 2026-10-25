# NullPhaaze core

Standalone Metroid Prime 3 file patching engine and command-line patcher.
This source tree contains the Python core, its declarative catalog, the native
MIT LZO codec and the standalone console build recipe. It has no CDV/Randovania
frontend, generator, progression solver, tracker, multiworld server, Qt resources
or frontend build targets.

The runtime uses Python 3.12 or later, the Python standard library and the
included source-built codec. The tested build setup uses 64-bit Python 3.12.
Source builds need no original patcher, frontend installation or game files.

## Windows source build

Install 64-bit Python 3.12 and Visual Studio 2022 C++ x64 tools with CMake.
From the repository root in PowerShell:

```powershell
python -m venv .venv-core
& .venv-core/Scripts/Activate.ps1
python -m pip install setuptools==75.8.0 wheel==0.45.1
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/build-core.ps1
python -m pip install --no-deps --no-build-isolation -e .
python scripts/verify_core_source.py
nullphaaze-core --help
```

The build compiles `native/lzokay` and the C ABI bridge, installs the codec under
`src/nullphaaze_core/native/`, and checks codec roundtrips and malformed inputs.
The source independence check records module and catalog provenance locally.

## Linux and macOS source build

Install Python 3.12, CMake and a C++ compiler. In a virtual environment:

```sh
python -m pip install setuptools==75.8.0 wheel==0.45.1
cmake -S native -B artifacts/core-native -DCMAKE_BUILD_TYPE=Release
cmake --build artifacts/core-native --config Release
python -m pip install --no-deps --no-build-isolation -e .
```

Set `NULLPHAAZE_CORE_CODEC` to the absolute path to the generated
`artifacts/core-native/liblzokay.so` on Linux or
`artifacts/core-native/liblzokay.dylib` on macOS. Then run:

```sh
python scripts/check_core_codec.py
nullphaaze-core --help
```

The codec may also be copied to `src/nullphaaze_core/native/` with that platform's
filename. Platform build outputs are excluded from version control.

## Patch extracted files

Supply your own verified USA revision 0 extracted game files (RM3E01), an existing
native 100-placement layout, and a new output directory separate from the input:

```powershell
nullphaaze-core --input-path 'INPUT_FILES' --output-path 'NEW_OUTPUT' --layout 'NATIVE_LAYOUT'
```

The core consumes layouts; it does not generate seeds or accept frontend settings
permalinks. It patches extracted files and does not rebuild ISO/WBFS images.
`--help` lists inventory, starting location and patch options. Original media is
never included in this repository. MP3Update payloads are absent.

## Optional standalone Windows console executable

After the Windows source build, in the same environment:

```powershell
python -m pip install -r requirements-build.txt
python -m PyInstaller --noconfirm --distpath artifacts/portable/dist --workpath artifacts/portable/work build/standalone-patcher/nullphaaze-core.spec
& ./artifacts/portable/dist/NullPhaazePatcher/NullPhaazePatcher.exe --help
```

Keep the entire generated `NullPhaazePatcher` folder, including `_internal`.
This target produces a console patcher; it has no desktop frontend.

## Attribution and validation boundary

Retained MIT notices are in `LICENSE`, `native/lzokay/LICENSE` and
`licenses/lzokay-LICENSE`. See `THIRD_PARTY.md` and
`src/nullphaaze_core/data/provenance.json` for the source and catalog boundary.
The catalog contains attributed reference-derived patch facts; this is not a
clean-room claim. Source, codec and synthetic checks do not establish gameplay
or physical-hardware acceptance.
