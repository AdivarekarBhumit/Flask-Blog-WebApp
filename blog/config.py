import os 

class Config:
    SECRET_KEY = os.environ.get('FLASK_SECRET')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLITE_STRING')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
