"""
URL configuration for bookarchivemain project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from bookapp.views import *
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main, name='main'),
    path('limited_events/', events, name = 'events'),
    path('katalog/', katalog, name='katalogurl'),
    path('newbooks/', newbooks, name='newsbooks'),
    path('books/', books, name='books'),
    path('books/<int:book_id>', booksinside, name='insidebook'),
    path('createglava/',create_glava,name='createglava'),
    path('registration/', registration, name='reg'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('lk/', lk, name='lk')
]
