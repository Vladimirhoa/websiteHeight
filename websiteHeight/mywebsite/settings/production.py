# Импортируем все базовые настройки
from .base import *

# --- 1. Настройки безопасности и хостов ---
# Отключаем режим отладки для продакшена!
DEBUG = False

# Разрешенные хосты (IP-адреса и доменное имя)
ALLOWED_HOSTS = [
    '127.0.0.1', 
    '93.175.13.6', 
    '192.168.31.232', 
    'vkvysota.ru',
    'www.vkvysota.ru',
]

# --- 2. Настройки приложений (для WhiteNoise) ---
# WhiteNoise используется для раздачи статических файлов в продакшене.
# Его нужно добавить выше django.contrib.staticfiles
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    # Убедитесь, что остальные приложения из base.py здесь импортированы 
    # или добавлены вручную, например:
    'django.contrib.staticfiles', 
    # ... другие приложения
]

# --- 3. Настройки Middleware (для WhiteNoise) ---
# WhiteNoiseMiddleware должен идти сразу после SecurityMiddleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Вставляем здесь
    # Убедитесь, что остальные Middleware из base.py здесь импортированы:
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    # ... другие Middleware
]

# --- 4. Настройки базы данных (MariaDB/MySQL) ---
# Используем ваши данные: логин 'wolodimir' и пароль '5679867'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'sql_mode': 'traditional',
        },
        'NAME': ' site_height_db',  # <<< ПРОВЕРЬТЕ: Имя базы данных, которую вы создали (например, 'vysota_db')
        'USER': 'wolodimir',
        'PASSWORD': '5679867',
        'HOST': 'localhost',   # Оставляем, так как БД находится на том же сервере
        'PORT': '3306',
    }
}

# --- 5. Настройки CORS / CSRF ---
# Включаем ваш домен для разрешенных запросов/источников
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'https://vkvysota.ru', # Используйте HTTPS для продакшена
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'https://vkvysota.ru',
]

# Этот параметр в новых версиях Django/CORS может быть устаревшим, 
# но включен для совместимости по требованию инструкции:
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8000',
    'https://vysota.ru',
]

# --- 6. Настройки статических файлов (для WhiteNoise) ---
# Убедитесь, что эти пути соответствуют путям в base.py, 
# но STATIC_ROOT должен быть определен для сбора статики.
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root') # Здесь будут собраны все статические файлы

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')