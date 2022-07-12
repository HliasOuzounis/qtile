from libqtile import qtile, widget

from themes.colours import colours
from themes.fonts import font

from modules.keys import shutdown

bg = colours["widget_bg"]
fg = colours["power_button"]

from libqtile.command import lazy
import os

def my_power_button():
    return widget.TextBox(
        text="",
        font=font["font"],
        fontsize=font["fontsize"] + 5,
        padding=0,
        background=bg,
        foreground=fg,
        mouse_callbakcs={"Button1": lazy.spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))}
    )