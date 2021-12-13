import sqlite3

def init(path: str) -> connection_and_cursor:
    db_conn = sqlite3.connect(path)
    db_cursor = db_conn.cursor()
    return db_conn, db_cursor