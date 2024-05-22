from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("<h1>Главная</h1>")


def writers(request):
    name = request.GET.get('writers')
    year = request.GET.get('year')
    if year == '1926':
        return HttpResponse(f"<h1>Книги которые написал {name} в 1926 году</h1>")
    elif year == '1940':
        return HttpResponse(f"<h1>Книги которые написал {name} в 1940 году</h1>")
    else:
        return HttpResponse("<h1>Писатели</h1>")


def books(request):
    return HttpResponse("<h1>Топ лучших книг</h1>")


def hemingway(request):
    return HttpResponse(f"<h1>о Хемингуэе {request.GET}</h1>")


def shakespeare(request):
    return HttpResponse("<h1>о Шекспире</h1>")


def top(request, bookid):
    return HttpResponse(f"<h1>На {bookid} месте книга... </h1>")


def old_man(request):
    return HttpResponse("<h1>Старик и море...</h1>")


def sun(request):
    return HttpResponse("<h1>И восходит солнце</h1>")


# def req(request):
#     name = request.GET.get('writers')
#     year = request.GET.get('year')
#     return HttpResponse(f"<h1>Книги которые написал {name} в {year} году</h1>")
