# PyGame template.

import sys
import socket

import pygame
from pygame.locals import *

connection = socket.socket()
connection.connect(("localhost", 24680))
#username = input("Username> ")
#password = input("Password> ")
#connection.send(("LOGIN " + username + " " + password).encode())

connection.send(("LOGIN Eis3 family10").encode())
class Player:

    def __init__(self):
        self.name = "Defualt"
        self.size = 10

    def expand(self):
        pass

    def shrink(self):
        pass

    def draw(self):
        pass


def update():

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()


def draw(screen):

    screen.fill((0, 0, 0))

    pygame.display.flip()


def runPyGame():

    pygame.init()

    fps = 60.0
    fpsClock = pygame.time.Clock()

    # Set up the window.
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))

    dt = 1 / fps
    while True:
        update()
        draw(screen)

        dt = fpsClock.tick(fps)
