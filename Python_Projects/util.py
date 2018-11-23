from os import getcwd

DEBUGMODE = True


class File:
    def __init__(self, file=""):
        if "../" in file or "..\\" in file:
            self.file = self._getRealPath(file)
        else:
            self.file = file

    def changeFile(self, file):
        self.file = file

    def _getRealPath(self, path):
        returnNumber = path.count("../") + path.count("..\\")
        currentPath = getcwd().split("\\")
        for x in range(0, returnNumber):
            currentPath.pop()
        realPath = ""
        for folder in currentPath:
            realPath += folder
        return realPath

    def readFile(self):
        result = []
        with open(self.file, "r") as openedFile:
            for line in openedFile:
                result += [line]
        return result

    def cmdPrintFile(self):
        for line in self.readFile():
            print(line[:-1])


def getArgs(userinput=""):
    kwargSuffixs = ("/", "-")
    command = userinput.split(" ", 1)[0]
    try:
        allArgs = userinput.split(" ", 1)[1]  # sets args to "" if no args found
    except:
        allArgs = ""
    args = []
    kwargs = {}
    kwarg = None
    arg = None
    kwargFirst = False
    if allArgs != "":
        for unit in allArgs.split(" "):
            if kwarg is not None and not unit.startswith(kwargSuffixs):
                if kwargFirst:
                    kwargs[kwarg] = kwargs[kwarg] + unit
                    kwargFirst = False
                else:
                    kwargs[kwarg] = kwargs[kwarg] + " " + unit
                if unit.endswith("\""):
                    kwarg = None

            elif arg is not None and not unit.startswith(kwargSuffixs):
                arg = arg + " " + unit
                if unit.endswith("\""):
                    args.append(arg)
                    arg = None

            elif unit.startswith(kwargSuffixs):
                kwargs[unit] = ""
                kwarg = unit
                kwargFirst = True

            elif unit.startswith("\""):
                arg = unit
                if unit.endswith("\""):
                    args.append(arg)
                    arg = None

            else:
                args.append(unit)
    for id, arg in enumerate(args):
        if arg.startswith("\"") and arg.endswith("\""):
            args[id] = arg[1:-1]
    for name, value in kwargs.items():
        if value.startswith("\"") and value.endswith("\""):
            kwargs[name] = value[1:-1]
    return command.lower(), args, kwargs


def printCmd(string="", start="", end="", title=""):
    if title != "":
        title = "[" + title +"]"
    print(title + " " + start + string + end)


def DEBUG(string="", start="", end=""):
    if DEBUGMODE:
        printCmd(string=string, start=start, end=end, title="DEBUG")