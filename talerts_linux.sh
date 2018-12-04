#!/bin/sh

if [ $# -eq 0 ]; then
    echo "usage: talerts [loop|add] [options]"
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
