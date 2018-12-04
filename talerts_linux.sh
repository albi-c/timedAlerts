#!/bin/sh

if [ $# -eq 0 ]; then
    echo "Too few arguments!"
    exit
fi

if [ $1 = "loop" ]; then
    check_alerts_loop $@
    exit
else
    if [ $1 = "set" ]; then
        set_timed_alert $@
        exit
    fi
fi

