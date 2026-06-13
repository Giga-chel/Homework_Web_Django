import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default_secret_key'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your_email@gmail.com'
    MAIL_PASSWORD = 'your_password'
