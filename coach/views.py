from django.shortcuts import render, get_object_or_404
from .models import Coach

def coach_detail(request):
    # 1. Получаем первого (или единственного) тренера по ID 1.
    # get_object_or_404 автоматически вызовет ошибку 404,
    # если тренера с ID=1 нет в базе (лучше, чем ошибка сервера).
    try:
        coach = Coach.objects.get(pk=1)
    except Coach.DoesNotExist:
        # Если вы хотите более гибкий подход (например, если нет тренера с pk=1),
        # можно просто взять первого попавшегося, если он есть
        coach = Coach.objects.all()
        if not coach:
            # Если в базе вообще нет тренеров
            return render(request, 'coach/coach_detail.html', {'coach': None})

    context = {
        'coach': coach,
        'page_title':'Наши Тренеры'
    }
    # 2. Передаем данные в шаблон
    return render(request, 'coach/coach_detail.html', context)
