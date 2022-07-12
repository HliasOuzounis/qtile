from libqtile import qtile, widget, bar
from libqtile.lazy import lazy
from themes.fonts import font
from themes.colours import colours

bg = colours["bar_bg"]
widget_bg = colours["widget_bg"]

from .widgets import *

padding = 10 
def get_widget_list():
    return [
        *left_side_padding(padding),
        my_current_screen(),
        *right_side_padding(padding),
        widget.Prompt(),
        *left_side_padding(padding),
        my_window_name(),
        in_line_sep(padding, widget_bg),
        my_layout_icon(),
        *full_padding(),
        my_group_box(),
        *full_padding(),
        my_date(),
        in_line_sep(padding, widget_bg),
        my_time(),
        *full_padding(),
        my_keyboard(),
        in_line_sep(padding, widget_bg),
        my_text("墳"),
        in_line_sep(5, widget_bg),
        my_volume(),
        in_line_sep(padding, widget_bg),
        my_battery(),
        in_line_sep(padding, widget_bg),
        my_power_button(),
        *right_side_padding(padding)
    ]

def get_widget_list_primary():
    widgets = get_widget_list()
    widgets.insert(18, my_systray())
    widgets.insert(19, right_pad())
    widgets.insert(20, sep(padding))
    widgets.insert(21, left_pad())
    return widgets

def my_bar(is_primary):
    return bar.Bar(
        get_widget_list_primary(), 
        42,
        opacity=1.0,
        margin=[10, 10, 5, 10],
        background=bg,
        border_color=bg,
        border_width=[5, 5, 5, 5]
    ) if is_primary else bar.Bar(
        get_widget_list(), 
        42,
        opacity=1.0,
        margin=[10, 10, 5, 10],
        background=bg,
        border_color=bg,
        border_width=[5, 5, 5, 5]
    )
