#!/bin/sh

# focused_window_border_mode="$(swaymsg -t get_tree | jq -r '.. | select(.type?) | select(.focused==true).border')"

keyboard="1:1:AT_Translated_Set_2_keyboard"

case "$1" in
    # tablet)    new_border_mode="normal" && swaymsg input $keyboard events disabled && swaymsg default_border normal;;
    # *) new_border_mode="pixel" && swaymsg input $keyboard events enabled && swaymsg default_border pixel 2;;
    tablet)    swaymsg input $keyboard events disabled && swaymsg "[app_id='.*']" inhibit_idle open;;
    *) swaymsg input $keyboard events enabled && swaymsg "[app_id='.*']" inhibit_idle none;;
esac

swaymsg "[workspace=\"^[1-5]$\"] border $new_border_mode"

