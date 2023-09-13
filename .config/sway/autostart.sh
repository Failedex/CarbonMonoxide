#!/usr/bin/sh

~/dwm-6.3/i3-battery-popup &
exec wl-paste -t text --watch clipman store &
# rm -f /tmp/sovpipe && mkfifo /tmp/sovpipe && tail -f /tmp/sovpipe | sov &
swayidle -w \
	timeout 600 'swaylock -f --image ~/Pictures/wallpapers/minimalistic/dark-cat-rosewater.png' \
	timeout 900 'swaymsg "output * dpms off"' \
		resume 'swaymsg "output * dpms on"' &

$HOME/.config/eww/meowayland/scripts/timer.py loop &

ewww daemon &
ewww --config ~/.config/eww/sidebar open bar &

# waybar &
# nm-applet --indicator &

# scratchpads
foot -a sterm &
foot -a sncmpcpp ncmpcpp &
foot -a sranger ranger &

dunst &
pulseaudio &
