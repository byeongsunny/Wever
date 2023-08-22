from django.shortcuts import render, redirect, get_object_or_404
from.models import wedding

def main_page(request):
    main_page = wedding.objects.all()
    return render(request, "main_page.html", { "main_page": main_page} )

def about_page(request):
    main_page = wedding.objects.all()
    return render(request, "about_page.html", { "about_page": about_page} )

def reservation_page(request):
    main_page = wedding.objects.all()
    return render(request, "reservation_page.html", { "reservation_page": reservation_page} )

def Nonhyeon_page(request):
    main_page = wedding.objects.all()
    return render(request, "Nonhyeon_page.html", { "Nonhyeon_page": Nonhyeon_page} )

def Samsung_page(request):
    main_page = wedding.objects.all()
    return render(request, "Samsung_page.html", { "samsung_page": Samsung_page} )

def Sinsa_page(request):
    main_page = wedding.objects.all()
    return render(request, "Sinsa_page.html", { "sinsa_page": Sinsa_page} )

def Chungdam_page(request):
    main_page = wedding.objects.all()
    return render(request, "Chungdam_page.html", { "chungdam_page": Chungdam_page} )