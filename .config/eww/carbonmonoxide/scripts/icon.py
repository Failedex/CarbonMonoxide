#!/usr/bin/env python3
from iconfetch import fetch
import subprocess
import json
import os 

eww_bin= [subprocess.getoutput("which eww"), "-c", f"{os.path.expanduser('~')}/.config/eww/carbonmonoxide"]

def recurse(node, apps): 
    if "app_id" in node and node["app_id"]:
        node["app_id"] = node["app_id"].lower()

        if node["app_id"] == "com.github.xournalpp.xournalpp":
            node["app_id"] = "xournalpp"

        apps.append({
            "app_id": node["app_id"],
            "name": node["name"],
            "pid": node["pid"], 
            "focused": node["focused"],
            "rect": node["rect"],
            "path": fetch(node["app_id"]) or fetch("unknown")
        })

        # memo.add(node["app_id"])
        
    for n in node["nodes"]: 
        recurse(n, apps)

    for n in node["floating_nodes"]: 
        recurse(n, apps)

def main(): 

    result = subprocess.run("swaymsg -r -t get_tree", shell=True, capture_output=True, text=True).stdout
    result = json.loads(result)

    # result2 = subprocess.run("swaymsg -r -t get_workspaces", shell = True, capture_output=True, text=True).stdout
    # result2 = json.loads(result2)

    # get focused workspace 
    # focus = 0
    #
    # for res in result2: 
    #     if res["focused"]: 
    #         focus = res["name"]

    apps = []
    windows = [[] for _ in range(5)]
    external = False

    for output in result["nodes"]:
        if output["name"] != "eDP-1" and output["name"] != "DP-1": 
            continue 
        if output["name"] == "DP-1": 
            external = True
        for workspace in output["nodes"]: 
            # if not workspace["name"] == focus: 
            #     continue

            found = []
            recurse(workspace, found)

            apps.extend(found)
            if output["name"] == "eDP-1":
                windows[int(workspace["name"])-1] = found

    if external: 
        for w in windows: 
            for i in w:
                i["rect"]["x"] -= 1440

    appsdict = {
        "firefox": [],
        "thunar": [], 
        "xournalpp": [], 
        "discord": [], 
        "foot": []
    }
    appsjson = []

    for app in apps: 
        a = app.copy()
        name = a["app_id"]

        if name not in appsdict: 
            appsdict[name] = []
        appsdict[name].append(a)

    for key, value in appsdict.items(): 
        if len(value) == 0: 
            appsjson.append(dict(
                path = fetch(key),
                name = key,
                app_id = key, 
                pid = None, 
                focused = []
            ))

        else: 
            f = []
            for v in value: 
                f.append(v["focused"])

            appsjson.append(dict(
                path = value[0]["path"],
                name = value[0]["name"], 
                app_id = value[0]["app_id"].lower(), 
                pid = value[0]["pid"], 
                focused = f
            ))


    subprocess.run(eww_bin + ["update", f"windows={json.dumps(windows)}"])

    print(json.dumps(appsjson))

if __name__ == "__main__":
    main()
