from libqtile import qtile, widget, bar
from libqtile.lazy import lazy
from themes.fonts import font
from themes.colours import colours
import os

CENTER_SPACERS = 100
MARGIN = 0
BORDER_WIDTH = 3
windowname = "Source Code Pro"

DEFAULT_FG = colours["fg"]
DEFAULT_BG = colours["bg"]
WIDTH=34

def launcher(qtile):
    lazy.spawn("sh " + os.path.expanduser("~/.scripts/rofi-launchpad.sh"))
    

groupbox = [widget.GroupBox, {
                "font" : font["font"],
                "padding" : font["padding"],
                "fontsize" : font["fontsize"],
                "foreground": colours["cyan"],
                "highlight_method": "text",
                "block_highlight_text_color": colours["white"],
                "active": colours["fg"],
                "inactive": colours["cyan"],
                "rounded": False,
                "highlight_color": [colours["fg"], colours["yellow"]],
                "urgent_alert_method": "line",
                "urgent_text": colours["red"],
                "urgent_border": colours["red"],
                "disable_drag": True,
                "use_mouse_wheel": False,
                "hide_unused": False,
                "spacing": 5,
                "this_current_screen_border": colours["yellow"],
            }
        ]

windowname = [widget.WindowName, {
                "font": windowname,
                "fontsize": 16,
                "padding": 3,
                "format": '{name}',
                "background": colours["fg_gutter"],
                "center_aligned": True
            }
        ]

systray = [widget.Systray, {
        "background": colours["orange"],
        "foreground": colours["black"],
        "theme_path": "rose-pine-gtk",
        }
    ]

spacer_small = [ widget.Spacer, {
        "length" : 5,
        # these values are used by style func, not qtile
        "is_spacer": True,
        "inheirit": True,
        "use_separator": False
    }
]

logo_image = [ widget.Image, {
        "background": colours["magenta"],
        "margin" : 3,
        "filename" : "~/.config/qtile/icon/artixlinux-logo-flat.png",
        "mouse_callbacks":{
            "Button1": lazy.spawn("sh " + os.path.expanduser("~/.scripts/rofi-launchpad.sh"))
        },
    }
]

logo = [widget.TextBox, {
                # text="  ",
                "font" : font["font"],
                "padding" : -2,
                "fontsize" : font["fontsize"]*1.6,
                "text": " ",
                #"text": " Σ",
                "background": colours["magenta"],
                "foreground": colours["bg"],
                "mouse_callbacks":{
                    "Button1": lazy.spawn("sh " + os.path.expanduser("~/.scripts/rofi-launchpad.sh")) 
                },
            }
        ]

cpu = [widget.CPU, {
                **font,
                "format": " {freq_current}GHz {load_percent}%",
                "background": colours["yellow"],
                "foreground": colours["bg"]
            }
        ]

disk = [widget.DF, {
                **font,
                "partition": "/",
                "warn_color": colours["red"],
                "warn_space":40,
                "visible_on_warn": False,
                "measure":"G",
                "format":"DISK: ({uf}{m}|{r:.0f}%)",
            }
        ]

net = [widget.Net, {
                **font,
                "format": "\u2193 {down} \u2191 {up}",
                "interface": "wlp0s20f3",
                "update_interval": 3,
                "background": colours["pink"]
            }
        ]

mem = [widget.Memory, {
                **font,
                "format": ": {MemUsed:.2f}/{MemTotal:.2f}{mm}",
                "update_interval": 1.0,
                "measure_mem": "G",
            }
        ]

batt = [widget.Battery, {
                **font,
                "background": colours["magenta"],
                "foreground": colours["bg"],
                "low_foreground": colours["red"],
                "low_background": None,
                "low_percentage": 0.30,
                "charge_char": "",
                "discharge_char": "",
                "full_char": "",
                "empty_char": "X",
                "unknown_char": "?",
                "format": "  {char} {percent:2.0%}",
                "show_short_text": False,
            }
        ]

layout = [widget.CurrentLayout, {
                **font,
                "background": colours["pink"]
            }
        ]

date = [widget.Clock, {
                **font,
                "format": '%m/%d/%Y',
                "background": colours["orange"]
            }
        ]

time = [widget.Clock, {
                **font,
                "format": '%I:%M %p ',
                "background": colours["fg_gutter"]
            }
        ]

from .widgets.battery import my_battery
from .widgets.groupbox import my_group_box

def widgetlist():
    return [
        spacer_small,
        logo,
        # groupbox,
        my_group_box,
        windowname,
        systray,
        # cpu,
        batt,
        my_battery,
#        disk,
#        net,
        # mem,
#        batt,
        layout,
        date,
        time,
    ]

def style(widgetlist):
    # adds separator widgets in between the initial widget list
    styled = widgetlist[:]
    
    for index, wid in enumerate(widgetlist): 
        end_sep = {
            "font": "Iosevka Nerd Font",
            "text": " ",
            "fontsize": WIDTH,
            "padding": -1
        }

        if index < len(widgetlist)-1:
            #end_sep["background"]=widgetlist[index+1][1].get("background", DEFAULT_BG)
            #end_sep["foreground"]=wid[1].get("background", DEFAULT_BG)

            end_sep["foreground"]=widgetlist[index+1][1].get("background", DEFAULT_BG)
            end_sep["background"]=wid[1].get("background", DEFAULT_BG)
            if wid[1].get("is_spacer") and wid[1].get("inheirit"):
                bg=widgetlist[index+1][1].get("background", DEFAULT_BG)
                wid[1]["background"] = bg
                end_sep["background"] = bg
            # insert separator before current
            if wid[1].get("use_separator", True):
                styled.insert(styled.index(wid)+1, (widget.TextBox, end_sep))
        
    return [w[0](**w[1]) for w in styled]

def my_bar():
    return bar.Bar(
        [
            # *widgetlist()
            *style(widgetlist())
        ],
        WIDTH,
        foreground=DEFAULT_FG,
        background=DEFAULT_BG,
        opacity=1.0,
        margin=[MARGIN, MARGIN, BORDER_WIDTH, MARGIN],
    )
