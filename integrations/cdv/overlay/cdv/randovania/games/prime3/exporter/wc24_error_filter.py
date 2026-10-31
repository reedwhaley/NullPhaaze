# Suppress only WC24 error 109042 in Corruption multiworld exports. Boundary names here:
# patch, install.
"""Suppress only WC24 error 109042 in Corruption multiworld exports.

Preserves the native error, unrelated categories and network runtime. This filter
is entered only when the retail message selector is invoked; hardware-tested
against the prior blocking runtime, with newer runtime hardware checks pending.
"""
import hashlib
import json
import struct
from pathlib import Path
from randovania.games.prime3.exporter.dol_patcher import parse_dol_header, encode_ppc_unconditional_branch

SELECTOR=0x802c2adc
RESUME=0x802c2ae0
RUNTIME_BASE=0x817c1000
STAGING=0x806843c0
EXTENSION=64
EXPECTED_SECTION_SIZE=0x3ca80
EXPECTED_RUNTIME_SIZE=0x3c880

def patch(data: bytes) -> tuple[bytes, dict]:
    p=bytearray(data);h=parse_dol_header(data);sel=h.offset_for_address(SELECTOR)
    if sel is None or bytes(p[sel:sel+4]) != bytes.fromhex('8003001c'):
        raise ValueError('WC24 109042 filter: unsupported retail error selector at 0x802c2adc')
    section=next((s for s in h.sections if s.kind=='text' and s.address==STAGING),None)
    if section is None or section.size!=EXPECTED_SECTION_SIZE or section.file_offset+section.size!=len(p):
        raise ValueError('WC24 109042 filter: unexpected multiworld bootstrap section; rebuild runtime assets')
    off=section.file_offset
    if bytes(p[off+0xec:off+0xf0])!=bytes.fromhex('616b0e40') or bytes(p[off+0x134:off+0x138])!=bytes.fromhex('616bd880'):
        raise ValueError('WC24 109042 filter: unexpected bootstrap copy/cache bounds')
    target=RUNTIME_BASE+EXPECTED_RUNTIME_SIZE
    if target+EXTENSION>=0x817fe000:
        raise ValueError('WC24 109042 filter exceeds the reserved runtime guard')
    shim_words=[0x80030018,0x3d80fffe,0x618c560e,0x7c006000,0x4182000c,0x8003001c,
                encode_ppc_unconditional_branch(target+24,RESUME),0x38600000,0x4e800020]
    shim=struct.pack('>9I',*shim_words)
    p[sel:sel+4]=struct.pack('>I',encode_ppc_unconditional_branch(SELECTOR,target))
    p[off+0xec:off+0xf0]=bytes.fromhex('616b0e80')
    p[off+0x134:off+0x138]=bytes.fromhex('616bd8c0')
    p.extend(shim+bytes(EXTENSION-len(shim)))
    struct.pack_into('>I',p,0x90+4*section.kind_index,section.size+EXTENSION)
    updated=bytes(p);check=parse_dol_header(updated)
    if check.offset_for_address(target) is not None:
        raise ValueError('WC24 filter unexpectedly overlaps a DOL section')
    return updated,{'error_code':109042,'selector':SELECTOR,'shim':target,'bytes_added':EXTENSION,
                    'network_runtime_unchanged':True,'sha256':hashlib.sha256(updated).hexdigest()}

def install(data_root: Path) -> dict:
    target=Path(data_root)/'sys/main.dol';original=target.read_bytes();updated,report=patch(original)
    temp=target.with_name('main.dol.wc24-filter-new')
    with temp.open('xb') as stream:stream.write(updated)
    temp.replace(target)
    return report
