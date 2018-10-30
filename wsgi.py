from flask import render_template, request, url_for, redirect, session
from pyclub.dbconnect import create_user, confirm_email, get_user
from werkzeug.security import generate_password_hash, check_password_hash
from email_confirmation import confirm_token, send_email_authentication
from main import app


@app.route("/")
def index_page():
    logged_in = None
    if 'first_name' in session:
        logged_in = session['first_name']
    return render_template("index.html", session_true = logged_in)


@app.route("/register/", methods = ["POST", "GET"])
def register_page():
    logged_in = None
    error_message = None
    if request.method == "POST":
        new_email = request.form['email']
        new_password = request.form['password']
        new_password_confirm = request.form['password_confirm']
        new_first_name = request.form['name']
        new_last_name = request.form['last_name']
        if new_email and new_password and new_first_name and new_last_name and new_password == new_password_confirm and '@' in new_email:
            new_password = generate_password_hash(new_password)
            create_user(new_first_name, new_last_name, new_email, new_password)
            send_email_authentication(new_email)
            return redirect(url_for('index_page'))
        elif '@' not in new_email:
            error_message = "Email musi zawierać znak @"
        elif new_password != new_password_confirm:
            error_message = "Hasła muszą się zgadzać"
        else:
            error_message = "Uzupełnij wszystkie pola"
    return render_template("register.html", error = error_message, session_true = logged_in)


@app.route("/login/", methods = ["POST", "GET"])
def login_page():
    error_message = None
    logged_in = None
    if request.method == "POST":
        attempted_email = request.form['email']
        attempted_password = request.form['password']
        user_dict = get_user(str(attempted_email))
        if user_dict is None:
            error_message = 'Użytkownika nie ma w systemie'
        else:
            db_password = user_dict.get('password')
            if check_password_hash(db_password, attempted_password):
                db_name = user_dict.get('first_name')
                session['first_name'] = db_name
                db_id = user_dict.get('iduser')
                session['ID'] = db_id
                return redirect(url_for('index_page'))
            error_message = "Nieprawidłowe hasło"
    return render_template("login.html", session_true = logged_in, error = error_message)

@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('index_page'))


@app.route("/contact/")
def contact_page():
    logged_in = None
    if 'first_name' in session:
        logged_in = session['first_name']
    return render_template("contact.html", session_true = logged_in)


@app.route("/about/")
def about_page():
    logged_in = None
    if 'first_name' in session:
        logged_in = session['first_name']
    return render_template("about.html", session_true = logged_in)

@app.route("/profile/")
def profile_page():
    logged_in = None
    if 'first_name' in session:
        logged_in = session['first_name']
        user_id = session['ID']
        current_user_dict = get_user(str(user_id))
        first_name = current_user_dict['first_name']
        last_name = current_user_dict['last_name']
        email = current_user_dict['email']
    return render_template("profile.html", session_true = logged_in, user_first_name = first_name, user_last_name = last_name, user_email = email)



@app.route("/activate/<confirmation_token>/")
def activate_account(confirmation_token):
        mail = confirm_token(confirmation_token)
        confirm_email(mail)
        return redirect(url_for('index_page'))


#error handlers

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404notfound.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('505server_error.html')


if __name__ == "__main__":
    app.run(host = app.config["HOST"], port = app.config["PORT"], debug=app.config["DEBUG"])
