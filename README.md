# NullPhaaze RDS backend — lean source

This is the current `.14r2` behavior with the corrected RDS backend, network/model
integration and a guarded CDV overlay. The desktop frontend is supplied by a
separate compatible checkout. It is not duplicated in this archive.

`src/nullphaze_core` owns layout planning and extracted-file patching. RDS owns
resource framing and compression. `integrations/cdv/overlay` contains the current
CDV-facing exporter, delivery/receipt, native runtime and cross-world model code.
The [network/model walkthrough](docs/NETWORK_AND_MODELS.md) connects those paths;
the [migration notes](docs/RDS_MIGRATION.md) explain the preservation adapters.

Every included file has technical notation in `SOURCE_MANIFEST.json`. Authored
code also has inline comments at its module boundary and relevant decisions.
Generated RDS readers, data and license texts retain their exact bytes, with
file-specific companion notes. I keep the prerequisite source pin visible rather
than rewriting generated readers to make their comments look locally authored.

## Build the backend

Use 64-bit Python 3.12. From this extracted directory:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements-build.txt -r requirements-runtime.txt
.venv\Scripts\python.exe -m pip install --no-build-isolation --no-deps ./vendor/retro-data-structures
.venv\Scripts\python.exe scripts/build_source.py --output ../nullphaze-rds-build
.venv\Scripts\python.exe -m pip install --no-deps ../nullphaze-rds-build/dist/nullphaze_core-0.1.0-py3-none-any.whl
.venv\Scripts\python.exe -m nullphaze_core --help
```

The private RDS version is `0.44.1+nullphaze.20261024`; install it from this source
before the backend. The build uses separate staging/output directories. Original
game files are unnecessary to build the backend. A patch operation requires the
user's verified USA revision-0 extracted `DATA/files`, a native layout and a new
output directory. The core writes the patched PAKs and NTWK; CDV owns image export.

## Apply the integration

Use an isolated copy of the October 29 `.14r2` NullPhaaze repository, with `cdv/`
at its root. The overlay recognizes the accepted base and its own complete result.
Unknown local edits are rejected before writing. The script checks every file,
including newly introduced paths; it does not merge ambiguous source.

```powershell
python scripts/apply_cdv_overlay.py --target C:\work\isolated-nullphaze
python scripts/apply_cdv_overlay.py --target C:\work\isolated-nullphaze --apply
```

Install the built RDS/backend wheels into that checkout's separate CDV Python
environment, then its constrained `cdv/requirements.txt`. The frontend environment
also needs `pyqt-distutils==0.7.3`; compile its forms with `python setup.py build_ui`
from `cdv/`. Keep its existing frontend resources and `cdv/README.md` for runtime
credits. The overlay includes neither user configuration nor converted game assets.

The shared adapters preserve current grants, seed/sender identity, checkpoint
receipts and model-style choices. Unfinished feature requests remain pending.
Native-only visual choices retain their existing paths; imported models require
the user's validated local cache. See the walkthrough for exact fallback rules.

## Rebuild the native templates

Compiled templates are excluded. Use devkitPPC release 47.1, GCC 15.1.0,
binutils 2.44 and target `powerpc-eabi`, with `DEVKITPRO`/`DEVKITPPC` set. Run this
script with the overlaid checkout's CDV environment so its frontend dependencies
are available:

```powershell
python scripts/build_native.py --cdv-root C:\work\isolated-nullphaze --output C:\work\native-build-new --install
```

The output must be separate and new. The builder compiles the bridge twice,
checks identical metadata/output, and compares the runtime/bootstrap to the
accepted `.14r2` bytes with only the two seed/profile regions normalized. It then
records the hashes of this exact annotated native source. Stale template receipts
must not be accepted merely because comments left the instructions unchanged.

Image export still requires external WIT. Supply the matching frontend's prepared
runtime or set `NULLPHAZE_RUNTIME` to a directory containing `wit/wit.exe` on
Windows (`wit/wit` elsewhere). No old standalone codec DLL is needed by this RDS
backend. Prime/Echoes exporter helpers remain dependencies of the external CDV.

## Scope and attribution

The archive contains source, required declarative data, build inputs, file notes
and licenses. It excludes executables, compiled templates, game media, converted
models, caches, environments, tests, reports and the recovered implementation.
Build outputs and validation evidence belong outside this source directory.

Read [NOTICE.md](NOTICE.md) and the vendor notices for the combined GPL and retained
MIT attribution. Packaging and build checks do not establish live delivery,
rendering, save/reload or Wii/vWii acceptance. Nothing here publishes a release,
changes an installed client or deploys a server.
