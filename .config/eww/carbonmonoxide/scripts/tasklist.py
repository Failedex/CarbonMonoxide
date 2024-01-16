#!/usr/bin/env python3
from iconfetch import fetch
import subprocess
import json
import os 

eww_bin= [subprocess.getoutput("which eww"), "-c", f"{os.getcwd()}"]

def recurse(node, apps, output): 
    if "app_id" in node and node["app_id"]:
        node["app_id"] = node["app_id"].lower()

        if node["app_id"] == "com.github.xournalpp.xournalpp":
            node["app_id"] = "xournalpp"

        node["rect"]["x"] -= output["rect"]["x"]
        node["rect"]["y"] -= output["rect"]["y"]
        # for monitors that aren't 1920/1080
        node["rect"]["width"] *= 1920/output["rect"]["width"]
        node["rect"]["height"] *= 1080/output["rect"]["height"]
        node["rect"]["x"] *= 1920/output["rect"]["width"]
        node["rect"]["y"] *= 1080/output["rect"]["height"]

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
        recurse(n, apps, output)

    for n in node["floating_nodes"]: 
        recurse(n, apps, output)

def update(): 

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
    windows = [[] for _ in range(10)]

    for output in result["nodes"]:
        if output["name"] != "eDP-1" and output["name"] != "DP-1": 
            continue 
        for workspace in output["nodes"]: 
            # if not workspace["name"] == focus: 
            #     continue

            found = []
            recurse(workspace, found, output)

            apps.extend(found)
            # if output["name"] == "eDP-1":
            #     windows[int(workspace["name"])-1] = found
            windows[int(workspace["name"])-1] = found

    # change this yourself lol
    appsdict = {
        "firefox": [],
        "thunar": [], 
        "xournalpp": [], 
        "discord": [], 
        "foot": []
    }
    # translate to launch cmd
    appsexec = {
        "discord": "discord-wayland",
        "xournalpp": "com.github.xournalpp.xournalpp",
        "foot": "org.codeberg.dnkl.foot",
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
                app_id = key if key not in appsexec else appsexec[key], 
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
    subprocess.run(eww_bin + ["update", f"tasksjson={json.dumps(appsjson)}"])

def main():
    update()
    while True: 
        subprocess.run(["swaymsg", "-t", "subscribe", "[\"window\", \"workspace\"]"], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

        update()
    

if __name__ == "__main__":
    main()
