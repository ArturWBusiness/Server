from random import randint
class World:
    def __init__(self):
        self.world = []
        self.world_size = 0, 0
        # x5
        """ 
        
        [0,0,0,1,1] <-- world[0][3] = 0
        [0,0,1,1,1]
        [0,1,1,1,0]
        [0,0,0,1,0]
        [0,0,0,0,0]
        """

    def new(self, max_x, max_y, land_percentage):
        max_y = int(max_y)
        max_x = int(max_x)
        land_percentage = float(land_percentage)
        self.world_size = max_x, max_y
        x, y = 0, 0
        row = []
        while x <= max_x:
            while y <= max_y:
                if randint(0, 1) < land_percentage:
                    row.append("X")
                else:
                    row.append(" ")
                y += 1
            self.world.append(row)
            row = []
            x += 1
            y = 0

    def get_block(self, x=0, y=0):
        block = self.world[x][y]

    def get_world(self):
        return self.world


world = World()

# world.new(input("max_Y> "), input("max_X> "), input("land 0.XX %> "))
world.new(35,120,0.8)
for x in world.get_world():
    render = ""
    for block in x:
        if block == "X":
            render += "X"
        else:
            render += " "
    print(render)