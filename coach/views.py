from django.shortcuts import render
from .models import Coach

def coach_detail(request):
    # Получаем ВСЕХ тренеров из базы данных
    coaches = Coach.objects.all()

    context = {
        'coaches': coaches,
        'page_title': 'Наши Тренеры'
    }
    # Используем тот же шаблон (или можно переименовать его в coach_list.html)
    return render(request, 'coach/coach_detail.html', context)