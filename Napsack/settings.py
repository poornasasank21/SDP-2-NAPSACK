"""
Django settings for Napsack project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4ou8zk7k^#e6^nu2o+x#s^7toa%ry6-0_-&%!cme$zv&oqnfbf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'NapsackAdmin.apps.NapsackadminConfig',
    'Customer.apps.CustomerConfig',
    'Agents.apps.AgentsConfig',
    'Dealer.apps.DealerConfig',
    'Payments.apps.PaymentsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'phonenumber_field',
    'django_bootstrap_icons'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Napsack.urls'

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

WSGI_APPLICATION = 'Napsack.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'napdb',
        'USER': 'root',
        'PASSWORD': 'mVre9392',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",

        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'napsack',
        # 'USER': 'napsack',
        # 'PASSWORD': 'mVre@9392',
        # 'HOST': 'napsack.mysql.database.azure.com',
        # 'PORT': '3306',
        # 'OPTIONS': {
        #     'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        #     'ssl': {'ca': 'DigiCertGlobalRootCA.crt.pem'}

        }
    }
}

WHITENOISE_USE_FINDERS = True


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
# STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# STATIC_ROOT = 'D:/home/site/wwwroot/static'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


API_KEY = "df1606dc-a515-11ec-a4c2-0200cd936042"


CSRF_TRUSTED_ORIGINS = ['https://napsack.azurewebsites.net']

# Base url to serve media files


MEDIA_URL = '/media/'
# Path where media is stored



MEDIA_ROOT = os.path.join(BASE_DIR, 'media')




BS_ICONS_BASE_URL = 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/'

BS_ICONS_CUSTOM_PATH = 'custom-icons'