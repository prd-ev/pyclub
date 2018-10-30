#config file

class Config(object):
    #SERVER CONFIGURATION
    HOST = "127.0.0.1"
    PORT = 5000
    DEBUG = False
    #EMAIL CONFIGURATION
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USERNAME = "pyclubpoznan@gmail.com"
    MAIL_PASSWORD = ""
    #SECURITY CONFIGURATION
    SECRET_KEY = b'Hello-there-general-kenobi'
    SECURITY_PASSWORD_SALT = 'witam123mordeczko'