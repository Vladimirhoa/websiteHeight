from django.db import models
from django.contrib.auth.models import User  # Импортируем модель пользователя


class NewsItem(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    image_news = models.ImageField(upload_to='news', blank=True, null=True, verbose_name="Фото для новости")

    # Новое поле: Лайки (Многие пользователи могут лайкнуть одну новость)
    likes = models.ManyToManyField(User, related_name='news_likes', blank=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    # Удобный метод для подсчета лайков
    def total_likes(self):
        return self.likes.count()


# Новая модель: Комментарий
class Comment(models.Model):
    post = models.ForeignKey(NewsItem, on_delete=models.CASCADE, related_name='comments', verbose_name="Новость")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.TextField(verbose_name="Текст комментария")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['-created_date']  # Свежие комментарии сверху

    def __str__(self):
        return f"Комментарий от {self.author.username} к {self.post.title}"