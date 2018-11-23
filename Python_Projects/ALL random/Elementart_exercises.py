

def drawTABLE(WIDTH, HEIGHT):
    if WIDTH > 999:
        WIDTH = 1000
    if HEIGHT > 999:
        HEIGHT = 1000

    toprow = "[   ] "
    for x in range(1, WIDTH):
        summ = str(x)
        if len(summ) == 1:
            summ += "_____"
        elif len(summ) == 2:
            summ += "____"
        elif len(summ) == 3:
            summ += "___"
        elif len(summ) == 4:
            summ += "__"
        elif len(summ) == 5:
            summ += "_"
        toprow += summ + "|"
    print(toprow)
    for y in range(1, HEIGHT):
        row = ""
        if len(str(y)) == 1:
            row = "[" + str(y) + "  ] "
        elif len(str(y)) == 2:
            row = "[" + str(y) + " ] "
        elif len(str(y)) == 3:
            row = "[" + str(y) + "] "
        for x in range(1, WIDTH):
            summ = str(x*y)
            if len(summ) == 1:
                summ += "     "
            elif len(summ) == 2:
                summ += "    "
            elif len(summ) == 3:
                summ += "   "
            elif len(summ) == 4:
                summ += "  "
            elif len(summ) == 5:
                summ += " "
            row += summ + "|"
        print(row)


def clear():
    print("\n"*55)


clear()
while True:
    command = str(input("$root> ")).lower()
    if command == "help":
        print("?" + "-"*7 + "[Possible Commands]" + "-"*7 + "?\n" + "1) help - Displayes this help window\n" + "2) table - Allow a user to make a table\n" + "3) cls/clear - Prints 40 blank lines\n")
    elif command == "table":
        args = str(input("Please write in the format WIDTHxHEIGHT (e.g. 60x30)\n&root TABLE> ")).lower()
        if "x" in args:
            try:
                width, height = args.split("x")
                width = int(width)
                height = int(height)
                drawTABLE(width + 1, height + 1)
            except ValueError:
                print("            Syntax error. Usage: WIDTHxHEIGHT")
    elif command == "cls" or command == "clear":
        clear()
