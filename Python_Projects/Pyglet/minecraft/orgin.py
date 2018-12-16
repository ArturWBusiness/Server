from pyglet.gl import *
from pyglet.window import key
import math
import time

class Grass:

    def get_tex(self,file):
        tex = pyglet.image.load(file).texture
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        return pyglet.graphics.TextureGroup(tex)

    def __init__(self, x, y, z):

        self.top = self.get_tex('grass_top.png')
        self.side = self.get_tex('grass_side.png')
        self.bottom = self.get_tex('dirt.png')

        self.batch = pyglet.graphics.Batch()

        tex_cords = ('t2f',(0,0, 1,0, 1,1, 0,1, ))
        size = 1
        X,Y,Z = x+size,y+size,z+size

        #self.batch.add(4,GL_QUADS,self.side,('v3f',(x,y,z, x,y,Z, x,Y,Z, x,Y,z, )),tex_cords)
        #self.batch.add(4,GL_QUADS,self.side,('v3f',(X,y,Z, X,y,z, X,Y,z, X,Y,Z, )),tex_cords)
        #self.batch.add(4,GL_QUADS,self.bottom,('v3f',(x,y,z, X,y,z, X,y,Z, x,y,Z, )),tex_cords)
        self.batch.add(4,GL_QUADS,self.top,('v3f',(x,Y,Z, X,Y,Z, X,Y,z, x,Y,z, )),tex_cords)
        #self.batch.add(4,GL_QUADS,self.side,('v3f',(X,y,z, x,y,z, x,Y,z, X,Y,z, )),tex_cords)
        #self.batch.add(4,GL_QUADS,self.side,('v3f',(x,y,Z, X,y,Z, X,Y,Z, x,Y,Z, )),tex_cords)


    def draw(self): self.batch.draw()
    def btype(self):return 1

class Air:
    def __init__(self): pass
    def draw(self): pass
    def btype(self): return 0

class World:
    def __init__(self):
        self.chunk = []

    def load(self):
        with open("flat-chunk-0-0", "r") as f:
            y_line = []
            for y, y_layer in enumerate(f):
                y_layer = y_layer.strip("\n")
                x_line = []
                for x, x_layer in enumerate(y_layer.split("*")):
                    z_line = []
                    for z, block in enumerate(x_layer.split(",")):
                        if block == "1":
                            z_line.append(Grass(z, y, x))
                        else:
                            z_line.append(Air())
                    x_line.append(z_line)
                y_line.append(x_line)
            self.chunk = y_line
        self.update(0,0)

    def render(self):
        #time.sleep(0)
        for y, y_layer in enumerate(self.chunk):
            for x, x_layer in enumerate(y_layer):
                for z, block in enumerate(x_layer):
                    self.chunk[y][x][z].draw()

    def update(self, chunk_x=0, chunk_z=0):
        pass

    def check_block(self, check_x , check_z, check_y):
        if check_x<0:
            check_x-=1.0
        if check_z<0:
            check_z-=1.0
        check_x, check_z = int(check_x), int(check_z)
        for y, y_layer in enumerate(self.chunk):
            for x, x_layer in enumerate(y_layer):
                for z, block in enumerate(x_layer):
                    if x == check_x and z == check_z and y == check_y:
                        if block.btype() == 1:
                            print(z, x , "Standing!")
                            return True
                        elif block.btype() == 0:
                            print(z, x , "Floating!")
                            return False
                        else:
                            print("ERROR NO BLOCK")
                            return True
class Player:
    def __init__(self, import_world, pos=(0,0,0),rot=(0,0) ):
        self.pos = list(pos)
        self.rot = list(rot)
        self.world = import_world
        self.velocity = 0
        self.holding = False
        self.boost = 1

    def mouse_motion(self,dx,dy):
        dx/=8; dy/=8; self.rot[0]+=dy; self.rot[1]-=dx
        if self.rot[0]>90: self.rot[0] = 90
        elif self.rot[0]<-90: self.rot[0] = -90

    def update(self,dt,keys):
        #print(int(self.pos[0]),int(self.pos[2]),int(self.pos[1]))
        s = dt*5
        #print(s)
        gravity = 0.1
        if self.world.check_block(self.pos[2],self.pos[0],int(self.pos[1])-2):
            self.velocity = 0
        else:
            self.velocity -= gravity
        rotY = -self.rot[1]/180*math.pi
        dx,dz = s*math.sin(rotY),s*math.cos(rotY)
        if keys[key.R]: self.boost = 1.75
        else: self.boost = 1
        if keys[key.W]: self.pos[0]+=dx*self.boost; self.pos[2]-=dz*self.boost
        if keys[key.S]: self.pos[0]-=dx*self.boost; self.pos[2]+=dz*self.boost
        if keys[key.A]: self.pos[0]-=dz*self.boost; self.pos[2]-=dx*self.boost
        if keys[key.D]: self.pos[0]+=dz*self.boost; self.pos[2]+=dx*self.boost

        if keys[key.SPACE]:
            if self.world.check_block(int(self.pos[2]), int(self.pos[0]), int(self.pos[1]) - 2):
                self.velocity = 2
        if keys[key.LSHIFT]: self.pos[0]=0.5;self.pos[2]=0.5;self.pos[1]=10;self.velocity=1

        self.pos[1] += s*self.velocity

class Window(pyglet.window.Window):

    def push(self,pos,rot): glPushMatrix(); glRotatef(-rot[0],1,0,0); glRotatef(-rot[1],0,1,0); glTranslatef(-pos[0],-pos[1],-pos[2],)
    def Projection(self): glMatrixMode(GL_PROJECTION); glLoadIdentity()
    def Model(self): glMatrixMode(GL_MODELVIEW); glLoadIdentity()
    def set2d(self): self.Projection(); gluOrtho2D(0,self.width,0,self.height); self.Model()
    def set3d(self): self.Projection(); gluPerspective(70,self.width/self.height,0.05,1000); self.Model()

    def setLock(self,state): self.lock = state; self.set_exclusive_mouse(state)
    lock = False; mouse_lock = property(lambda self:self.lock,setLock)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.set_minimum_size(300,200)
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        pyglet.clock.schedule(self.update)
        self.world = World()
        self.world.load()
        #self.model = Grass(0, 0, -1)
        self.player = Player(self.world, (5.5,10,5.5),(-30,0))

    def on_mouse_motion(self,x,y,dx,dy):
        if self.mouse_lock: self.player.mouse_motion(dx,dy)

    def on_key_press(self,KEY,MOD):
        if KEY == key.ESCAPE: self.close()
        elif KEY == key.E: self.mouse_lock = not self.mouse_lock

    def update(self,dt):
        self.player.update(dt,self.keys)

    def on_draw(self):
        self.clear()
        self.set3d()
        self.push(self.player.pos,self.player.rot)
        self.world.render()
        #self.model.draw()
        glPopMatrix()


if __name__ == '__main__':
    window = Window(width=854,height=480,caption='Minecraft',resizable=True)
    glClearColor(0.5,0.7,1,1)
    #glEnable(GL_DEPTH_TEST)
    #glEnable(GL_CULL_FACE)
    pyglet.app.run()



