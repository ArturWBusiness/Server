from utils import Server
from time import sleep
from _thread import start_new_thread
from _thread import exit_thread
# server = Server()
#
# server.set_server_ip("0.0.0.0")


def wait(x):
    for y in range(x):
        sleep(1)
        print(y)
        exit_thread()


x = start_new_thread(wait, (300,))
print(x)
del x
while True:
    pass