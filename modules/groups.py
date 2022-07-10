from libqtile.lazy import lazy
from libqtile.config import Key, Group

from modules.keys import keys, mod, alt

group_names = [
    {"name": "1", "key_binding": "1"},
    {"name": "2", "key_binding": "2"},
    {"name": "3", "key_binding": "3"},
    {"name": "4", "key_binding": "4"},
    {"name": "5", "key_binding": "5"},
    {"name": "6", "key_binding": "6"},
    {"name": "7", "key_binding": "7"},
    {"name": "8", "key_binding": "8"},
]

groups = [Group(i["name"]) for i in group_names]

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