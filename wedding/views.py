from django.shortcuts import render, redirect, get_object_or_404
from.models import wedding,CheongdamDong,Gangnam,NonhyeonDong,SamsungDong,SinsaDong
from .forms import WeddingForm
from django.core.mail import EmailMessage
from django.core.paginator import  Paginator

def main_page(request):
    main_pages = Gangnam.objects.all()
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
    nonhyeon = NonhyeonDong.objects.all()
    return render(request, "Nonhyeon_page.html", { "nonhyeon": nonhyeon} )
    page = request.GET.get("page")



def Samsung_page(request):
    samsung_page = SamsungDong.objects.all()
    return render(request, "Samsung_page.html", { "samsung": samsung_page} )

def Chungdam_page(request):
    chungdam = CheongdamDong.objects.all()
    return render(request, "Chungdam_page.html", { "chungdam": chungdam} )

def Sinsa_page(request):
    sinsa = SinsaDong.objects.all()
    return render(request, "Sinsa_page.html", { "sinsa": sinsa} )

