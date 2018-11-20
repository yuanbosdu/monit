"""moint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.urls import include
from homepage import views
from company import views as cviews
urlpatterns = [
    re_path('^$', include('homepage.urls')),
    path('index/', include('homepage.urls')),
    path('serial/', include('monitserial.urls')),
    path('rabbitmq/', include('rabbitmq.urls')),
    path('admin/', admin.site.urls),

    path('user/index/', views.user_index, name='user_index'),
    path('user/signin/', views.user_signin, name='user_signin'),
    path('user/signout/', views.user_signout, name='user_signout'),
    path('user/signup/', views.user_signup, name='user_signup'),
    path('user/device/list', cviews.device_list_view, name='device_list'),
    path('user/device/add', cviews.device_add_view, name='device_add'),
]
