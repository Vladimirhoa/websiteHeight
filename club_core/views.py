
from django.shortcuts import render
from news.models import NewsItem
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
def home_page(request):
    latest_news = NewsItem.objects.filter(is_published=True)[:5]
    context = {
        'page_title': 'Главная',
        'latest_news': latest_news,  # Передаем новости в шаблон
    }
    return render(request, 'club_core/home.html', context)
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




# Create your views here.
