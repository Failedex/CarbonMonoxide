#!/usr/bin/env python3
from iconfetch import fetch
import subprocess
import json

def recurse(node, apps, memo): 
    if "app_id" in node and node["app_id"] not in memo and node["app_id"]:
        apps.append({
            "app_id": node["app_id"],
            "pid": node["pid"], 
            "focused": node["focused"]
        })
        memo.add(node["app_id"])
        
    for n in node["nodes"]: 
        recurse(n, apps, memo)

    for n in node["floating_nodes"]: 
        recurse(n, apps, memo)

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
    memo = set()

    for output in result["nodes"]:
        if output["name"] != "eDP-1" and output["name"] != "DP-1": 
            continue 
        for workspace in output["nodes"]: 
            # if not workspace["name"] == focus: 
            #     continue
            recurse(workspace, apps, memo)

    # literal = "(box :orientation 'h' :space-evenly true "
    appsjson = []

    # apps that should just be there

    permanent = ["firefox", "thunar", "xournalpp", "discord"]

    for p in permanent:
        found = False
        i = 0
        while i < len(apps):
            app = apps[i]["app_id"].lower()
            pid = apps[i]["pid"]
            if app == p or (app == "com.github.xournalpp.xournalpp" and p == "xournalpp"):
                # literal += f"(button :onclick 'swaymsg \"[pid={pid}] focus\" '(image :image-width 50 :image-height 50 :path \"{path}\")) "
                apps[i]["path"] = fetch(app)
                appsjson.append(apps[i].copy())
                found = True
                del apps[i]
                break
            i += 1

        if not found: 
            appsjson.append({
                "path": fetch(p),
                "app_id": p, 
                "pid": None , 
                "focused": False
            })
            # literal += f"(button :onclick '{p} &' (image :image-width 50 :image-height 50 :path \"{path}\")) "


    for app in apps: 
        path = fetch(app["app_id"].lower())
        if path: 
            a = app.copy()
            a["path"] = fetch(app["app_id"].lower())
            appsjson.append(a)
            # literal += f"(button :onclick 'swaymsg \"[pid={pid}] focus\" '(image :image-width 50 :image-height 50 :path \"{path}\")) "

    print(json.dumps(appsjson))

if __name__ == "__main__":
    main()
