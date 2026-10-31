# Canonical world/region locations for the legacy Hyper-item scan hints. Boundary names
# here: placement_text, create_data, validate_data, install.
"""Canonical world/region locations for the legacy Hyper-item scan hints."""
from __future__ import annotations

import json
from pathlib import Path

from randovania.game_description import default_database
from randovania.games.prime3.exporter.hint_text import _safe
from randovania.games.prime3.layout.hint_mode import HintMode, mode_for

ITEMS = {
    'hyper_missile':('HyperModeMissile','Hyper Missile',0xEDFC15CF2776AEF2),
    'hyper_grapple':('HyperModeGrapple','Hyper Grapple',0xD87C81AEE6B84424),
}


def placement_text(factory, provider, index, *, detailed=False):
    """The owner of the source world can differ from the item's recipient."""
    game=factory.description.get_preset(provider).game
    regions=default_database.game_description_for(game).region_list
    node=regions.node_from_pickup_index(index)
    region=_safe(regions.region_name_from_node(node,distinguish_dark_aether=True))
    owner='your' if provider==factory.players_config.player_index else f"{_safe(factory.players_config.player_names[provider])}'s"
    location=f'{owner} {region}'
    if detailed:
        location+=f' / {_safe(regions.nodes_to_area(node).name)}'
    return location


def create_data(factory, *, items=ITEMS):
    own=factory.players_config.player_index
    starting={r.short_name for r,n in factory.patches.starting_resources().as_resource_gain() if n>0}
    places={key:[] for key in items}
    modes={key:mode_for(factory, key+'_hint') for key in items}
    for provider,patches in sorted(factory.description.all_patches.items()):
        for index,target in sorted(patches.pickup_assignment.items(),key=lambda pair:pair[0].index):
            if target.player!=own:continue
            resources={r.short_name for r,n in (*target.pickup.progression,*target.pickup.extra_resources) if n>0}
            for key,value in items.items():
                resource=value[0]
                if resource in resources and modes[key] != HintMode.DISABLED:
                    location=placement_text(factory,provider,index,detailed=modes[key] == HintMode.AREA)
                    if location not in places[key]:places[key].append(location)
    data={'schema':1}
    for key,value in items.items():
        resource,name=value[:2]
        if modes[key] == HintMode.DISABLED:
            text = None
        elif resource in starting:
            text=f'{name} is in your starting inventory.'
        elif places[key]:
            text=f"{name} is in {'; '.join(places[key])}."
        else:
            text=f'{name} is not placed in this seed.'
        data[key]=text
    validate_data(data, items=items)
    return data


def validate_data(data, *, items=ITEMS):
    if not isinstance(data,dict) or type(data.get('schema')) is not int or data['schema']!=1:
        raise ValueError('Item location hints require canonical world/region export data')
    if set(data)!={'schema',*items}:
        raise ValueError('Item location hints require both Hyper-item reports')
    for key,value in items.items():
        name=value[1]
        text=data[key]
        if text is None:
            continue
        if (not isinstance(text,str) or not text.startswith(name+' is ') or not text.endswith('.')
                or len(text)>8192 or '&' in text or not text.isprintable()):
            raise ValueError(f'Invalid canonical {name} location hint')


def install(files,output,data):
    from nullphaze_core.archives import Archive
    from randovania.games.prime3.exporter.seed_hints import text_resource
    validate_data(data)
    output=Path(output);output.mkdir(exist_ok=False)
    # Neutralize legacy bot reports too: never leave a disabled hint's native
    # text (or a previous randomized location) in the exported image.
    targets={identity:data[key] or 'No hint available.' for key,(_,_,identity) in ITEMS.items()}
    report={'archives':{},'reports':[],'addedObjects':0,'gameplayVerified':False}
    for name in ('Metroid1.pak','Logbook.pak'):
        archive=Archive(Path(files)/name)
        found=set();resources=[]
        for resource in archive.resources:
            if resource.identity in targets:
                if resource.kind!=b'STRG':raise ValueError(f'Unexpected Hyper hint resource type in {name}')
                text=targets[resource.identity]
                resource=text_resource(resource.identity,(text,text,text))
                found.add(resource.identity)
                report['reports'].append({'archive':name,'resource':f'{resource.identity:016X}','text':text})
            resources.append(resource)
        if found!=targets.keys():raise ValueError(f'Missing native Hyper-item hint strings in {name}')
        destination=output/name;archive.write(destination,resources)
        actual=Archive(destination).resources
        if len(actual)!=len(resources) or any(a.identity!=b.identity or a.kind!=b.kind or a.read()!=b.read()
                                             for a,b in zip(actual,resources,strict=True)):
            raise ValueError('Item location hint archive readback mismatch')
        report['archives'][name]=str(destination)
    (output/'report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    return report
