from flask import Flask, render_template, request, session, redirect, url_for, g
import sqlite3
import model

app = Flask(__name__)
app.secret_key = "mujluguni"
username = ''
user = ''

@app.route('/')
def home():
    if 'username' in session:
        g.user = session['username']
    return render_template('home.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        age = request.form.get('age')
        if username and email and password and age:
            msg = model.register_user(username, email, password, age)
            session.pop('username', None)
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('register.html', message="Enter all field")
    else:
        return render_template('register.html', message="Please register")

@app.route('/login', methods=['GET' ,'POST'])
def login():
    if request.method == 'POST':
        session.pop('username', None)
        email = request.form.get('email')
        password = request.form.get('password')
        if email and password:
            db_user = model.check_user(email)
            if db_user[1] == password:
                session['username'] = db_user[0]
                return redirect(url_for('dashboard'))
            return render_template('login.html', message="Email or Password incorrect")
        else:
            return render_template('login.html', message="Enter all fields")
    else:
        return render_template('login.html', message='Please Log In')

@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username']

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == "POST":
        user = session['username']
        post = request.form.get('post')
        if post:
            model.do_post(user, post)
        return redirect(url_for("dashboard"))
    else:
        if 'username' in session:
            user = session['username']
            table = model.get_dashboard(user)
            return render_template('dashboard.html', table=table)
        else:
            return redirect(url_for('login'))

@app.route('/delete', methods=['POST'])
def delete():
    post = request.form.get("post")
    model.delete_post(post)
    return redirect(url_for('dashboard'))

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/terms', methods=['GET'])
def terms():
    return render_template('terms.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    return render_template('admin_login.html')

@app.route('/admin/users')
def admin_users():
    users = model.users_for_admin()
    return render_template('admin_users.html', users=users)

@app.route('/admin_dashboard')
def admin_dashboard():
    posts, users_count, lists_count = model.admin_dashboard()
    return render_template('admin_dashboard.html', posts=posts, users_count=users_count, lists_count=lists_count)

@app.route('/getsession')
def getsession():
    if 'username' in session:
        return session['username']
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)