
from django.shortcuts import render


def home_page(request):
    # Здесь можно добавить логику для получения последних новостей
    context = {
        'latest_news': [
            {'title': 'Победа в турнире!', 'date': '20.10.2025'},
            {'title': 'Новое расписание тренировок', 'date': '15.10.2025'},
        ],
        'page_title': 'Главная страница клуба'
    }
    return render(request, 'club_core/home.html', context)


from django.shortcuts import render

# Create your views here.
