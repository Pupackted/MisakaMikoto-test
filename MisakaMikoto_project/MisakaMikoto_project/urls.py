"""
URL configuration for MisakaMikoto_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

# notes: url is changed to re_path

from django.contrib import admin
from django.urls import path
from django.urls import path, re_path, include  # Import re_path for regex routes
from django.conf.urls import include
from MisakaMikotoApp1 import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),  # Use re_path instead of url
    re_path(r'^Misaka_Mikoto/', include('MisakaMikotoApp1.urls')),
    path("form_page/", views.form_name_view, name="form_name"),
    path("TheAdrian/", views.user_form_view, name="TheAdrian"),
    path("registeration/", views.register, name="register"),
    path(r'^logout/$', views.user_logout, name='logout'),
    # path(r'special/', views.special, name='special'),
    path("admin/", admin.site.urls),
]