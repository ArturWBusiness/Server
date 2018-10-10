from pyglet.gl import *
from pyglet.window import key
import math
'''
This application is made from a tutorial
https://www.youtube.com/watch?v=Hqg4qePJV2U
Will be continues later on.
'''


class Model:

    def get_tex(self, file):
        tex = pyglet.image.load(file).texture
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        return pyglet.graphics.TextureGroup(tex)

    def __init__(self):

        self.top = self.get_tex("grass_top.png")
        self.side = self.get_tex("grass_side.png")
        self.bottom = self.get_tex("dirt.png")

        self.batch = pyglet.graphics.Batch()

        tex_coords = ("t2f", (0,0, 1,0, 1,1, 0,1, ))

        x, y, z = 0, 0, 0
        X, Y, Z = x+1, y+1, z+1

        self.batch.add(4, GL_QUADS, self.side, ("v3f", (x,y,z, X,y,z, X,Y,z, x,Y,z, )), tex_coords)

    def draw(self):
        self.batch.draw()


class Player:
    def __init__(self):
        self.pos = [0, 0, 0]
        self.rot = [0, 0]

    def update(self, dt, keys):
        s = dt*10
        rotY = self.rot[1]/180*math.pi
        dx, dz = math.sin(rotY), math.cos(rotY)
        if keys[key.W]: self.pos[0] += dx; self.pos[2] -= dz
        if keys[key.S]: self.pos[0] -= dx; self.pos[2] += dz
        if keys[key.A]: self.pos[0] -= dx; self.pos[2] -= dz
        if keys[key.D]: self.pos[0] += dx; self.pos[2] += dz

        if keys[key.SPACE]: self.pos[1] +=s
        if keys[key.LSHIFT]: self.pos[1] -=s

class Window(pyglet.window.Window):

    def Projection(self): glMatrixMode(GL_PROJECTION); glLoadIdentity()
    def Model(self): glMatrixMode(GL_PROJECTION); glLoadIdentity()
    def set2d(self): self.Projection(); gluOrtho2D(0, self.width/self.heigh, 0.05, 1000); self.Model();
    def set3d(self): self.Projection(); gluPerspective(70, self.width/self.height, 0.05, 1000); self.Model();

    def setLock(self, state): self.lock = state; self.set_exclusive_mouse(state)
    lock = False; mouse_lock = property(lambda self:self.lock, setLock)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        pyglet.clock.schedule(self.update)

        self.model = Model()
        self.player = Player()

    def on_key_press(self, KEY, MOD):
        if KEY == key.ESCAPE: self.close()
        elif KEY == key.E: self.mouse_lock = not self.mouse_lock

    def update(self, dt):
        self.player.update(dt, self.keys)

    def on_draw(self):
        self.clear()
        self.set3d()
        # glRotatef(-30, 1, 0, 0)
        x, y, z = self.player.pos
        glTranslatef(-x, -y, -z)
        self.model.draw()


if __name__ == "__main__":
    window = Window(width=1280, height=720, caption="Application v1.0")
    glClearColor(0.5, 0.7, 1, 1)
    pyglet.app.run()

