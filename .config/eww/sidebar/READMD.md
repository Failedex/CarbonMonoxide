# Ewwwtf 2, Electric Boogaloo
This configuration is made friendly to touchscreen laptops, feel free to remove the feature if you want though.

## Warning! 
The following dotfile may contain code that may be harmful or traumatizing to some readers. 

## Dependencies
This configuration is made for sway, but can be modified to be used on X window managers or other compositors. Good luck with that.

- pamixer
- brightnessctl
- nmcli
- playerctl
- mpc (and mpd I guess)
- grim and wl-copy
- python3 (for quotes, weather, timer, and sway workspaces)
- wvkbd-mobintl and wofi (for touchscreen purposes)

## Set up
Modify the path under `./scripts/workspace.sh` and `./scripts/pop`. 

Run the config using
```
/PATH/to/dir/.scripts/timer.py loop &
eww daemon &
eww -c /PATH/to/file open bar &
```
You can run this with your wm at start up.



We don't talk about ewwwtf 1. 
