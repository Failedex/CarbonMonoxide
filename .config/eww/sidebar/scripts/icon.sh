#!/bin/bash
EWW_BIN="$HOME/.local/bin/eww -c $HOME/.config/eww/sidebar"

$HOME/.config/eww/sidebar/scripts/icon.py
while [ 1 == 1 ] ; do
    swaymsg -t subscribe '["window", "workspace"]' > /dev/null
    focus=$(swaymsg -t get_tree | jq '.. | select(.type?) | select(.focused==true) | .pid')
    if [[ $focus == "null" ]]; then
        ${EWW_BIN} update revealdock=true
    else 
        ${EWW_BIN} update revealdock=false
    fi
    $HOME/.config/eww/sidebar/scripts/icon.py
done
