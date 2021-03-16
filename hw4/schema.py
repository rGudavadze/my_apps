import sqlite3

conn = sqlite3.connect('table.db', check_same_thread=False)

cursor = conn.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(16),
        email VARCHAR(32),
        password VARCHAR(32),
        age INTEGER);"""
)

cursor.execute(
    """CREATE TABLE IF NOT EXISTS posts(
        post_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        post TEXT,
        date TEXT
        );"""
)

conn.commit()
cursor.close()
conn.close()