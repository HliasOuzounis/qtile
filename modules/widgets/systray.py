from libqtile import qtile, widget

from themes.colours import colours
from themes.fonts import font

bg = colours["widget_bg"]
fg = colours["widget_fg"]

def my_systray():
    return widget.Systray(
        background = bg,
        foreground = fg,
    )