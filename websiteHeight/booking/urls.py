from django.urls import path
from . import views

urlpatterns = [
    # Если пользователь переходит на корень приложения (например, /booking/)
    path('', views.session_list, name='session_list'),
]