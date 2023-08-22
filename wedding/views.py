from django.shortcuts import render, redirect, get_object_or_404
from.models import wedding

def main_page(request):
    main_page = wedding.objects.all()
    return render(request, "main_page.html", { "main_page": main_page} )

def Nonhyeon_page(request):
    main_page = wedding.objects.all()
    return render(request, "Nonhyeon_page.html", { "Nonhyeon_page": Nonhyeon_page} )