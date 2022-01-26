import sqlite3

def init(path: str) -> tuple:
    db_con = sqlite3.connect(path)
    db_cursor = db_con.cursor()
    return db_con, db_cursor