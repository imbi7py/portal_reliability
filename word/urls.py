from django.contrib import admin
from django.urls import path
from . import views
# from .views import *

app_name = 'word'

urlpatterns = [
    path('', views.index, name='index'),
]