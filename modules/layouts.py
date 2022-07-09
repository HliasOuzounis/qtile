from libqtile.lazy import lazy
from libqtile.config import Key

from modules.keys import keys, mod

keys.extend(
    [
        # Change focus window
        Key([mod], "Left", lazy.layout.left()),
        Key([mod], "Up", lazy.layout.up()),
        Key([mod], "Down", lazy.layout.down()),
        Key([mod], "Right", lazy.layout.right()),

        Key([mod], "Tab", lazy.layout.next()),

        # Move windows
        Key([mod, "shift"], "Left", lazy.layout.shuffle_left()),
        Key([mod, "shift"], "Up", lazy.layout.shuffle_up()), 
        Key([mod, "shift"], "Down", lazy.layout.shuffle_down()), 
        Key([mod, "shift"], "Right", lazy.layout.shuffle_right()),
    ]
)

from libqtile import layout

# Different layouts
layouts = [
    layout.MonadTall(margin=8, border_focus='#5294e2',
                     border_normal='#2c5380'),
    #layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
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
