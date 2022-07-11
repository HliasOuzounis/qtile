from libqtile import widget

from themes.colours import colours
from themes.fonts import font

bg = colours["bg"]
colorscheme = colours["group_box"] 


def my_group_box():
    return widget.GroupBox(
            background = bg,
            foreground = colorscheme["fg"],
            this_current_screen_border = colorscheme["focused"],
            other_current_screen_border = colorscheme["other_screen_focused"],
            active = colorscheme["active"],
            inactive = colorscheme["inactive"],
            highlight_color = [colorscheme["active"], colorscheme["inactive"]],
            highlight_method = "text", # Method of highlighting ('border', 'block', 'text', or 'line')
            rounded = True,
            font = font["font"],
            fontsize = font["fontsize"] + 5,
    )

    