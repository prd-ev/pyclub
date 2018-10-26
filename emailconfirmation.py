from main import app
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Mail, Message
from pyclub.dbconnect import get_user

mail = Mail(app)

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer("Hello there")
    return serializer.dumps(email, salt="General Kenobi")


def confirm_token(token):
    serializer = URLSafeTimedSerializer("Hello there")
    try:
        email = serializer.loads(
            token,
            salt = "General Kenobi",
        )
    except:
        return False
    return email


def send_email_authentication(email):
    activation_link = "{0}/activate/{1}".format("127.0.0.1:5000", generate_confirmation_token(email))
    msg = Message ("E-mail authentication",
        sender="pyclubpoznan@gmail.com",
        recipients=[email])
    msg.body = "Hello {0}!\nTo authenticate your email enter this link:\n {1}\n \nPyClub".format(get_user(email)['first_name'],
    activation_link)
    mail.send(msg)
