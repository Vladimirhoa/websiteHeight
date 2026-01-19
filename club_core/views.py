from django.shortcuts import render, redirect
from news.models import NewsItem
from django.contrib.auth.forms import UserCreationForm


def home_page(request):
    # 1. Новости для карусели (только с картинками, 3 самые свежие)
    carousel_news = NewsItem.objects.filter(
        is_published=True,
        image_news__isnull=False
    ).order_by('-pub_date')[:3]

    # Собираем ID новостей, попавших в карусель, чтобы исключить их из общего списка
    # (чтобы не дублировать новость и в карусели, и в списке снизу)
    carousel_ids = [news.id for news in carousel_news]

    # 2. Все остальные новости (бесконечная лента)
    # Берем все опубликованные и исключаем (exclude) те, что уже в карусели
    other_news = NewsItem.objects.filter(
        is_published=True
    ).exclude(id__in=carousel_ids).order_by('-pub_date')

    context = {
        'page_title': 'Главная',
        'carousel_news': carousel_news, # Передаем топ-3
        'other_news': other_news,       # Передаем всё остальное
    }
    return render(request, 'club_core/home.html', context)
#
# Эту функцию мы не трогали, она остается как была
#
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Перенаправляем на главную после успешной регистрации
            return redirect('home')
    else:
        form = UserCreationForm()

    context = {
        'form': form,
        'page_title': 'Регистрация'
    }
    return render(request, 'club_core/register.html', context)