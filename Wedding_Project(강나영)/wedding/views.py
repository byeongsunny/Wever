from django.shortcuts import render, redirect, get_object_or_404
from.models import Wedding

def main_page(request):
    main_page = Wedding.objects.all()
    return render(request, "wedding/main_page.html", { "main_page": main_page} )

def Nonhyeon_page(request):
    Nonhyeon_page = Wedding.objects.all()
    return render(request, "wedding/Nonhyeon_page.html", {"Nonhyeon_page": Nonhyeon_page} )