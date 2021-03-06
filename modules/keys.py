from libqtile.lazy import lazy
from libqtile.config import Key

keys = []
mod, alt = "mod4", "mod1"
terminal = "alacritty"

from libqtile.command import lazy as lz
from libqtile import qtile as qt
import os

@lz.function
def shutdown(qtile): 
    qt.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))

keys.extend(
    [   
        Key([mod], "s", shutdown, desc="Open a shutdown panel"),
        Key([mod], "Return", lazy.spawn(terminal), desc="Spawn a terminal window"),
        Key([mod, "shift"], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
        Key([mod], "r", lazy.spawn("rofi -show combi"), desc="Spawn quick search bar"),
        Key([mod], "b", lazy.spawn("firefox"), desc="Spawn browser"),
        Key([mod], "d", lazy.spawn("discord"), desc="Spawn discord"),

        Key([mod, "control"], "r", lazy.restart(), desc="Resatart Qtile"),

         # Sound Keys
        Key([], "XF86AudioRaiseVolume",lazy.spawn("amixer set Master 3%+")),
        Key([], "XF86AudioLowerVolume",lazy.spawn("amixer set Master 3%-")),
        Key([], "XF86AudioMute",lazy.spawn("amixer set Master toggle")),

        #Brightness
        # Key([], "XF86MonBrightnessUp", lazy.spawn("sh " + os.path.expanduser("~/.scripts/backlight/increase.sh")), desc="Increase brightness"),
        # Key([], "XF86MonBrightnessDown", lazy.spawn("sh " + os.path.expanduser("~/.scripts/backlight/decrease.sh")), desc="Decrease brightness"),

        ## Window shortcuts ##
        Key([mod], "w", lazy.window.kill()),
        Key([mod], "f", lazy.window.toggle_floating()),
        Key([mod, "shift"], "f", lazy.window.toggle_fullscreen()),

        # Grow Window Size
        # Key([mod, "shift"], "Left", lazy.layout.grow_left()),
        # Key([mod, "shift"], "Up", lazy.layout.grow_up()), 
        # Key([mod, "shift"], "Down", lazy.layout.grow_down()), 
        # Key([mod, "shift"], "Right", lazy.layout.grow_right()),

        # Reset
        Key([mod], "n", lazy.layout.normalize())
    ]
)
