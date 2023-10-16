#!/usr/bin/env python3
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess
import json

def iconfetch(icon_name):
    icon_theme = Gtk.IconTheme.get_default()
    icon = icon_theme.lookup_icon(icon_name, 48, 0)
    if icon:
        return icon.get_filename()
    else:
        return
def recurse(node, apps): 
    if "app_id" in node:
        apps.append(node["app_id"])
        
    for n in node["nodes"]: 
        recurse(n, apps)

def main(): 

    result = subprocess.run("swaymsg -r -t get_tree", shell=True, capture_output=True, text=True).stdout
    result = json.loads(result)

    result2 = subprocess.run("swaymsg -r -t get_workspaces", shell = True, capture_output=True, text=True).stdout
    result2 = json.loads(result2)

    # get focused workspace 
    focus = 0

    for res in result2: 
        if res["focused"]: 
            focus = res["name"]

    apps = []

    for output in result["nodes"]:
        if output["name"] != "eDP-1": 
            continue 
        for workspace in output["nodes"]: 
            if not workspace["name"] == focus: 
                continue
            recurse(workspace, apps)

    literal = "(box :class 'tasklist' :orientation 'v' :space-evenly true "
    for app in apps: 
        path = iconfetch(app.lower())
        if path: 
            literal += f"(image :image-width 30 :image-height 30 :path \"{path}\") "

    print(literal + ")")

if __name__ == "__main__":
    main()
