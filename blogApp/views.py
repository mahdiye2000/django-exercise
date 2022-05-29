from django.shortcuts import render
from django.http import HttpResponse
from . import models

def articles(request):
    articles = models.BlogPost.objects.all()
    return render(request, 'blogApp/index.html', {'articles' : articles})

def article(request, slug):
    article = models.BlogPost.objects.get(pk=slug)
    return render(request, 'blogApp/detail.html', {'article' : article})
