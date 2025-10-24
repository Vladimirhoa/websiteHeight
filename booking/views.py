# booking/views.py
from django.shortcuts import render
from .models import TrainingSession # <--- Импортируем нашу модель

def session_list(request):
    # 1. Запрос данных: Получаем все тренировки, сортируем по дате и времени
    sessions = TrainingSession.objects.all().order_by('date_time')

    # 2. Создание контекста: Подготавливаем данные для передачи в шаблон
    context = {
        'sessions': sessions
    }

    # 3. Отображение: Вызываем HTML-шаблон и передаем ему контекст
    return render(request, 'booking/session_list.html', context)