from django.contrib import admin
from .models import NewsItem, Comment, NewsImage

# 1. Создаем "вставку" для картинок
class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1  # Количество пустых полей для загрузки по умолчанию
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        # Отображение миниатюры (по желанию, для удобства)
        from django.utils.html import mark_safe
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" style="object-fit:cover;" />')
        return ""
    image_preview.short_description = "Предпросмотр"

# 2. Регистрируем саму новость с подключенным Inline
@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'is_published')
    inlines = [NewsImageInline] # <-- Вот здесь мы подключаем загрузку фото

# Регистрируем остальные модели
admin.site.register(Comment)
# admin.site.register(NewsImage) # Отдельно регистрировать не обязательно, так как он внутри NewsItem