# contacts/views.py
from django.shortcuts import render
from .models import ContactInfo


def contact_page(request):
    # Получаем единственную запись с контактами (или None, если ее нет)
    contact_info = ContactInfo.objects.first()

    context = {
        'contact_info': contact_info,
        'page_title': 'Контакты'
    }
    return render(request, 'contacts/contact_page.html', context)