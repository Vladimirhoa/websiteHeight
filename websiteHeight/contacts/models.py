from django.db import models
from django.core.exceptions import ValidationError

class ContactInfo(models.Model):
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Электронная почта")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    map_link = models.URLField(max_length=500, blank=True, null=True, verbose_name="Ссылка на Google/Яндекс.Карты")
    vk_link = models.URLField(max_length=500, blank=True, null=True, verbose_name="Ссылка на ВК")

    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактная информация"

    def __str__(self):
        return self.address

    # Добавляем метод для ограничения количества записей до одной
    def clean(self):
        if not self.pk and ContactInfo.objects.exists():
            raise ValidationError('Можно создать только одну запись с контактной информацией клуба.')

    def save(self, *args, **kwargs):
        # Принудительно вызываем clean перед сохранением для проверки ограничения
        self.full_clean()
        super().save(*args, **kwargs)

