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
board = (GAME_WIDTH, GAME_HEIGHT)

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True

class Gem(GameElement):
    IMAGE = "BlueGem"
    SOLID = False

    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a gem! You have %d items!" % (len(player.inventory)))

class Character(GameElement):
    IMAGE = "Girl"

    
    def get_boundary(self, x, y):
        b = "this is the next position "
        print 0, b, x, y
        print_cant_go_there = 0
        # save the unchanged value of x and y
        if (x >= 5 ):
            x -= 1
            print_cant_go_there = 1
            GAME_BOARD.draw_msg("You can't go there! Try another direction.")
        elif ( y >= 5 ): 
            y -= 1
            print_cant_go_there = 1
            GAME_BOARD.draw_msg("You can't go there! Try another direction.")
        elif (x <= -1 ):
            x += 1
            print_cant_go_there = 1
            GAME_BOARD.draw_msg("You can't go there! Try another direction.")
        elif ( y <= -1):
            y += 1
            print_cant_go_there = 1
            GAME_BOARD.draw_msg("You can't go there! Try another direction.")
        
        print 0.1, b, x, y        
        return x, y, print_cant_go_there  # pass unchanged value of x and y
    

    def next_pos(self, x, y):
        # save_x = x
        # # save_y = y
        # if direction == "up":
        print 4.1, self.x, self.y
        return (self.get_boundary(self.x, self.y))
        #elif direction == "down":
        #    return (self.get_boundary(self.x, self.y))
            # if (self.get_boundary(self.x, self.y)) == True:
            #     print 4.2, self.x, (self.y + 1)
            #     return (self.x, self.y + 1)
            # else:
            #     print 4.3, self.x, self.y
            #     return (self.x, self.y)
        # elif direction == "left":
        #     if (self.get_boundary(self.x, self.y)) == True:
        #         return (self.x - 1, self.y)
        #     else:
        #          return (self.x, self.y)
        # elif direction == "right":
        #     if (self.get_boundary(self.x, self.y)) == True:
        #         return (self.x + 1, self.y)
        #     else:
        #         return (self.x, self.y)

    def keyboard_handler(self, symbol, modifer):
        direction = None
        next_x = self.x
        next_y = self.y
        if symbol== key.UP:
            direction = "up"
            self.y -= 1
        elif symbol == key.DOWN:
            direction = "down"
            self.y += 1 
        elif symbol == key.LEFT:
            direction = "left"
            self.x -= 1
        elif symbol == key.RIGHT:
            self.x += 1
            direction = "right"

        self.board.draw_msg("[%s] moves %s" % (self.IMAGE, direction))

        if direction:
            print_cant_go_there = 0
            next_location = self.next_pos(self.x, self.y)
            b = " this is the return value of next_pos = "
            print 1.0, b, next_location
            print_cant_go_there = next_location[2]
            if print_cant_go_there == 1:
                self.x = next_x
                self.y = next_y

            b = " == "
            if next_location:
                # next_x = next_location[0]
                # next_y = next_location[1]
                # print 1.3, self.x, self.y, b, next_x, next_y
                # save occupant of next position
                existing_el = self.board.get_el(next_x, next_y)
                if existing_el:
                    existing_el.interact(self)
                if existing_el and existing_el.SOLID:
                    self.board.draw_msg("There's something in my way!")
                    print 1.5, self.x, self.y, b, next_x, next_y
                elif existing_el is None or not existing_el.SOLID:
                    print 1.7, self.x, self.y, b, next_x, next_y
                    self.board.del_el(self.x, self.y)
                    self.board.set_el(next_x, next_y, self)
#                    self.board.del_el(next_x, next_y)
#                    self.board.set_el(self.x, self.y, self)


    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []

#         if symbol == key.UP:
#             #self.board.draw_msg('%s says: "You pressed up!"' % self.IMAGE)
#             self.board.del_el(self.x, self.y)
#             self.x, self.y = self.next_pos("up")
#             self.board.set_el(self.x, self.y, self)
#         elif symbol == key.SPACE:
#             self.board.erase_msg()
#         elif symbol == key.DOWN:
#             #self.board.draw_msg('%s says: "You pressed down!"' % self.IMAGE)
#             self.board.del_el(self.x, self.y)
#             self.x, self.y = self.next_pos("down")
#             self.board.set_el(self.x, self.y, self)
#         elif symbol == key.LEFT:
#             #self.board.draw_msg('%s says: "You pressed left!"' % self.IMAGE)
#             self.board.del_el(self.x, self.y)
#             self.x, self.y = self.next_pos("left")
#             self.board.set_el(self.x, self.y, self)
#         elif symbol == key.RIGHT:
#             #self.board.draw_msg('%s says: "You pressed right!"' % self.IMAGE)
#             self.board.del_el(self.x, self.y)
#             self.x, self.y = self.next_pos("right")
#             self.board.set_el(self.x, self.y, self)
# # class Character_Horns(GameElement):
# #     IMAGE = "Horns"
# ####   End class definitions    ####

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

    #initializes Character
    player = Character()
    GAME_BOARD.register(player)
    GAME_BOARD.set_el(2, 4, player)

    """
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
    """    
    GAME_BOARD.draw_msg("This game is wicked awesome.")
    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(3, 1, gem)