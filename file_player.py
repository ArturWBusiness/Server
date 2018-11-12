import os
from msvcrt import getch
import _thread
from time import sleep

print("\n"*300)
file_path = os.path.dirname(os.path.realpath(__file__))
current_path = "\\"
path_cut = len(file_path) + len(current_path)
print(file_path+current_path)
arrow = [" <---"] + [""]*23
line_selected = 0


def get_path():
    folders = [x[0] for x in os.walk(file_path+current_path)]
    path_cut = len(file_path) + len(current_path)
    existing_folders = [""]
    for folder in folders:
        folder_name = folder[path_cut:]
        if "\\" in folder_name:
            folder_name = folder_name.split("\\")[0]
        if folder_name in existing_folders:
            continue
        else:
            existing_folders.append(folder_name)
    return existing_folders


def display():
    while True:
        sleep(1/60)
        files = get_path()
        for i, x in enumerate(arrow):
            try:
                print(files[i] + x)
            except:
                print(x)

def arrow_up():
    global arrow, line_selected
    if line_selected == 0:
        return
    line_selected -= 1
    arrow.pop(0)
    arrow.append("")


def arrow_down():
    global arrow, line_selected
    if line_selected == 23:
        return
    line_selected += 1
    arrow.pop()
    arrow = [""] + arrow


def keyboard():
    global current_path, line_selected, arrow
    while True:
        key = ord(getch())
        if key == 27:  # ESC
            # go back 1
            pass
        elif key == 13: #Enter NOT WORKING <------------------
            try:
                if get_path()[line_selected] == "":
                    raise NameError
                current_path = current_path + get_path()[line_selected] + "\\"
                arrow = ["<---"] + [""] * 23
                line_selected = 0
            except:
                print("No folder found!\n"*100)
        elif key == 224:  # Special keys (arrows, f keys, ins, del, etc.)
            key = ord(getch())
            if key == 72:  # Up arrow
                arrow_up()
            elif key == 80:  # Down arrow
                arrow_down()


_thread.start_new_thread(display, ())

keyboard()