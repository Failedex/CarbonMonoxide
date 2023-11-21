#!/bin/env python3

import json 
import subprocess
import os
from iconfetch import fetch
from sys import argv

eww_bin= [subprocess.getoutput("which eww"), "-c", f"{os.path.expanduser('~')}/.config/eww/sidebar"]

def get_log():
    return json.loads(subprocess.getoutput(f"{' '.join(eww_bin)} get notifications"))

def update_log(updated, recent): 
    subprocess.run([eww_bin[0], eww_bin[1], eww_bin[2], "update", f"notifications={json.dumps(updated)}"])
    subprocess.run([eww_bin[0], eww_bin[1], eww_bin[2], "update", f"newnotification={json.dumps(recent)}"])

def dismiss(): 
    blank = {"source": "", "icon": "", "summary": "", "body": "", "action": "", "timeout": -1}
    subprocess.run([eww_bin[0], eww_bin[1], eww_bin[2], "update", f"newnotification={json.dumps(blank)}"])


if __name__ == "__main__": 
    if argv[1] == "listen":
        proc = subprocess.Popen(["tiramisu", "-s", "-o", '{"source": "#source", "icon": "#icon", "summary": "#summary", "body": "#body", "action": "#actions", "timeout": #timeout}'], stdout=subprocess.PIPE, text=True)
        while True:
            new_noti = proc.stdout.readline()
            if new_noti:
                try:
                    new_noti = json.loads(new_noti)
                    if new_noti["icon"] == "":
                        new_noti["icon"] = fetch(new_noti["source"])
                    noti = get_log()
                    noti.append(new_noti)
                    update_log(noti, new_noti)
                except Exception as e:
                    print(e)
                    pass

    if argv[1] == "dismiss":
        dismiss()


