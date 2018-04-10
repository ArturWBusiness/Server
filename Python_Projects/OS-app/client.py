import _thread as thread
import socket
import tkinter
# This version is: Alpha 1.110a
this_version = "Alpha 1.110a"

# Check if config.txt exists
try:
    # version check
    with open("config.txt", "r") as file:
        for line in file:
            # find version=X.X
            variable = line.strip("\n").split("=")  # 0 = name 1 = value
            # Setting correct values in the config.txt
            if variable[0] == "version":
                if variable[1] != this_version:
                    change the version number
            if variable[0]


# First time boot up
except:
    with open("config.txt", "w") as file:


    make it with defualt options
else
    read config.txt
    update the version
    set up a version

load graphics(




)

set up defualt connection

