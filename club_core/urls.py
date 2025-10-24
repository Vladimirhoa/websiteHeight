# club_core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.home_page, name='home'),
]