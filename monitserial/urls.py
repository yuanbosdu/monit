# -*- coding: utf-8 -*-

from django.urls import path
from .views import serial_push, serial_change

urlpatterns = [
    path('push/', serial_push, name='serial_push'),
    path('change/', serial_change, name='serial_change')
]
