from django.shortcuts import render, redirect
from news.models import NewsItem
from django.contrib.auth.forms import UserCreationForm


def home_page(request):
    # ---- НАЧАЛО ИЗМЕНЕНИЙ ----

    # Мы изменили этот запрос, чтобы он:
    # 1. Брал только новости, где есть фото (image_news__isnull=False)
    # 2. Явно сортировал их от новых к старым
    # 3. Брал 3 новости для карусели (а не 5)

    latest_news = NewsItem.objects.filter(
        is_published=True,
        image_news__isnull=False  # <-- Убеждаемся, что фото есть
    ).order_by('-pub_date')[:3]  # <-- Берем 3

    # ---- КОНЕЦ ИЗМЕНЕНИЙ ----

    context = {
        'page_title': 'Главная',
        'latest_news': latest_news,  # Эта переменная теперь содержит 3 новости с фото
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