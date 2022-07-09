### Main Config File ###

from modules import(
    keys, 
    groups,
    layouts,
    floating_layout,
    screens,
    mouse,
    hooks
)

auto_fullscreen = True
auto_minimize = True
bring_front_click = False
cursor_warp = False
dgroups_key_binder = None
dgroups_app_rules = [] # type: list
follow_mouse_focus = True
focus_on_window_activation = 'smart'
reconfigure_screens = True
wl_input_rules = None
wmname = 'qtile'

widget_defaults = dict(
    font = 'SourceCodePro Medium',
    fontsize = 10,
    padding = None,
)