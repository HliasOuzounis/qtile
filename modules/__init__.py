from modules.keys import keys
from modules.groups import groups
from modules.layouts import layouts, floating_layout
from modules.mouse import mouse
from modules.screens import screens

from modules import hooks


widget_defaults = dict(
    font = 'SourceCodePro Medium',
    fontsize = 10,
    padding = None,
)

__all__ = [
    'groups',
    'keys',
    'layouts',
    'floating_layout',
    'mouse',
    'screens',
    'hooks',
    'widget_defaults',
]