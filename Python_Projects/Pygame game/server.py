from _thread import start_new_thread
from _thread import exit_thread
import socket

# Socket set up

SERVER_IP, SERVER_PORT = "localhost", 24680
server = socket.socket()
server.bind((SERVER_IP, SERVER_PORT))
server.listen(10)


class Users:
    def __init__(self):
        self.users = []

    def load(self):
        with open("database.txt", "r") as f:
            for line in f:
                line = line.split("{")[1].split("}")[0]
                user_id, username, password = line.split(",")
                self.users.append((user_id, username, password))
    def password(self, username):
        print(self.users)
        for user in self.users:
            print("Testing " + user[1] + " on " + username)
            if username == user[1]:
                print(user[2])
                return user[2]


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
    print("USER> Package Received (" + respond + ")")

    username = respond.split(" ")[1]
    password = respond.split(" ")[2]
    print("USER> Logged in with " + username + " " + password)
    if users.password(username) == password:
        print("Logging in...")
        start_new_thread(connectionListener, (soc, address))
        start_new_thread(connectionSender, (soc, address))
        start_new_thread(connectionBrain, (soc, address))

    print("Closing")
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
