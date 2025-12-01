from django.shortcuts import render, get_object_or_404, redirect
from .models import NewsItem, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin



def news_details(request, pk):
    news_item = get_object_or_404(NewsItem, pk=pk)

    # 1. Обработка формы комментария
    if request.method == 'POST':
        # Если отправили форму и пользователь авторизован
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = news_item  # Привязываем к текущей новости
                new_comment.author = request.user  # Привязываем к текущему юзеру
                new_comment.save()
                return redirect('news_page', pk=pk)  # Перезагружаем страницу
        else:
            # Если неавторизованный пытается отправить POST (на всякий случай)
            return redirect('login')
    else:
        comment_form = CommentForm()

    # 2. Проверка: лайкнул ли уже этот пользователь новость?
    is_liked = False
    if request.user.is_authenticated:
        if news_item.likes.filter(id=request.user.id).exists():
            is_liked = True

    context = {
        'item': news_item,
        'page_title': news_item.title,
        'comments': news_item.comments.all(),  # Получаем все комменты
        'comment_form': comment_form,
        'is_liked': is_liked,
        'total_likes': news_item.total_likes(),
    }
    return render(request, 'news/news_page.html', context)


@login_required  # Декоратор: только для вошедших пользователей
def news_like(request, pk):
    news_item = get_object_or_404(NewsItem, pk=pk)

    # Если лайк уже стоит - убираем. Если нет - ставим.
    if news_item.likes.filter(id=request.user.id).exists():
        news_item.likes.remove(request.user)
    else:
        news_item.likes.add(request.user)

    return redirect('news_page', pk=pk)

#удалении комментариев
class CommentDeleteView(UserPassesTestMixin, DeleteView):
    # Указываем модель, которую удаляем
    model = Comment
    # Указываем шаблон для запроса подтверждения (см. Шаг 3)
    template_name = 'news/comment_confirm_delete.html'

    # 1. Проверка прав доступа
    def test_func(self):
        # Получаем объект комментария, который пользователь пытается удалить
        comment = self.get_object()

        # Разрешаем удаление, если:
        # a) Пользователь — суперпользователь (администратор)
        # ИЛИ
        # б) Пользователь является автором комментария (comment.author)
        return self.request.user.is_superuser or (comment.author == self.request.user)

    # 2. Куда перенаправить после успешного удаления
    def get_success_url(self):
        # Используем имя URL 'news_page', которое ты уже используешь
        # в своей функции news_details для перенаправления.
        # self.object.post.pk получает ID новости, к которой относился комментарий
        return reverse('news_page', kwargs={'pk': self.object.post.pk})