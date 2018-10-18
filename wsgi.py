from flask import Flask, render_template, request
from pyclub.dbconnect import create_user
from werkzeug.security import generate_password_hash
import CONFIG 

app = Flask(__name__)

@app.route("/")
def index_page():
    return render_template("index.html")


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
            new_password = generate_password_hash(new_password)
            create_user(new_first_name, new_last_name, new_email, new_password)
        elif new_password != new_password_confirm:
            error_message = "Hasła muszą się zgadzać"
        else:
            error_message = "Uzupełnij wszystkie pola"
    return render_template("register.html", error = error_message)


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
    app.run(debug=CONFIG.DEBUG, host=CONFIG.HOST, port=CONFIG.PORT)