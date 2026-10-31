# Native Hints logbook category, installed when Seed Hints is enabled. Boundary names here:
# scan_dependencies, collect, patch_frame, edit_table, install.
"""Native Hints logbook category, installed when Seed Hints is enabled.

Retains save slot counts/order and native menu/scan behavior. A matching retail
file tree supplies the original scan IDs for existing persistent save slots.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import struct

FRAME = 0x1EEDF22FC9FD3615
TABLES = {'links':0x0F739328C4F7A814,'tooltips':0x2D8F16AEDBE5F82C,
          'titles':0x39BCEA6076A82F0E,'rules':0x5FDA40289F126ABF,
          'lists':0x81BAD41AC2FC8F8A,'labels':0xCE8ED5D9B43911FE}
FRAME_HASH = 'c37006d43515b97ef9b4b7c2570793f9b2a9d06ca94797a9533b96ccb2558201'
HINTS_LINK = ('&link=Pause/LogBook/Hints;&tooltip=HintsTooltip;'
              '&disappearonrollover=CreaturePercent;&growonrollover=Hints,HintsLink;'
              '&wholepane;&endlink;')
HINTS_RULES = {'Hints_VisRule':'urlsegment:2|Hints',
               'HintsIcon_VisRule':'!urlsegment:2|Hints',
               'HintsActiveIcon_VisRule':'urlsegment:2|Hints'}


def scan_dependencies(raw):
    start=19+int.from_bytes(raw[17:19],'big')
    if len(raw)<start+4:raise ValueError('Hint logbook: truncated SCAN')
    count=struct.unpack_from('>I',raw,start)[0]
    if start+4+12*count>len(raw):raise ValueError('Hint logbook: truncated SCAN dependencies')
    return [(raw[start+4+12*i:start+8+12*i],int.from_bytes(raw[start+8+12*i:start+16+12*i],'big')) for i in range(count)]


def collect(files, original_files, enabled=None):
    from nullphaze_core.archives import Archive
    from nullphaze_network.prime3_lua_service.mrea_build import SeedMrea
    from randovania.games.prime3.exporter.hyper_hints import TARGETS
    from randovania.games.prime3.exporter.seed_hints import CELL_STRINGS,CORE_TARGETS,CORE_NAMES
    from randovania.games.prime3.exporter.main_menu import _decoded
    from retro_data_structures.formats.mlvl import Mlvl
    from retro_data_structures.game_check import Game
    archives={p.name:Archive(p) for p in Path(files).glob('*.pak')}
    original={p.name:Archive(p) for p in Path(original_files).glob('*.pak')}
    lookup={r.identity:r for arc in archives.values() for r in arc.resources}
    originals={r.identity:r for arc in original.values() for r in arc.resources}
    area_savw={}
    for r in archives['Worlds.pak'].resources:
        if r.kind==b'MLVL':
            raw=_decoded(r)
            try:world=Mlvl.parse(raw,Game.CORRUPTION)
            except Exception:
                if raw[-32:]!=b'\xff'*32:raise
                world=Mlvl.parse(raw[:-32],Game.CORRUPTION)
            for area in world.raw.areas:area_savw[area.area_mrea_id]=world.raw.world_save_info_id
    entries=[]
    for index,text_id in CELL_STRINGS.items():
        if enabled is not None and f'cell_{index}' not in enabled:
            continue
        found=[]
        for r in archives['Logbook.pak'].resources:
            if r.kind==b'SCAN' and (b'STRG',text_id) in scan_dependencies(_decoded(r)):found.append(r.identity)
        if len(found)!=1:raise ValueError(f'Hint logbook: expected one native Energy Cell {index} SCAN')
        entries.append({'key':f'cell_{index}','title':f'Energy Cell {index}','group':'Energy Cells',
                        'scans':found,'slot_remaps':[]})
    def target_entry(identity,ids,key,title,group):
        area=SeedMrea.parse(_decoded(lookup[identity]),Game.CORRUPTION)
        retail=SeedMrea.parse(_decoded(originals[identity]),Game.CORRUPTION)
        actors={int(a.id):a for l in area.script_layers for a in l.instances}
        oldactors={int(a.id):a for l in retail.script_layers for a in l.instances}
        scans=[];remaps=[]
        for actor_id in ids:
            if actor_id not in actors or actor_id not in oldactors:raise ValueError('Hint logbook: native scan actor missing')
            sid=actors[actor_id].get_properties().scan_info.scannable_info0
            old=oldactors[actor_id].get_properties().scan_info.scannable_info0
            if sid==old:raise ValueError(f'Hint logbook: {title} is not installed; export hints first')
            if sid not in scans:scans.append(sid)
            item={'savw':area_savw[identity],'old':old,'new':sid}
            if item not in remaps:remaps.append(item)
        entries.append({'key':key,'title':title,'group':group,'scans':scans,'slot_remaps':remaps})
    for identity,(index,ids) in CORE_TARGETS.items():
        if enabled is not None and f'core_{index}' not in enabled:
            continue
        target_entry(identity,ids,f'core_{index}',f'{CORE_NAMES[index]} Core','Leviathan Cores')
    titles={'hypermode':'Hypermode','hyper_ball':'Hyper Ball','hyper_missile':'Hyper Missile','hyper_grapple':'Hyper Grapple'}
    for identity,(_,key,_,targets) in TARGETS.items():
        if enabled is not None and key not in enabled:
            continue
        target_entry(identity,targets,key,titles[key],'Hyper Items')
    expected = 16 if enabled is None else len(enabled)
    if len(entries)!=expected:raise ValueError('Hint logbook: missing one or more enabled hints')
    return archives,lookup,entries


def patch_frame(raw):
    from nullphaze_core.binary import pad
    if hashlib.sha256(raw).hexdigest()!=FRAME_HASH:raise ValueError('Hint logbook: unsupported native LogBook frame')
    if struct.unpack_from('>I',raw,12924)[0]!=92:raise ValueError('Hint logbook: unexpected widget count')
    if raw[35369:]!=b'\xff'*(len(raw)-35369):raise ValueError('Hint logbook: unexpected widget tail')
    def clone(start,end,name,parent):
        block=raw[start:end]
        match=re.match(rb'(BWIG|TXPN|MODL)([^\0]+)\0([^\0]*)\0',block)
        if not match:raise ValueError('Hint logbook: invalid widget template')
        return match[1]+name.encode()+b'\0'+parent.encode()+b'\0',bytearray(block[match.end():])
    page_head,page=clone(24789,24963,'basewidget_Hints','basewidget_LogBook')
    list_head,listing=clone(24963,25283,'textpane_SCROLL_HintsList','basewidget_Hints')
    # Reuse the native Objectives question mark and invisible link hit area. The
    # models refer to embedded frame geometry, so no extra assets are needed.
    buttons=[]
    for start,end,name,parent,shift in (
        (13637,13821,'basewidget_HintsIcon','basewidget_LogBookButtons',False),
        (13821,14010,'model_Hints','basewidget_HintsIcon',True),
        (14010,14325,'textpane_HintsLink','basewidget_HintsIcon',True),
        (14325,14515,'basewidget_HintsActiveIcon','basewidget_LogBookButtons',False),
        (14515,14716,'model_HintsActive','basewidget_HintsActiveIcon',True),
    ):
        head,body=clone(start,end,name,parent)
        if shift:
            x,y,z=struct.unpack_from('>3f',body,len(body)-48)
            struct.pack_into('>3f',body,len(body)-48,x+1.0,y,z-13.42)
        buttons.append(head+body)
    result=bytearray(raw[:35369])
    struct.pack_into('>I',result,12924,99)
    result.extend(page_head+page+list_head+listing+b''.join(buttons))
    return pad(result,32,255)


def edit_table(resource, additions, scan_aliases=None):
    from randovania.games.prime3.exporter.main_menu import _decoded,build_sequential_strings
    from retro_data_structures.formats.strg import Strg
    from retro_data_structures.game_check import Game
    table=Strg.parse(_decoded(resource),Game.CORRUPTION)
    if any(name in table.raw.name_table for name in additions):raise ValueError('Hint logbook: category already installed')
    start=len(table.get_strings('ENGL'))
    if any(len(table.get_strings(lang))!=start for lang in table.get_language_list()):raise ValueError('Hint logbook: inconsistent native language tables')
    for lang in table.get_language_list():
        values=list(table.get_strings(lang))
        if scan_aliases:
            values=[re.sub(r'(?<=scan:SCAN,0x)[0-9A-Fa-f]{16}',
                           lambda m:f'{scan_aliases.get(int(m[0],16),int(m[0],16)):016X}',v) for v in values]
        table.set_string_list([*values,*additions.values()],lang)
    for index,name in enumerate(additions,start):table.raw.name_table[name]=index
    return resource.updated(build_sequential_strings(table),compressed=0)


def install(files, output, original_files, enabled=None):
    from nullphaze_core.archives import Archive
    from nullphaze_core.binary import Reader,pack,pad
    from randovania.games.prime3.exporter.main_menu import _decoded
    from retro_data_structures.formats.savw import Savw,ScannableObject
    from retro_data_structures.game_check import Game
    files,output=Path(files),Path(output);output.mkdir(exist_ok=False)
    archives,lookup,entries=collect(files,original_files,enabled)
    remaps={}
    for entry in entries:
        for row in entry['slot_remaps']:
            key=(row['savw'],row['old'])
            if key in remaps and remaps[key]!=row['new']:raise ValueError('Hint logbook: ambiguous native save-slot reuse')
            remaps[key]=row['new']
    native_aliases={}
    for (_,old),new in remaps.items():
        if old in native_aliases and native_aliases[old]!=new:
            raise ValueError('Hint logbook: one native logbook condition has ambiguous replacements')
        native_aliases[old]=new
    lines=[]
    group=None
    for entry in entries:
        if group!=entry['group']:
            group=entry['group'];lines.append(f'&push;&main-color=#E67E00FF;{group}&pop;\n')
        conditions='|'.join(f'(scan:SCAN,0x{sid:016X})' for sid in entry['scans'])
        lines.append(f"&if={conditions};&link=Pause/LogBook/ScanEntry/Article?nullphaaze_hint_{entry['key']};&lookup=listentry:nullphaaze_hint_{entry['key']};\n")
    additions={
        TABLES['links']:{'HintsLink':HINTS_LINK},
        TABLES['tooltips']:{'HintsTooltip':'Hints'},
        TABLES['titles']:{f"nullphaaze_hint_{e['key']}":e['title'] for e in entries},
        TABLES['rules']:HINTS_RULES,
        TABLES['lists']:{'SCROLL_HintsList':''.join(lines)},
        TABLES['labels']:{'BottomText_Hints':'Hints'},
    }
    replacements={FRAME:lookup[FRAME].updated(patch_frame(_decoded(lookup[FRAME])),compressed=0)}
    replacements.update({rid:edit_table(lookup[rid],values,native_aliases if rid==TABLES['lists'] else None)
                         for rid,values in additions.items()})
    found_remaps=set();save_reports=[]
    for rid,res in lookup.items():
        if res.kind!=b'SAVW' or not any(s==rid for s,o in remaps):continue
        save=Savw.parse(_decoded(res),Game.CORRUPTION)
        before=list(save.scannable_objects)
        after=[];slots=[]
        for index,scan in enumerate(before):
            key=(rid,scan.scan_asset_id)
            if key in remaps:
                found_remaps.add(key);slots.append(index)
                scan=ScannableObject(remaps[key],scan.logbook_category)
            after.append(scan)
        save.scannable_objects=after
        raw=save.build()
        if len(raw)!=len(_decoded(res)):raise ValueError('Hint logbook: save table size changed')
        replacements[rid]=res.updated(raw,compressed=0)
        save_reports.append({'savw':f'{rid:016X}','slot_count':len(before),'reused_slots':slots,'size_unchanged':True})
    if found_remaps!=remaps.keys():raise ValueError('Hint logbook: one or more hint scans have no original save slot')
    needed={sid for entry in entries for sid in entry['scans']}
    # SCAN declares its flattened native display closure, including model TXTRs.
    for sid in list(needed):
        for kind,rid in scan_dependencies(_decoded(lookup[sid])):
            if rid not in lookup or lookup[rid].kind!=kind:raise ValueError(f'Hint logbook: missing scan display dependency {rid:016X}')
            needed.add(rid)
    report={'archives':{},'entries':entries,'save_tables':save_reports,'gameplay_verified':False,
            'added_gui_widgets':7,'added_gameplay_actors':0,'save_slot_counts_and_order_preserved':True,
            'native_progress_scan_aliases':{f'{old:016X}':f'{new:016X}' for old,new in native_aliases.items()}}
    for name,arc in archives.items():
        rows=[replacements.get(r.identity,r) for r in arc.resources]
        modified=any(r.identity in replacements for r in arc.resources)
        if name=='Logbook.pak':
            existing={r.identity for r in rows}
            rows.extend(lookup[rid] for rid in sorted(needed-existing))
            # Add names for the native scan-entry URL resolver.
            reader=Reader(arc.names);count=reader.u32()
            for _ in range(count):reader.cstring();reader.read(12)
            raw_names=arc.names[4:reader.pos]
            name_additions=b''.join((f"SCAN_nullphaaze_hint_{e['key']}".encode()+b'\0'+b'SCAN'+pack('Q',e['scans'][0])) for e in entries)
            arc.names=pad(pack('I',count+len(entries))+raw_names+name_additions,64)
            modified=True
        if not modified:continue
        destination=output/name;arc.write(destination,rows)
        actual=Archive(destination).resources
        if len(actual)!=len(rows) or any((a.identity,a.kind,a.read())!=(b.identity,b.kind,b.read()) for a,b in zip(actual,rows,strict=True)):
            raise ValueError(f'Hint logbook: archive readback failed in {name}')
        report['archives'][name]=str(destination)
    (output/'report.json').write_text(json.dumps(report,indent=2)+'\n')
    return report


def capture_originals(files, output):
    """Retain only the seven room preimages needed to preserve native scan slots."""
    from nullphaze_core.archives import Archive
    from randovania.games.prime3.exporter.hyper_hints import TARGETS
    from randovania.games.prime3.exporter.seed_hints import CORE_TARGETS
    output=Path(output);output.mkdir(exist_ok=False)
    wanted=set(TARGETS)|set(CORE_TARGETS);found={};template=None
    for path in Path(files).glob('*.pak'):
        arc=Archive(path)
        if template is None:template=arc
        for resource in arc.resources:
            if resource.kind==b'MREA' and resource.identity in wanted:
                if resource.identity in found and found[resource.identity].read()!=resource.read():
                    raise ValueError(f'Hint logbook: conflicting original room {resource.identity:016X}')
                found[resource.identity]=resource.updated(resource.read())
    if set(found)!=wanted:raise ValueError('Hint logbook: missing original hint room preimages')
    template.write(output/'OriginalHints.pak',list(found.values()),clear=True)
    return {'room_count':len(found),'original_room_sha256':{
        f'{rid:016X}':hashlib.sha256(resource.read()).hexdigest() for rid,resource in found.items()}}
