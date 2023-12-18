import sqlite3
import os
import sys

def query_execute(cur, query: str, select: str = ''):
    # permet d'essayer d'exécuter une requête et de renvoyer les données
    # si la requête ne fonctionne pas, un print sera fait de la requête intégrant les paramètres
    # la requête pourra être réexécuée à l'identique dans DVeaver pour débogage

    try:
        cur.execute(query)
        if select == 'SELECT':
            return cur.fetchone()
        if select == 'SELECT_ALL':
            return cur.fetchall()

    except:
        query_error(query)


def query_error(query: str):
    # print des requêtes d'effectueuses

    print("")
    print("/!\\")
    print("La requête suivant n'a pas pu être exécutée : ", query)
    print("/!\\")
    print("")


def all_gamers(cur) -> str:
    return query_execute(cur, f'SELECT * FROM gamer', 'SELECT_ALL')


def categories():
    conn = sqlite3.connect('triv_ia_dlc.db')
    cur = conn.cursor()
    
    res = query_execute(cur, f'SELECT * FROM categorie', 'SELECT_ALL')

    conn.close()

    return res


##################################################
##################################################
##################################################


def gamer_choice_added(gamers_id: list):
    conn = sqlite3.connect('triv_ia_dlc.db')
    cur = conn.cursor()
    os.system('clear')

    gamers = {}

    for gamer in all_gamers(cur):
        if gamer[0] not in gamers_id:
            print(gamer)
            gamers[gamer[0]] = gamer[1]

    action = input("Choisir un joueur à partir de son 'id' : ")
    try:
        action = int(action)
    except:
        print("/!\ FATAL ERROR /!\ 001 : sql_game.py > choix ID joueur")
        sys.exit()
    
    personnage = int(input('''Quel personnage veux-tu prendre ?
1 : Deadpool
2 : Captain America
3 : orc
4 : un perso dark
5 : un deuxieme perso encore plus dark
6 : un viking'''))

    try:
        action = int(action)
    except:
        print("/!\ FATAL ERROR /!\ 002 : sql_game.py > choix personnage")
        sys.exit()

    conn.commit()
    conn.close()

    return action, gamers[action], personnage