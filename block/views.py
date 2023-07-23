from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("""<html>
    <title>Сайт Андрея Пяткина</title>
    <h1>Андрей Пяткин</h1>
    </html>""")
