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

class Character(GameElement):
    IMAGE = "Girl"

    def keyboard_handler(self, symbol, modifer):
        if symbol == key.UP:
            self.board.draw_msg('%s says: "You pressed up!"' % self.IMAGE)
        elif symbol == key.SPACE:
            self.board.erase_msg()
        elif symbol == key.DOWN:
            self.board.draw_msg('%s says: "You pressed down!"' % self.IMAGE)
        elif symbol == key.LEFT:
            self.board.draw_msg('%s says: "You pressed left!"' % self.IMAGE)
        elif symbol == key.RIGHT:
            self.board.draw_msg('%s says: "You pressed right!"' % self.IMAGE)
# class Character_Horns(GameElement):
#     IMAGE = "Horns"
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

    #initializes Character
    player = Character()
    GAME_BOARD.register(player)
    GAME_BOARD.set_el(2, 2, player)


    # initializes the Character Horns
    # player = Character(IMAGE="Horns")
    player = Character()
    player.IMAGE = "Horns"
    GAME_BOARD.register(player)
    GAME_BOARD.set_el(3, 3, player)

    # initializes the Character Cat
    # player = Character(IMAGE="Cat")
    player = Character()
    player.IMAGE = "Cat"
    GAME_BOARD.register(player)
    GAME_BOARD.set_el(1, 3, player)

    # initializes the Character Princess
    # player = Character(IMAGE="Princess")
    player = Character()
    player.IMAGE = "Princess"
    GAME_BOARD.register(player)
    GAME_BOARD.set_el(0, 4, player)
    
    GAME_BOARD.draw_msg("This game is wicked awesome.")