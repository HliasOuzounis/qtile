from libqtile.lazy import lazy
from libqtile.config import Key

keys = []
mod, alt = "mod4", "mod1"
terminal = "alacritty"

keys.extend(
    [   
        Key([mod], "enter", lazy.spawn(terminal), desc="Spawn a terminal window"),
        Key([mod, "shift"], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
        Key([mod], "r", lazy.spawn("rofi -show combi"), desc="Spawn quick search bar"),
        Key([mod], "b", lazy.spawn("firefox"), desc="Spawn browser"),
        Key([mod], "d", lazy.spawn("discord"), desc="Spawn discord"),

        Key([mod, "control"], "r", lazy.restart(), desc="Resatart Qtile"),

         # Sound Keys
        Key([], "XF86AudioRaiseVolume",lazy.spawn("amixer set Master 3%+")),
        Key([], "XF86AudioLowerVolume",lazy.spawn("amixer set Master 3%-")),
        Key([], "XF86AudioMute",lazy.spawn("amixer set Master toggle")),
    ]
)