from libqtile.lazy import lazy
from libqtile.config import Key, Group, Match

from modules.keys import keys, mod, alt

labels = ["", "", "", "", "", "", "", ""]
groups = [Group(name=str(i + 1), label=label) for i, label in enumerate(labels)]

for i in groups:
    keys.extend(
        [        
            Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group"),
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group"),
        ]
    )
    
keys.append(
        Key([mod, alt], "Tab", lazy.screen.next_group())
)