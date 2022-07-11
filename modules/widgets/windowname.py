from libqtile import qtile, widget

from themes.colours import colours
from themes.fonts import windowname as font

colorscheme = colours["window_name"] 
bg = colours["bg"]

def my_window_name():
    return widget.WindowName(
        **font,
        format='{name}',
        background=bg,
        foreground=colorscheme["fg"],
        center_aligned=True,
    )