from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse, Http404
from .models import Article

def home_page(request):
    article = Article.objects.all()
    return render(request, 'article/article.html', {'article':article})
