from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def index(request):
    return render(request, 'onlineshopmain/index.html')

def about(request):
    return render(request, 'onlineshopmain/about.html')

def categories(request):
    all_categories = Category.objects.all()
    return render(request, 'onlineshopmain/categories.html', {'categories': all_categories})

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')