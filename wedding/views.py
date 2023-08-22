from django.shortcuts import render, redirect, get_object_or_404
from.models import wedding
from .forms import WeddingForm


def main_page(request):
    main_pages = wedding.objects.all()
    return render(request, "main_page.html", {"main_pages": main_pages} )

def about_page(request):
    main_pages = wedding.objects.all()
    return render(request, "about_page.html", {"about_page": main_pages} )

def reservation_page(request):
    main_pages = wedding.objects.all()
    return render(request, "reservation_page.html", {"about_page": main_pages})


def Nonhyeon_page(request):
    main_pages = wedding.objects.all()
    return render(request, "Nonhyeon_page.html", { "Nonhyeon_page": main_pages} )

def Samsung_page(request):
    main_pages = wedding.objects.all()
    return render(request, "Samsung_page.html", { "samsung_page": main_pages} )