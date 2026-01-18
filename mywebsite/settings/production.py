# mywebsite/settings/production.py

from .base import *
# BASE_DIR уже корректно определен в base.py, но можно оставить переопределение,
# если оно совпадает (3 parent). Если в base.py исправили, здесь строку с BASE_DIR можно удалить.
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()
# 1. Безопасность
DEBUG = False

ALLOWED_HOSTS = ['*']

# 2. База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'websiteheight_db'),
        'USER': os.getenv('DB_USER', 'volodimir'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'mysecretpassword'),
        'HOST': os.getenv('DB_HOST', 'localhost'), 
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# 3. WhiteNoise (Статика)
try:
    # Проверка, чтобы не дублировать при перезагрузках
    if 'whitenoise.runserver_nostatic' not in INSTALLED_APPS:
        INSTALLED_APPS.insert(0, 'whitenoise.runserver_nostatic')
    if 'whitenoise.middleware.WhiteNoiseMiddleware' not in MIDDLEWARE:
        MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
except ValueError:
    pass

# 4. Пути
import os
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 5. HTTPS и Cloudflare
# ВАЖНО: Эта настройка говорит Django доверять заголовку X-Forwarded-Proto от прокси (Nginx/Cloudflare)
# Без этого SECURE_SSL_REDIRECT вызовет циклическую переадресацию.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = [
    'https://vkvysota.ru',
    'https://www.vkvysota.ru', # <--- Рекомендуется добавить версию с www
    'http://192.168.31.129',   # Для доступа по локальной сети (без https) может потребоваться
                               # отключить SECURE_SSL_REDIRECT или добавить исключения.
                               # Но Cloudflare работает по домену.
]
