from django.urls import resolve
from django.test import TestCase
from block.views import home_page
from block.models import Article
from django.http import HttpRequest
from django.http import HttpResponse
from datetime import datetime


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Сайт Андрея Пяткина</title>', html)
        self.assertIn('<h1>Андрей Пяткин</h1>', html)
        self.assertTrue(html.endswith('</html>'))


class ArticalModelTest(TestCase):
    def test_artical_model_save_and_retrieve(self):
        # Создай
        # статью 1 сохрани статью 1 в базе
        artical1 = Article(
            title="article 1",
            full_text='full_text 1',
            sumary='sumary 1',
            category='category 1',
            pubdate=datetime.now()
        )
        artical1.save()

        # сохрани  статью 2
        # сохрани статью 2 в базе
        artical2 = Article(
            title="article 1",
            full_text='full_text 1',
            sumary='sumary 1',
            category='category 1',
            pubdate=datetime.now
        )
        artical2.save()
        # загрузи из базы все статьи
        all_articles = Article.objects.all()
        # проверь статей должно быть 2
        self.assertEqual(len(all_articles), 2)
        # проверь: первая загруженная из базы статья == статья 1
        self.assertEqual(
            all_articles[0].title,
            artical1.title
        )
        # проверь: вторая загруженная из базы статья == статья 2
        self.assertEqual(
            all_articles[0].title,
            artical2.title
        )
