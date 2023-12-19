'''
classes pour la gestion du jeu
'''

import gamers
from random import randint
from time import time
import sys
import sql_game

class NewGame:
    def __init__(self, nb_gamers: int, board_game_width: int, board_game_height: int):
        
        board_game = [["" for y in range(board_game_width)] for x in range(board_game_height)]
        
        self.gamers = []
        gamers_id = []# pour ne pas ajouter plusieurs fois le même joueur

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

            id, alias, personnage = sql_game.gamer_choice_added(gamers_id)
            gamers_id.append(id)

            self.gamers.append(gamers.Gamer(x, y, id, alias, personnage))
    
    def nb_gamers(self) -> int:
        return len(self.gamers)
    
    def gamers_sprite(self):
        for gamer in self.gamers:
            yield gamer