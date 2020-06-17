from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
with open('/home/npallthings/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: define the correct hosts in production!
#ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['www.neighbourhood-planning.co.uk']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
