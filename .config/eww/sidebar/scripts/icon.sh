#!/bin/bash
$HOME/.config/eww/sidebar/scripts/icon.py
while [ 1 == 1 ] ; do
    swaymsg -t subscribe '["window"]' > /dev/null
    $HOME/.config/eww/sidebar/scripts/icon.py
done
