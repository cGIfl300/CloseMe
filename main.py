# Copyright (C) 2021 cGIfl300

import subprocess
import time

import wmi

c = wmi.WMI()

Forbidden_Apps = [
    "hexchat.exe",
]
Cycle = 5  # Delay to rescan.


def do_kill(processus):
    subprocess.Popen("taskkill /f /im " + processus)
    print("The application " + processus + " has been killed.")


while True:
    for process in c.Win32_Process():
        for application in Forbidden_Apps:
            if process.Name.upper() == application.upper():
                do_kill(process.Name)

    time.sleep(Cycle)