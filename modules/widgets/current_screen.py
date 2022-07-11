from libqtile import widget

from themes.colours import colours
from themes.fonts import font

bg = colours["bg"]
colorscheme = colours["current_screen"]

def my_current_screen():
    return widget.CurrentScreen(
        font=font["font"],
        fontsize=font["fontsize"] + 10,
        active_text="",
        inactive_text="",
        background=bg,
        active_color=colorscheme["active"],
        inactive_color=colorscheme["inactive"]
    )