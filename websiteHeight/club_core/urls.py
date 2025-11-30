# club_core/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    # Главная страница
    path('', views.home_page, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register_user, name='register'),
]