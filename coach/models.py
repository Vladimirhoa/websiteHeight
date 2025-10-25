# coach/models.py
from django.db import models

class Coach(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    specialty = models.CharField(max_length=200, verbose_name="Специализация")
    bio = models.TextField(verbose_name="Биография") # Длинное текстовое поле для истории/опыта
    image = models.ImageField(upload_to='coach_photos/', blank=True, null=True, verbose_name="Фото") # Для загрузки фото

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"