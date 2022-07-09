from libqtile.lazy import lazy
from libqtile.config import Key

from modules.keys import keys, mod

keys.extend(
    [        
        # Change focus monitor
        Key([mod], "Tab", lazy.next_screen()),
        Key([mod, "shift"], "Tab", lazy.prev_screen()),
    ]
)

# Configure Screens
from libqtile.config import Screen
# from .top_bar import custom_bar

import os, screeninfo

config = {
  'wallpaper': '~/.config/qtile/wallpapers/mob_city.png',
  'wallpaper_mode': 'fill',
}

screens = [Screen(**config) for screen in screeninfo.get_monitors()]