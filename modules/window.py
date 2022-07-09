from libqtile.lazy import lazy
from libqtile.config import Key

from modules.general import keys, mod

keys.extend(
    [        
        # General
        Key([mod], "w", lazy.window.kill()),
        Key([mod], "f", lazy.window.toggle_floating())
        Key([mod, "shift"], "f", lazy.window.toggle_fullscreen())

        # Grow Window Size
        Key([mod, "control"], "Left", lazy.layout.grow_left()),
        Key([mod, "control"], "Up", lazy.layout.grow_up()), 
        Key([mod, "control"], "Down", lazy.layout.grow_down()), 
        Key([mod, "control"], "Right", lazy.layout.grow_right()),

        # Reset
        Key([mod], "n", lazy.layout.normalize())
    ]
)

from libqtile.config import Click, Drag

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()), # Right-click
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()), # Left-click
    Click([mod], "Button2", lazy.window.bring_to_front()) # Middle-click
]
