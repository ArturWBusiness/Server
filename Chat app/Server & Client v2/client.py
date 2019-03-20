#!/usr/bin/python

import socket
from tkinter import*
import _thread as thread
from time import sleep
USERNAME = str(input("Input your username: "))

# Sets up the app
root = Tk()
root.title("Chat server")
root.geometry("310x500")
app = Frame(root)

# Server connection
s = socket.socket()
host = "192.168.0.2"  # input("IP: ")
port = 46821  # input("Password: ")
s.connect((host, port))
s.send((USERNAME + " has joined!" + " "*100).encode())

# My messy code that I have to fix.
trash = s.recv(1024)
sleep(0.1)

# Sets up all the lines for display
line = [None]*21
line[len(line)-1] = "#Username = " + USERNAME


# This is a separate thread that handles incoming data.
def server_connection(soc):
    global line
    while True:
        data = soc.recv(1024).decode()
        print("got " + data)
        # moves all the data down
        x = 0
        while x != len(line)-2:  # increase the line by 1 to get ride of the USERNAME
            line[len(line)-2-x] = line[len(line)-3-x]
            x += 1
        line[0] = data


# Setup
# Exit button
QUIT = Button(text="QUIT", width=50, fg="red", command=quit)
QUIT.pack({"side": "bottom"})


def counterPlus():
    if message.get() == "":
        pass
    else:
        print("sending " + message.get())
        s.send((USERNAME + "> " + message.get() + " "*100).encode())
    chatbox.delete(0, 'end')


# Send button
send = Button(text="Send message", width=50, command=counterPlus)
send.pack({"side": "bottom"})

# Chat box input
message = StringVar()
chatbox = Entry(width=50, textvariable=message)
chatbox.pack({"side": "bottom"})

# Chat


def update(soc):
    while True:
        sleep(0.25)
        x = 0
        while x != len(line):
            Label(text=line[x]).place(x=0, y=x*20)
            x += 1


# Run
thread.start_new_thread(server_connection, (s, ))
thread.start_new_thread(update, (s, ))
app.mainloop()
root.destroy()
