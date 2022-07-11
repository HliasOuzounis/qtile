from libqtile import qtile, widget

from themes.colours import colours
from themes.fonts import font

bg = colours["bg"]
fg = colours["volume"]["fg"]

def my_volume():
    return widget.Volume(
        font = font["font"],
        fontsize = font["fontsize"] + 5,
        background = bg,
        foreground = fg,
        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
    )