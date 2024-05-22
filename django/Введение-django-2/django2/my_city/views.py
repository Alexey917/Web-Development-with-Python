from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<ul>'
                        '<li><a href="/">Главная</a></li>'
                        '<li><a href="/news">новости</a></li>'
                        '<li><a href="/management">Руководство</a></li>'
                        '<li><a href="/facts">Факты</a></li>'
                        '<li><a href="/contacts">Контакты</a></li>'
                        '<li><a href="/history">Истроия</a></li>'
                        '</ul>'
                        '<h1>Главная</h1>')


def news(request):
    return HttpResponse('<ul>'
                        '<li><a href="/">Главная</a></li>'
                        '<li><a href="/news">новости</a></li>'
                        '<li><a href="/management">Руководство</a></li>'
                        '<li><a href="/facts">Факты</a></li>'
                        '<li><a href="/contacts">Контакты</a></li>'
                        '<li><a href="/history">Истроия</a></li>'
                        '</ul>'
                        '<h1>Новости города</h1>')


def management(request):
    return HttpResponse('<ul>'
                        '<li><a href="/">Главная</a></li>'
                        '<li><a href="/news">новости</a></li>'
                        '<li><a href="/management">Руководство</a></li>'
                        '<li><a href="/facts">Факты</a></li>'
                        '<li><a href="/contacts">Контакты</a></li>'
                        '<li><a href="/history">Истроия</a></li>'
                        '</ul>'
                        '<h1>Руководство города</h1>')


def facts(request):
    return HttpResponse('<ul>'
                        '<li><a href="/">Главная</a></li>'
                        '<li><a href="/news">новости</a></li>'
                        '<li><a href="/management">Руководство</a></li>'
                        '<li><a href="/facts">Факты</a></li>'
                        '<li><a href="/contacts">Контакты</a></li>'
                        '<li><a href="/history">Истроия</a></li>'
                        '</ul>'
                        '<h1>Факты о городе</h1>')


def contacts(request):
    return HttpResponse('<ul>'
                        '<li><a href="/">Главная</a></li>'
                        '<li><a href="/news">новости</a></li>'
                        '<li><a href="/management">Руководство</a></li>'
                        '<li><a href="/facts">Факты</a></li>'
                        '<li><a href="/contacts">Контакты</a></li>'
                        '<li><a href="/history">Истроия</a></li>'
                        '</ul>'
                        '<h1>Контактные телефоны городских служб</h1>')


def history(request):
    return HttpResponse('<ul>'
                        '<li><a href="/">Главная</a></li>'
                        '<li><a href="/news">новости</a></li>'
                        '<li><a href="/management">Руководство</a></li>'
                        '<li><a href="/facts">Факты</a></li>'
                        '<li><a href="/contacts">Контакты</a></li>'
                        '<li><a href="/history/people">Люди</a></li>'
                        '<li><a href="/history/photos">Фотографии</a></li>'
                        '</ul>'
                        '<h1>История</h1>')


def people(request):
    return HttpResponse('<ul>'
                        '<li><a href="/">Главная</a></li>'
                        '<li><a href="/news">новости</a></li>'
                        '<li><a href="/management">Руководство</a></li>'
                        '<li><a href="/facts">Факты</a></li>'
                        '<li><a href="/contacts">Контакты</a></li>'
                        '<li><a href="/history">Истроия</a></li>'
                        '</ul>'
                        '<h1>Какие-то люди</h1>')


def photos(request):
    return HttpResponse('<ul>'
                        '<li><a href="/">Главная</a></li>'
                        '<li><a href="/news">новости</a></li>'
                        '<li><a href="/management">Руководство</a></li>'
                        '<li><a href="/facts">Факты</a></li>'
                        '<li><a href="/contacts">Контакты</a></li>'
                        '<li><a href="/history">Истроия</a></li>'
                        '</ul>'
                        '<h1>Какие-то фотографии</h1>')


