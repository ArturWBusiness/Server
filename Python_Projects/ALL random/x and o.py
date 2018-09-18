screen = [
    [" "," "," ","|"," "," "," ","|"," "," "," "],
    [" "," "," ","|"," "," "," ","|"," "," "," "],
    [" "," "," ","|"," "," "," ","|"," "," "," "],
    ["─","─","─","+","─","─","─","+","─","─","─"],
    [" "," "," ","|"," "," "," ","|"," "," "," "],
    [" "," "," ","|"," "," "," ","|"," "," "," "],
    [" "," "," ","|"," "," "," ","|"," "," "," "],
    ["─","─","─","+","─","─","─","+","─","─","─"],
    [" "," "," ","|"," "," "," ","|"," "," "," "],
    [" "," "," ","|"," "," "," ","|"," "," "," "],
    [" "," "," ","|"," "," "," ","|"," "," "," "]
]

# image[0][y][x] = X
#      [1]       = O
image = [
    [
        ["\\"," ","/"],
        [" ","X"," "],
        ["/"," ","\\"]
    ],
    [
        ["/","─","\\"],
        ["|"," ","|"],
        ["\\","─","/"]
    ]
]
renter_temp = ""
turn = 1 # odd=X even=O
# Renders the play field.
def render():
    global renter_temp
    for i, line in enumerate(screen):
        for i2, pixel in enumerate(line):
            renter_temp += str(pixel)
        print(renter_temp)
        renter_temp = ""


def clear():
    print("\n"*50)


# 7 8 9
# 4 5 6
# 1 2 3
def set_box(args):
    global turn
    cords, type = args
    for y in (0, 1, 2):
        for x in (0, 1, 2):
            screen[x + (cords[0]*4-4)][y + (cords[1]*4)] = image[type][x][y]
    turn += 1


def user_plot():
    global turn, screen, screen_preset
    if turn%2 == 0:
        user_pick = int(input("\nIt is O's turn!\n7 8 9\n4 5 6\n1 2 3\n\nI pick> "))
        turn_type = 1
    else:
        user_pick = int(input("\nIt is X's turn!\n7 8 9\n4 5 6\n1 2 3\n\nI pick> "))
        turn_type = 0
    user_pick = user_pick_translate(user_pick)
    if user_pick == 0:
        screen = [[" "," "," ","|"," "," "," ","|"," "," "," "],[" "," "," ","|"," "," "," ","|"," "," "," "],[" "," "," ","|"," "," "," ","|"," "," "," "],["─","─","─","+","─","─","─","+","─","─","─"],[" "," "," ","|"," "," "," ","|"," "," "," "],[" "," "," ","|"," "," "," ","|"," "," "," "],[" "," "," ","|"," "," "," ","|"," "," "," "],["─","─","─","+","─","─","─","+","─","─","─"],[" "," "," ","|"," "," "," ","|"," "," "," "],[" "," "," ","|"," "," "," ","|"," "," "," "],[" "," "," ","|"," "," "," ","|"," "," "," "]]
        game()
    if user_pick > 6:
        y=0
        x=user_pick-6
    elif user_pick > 3:
        y=1
        x=user_pick-3
    else:
        y=2
        x=user_pick
    return (x, y), turn_type


def user_pick_translate(args):
    if args == 1:
        return 9
    if args == 2:
        return 6
    if args == 4:
        return 8
    if args == 6:
        return 2
    if args == 8:
        return 4
    if args == 9:
        return 1
    return args

def game():
    while True:
        clear()
        render()
        set_box(user_plot())


if __name__ == "__main__":
    game()