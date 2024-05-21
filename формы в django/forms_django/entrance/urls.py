from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index),
    path('numbers', views.numbers),
    path('registration', views.registration),
    path('programmer', views.date_programmer)
]
