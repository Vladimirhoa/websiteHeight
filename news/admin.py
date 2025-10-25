from django.contrib import admin
from .models import NewsItem

@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'is_published')
    list_filter = ('is_published', 'pub_date')
    search_fields = ('title', 'content')

