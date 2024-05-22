from django.contrib import admin
from . import views
from django.urls import path, re_path


urlpatterns = [
    path('', views.index),
    re_path('^news', views.news),
    re_path('^management', views.management),
    re_path('^facts', views.facts),
    re_path('^contacts', views.contacts),
    re_path('^history/people', views.people), # на историю
    re_path('^history/photos', views.photos), # на историю
    re_path('^history', views.history)
]
