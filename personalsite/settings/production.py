from .base import *

DATABASES = {
    'default': dj_database_url.config()
}
SECURE_SSL_REDIRECT = True
PREPEND_WWW = True
BASE_URL = "https://www.truongben.com"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)