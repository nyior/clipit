"""
Django settings for shortster project.

Generated by 'django-admin startproject' using Django 2.2.13.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 'q-07$lqceq^az917yc!$m5yiikb3b(&8u^mr=gzy&)th^m4^zc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    #third party packages
    'rest_framework',
    'rest_framework_swagger',
    'corsheaders',

    #developer apps
    'main'
]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
     'DEFAULT_AUTHENTICATION_CLASSES': [
    ]
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True
    },
]
#where django goes to find routing info
ROOT_URLCONF = 'shortster.urls'


WSGI_APPLICATION = 'shortster.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#use postgre-sql on heroku
if 'DATABASE_URL' in os.environ:
    import dj_database_url
    
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CORS_ALLOWED_ORIGINS = [
        'http://localhost:8080', 
        'https://shter.netlify.app'
]

CORS_ALLOW_CREDENTIALS = True
 