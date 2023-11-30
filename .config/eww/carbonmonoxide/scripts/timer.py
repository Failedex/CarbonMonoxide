#!/usr/bin/env python3
import time
import os
import sys

def startstop():
    if os.path.exists("/tmp/timerstamp"):
        os.remove("/tmp/timerstamp")
        os.popen("notify-send 'timer stopped'")
    else:
        with open("/tmp/timerstamp", "x") as f:
            f.write(str(time.time()))
        os.popen("notify-send 'timer start'")

        
def readtime():

    with open("/tmp/timer") as f:
        timer = int(f.read())

    current = time.time()
    
    if os.path.exists("/tmp/timerstamp"):
        with open("/tmp/timerstamp") as f:
            timestamp = float(f.read())

        if current - timestamp >= timer*60:
            print("OwO")
        else:
            m, s = divmod((timer*60) - (current-timestamp), 60)
            print (f"{int(m)}:{int(s)}")

    else:
        print(timer)

def loop():
    if not os.path.exists("/tmp/timer"):
        with open("/tmp/timer", "x") as f: 
            f.write("25")

    while True:
        with open("/tmp/timer") as f:
            timer = int(f.read())

        current = time.time()
        if os.path.exists("/tmp/timerstamp"):
            with open("/tmp/timerstamp") as f:
                timestamp = float(f.read())

            if current - timestamp >= timer*60:
                os.remove("/tmp/timerstamp")
                os.popen("notify-send 'time is up'")
            
        time.sleep(1)

def substate():
    if os.path.exists("/tmp/timerstamp"):
        print("stop")
    else: 
        print("start")

def timeinc():
    with open("/tmp/timer", "r") as f:
        timer = int(f.read())

    timer+=5
    with open("/tmp/timer", "w") as f:
        f.write(str(timer))

def timedec():
    with open("/tmp/timer", "r") as f:
        timer = int(f.read())

    timer-=5
    with open("/tmp/timer", "w") as f:
        f.write(str(timer))

a = sys.argv[1]

if a == "loop":
    loop()
if a == "toggle":
    startstop()
if a == "subscribe":
    readtime()
if a == "substate":
    substate()
if a == "timedec":
    timedec()
if a == "timeinc":
    timeinc()
