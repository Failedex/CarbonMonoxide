#!/usr/bin/python3
import requests

try:
    req = requests.get(r"https://wttr.in/?format=%t,%c").text
    print (req)
except:
    print("no wifi")
