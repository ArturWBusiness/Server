"""
Test?
some text?
hmm?
"""
from urllib import request

def boot():
    pass


try:
    with open("config.txt", "r") as file:
        for line in file:
            variable = line.strip("\n").split("=")  # 0 = name 1 = value
            if variable[0] == "version":
                print("Found the current version to be " + str(variable[1]))
                break
    for line in request.urlopen("https://raw.githubusercontent.com/Eis3/Server/master/Python%20Projects/OS-app/config.txt").read().decode().split("\n"):
        server_variable = line.split("=")  # 0 = name 1 = value
        if server_variable[0] == "version":
            print("The server requires version " + str(server_variable[1]))
            break
    if str(server_variable[1]) == str(variable[1]):
        print("Your version is up to date!\nBooting...")
    else:
        input("You need to update! Click enter to continue...")
except EOFError:
    pass
