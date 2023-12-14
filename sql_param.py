import sqlite3

def init_db():
    # new connexion (create db if doesn't exist)
    conn = sqlite3.connect('triv_ia_dlc.db')

    # new cursor
    cur = conn.cursor()

    # Fermeture de la connexion
    conn.close()