"""Check runtime independence and record reference-derived data provenance."""
import ast
import hashlib
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parent.parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    package = ROOT/'src/nullphaaze_core'
    (ROOT/'evidence').mkdir(exist_ok=True)
    forbidden = {'randovania', 'retro_data_structures', 'MP3Randomizer', 'subprocess', 'clr'}
    files = sorted(package.glob('*.py'))
    for path in files:
        tree = ast.parse(path.read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names = [item.name.split('.')[0] for item in node.names]
            elif isinstance(node, ast.ImportFrom):
                names = [(node.module or '').split('.')[0]]
            else:
                continue
            assert not forbidden.intersection(names), (path.name, names)
            if isinstance(node, ast.Import) or not node.level:
                assert all(name in sys.stdlib_module_names for name in names), (path.name, names)
    manifest = {'implementation': 'nullphaaze_core', 'runtimeLanguage': 'Python 3.12',
                'runtimeModules': [{'path': str(path.relative_to(ROOT)), 'sha256': sha(path)} for path in files],
                'recoveredManagedRuntimeRequired': False, 'frontendRequired': False,
                'independentVerifierRequired': False, 'thirdPartyPythonRuntimeDependencies': [],
                'declarativeData': {'path': 'src/nullphaaze_core/data/rules.json', 'sha256': sha(package/'data/rules.json'),
                    'origin': 'Attributed reference-derived IDs, patch templates, strings and dependency facts; not a clean-room claim.',
                    'generator': 'verification/CoreCatalog/Program.cs',
                    'referenceAssemblySha256': json.loads((package/'data/rules.json').read_text())['referenceAssemblySha256']},
                'codec': {'source': 'native/lzokay', 'bridge': 'native/bridge.cpp', 'license': 'MIT',
                          'binary': 'src/nullphaaze_core/native/lzokay.dll',
                          'macBinary': 'architecture-specific build runtime/liblzokay.dylib',
                          'linuxBinary': 'Linux build runtime/liblzokay.so'},
                'originalGamePayloadsIncluded': False}
    (package/'data/provenance.json').write_text(json.dumps(manifest, indent=2)+'\n')
    (ROOT/'evidence/core-source-independence.json').write_text(json.dumps(dict(passed=True, **manifest), indent=2)+'\n')
    print('Core runtime imports only its own modules and the Python standard library; reference data attributed')


if __name__ == '__main__':
    main()
