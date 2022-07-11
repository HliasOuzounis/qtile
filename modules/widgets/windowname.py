from libqtile import qtile, widget

from themes.colours import colours
from themes.fonts import windowname as font

bg = colours["widget_bg"]
fg = colours["widget_fg"]

def my_window_name():
    return widget.WindowName(
        **font,
        format='{name}',
        background=bg,
        foreground=fg,
        center_aligned=True,
    )