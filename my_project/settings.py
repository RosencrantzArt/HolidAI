from pathlib import Path
import os
import dj_database_url

if os.path.isfile('env.py'):
    import env


database_url = os.environ.get("DATABASE_URL")
if isinstance(database_url, bytes):
    database_url = database_url.decode("utf-8")


DATABASES = {
    'default': dj_database_url.parse(database_url)
}


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-default-key')

DEBUG = False  

ALLOWED_HOSTS = ['8000-rosencrantzart-holidai-7vw3vsg5ffm.ws-eu115.gitpod.io', '.herokuapp.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello_world',
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

ROOT_URLCONF = 'my_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'my_project.wsgi.application'

#STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'  # Statisk URL-sökväg

LANGUAGE_CODE = 'sv-se'

TIME_ZONE = 'Europe/Stockholm'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
