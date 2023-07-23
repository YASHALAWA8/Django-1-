
from selenium import webdriver

import unittest
from selenium.webdriver.common.by import By

# from django.core.management.commands.runserver import Command as RunserverCommand

# class Command(RunserverCommand):
#     def handle(self, *args, **options):
#         # Добавьте опцию для автоматического порта при запуске тестов
#         if not options.get('addrport'):
#             options['addrport'] = '8000'  # Здесь можно указать желаемый порт, если он свободен

#         super().handle(*args, **options)


class BasicInstallTest(unittest.TestCase):
    # Жил был вася
    # Вася работает аналитиком в какой то компании
    # Однажды вася захотел прокачаться в когортном анализе
    # Вася защел в Гугл, ввел запрос "Кородныйй анализ" и кликнул по одной из сылки
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        # В браузере Васи открылся сайт (по адресу ...)
        # В заголовке сайта Васи прочиатл "Андрей Пяткин"
        self.browser.get('http://localhost:8000')
        self.assertIn('Сайт Андрея Пяткина', self.browser.title)

    def test_home_page_header(self):
        # В шапке сайта написанно "Андрей Пяткин"
        browser = self.browser.get('http://localhost:8000')
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('Андрей Пяткин', header.text)


if __name__ == '__main__':
    unittest.main()


# В шапке сайта расположен блог  со статьям.

# У каждой статьи есть заголовок и один обзац с текстом

# Вася кликнул по заголовку и один абзац с текстом

# Вася кликнул по заголовку и у него открылась станица с полным текстом статьи

# Проичитав статью Вася кликнул по тексту "Андрей Пяткин" в шапке сайта
# Попал обратно на главную страницу
