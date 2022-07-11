from libqtile import widget
from libqtile.lazy import lazy

from themes.colours import colours
from themes.fonts import font

bg = colours["widget_bg"]
fg = colours["widget_fg"]

def my_layout_icon():
    return widget.CurrentLayoutIcon(
        background=bg,
        mouse_callbakcs={"Button1": lazy.next_layout},
        scale=0.75
    )