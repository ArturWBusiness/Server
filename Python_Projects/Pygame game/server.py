from _thread import start_new_thread
from _thread import exit_thread
import socket

# Socket set up

SERVER_IP, SERVER_PORT = "localhost", 64590
server = socket.socket()
server.bind((SERVER_IP, SERVER_PORT))
server.listen(10)


class Users:
    def __init__(self):
        self.users = ()

    def load(self):
        with open("database.txt", "r") as f:
            for line in f:
                try:
                    line = line.split("{")[1].split("}")[0]
                    user_id, username, password = line.split(",")
                    self.users.append((user_id, username, password))
                except:
                    pass

    def password(self, username):
        pass


class Player:

    def __init__(self):
        self.id = 0
        self.name = "Defualt"
        self.size = 10
        self.position = (0, 0)


def connectionAuthorise(soc, address):

    # Request format "LOGIN [USERNAME] [PASSWORD]"
    print("USER> Requesting a login")
    soc.send("DATA.REQUEST LOGIN".encode())
    respond = soc.recv(1024).decode()
    print("USER> Package Received")
    try:
        username = respond.split(" ")[1]
        password = respond.split(" ")[2]
        if users.password(username) == password:
            print("Logging in...")
            start_new_thread(connectionListener, (soc, address))
            start_new_thread(connectionSender, (soc, address))
            start_new_thread(connectionBrain, (soc, address))
    except:
        pass
    exit_thread()
    print("test?")


def connectionHandler(uinput):
    global users
    if str(uinput) != "yes":
        exit()

    # Loading users
    users = Users()
    users.load()

    while True:
        print("Server> Waiting for a connection")
        soc, address = server.accept()
        print("Server> Testing a captured connection!")
        start_new_thread(connectionAuthorise, (soc, address))


if __name__ == "__main__":
    connectionHandler("yes")  # input("This file needs permission to run!\nRun? "))
