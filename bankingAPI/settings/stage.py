from .base import *
from .secrets import *

DEBUG = True

SERVER_ = ''

ALLOWED_HOSTS = ['*']

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],

    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dfo6283p92kijd',
        'USER': 'yllgynwycuhyaj',
        'PASSWORD': 'b9d1bd048d81b97e7c8cf34663c8db6640b35b5fc2ddc253f00b14ac58982ba8',
        'HOST': 'ec2-34-200-116-132.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}
"""

def show_toolbar(request):
    return False

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'library.settings.stage.show_toolbar',
}
