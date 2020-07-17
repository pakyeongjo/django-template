from backend.settings.config import conf_info
from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*', ]
INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
