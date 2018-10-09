from pyglet.gl import *

'''
This application is made from a tutorial
https://www.youtube.com/watch?v=Hqg4qePJV2U
Will be continues later on.
'''


class Model:
    def __init__(self):
        self.batch = pyglet.graphics.Batch()

        color = ("c3f", (1, 1, 1,)*4)

        x, y, z = 0, 0, 0
        X, Y, Z = x+1, y+1, z+1

        self.batch.add(4, GL_QUADS, None, ("v3f", (x, y, z, X, y, z, X, Y, z, x, Y, z, )), color)

    def draw(self):
        self.batch.draw()


class Window(pyglet.window.Window):

    def Projection(self): glMatrixMode(GL_PROJECTION); glLoadIdentity()

    def Model(self): glMatrixMode(GL_PROJECTION); glLoadIdentity()

    def set3d(self):
        self.Projection()
        # perspective
        self.Model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.model = Model()

    def on_draw(self):
        self.clear()
        self.set3d()
        self.model.draw()


if __name__ == "__main__":
    window = Window(width=1280, height=720, caption="Application v1.0")
    glClearColor(0.5, 0.7, 1, 1)
    pyglet.app.run()

