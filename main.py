from flask import Flask

app = Flask(__name__)

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = "pyclubpoznan@gmail.com",
    MAIL_PASSWORD = ""
)
