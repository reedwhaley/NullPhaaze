"""
Independently authored resource envelopes and world-layer mutations.
See https://wiki.axiodl.com/w/MREA_(Metroid_Prime_3) and https://wiki.axiodl.com/w/MLVL_(File_Format)
"""
from .binary import Reader, FormatError, pack, pad
from .scripts import apply_layer


def add_dependencies(data, dependencies):
    reader = Reader(data)
    count = reader.count(12)
    entries = reader.read(12*count)
    additions = [item for item in dependencies if item['resource_type'] != b'STRM']
    extra = b''.join(pack('Q4s', item['file_id'], item['resource_type']) for item in additions)
    # Existing layer offsets remain unchanged: the extra assets are appended to
    # the common dependency tail, as established by the validated reference.
    return pack('I', count+len(additions))+entries+extra+reader.read(reader.remaining)


def patch_mrea(data, identity, area_index, plan, codec, evaluator):
    """
    Apply patches to a given MREA resource

    Arguments :
    - data : The raw bytes data of the base MREA resource
    - identity : the ResourceId of the MREA in its PAK ????
    - area_index : ????
    - plan : ????
    - codec : The LZO codec used for (de)compression
    - evaluator : ????
    """
    ## Note : This function is very big. There are probably some sequences that could be refactored into 
    ## separate functions to make this one a lot more readable.
    ## Also, a class representing MREAs and MLVLs should be created and used instead, as it will make 
    ## the resulting code a lot more readable for everyone else, though we'll probably do it at the same time 
    ## as the RDS migration

    # TODO : This filtering could probably stand to be its own function. Also, explain why we filter plan
    plan = {key: values if key == 'dependency_patches' else 
        [rule for rule in values if not rule.get('mrea_ids') or identity in rule['mrea_ids']]
        for key, values in plan.items()}

    reader = Reader(data)

    # Parsing header data
    # Read up to data section sizes
    header = bytearray(reader.read(96))
    # Check MREA version
    if header[:4] != b'\xde\xad\xbe\xef' or int.from_bytes(header[4:8], 'big') != 30:
        raise FormatError('Expected Corruption MREA version 30')
    ## Note : The names of the variables don't align with those listed on the Retro modding wiki
    ## layers : Script Layer Count
    ## section_count : Data Section Count
    ## block_count : Compressed Block Count
    ## category_count : Section Number Count 
    ## Also, we seem to be completely ignoring both the area transform and world model count fields ; 
    ## I suppose this is because we don't need to modify them for now
    layers, section_count, block_count, category_count = [int.from_bytes(header[i:i+4], 'big') for i in (60, 64, 68, 72)]
    # Check counts consistency
    if section_count > reader.remaining//4 or block_count > section_count or layers > section_count:
        raise FormatError('MREA section counts exceed record')
    # Parse Data Section Sizes
    sizes = [reader.u32() for _ in range(section_count)]
    reader.align(32)

    # Parse compressed blocks section
    blocks = [[reader.u32() for _ in range(4)] for _ in range(block_count)]
    reader.align(32)

    # Parse Section Numbers section
    if category_count > reader.remaining//8:
        raise FormatError('MREA category table exceeds record')
    categories = [(reader.read(4), reader.u32()) for _ in range(category_count)]
    reader.align(32)

    # Look for Script Objects and Dependencies sections
    labels = dict(categories)
    # Check for index consistency in Section Numbers and the presence of a Script Objects and Dependencies section
    if b'SOBJ' not in labels or b'DEPS' not in labels or any(value >= section_count for _, value in categories):
        raise FormatError('Required MREA section index missing or invalid')
    script_start, dependency_index = labels[b'SOBJ'], labels[b'DEPS']
    # Check if layer quantity aligns with sections quantity
    if script_start+layers > section_count:
        raise FormatError('MREA script layers exceed section table')

    # Work on compressed blocks
    section = 0
    encoded_blocks = []
    dependencies = plan['dependency_patches'].get(str(identity), [])
    for number, (buffer_size, decoded_size, encoded_size, count) in enumerate(blocks):
        # Isolate each block in the MREA
        ## Raise an error if either
        ## - The block contains no MREA segment
        ## - The section indexation in goes out of bounds
        ## - The section has a declared decompressed size exceeding 268 435 456 bytes
        ## Note : I don't know where that upper bound for uncompressed size comes from, is there a source for it ?
        if not count or section+count > section_count or decoded_size > 256*1024**2:
            raise FormatError('Invalid MREA block extent')
        # Block padding is at the start. Only compressed blocks have padding, uncompressed blocks should already be 32 bytes aligned
        front_padding = reader.read((-encoded_size) % 32) if encoded_size else b''
        # If the block's compressed size is 0, it is not compressed
        encoded = reader.read(encoded_size or decoded_size)
        indices = range(section, section+count)
        # A block is considered dirty if any of its section indices contain the dependecies section or any script object section
        dirty = dependency_index in indices or any(script_start <= i <= script_start+layers for i in indices)
        # Only modify dirty blocks, other blocks are left as-is
        if not dirty:
            encoded_blocks.append(front_padding+encoded)
            section += count
            continue

        # Decompress the dirty block in order to modify it
        decoded = codec.decode_chunks(encoded, decoded_size) if encoded_size else encoded
        content = Reader(decoded)

        # Apply modifications to the dirty block
        changed = bytearray()
        for index in indices:
            value = content.read(sizes[index])
            # Apply script object modifications
            if script_start <= index < script_start+layers:
                value = apply_layer(value, plan, identity, area_index, evaluator)
            # Add extra necessary dependencies
            if index == dependency_index and dependencies:
                value = add_dependencies(value, dependencies)
            sizes[index] = len(value)
            changed.extend(value)
        # A block may carry alignment bytes beyond its declared sections.
        if any(content.read(content.remaining)):
            raise FormatError('Unexpected nonzero MREA block tail')
        changed = pad(changed, 32)

        # Recompress the dirty block if necessary, then move on to the next block
        if encoded_size:
            encoded = codec.encode_chunks(changed)
            blocks[number] = [len(changed)+288, len(changed), len(encoded), count]
            encoded_blocks.append(bytes((-len(encoded)) % 32)+encoded)
        else:
            blocks[number] = [max(buffer_size, len(changed)), len(changed), 0, count]
            encoded_blocks.append(changed)
        section += count

    # Check if all sections have been covered
    if section != section_count:
        raise FormatError('MREA blocks do not cover all sections')

    # Reattach all parts of the MREA, then return it pre-padded for a PAK file
    size_table = pad(b''.join(pack('I', size) for size in sizes), 32)
    block_table = pad(b''.join(pack('4I', *block) for block in blocks), 32)
    category_table = pad(b''.join(pack('4sI', *category) for category in categories), 32)
    return pad(header+size_table+block_table+category_table+b''.join(encoded_blocks), 64, 255)


def patch_world(data, identity, operations):
    reader = Reader(data)
    if reader.read(8) != bytes.fromhex('DEAFBABE00000019'):
        raise FormatError('Expected Corruption MLVL version 25')
    reader.read(28)
    areas = reader.count(105)
    for _ in range(areas):
        reader.read(96)
        reader.read(reader.count(2)*2)
        for _ in range(reader.count(8)):
            reader.read(reader.count(8)*8)
            reader.read(reader.count(12)*12)
        reader.cstring()
    reader.read(13)
    count = reader.count(12)
    positions = []
    for _ in range(count):
        reader.u32()
        positions.append(reader.pos)
        reader.u64()
    result = bytearray(data)
    for operation in operations:
        if operation['mlvl_id'] != identity:
            continue
        index = operation['area_index']
        if index >= len(positions):
            raise FormatError('World-layer rule targets a missing area')
        offset = positions[index]
        flags = int.from_bytes(result[offset:offset+8], 'big')
        for state, key in [(True, 'bits_to_activate'), (False, 'bits_to_deactivate')]:
            for bit in operation[key]:
                if not 0 <= bit < 64:
                    raise FormatError('Layer bit exceeds 64-bit mask')
                flags = flags | (1 << bit) if state else flags & ~(1 << bit)
        result[offset:offset+8] = pack('Q', flags)
    # Validate the retained trailing arrays too; unknown trailing padding is not
    # interpreted as an unbounded string or array.
    for _ in range(reader.count(1)):
        reader.cstring()
    reader.read(reader.count(16)*16)
    reader.read(reader.count(4)*4)
    return pad(result[:reader.pos], 64, 255)


def make_string_table(strings):
    encoded = [string.encode('utf-8')+b'\0' for string in strings]
    offsets, payload = [], bytearray()
    for value in encoded:
        offsets.append(len(payload))
        payload.extend(pack('I', len(value))+value)
    header = pack('4I', 0x87654321, 3, 1, len(strings))+bytes(8)+b'ENGL'
    metadata = pack('I', sum(map(len, encoded)))+b''.join(pack('I', offset) for offset in offsets)
    return pad(header+metadata+payload, 64, 255)
