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

def parse_arguments(argvs):
    out = {"time": time.time() + 1, "type": "info", "title": "MessageBox", "msg": "Message"}
    for arg in argvs:
        if arg.startswith("--time="):
            out["time"] = arg.split("=", 1)[1]
        elif arg.startswith("--type="):
            out["type"] = arg.split("=", 1)[1]
        elif arg.startswith("--title="):
            out["title"] = arg.split("=", 1)[1]
        elif arg.startswith("--msg="):
            out["msg"] = arg.split("=", 1)[1]
    return out

def parse_time(t):
    try:
        return time.mktime(datetime.strptime(t, "%d/%m/%Y %H:%M:%S").timetuple())
    except ValueError:
        print("Invalid time format \"{}\"".format(t))
        sys.exit(1)

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

argv = sys.argv

if (__file__ in argv and len(argv) == 1) or len(argv) == 0 or "-h" in argv or "--help" in argv:
    print("usage: set_timed_alert [-h] [--help] [--time=time_to_set_alert] [--type=info|warning|error] [--title=alert_title] [--msg=alert_message]")
    print("\nOptional arguents:")
    print("\t-h --help Print this message and exit")
    print("\t--time Time to set alert (day/month/year hour:minute:second) (example: 20/8/2018 17:41:53)")
    print("\t--type Alert type [info|warning|error]")
    print("\t--title Alert title")
    print("\t--msg Alert message")
    sys.exit(0)

argvs = parse_arguments(argv)

argvs["time"] = parse_time(argvs["time"])

config["timers"].append(argvs)

save_config(configfile, config)
