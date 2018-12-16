import pyglet
import random

Width = 1024
Height = 720
window = pyglet.window.Window(Width, Height)

density = int(input("Amount of snow created per tick:  (Recommended 1-3)\n> "))

snow_particles = []

def create_snow(amount=1):
    for i in range(0, amount):
        particleX = random.randint(-50, Width + 50)
        particleY = Height + 100
        velocityY = random.randint(0, 10)
        velocityX = random.randint(-3, 3)
        snow_particle_object = pyglet.sprite.Sprite(img=pyglet.resource.image("snow.png"), x=particleX, y=particleY)

        snow_particles.append(
            [
                snow_particle_object,  # particleX, y=particleY),
                (particleX, particleY),
                (velocityX, velocityY)
            ]
        )


xxx = 0
def update(dt):
    global xxx
    if xxx % 10:
        create_snow(density)
        # snow_particle.update(y=random.randint(0, Height), x=random.randint(0, Width))
    xxx += 1
    back = 0
    while "Delete" in snow_particles:
        snow_particles.remove("Delete")
    on_draw()



def on_draw():
    window.clear()
    #print(snow_particles)
    for i, data in enumerate(snow_particles):
        if data[1][1] < -50:
            snow_particles[i] = "Delete"
            continue
        velocityY = data[2][1] + random.randint(-1, 1)
        velocityX = data[2][0] + random.randint(-1, 1)
        if velocityX < -3:
            velocityX = -3
        if velocityX > 3:
            velocityX = 3
        if velocityY < 1:
            velocityY = 1
        if velocityY > 10:
            velocityY = 10
        new_y = data[1][1] - velocityY
        new_x = data[1][0] - velocityX
        snow_particles[i][0].update(x=new_x, y=new_y)
        snow_particles[i][1] = (new_x, new_y)
        snow_particles[i][2] = (velocityX, velocityY)
        snow_particles[i][0].draw()
        # print("Particle at ", new_y, data[1])

    print("Objects: " + str(len(snow_particles)))

pyglet.clock.schedule_interval(update, 1/120)
pyglet.app.run()
"""


1 2 5 6 7


"""