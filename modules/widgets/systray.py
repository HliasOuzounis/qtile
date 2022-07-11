from libqtile import qtile, widget

from themes.colours import colours
from themes.fonts import font

colorscheme = colours["systray"] 
bg = colours["bg"]

def my_systray():
    return widget.Systray(
        background = bg,
        foreground = colorscheme["fg"],
    )