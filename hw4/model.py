import sqlite3

def register_user(username, password, age):
    conn = sqlite3.connect('table.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(f"""SELECT * FROM users WHERE username='{username}';""")
    db_username = cursor.fetchone()
    if db_username is None:
        cursor.execute(f"""INSERT INTO users (username, password, age)
        VALUES('{username}', '{password}', '{age}');""")
        conn.commit()
        cursor.close()
        conn.close()
        return "You registered successfuly"
    else:
        return "username already exist"
    return "You've succesfully signed up"

def get_dashboard():
    conn = sqlite3.connect('table.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM users;""")
    tb = cursor.fetchall()
    
    conn.commit()
    cursor.close()
    conn.close()

    return tb