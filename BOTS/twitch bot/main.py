# The only import you need!
import socket

with open("settings.txt", "r") as f:
    for line in f:
        # if line.startswith(""):
        #     line = line.strip("").strip("\n")
        #     x = line
        #     continue
        if line.startswith("#") or line == "\n":
            continue
        if line.startswith("discord_link="):
            line = line.strip("discord_link=").strip("\n")
            discord_link = line
            continue
        if line.startswith("PASS="):
            line = line.strip("PASS=").strip("\n")
            PASS = line
            continue
        if line.startswith("BOT="):
            line = line.strip("BOT=").strip("\n")
            BOT = line
            continue
        if line.startswith("CHANNEL="):
            line = line.strip("CHANNEL=").strip("\n")
            CHANNEL = line
            continue
        if line.startswith("OWNER="):
            line = line.strip("OWNER=").strip("\n")
            OWNER = line
            continue
        if line.startswith("SERVER="):
            line = line.strip("SERVER").strip("\n")
            SERVER, PORT = line.strip(",")
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
    sendMessage(s, "Chat room joined!")
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
                sendMessage(s, "Understand! Leaving the chat room!")
                exit()
            #if message.startswith("!private"):
            #    sendMessage(s, PMSG + "This is a private message send to the user")
            #    break
            if message.startswith("!discord"):
                sendMessage(s, "You can join our group discord here " + discord_link)
                break

############################################################################