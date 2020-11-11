import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wq3rfqaGBW325121@!#!$!@$!@2RFD23RFQ@*rdn%8^whnq7x)'

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "185.246.67.8"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gamesite',
        'USER': 'max_user',
        'PASSWORD': 'pacum140820007',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')