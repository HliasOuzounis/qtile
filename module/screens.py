from libqtile.lazy import lazy
from libqtile.config import Key

from config import keys, mod

keys.extend(
    [        
        # Change focus monitor
        Key([mod], "Tab", lazy.next_screen()),
        Key([mod, "shift"], "Tab", lazy.prev_screen()),
    ]
)

# Configure Screens
from libqtile.config import Screen
from .top_bar import custom_bar

import os, screeninfo

def screen_init():
    return Screen(
        # top=custom_bar()
        wallpaper="~/.config/qtile/wallpapers/mob_city.png"
        wallpaper_mdode="fill"
    )

screens = [screen_init() for screen in screeninfo.get_monitors()]