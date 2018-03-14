"""
Test?
some text?
hmm?
"""


with open("config.txt", "r") as file:
    for line in file:
        variable = line.strip("\n").split("=")  # 0 = name 1 = value
        if variable[0] == "version":
            print("Found the current version to be " + str(variable[1]))
