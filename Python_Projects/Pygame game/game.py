# PyGame template.

# Import standard modules.
import sys
import time
# Import non-standard modules.
import pygame
from pygame.locals import *


class MouseSprite:
    def __init__(self):
        self.size = 20
        self.color = (0, 0, 0)

    def grow(self, speed):
        if self.size < 100:
            self.size = self.size + speed
            self.color = ((self.size*2.5), (self.size*2.5), (self.size*2.5))

    def shrink(self, speed):
        if self.size > 1:
            self.size = self.size - speed
            self.color = ((self.size*2.5), (self.size*2.5), (self.size*2.5))

    def change_color(self, args):
        self.color = args

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, pygame.mouse.get_pos(), self.size)


key_pressed = None


def update():
    global key_pressed
    """
    Update game. Called once per frame.
    dt is the amount of time passed since last frame.
    If you want to have constant apparent movement no matter your framerate,
    what you can do is something like

    x += v * dt

    and this will scale your velocity based on time. Extend as necessary."""

    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        print("event")
        # We need to handle these events. Initially the only one you'll want to care
        # about is the QUIT event, because if you don't handle it, your game will crash
        # whenever someone tries to exit.
        if event.type == QUIT:
            pygame.quit()  # Opposite of pygame.init
            sys.exit()  # Not including this line crashes the script on Windows. Possibly
            # on other operating systems too, but I don't know for sure.

        # Key Clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            key_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            key_pressed = False
        # Key Hold
    if key_pressed:
        mouseSprite.grow(2)
    elif not key_pressed:
        mouseSprite.shrink(4)


def draw(screen):
    """
    Draw things to the window. Called once per frame.
    """
    screen.fill((0, 0, 0))  # Fill the screen with black.
    mouseSprite.draw(screen)
    # Redraw screen here.

    # Flip the display so that the things we drew actually show up.
    pygame.display.flip()


def runPyGame():
    # Class globalization
    global mouseSprite

    # Initialise PyGame.
    pygame.init()

    # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
    fps = 60
    fpsClock = pygame.time.Clock()

    # Set up the window.
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))

    # screen is the surface representing the window.
    # PyGame surfaces can be thought of as screen sections that you can draw onto.
    # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.

    # Main game loop.
    dt = 1 / fps  # dt is the time since last frame.

    # Object creation
    mouseSprite = MouseSprite()
    x = 0
    while True:  # Loop forever!
        # You can update/draw here, I've just moved the code for neatness.
        if (x%60) == 0:
            print(x/60)
        x = x + 1
        update()
        draw(screen)
        dt = fpsClock.tick(fps)


if __name__ == "__main__":
    runPyGame()