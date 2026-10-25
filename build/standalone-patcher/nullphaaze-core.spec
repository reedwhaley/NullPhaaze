from pathlib import Path

root = Path(SPECPATH).parents[1]
core = root/'src/nullphaaze_core'
a = Analysis([str(root/'build/standalone-patcher/run_patcher.py')],
             pathex=[str(root/'src')],
             binaries=[(str(core/'native/lzokay.dll'), 'nullphaaze_core/native')],
             datas=[(str(core/'data'), 'nullphaaze_core/data')],
             hiddenimports=[], hookspath=[], runtime_hooks=[],
             excludes=['pytest', 'numpy', 'pandas', 'PySide6', 'tkinter', 'IPython'],
             noarchive=False)
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, [], exclude_binaries=True, name='NullPhaazePatcher',
          console=True, debug=False, strip=False, upx=False)
coll = COLLECT(exe, a.binaries, a.datas, strip=False, upx=False, name='NullPhaazePatcher')
