import os
import time
from termcolor import colored
import math 


class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsWall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x or round(point[1]) < 0 or round(point[1]) >= self._y

    def setPos(self, pos, mark):
        self._canvas[round(pos[0])][round(pos[1])] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.05
        self.pos = [0, 0]

        self.direction = [0, 1]
        self.color = "grey"

    def setDegrees(self, degrees):
        radians = (degrees/180) * math.pi 
        self.direction = [math.sin(radians), -math.cos(radians)]

    def up(self):
        self.direction = [0, -1]
        self.forward()

    def down(self):
        self.direction = [0, 1]
        self.forward()

    def right(self):
        self.direction = [1, 0]
        self.forward()

    def left(self):
        self.direction = [-1, 0]
        self.forward()

    def forward(self):
        pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def drawSquare(self, size):
        for i in range(size):
            self.right()
        for i in range(size):
            self.down()
        for i in range(size):
            self.left()
        for i in range(size):
            self.up()

    def draw(self, pos):
        # self.canvas.setPos(self.pos, colored(self.trail, 'magenta'))
        # self.pos = pos
        # self.canvas.setPos(self.pos, colored(self.mark, self.color))
        self.canvas.setPos(self.pos, colored(self.trail, self.color))
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, 'magenta'))
        self.canvas.print()
        time.sleep(self.framerate)

    def drawScribe(self, dict):
        self.color = dict['color']
        self.pos = dict['position']
        self.setDegrees(dict['degrees'])
        self.framerate = dict['framerate']
        print(f"name: {dict['name']}")
        print(f"color: {self.color}")
        print(f"pos: {self.pos}")
        print(f"degrees: {dict['degrees']}")
        print(f"direction: {self.direction}")
        print(f"framerate: {self.framerate}")
        for i in range(60):
            scribe.forward()


canvas = Canvas(31, 31)
scribe = TerminalScribe(canvas)
# scribe.setDegrees(135)
# for i in range(30):
#     scribe.forward()


scribes_dict = {
    "red": {
        "name": "red",
        "color": "red",
        "position": [0,0],
        "degrees": 135,
        "framerate": 0.05,
    },
    "blue": {
        "name": "blue",
        "color": "blue",
        "position": [30,0],
        "degrees": 225,
        "framerate": 0.25,
    },
    "green": {
        "name": "green",
        "color": "green",
        "position": [0,15],
        "degrees": 90,
        "framerate": 0.02,
    },
    "yellow": {
        "name": "yellow",
        "color": "yellow",
        "position": [15,0],
        "degrees": 180,
        "framerate": 0.50,
    },
}


for v in scribes_dict.keys():
    # x = scribes_dict.get(v)
    # print(type(x))
    # print(x['position'])
    # scribe.drawScribe(x)
    scribe.drawScribe(scribes_dict.get(v))
    # for i in range(30):
    #     scribe.forward()
