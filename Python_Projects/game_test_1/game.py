import pygame
import os
from random import randint
from time import sleep
from pygame.locals import *

dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)


class App:
    def __init__(self):
        self._running = True
        self.screen = None
        self.size = self.weight, self.height = 1280, 720
        self.fps = input("FPS: ")
        if self.fps == "":
            self.fps = 60
        self.fps = int(self.fps)

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        if self.menu_loading != 100:
            self.load_menu()


        pygame.display.set_caption("My program")

    def on_render(self):
        self.screen.fill(self.render_background)
        pygame.display.flip()

    def on_menu_open(self):
        pygame.mixer.music.load(dir_path + "\\assets\music\menu\menu_" + str(randint(1, 1)) + ".midi")
        pygame.mixer.music.play(-1)
        self.menu_loading = 0

    def load_menu(self):
        self.menu_loading += 1
        x = self.menu_loading * 2
        self.render_background = x, x, x
        print(x)

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() is False:
            self._running = False
        self.on_menu_open()
        i = 0
        while self._running:

            sleep(1/60)
            self.current_frame = i * (self.fps / 60)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            if self.current_frame % 1 == 0:
                self.on_render()
            if i == 59:
                i = 0
            else:
                i += 1
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()