from django.contrib import admin
from . import views
from django.urls import path, include, re_path

urlpatterns = [
    path('', views.index),
   # re_path('^writers', views.req),
    re_path('^writers/Hemingway/The_Old_Man_and_the_Sea', views.old_man),
    re_path('^writers/Hemingway/The_Sun_Also_Rises', views.sun),
    re_path('^writers/Hemingway', views.hemingway),
    re_path('^writers/Shakespeare', views.shakespeare),
    re_path('^writers', views.writers),
    re_path('books/<int:bookid>', views.top),
    re_path('^books', views.books)
]
