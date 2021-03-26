from datetime import datetime
import sqlite3

def register_user(username, email, password, age):
    conn = sqlite3.connect('table.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(f"""SELECT * FROM users WHERE username="{username}";""")
    db_user = cursor.fetchone()
    if db_user is None:
        now = datetime.now()
        cursor.execute(f"""INSERT INTO users (username, email, password, age, reg_date)
        VALUES("{username}","{email}", "{password}", "{age}", "{now}");""")
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
    cursor.execute(f"""SELECT * FROM posts JOIN users ON user_id=pk WHERE user_id={user_id} ORDER BY reg_date DESC;""")
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

    now = datetime.now()

    cursor.execute(f"""INSERT INTO posts (user_id, post, post_date) VALUES ("{user_id}", "{post}", "{now}");""")

    conn.commit()
    cursor.close()
    conn.close()

def delete_post(post_id):
    conn = sqlite3.connect('table.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(f"""DELETE FROM posts WHERE post_id={post_id};""")

    conn.commit()
    cursor.close()
    conn.close()

def admin_dashboard():
    conn = sqlite3.connect('table.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("""SELECT post FROM posts WHERE post_date >= datetime('now','-1 day') ORDER BY post_date DESC;""")
    posts = cursor.fetchall()
    cursor.execute("""SELECT COUNT(*) FROM users""")
    users_count = cursor.fetchone()[0]
    cursor.execute("""SELECT COUNT(*) FROM posts""")
    lists_count = cursor.fetchone()[0]
    cursor.execute("""SELECT COUNT(*) FROM users WHERE reg_date >= datetime('now','-1 day');""")
    lastday = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return posts, users_count, lists_count, lastday

def users_for_admin(number):
    conn = sqlite3.connect('table.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(f"""SELECT username FROM users LIMIT {50} OFFSET {(number-1)*50};""")
    users = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()

    return users

def about_user(username):
    conn = sqlite3.connect('table.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(f"""SELECT pk, username, email, age FROM users WHERE username="{username}";""")
    user = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()

    return user

def delete_user_info(username):
    conn = sqlite3.connect('table.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(f"""SELECT pk FROM users WHERE username="{username}";""")
    pk = cursor.fetchone()[0]
    cursor.execute(f"""DELETE FROM posts WHERE user_id="{pk}";""")
    cursor.execute(f"""DELETE FROM users WHERE pk={pk};""")

    conn.commit()
    cursor.close()
    conn.close()

def admin_login(email, password):
    conn = sqlite3.connect('table.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(f"""SELECT email, password FROM admin WHERE email='{email}';""")
    user = cursor.fetchone()
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return user
