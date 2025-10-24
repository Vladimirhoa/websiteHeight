# booking/admin.py
from django.contrib import admin
from .models import TrainingSession, Booking

admin.site.register(TrainingSession)
admin.site.register(Booking)

# Register your models here.
