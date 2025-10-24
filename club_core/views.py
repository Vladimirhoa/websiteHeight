
from django.shortcuts import render
from news.models import NewsItem

def home_page(request):
    latest_news = NewsItem.objects.filter(is_published=True)[:5]
    context = {
        'page_title': 'Главная',
        'latest_news': latest_news,  # Передаем новости в шаблон
    }
    return render(request, 'club_core/home.html', context)


from django.shortcuts import render

# Create your views here.
