from django.contrib import admin
from . import views
from django.urls import path, include, re_path

urlpatterns = [
    re_path('^', views.index, name='home'),
]