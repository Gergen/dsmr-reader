"""
Django settings for dsmrreader project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.utils.translation import ugettext_lazy as _


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'As]7aV!PRYS>z"UtigJn(T{)p8y=}0iEfj&<#Ykx3"=Uk?M^B,'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    # Django internals.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # Third party apps/plugins.
    'solo.apps.SoloAppConfig',
    'colorfield',
    'django_filters',
    'rest_framework',

    # Local project apps.
    'dsmr_api.apps.AppConfig',
    'dsmr_datalogger.apps.AppConfig',
    'dsmr_consumption.apps.AppConfig',
    'dsmr_weather.apps.AppConfig',
    'dsmr_stats.apps.AppConfig',
    'dsmr_backend.apps.AppConfig',
    'dsmr_frontend.apps.AppConfig',
    'dsmr_backup.apps.AppConfig',
    'dsmr_dropbox.apps.AppConfig',
    'dsmr_mindergas.apps.AppConfig',
    'dsmr_notification.apps.AppConfig',
    'dsmr_mqtt.apps.AppConfig',
    'dsmr_pvoutput.apps.AppConfig',
    'dsmr_plugins.apps.AppConfig',
)

MIDDLEWARE = (
    # Debug toolbar.
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    # Local.
    'dsmr_frontend.middleware.exception_traceback.ExceptionTracebackMiddleware',
)

ROOT_URLCONF = 'dsmrreader.urls'

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

                # Project version.
                'dsmr_frontend.context_processors.version',
            ],
        },
    },
]

WSGI_APPLICATION = 'dsmrreader.wsgi.application'

LOGIN_URL = 'admin:login'
LOGOUT_URL = 'admin:logout'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {}  # Force in sub configs.


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# Django creates migrations based on default language. Therefor we need to force English here.
LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Localization.
# https://docs.djangoproject.com/en/1.8/topics/i18n/formatting/
FORMAT_MODULE_PATH = [
    'dsmrreader.formats'
]
USE_THOUSAND_SEPARATOR = True

# Caching framework. Advantages of caching in memory but without requiring memcached installed.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': 10,
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'

# Translation files.
LANGUAGES = (
    ('nl', _('Dutch')),
    ('en', _('English')),
)

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locales'), )


""" Python Logging. """
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)-8s %(message)s'
        },
        'verbose': {
            'format': '[%(asctime)s] %(levelname)-8s @ %(module)s | %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'django_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, '..', 'logs', 'django.log'),
            'formatter': 'verbose',
            'maxBytes': 5 * 1024 * 1024,  # 5 MB max.
            'backupCount': 7,
        },
        'dsmrreader_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, '..', 'logs', 'dsmrreader.log'),
            'formatter': 'verbose',
            'maxBytes': 5 * 1024 * 1024,  # 5 MB max.
            'backupCount': 7,
        },
    },
    'loggers': {
        'commands': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django': {
            'handlers': ['django_file'],
            'level': 'WARNING',
            'propagate': True,
        },
        'dsmrreader': {
            'handlers': ['dsmrreader_file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}


""" Django Rest Framework. """

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.OrderingFilter',
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dsmr_api.authentication.HeaderAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 25,
}


""" DSMR Project settings. """
from .dsmrreader import *
