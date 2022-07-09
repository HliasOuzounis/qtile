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

        ## Window shortcuts ##
        Key([mod], "w", lazy.window.kill()),
        Key([mod], "f", lazy.window.toggle_floating()),
        Key([mod, "shift"], "f", lazy.window.toggle_fullscreen()),

        # Grow Window Size
        Key([mod, "control"], "Left", lazy.layout.grow_left()),
        Key([mod, "control"], "Up", lazy.layout.grow_up()), 
        Key([mod, "control"], "Down", lazy.layout.grow_down()), 
        Key([mod, "control"], "Right", lazy.layout.grow_right()),

        # Reset
        Key([mod], "n", lazy.layout.normalize())
    ]
)