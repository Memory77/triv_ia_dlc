import sql_param
import sql_game
from new_game import NewGame
import os
import sys

sql_param.init_db()

# récupération des paramètres généraux
params = sql_param.gen_param()
small_dice = params[0]
big_dice = params[1]
max_player = params[2]
board_game_width = params[3]
board_game_height = params[4]

os.system('clear')

# shunter
if True == False:
    # nombre de joueur
    nb_gamers = input(f"Combien de joueurs pour cette partie ? (choisir un nombre entre 2 et {max_player}) ")

    try:
        nb_gamers = int(nb_gamers)
    except:
        print("C'est même pas un nombre ça !")
        sys.exit()

    if nb_gamers < 2 or nb_gamers > max_player:
        print("Quel dommage de vous voir partir ainsi, en ne sachant pas répondre correctement à cette question !")
        sys.exit()

    # type de dé
    dice = input(f"Quel type de dé voulez-vous utiliser ? (choisir un nombre entre {small_dice} et {big_dice}) ")

    try:
        dice = int(dice)
    except:
        print("C'est même pas un nombre ça !")
        sys.exit()

    if dice < small_dice or dice > big_dice:
        print("Quel dommage de vous voir partir ainsi, en ne sachant pas répondre correctement à cette question !")
        sys.exit()
else:
    # shunte
    nb_gamers = 2
    dice = 6

game = NewGame(nb_gamers, dice, board_game_width, board_game_height)

def new_game():
    return game