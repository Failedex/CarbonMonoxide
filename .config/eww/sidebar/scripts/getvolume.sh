#!/bin/bash

MUTED=$(pacmd list-sinks | awk '/muted/ { print $2 }' | grep "no")

if [[ -z "$MUTED" ]]; then
    echo "󰝟 Muted"
else 
    echo -n "󰕾 "
    amixer sget Master | grep 'Left:' | awk -F'[][]' '{ print $2 }'  
fi
