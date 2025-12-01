from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.news_details, name='news_page'),
    # Новый маршрут для лайка
    path('<int:pk>/like/', views.news_like, name='news_like'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]