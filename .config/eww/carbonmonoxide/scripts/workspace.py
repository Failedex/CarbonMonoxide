#!/usr/bin/env python3

import subprocess
import json
import os

eww_bin= [subprocess.getoutput("which eww"), "-c", f"{os.getcwd()}"]

def get_workspaces():
    result = subprocess.run("swaymsg -r -t get_workspaces", shell = True, capture_output=True, text=True).stdout
    result = json.loads(result)

    # active = ["(label :style 'color: #6e6a86;' :text '')" for _ in range (5)]
    active = []

    for i in range(1, 6): 
        active.append(dict(
            focused = False,
            empty = True, 
            name = i
        ))

    for res in result:
        if not res["output"] == "eDP-1": continue
        if res["num"]%10-1 > 4 or res["num"]%10-1 < 0:
            continue
        active[res["num"]%10-1]["empty"] = False
        if res["focused"]:
            active[res["num"]%10-1]["focused"] = True

    return active

def main():
    print(json.dumps(get_workspaces()))
    while True: 
        subprocess.run(["swaymsg", "-t" ,"subscribe", "[\"workspace\"]"], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        subprocess.run(eww_bin + ["update", f"workspacejson={json.dumps(get_workspaces())}"])

if __name__ == "__main__":
    main()
