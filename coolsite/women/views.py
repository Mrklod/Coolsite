from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

def index(request):
    return HttpResponse("Главная страница")

def pageNotFound(request,exeption):
    return HttpResponseNotFound("Страница не найдена")