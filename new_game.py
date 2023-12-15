'''
classes pour la gestion du jeu
'''

import gamers

class NewGame:
    def __init__(self, nb_gamers: int):
        self.gamers = []
        for i in range(nb_gamers):
            self.gamers.append(gamers.Gamer(0, 0, i))