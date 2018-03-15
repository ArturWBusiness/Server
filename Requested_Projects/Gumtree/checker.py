"""
# Algorithm 1
X= user input()

create old with content

loop wait Xs
create new file with content

new = old?
if yes pass
else play sound

del old
new rename to old
"""
# Output console is written in Polish as the requester is of Polish nationality.
from urllib import request
from filecmp import cmp
from os import remove, rename
from time import sleep

source = "https://www.gumtree.com/motorbikes-scooters/ub49lg?vehicle_engine_size=51_to_125"

retry_time = input("Sprawdzaj co ile sekund? (minimum 3s)\n> ")

def download_web(filename):
    web = request.urlopen(source)
    with open(filename + ".txt", "w") as file:
        file.close()
    with open(filename + ".txt", "a") as file:
        write = False
        for line in web.read().decode('utf-8').split("\n"):
            if '<ul class="clearfix list-listing-mini" data-q=naturalresults>' in line:
                write = True
                continue
            elif '<div class="grid-col-12 grid-col-m-7 grid-col-xl-12" role="complementary">' in line:
                write = False
                break
            if write:
                file.write(line + "\n")
            else:
                pass
        file.close()


while True:
    try:
        retry_time = int(retry_time)
    except ValueError:
        print("Prosze podaj liczbe! Na przyklad 3, 5, 10 albo 25")
        retry_time = input("Podaj liczbe jeszcze raz\n> ")
        continue
    if retry_time < 3:
        print("Podales czas ktory byl krotszy niz 3s. Ustawiam czas na 3s.")
        retry_time = 3
        break
    elif retry_time > 60:
        print("To za dlugo! Podaj czas mniejszy nisz 60s!")
        retry_time = input("> ")
    elif retry_time >= 3:
        break
    else:
        input("ERROR! Prosze zawolaj o pomoc od IT!\nKliknij ENTER aby zamknac program...")
        exit()

download_web("old")
while True:
    download_web("new")
    if cmp('new.txt', 'old.txt'):
        print("No Change found!")
    else:
        print("CHANGE!")
    remove("old.txt")
    rename("new.txt", "old.txt")
    sleep(retry_time)
