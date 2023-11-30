#!/usr/bin/python3
import requests
import json
import time

mytime = time.localtime() 
day = (6 < mytime.tm_hour < 20)

code_icon = {
    113: "clear", 
    116: "few-clouds",
    119: "clouds",
    122: "clouds",
    143: "fog",
    176: "rain",
    179: "snow",
    182: "snow",
    185: "snow",
    200: "storm",
    227: "snow",
    230: "storm",
    248: "fog",
    260: "fog",
    263: "rain-light",
    266: "rain-light",
    281: "rain-light",
    284: "rain-light",
    293: "rain-light",
    296: "rain-light",
    299: "rain",
    302: "rain",
    305: "rain",
    308: "rain",
    311: "rain",
    353: "rain-light",
    356: "rain",
}

code_icon_n = {
    113: "clear-n", 
    116: "few-clouds-n",
    119: "clouds",
    122: "clouds",
    143: "fog",
    176: "rain",
    179: "snow",
    182: "snow",
    185: "snow",
    200: "storm",
    227: "snow",
    230: "storm",
    248: "fog",
    260: "fog",
    263: "rain-light",
    266: "rain-light",
    281: "rain-light",
    284: "rain-light",
    293: "rain-light",
    296: "rain-light",
    299: "rain",
    302: "rain",
    305: "rain",
    308: "rain",
    311: "rain",
    353: "rain-light",
    356: "rain",
}

try:
    req = requests.get(r"https://wttr.in/?format=j1").text
    req = json.loads(req)
    res = req["current_condition"][0].copy() 

    res["success"] = True

    code = int(res["weatherCode"])
    if day:
        if code in code_icon: 
            res["icon"] = code_icon[code]
        else: 
            res["icon"] = "idk"
    else:
        if code in code_icon_n: 
            res["icon"] = code_icon_n[code]
        else: 
            res["icon"] = "idk"

    # hourly 
    
    it = 0
    while it < 8 and int(req["weather"][0]["hourly"][it]["time"]) < mytime.tm_hour * 100:
        it += 1

    res["hourly"] = []
    for i in range(8): 
        res["hourly"].append(req["weather"][(it+i)//8]["hourly"][(it+i)%8].copy())

    for hour in res["hourly"]: 
        t = int(hour["time"])//100
        if t > 12:
            hour["time"] = f"{t-12}pm"
        elif t == 12: 
            hour["time"] = "12pm"
        elif t == 0: 
            hour["time"] = "12am"
        else:
            hour["time"] = f"{t}am"

        code = int(hour["weatherCode"])
        if day:
            if code in code_icon: 
                hour["icon"] = code_icon[code]
            else: 
                hour["icon"] = "idk"
        else:
            if code in code_icon_n: 
                hour["icon"] = code_icon_n[code]
            else: 
                hour["icon"] = "idk"


    print(json.dumps(res))

except Exception as e:
    print(e)
    print('{"success": false}')
