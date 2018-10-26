# -*- coding: utf-8 -*-

from django.urls import path
from .views import serial_push, serial_change, serial_get

urlpatterns = [
    path('push/', serial_push, name='serial_push'),
    path('change/', serial_change, name='serial_change'),
    path('get/', serial_get, name='serial_get'),
]
