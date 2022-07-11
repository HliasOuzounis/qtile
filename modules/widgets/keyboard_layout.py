from libqtile import widget
from libqtile.lazy import lazy
from libqtile.config import Key

from themes.colours import colours
from themes.fonts import font

from modules.keys import keys, mod

import subprocess

bg = colours["widget_bg"]
fg = colours["widget_fg"]

def get_keyboard_layout():
    keyboard_code = subprocess.run(
        "xset -q | grep -A 0 'LED' | cut -c59-67".split(),
        stdout=subprocess.PIPE
        ).stdout.decode("utf-8")
    with open("output.txt", "w") as f:
        f.write(keyboard_code)
    return "  us" if "00000000" in keyboard_code else "  gr"
    

def my_keyboard():
    return widget.GenPollText(
        background=bg,
        foreground=fg,
        fontsize=font["fontsize"] + 5, 
        func=get_keyboard_layout, 
        update_interval=0.1
        )

    
