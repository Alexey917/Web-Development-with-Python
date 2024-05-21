from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index),
    path('fr', views.french),
    path('de', views.german),
    path('es', views.spanish)
]
