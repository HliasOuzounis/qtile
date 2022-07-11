from libqtile.lazy import lazy
from libqtile.config import Key

from modules.keys import keys, mod, alt

keys.extend(
    [
        # Change focus window
        Key([mod], "Left", lazy.layout.left()),
        Key([mod], "Up", lazy.layout.up()),
        Key([mod], "Down", lazy.layout.down()),
        Key([mod], "Right", lazy.layout.right()),

        Key([alt], "Tab", lazy.layout.next()),

        # Move windows
        Key([mod, "control"], "Left", lazy.layout.shuffle_left()),
        Key([mod, "control"], "Up", lazy.layout.shuffle_up()), 
        Key([mod, "control"], "Down", lazy.layout.shuffle_down()), 
        Key([mod, "control"], "Right", lazy.layout.shuffle_right()),

        Key([mod], "l", lazy.next_layout(), desc="Switch to next layout")
    ]
)

from libqtile import layout
from themes.colours import colours

border_focus = colours["layout"]["border_focus"]
border_normal = colours["layout"]["border_normal"]

default_config = {
    "margin": 12,
    "border_width": 1,
    "border_focus": border_focus,
    "border_normal": border_normal
}

# Different layouts
layouts = [
    layout.MonadTall(**default_config),
    #layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(**default_config),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(**default_config, num_stacks=2),
    layout.RatioTile(**default_config),
    layout.Tile(**default_config),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

from libqtile.config import Match
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
