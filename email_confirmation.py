from main import app
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Mail, Message
from pyclub.dbconnect import get_user

mail = Mail(app)

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])


def confirm_token(token):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt = app.config['SECURITY_PASSWORD_SALT'],
        )
    except Exception:
        return False
    return email


def send_email_authentication(email):
    activation_link = "{0}/activate/{1}".format("{0}:{1}".format(
    app.config["HOST"], app.config["PORT"]
    ), generate_confirmation_token(email))
    msg = Message ("E-mail authentication",
        sender=app.config["MAIL_USERNAME"],
        recipients=[email])
    msg.body = "Hello {0}!\nTo authenticate your email enter this link:\n {1}\n \nPyClub".format(get_user(email)['first_name'],
    activation_link)
    mail.send(msg)
