from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'SIM',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'db',
        'PORT': '5432',
    },
}