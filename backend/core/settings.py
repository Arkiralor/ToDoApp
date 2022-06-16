from pathlib import Path
from os import environ, path, makedirs

ENV_TYPE = environ.get('ENV_TYPE', 'dev').lower()
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = environ.get('SECRET_KEY', 'secret-key-random-sequence-of-characters')
DEBUG = eval(environ.get('DEBUG', 'False'))

ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'api.apps.ApiConfig',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ.get('PGDATABASE'),
        'USER': environ.get('PGUSER'),
        'PASSWORD': environ.get('PGPASSWORD'),
        'HOST': environ.get('PGHOST'),
        'PORT': environ.get('PGPORT'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


## Internationalization
LANGUAGE_CODE = environ.get('LANGUAGE_CODE', 'en-us')
TIME_ZONE = environ.get('TIME_ZONE', 'UTC')
USE_I18N = eval(environ.get('USE_I18N', 'True'))
USE_TZ = eval(environ.get('USE_TZ', 'True'))

STATIC_URL = 'static/'
STATIC_FILES_DIRS = [
    path.join(BASE_DIR, 'static'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ORIGIN_WHITELIST = environ.get('CORS_ORIGIN_WHITELIST', ' ').split(' ')

## Create directory for logs
LOG_DIR = path.join(BASE_DIR, 'logs/')
if not path.exists(LOG_DIR):
    makedirs(LOG_DIR)
ENV_LOG_FILE = path.join(LOG_DIR, f'{ENV_TYPE}_root.log')
DJANGO_LOG_FILE = path.join(LOG_DIR, 'django.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'root_file': {
            'class': 'logging.FileHandler',
            'filename': ENV_LOG_FILE,
            'formatter': 'verbose',
            'encoding': 'utf-8',
        },
        'django_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': DJANGO_LOG_FILE,
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'local',
            'encoding': 'utf-8',
        }
    },
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s|%(asctime)s.%(msecs)d|%(name)s|%(module)s|%(funcName)s:%(lineno)s]    %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
        'local': {
            'format': '[%(asctime)s|%(name)s|%(module)s|%(funcName)s:%(lineno)s]    %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
    },
    'loggers': {
        'root': {
            'handlers': ['console', 'root_file'],
            "level": 'INFO'
        },
        'django': {
            'handlers': ['console', 'django_file'],
            'level': 'INFO',
            'propagate': True
        },
    },
}
