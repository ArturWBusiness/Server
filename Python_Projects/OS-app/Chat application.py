"""
This is the central file of the application.
It will update and download the main software so you will never need to come here
to obtain the newest version of the software! I plan on expanding this concept, but
for now I will only stay with this app.

"""

from urllib import request
import os
from time import sleep
import subprocess

online_path = "https://raw.githubusercontent.com/Eis3/Server/master/Python_Projects/OS-app/"  # Should never change.
path = os.getcwd() + "\\"


# app boot
def boot():
    os.system("python startup.py")
    exit()


# app update all
def update():
    download_path = ""
    print("Downloading...")
    for line in request.urlopen(online_path + "UPDATE_FILES.txt").read().decode().split("\n"):
        line = line.strip("\r")
        if "path=" in line:
            download_path = line.split("=")[1]
            continue
        if line == "":
            continue
        try:
            get_file(download_path, line)
            print("Downloading files from '" + download_path + "/" + line)
        except EnvironmentError:
            print("Error")
    boot()


# Function to obtain the file from the "cloud"
def get_file(file_path, name):
    # Checks if the directory exists.
    if file_path == "":
        pass
    elif not os.path.exists(file_path):
        os.makedirs(file_path)  # TODO: Allow for folders in folders
    print("requesting " + name)
    # Take care of .png's
    if name[-4:] == ".png":
        print("Downloading")
        with open(file_path + name, "wb") as file:
            file.write(request.urlopen(online_path + file_path + name).read())
    # Files that are not images.
    else:
        with open(file_path + name, "w") as file:  # makes the files
            pass
        with open(file_path + name, "a") as file:  # prints into the file
            for line in request.urlopen(online_path + file_path + name).read().decode():
                file.write(line)


try:
    # version check
    with open("config.txt", "r") as file:
        for line in file:
            # find version=X.X
            variable = line.strip("\n").split("=")  # 0 = name 1 = value
            if variable[0] == "version":
                print("Found the current version to be " + str(variable[1]))
                break
    # get most updated version
    for line in request.urlopen(online_path + "config.txt").read().decode().split("\n"):
        server_variable = line.split("=")  # 0 = name 1 = value
        if server_variable[0] == "version":
            print("The server requires version " + str(server_variable[1]))
            break
    # if up to date
    if str(server_variable[1]) == str(variable[1]):
        print("Your version is up to date!\nBooting...")
        boot()
        exit()
    else:
        user_respond = input("Your version is not up-to-date! We highly recomend that you update!\nClick enter to continue or type in \"noupdate\" to cancel the updating")
        if user_respond == "noupdate":
            boot()
        else:
            update()
        exit()
# config.txt not found
except FileNotFoundError:
    print("config.txt not found!")
    answer = str(input("Is this your first start up? YES/NO\n> ")).upper()
    if "N" in answer:
        print("Please contact the support as the current version can't be obtained!\nIt must be that the program is" +
              "simply not installed or that you have mistakenly deleted the file.")
        input("Press enter to close...")
    else:
        update()