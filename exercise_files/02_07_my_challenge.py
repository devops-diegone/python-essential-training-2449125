import os
import time
from termcolor import colored

# This is the Canvas class. It defines some height and width, and a 
# matrix of characters to keep track of where the TerminalScribes are moving
class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        # This is a grid that contains data about where the 
        # TerminalScribes have visited
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    # Returns True if the given point is outside the boundaries of the Canvas
    def hitsWall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

    # Set the given position to the provided character on the canvas
    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    # Clear the terminal (used to create animation)
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Clear the terminal and then print each line in the canvas
    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.2
        self.pos = [0, 0]

    def up(self):
        pos = [self.pos[0], self.pos[1]-1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def down(self):
        pos = [self.pos[0], self.pos[1]+1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def right(self):
        pos = [self.pos[0]+1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0]-1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def draw(self, pos):
        # Set the old position to the "trail" symbol
        self.canvas.setPos(self.pos, self.trail)
        # Update position
        self.pos = pos
        # Set the new position to the "mark" symbol
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        # Print everything to the screen
        self.canvas.print()
        # Sleep for a little bit to create the animation
        time.sleep(self.framerate)

# Create a new Canvas instance that is 30 units wide by 30 units tall 
# canvas = Canvas(30, 30)

# Create a new scribe and give it the Canvas object
# scribe = TerminalScribe(canvas)

# Draw a small square
# scribe.right()
# scribe.right()
# scribe.right()
# scribe.down()
# scribe.down()
# scribe.down()
# scribe.left()
# scribe.left()
# scribe.left()
# scribe.up()
# scribe.up()
# scribe.up()

#
## Function that draws the side of a square, taking direction, size and scribe
## object as input.
#
def drawSquareSide(object,direction,size):

    # Initialising size index
    i = 0

    # Matching requested direction and drawing requested size
    match direction:
        case 'right':
            while i < size -1:
                i += 1
                object.right()
        case 'left':
            while i < size -1:
                i += 1
                object.left()
        case 'up':
            while i < size -1:
                i += 1
                object.up()
        case 'down':
            while i < size -1:
                i += 1
                object.down()


#
## Function that draws a square, taking the size of its sides as an argument
#  (default = 2)
#
def drawSquare(sideSize=2):

    # Create a new Canvas instance that is 30 units wide by 30 units tall 
    canvas = Canvas(30, 30)

    # Create a new scribe and give it the Canvas object
    scribe = TerminalScribe(canvas)

    # Call side drawing function (4 times)
    drawSquareSide(scribe,'right',sideSize)
    drawSquareSide(scribe,'down',sideSize)
    drawSquareSide(scribe,'left',sideSize)
    drawSquareSide(scribe,'up',sideSize)


def drawCross(sideSize=2):

    # Create a new Canvas instance that is 30 units wide by 30 units tall 
    canvas = Canvas(30, 30)

    # Create a new scribe and give it the Canvas object
    scribe = TerminalScribe(canvas)

    # Moving marker's starting position to correct point in space
    scribe.pos = [0, sideSize - 1]

    # Call side drawing function (4 times)
    drawSquareSide(scribe,'right',sideSize)
    drawSquareSide(scribe,'up',sideSize)
    drawSquareSide(scribe,'right',sideSize)
    drawSquareSide(scribe,'down',sideSize)
    drawSquareSide(scribe,'right',sideSize)
    drawSquareSide(scribe,'down',sideSize)
    drawSquareSide(scribe,'left',sideSize)
    drawSquareSide(scribe,'down',sideSize)
    drawSquareSide(scribe,'left',sideSize)
    drawSquareSide(scribe,'up',sideSize)
    drawSquareSide(scribe,'left',sideSize)
    drawSquareSide(scribe,'up',sideSize)


# drawSquare(12)
drawCross(4)
