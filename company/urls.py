# -*- coding: utf-8 -*-
from django.urls import path
from .views import user_permission_api


urlpatterns = [
    path('permission', user_permission_api),
]
