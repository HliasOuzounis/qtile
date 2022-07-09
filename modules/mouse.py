from libqtile.lazy import lazy

from modules.keys import mod
from libqtile.config import Click, Drag

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()), # Right-click
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()), # Left-click
    Click([mod], "Button2", lazy.window.bring_to_front()) # Middle-click
]
