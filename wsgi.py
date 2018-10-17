from flask import Flask, render_template, request, url_for, redirect, flash
from pyclub.dbconnect import *

app = Flask(__name__)

@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/register/", methods = ["POST", "GET"])
def register_page():
    if request.method == "POST":

        new_email = request.form['email']
        new_password = request.form['password']
        new_password_confirm = request.form['password_confirm']
        new_first_name = request.form['name']
        new_last_name = request.form['last_name']

        if new_email and new_password and new_first_name and new_last_name and new_password == new_password_confirm:
            add_user(new_first_name, new_last_name, new_email, new_password)
    return render_template("register.html")


@app.route("/login/")
def login_page():
    return render_template("login.html")


@app.route("/contact/")
def contact_page():
    return render_template("contact.html")


@app.route("/about/")
def about_page():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1")