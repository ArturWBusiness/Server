# The only import you need!
import socket
import _thread as thread
import urllib.request
from time import sleep

BOT = "eis3bot"
CHANNEL = "eis3twitch"
OWNER = "eis3twitch"
SERVER, PORT = "irc.twitch.tv", 6667

with open("settings.txt", "r") as f:
    for line in f:
        # if line.startswith(""):
        #     line = line.strip("").strip("\n")
        #     x = line
        #     continue
        if line.startswith("#") or line == "\n":
            continue
        if line.startswith("PASS="):
            line = line.strip("PASS=").strip("\n")
            PASS = line
            continue
# Functions


def sendMessage(s, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send((messageTemp + "\r\n").encode())


def getUser(line):
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user


def getMessage(line):
    global message
    try:
        message = (line.split(":", 2))[2]
    except:
        message = ""
    return message


def join_chat():
    readbuffer_join = "".encode()
    Loading = True
    while Loading:
        readbuffer_join = s.recv(1024)
        readbuffer_join = readbuffer_join.decode()
        temp = readbuffer_join.split("\n")
        readbuffer_join = readbuffer_join.encode()
        readbuffer_join = temp.pop()
        for line in temp:
            Loading = loading_completed(line)
    # sendMessage(s, "Chat room joined!")
    print("Bot has joined " + CHANNEL + " Channel!")


def loading_completed(line):
    if ("End of /NAMES list" in line):
        return False
    else:
        return True
### Code runs
s_prep = socket.socket()
s_prep.connect((SERVER, PORT))
s_prep.send(("PASS " + PASS + "\r\n").encode())
s_prep.send(("NICK " + BOT + "\r\n").encode())
s_prep.send(("JOIN #" + CHANNEL + "\r\n").encode())
s = s_prep
join_chat()
readbuffer = ""


def Console(line):
    # gets if it is a user or twitch server
    if "PRIVMSG" in line:
        return False
    else:
        return True


class Bank:
    def __init__(self, file):
        global users_gold
        users_gold = []
        with open(file, "r+") as f:
            for line in f.readlines():
                if line == "" or line == "\n":
                    continue
                line = line.strip("\n")
                user, points = line.split("=")
                users_gold.append((user, points))


def gold_give(user, amount):
    worked=False
    global users_gold
    for index, item in enumerate(users_gold):
        itemlist = list(item)
        if itemlist[0] == user:
            itemlist[1] = int(itemlist[1]) + int(amount)
            worked=True
        item = tuple(itemlist)
        users_gold[index] = item

def gold_give_admin(user, amount):
    worked=False
    global users_gold
    for index, item in enumerate(users_gold):
        itemlist = list(item)
        if itemlist[0] == user:
            itemlist[1] = int(itemlist[1]) + int(amount)
            worked=True
        item = tuple(itemlist)
        users_gold[index] = item
    if not worked:
        sendMessage(s, "User not found")
    else:
        sendMessage(s, str(amount) + " gold given to " + user)

def gold_giver():
    global users_gold
    while True:
        print("waiting")
        sleep(60)
        content = urllib.request.FancyURLopener({}).open("https://tmi.twitch.tv/group/user/eis3twitch/chatters").read().decode()
        temp = content.split('"moderators": [\n')[1].split('\n    ],\n    "staff": [],')[0]
        users_list_mods = temp.replace(" ", "").replace('"', "").replace("\n", "").split(",")
        temp = content.split('"viewers": [\n')[1].split('\n    ]\n  }\n}')[0]
        users_list_users = temp.replace(" ", "").replace('"', "").replace("\n", "").split(",")
        user_list = users_list_mods + users_list_users
        print(user_list)
        user_to_add = []
        for user in user_list:
            x = 0
            userfound = False
            for registered_user in users_gold:
                if registered_user[0] == user:
                    gold_give(user, 1)
                    userfound = True
                x = x + 1
            if not userfound:
                user_to_add.append(user)
        with open("users_gold.txt", "a") as f:
            for user in user_to_add:
                users_gold.append((user, 0))
                f.write(user + "=0\n")
                print(users_gold)


def get_gold(target_user):
    for data in users_gold:
        if data[0] == target_user:
            sendMessage(s, target_user + " has " + str(data[1]) + " gold")
            break

bank = Bank("users_gold.txt")
thread.start_new_thread(gold_giver, ())
print("print going on")
while True:
        try:
            readbuffer = s.recv(1024)
            readbuffer = readbuffer.decode()
            temp = readbuffer.split("\n")
            readbuffer = readbuffer.encode()
            readbuffer = temp.pop()
        except:
            temp = ""
        for line in temp:
            if line == "":
                break
            # So twitch doesn't timeout the bot.
            if "PING" in line and Console(line):
                msgg = "PONG tmi.twitch.tv\r\n".encode()
                s.send(msgg)
                print(msgg)
                break
            # get user
            user = getUser(line)
            # get message send by user
            message = getMessage(line)
            # for you to see the chat from CMD
            print(user + " > " + message)
            # sends private msg to the user (start line)
            PMSG = "/w " + user + " "

################################# Command ##################################
############ Here you can add as meny commands as you wish of ! ############
############################################################################

            if user == OWNER and "!stop" in message:
                sendMessage(s, "Saving before closing...")
                f = open("users_gold.txt", "w")
                f.close()
                with open("users_gold.txt", "a") as f:
                    for user in users_gold:
                        f.write(str(user[0]) + "=" + str(user[1] + "\n"))
                print(users_gold)
                exit()


            if user == OWNER and message.startswith("!give"):
                #if message.split(" ")[1] == "all":
                gold_give_admin(message.split(" ")[1], message.split(" ")[2])
            #if message.startswith("!private"):
            #    sendMessage(s, PMSG + "This is a private message send to the user")
            #    break
            if message.startswith("!gold"):
                thread.start_new_thread(get_gold, (user,))
                break

############################################################################