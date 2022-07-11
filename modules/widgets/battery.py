from libqtile import widget

from themes.colours import colours
from themes.fonts import font
from libqtile.widget.battery import BatteryState

colorscheme = colours["battery"]
bg = colours["bg"]

from libqtile.log_utils import logger

class MyBattery(widget.Battery):
    def build_string(self, status):
        super().build_string(status)
        char = status.state
        if status.state == BatteryState.CHARGING:
            char = self.charging(status.percent)
        elif status.state == BatteryState.DISCHARGING:
            char = self.discharging(status.percent)
        elif status.state == BatteryState.FULL:
            char = ''
        elif status.state == BatteryState.EMPTY:
            char = ''
        elif status.state == BatteryState.UNKNOWN:
            char = ''
    
        hour = status.time // 3600
        minute = (status.time // 60) % 60
        
        logger.warning(status, status.state)
        return self.format.format(
            char=char, percent=status.percent, watt=status.power, hour=hour, min=minute
        )

    def charging(self, percent):
        icons = [
            '', '', '', '', '', ''
        ]
        if percent <= 0.20: return icons[0]
        if percent <= 0.30: return icons[1]
        if percent <= 0.40: return icons[2]
        if percent <= 0.60: return icons[3]
        if percent <= 0.80: return icons[4]
        return icons[5]
    
    def discharging(self, percent):
        icons = [
            '', '', '', '', '', ''
        ]
        if percent <= 0.20: return icons[0]
        if percent <= 0.30: return icons[1]
        if percent <= 0.40: return icons[2]
        if percent <= 0.60: return icons[3]
        if percent <= 0.80: return icons[4]
        return icons[5]
    
    def mouse_enter(self, *args, **kwargs):
        self.format = " {char} {percent:2.0%} {hour}:{min:02d}"
    def mouse_leave(self, *args, **kwargs):
        self.format = " {char} {percent:2.0%}"


def my_battery():
    return MyBattery(
        font = font["font"],
        fontsize = font["fontsize"] + 5,
        background= bg,
        foreground= colorscheme["fg"],
        notify_below= 0.2,
        low_percentage= 0.2,
        low_background= colorscheme["low_bg"],
        low_foreground= colorscheme["low_fg"],
        update_interval= 1,
        format= " {char} {percent:2.0%}",
        show_short_text= False,
    )