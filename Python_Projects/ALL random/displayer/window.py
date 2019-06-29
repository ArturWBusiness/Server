colorf = {
    "dark_gray": "1;30",
    "bright_red": "1;31",
    "bright_green": "1;32",
    "yellow": "1;33",
    "bright_blue": "1;34",
    "bright_magenta": "1;35",
    "bright_cyan": "1;36",
    "white": "1;37",
    "black": "0;30",
    "red": "0;31",
    "green": "0;32",
    "brown": "0;33",
    "blue": "0;34",
    "magenta": "0;35",
    "cyan": "0;36",
    "light_gray": "0;37",
}
colorb = {
    "red": "41",
    "green": "42",
    "yellow": "43",
    "blue": "44",
    "magenta": "45",
    "cyan": "46",
    "white": "47",
    "black": "48"
}

def createColor(foreground="white", background="black"):
    return "\033["+colorf[foreground]+";"+colorb[background]+"m"

class Window:
    def __init__(self, width=82, height=31, char=u"\u2588", foreground="white", background="black"):
        self.char = char
        self.background = background
        self.foreground = foreground
        self.width = width
        self.height = height
        __import__("colorama").init()
        __import__("os").system("mode con: cols={} lines={}".format(str(width), str(height+1)))
        self.display = [[[char,(foreground, background)]]*width]*height
        self.old_display = [[[char, (foreground, background)]]*width]*height
        self.render()

    def render(self):
        for y, row in enumerate(self.display):
            for x, pixel in enumerate(row):
                print("\033[" + str(y+1) + ";" + str(x+1) + "H" + createColor(pixel[1][0], pixel[1][1]) + pixel[0])

    def draw(self):
        for y, row in enumerate(self.display):
            for x, pixel in enumerate(row):
                if pixel != self.old_display[y][x]:
                    print("\033[" + str(y+1) + ";" + str(x+1) + "H" + createColor(pixel[1][0], pixel[1][1]) + pixel[0])

        self.old_display = self.display.copy()

    def clear(self):
        self.display = [[[u"\u2588",("white", "black")]]*self.width]*self.height

    def setPixel(self, x, y, char="X", color="blue", background="black"):
        row = self.display[y].copy()
        print(row)
        hell = row[x] = [char, (color, background)]
        print(self.display[y])
        exit()

