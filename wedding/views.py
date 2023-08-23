from django.shortcuts import render, redirect, get_object_or_404
from.models import wedding
from .forms import WeddingForm
from django.core.mail import EmailMessage


def main_page(request):
    main_pages = wedding.objects.all()
    return render(request, "main_page.html", {"main_pages": main_pages} )

def about_page(request):
    main_pages = wedding.objects.all()
    return render(request, "about_page.html", {"about_page": main_pages} )

def reservation_page(request):
    if request.method == "POST":
        form = WeddingForm(request.POST)
        email = EmailMessage(
            f"{request.POST.get('writer', '고객님')}의 예약 요청",  # 이메일 제목
            f"""{request.POST.get("writer", "익명의 고객님")}님이 주신 예약 요청 건 
내용 : {request.POST.get("content", "예약 내용")} 
연락처 : {request.POST.get("tel", "연락처 미공개")}""",  #이메일 내용
            to=['starhochoitest@gmail.com'],  # 받는 이메일
        )
        email.send()
        return redirect("wedding_urls")
    else:
        form = WeddingForm()
        return render(request, "reservation_page.html", {"form": form})


def Nonhyeon_page(request):
    main_pages = wedding.objects.all()
    return render(request, "Nonhyeon_page.html", { "Nonhyeon_page": main_pages} )

def Samsung_page(request):
    main_pages = wedding.objects.all()
    return render(request, "Samsung_page.html", { "samsung_page": main_pages} )


