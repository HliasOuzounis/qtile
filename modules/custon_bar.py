from libqtile import qtile, widget, bar
from libqtile.lazy import lazy
from themes.fonts import font
from themes.colours import colours

bg = colours["bg"]

from .widgets.battery import my_battery
from .widgets.groupbox import my_group_box
from .widgets.volume import my_volume
from .widgets.padding import *
from .widgets.text import my_text
from .widgets.systray import my_systray
from .widgets.windowname import my_window_name
from .widgets.current_screen import my_current_screen
from .widgets.keyboard_layout import my_keyboard

padding = 10 
def get_widget_list():
    return [
        *left_side_padding(padding),
        my_current_screen(),
        *right_side_padding(padding),
        widget.Prompt(),
        *left_side_padding(padding),
        my_window_name(),
        *full_padding(padding),
        my_group_box(),
        *full_padding(padding),
        my_keyboard(),
        in_line_sep(padding, "#212529"),
        my_battery(),
        in_line_sep(padding, "#212529"),
        my_text("墳 "),
        my_volume(),
        *right_side_padding(padding)
    ]

def get_widget_list_primary():
    return [
        *left_side_padding(padding),
        my_current_screen(),
        *right_side_padding(padding),
        widget.Prompt(),
        *left_side_padding(padding),
        my_window_name(),
        *full_padding(padding),
        my_group_box(),
        *full_padding(padding),
        my_systray(),
        *full_padding(padding),
        my_keyboard(),
        in_line_sep(padding, "#212529"),
        my_battery(),
        in_line_sep(padding, "#212529"),
        my_text("墳 "),
        my_volume(),
        *right_side_padding(padding)
    ]


def my_bar(is_primary):
    return bar.Bar(
        get_widget_list_primary(), 
        42,
        opacity=1.0,
        margin=[10, 10, 10, 10],
        background = "#000000"
    ) if is_primary else bar.Bar(
        get_widget_list(), 
        42,
        opacity=1.0,
        margin=[10, 10, 10, 10],
        background = "#000000"
    )
