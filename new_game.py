'''
classes pour la gestion du jeu
'''

import gamers
from random import randint
from time import time
import sys

class NewGame:
    def __init__(self, nb_gamers: int, board_game_width: int, board_game_height: int):
        
        board_game = [["" for y in range(board_game_width)] for x in range(board_game_height)]
        
        self.gamers = []

        for i in range(nb_gamers):
            x_y = True
            time_start = time()
            while x_y:
                if time_start + 2 < time():
                    print("/!\ FATAL ERROR /!\ 001 : new_game.py > timer")
                    sys.exit()

                x = randint(0, board_game_width - 1)
                y = randint(0, board_game_height - 1)
                if board_game[y][x] == "":
                    x_y = False
            self.gamers.append(gamers.Gamer(x, y, i))