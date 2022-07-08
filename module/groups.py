from libqtile.lazy import lazy
from libqtile.config import Key, Group

from config import keys, mod

groups = [Group(i) for i in "123456789"]

for i in "123456789":
    keys.extend(
        [        
            Key([mod], i, lazy.group[i].toscreen(), desc="Switch to group {}".format(i)),
            Key([mod, "shift"], i, lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i)),
            
        ]
    )
    
keys.append(
        Key([mod, "mod1"], "Tab", lazy.screen.next_group())
)