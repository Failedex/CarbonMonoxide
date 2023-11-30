#!/bin/env python3

import json 
import subprocess
import random
import os
import time 
import threading
from iconfetch import fetch
from sys import argv
import base64

eww_bin= [subprocess.getoutput("which eww"), "-c", f"{os.path.expanduser('~')}/.config/eww/carbonmonoxide"]

def get_log():
    return json.loads(subprocess.getoutput(f"{' '.join(eww_bin)} get notifications"))

def update_log(updated, recent): 
    if updated is not None: 
        subprocess.run([eww_bin[0], eww_bin[1], eww_bin[2], "update", f"notifications={json.dumps(updated)}"])
    if recent is not None:
        subprocess.run([eww_bin[0], eww_bin[1], eww_bin[2], "update", f"newnotification={json.dumps(recent)}"])

def dismiss(): 
    blank = {"source": "", "icon": "", "summary": "", "body": "", "action": "", "timeout": -1, "id": "", "sicon": ""}
    update_log(None, blank)

def timeout(t): 
    time.sleep(t/1000)
    blank = {"source": "", "icon": "", "summary": "", "body": "", "action": "", "timeout": -1, "id": "", "sicon": ""}
    update_log(None, blank)

def remove(id): 
    notis = get_log()
    for i in range(len(notis)): 

        if notis[i]["id"] == id:
            del notis[i]
            break

    update_log(notis, None)

if __name__ == "__main__": 
    if argv[1] == "listen":
        proc = subprocess.Popen(["tiramisu", "-s", "-o", '{"source": "#source", "icon": "#icon", "summary": "#summary", "body": "#body", "action": "#actions", "timeout": #timeout, "id": "#id"}'], stdout=subprocess.PIPE, text=True)
        while True:
            new_noti = proc.stdout.readline().replace("\\", "\\\\")
            if new_noti:
                try:
                    new_noti = json.loads(new_noti)

                    # parse hints 
                    # hints = new_noti["hints"]
                    #
                    # print(hints)

                    # hints = hints.split(",")
                    # new_noti["sender-pid"]=hints[0].split("=")[1]
                    # new_noti["urgency-pid"]=hints[2].split("=")[1]
                    # img = new_noti["hints"].split(":")[-1]

                    # with open("/tmp/img.png", "wb") as fh: 
                    #     fh.write(img)
                    #
                    # del new_noti["hints"]

                    noti = get_log()

                    new_noti["sicon"] = fetch(new_noti["source"])

                    new_noti["id"] = str(random.randint(0, 999999))

                    if new_noti["timeout"] != -1:
                        d = threading.Thread(target=timeout, args=(new_noti["timeout"],))
                        d.start()

                    noti.insert(0, new_noti)
                    update_log(noti, new_noti)
                except Exception as e:
                    print(e)
                    pass

    if argv[1] == "dismiss":
        dismiss()

    if argv[1] == "remove":
        if argv[2]:
            remove(argv[2])

    if argv[1] == "removeall":
        update_log([], None)
