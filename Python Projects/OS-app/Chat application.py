"""
This is the central file of the application.
It will update and download the main software so you will never need to come here
to obtain the newest version of the software! I plan on expanding this concept, but
for now I will only stay with this app.

"""

from urllib import request
from os import system, getcwd

online_path = "https://raw.githubusercontent.com/Eis3/Server/master/Python%20Projects/OS-app/"
path = getcwd() + "\\"


# app boot
def boot():
    system("python startup.py")
    exit()


# app update all
def update():
    download_path = ""
    for line in request.urlopen(online_path + "UPDATE_FILES.txt").read().decode().split("\n"):
        if "path=" in line:
            download_path = line.split("=")[1]
        try:
            get_file(download_path, line)
        except NameError:
            pass
    pass


def get_file(file_path, name):
    with open(name, "w") as file:
        pass
    with open(name, "a") as file:
        for line in request.urlopen(online_path + file_path + name).read().decode().split("\n"):
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
        input("You need to update! Click enter to continue...")
        update()
        exit()
# config.txt not found
except FileNotFoundError:
    print("config.txt not found!")
    answer = str(input("Is this your first start up? YES/NO\n> ")).upper()
    if "N" in answer:
        print("Please contact the support as the current version can't be obtained! It must be that the program is" +
              "simply not installed or that you have mistakenly deleted the file.")
        input("Press enter to close...")
    else:
        update()