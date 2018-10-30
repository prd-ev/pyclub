from flask import Flask

app = Flask(__name__)

app.secret_key = 'cokolwiek'

app.config.from_object('config.Config')

