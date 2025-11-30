from django.contrib import admin
from .models import ContactInfo

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email')
    # Это позволяет пользователям редактировать запись, кликая по любому полю
    list_display_links = ('address', 'phone', 'email')
