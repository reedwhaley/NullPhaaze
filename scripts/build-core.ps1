$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
Push-Location -LiteralPath $root
try {
    & python -c 'import sys; assert sys.version_info[:2] == (3,12) and sys.maxsize > 2**32, "Use 64-bit Python 3.12"'
    if ($LASTEXITCODE) { throw 'Independent core requires 64-bit Python 3.12' }
    $vswhere = Join-Path ${env:ProgramFiles(x86)} 'Microsoft Visual Studio/Installer/vswhere.exe'
    $installation = & $vswhere -latest -products '*' -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 -property installationPath
    if (-not $installation) { throw 'Visual Studio C++ x64 tools and CMake are required.' }
    $cmake = Join-Path $installation 'Common7/IDE/CommonExtensions/Microsoft/CMake/CMake/bin/cmake.exe'
    & $cmake -S native -B artifacts/core-native -G 'Visual Studio 17 2022' -A x64
    if ($LASTEXITCODE) { throw 'Core codec configuration failed' }
    & $cmake --build artifacts/core-native --config Release
    if ($LASTEXITCODE) { throw 'Core codec build failed' }
    New-Item -ItemType Directory -Force src/nullphaaze_core/native | Out-Null
    Copy-Item -LiteralPath artifacts/core-native/Release/lzokay.dll -Destination src/nullphaaze_core/native/lzokay.dll -Force
    & python scripts/check_core_codec.py
    if ($LASTEXITCODE) { throw 'Core codec checks failed' }
} finally { Pop-Location }
