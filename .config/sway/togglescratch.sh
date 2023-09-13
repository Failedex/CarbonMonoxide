#!/usr/bin/bash

if swaymsg -t get_tree | grep $1;
then
    cur_focus="$(swaymsg -t get_tree | jq -r '.. | select(.type?) | select(.focused==true) | .app_id')"

    if [ "$cur_focus" == $1 ]; then
        swaymsg scratchpad show
    else
        swaymsg [app_id=$1] focus
    fi
else
    case "$1" in 
        "sterm") foot -a sterm &
        ;;
        "sncmpcpp") foot -a sncmpcpp ncmpcpp &
        ;;
        "sranger") foot -a sranger ranger&
        ;;
    esac
fi
