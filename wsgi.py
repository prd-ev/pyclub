from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/register/")
def register_page():
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