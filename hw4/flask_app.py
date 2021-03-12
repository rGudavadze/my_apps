from flask import Flask, render_template, request, session, redirect, url_for, g
import sqlite3
import model

app = Flask(__name__)
app.secret_key = "mujluguni"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/terms', methods=['GET'])
def terms():
    return render_template('terms.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        age = request.form.get('age')
        msg = model.register_user(username, password, age)
        return render_template('register.html', message=msg)
    else:
        return render_template('register.html', message="Please register")

@app.route('/login', methods=['GET' ,'POST'])
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    table = model.get_dashboard()
    return render_template('dashboard.html', table=table)

if __name__ == "__main__":
    app.run(debug=True)