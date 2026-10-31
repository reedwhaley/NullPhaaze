# Freeze the overlaid backend and generated RDS readers together. Native templates
# are build outputs prepared from this exact source before freezing; pathex refers
# to the target repository layout after the guarded overlay, not this bundle.
# Nullphaze modification, 2026-10-16. GPL-3.0-or-later.
from pathlib import Path
from PyInstaller.utils.hooks import copy_metadata, collect_submodules

root = Path(SPECPATH)
datas = [(str(root/'randovania/data'), 'data'),
         (str(root/'randovania/games'), 'games'),
         (str(root/'core_runtime'), 'runtime'),
         (str(root.parent/'src/nullphaze_core/data'), 'nullphaze_core/data'),
         (str(root/'README.md'), 'data'),
         (str(root/'LICENSE'), '.'),
         (str(root/'PORT_README.md'), '.')]
datas += [(str(root/'randovania/games/prime3/exporter/olympus_strip.json'),
           'randovania/games/prime3/exporter')]
datas += [(str(root/'randovania/games/prime3/exporter/friend_credit.json'),
           'randovania/games/prime3/exporter')]
datas += [(str(root/'randovania/games/prime3/exporter/fast_ziplines.json'),
           'randovania/games/prime3/exporter'),
          (str(root/'randovania/games/prime3/exporter/MP3Update-LICENSE.txt'),
           'randovania/games/prime3/exporter')]

datas += [(str(root/'nullphaze_network/LICENSE'), 'nullphaze_network'),
          (str(root/'nullphaze_network/prime3_lua_service/MULTIWORLD_MODELS.md'), 'nullphaze_network')]
datas += [(str(root/'nullphaze_network/data'), 'nullphaze_network/data')]

datas += copy_metadata('nullphaze-cdv', recursive=True)
datas += copy_metadata('nullphaze-core')
datas += [(str(root.parent/'vendor/retro-data-structures/LICENSE'), 'licenses/retro-data-structures'),
          (str(root.parent/'vendor/retro-data-structures/LICENSE.RSOT'), 'licenses/retro-data-structures'),
          (str(root.parent/'vendor/retro-data-structures/NOTICE.md'), 'licenses/retro-data-structures')]
for distribution in ('open-prime-rando', 'dolphin-memory-engine', 'pid', 'capstone'):
    datas += copy_metadata(distribution, recursive=True)
a = Analysis([str(root/'run_nullphaze.py')], pathex=[str(root), str(root.parent/'src')], binaries=[], datas=datas,
             hiddenimports=['unittest.mock', 'nullphaze_core.__main__',
                            *collect_submodules('open_prime_rando.dol_patching'),
                            *collect_submodules('retro_data_structures.properties'),
                            *collect_submodules('nullphaze_core.patches')], hookspath=[], runtime_hooks=[],
             excludes=['PyQt5', 'randovania.server', 'pytest', 'IPython', 'tkinter',
                       'torch', 'tensorflow'], noarchive=False)
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, [], exclude_binaries=True, name='NullPhaazeCDV', console=True,
          debug=False, strip=False, upx=False, icon=str(root/'randovania/data/icons/rdv_logo_blue.ico'))
coll = COLLECT(exe, a.binaries, a.datas, strip=False, upx=False, name='NullPhaazeCDV')
