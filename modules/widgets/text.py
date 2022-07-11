from libqtile import qtile, widget

from themes.colours import colours
from themes.fonts import font

bg = colours["bg"]
fg = colours["volume"]["fg"]

def my_text(text):
    return widget.TextBox(
        text=text,
        fontsize='25',
        font='space mono for powerline',
        padding=0,
        background=bg,
        foreground=fg
    )