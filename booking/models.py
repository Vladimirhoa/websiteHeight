# booking/models.py
from django.db import models
from django.contrib.auth.models import User  # Используем встроенную модель пользователя


class TrainingSession(models.Model):
    name = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    is_tournament = models.BooleanField(default=False)
    max_participants = models.IntegerField(default=20)

    def __str__(self):
        return f"{self.name} ({self.date_time})"


class Booking(models.Model):
    session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ссылка на того, кто записался
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('session', 'user')  # Пользователь может записаться только 1 раз



# Create your models here.
