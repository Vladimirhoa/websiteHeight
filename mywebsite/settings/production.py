from .base import *
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent.parent
# 1. Безопасность
DEBUG = False

ALLOWED_HOSTS = [
    '93.175.13.6', 
    'localhost', 
    '127.0.0.1', 
    'vkvysota.ru',
    'www.vkvysota.ru',
]

# 2. База данных (PostgreSQL)
# Мы настраивали Postgres, поэтому используем этот движок и твои данные
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'websiteheight_db',
        'USER': 'volodimir',
        'PASSWORD': '5679867',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# 3. Настройка WhiteNoise (статика)
# Добавляем WhiteNoise в начало списка приложений
INSTALLED_APPS.insert(0, 'whitenoise.runserver_nostatic')

# Добавляем WhiteNoiseMiddleware после SecurityMiddleware
# (SecurityMiddleware обычно идет первым элементом с индексом 0)
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# 4. Пути к статике
import os
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 5. HTTPS настройки (раскомментируй, когда подключишь SSL сертификат)
# CSRF_TRUSTED_ORIGINS = ['https://vkvysota.ru']
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True          # Перенаправлять всех на HTTPS
SESSION_COOKIE_SECURE = True        # Куки только через HTTPS
CSRF_COOKIE_SECURE = True           # CSRF-токен только через HTTPS
CSRF_TRUSTED_ORIGINS = [
    'https://vkvysota.ru'
]
