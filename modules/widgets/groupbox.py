from libqtile import qtile, widget

from themes.colours import colours
from themes.fonts import font

colorscheme = colours["group_box"] 

my_group_box = [widget.GroupBox, {
    "background": colorscheme["bg"],
    "foreground": colorscheme["fg"],
    "this_current_screen_border": colorscheme["focused"],
    "active": colorscheme["active"],
    "inactive": colorscheme["inactive"],
    "highlight_color": [colorscheme["active"], colorscheme["inactive"]],
    "highlight_method": "text", # Method of highlighting ('border', 'block', 'text', or 'line')
    "rounded": True,
    "font": font["font"],
    "fontsize": font["fontsize"],
    }
]
    