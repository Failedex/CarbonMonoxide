# Carbon Monoxide, a sway dotfile

![Carbon Monoxide ss](https://github.com/Failedex/CarbonMonoxide/blob/main/assests/carbonmonoxide.png?raw=true)

![Carbon Monoxide bar demonstration](https://github.com/Failedex/CarbonMonoxide/blob/main/assests/carbonmonoxide.gif?raw=true)

## Featuring
- Oxocarbon colour scheme
- Eww bar and animations
- Widgets
- Iosevka, if you want
- "Touch friendly" set up (configuration was made for my touchscreen laptop)
- Light mode bar???
- The worst configuration files you have ever seen
- A few [symptoms](https://www.mayoclinic.org/diseases-conditions/carbon-monoxide/symptoms-causes/syc-20370642), only a few.

## Dependencies 

The config will still run without these, but there will be silent errors and missing features. 
- Iosevka Nerd Font
- pamixer
- brightnessctl
- nmcli
- playerctl
- mpc (and mpd I guess)
- grim and wl-copy
- python3 (for quotes, weather, timer, and sway workspaces)
- wvkbd-mobintl and wofi (for touchscreen purposes)
- swaylock
- a file under `~/Documents/fuck.txt`. This is a to do list

## Set up 
Just a heads up that my eww binary is under `~/.local/bin/eww`, which might not be the case for you. If this is the case, edit `/.config/sway/autostart.sh` and `/.config/eww/sidebar/scripts/pop`.

It should be possible to set this configuration up using 
```
stow .
```

If there are any conflicts, move your current configurations somewhere else. I ecourage users to look through the config and make your own changes, because the defaults are tailored to my preferences, and my preference is a bit silly. 
Alternatively, just use this as a reference.
