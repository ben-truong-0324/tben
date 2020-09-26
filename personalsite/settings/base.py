import os
import sys
from decouple import config
from unipath import Path
from dj_database_url import parse as db_url


import dj_database_url

 
SECRET_KEY = config('SECRET_KEY')
GOOGLE_GEOCODE_KEY = config('GOOGLE_GEOCODE_KEY')
MAPBOX_TOKEN = config('MAPBOX_TOKEN')
DEBUG = config('DEBUG', default=False, cast=bool)
DEBUG_PROPAGATE_EXCEPTIONS = True

EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ALLOWED_HOSTS = ['.herokuapp.com',
                 'truongben.com',
                 '127.0.0.1',
                 'localhost',
                 '*'
                 ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'home.apps.HomeConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'personalsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'personalsite.wsgi.application'


SITE_ID = 1

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True

COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)

##########################################################
region = 'us-west-1'
BUILD_VERSION = 'tben-1.0'
##########################################################
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'compressor.finders.CompressorFinder',
]


#  Add configuration for static files storage using whitenoise
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
COMPRESS_OFFLINE = False
# COMPRESS_ENABLED = True
LIBSASS_OUTPUT_STYLE = 'compressed'

###################################################
SOCIAL_MEDIA_LINKS = (
    (1, 'twitter'),
    (2, 'facebook'),
    (3, 'instagram'),
    (4, 'youtube'),
    (5, 'linkedin'),
    (6, 'github'),
)