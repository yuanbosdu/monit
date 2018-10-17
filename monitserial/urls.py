# -*- coding: utf-8 -*-

from django.urls import path
from .views import serial_push

urlpatterns = [
    path('push/', serial_push, name='serial_push')
]
