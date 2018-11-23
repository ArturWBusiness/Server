from util import File, getArgs


suffix = ["$"]
filepath = "C:\\Users\\Artur\\Documents\\GitHub\\Server\\Python_Projects\\circleGenerator.py"



def userInput():
    starter = suffix[0]
    for loopN, x in enumerate(suffix):
        if loopN == 0:
            continue
        starter += x
    result = input("\n" + starter + "> ")
    return result
    # return "help commands -p Eis3 -H \"{}\"".format(filepath)


def main():
    global suffix
    while True:
        userinput = userInput()

        # From user input makes "command args "line args" -kwargs value -kwargs "line value"
        command, args, kwargs = getArgs(userinput)
        print(command)
        print(args)
        print(kwargs)

        if command == "help":

            # Variables detected
            if len(args) != 0 or len(kwargs) != 0:
                pass

            print("?" + "-"*10 + "Help" + "-"*10 + "?")
            print("1) ")
        commands = {"file": File()}
        if command == "file":
            file = commands[command]
            file.changeFile("C:\\Users\\Artur\\Documents\\GitHub\\Server\\Python_Projects\\circleGenerator.py")
            file.cmdPrintFile()

if __name__ == "__main__":
    main()
