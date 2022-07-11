from libqtile import widget

from themes.colours import colours
from themes.fonts import font

bg = colours["bar_bg"]
fg = colours["widget_bg"]

def left_pad():
    return widget.TextBox(
        text='',
        fontsize='40',
        font='space mono for powerline',
        padding=0,
        background=bg,
        foreground=fg
    )
def right_pad():
    return widget.TextBox(
        text='',
        fontsize='40',
        font='space mono for powerline',
        padding=0,
        background=bg,
        foreground=fg
    )

def sep(padding):
    return widget.Sep(
        padding=padding,
        linewidth=0,
        background=bg
    )
    
def in_line_sep(padding, new_bg):
    return widget.Sep(
        padding=padding,
        linewidth=0,
        background=new_bg
    )

def left_side_padding(padding):
    return [
        sep(padding),
        left_pad()
    ]
def right_side_padding(padding):
    return [
        right_pad(),
        sep(padding)
    ]
def full_padding(padding):
    return [
        right_pad(),
        sep(padding),
        left_pad()
    ]