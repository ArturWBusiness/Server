letters = {
    "a": [
        "╔═╗",
        "║ ║",
        "╠═╣",
        "║ ║",
        "║ ║"
    ],
    "b": [
        "╔═ ",
        "║ )",
        "╠═ ",
        "║ )",
        "╚═ "
    ],
    "c": [
        "╔══",
        "║  ",
        "║  ",
        "║  ",
        "╚══"
    ],
    "d": [
        "╔X ",
        "X X",
        "X X",
        "X X",
        "XX "
    ],
    "e": [
        "╔══",
        "║  ",
        "╠══",
        "║  ",
        "╚══"
    ],
    "f": [
        "╔══",
        "║  ",
        "╠══",
        "║  ",
        "║  "
    ],
    "g": [
        "XXX",
        "X  ",
        "X X",
        "X X",
        "XXX"
    ],
    "h": [
        "║ ║",
        "║ ║",
        "╠═╣",
        "║ ║",
        "║ ║"
    ],
    "i": [
        "XXX",
        " X ",
        " X ",
        " X ",
        "XXX"
    ],
    "j": [
        "  X",
        "  X",
        "  X",
        "X X",
        "XXX"
    ],
    "k": [
        "X X",
        "X X",
        "XX ",
        "X X",
        "X X"
    ],
    "l": [
        "X  ",
        "X  ",
        "X  ",
        "X  ",
        "XXX"
    ],
    "m": [
        "XXXXX",
        "X X X",
        "X X X",
        "X X X",
        "X X X"
    ],
    "n": [
        "XXX",
        "X X",
        "X X",
        "X X",
        "X X"
    ],
    "o": [
        "XXXX",
        "X  X",
        "X  X",
        "X  X",
        "XXXX"
    ],
    "p": [
        "XXX",
        "X X",
        "XXX",
        "X  ",
        "X  "
    ],
    "q": [
        "XXX",
        "X X",
        "XXX",
        "  X",
        "  X"
    ],
    "r": [
        "XX ",
        "X X",
        "XX ",
        "X X",
        "X X"
    ],
    "s": [
        "XXX",
        "X  ",
        " X ",
        "  X",
        "XXX"
    ],
    "t": [
        "═╦═",
        " ║ ",
        " ║ ",
        " ║ ",
        " ║ "
    ],
    "u": [
        "║ ║",
        "║ ║",
        "║ ║",
        "║ ║",
        "╚═╝"
    ],
    "v": [
        "X X",
        "X X",
        "X X",
        "X X",
        " X "
    ],
    "w": [
        "X   X",
        "X   X",
        "X X X",
        "X X X",
        " X X "
    ],
    "x": [
        "X X",
        "X X",
        " X ",
        "X X",
        "X X"
    ],
    "y": [
        "X X",
        "X X",
        " X ",
        " X ",
        " X "
    ],
    "z": [
        "XXX",
        "  X",
        " X ",
        "X  ",
        "XXX"
    ],
    " ": [
        "   ",
        "   ",
        "   ",
        "   ",
        "   "
    ],
    "0": [
        "XXX",
        "X X",
        "X X",
        "X X",
        "XXX"
    ],
    "1": [
        "XX ",
        " X ",
        " X ",
        " X ",
        "XXX"
    ],
    "2": [
        "XXX",
        "  X",
        "XXX",
        "X  ",
        "XXX"
    ],
    "3": [
        "XXX",
        "  X",
        "XXX",
        "  X",
        "XXX"
    ],
    "4": [
        "X X",
        "X X",
        "XXX",
        "  X",
        "  X"
    ],
    "5": [
        "XXX",
        "X  ",
        "XXX",
        "  X",
        "XXX"
    ],
    "6": [
        "XXX",
        "X  ",
        "XXX",
        "X X",
        "XXX"
    ],
    "7": [
        "XXX",
        "  X",
        "  X",
        "  X",
        "  X"
    ],
    "8": [
        "XXX",
        "X X",
        "XXX",
        "X X",
        "XXX"
    ],
    "9": [
        "XXX",
        "X X",
        "XXX",
        "  X",
        "XXX"
    ],
    "!": [
        " X ",
        " X ",
        " X ",
        "   ",
        " X "
    ],
    "?": [
        "XXX",
        "  X",
        " XX",
        "   ",
        " X "
    ],
    ".": [
        " ",
        " ",
        " ",
        " ",
        "O"
    ],
    ",": [
        " ",
        " ",
        " ",
        " ",
        "/"
    ]
}

def gpring(string):
    out = [""]*5
    for character in string.lower():
        for i, row in enumerate(letters[character]):
            out[i] += row + " "
    for line in out:
        print(line)

user = "undefined"
while not user == "":
    user = input("\nDISPLAY>")
    print("")
    gpring(user)