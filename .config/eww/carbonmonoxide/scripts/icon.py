#!/usr/bin/env python3
from iconfetch import fetch
import subprocess
import json

def recurse(node, apps): 
    if "app_id" in node and node["app_id"]:

        apps.append({
            "app_id": node["app_id"],
            "name": node["name"],
            "pid": node["pid"], 
            "focused": node["focused"]
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
    # memo = set()

    for output in result["nodes"]:
        if output["name"] != "eDP-1" and output["name"] != "DP-1": 
            continue 
        for workspace in output["nodes"]: 
            # if not workspace["name"] == focus: 
            #     continue
            recurse(workspace, apps)

    # literal = "(box :orientation 'h' :space-evenly true "
    # apps that should just be there

    # permanent = ["firefox", "thunar", "xournalpp", "discord"]
    #
    # for p in permanent:
    #     found = False
    #     i = 0
    #     while i < len(apps):
    #         app = apps[i]["app_id"].lower()
    #         pid = apps[i]["pid"]
    #         if app == p or (app == "com.github.xournalpp.xournalpp" and p == "xournalpp"):
    #             apps[i]["path"] = fetch(app)
    #             appsjson.append(apps[i].copy())
    #             found = True
    #             del apps[i]
    #             break
    #         i += 1
    #
    #     if not found: 
    #         appsjson.append({
    #             "path": fetch(p),
    #             "app_id": p, 
    #             "pid": None , 
    #             "focused": False
    #         })
    #

    appsdict = {
        "firefox": [],
        "thunar": [], 
        "xournalpp": [], 
        "discord": [], 
        "foot": []
    }
    appsjson = []

    for app in apps: 
        name = app["app_id"].lower()
        path = fetch(name)
        
        # xournalpp is annoying
        if name == "com.github.xournalpp.xournalpp":
            name = "xournalpp"

        if path: 
            a = app.copy()
            a["path"] = fetch(name)
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


    print(json.dumps(appsjson))

if __name__ == "__main__":
    main()
