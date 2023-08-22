"""
URL configuration for Wedding_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from wedding import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.main_page, name="main_page"),
    path("about", views.about_page, name="about_page"),
    path("res", views.reservation_page, name="reservation_page"),
    path("non", views.Nonhyeon_page, name="non_page"),
    path("sam", views.Samsung_page, name="sam_page"),
    path("sin", views.Sinsa_page, name="sin_page"),
    path("chu", views.Chungdam_page, name="chu_page"),
]
