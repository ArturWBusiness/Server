#!/usr/bin/python

import socket
import _thread as thread


def send_all(msg):
    for i in clients:
        try:
            i.send(msg)
        except:
            pass


def send_this(s, msg):
    s.send(msg.encode())


def on_new_client(clientsocket, addr):
    global clients
    send_this(clientsocket, "fix me later")
    send_all(clientsocket.recv(1024))
    while True:
        msg = clientsocket.recv(1024)
        print(addr, msg.decode())
        send_all(msg)
    clientsocket.close()


s = socket.socket()
host = "192.168.0.2"
port = 46821

print('Server started!')
print('Waiting for clients...')

s.bind((host, port))
s.listen(10)

clients = []
while True:
    c, addr = s.accept()
    clients.append(c)
    print('Got connection from', addr)
    thread.start_new_thread(on_new_client, (c, addr))