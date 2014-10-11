import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
######################

GAME_WIDTH = 5
GAME_HEIGHT = 5

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True

class Character(GameElement):
    IMAGE = "Girl"

    def get_boundary(self, x, y):

        boundary_error = False
        if x <= -1:
            self.x = 0 # or maybe a saved value?
            boundary_error = True
        elif y <= -1:
            self.y = 0
            boundary_error = True
        elif x >= GAME_WIDTH:
            self.x = 4
            boundary_error = True
        elif y >= GAME_HEIGHT:
            self.y = 4
            boundary_error = True
        else:
            boundary_error = False
        
        return x, y, boundary_error

    def next_pos(self, direction):
        
        if direction == "up":
            return self.get_boundary(self.x, self.y-1)
        elif direction == "down":
            return self.get_boundary(self.x, self.y+1)
        elif direction == "left":
            return self.get_boundary(self.x-1, self.y)
        elif direction == "right":
            return self.get_boundary(self.x+1, self.y)

        return self.x, self.y, None

    def keyboard_handler(self, symbol, modifier):

        direction = None
        if symbol == key.UP:
            direction = "up"
        elif symbol == key.DOWN:
            direction = "down"
        elif symbol == key.LEFT:
            direction = "left"
        elif symbol == key.RIGHT:
            direction = "right"

        self.board.draw_msg("[%s] moves %s" % (self.IMAGE, direction))

        if direction:
            next_location = self.next_pos(direction)
            
            if next_location[2] == True:
                self.board.draw_msg(
                    "You can't move %s! Choose a different direction." % direction)
            elif next_location and next_location[2] == False: 
                next_x = next_location[0]
                next_y = next_location[1]

                existing_el = self.board.get_el(next_x, next_y)
                
                if existing_el and existing_el.SOLID:
                    self.board.draw_msg("There's something in my way!")
                elif existing_el is None or not existing_el.SOLID:
                    self.board.del_el(self.x, self.y)
                    self.board.set_el(next_x, next_y, self)

####   End class definitions    ####

def initialize():
    """Put game initialization code here"""
    rock_positions = [
            (2, 1),
            (1, 2),
            (3, 2),
            (2, 3) 
        ]

    rocks = []

    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    rocks[-1].SOLID = False

    player = Character()
    GAME_BOARD.register(player)
    GAME_BOARD.set_el(2, 2, player)