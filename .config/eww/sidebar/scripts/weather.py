#!/usr/bin/python3
import requests

try:
    req = requests.get(r"https://wttr.in?0QT").text.replace("\\", "\\\\")
    print (req)
except:
    print("no wifi")
