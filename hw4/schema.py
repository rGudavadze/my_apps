import sqlite3

conn = sqlite3.connect('table.db', check_same_thread=False)

cursor = conn.cursor()

cursor.execute(
    """CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(16),
        email VARCHAR(32),
        password VARCHAR(32),
        age INTEGER);"""
)

conn.commit()
cursor.close()
conn.close()