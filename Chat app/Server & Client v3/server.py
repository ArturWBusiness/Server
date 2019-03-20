#!/usr/bin/python

import socket
import _thread as thread


with open("badwords.txt", "r") as f:
    bad_words = []
    for line in f:
        bad_words.append(line.strip("\n"))


# Filters through words
def clear(msg):
    msg = msg.decode().lower()  # TODO find a way for code to understand both non and capital letter
    for word in bad_words:
        msg = msg.replace(" " + word.lower() + " ", " " + (len(word) * "*") + " ")
    return msg.encode()


def send_all(msg):
    for i in clients:
        try:
            i.send(clear(msg))
        except:
            pass


def send_this(sPriv, msg):
    sPriv.send(msg.encode())


def on_new_client(clientsocket, addr):
    global clients
    send_this(clientsocket, "fix me later")
    send_all(clientsocket.recv(1024))
    while True:
        msg = clientsocket.recv(1024)
        print(addr, msg.decode())
        send_all(msg)


# Sets up the socket and host
s = socket.socket()
host = "192.168.0.13"
port = 80


# Sets local machine as a server host
s.bind((host, port))
s.listen(10)
print('Server started!')
print('Waiting for clients...')

clients = [] # Ugly!

# TODO make it so you have a menu as an admin of the server from cmd.
# Accepts the connection
while True:
    c, addr = s.accept()
    clients.append(c)
    print('Got connection from' + addr[0] + ":" + str(addr[1]))
    # Gives a separate thread for the client.
    thread.start_new_thread(on_new_client, (c, addr))