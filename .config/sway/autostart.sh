#!/usr/bin/sh

exec wl-paste -t text --watch clipman store &
# rm -f /tmp/sovpipe && mkfifo /tmp/sovpipe && tail -f /tmp/sovpipe | sov &
swayidle -w \
	timeout 600 'swaylock -c 262626' \
	timeout 900 'swaymsg "output * dpms off"' \
		resume 'swaymsg "output * dpms on"' &

$HOME/.config/eww/carbonmonoxide/scripts/timer.py loop &

$(which eww) daemon &
# $(which eww) --config ~/.config/eww/carbonmonoxide open-many bar dock desktopicons notifypopup &
$(which eww) --config ~/.config/eww/carbonmonoxide open-many bar sidectl1 sidectl2 sidectl3 notifypopup &

# I used to use waybar
# waybar &
# nm-applet --indicator &

# scratchpads
foot -a sterm &
foot -a sncmpcpp ncmpcpp &
foot -a sranger ranger &

# dunst &
# pulseaudio &
pipewire &
wireplumber &
pipewire-pulse &

mpd &
