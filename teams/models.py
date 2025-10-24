from django.db import models

class Team(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название команды"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание"
    )
    logo = models.ImageField(
        upload_to='teams/logos/',
        blank=True,
        null=True,
        verbose_name="Логотип"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Активна"
    )

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Если вы захотите создать детальную страницу для команды
        from django.urls import reverse
        return reverse('team_detail', args=[self.id])