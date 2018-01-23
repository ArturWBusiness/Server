"""
[*****************************************************************]
[ I believe that if you have access to this file then I fucked up ]
[ You were never meant to get this file to be seen by your eyes!  ]
[ I believe that we will need to have a small talk... Shall we?   ]
[*****************************************************************]
"""
# TODO  : fix the no data send bug
# TODO 1: Later split it into functions.

# Default imports:
print("Loading default modules")
from time import sleep
import _thread as thread
import socket

# Custom imports:
print("Loading custom modules")
from modules.defualt_settings import socket_IP, socket_PORT
from modules.descriptions import description_help, description_user
"""
List of all processes/threads running:
Single:
* 

Per server:
* server.start_listening

Per user:
* user_incoming_data
* user_outgoing_data
* user_command
"""

'''
-============================-
|          Classes           |
-============================-
'''


class Socket:
    def __init__(self, socket_ip, socket_port):
        # Main soc set up
        print("Starting the server!")
        self.s = socket.socket()
        print("Hosted on: " + socket_ip + ":" + str(socket_port))
        self.s.bind((socket_ip, socket_port))
        print("Allowing 10 users max.")
        self.s.listen(10)
        self.user = [""]*20

    def start_listening(self):
        print("Server listener started!")
        while True:
            socket_credit, address = self.s.accept()
            i = 0
            while True:
                # Finds and empty user slot
                if self.user[i] == "":
                    # Adds to user to the server
                    self.user[i] = User(address, socket_credit)
                    break
                i += 1
            # Starts personal services for the user
            thread.start_new_thread(user_incoming_data, (i,))
            thread.start_new_thread(user_outgoing_data, (i,))
            thread.start_new_thread(user_command, (i,))

    def clear(self):
        i = -1
        for user in self.user:
            i += 1
            try:
                if user == "":
                    user.pop(i)
                    i -= 1
            except:
                pass
        while len(self.user) < 20:
            self.user.append("")

    def users(self):
        self.clear()
        temp = []
        for user in self.user:
            try:
                if user == "":
                    continue
            except:
                temp.append(user.ip())
        return temp

    def restart(self, socket_ip, socket_port, reason="Server restarting!"):
        print("W.I.P")
        pass

    def shutdown(self, reason="Shutting down!"):
        print("W.I.P (Kind off, just a kill for now)")
        exit()


# Defines the user
class User:
    def __init__(self, user_address, user_socket):
        self.user_ip, self.user_port = user_address
        self.user_socket = user_socket
        self.data_received = []
        self.data_sent = []

    # Returns IP in format 255.255.255.255:?????
    def info(self):
        return self.user_ip, str(self.user_port)

    # Sending data to the "User"
    def send(self):
        self.user_socket.send(self.data_sent[0].encode())  # Incoming
        self.data_sent.pop(0)

    # Queuing data to be sent. To prevent data collision
    def respond(self, data):
        self.data_sent.append(data)

    # Returns data packages
    def receive(self):
        try:
            temp = self.data_received[0]
            self.data_received.pop(0)
        except:
            temp = ""
        return temp

    # Receiver data packages
    def listen(self, buffer=2048):
        self.data_received.append(self.user_socket.recv(buffer).decode())  # Outgoing


'''
-============================-
|          Services          |
-============================-
'''


def server_brain():
    global server
    # Prepares the server.
    server = Socket(socket_IP, socket_PORT)
    # Server boots up the listening program.
    thread.start_new_thread(server.start_listening, ())
    # Starts the administrator management prompt in main thread
    cmd()


def cmd():
    max_args = 6  # Including the main command
    # Administrator command register
    while True:
        # Command intake
        command = input("root> ")
        try:
            # Makes the command into a (command, max_args args) style
            command = command.split(" ")
            if len(command) > max_args:
                print("Only " + str(max_args-1) + " args are allowed!")
                continue
            while len(command) != max_args:
                command.append("")
        except:
            # there is not args
            command = [command, [""]*(max_args-1)]

        # Commands TODO: ***1***
        # run_command(command) ???
        if command[0] == "help":
            if command[1] == "user":
                print(description_user)
            elif command[1] == "2":  # Number of pages in help
                print(description_help[int(command[1])-1])
            else:
                print(description_help[0])
        elif command[0] == "user":
            if command[1] == "send":
                if command[2] == "all":
                                                        # TODO: Group command[3,4,5,6...] into command[3]
                    for user in server.user:
                        try:
                            print(user.info())
                            print("Sending \"" + command[3] + "\" to " + user.info()[0] + ":" + str(user.info()[1]))
                            user.respond(command[3])
                        except:
                            pass
            elif command[1] == "list":
                print("Users connected")
                for i, user in enumerate(server.user):
                    try:
                        temp = user.info()
                        print("User " + str(i) + " with ip " + user.info()[0] + ":" + str(user.info()[1]))
                    except:
                        pass

        elif command[0] == "restart":
            new_ip = input("New IP: ")
            if new_ip == "":
                new_ip = socket_IP
                new_port = socket_PORT
            else:
                new_port = int(input("New PORT: "))
            new_reason = input("Reason for the restart: ")
            if new_reason == "":
                server.restart(new_ip, new_port)
            else:
                server.restart(new_ip, new_port, new_reason)

        elif command[0] == "shutdown":
            new_reason = input("Reason for the shutdown: ")
            server.shutdown(new_reason)
            exit()


'''
-============================-
|       User connected       |
-============================-
'''


# When command are queued it will execute them:
def user_command(i):
    user = server.user[i]
    while True:
        max_args = 6  # Including the main command
        # Command intake
        command = user.receive()
        try:
            # Makes the command into a (command, max_args args) style
            command = command.split(" ")

            while len(command) < max_args:
                command.append("")
        except:
            command = [command, [""]*(max_args-1)]
        # User commands
        # run_command_user(command) ???
        if command[0] == "login":
            if command[1] == "admin":
                user.respond("You have logged in successfully!")
        else:
            sleep(0.01)


# Takes care of data to send per user.
def user_outgoing_data(i):
    user = server.user[i]
    while True:
        # Checks if there is data to send
        if len(user.data_sent) != 0:
            # Sends queued data
            user.send()
            sleep(0.1)
        else:
            sleep(0.01)


# Grabs the data send by the user
def user_incoming_data(i):
    user = server.user[i]
    while True:
        user.listen()


# Run
print("Set up completed!")
if __name__ == "__main__":
    server_brain()
    while True:
        sleep(1)
