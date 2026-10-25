# Retained source and attribution

The standalone Python patch engine is in `src/nullphaaze_core/`. Its retained
MIT notice is in `LICENSE`, including Gollop's original copyright notice.
Reference-derived resource identifiers, declarative patch templates, strings
and dependency facts are attributed in `src/nullphaaze_core/data/provenance.json`.
That catalog records the historical reference assembly hash and catalog
generator; neither is a build or runtime dependency. This is not a clean-room
claim. Game resource payloads and original patcher binaries are not included.

`native/lzokay/` vendors the MIT LZO implementation from AxioDL/lzokay commit
`db2df1fcbebc2ed06c10f727f72567d40f06a2be`. Its upstream copyright is
2018 Jack Andersen. The upstream source, README and MIT license remain intact;
`licenses/lzokay-LICENSE` preserves the corresponding notice.
`native/bridge.cpp` supplies a bounded C ABI consumed through Python `ctypes`.
The Windows codec uses the static C++ runtime.

The Python runtime requires only its own modules and the standard library.
Setuptools and wheel build/install the Python package. PyInstaller and its
hooks are optional build dependencies for the standalone Windows console
executable; their own distribution notices remain applicable to those tools.

The frontend, networking/server implementation, WIT, NOD, Mono, Qt and their
source/build recipes are not components of this standalone source tree.
No retained target builds a frontend, seed generator, tracker or server.
