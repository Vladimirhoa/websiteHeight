from django.db import models

class NewsItem(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    #image_news = models.ImageField(upload_to='staticfiles/coach', blank=True, null=True, verbose_name="Фото")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        # Сортируем новости от новых к старым
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
