import pyglet
import random
from time import sleep

Width = 1000
Height = 200
window = pyglet.window.Window(Width, Height)


class Pointer:
    def __init__(self):
        self.acceleration = 0.0
        self.velocity = 0.0
        self.height = 0.0

    def __next_acceleration(self):
        movement = 0
        if self.velocity <= -5.0:
            self.acceleration = self.acceleration*0.5 + 1
        if self.velocity >= 5.0:
            self.acceleration = self.acceleration*0.5 - 1
        if self.height <= -10.0:
            movement = random.random()*2      # Rand  0 to 2
        elif self.height >= 10:
            movement = random.random()*2 - 2  # Rand -2 to 0
        else:
            movement = random.random()*2 - 1  # Rand -1 to 1

        if self.acceleration >= 2 and movement >= 0:
            movement = 0
        elif self.acceleration <= -2 and movement <= 0:
            movement = 0
        self.acceleration += movement

    def __next_velocity(self):
        self.velocity += self.acceleration

    def __next_height(self):
        self.height += self.velocity

    def next_point(self):
        self.__next_acceleration()
        self.__next_velocity()
        self.__next_height()

    def get_point(self):
        return self.height


class Graph:
    def __init__(self):
        self.size = 50
        self.points = []
        self.pointer = Pointer()

    def clear(self):
        self.points = []

    def set_size(self, size):
        self.size = size

    def generate(self):
        for x in range(0, self.size):
            self.pointer.next_point()
            y = self.pointer.get_point()
            self.points.append((x, y))

    def next_point(self):
        self.points.pop(0)
        temp_list = []
        for point in self.points:
            temp_list.append((point[0]-1, point[1]))
        self.points = temp_list
        self.pointer.next_point()
        y = self.pointer.get_point()
        self.points.append((self.size-1, y))

    def get_points(self):
        return self.points


class Display:
    def __init__(self):
        self.graph = Graph()
        self.color = (255, 255, 255)

    def draw(self):
        for point in self.graph.get_points():
            draw_pixel(point, self.color)

    def next_graph_point(self):
        self.graph.next_point()

    def new_graph(self, size):
        self.graph.clear()
        self.graph.set_size(size)
        self.graph.generate()


def draw_pixel(cord=(0, 0), color=(0, 0, 0)):
    x = round(cord[0] * 5)
    y = round(cord[1]) + int(Height/2)
    pyglet.graphics.draw(1, pyglet.gl.GL_POINTS, ('v2i', (x, y)), ('c3B', (color[0], color[1], color[2])))


displayable = []
first_run = True


def update(dt):
    global first_run
    sleep(1/60)
    if first_run:
        display = Display()
        display.new_graph(200)
        displayable.append(display)
        first_run = False
    if len(displayable) != 0:
        for item in displayable:
            item.next_graph_point()
    on_draw()


def on_draw():
    window.clear()
    if len(displayable) != 0:
        for item in displayable:
            item.draw()


pyglet.clock.schedule_interval(update, 1/120)
pyglet.app.run()
