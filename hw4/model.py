import sqlite3

def register_user(username, password, age):
    conn = sqlite3.connect('database.db', check_same_thread=False)
    cursor = conn.cursor()
    db_username = cursor.execute(f"""SELECT username FROM users WHERE username='{username}'""")
    if db_username == username:
        return "username already exist"
    else:
        cursor.execute(f"""INSERT INTO users (username, password, age)VALUES('{username}','{password}','{age}')""")
        return "You registered successfuly"
    
    conn.commit()
    cursor.close()
    conn.close()