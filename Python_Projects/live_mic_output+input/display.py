import pyglet
import random
from time import sleep
import pyaudio
import numpy as np

RATE    = 16000
CHUNK   = 256

p = pyaudio.PyAudio()

player = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, output=True,
frames_per_buffer=CHUNK)
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)
maxx = 1000

Width = 1000
Height = 500
window = pyglet.window.Window(Width, Height)
batch = pyglet.graphics.Batch()
snow = pyglet.image.load("snow.png").texture
x_offset = 5
y_offset = 2




class Graph:
    def __init__(self):
        self.size = 256
        self.points = []
        self.objects = []

    def clear(self):
        self.points = []
        self.objects = []

    def set_size(self, size):
        self.size = size

    def generate(self):
        self.objects = []
        data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
        for x in range(0, self.size):
            y = data[x]/300
            self.objects.append(pyglet.sprite.Sprite(snow, batch=batch, x=x*x_offset, y=y*y_offset+250))

    def next_point(self):
        self.points.pop(0)
        self.objects.pop(0)
        temp_list = []
        for point in self.points:
            temp_list.append((point[0]-1, point[1]))
        for obj in self.objects:
            obj.x -= x_offset
        self.points = temp_list
        self.pointer.next_point()
        y = self.pointer.get_point()
        self.points.append((self.size-1, y))

        self.objects.append(pyglet.sprite.Sprite(snow, batch=batch, x=self.size*x_offset-x_offset, y=y*y_offset+250))

    def get_points(self):
        return self.points


class Display:
    def __init__(self):
        self.graph = Graph()
        self.color = (255, 255, 255)

    def draw(self):
        #for point in self.graph.get_points():
        #    draw_pixel(point, self.color)
        batch.draw()

    def next_graph_point(self):
        self.graph.generate()

    def new_graph(self, size):
        self.graph.clear()
        self.graph.generate()


def draw_pixel(cord=(0, 0), color=(0, 0, 0)):
    x = round(cord[0] * 5)
    y = round(cord[1]) + int(Height/2)
    pyglet.graphics.draw(1, pyglet.gl.GL_POINTS, ('v2i', (x, y)), ('c3B', (color[0], color[1], color[2])))


displayable = []
first_run = True


def update(dt):
    global first_run
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
