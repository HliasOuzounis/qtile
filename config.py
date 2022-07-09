### Main Config File ###

from modules.keys import keys
from modules.groups import groups
# from modules.hooks import * 
from modules.layouts import layouts, floating_layout
from modules.mouse import mouse
from modules.screens import screens

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
