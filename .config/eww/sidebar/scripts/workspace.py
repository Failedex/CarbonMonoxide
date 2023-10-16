#!/usr/bin/env python3

import subprocess
import json

def get_workspaces():
    result = subprocess.run("swaymsg -r -t get_workspaces", shell = True, capture_output=True, text=True).stdout
    result = json.loads(result)

    active = ["(label :style 'color: #6e6a86;' :text '')" for _ in range (5)]

    for res in result:
        if not res["output"] == "eDP-1": continue
        if res["num"]%10-1 > 4 or res["num"]%10-1 < 0:
            continue
        active[res["num"]%10-1] = "(label :text '')"
        if res["focused"]:
            active[res["num"]%10-1] = "(label :text '')"

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
    literal = "(box	:class 'workspaces widget'	:orientation 'v' :space-evenly true "
    for i, lab in enumerate(active):
        literal += f"(button :onclick \"swaymsg -t command 'workspace number {i+1}'\" {lab}) "
    print (literal + ")")

if __name__ == "__main__":
    main()
