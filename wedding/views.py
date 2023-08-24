from django.shortcuts import render, redirect, get_object_or_404
from.models import wedding,CheongdamDong,Gangnam,NonhyeonDong,SamsungDong,SinsaDong
from .forms import WeddingForm
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, PageNotAnInteger

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

    # GET 방식으로 정보를 받아오는 데이터
    # request.GET으로 들어온 값 중 'page'라는 명으로 들어온 값을 가져오겠다.
    page = request.GET.get("page")
    # Paginator(분할될 객체(queryset), 페이지 당 담길 객체)
    paginator = Paginator(nonhyeon, 20)

    #페이지를 입력하지 않고, 그냥 접속하면 PageNotAnInteger at이라는 에러가 발생한다.
    #paginator.page(page) 메소드에서 page에 숫자가 들어오길 기다리는데
    #아무값도 들어오지 않으니 발생하는 에러이다
    # 이를 해결하기 위해 아무것도 안들어올 경우는 그냥 1페이지로 인식하도록 코드를 만들었다.
    try:
        # paginator 객체를 .page라는 메소드를 통해 page_obj를 만든다.
        nonhyeon_page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        nonhyeon_page_obj = paginator.page(page)

    return render(request, "Nonhyeon_page.html",
                  { "nonhyeon": nonhyeon,
                            "nonhyeon_page_obj": nonhyeon_page_obj,})




# class Nonhyeon_page(ListView):
#     model = NonhyeonDong
#     template_name = "Nonhyeon_page.html"
#     paginate_by = 25



def Samsung_page(request):
    samsung = SamsungDong.objects.all()
    # GET 방식으로 정보를 받아오는 데이터
    samsung_page = request.GET.get("page")
    # Paginator(분할될 객체, 페이지 당 담길 객체)
    paginator = Paginator(samsung, 20)

    try:
        # paginator.get_page() 메서드를 사용하여 해당 페이지의 데이터를 가져옵니다.
        samsung_page_obj = paginator.page(samsung_page)
    except PageNotAnInteger:
        samsung_page = 1
        samsung_page_obj = paginator.page(samsung_page)
    return render(request, "Samsung_page.html",
                  { "samsung": samsung,
                            "samsung_page_obj": samsung_page_obj, })


def Chungdam_page(request):
    chungdam = CheongdamDong.objects.all()
    # GET 방식으로 정보를 받아오는 데이터
    chungdam_page = request.GET.get("page")
    # Paginator(분할될 객체, 페이지 당 담길 객체)
    paginator = Paginator(chungdam, 20)

    try:
        # paginator.get_page() 메서드를 사용하여 해당 페이지의 데이터를 가져옵니다.
        chungdam_page_obj= paginator.page(chungdam_page)
    except PageNotAnInteger:
        chungdam_page = 1
        chungdam_page_obj = paginator.get_page(chungdam_page)

    return render(request, "Chungdam_page.html",
                      { "chungdam": chungdam,
                                "chungdam_page_obj": chungdam_page_obj, })

def Sinsa_page(request):
    sinsa = SinsaDong.objects.all()
    # GET 방식으로 정보를 받아오는 데이터
    sinsa_page= request.GET.get("page")
    # Paginator(분할될 객체, 페이지 당 담길 객체)
    paginator = Paginator(sinsa , 20)

    try:
        # paginator.get_page() 메서드를 사용하여 해당 페이지의 데이터를 가져옵니다.
        sinsa_page_obj = paginator.page(sinsa_page)
    except PageNotAnInteger:
        sinsa_page = 1
        # paginator.get_page() 메서드를 사용하여 해당 페이지의 데이터를 가져옵니다.
        sinsa_page_obj = paginator.get_page(sinsa_page)
    return render(request, "Sinsa_page.html",
                  { "sinsa": sinsa,
                            "sinsa_page_obj": sinsa_page_obj, })

