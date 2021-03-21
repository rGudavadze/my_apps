from datetime import datetime
import sqlite3

def register_user(username, email, password, age):
    conn = sqlite3.connect('table.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(f"""SELECT * FROM users WHERE username="{username}";""")
    db_user = cursor.fetchone()
    if db_user is None:
        cursor.execute(f"""INSERT INTO users (username, email, password, age)
        VALUES("{username}","{email}", "{password}", "{age}");""")
        conn.commit()
        cursor.close()
        conn.close()
        return "You registered successfuly"
    else:
        return "username already exist"
    return "You've succesfully signed up"

def check_user(email):
    conn = sqlite3.connect('table.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(f"""SELECT username, password FROM users WHERE email="{email}";""")
    user = cursor.fetchone()

    conn.commit()
    cursor.close()
    conn.close()

    if user:
        return user
    else:
        return ["", ""]

def get_dashboard(user):
    conn = sqlite3.connect('table.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(f"""SELECT pk FROM users WHERE username="{user}";""")
    user_id = cursor.fetchone()[0]
    cursor.execute(f"""SELECT * FROM posts JOIN users ON user_id=pk WHERE user_id={user_id} ORDER BY date DESC;""")
    user_posts = cursor.fetchall()
    
    conn.commit()
    cursor.close()
    conn.close()

    return user_posts


def do_post(user, post):
    conn = sqlite3.connect('table.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(f"""SELECT pk FROM users WHERE username = "{user}";""")
    user_id = cursor.fetchone()[0]

    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    cursor.execute(f"""INSERT INTO posts (user_id, post, date) VALUES ("{user_id}", "{post}", "{now}");""")

    conn.commit()
    cursor.close()
    conn.close()

def delete_post(post_id):
    conn = sqlite3.connect('table.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(f"""DELETE FROM posts WHERE post_id={post_id}""")

    conn.commit()
    cursor.close()
    conn.close()