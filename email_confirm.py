from flask import Flask
from flask_mail import Mail, Message
from pyclub.dbconnect import *
from werkzeug.security import generate_password_hash

app = Flask(__name__)


app.config.update(
    DEBUG = True,
    HOST = "127.0.0.1",

    MAIL_SERVER = "smtp.gmail.com",
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = "pyclubpoznan@gmail.com",
    MAIL_PASSWORD = "pyclub123",
    )

mail = Mail(app)

@app.route("/confirmemail")
def sendmail():
    send_email_authenticator("kostekkor@gmail.com")
    return "Sent"

def send_email_authenticator(recipient):
    activation_link = "{0}/activate/{1}".format(app.config['HOST'], generate_password_hash(recipient))
    msg = Message ("E-mail authentication",
        sender="pyclubpoznan@gmail.com",
        recipients=[recipient])
    msg.body = "Hello {0}!\nTo authenticate your email enter this link:\n {1}\n \nPyClub".format(get_user_name(recipient)['first_name'],
    activation_link)
    mail.send(msg)

if __name__ == "__main__":
    app.run()

