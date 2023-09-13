#!/usr/bin/env python3

import subprocess
import json

def get_workspaces():
    result = subprocess.run("swaymsg -r -t get_workspaces", shell = True, capture_output=True, text=True).stdout
    result = json.loads(result)

    active = ["", "", "", "", ""]

    for res in result:
        if not res["output"] == "eDP-1": continue
        if res["num"]%10-1 > 4 or res["num"]%10-1 < 0:
            continue
        active[res["num"]%10-1] = ""
        if res["focused"]:
            active[res["num"]%10-1] = ""

    return active

def main():
    # while True:
    #     # subprocess.call(["swaymsg",  "-t",  "subscribe",  "['workspace']"], shell=True) 
    #     subprocess.call("sleep 5s", shell=True)
    #     active = get_workspaces()
    #     literal = "(box	:class \"workspaces widget\"	:orientation \"h\" :spacing 5 :space-evenly \"false\" "
    #     for lab in active:
    #         literal += f"(label \"{lab}\") "
    #     print (literal)
    active = get_workspaces()
    literal = "(box	:class \"workspaces widget\"	:orientation \"v\" :spacing 5 :space-evenly \"false\" "
    for lab in active:
        literal += f"(label :text \"{lab}\") "
    print (literal + ")")

if __name__ == "__main__":
    main()
