from libqtile import widget
from libqtile import qtile

class MyVolume(widget.Volume):
    pass


volume = MyVolume(
    # fontsize=18,
    # font='Font Awesome 5 Free',
    # foreground=colors[4],
    # background='#2f343f',
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
)