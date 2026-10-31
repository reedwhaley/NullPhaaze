# Only exactly equal resource payloads may share a PAK extent. Retain every directory entry
# and its metadata; structural readback is separate from native loader acceptance. Boundary
# names here: compact.
"""Exact duplicate PAK payload aliasing; preserves every original table entry.

Keeps each resource entry and aliases only identical stored payloads.
Only equal typed IDs, compression flags, lengths AND exact stored bytes alias.
"""
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import struct
import sys

from nullphaze_core.archives import Archive
from nullphaze_core.binary import pack, pad


def compact(source, destination):
    source, destination = Path(source), Path(destination)
    if source.resolve() == destination.resolve():
        raise ValueError('Input and output must be isolated')
    archive = Archive(source)
    source_sha = hashlib.file_digest(source.open('rb'), 'sha256').hexdigest()
    groups = defaultdict(list)
    unique, records = [], []
    offset = 0
    for resource in archive.resources:
        raw = resource.read()
        key = (resource.identity, resource.kind, resource.compressed, resource.size,
               hashlib.sha256(raw).digest())
        match = next((o for r,o in groups[key] if r.read() == raw), None)
        if match is None:
            match = offset
            unique.append(resource)
            groups[key].append((resource, match))
            offset += resource.size
        records.append((resource, match))
    # Preserve the complete original names section, including padding.
    with source.open('rb') as stream:
        header = stream.read(128)
        names = stream.read(struct.unpack_from('>I', header, 72)[0])
    from .rds_directory import write_records
    write_records(archive, destination, records, unique)
    check = Archive(destination)
    assert len(check.resources) == len(archive.resources)
    assert check.header == archive.header
    with destination.open('rb') as stream:
        stream.seek(128)
        assert stream.read(len(names)) == names
    for original, reread in zip(archive.resources, check.resources, strict=True):
        assert (original.identity, original.kind, original.compressed, original.size) == (
            reread.identity,reread.kind,reread.compressed,reread.size)
        assert original.read() == reread.read()
    # A second, independent table walk checks all extents without Archive.
    with destination.open('rb') as stream:
        raw_header = stream.read(128)
    ns,ts,ds = (struct.unpack_from('>I',raw_header,o)[0] for o in (72,80,88))
    assert 128+ns+ts+ds == destination.stat().st_size
    count = 0
    with destination.open('rb') as stream:
        stream.seek(128+ns)
        count = struct.unpack('>I',stream.read(4))[0]
        table_bytes = stream.read(count*24)
        base = 128+ns+ts
        for index,(original,expected_offset) in enumerate(records):
            flag,kind,identity,length,actual_offset = struct.unpack_from('>I4sQII',table_bytes,index*24)
            assert (flag,kind,identity,length,actual_offset) == (original.compressed,
                original.kind,original.identity,original.size,expected_offset)
            assert actual_offset%64 == 0 and actual_offset+length <= ds
            stream.seek(base+actual_offset)
            assert stream.read(length) == original.read()
    assert source_sha == hashlib.file_digest(source.open('rb'),'sha256').hexdigest()
    backwards = sum(records[i][1] < records[i-1][1] for i in range(1,len(records)))
    return {'source':str(source),'output':str(destination),'input_sha256':source_sha,
            'output_sha256':hashlib.file_digest(destination.open('rb'),'sha256').hexdigest(),
            'input_bytes':source.stat().st_size,'output_bytes':destination.stat().st_size,
            'saved_bytes':source.stat().st_size-destination.stat().st_size,
            'original_entries':len(records),'retained_entries':count,'unique_payloads':len(unique),
            'backward_offset_steps':backwards,'all_entry_payloads_byte_identical':True,
            'independent_table_readback':True,'named_resource_section_preserved':True,
            'input_unchanged':True,'native_loader_compatibility_proven':False}
