#!/usr/bin/python3

import tkinter
from tkinter import messagebox as msg
import time
import json
import traceback
import os
import sys
from datetime import datetime

root = tkinter.Tk()
root.withdraw()

class alert:
    def info(title, message):
        msg.showinfo(title, message)
    def warning(title, message):
        msg.showwarning(title, message)
    def error(title, message):
        msg.showerror(title, message)

def load_config(fn):
    try:
        with open(fn, "r") as f:
            return json.loads(f.read())
    except Exception as err:
        traceback.print_exc()
        return None

def save_config(fn, cfg):
    try:
        with open(fn, "w+") as f:
            f.write(json.dumps(cfg))
            return True
    except Exception as err:
        traceback.print_exc()
        return False

home = os.path.expanduser("~")
if not home:
    sys.stderr.write("Error getting user home directory!\n")
    sys.stderr.flush()
    sys.exit(1)

configfile = os.path.join(home, ".timedAlerts_config")

config = {"timers": []}

if not os.path.exists(configfile):
    with open(configfile, "w+") as f:
        f.write("")
    save_config(configfile, config)

config = load_config(configfile)

def make_alert(data):
    if data["type"] == "info":
        alert.info(data["title"], data["msg"])
    elif data["type"] == "warning":
        alert.warning(data["title"], data["msg"])
    elif data["type"] == "error":
        alert.warning(data["title"], data["msg"])

def check_timers():
    global config
    global configfile
    config = load_config(configfile)
    i = 0
    res = False
    for timer in config["timers"]:
        if time.time() >= timer["time"]:
            res = True
            make_alert(timer)
            config["timers"].pop(i)
            save_config(configfile, config)
            break
        i += 1
    if res:
        check_timers()

while True:
    check_timers()
    time.sleep(1)
