# mywebsite/settings/local.py

# 1. Импортируем все базовые настройки
from .base import *

# 2. Перезаписываем настройки для локальной разработки
# ВАЖНО: DEBUG = True для runserver
DEBUG = True

# 3. Разрешаем локальные хосты (обычно можно оставить пустым, если DEBUG=True)
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# 4. Убедитесь, что для локальной БД используется SQLite3 (если это не так)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 5. Убедитесь, что STATIC_ROOT корректен (может быть унаследован из base.py)
# Если base.py содержит: STATIC_ROOT = os.path.join(BASE_DIR, '../../staticfiles')
# А local.py находится в mywebsite/settings/, то BASE_DIR (которая указывает на mywebsite/)
# не соответствует этой относительной логике.

# Для локальной разработки часто можно вообще не указывать STATIC_ROOT
# Или используйте:
# STATIC_ROOT = BASE_DIR / 'static'