#!/usr/bin/python3
import requests
import json

try:
    req = requests.get("https://api.quotable.io/random/?maxLength=78").text
    res = json.loads(req)
    print(f"(box :orientation 'v' :space-evenly true (label :text `\"{res['content']}\"`) (label :style 'font-size: 14;' :text `- {res['author']}`))")
except:
    print("(box :orientation 'v' :space-evenly true (label :text `\"I can't get quotes, you are not online right now.\"`) (label :style 'font-size: 14;' :text '- quote widget'))")
