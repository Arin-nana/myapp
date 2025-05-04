import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '<ваш-telegram-token>')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'myapp.apps.MyAppConfig',
]

# timezone и локаль
TIME_ZONE = 'UTC'
USE_TZ = True

