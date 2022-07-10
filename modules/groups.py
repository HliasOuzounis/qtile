from libqtile.lazy import lazy
from libqtile.config import Key, Group, Match

from modules.keys import keys, mod, alt

group_names = [
    {"name": " Home", "key_binding": "1",},
    {"name": " Sys", "key_binding": "2",},
    {"name": " Web", "key_binding": "3",},
    {"name": " Games", "key_binding": "4",},
    {"name": "5", "key_binding": "5",},
    {"name": "6", "key_binding": "6",},
    {"name": "7", "key_binding": "7",},
    {"name": "8", "key_binding": "8",},
]

groups = [Group(name=i["name"]) for i in group_names]

for i in group_names:
    keys.extend(
        [        
            Key([mod], i["key_binding"], lazy.group[i["name"]].toscreen(), desc="Switch to group"),
            Key([mod, "shift"], i["key_binding"], lazy.window.togroup(i["name"], switch_group=True),
                    desc="Switch to & move focused window to group"),
        ]
    )
    
keys.append(
        Key([mod, alt], "Tab", lazy.screen.next_group())
)