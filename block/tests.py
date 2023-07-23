from django.urls import resolve
from django.test import TestCase
from block.views import home_page
from django.http import HttpRequest
from django.http import HttpResponse

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