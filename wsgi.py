from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask.sessions import SessionInterface
import pymysql
import pyclub
from pyclub.dbconnect import *


app = Flask(__name__)
app.secret_key = 'cokolwiek'
users = {'iduser': 1, 'email': 'admin@gmail.com', 'login': 'admin', 'password': 'admin'}
attempted_password = None
attempted_username = None


@app.route('/')
def index():
    if 'ID' not in session:
        return render_template('index.html')
    else:
        return render_template('profile.html', owner=session['ID'])


@app.route('/login/', methods=["GET", "POST"])
def login_page():

    if request.method == "POST":

        attempted_email = request.form['email']
        attempted_password = request.form['password']

        if attempted_password == users['password'] and attempted_email == users['email']:
            session['ID'] = users['iduser']
            return redirect(url_for('index'))

        return redirect(url_for('loginerror'))

    return render_template("login.html")


@app.route('/database/', methods=["GET", "POST"])
def database():
    user = str(get_user(3))
    return user



@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/loginerror/')
def loginerror():
    return render_template("loginerror.html")


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1")
