import sqlite3

def query_execute(cur, query: str, select: str = ''):
    # permet d'essayer d'exécuter une requête et de renvoyer les données
    # si la requête ne fonctionne pas, un print sera fait de la requête intégrant les paramètres
    # la requête pourra être réexécuée à l'identique dans DVeaver pour débogage

    try:
        cur.execute(query)
        if select == 'SELECT':
            return cur.fetchone()

    except:
        query_error(query)


def query_error(query: str):
    # print des requêtes d'effectueuses

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
    datetime DATETIME NOT NULL,
    dice_type INTEGER NOT NULL);''')

    # CREATE TABLE "game_gamer"
    query_execute(cur, f'''
CREATE TABLE IF NOT EXISTS game_gamer (
	game_id INTEGER NOT NULL,
	gamer_id INTEGER NOT NULL,
	alias TEXT NOT NULL,
	score INTEGER NOT NULL,
	CONSTRAINT game_gamer_PK PRIMARY KEY (game_id,gamer_id)
    CONSTRAINT game_gamer_FK FOREIGN KEY (game_id) REFERENCES game(id),
	CONSTRAINT game_gamer_FK_1 FOREIGN KEY (gamer_id) REFERENCES gamer(id)
);''')
    
    # CREATE TABLE "param"
    query_execute(cur, f'''
CREATE TABLE IF NOT EXISTS param (
	small_dice INTEGER NOT NULL,
	big_dice INTEGER NOT NULL,
	max_player INTEGER NOT NULL
);''')
    
    # CREATE TABLE "categorie"
    query_execute(cur, f'''
CREATE TABLE IF NOT EXISTS categorie (
	name TEXT NOT NULL,
	CONSTRAINT categorie_PK PRIMARY KEY (name)
);''')
    query_execute(cur, f'''CREATE UNIQUE INDEX IF NOT EXISTS categorie_name_IDX ON categorie (name);''')
    
    # CREATE TABLE "answer"
    query_execute(cur, f'''
CREATE TABLE IF NOT EXISTS answer (
	categorie_name TEXT NOT NULL,
	question TEXT NOT NULL,
	answer TEXT NOT NULL,
	good_answer BOOL NOT NULL,
	CONSTRAINT answer_PK PRIMARY KEY (categorie_name,question,answer),
	CONSTRAINT answer_FK FOREIGN KEY (categorie_name) REFERENCES categorie(name)
);''')
    
    #paramètre par défaut du jeu 
    query_execute(cur, f'''
    DELETE FROM param 
    ''')
    query_execute(cur, f'''
    INSERT INTO param VALUES (4, 10, 8)
    ''')
    
    # Fermeture de la connexion
    conn.commit()
    conn.close()


def gen_param() -> tuple:
    # récupération des paramètres généraux pour le fonctionnement du jeu
    
    conn = sqlite3.connect('triv_ia_dlc.db')
    cur = conn.cursor()
    res = query_execute(cur, f'SELECT * FROM param', 'SELECT')
    conn.close()
    return res