from flask import Flask, render_template, request, redirect, url_for, session
from flask.sessions import SessionInterface
from pyclub.dbconnect import *
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = 'cokolwiek'

@app.route("/")
def index_page():
    qwe = None
    if 'ID' in session:
        qwe = '123'
    return render_template("index.html", session_true = qwe)


@app.route("/register/", methods = ["POST", "GET"])
def register_page():
    error_message = None
    if request.method == "POST":
        new_email = request.form['email']
        new_password = request.form['password']
        new_password_confirm = request.form['password_confirm']
        new_first_name = request.form['name']
        new_last_name = request.form['last_name']
        if new_email and new_password and new_first_name and new_last_name and new_password == new_password_confirm:
            create_user(new_first_name, new_last_name, new_email, new_password)
        elif new_password != new_password_confirm:
            error_message = "Hasła muszą się zgadzać"
        else:
            error_message = "Uzupełnij wszystkie pola"
    return render_template("register.html", error = error_message)


@app.route("/login/", methods = ["POST", "GET"])
def login_page():
    if request.method == "POST":
        attempted_email = request.form['email']
        attempted_password = request.form['password']
        test = get_user(str(attempted_email))
        db_password = test.get('password')
        db_id = test.get('iduser')
        if db_password == attempted_password:
            session['ID'] = db_id
            return redirect(url_for('index_page'))
    return render_template("login.html")

@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('index_page'))


@app.route("/contact/")
def contact_page():
    return render_template("contact.html")


@app.route("/about/")
def about_page():
    return render_template("about.html")


"""@app.route('/test/')
def test():
"""



if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1")