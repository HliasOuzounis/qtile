from libqtile import widget

from themes.colours import colours
from themes.fonts import font

bg = colours["widget_bg"]
fg = colours["widget_fg"]
focused = colours["focused"]
active = colours["active"]
inactive = colours["inactive"]

def my_group_box():
    return widget.GroupBox(
            background = bg,
            foreground = fg,
            this_current_screen_border = focused,
            active = active,
            inactive = inactive,
            highlight_method = "text", # Method of highlighting ('border', 'block', 'text', or 'line')
            rounded = True,
            font = font["font"],
            fontsize = font["fontsize"] + 3,
    )

    