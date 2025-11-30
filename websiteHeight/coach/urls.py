# coach/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Если пользователь переходит на /coach/
    path('', views.coach_detail, name='coach_detail'),
]