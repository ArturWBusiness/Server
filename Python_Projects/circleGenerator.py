from math import sqrt

window = {
    "height": 20,
    "width": 10
}


class Circle:

    def __init__(self):
        self.r = 50
        self.x = int(window["height"]/2)
        self.y = int(window["width"]/2)
        self.screen = [["."] * window["width"]] * window["height"]

    def move(self, x, y):
        self.x = x
        self.y = y
        self.draw()

    def radius(self, value):
        self.r = value
        self.draw()

    def draw(self):
        y=0
        for x in range(0, window["height"]):
            try:
                print(x, y)
                y = int(sqrt(self.r*self.r-(x+self.x)*(x+self.x)))
                self.screen[x][y+self.y] = "X"
            except ValueError:
                print("Error")
        self.render()

    def clear(self):
        self.screen = ["." * window["height"]] * window["width"]

    def render(self):
        for y in self.screen:
            temp = ""
            for x in y:
                temp += x
            print(temp)


circle = Circle()
circle.draw()
