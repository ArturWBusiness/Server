

WIDTH, HEIGHT = int(input("Width: ")) + 1, int(input("Height: ")) + 1
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