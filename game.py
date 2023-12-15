import sql_param
import sql_game
import new_game
import os
import sys

sql_param.init_db()

# récupération des paramètres généraux
params = sql_param.gen_param()
small_dice = params[0]
big_dice = params[1]
max_player = params[2]

os.system('clear')

nb_gamers = input(f"Combien de joueurs pour cette partie ? (choisir un nombre entre 2 et {max_player}) ")

try:
    nb_gamers = int(nb_gamers)
except:
    print("C'est même pas un nombre ça !")
    sys.exit()

if nb_gamers < 2 or nb_gamers > max_player:
    print("Quel dommage de vous voir partir ainsi, en ne sachant pas répondre correctement à cette question !")
    sys.exit()

