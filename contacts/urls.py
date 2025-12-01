from django.urls import path
from . import views

urlpatterns = [
    # Если пользователь переходит на /contacts/
    path('', views.contact_page, name='contacts'),
]