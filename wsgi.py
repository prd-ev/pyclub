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


@app.route('/database/')
def database():
    user = str(get_user(3))
    return user

@app.route('/register/', methods=["GET","POST"])
def register():

    if request.method == "POST":

        new_first_name = request.form['first_name']
        new_last_name = request.form['last_name']
        new_email = request.form['email']
        new_password = request.form['password']
        if new_first_name and new_last_name and new_email and new_password:
            create_user(new_first_name, new_last_name, new_email, new_password)
        return redirect(url_for("index"))
    return render_template("register.html")

@app.route('/hello/', methods=["GET","POST"])
def hello():
    return '123'



@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('index'))



@app.route("/about/")
def about_page():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1")