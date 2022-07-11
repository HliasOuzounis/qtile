from libqtile import widget

from themes.colours import colours
from themes.fonts import font

bg = colours["widget_bg"]
fg = colours["widget_fg"]

def my_time():
    return widget.Clock(
        background=bg,
        foreground=fg,
        format=" %H:%M",
        **font
    )
def my_date():
    return widget.Clock(
        background=bg,
        foreground=fg,
        format=" %d-%m-%y",
        **font
    )