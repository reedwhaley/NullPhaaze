# Current .14r2 RDS integration

The backend uses the corrected private RDS project in vendor/retro-data-structures.
Install that project first, then the root backend into the frontend's isolated
Python 3.12 environment. RDS supplies compression; the earlier codec DLL build
steps below are historical. CDV still needs external WIT for image rebuilding.

The aggregate RDS-backed package carries GPL terms; the core's original MIT grant
is retained at src/nullphaze_core/LICENSE. See NOTICE.md and the vendor notices.
Current network, receipt/save and cross-world model behavior is explained in
docs/NETWORK_AND_MODELS.md. Keep the generated native templates paired with the
annotated source and rebuild them through the lean source package's
scripts/build_native.py before export. The strict overlay applies source only;
it does not validate an old compiled template merely because its instructions
may match. Existing gameplay/Wii/vWii acceptance remains separate.

The earlier implementation overview is retained below for historical context.

# NullPhaaze

Private development repository for the NullPhaaze CDV client, independent core,
and Corruption multiworld addon. The initial source import is based on the
2026-10-25 networking release. It includes the CGraphics::EndScene networking
fix, two-second client polling, cross-game models, and the menu version/seed
display. See [team setup](docs/TEAM_SETUP.md) before building.

Game media, saves, credentials, personal configuration, release packages, and
research scratch files are kept outside this repository.

The independently written **NullPhaaze core** lives in `src/nullphaze_core/`.
It implements archive/resource handling, script editing, dependency ordering,
layout decoding, inventory/start options and protected exports. Its runtime uses
Python 3.12, the standard library and the included MIT source-built LZO codec.
It does not load or launch the recovered managed patcher. Reference-derived
IDs, templates and dependency facts remain separately attributed in its catalog;
this is not a clean-room claim. See [core instructions](docs/CORE_README.txt).

The **NullPhaaze CDV** frontend in `cdv/` provides seed generation, a progression
solver, presets and ISO/WBFS export using that core. The frontend derives from
GPL Corruptovania/Randovania source; the independent core and native codec retain
their MIT notices. See [the CDV guide](docs/FULL_CDV_PORT.md).

Gollop's recovered C# implementation remains in `src/MP3Randomizer/` as a
compatibility reference, with preserved attribution and documented repairs.
It is not the new core's implementation or runtime dependency. MP3Update remains excluded.

## Build the independent core

Install 64-bit Python 3.12 and Visual Studio 2022 C++ x64 tools with CMake:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/build-core.ps1
python -m unittest discover -s tests/core -v
python -m pip install --no-deps --no-build-isolation -e .
nullphaaze-core --help
```

The core builds and tests without .NET, the recovered implementation, original
binaries, CDV or game data. Supply your own verified USA revision 0 extracted
files for an actual patch operation. Use a new output directory. Native item
layouts and CDV settings permalinks are different formats.

```powershell
nullphaaze-core --input-path 'E:\ROMS\Corruption Extract\DATA\files' --output-path 'E:\ROMS\New patched files' --layout 'NATIVE_LAYOUT'
```

## Build and verify the recovered compatibility reference

On Windows, install the pinned .NET SDK 8.0.404 and Visual Studio 2022 C++ build
tools with CMake. Python 3.11+ is needed for validation, not for running the
patcher. The tested Python version is 3.12. No game data or original binaries
are needed for these commands:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/build-maintained.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/validate-source.ps1
```

The patcher is `src/MP3Randomizer/bin/Release/net40/MP3Randomizer.exe`.
Keep its source-built `lzokay.dll` beside it. It runs as x86 on Windows with a
compatible .NET Framework 4.x installation. Build prerequisites, outputs,
validation scope and troubleshooting are in [BUILDING.md](BUILDING.md).

## Patch extracted files

```powershell
& src/MP3Randomizer/bin/Release/net40/MP3Randomizer.exe --help
& src/MP3Randomizer/bin/Release/net40/MP3Randomizer.exe `
  --input-path 'E:\ROMS\Corruption Extract\DATA\files' `
  --output-path 'E:\ROMS\New patched files' --layout 'PATCHER_LAYOUT'
```

Supply your own extracted game files. The verified input is USA revision 0
(RM3E01). Use a new output directory, separate from the input. `PATCHER_LAYOUT`
is the native 100-placement layout, not a launcher settings permalink. This
program consumes layouts; seed generation, progression solving and ISO rebuilding
are separate work. MP3Update is excluded from this project.

## Source and delivery

[Component and license inventory](docs/SOURCE_COMPONENTS.md) describes the patcher,
codec, inspection tools and optional verification dependencies. The main build
uses vendored MIT codec source; original native binaries are reference material
only. [THIRD_PARTY.md](THIRD_PARTY.md) preserves dependency attribution.

- [Contributing](CONTRIBUTING.md)
- [Reverse-engineering status](docs/REVERSE_ENGINEERING_STATUS.md)
- [Maintained behavior and repairs](docs/MAINTAINED_SOURCE.md)
- [Inspection tools and coverage](docs/SOURCE_COMPONENTS.md)
- [Historical recovery workspace](docs/RECOVERY_HISTORY.md)

The source archive excludes original binaries, launcher modules, game assets
and generated outputs. A separately generated local Windows runtime bundle
contains only source-built executables, the codec DLL, the standard-library
inspection scripts and notices. Its manifest identifies the corresponding
source archive. Neither bundle has been published.

Structural checks and controlled export comparisons do not establish a full
playthrough. User-confirmed generation, export and Dolphin launch of the earlier
backend are recorded separately from acceptance of the new independent core.
