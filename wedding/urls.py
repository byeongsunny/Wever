from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="wedding_urls"),
    path("about/", views.about_page, name="about_page"),
    path("res/", views.reservation_page, name="reservation_page"),
    path("non/", views.Nonhyeon_page, name="non_page"),
    path("sam/", views.Samsung_page, name="sam_page"),
    path("chu/", views.Samsung_page, name="chu_page"),
    path("sin/", views.Samsung_page, name="sin_page"),
]