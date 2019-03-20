#!/usr/bin/python
#
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
trash = s.recv(1024)
sleep(0.1)

# Server data listener
line21 = "#Username = " + USERNAME
line20 = ""
line19 = ""
line18 = ""
line17 = ""
line16 = ""
line15 = ""
line14 = ""
line13 = ""
line12 = ""
line11 = ""
line10 = ""
line9 = ""
line8 = ""
line7 = ""
line6 = ""
line5 = ""
line4 = ""
line3 = ""
line2 = ""
line1 = ""


def server_connection(soc):
    global line1, line2, line3, line4, line5, line6, line7, line8, line9, line10
    global line11, line12, line13, line14, line15, line16, line17, line18, line19
    global line20, line21, line22
    while True:
        data = soc.recv(1024).decode()
        print("got " + data)
        line20 = line19
        line19 = line18
        line18 = line17
        line17 = line16
        line16 = line15
        line15 = line14
        line14 = line13
        line13 = line12
        line12 = line11
        line11 = line10
        line10 = line9
        line9 = line8
        line8 = line7
        line7 = line6
        line6 = line5
        line5 = line4
        line4 = line3
        line3 = line2
        line2 = line1
        line1 = data


# Setup
# Exit button
QUIT = Button(text="QUIT", width=50, fg="red", command=quit)
QUIT.pack({"side": "bottom"})

# Send button


def counterPlus():
    if message.get() == "":
        pass
    else:
        print("sending " + message.get())
        s.send((USERNAME + "> " + message.get() + " "*100).encode())
    chatbox.delete(0, 'end')


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
        Label(text=line21).place(x=0, y=400)
        Label(text=line20).place(x=0, y=380)
        Label(text=line19).place(x=0, y=360)
        Label(text=line18).place(x=0, y=340)
        Label(text=line17).place(x=0, y=320)
        Label(text=line16).place(x=0, y=300)
        Label(text=line15).place(x=0, y=280)
        Label(text=line14).place(x=0, y=260)
        Label(text=line13).place(x=0, y=240)
        Label(text=line12).place(x=0, y=220)
        Label(text=line11).place(x=0, y=200)
        Label(text=line10).place(x=0, y=180)
        Label(text=line9).place(x=0, y=160)
        Label(text=line8).place(x=0, y=140)
        Label(text=line7).place(x=0, y=120)
        Label(text=line6).place(x=0, y=100)
        Label(text=line5).place(x=0, y=80)
        Label(text=line4).place(x=0, y=60)
        Label(text=line3).place(x=0, y=40)
        Label(text=line2).place(x=0, y=20)
        Label(text=line1).place(x=0, y=0)


# Run
thread.start_new_thread(server_connection, (s, ))
thread.start_new_thread(update, (s, ))
app.mainloop()
root.destroy()
