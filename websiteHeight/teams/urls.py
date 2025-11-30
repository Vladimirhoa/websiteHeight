from django.urls import path
from . import views

urlpatterns = [
    # Маршрут для страницы со списком команд
    path('', views.team_list, name='team_list'),
]