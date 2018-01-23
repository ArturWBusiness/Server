"""
Connect to the secret
"""
import socket
from time import sleep
import _thread as thread
from os import system

message = ""
address = ["localhost", 46821]

def sending():
    while True:
        cmd = input("@Turtle>")
        try:
            s.send(cmd.encode())
        except:
            pass


def brain():
    global message
    while True:
        if message == "":
            sleep(0.03)
        else:
            print("Got: " + message)
            message = ""


def receiver():
    global message
    while True:
        try:
            message = (s.recv(1024)).decode()
        except NameError:
            reconnect()
        except ConnectionResetError:
            reconnect()


def reconnect():
    global s
    system("color 4")
    print("Lost connection with the server")
    try:
        s.shutdown(socket.SHUT_RDWR)
    except NameError:
        pass
    while True:
        try:
            s = socket.socket()
            s.connect(address)
            system("color f")
            print("Connected!")
            break
        except ConnectionRefusedError:
            print("Connecting...")
            sleep(3)

thread.start_new_thread(receiver, ())
thread.start_new_thread(brain, ())
sending()
