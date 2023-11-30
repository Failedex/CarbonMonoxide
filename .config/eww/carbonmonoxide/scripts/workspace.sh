#!/bin/bash

$HOME/.config/eww/carbonmonoxide/scripts/workspace.py
while [ 1 == 1 ] ; do
    swaymsg -t subscribe '["workspace"]' > /dev/null
    $HOME/.config/eww/carbonmonoxide/scripts/workspace.py
done
