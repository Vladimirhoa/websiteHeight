# mywebsite/context_processors.py
from contacts.models import ContactInfo


def global_contact_info(request):
    """
    Добавляет единственную запись ContactInfo в контекст всех шаблонов.
    """
    try:
        # Пытаемся получить единственную запись
        contact_info = ContactInfo.objects.first()
    except Exception:
        # Обработка исключения на случай, если таблица еще не создана
        contact_info = None

    return {
        'GLOBAL_CONTACT': contact_info
    }