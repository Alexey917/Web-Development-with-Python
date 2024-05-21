from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='home'),
    path('toyota', views.toyota, name='toyota'),
    path('honda', views.honda, name='honda'),
    path('renault', views.renault, name='renault')
]
