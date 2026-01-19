import vk_api
import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from news.models import NewsItem, NewsImage
from django.utils import timezone
import datetime


class Command(BaseCommand):
    help = 'Синхронизация новостей из группы ВК'

    def handle(self, *args, **kwargs):
        # НАСТРОЙКИ
        VK_TOKEN = '9855690f9855690f9855690f8c9b6b1500998559855690ff13b25425cae0599f180c26d'
        GROUP_ID = -215432720  # ID группы ОБЯЗАТЕЛЬНО со знаком минус (если это сообщество)
        COUNT = 100  # Сколько последних постов проверять

        # Подключение к ВК
        vk_session = vk_api.VkApi(token=VK_TOKEN)
        vk = vk_session.get_api()

        self.stdout.write("Начинаю синхронизацию...")

        try:
            wall = vk.wall.get(owner_id=GROUP_ID, count=COUNT)

            for post in wall['items']:
                # Пропускаем, если уже есть в базе
                post_id = post['id']
                if NewsItem.objects.filter(vk_id=post_id).exists():
                    self.stdout.write(f"Пост {post_id} уже есть. Пропуск.")
                    continue

                text = post['text']
                if not text:
                    text = "Фотоотчет"

                timestamp = post['date']
                date = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)

                title = text[:50] + "..." if len(text) > 50 else text

                # 1. Создаем саму новость (пока без картинок)
                news = NewsItem(
                    title=title,
                    content=text,
                    pub_date=date,
                    is_published=True,
                    vk_id=post_id
                )
                news.save()  # Сохраняем, чтобы получить ID новости

                # 2. Собираем все ссылки на фото из вложений
                photo_urls = []
                if 'attachments' in post:
                    for att in post['attachments']:
                        if att['type'] == 'photo':
                            # Ищем максимальный размер
                            sizes = att['photo']['sizes']
                            best_url = sorted(sizes, key=lambda x: x['width'])[-1]['url']
                            photo_urls.append(best_url)

                # 3. Распределяем фото
                if photo_urls:
                    # ПЕРВОЕ ФОТО -> НА ОБЛОЖКУ
                    main_photo_url = photo_urls[0]
                    resp = requests.get(main_photo_url)
                    if resp.status_code == 200:
                        file_name = f"vk_main_{post_id}.jpg"
                        news.image_news.save(file_name, ContentFile(resp.content), save=True)

                    # ОСТАЛЬНЫЕ ФОТО -> В ГАЛЕРЕЮ
                    if len(photo_urls) > 1:
                        for i, url in enumerate(photo_urls[1:]):  # Начинаем со 2-го элемента
                            resp_gal = requests.get(url)
                            if resp_gal.status_code == 200:
                                gal_file_name = f"vk_gal_{post_id}_{i}.jpg"
                                # Создаем объект NewsImage
                                gallery_item = NewsImage(news=news)
                                gallery_item.image.save(gal_file_name, ContentFile(resp_gal.content))
                                gallery_item.save()

                self.stdout.write(self.style.SUCCESS(f"Добавлена новость: {title} (+{len(photo_urls)} фото)"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ошибка: {e}"))