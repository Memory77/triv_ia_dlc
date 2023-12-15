import sqlite3

def query_execute(cur, query: str):
    try:
        cur.execute(query)

    except:
        query_error(query)

def query_error(query: str):
    print("")
    print("/!\\")
    print("La requête suivant n'a pas pu être exécutée : ", query)
    print("/!\\")
    print("")

def init_db():
    # new connexion (create db if doesn't exist)
    conn = sqlite3.connect('triv_ia_dlc.db')

    # new cursor
    cur = conn.cursor()

    # CREATE TABLE "gamer"
    query_execute(cur, f'''
CREATE TABLE IF NOT EXISTS gamer (
    id INTEGER PRIMARY KEY,
    alias TEXT NOT NULL);''')
    query_execute(cur, f'''CREATE UNIQUE INDEX IF NOT EXISTS gamer_alias_IDX ON gamer (alias);''')

    # CREATE TABLE "game"
    query_execute(cur, f'''
CREATE TABLE IF NOT EXISTS game (
    id INTEGER PRIMARY KEY,
    datetime TEXT NOT NULL,
    dice_type INTEGER NOT NULL);''')

    # CREATE TABLE "game_gamer"
    query_execute(cur, f'''
CREATE TABLE game_gamer (
	game_id INTEGER NOT NULL,
	gamer_id INTEGER NOT NULL,
	alias TEXT NOT NULL,
	score INTEGER NOT NULL,
	CONSTRAINT game_gamer_PK PRIMARY KEY (game_id,gamer_id)
);''')
    
    # Fermeture de la connexion
    conn.close()