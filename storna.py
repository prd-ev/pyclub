from flask import Flask, render_template, request, redirect, url_for
from lista import generator
from name import imie
from Users import users
from Passwords import passwords
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/login/', methods=["GET","POST"])
def login_page():

    if request.method == "POST":

        attempted_username = request.form['username']
        attempted_password = request.form['password']

            #flash(attempted_username)
            #flash(attempted_password)

        if attempted_username in users and attempted_password in passwords:
            return redirect(url_for('hi'))
        else:
            return redirect(url_for('loginerror'))
    return render_template("login.html") 
		
@app.route('/register/', methods=["GET","POST"])
def rejestracja():

    error = ''
    try:
	
        if request.method == "POST":
		
            attempted_username = request.form['username']
            attempted_password = request.form['password']

            #flash(attempted_username)
            #flash(attempted_password)

            users.append(attempted_username)
            passwords.append(attempted_password)

        return render_template("register.html", error = error)

    except Exception as e:
        #flash(e)
        return render_template("register.html", error = error)


@app.route('/app/')
def hi():
    return "Hello there"


@app.route('/loginerror/')
def loginerror():
    return render_template("loginerror.html")


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1")
