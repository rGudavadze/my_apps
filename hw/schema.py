import sqlite3

conn = sqlite3.connect('table.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(16),
        email VARCHAR(32),
        password VARCHAR(32),
        age INTEGER,
        reg_date datetime);"""
)

cursor.execute(
    """CREATE TABLE IF NOT EXISTS posts(
        post_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        post TEXT,
        post_date datetime,
        FOREIGN KEY (user_id) REFERENCES users (pk)
        );"""
)

cursor.execute(
    """CREATE TABLE IF NOT EXISTS admin(
        username VARCHAR(16),
        email VARCHAR(32),
        password VARCHAR(32));"""
)
cursor.execute(
    """INSERT INTO admin(username, email, password) VALUES("romaroma", "romaroma@gmail.com", "password");"""
)


conn.commit()
cursor.close()
conn.close()