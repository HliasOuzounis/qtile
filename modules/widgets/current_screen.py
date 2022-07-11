from libqtile import widget

from themes.colours import colours
from themes.fonts import font

bg = colours["widget_bg"]
fg = colours["widget_fg"]
active = colours["focused"]
inactive = colours["active"]

def my_current_screen():
    return widget.CurrentScreen(
        font=font["font"],
        fontsize=font["fontsize"] + 10,
        active_text="",
        inactive_text="",
        background=bg,
        active_color=active,
        inactive_color=inactive
    )