#!/bin/sh

export MOZ_ENABLE_WAYLAND=1
export XDG_CURRENT_DESKTOP=sway
# source /etc/profile
dbus-run-session sway
