import sqlite3

def get_all_pals():
    con = sqlite3.connect("Database/Paldata.db")
    cur = con.cursor()
    palnames = cur.execute("SELECT name FROM pal")
    return palnames