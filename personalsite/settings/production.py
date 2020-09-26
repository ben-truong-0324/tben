from .base import *

DATABASES = {
    'default': dj_database_url.config()
}
SECURE_SSL_REDIRECT = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'personalize/static'),)
