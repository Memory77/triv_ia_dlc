'''
classes pour la gestion du jeu
'''

import gamers
from random import randint
from time import time
import sys
import sql_game

class NewGame:
    def __init__(self,
                 nb_gamers: int,
                 dice: int,
                 board_game_width: int,
                 board_game_height: int,
                 simple_question_points: int,
                 camembert_question_points: int,
                 hole_points: int,
                 time_points: int,
                 time_answer_out: int,
                 end_game_max_points: int,
                 end_game_max_camembert: int):
        
        self.dice = dice

        board_game = [["" for y in range(board_game_width)] for x in range(board_game_height)]
        self.board_game_width = board_game_width
        self.board_game_height = board_game_height
        self.simple_question_points = simple_question_points
        self.camembert_question_points = camembert_question_points
        self.hole_points = hole_points
        self.time_points = time_points
        self.time_answer_out = time_answer_out
        self.end_game_max_points = end_game_max_points
        self.end_game_max_camembert = end_game_max_camembert
        
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
    
    #retourne le gagnant si les conditions de victoire sont verifiés
    def victory(self) -> bool:
        for gamer in self.gamers:
            if gamer.score >= self.end_game_max_points or len(gamer.camembert_part) >= self.end_game_max_camembert:
                return gamer 
        return None