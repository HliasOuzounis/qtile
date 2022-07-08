from libqtile.lazy import lazy
from libqtile.config import Key

from .screens import screens
from .keys import keys, mod
import os

@lazy.function
def wallpaper_generator():
    for root, dirs, wallpaper in os.walk("~/.config/qtile/wallpapers"):
        yield "".join("~/.config/qtile/", wallpaper)

wallpapers = wallpaper_generator()

@lazy.function
def change_wallpaper(qtile):
    new_wallpaper = next(wallpapers, None)
    if not new_wallpaper:
        wallpapers = wallpaper_generator()
        new_wallpaper = next(wallpapers)

    for screen in screens: 
        lazy.screen.cmd_set_wallpaper(new_wallpaper, mode="fill")
    open("FILE NAME", "x")

keys.extend([
    Key([mod], 'b', change_wallpaper())
])

