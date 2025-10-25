from django.shortcuts import render, get_object_or_404
from .models import NewsItem

def news_details(request, pk):
    news_item = get_object_or_404(NewsItem, pk=pk)

    context = {
        'item': news_item,
        'page_title': news_item.title,
    }
    return render(request, 'news/news_page.html', context)