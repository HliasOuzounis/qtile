from libqtile.lazy import lazy
from libqtile.config import Key
from libqtile import bar
from libqtile.log_utils import logger

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
from .custon_bar import my_bar

import os, screeninfo

config = {
    'wallpaper': '~/.config/qtile/wallpapers/mob_city.png',
    'wallpaper_mode': 'fill',
}

screens = [
    Screen(
        **config, 
        top=my_bar(screen.is_primary), 
        bottom=bar.Gap(8),
        left=bar.Gap(8),
        right=bar.Gap(8),
    ) 
    for screen in screeninfo.get_monitors()
]
